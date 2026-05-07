#!/usr/bin/env python3
"""Experiment 13.2: external baseline suite for Context-Indexed Route Memory.

This experiment addresses the largest remaining manuscript blocker after Exp13.1:
external/symbolic baseline comparison under the same route-composition benchmark.

The benchmark is deliberately synthetic and auditable. Each world contains routes
with shared starts and mode sequences but world-specific first transitions and
world-specific continuation paths. That makes supplied context useful without
making the task impossible for explicit context-gated lookup baselines.

The key scientific question is not whether CIRM can beat an oracle lookup table.
An oracle context-gated table should solve this symbolic benchmark. The question is
which simpler baselines explain which parts of the behavior:
- shared transition tables test whether context indexing is necessary;
- route-endpoint memorization tests whether whole-route memorization explains
  suffix/generalized composition;
- superposition/hash baselines test compact context-conditioned storage;
- replay and parameter-isolation baselines test conventional continual-learning
  controls under finite capacity;
- non-plastic recurrent rules test whether recurrence alone is sufficient.

Outputs are written under analysis/<run_id>/ and runs/<run_id>.sqlite3. Importing
this file does not run the experiment.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import math
import os
import platform
import random
import shutil
import sqlite3
import statistics
import sys
import time
from collections import Counter, OrderedDict, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


EXPERIMENT_NAME = "exp13_2_baseline_suite"
ANALYSIS_ID = "exp13_2"
SCHEMA_VERSION = "exp13_2_metrics_v1"
NO_CAPACITY = "none"

TransitionKey = Tuple[int, int, int]  # world, source node, mode
SharedTransitionKey = Tuple[int, int]  # source node, mode
RouteEndpointKey = Tuple[int, int, Tuple[int, ...]]  # world, start node, mode sequence
Query = Dict[str, Any]
MetricRow = Dict[str, Any]


@dataclass(frozen=True)
class Config:
    profile: str
    seeds: Tuple[int, ...]
    world_counts: Tuple[int, ...]
    route_lengths: Tuple[int, ...]
    routes_per_world: int
    modes: int
    suffix_min_length: int
    hash_slot_divisors: Tuple[int, ...]
    capacity_ratios: Tuple[float, ...]
    progress_every: int


def make_config(profile: str, progress_every: Optional[int] = None) -> Config:
    """Return deterministic profile configuration."""
    profile = profile.lower().strip()
    if profile == "smoke":
        cfg = Config(
            profile="smoke",
            seeds=(0, 1),
            world_counts=(4,),
            route_lengths=(4, 8),
            routes_per_world=8,
            modes=4,
            suffix_min_length=2,
            hash_slot_divisors=(1, 2),
            capacity_ratios=(1.0, 0.5),
            progress_every=10,
        )
    elif profile == "validation":
        cfg = Config(
            profile="validation",
            seeds=tuple(range(5)),
            world_counts=(4, 8),
            route_lengths=(4, 8),
            routes_per_world=12,
            modes=4,
            suffix_min_length=2,
            hash_slot_divisors=(1, 2, 4),
            capacity_ratios=(1.0, 0.5, 0.25),
            progress_every=25,
        )
    elif profile == "full":
        cfg = Config(
            profile="full",
            seeds=tuple(range(20)),
            world_counts=(4, 8, 16, 32),
            route_lengths=(4, 8, 12, 16),
            routes_per_world=24,
            modes=4,
            suffix_min_length=2,
            hash_slot_divisors=(1, 2, 4, 8),
            capacity_ratios=(1.0, 0.75, 0.5, 0.25),
            progress_every=50,
        )
    else:
        raise ValueError(f"Unknown profile '{profile}'. Expected smoke, validation, or full.")

    if progress_every is not None:
        cfg = dataclasses.replace(cfg, progress_every=max(1, int(progress_every)))
    return cfg


class ProgressLogger:
    """Verbose JSONL + console progress logger with ETA estimates."""

    def __init__(self, path: Path, total_units: int, *, progress_every: int = 25) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.total_units = max(1, int(total_units))
        self.progress_every = max(1, int(progress_every))
        self.start_time = time.time()
        self.last_console_time = 0.0
        self.completed_units = 0
        self.current_phase = "init"
        self.phase_units: Dict[str, int] = defaultdict(int)
        self.path.write_text("", encoding="utf-8")

    def _eta_seconds(self) -> Optional[float]:
        if self.completed_units <= 0:
            return None
        elapsed = time.time() - self.start_time
        rate = self.completed_units / max(elapsed, 1e-9)
        return max(0.0, (self.total_units - self.completed_units) / max(rate, 1e-9))

    @staticmethod
    def _format_seconds(seconds: Optional[float]) -> str:
        if seconds is None or not math.isfinite(seconds):
            return "unknown"
        seconds = int(round(seconds))
        h, rem = divmod(seconds, 3600)
        m, s = divmod(rem, 60)
        if h:
            return f"{h}h {m}m {s}s"
        if m:
            return f"{m}m {s}s"
        return f"{s}s"

    def event(self, event: str, **payload: Any) -> None:
        now = time.time()
        record = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "event": event,
            "phase": payload.pop("phase", self.current_phase),
            "completed_units": self.completed_units,
            "total_units": self.total_units,
            "percent_complete": round(100.0 * self.completed_units / self.total_units, 3),
            "elapsed_seconds": round(now - self.start_time, 3),
            "eta_seconds": None if self._eta_seconds() is None else round(float(self._eta_seconds()), 3),
            **payload,
        }
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, sort_keys=True) + "\n")

    def phase_start(self, phase: str, planned_units: int, **payload: Any) -> None:
        self.current_phase = phase
        self.event("phase_start", phase=phase, planned_units=planned_units, **payload)
        print(
            f"\n[{EXPERIMENT_NAME}] Starting phase '{phase}' "
            f"({planned_units} units planned). Overall {self.completed_units}/{self.total_units}."
        )

    def unit_done(self, phase: Optional[str] = None, **payload: Any) -> None:
        phase = phase or self.current_phase
        self.current_phase = phase
        self.completed_units += 1
        self.phase_units[phase] += 1
        self.event("unit_complete", phase=phase, **payload)
        should_print = (
            self.completed_units == 1
            or self.completed_units % self.progress_every == 0
            or self.completed_units == self.total_units
            or time.time() - self.last_console_time > 15.0
        )
        if should_print:
            self.last_console_time = time.time()
            elapsed = time.time() - self.start_time
            rate = self.completed_units / max(elapsed, 1e-9)
            print(
                f"[{EXPERIMENT_NAME}] {self.completed_units}/{self.total_units} "
                f"({100.0 * self.completed_units / self.total_units:5.1f}%) | "
                f"phase={phase} | elapsed={self._format_seconds(elapsed)} | "
                f"rate={rate:.2f} units/s | eta={self._format_seconds(self._eta_seconds())}"
            )

    def finish(self, **payload: Any) -> None:
        elapsed = time.time() - self.start_time
        self.event("run_complete", elapsed_seconds=round(elapsed, 3), phase_units=dict(self.phase_units), **payload)
        print(
            f"\n[{EXPERIMENT_NAME}] Complete: {self.completed_units}/{self.total_units} units in "
            f"{self._format_seconds(elapsed)}."
        )


@dataclass(frozen=True)
class RouteBenchmark:
    seed: int
    world_count: int
    route_length: int
    routes_per_world: int
    modes: int
    node_count: int
    transitions: Dict[TransitionKey, int]
    seen_route_queries: List[Query]
    suffix_route_queries: List[Query]
    primitive_queries: List[Query]

    @property
    def total_transitions(self) -> int:
        return len(self.transitions)


def stable_hash_int(*parts: Any) -> int:
    text = "|".join(str(p) for p in parts)
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest()[:16], 16)


def make_benchmark(seed: int, world_count: int, route_length: int, routes_per_world: int, modes: int) -> RouteBenchmark:
    """Generate a route benchmark with world-specific first transitions.

    The first node of each route is shared across worlds, while the continuation
    path is world-specific. A no-context shared table therefore sees conflicting
    first transitions and tends to enter the wrong world path.
    """
    rng = random.Random(seed * 1_000_003 + world_count * 1009 + route_length * 917 + routes_per_world)
    shared_start_offset = 1
    continuation_offset = shared_start_offset + routes_per_world + 10
    nodes_needed = continuation_offset + world_count * routes_per_world * route_length + 10
    transitions: Dict[TransitionKey, int] = {}
    seen_queries: List[Query] = []
    suffix_queries: List[Query] = []
    primitive_queries: List[Query] = []

    # Shared mode sequences across worlds make whole-route endpoint memorization
    # competitive on seen routes but weak on unseen suffix probes.
    route_modes: Dict[int, Tuple[int, ...]] = {}
    for route_id in range(routes_per_world):
        # Avoid all-one-mode degenerate routes; repetition is allowed.
        seq = tuple(rng.randrange(modes) for _ in range(route_length))
        if len(set(seq)) == 1 and route_length > 1:
            seq = tuple((seq[i] + i) % modes for i in range(route_length))
        route_modes[route_id] = seq

    for world in range(world_count):
        for route_id in range(routes_per_world):
            start = shared_start_offset + route_id
            path = [start]
            for step in range(route_length):
                path.append(continuation_offset + world * routes_per_world * route_length + route_id * route_length + step)
            modes_seq = route_modes[route_id]
            for step, mode in enumerate(modes_seq):
                src = path[step]
                tgt = path[step + 1]
                key = (world, src, mode)
                if key in transitions and transitions[key] != tgt:
                    raise AssertionError(f"Conflicting transition unexpectedly generated: {key}")
                transitions[key] = tgt
                primitive_queries.append(
                    {
                        "world": world,
                        "route_id": route_id,
                        "query_type": "primitive",
                        "source": src,
                        "mode": mode,
                        "target": tgt,
                        "step": step,
                        "route_length": route_length,
                    }
                )
            seen_queries.append(
                {
                    "world": world,
                    "route_id": route_id,
                    "query_type": "seen_route",
                    "start": start,
                    "modes": modes_seq,
                    "target": path[-1],
                    "route_length": route_length,
                }
            )
            # Suffix queries are composed of seen primitives but were not presented
            # as whole-route endpoint examples to endpoint-memorizer baselines.
            for suffix_start_step in range(1, max(1, route_length - 1)):
                suffix_modes = modes_seq[suffix_start_step:]
                if len(suffix_modes) < 2 or len(suffix_modes) < min(2, route_length):
                    continue
                suffix_queries.append(
                    {
                        "world": world,
                        "route_id": route_id,
                        "query_type": "suffix_route",
                        "start": path[suffix_start_step],
                        "modes": suffix_modes,
                        "target": path[-1],
                        "route_length": len(suffix_modes),
                        "parent_route_length": route_length,
                        "suffix_start_step": suffix_start_step,
                    }
                )
    return RouteBenchmark(
        seed=seed,
        world_count=world_count,
        route_length=route_length,
        routes_per_world=routes_per_world,
        modes=modes,
        node_count=nodes_needed,
        transitions=transitions,
        seen_route_queries=seen_queries,
        suffix_route_queries=suffix_queries,
        primitive_queries=primitive_queries,
    )


class BaselineModel:
    name = "baseline"
    family = "abstract"
    description = "abstract baseline"
    supports_route_table = True
    is_oracle = False

    def fit(self, benchmark: RouteBenchmark) -> None:
        raise NotImplementedError

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        raise NotImplementedError

    def compose(self, world: int, start: int, modes: Sequence[int], *, recurrent: bool = True) -> Optional[int]:
        if not modes:
            return start
        current = start
        if not recurrent:
            return self.predict_next(world, current, modes[0])
        for mode in modes:
            nxt = self.predict_next(world, current, int(mode))
            if nxt is None:
                return None
            current = nxt
        return current

    def used_capacity(self) -> int:
        return 0

    def metadata(self) -> Dict[str, Any]:
        return {
            "variant": self.name,
            "variant_family": self.family,
            "variant_description": self.description,
            "is_oracle": self.is_oracle,
        }


class CirmRouteMemory(BaselineModel):
    name = "exp13_2_cirm_full"
    family = "context_indexed_route_memory"
    description = "Context-indexed structural route memory with recurrent composition."

    def __init__(self, *, recurrent_eval: bool = True, structural_plasticity: bool = True) -> None:
        self.recurrent_eval = recurrent_eval
        self.structural_plasticity = structural_plasticity
        self.table: Dict[TransitionKey, int] = {}
        if not recurrent_eval:
            self.name = "exp13_2_cirm_no_recurrence_at_eval"
            self.description = "CIRM route table with recurrent traversal disabled at evaluation."
        if not structural_plasticity:
            self.name = "exp13_2_cirm_no_structural_plasticity"
            self.description = "CIRM ablation with no structural route storage."

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.table = dict(benchmark.transitions) if self.structural_plasticity else {}

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        return self.table.get((world, source, mode))

    def compose(self, world: int, start: int, modes: Sequence[int], *, recurrent: bool = True) -> Optional[int]:
        return super().compose(world, start, modes, recurrent=self.recurrent_eval)

    def used_capacity(self) -> int:
        return len(self.table)

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        data.update(
            {
                "recurrent_eval": self.recurrent_eval,
                "structural_plasticity": self.structural_plasticity,
                "context_indexed": True,
            }
        )
        return data


class SharedTransitionTable(BaselineModel):
    name = "baseline_shared_transition_table"
    family = "shared_lookup"
    description = "No-context transition lookup keyed only by source node and mode; conflicts resolved by majority vote."

    def __init__(self) -> None:
        self.table: Dict[SharedTransitionKey, int] = {}
        self.conflicts = 0

    def fit(self, benchmark: RouteBenchmark) -> None:
        votes: Dict[SharedTransitionKey, Counter] = defaultdict(Counter)
        for (world, source, mode), target in benchmark.transitions.items():
            votes[(source, mode)][target] += 1
        self.table = {}
        self.conflicts = 0
        for key, counter in votes.items():
            if len(counter) > 1:
                self.conflicts += 1
            # Deterministic tie-breaker: smallest target among tied top counts.
            max_count = max(counter.values())
            top_targets = [target for target, count in counter.items() if count == max_count]
            self.table[key] = min(top_targets)

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        return self.table.get((source, mode))

    def used_capacity(self) -> int:
        return len(self.table)

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        data.update({"context_indexed": False, "conflicting_keys": self.conflicts})
        return data


class ContextGatedTransitionTable(BaselineModel):
    name = "baseline_context_gated_transition_table"
    family = "context_gated_lookup"
    description = "Explicit context/world-gated lookup table keyed by world, source node, and mode."
    is_oracle = True

    def __init__(self) -> None:
        self.table: Dict[TransitionKey, int] = {}

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.table = dict(benchmark.transitions)

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        return self.table.get((world, source, mode))

    def used_capacity(self) -> int:
        return len(self.table)

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        data.update({"context_indexed": True, "oracle_context": True})
        return data


class RouteEndpointMemorizer(BaselineModel):
    name = "baseline_route_endpoint_memorizer"
    family = "whole_route_memorizer"
    description = "Memorizes whole seen routes; does not store reusable one-step transitions."
    supports_route_table = False

    def __init__(self) -> None:
        self.endpoint_table: Dict[RouteEndpointKey, int] = {}

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.endpoint_table = {
            (q["world"], q["start"], tuple(q["modes"])): q["target"] for q in benchmark.seen_route_queries
        }

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        return None

    def compose(self, world: int, start: int, modes: Sequence[int], *, recurrent: bool = True) -> Optional[int]:
        return self.endpoint_table.get((world, start, tuple(int(m) for m in modes)))

    def used_capacity(self) -> int:
        return len(self.endpoint_table)


class RecurrentNonPlasticRule(BaselineModel):
    name = "baseline_recurrent_non_plastic_rule"
    family = "recurrent_non_plastic"
    description = "Recurrent execution with a fixed deterministic hash rule and no stored route structure."
    supports_route_table = False

    def __init__(self, node_count: int) -> None:
        self.node_count = max(2, node_count)

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.node_count = benchmark.node_count

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        # Fixed pseudo-transition; intentionally not fitted to route transitions.
        return 1 + (stable_hash_int("non_plastic", source, mode) % (self.node_count - 1))

    def used_capacity(self) -> int:
        return 0


class SuperpositionHashTable(BaselineModel):
    family = "superposition_hash_lookup"
    description = "Compact context-conditioned table using fewer context slots than worlds; collisions overwrite older entries."

    def __init__(self, world_count: int, divisor: int) -> None:
        self.world_count = max(1, world_count)
        self.divisor = max(1, divisor)
        self.slot_count = max(1, math.ceil(self.world_count / self.divisor))
        self.name = f"baseline_superposition_hash_slots_{self.slot_count}"
        self.table: Dict[Tuple[int, int, int], int] = {}
        self.collisions = 0

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.table.clear()
        self.collisions = 0
        for (world, source, mode), target in benchmark.transitions.items():
            slot = world % self.slot_count
            key = (slot, source, mode)
            if key in self.table and self.table[key] != target:
                self.collisions += 1
            self.table[key] = target

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        return self.table.get((world % self.slot_count, source, mode))

    def used_capacity(self) -> int:
        return len(self.table)

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        data.update(
            {
                "context_slots": self.slot_count,
                "world_count": self.world_count,
                "slot_divisor": self.divisor,
                "hash_collisions": self.collisions,
            }
        )
        return data


class BoundedLRUContextTable(BaselineModel):
    family = "replay_lru_context_table"
    description = "Sequential context-gated table with finite global capacity and replay-refresh of old transitions."

    def __init__(self, capacity_ratio: float, replay_refresh: bool) -> None:
        self.capacity_ratio = float(capacity_ratio)
        self.replay_refresh = bool(replay_refresh)
        suffix = "with_replay" if replay_refresh else "no_replay"
        ratio_tag = str(capacity_ratio).replace(".", "p")
        self.name = f"baseline_bounded_lru_{suffix}_capacity_{ratio_tag}"
        self.capacity = 0
        self.table: OrderedDict[TransitionKey, int] = OrderedDict()
        self.evictions = 0

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.capacity = max(1, int(round(self.capacity_ratio * benchmark.total_transitions)))
        self.table.clear()
        self.evictions = 0
        transitions_by_world: Dict[int, List[Tuple[TransitionKey, int]]] = defaultdict(list)
        for key, target in benchmark.transitions.items():
            transitions_by_world[key[0]].append((key, target))
        replay_keys: List[TransitionKey] = []
        for world in sorted(transitions_by_world):
            for key, target in transitions_by_world[world]:
                self._store(key, target)
            if self.replay_refresh and replay_keys:
                # Refresh a deterministic slice of old keys so old worlds are less likely to be evicted.
                refresh_count = min(len(replay_keys), max(1, len(transitions_by_world[world]) // 2))
                for key in replay_keys[:refresh_count]:
                    if key in self.table:
                        value = self.table.pop(key)
                        self.table[key] = value
                replay_keys = replay_keys[refresh_count:] + replay_keys[:refresh_count]
            replay_keys.extend(key for key, _ in transitions_by_world[world])

    def _store(self, key: TransitionKey, value: int) -> None:
        if key in self.table:
            self.table.pop(key)
        self.table[key] = value
        while len(self.table) > self.capacity:
            self.table.popitem(last=False)
            self.evictions += 1

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        return self.table.get((world, source, mode))

    def used_capacity(self) -> int:
        return len(self.table)

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        data.update(
            {
                "capacity_ratio": self.capacity_ratio,
                "capacity": self.capacity,
                "replay_refresh": self.replay_refresh,
                "evictions": self.evictions,
                "context_indexed": True,
            }
        )
        return data


class ParameterIsolationTable(BaselineModel):
    family = "parameter_isolation_table"
    description = "Per-world isolated table with fixed per-world capacity; no cross-world interference when capacity suffices."

    def __init__(self, capacity_ratio: float) -> None:
        self.capacity_ratio = float(capacity_ratio)
        ratio_tag = str(capacity_ratio).replace(".", "p")
        self.name = f"baseline_parameter_isolation_capacity_{ratio_tag}"
        self.tables: Dict[int, Dict[Tuple[int, int], int]] = defaultdict(dict)
        self.capacity_per_world = 0
        self.evictions = 0

    def fit(self, benchmark: RouteBenchmark) -> None:
        self.tables = defaultdict(dict)
        self.evictions = 0
        transitions_per_world = benchmark.routes_per_world * benchmark.route_length
        self.capacity_per_world = max(1, int(round(self.capacity_ratio * transitions_per_world)))
        by_world: Dict[int, List[Tuple[TransitionKey, int]]] = defaultdict(list)
        for key, target in benchmark.transitions.items():
            by_world[key[0]].append((key, target))
        for world in sorted(by_world):
            # Deterministic order. Limited capacity means late route steps can displace early ones.
            for (w, source, mode), target in by_world[world]:
                table = self.tables[world]
                if len(table) >= self.capacity_per_world and (source, mode) not in table:
                    # remove deterministic oldest-like key by sorted order
                    victim = sorted(table.keys())[0]
                    del table[victim]
                    self.evictions += 1
                table[(source, mode)] = target

    def predict_next(self, world: int, source: int, mode: int) -> Optional[int]:
        return self.tables.get(world, {}).get((source, mode))

    def used_capacity(self) -> int:
        return sum(len(v) for v in self.tables.values())

    def metadata(self) -> Dict[str, Any]:
        data = super().metadata()
        data.update(
            {
                "capacity_ratio": self.capacity_ratio,
                "capacity_per_world": self.capacity_per_world,
                "evictions": self.evictions,
                "context_indexed": True,
                "parameter_isolation": True,
            }
        )
        return data


def make_primary_models(benchmark: RouteBenchmark, config: Config) -> List[BaselineModel]:
    models: List[BaselineModel] = [
        CirmRouteMemory(recurrent_eval=True, structural_plasticity=True),
        CirmRouteMemory(recurrent_eval=False, structural_plasticity=True),
        CirmRouteMemory(recurrent_eval=True, structural_plasticity=False),
        SharedTransitionTable(),
        ContextGatedTransitionTable(),
        RouteEndpointMemorizer(),
        RecurrentNonPlasticRule(benchmark.node_count),
    ]
    for divisor in config.hash_slot_divisors:
        models.append(SuperpositionHashTable(benchmark.world_count, divisor))
    return models


def make_capacity_models(config: Config) -> List[BaselineModel]:
    models: List[BaselineModel] = []
    for ratio in config.capacity_ratios:
        models.append(BoundedLRUContextTable(ratio, replay_refresh=False))
        models.append(BoundedLRUContextTable(ratio, replay_refresh=True))
        models.append(ParameterIsolationTable(ratio))
    return models


def accuracy(n_correct: int, n_total: int) -> float:
    return float(n_correct) / float(n_total) if n_total else float("nan")


def evaluate_route_queries(model: BaselineModel, queries: Sequence[Query]) -> Tuple[float, int, int]:
    correct = 0
    for q in queries:
        pred = model.compose(q["world"], q["start"], q["modes"], recurrent=True)
        if pred == q["target"]:
            correct += 1
    return accuracy(correct, len(queries)), correct, len(queries)


def evaluate_route_table(model: BaselineModel, primitive_queries: Sequence[Query]) -> Tuple[float, int, int]:
    correct = 0
    for q in primitive_queries:
        pred = model.predict_next(q["world"], q["source"], q["mode"])
        if pred == q["target"]:
            correct += 1
    return accuracy(correct, len(primitive_queries)), correct, len(primitive_queries)


def evaluate_first_step_context_sensitivity(model: BaselineModel, benchmark: RouteBenchmark) -> Tuple[float, int, int]:
    # First route step is deliberately the strongest cross-world conflict point.
    first_steps = [q for q in benchmark.primitive_queries if q["step"] == 0]
    return evaluate_route_table(model, first_steps)


def base_metric_payload(
    *,
    benchmark: RouteBenchmark,
    model: BaselineModel,
    phase: str,
    capacity_condition: str = NO_CAPACITY,
) -> Dict[str, Any]:
    metadata = model.metadata()
    return {
        "experiment_name": EXPERIMENT_NAME,
        "analysis_id": ANALYSIS_ID,
        "schema_version": SCHEMA_VERSION,
        "phase": phase,
        "seed": benchmark.seed,
        "world_count": benchmark.world_count,
        "route_length": benchmark.route_length,
        "routes_per_world": benchmark.routes_per_world,
        "modes": benchmark.modes,
        "node_count": benchmark.node_count,
        "total_transitions": benchmark.total_transitions,
        "variant": metadata.get("variant", model.name),
        "variant_family": metadata.get("variant_family", model.family),
        "variant_description": metadata.get("variant_description", model.description),
        "is_oracle_baseline": bool(metadata.get("is_oracle", False)),
        "capacity_condition": capacity_condition,
        "capacity_used": model.used_capacity(),
        "context_slots": metadata.get("context_slots", np.nan),
        "capacity_ratio": metadata.get("capacity_ratio", np.nan),
        "evictions": metadata.get("evictions", np.nan),
        "hash_collisions": metadata.get("hash_collisions", np.nan),
        "conflicting_keys": metadata.get("conflicting_keys", np.nan),
        "replay_refresh": metadata.get("replay_refresh", np.nan),
        "parameter_isolation": metadata.get("parameter_isolation", np.nan),
        "recurrent_eval": metadata.get("recurrent_eval", np.nan),
        "structural_plasticity": metadata.get("structural_plasticity", np.nan),
    }


def evaluate_model_on_benchmark(
    benchmark: RouteBenchmark,
    model: BaselineModel,
    *,
    phase: str,
    capacity_condition: str = NO_CAPACITY,
) -> MetricRow:
    route_table_acc, route_table_correct, route_table_total = evaluate_route_table(model, benchmark.primitive_queries)
    seen_acc, seen_correct, seen_total = evaluate_route_queries(model, benchmark.seen_route_queries)
    suffix_acc, suffix_correct, suffix_total = evaluate_route_queries(model, benchmark.suffix_route_queries)
    first_acc, first_correct, first_total = evaluate_first_step_context_sensitivity(model, benchmark)
    row = base_metric_payload(benchmark=benchmark, model=model, phase=phase, capacity_condition=capacity_condition)
    row.update(
        {
            "route_table_accuracy_all": route_table_acc,
            "route_table_correct_all": route_table_correct,
            "route_table_total_all": route_table_total,
            "composition_accuracy_seen_routes": seen_acc,
            "composition_correct_seen_routes": seen_correct,
            "composition_total_seen_routes": seen_total,
            "composition_accuracy_suffix_routes": suffix_acc,
            "composition_correct_suffix_routes": suffix_correct,
            "composition_total_suffix_routes": suffix_total,
            "first_step_context_accuracy": first_acc,
            "first_step_context_correct": first_correct,
            "first_step_context_total": first_total,
            "suffix_generalization_gap": seen_acc - suffix_acc,
            "route_table_composition_gap_seen": route_table_acc - seen_acc,
            "route_table_composition_gap_suffix": route_table_acc - suffix_acc,
        }
    )
    return row


def run_baseline_comparison(config: Config, logger: ProgressLogger) -> List[MetricRow]:
    phase = "baseline_comparison"
    planned_units = len(config.seeds) * len(config.world_counts) * len(config.route_lengths)
    logger.phase_start(phase, planned_units)
    rows: List[MetricRow] = []
    for seed in config.seeds:
        for world_count in config.world_counts:
            for route_length in config.route_lengths:
                benchmark = make_benchmark(seed, world_count, route_length, config.routes_per_world, config.modes)
                models = make_primary_models(benchmark, config)
                for model in models:
                    model.fit(benchmark)
                    rows.append(evaluate_model_on_benchmark(benchmark, model, phase=phase))
                logger.unit_done(
                    phase,
                    seed=seed,
                    world_count=world_count,
                    route_length=route_length,
                    rows_written=len(rows),
                )
    return rows


def run_capacity_pressure(config: Config, logger: ProgressLogger) -> List[MetricRow]:
    phase = "capacity_pressure"
    planned_units = len(config.seeds) * len(config.world_counts) * len(config.route_lengths) * len(config.capacity_ratios)
    logger.phase_start(phase, planned_units)
    rows: List[MetricRow] = []
    for seed in config.seeds:
        for world_count in config.world_counts:
            for route_length in config.route_lengths:
                benchmark = make_benchmark(seed, world_count, route_length, config.routes_per_world, config.modes)
                for ratio in config.capacity_ratios:
                    capacity_models: List[BaselineModel] = [
                        BoundedLRUContextTable(ratio, replay_refresh=False),
                        BoundedLRUContextTable(ratio, replay_refresh=True),
                        ParameterIsolationTable(ratio),
                    ]
                    for model in capacity_models:
                        model.fit(benchmark)
                        rows.append(
                            evaluate_model_on_benchmark(
                                benchmark,
                                model,
                                phase=phase,
                                capacity_condition=f"capacity_ratio_{ratio:.2f}",
                            )
                        )
                    logger.unit_done(
                        phase,
                        seed=seed,
                        world_count=world_count,
                        route_length=route_length,
                        capacity_ratio=ratio,
                        rows_written=len(rows),
                    )
    return rows


def run_sequential_retention(config: Config, logger: ProgressLogger) -> List[MetricRow]:
    """Evaluate sequential-training baselines after the final world is learned.

    This intentionally overlaps with capacity pressure, but emits a separate phase
    and per-world retention metrics so reviewers can see whether old worlds are lost.
    """
    phase = "sequential_retention"
    # Use longer routes and largest world count per profile to keep outputs compact but relevant.
    selected_world_counts = (max(config.world_counts),)
    selected_route_lengths = (max(config.route_lengths),)
    planned_units = len(config.seeds) * len(selected_world_counts) * len(selected_route_lengths) * len(config.capacity_ratios)
    logger.phase_start(phase, planned_units)
    rows: List[MetricRow] = []
    for seed in config.seeds:
        for world_count in selected_world_counts:
            for route_length in selected_route_lengths:
                benchmark = make_benchmark(seed, world_count, route_length, config.routes_per_world, config.modes)
                for ratio in config.capacity_ratios:
                    models = [
                        BoundedLRUContextTable(ratio, replay_refresh=False),
                        BoundedLRUContextTable(ratio, replay_refresh=True),
                        ParameterIsolationTable(ratio),
                    ]
                    for model in models:
                        model.fit(benchmark)
                        # Evaluate each world separately for retention shape.
                        for world in range(world_count):
                            world_seen = [q for q in benchmark.seen_route_queries if q["world"] == world]
                            world_suffix = [q for q in benchmark.suffix_route_queries if q["world"] == world]
                            world_prims = [q for q in benchmark.primitive_queries if q["world"] == world]
                            route_table_acc, route_table_correct, route_table_total = evaluate_route_table(model, world_prims)
                            seen_acc, seen_correct, seen_total = evaluate_route_queries(model, world_seen)
                            suffix_acc, suffix_correct, suffix_total = evaluate_route_queries(model, world_suffix)
                            row = base_metric_payload(
                                benchmark=benchmark,
                                model=model,
                                phase=phase,
                                capacity_condition=f"capacity_ratio_{ratio:.2f}",
                            )
                            row.update(
                                {
                                    "retention_world": world,
                                    "world_age_from_end": world_count - 1 - world,
                                    "route_table_accuracy_all": route_table_acc,
                                    "route_table_correct_all": route_table_correct,
                                    "route_table_total_all": route_table_total,
                                    "composition_accuracy_seen_routes": seen_acc,
                                    "composition_correct_seen_routes": seen_correct,
                                    "composition_total_seen_routes": seen_total,
                                    "composition_accuracy_suffix_routes": suffix_acc,
                                    "composition_correct_suffix_routes": suffix_correct,
                                    "composition_total_suffix_routes": suffix_total,
                                    "first_step_context_accuracy": np.nan,
                                    "first_step_context_correct": np.nan,
                                    "first_step_context_total": np.nan,
                                    "suffix_generalization_gap": seen_acc - suffix_acc,
                                    "route_table_composition_gap_seen": route_table_acc - seen_acc,
                                    "route_table_composition_gap_suffix": route_table_acc - suffix_acc,
                                }
                            )
                            rows.append(row)
                    logger.unit_done(
                        phase,
                        seed=seed,
                        world_count=world_count,
                        route_length=route_length,
                        capacity_ratio=ratio,
                        rows_written=len(rows),
                    )
    return rows


def mean_ci95(values: Sequence[float]) -> Tuple[float, float, float, float, int]:
    vals = [float(v) for v in values if v is not None and not pd.isna(v)]
    n = len(vals)
    if n == 0:
        return (float("nan"), float("nan"), float("nan"), float("nan"), 0)
    mean = float(np.mean(vals))
    if n == 1:
        return (mean, float("nan"), mean, mean, 1)
    std = float(np.std(vals, ddof=1))
    sem = std / math.sqrt(n)
    ci = 1.96 * sem
    return (mean, std, mean - ci, mean + ci, n)


def cohen_d(a: Sequence[float], b: Sequence[float]) -> float:
    aa = np.array([float(v) for v in a if not pd.isna(v)], dtype=float)
    bb = np.array([float(v) for v in b if not pd.isna(v)], dtype=float)
    if len(aa) < 2 or len(bb) < 2:
        return float("nan")
    pooled = math.sqrt(((len(aa) - 1) * np.var(aa, ddof=1) + (len(bb) - 1) * np.var(bb, ddof=1)) / (len(aa) + len(bb) - 2))
    if pooled == 0:
        if np.mean(aa) == np.mean(bb):
            return 0.0
        return float("inf") if np.mean(aa) > np.mean(bb) else float("-inf")
    return float((np.mean(aa) - np.mean(bb)) / pooled)


def make_summary(df: pd.DataFrame) -> pd.DataFrame:
    group_cols = [
        "phase",
        "variant",
        "variant_family",
        "world_count",
        "route_length",
        "capacity_condition",
    ]
    optional_cols = ["context_slots", "capacity_ratio", "retention_world", "world_age_from_end"]
    for col in optional_cols:
        if col in df.columns and df[col].notna().any():
            group_cols.append(col)
    metrics = [
        "route_table_accuracy_all",
        "composition_accuracy_seen_routes",
        "composition_accuracy_suffix_routes",
        "first_step_context_accuracy",
        "suffix_generalization_gap",
        "route_table_composition_gap_seen",
        "route_table_composition_gap_suffix",
        "capacity_used",
        "evictions",
        "hash_collisions",
    ]
    rows: List[Dict[str, Any]] = []
    grouped = df.groupby(group_cols, dropna=False)
    for keys, group in grouped:
        if not isinstance(keys, tuple):
            keys = (keys,)
        base = dict(zip(group_cols, keys))
        base["seed_count"] = int(group["seed"].nunique()) if "seed" in group else len(group)
        base["row_count"] = int(len(group))
        for metric in metrics:
            if metric not in group.columns:
                continue
            mean, std, lo, hi, n = mean_ci95(group[metric].tolist())
            base[f"{metric}_mean"] = mean
            base[f"{metric}_std"] = std
            base[f"{metric}_ci95_low"] = lo
            base[f"{metric}_ci95_high"] = hi
            base[f"{metric}_n"] = n
        rows.append(base)
    return pd.DataFrame(rows).sort_values(group_cols).reset_index(drop=True)


def make_effect_sizes(df: pd.DataFrame) -> pd.DataFrame:
    metrics = [
        "route_table_accuracy_all",
        "composition_accuracy_seen_routes",
        "composition_accuracy_suffix_routes",
        "first_step_context_accuracy",
    ]
    rows: List[Dict[str, Any]] = []
    base_variant = "exp13_2_cirm_full"
    group_cols = ["phase", "world_count", "route_length", "capacity_condition"]
    for keys, group in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        key_payload = dict(zip(group_cols, keys))
        base_group = group[group["variant"] == base_variant]
        if base_group.empty:
            continue
        for variant, vg in group.groupby("variant"):
            if variant == base_variant:
                continue
            for metric in metrics:
                if metric not in group.columns:
                    continue
                d = cohen_d(base_group[metric].tolist(), vg[metric].tolist())
                diff = float(np.nanmean(base_group[metric]) - np.nanmean(vg[metric]))
                rows.append(
                    {
                        **key_payload,
                        "baseline_variant": base_variant,
                        "comparison_variant": variant,
                        "metric": metric,
                        "mean_difference_cirm_minus_comparison": diff,
                        "cohen_d_cirm_minus_comparison": d,
                        "n_cirm": int(base_group["seed"].nunique()),
                        "n_comparison": int(vg["seed"].nunique()),
                    }
                )
    return pd.DataFrame(rows)


def save_plot_bar(
    summary: pd.DataFrame,
    *,
    out_path: Path,
    phase: str,
    metric_mean_col: str,
    title: str,
    ylabel: str,
    route_length: Optional[int] = None,
    world_count: Optional[int] = None,
    max_variants: int = 14,
) -> None:
    data = summary[summary["phase"] == phase].copy()
    if route_length is not None and "route_length" in data:
        data = data[data["route_length"] == route_length]
    if world_count is not None and "world_count" in data:
        data = data[data["world_count"] == world_count]
    if data.empty or metric_mean_col not in data.columns:
        return
    # Prefer non-capacity primary condition where applicable.
    if "capacity_condition" in data.columns and (data["capacity_condition"] == NO_CAPACITY).any():
        data = data[data["capacity_condition"] == NO_CAPACITY]
    group = data.groupby("variant", dropna=False)[metric_mean_col].mean().sort_values(ascending=False).head(max_variants)
    plt.figure(figsize=(max(10, 0.45 * len(group)), 6))
    group.plot(kind="bar")
    plt.ylim(0, 1.05 if "accuracy" in metric_mean_col else max(1.05, float(group.max()) * 1.1 if len(group) else 1.0))
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=160)
    plt.close()


def save_capacity_plot(summary: pd.DataFrame, out_path: Path) -> None:
    data = summary[summary["phase"] == "capacity_pressure"].copy()
    if data.empty or "capacity_ratio" not in data.columns:
        return
    # Aggregate over world/route settings for a compact overview.
    agg = (
        data.groupby(["variant_family", "capacity_ratio"], dropna=False)["composition_accuracy_suffix_routes_mean"]
        .mean()
        .reset_index()
    )
    if agg.empty:
        return
    plt.figure(figsize=(10, 6))
    for family, g in agg.groupby("variant_family"):
        g = g.sort_values("capacity_ratio")
        plt.plot(g["capacity_ratio"], g["composition_accuracy_suffix_routes_mean"], marker="o", label=family)
    plt.xlabel("Capacity ratio")
    plt.ylabel("Suffix composition accuracy")
    plt.title("Finite-capacity baseline pressure")
    plt.ylim(0, 1.05)
    plt.legend(fontsize=8)
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=160)
    plt.close()


def save_retention_plot(summary: pd.DataFrame, out_path: Path) -> None:
    data = summary[summary["phase"] == "sequential_retention"].copy()
    if data.empty or "world_age_from_end" not in data.columns:
        return
    agg = (
        data.groupby(["variant_family", "world_age_from_end"], dropna=False)["composition_accuracy_suffix_routes_mean"]
        .mean()
        .reset_index()
    )
    if agg.empty:
        return
    plt.figure(figsize=(10, 6))
    for family, g in agg.groupby("variant_family"):
        g = g.sort_values("world_age_from_end")
        plt.plot(g["world_age_from_end"], g["composition_accuracy_suffix_routes_mean"], marker="o", label=family)
    plt.xlabel("World age from end of sequential training")
    plt.ylabel("Suffix composition accuracy")
    plt.title("Sequential retention by world age")
    plt.ylim(0, 1.05)
    plt.legend(fontsize=8)
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=160)
    plt.close()


def generate_plots(summary: pd.DataFrame, plots_dir: Path, config: Config) -> List[str]:
    plots_dir.mkdir(parents=True, exist_ok=True)
    selected_wc = max(config.world_counts)
    selected_len = max(config.route_lengths)
    plot_paths: List[str] = []
    specs = [
        (
            "exp13_2_seen_route_composition_accuracy.png",
            "baseline_comparison",
            "composition_accuracy_seen_routes_mean",
            "Seen-route composition accuracy",
            "Accuracy",
        ),
        (
            "exp13_2_suffix_generalization_accuracy.png",
            "baseline_comparison",
            "composition_accuracy_suffix_routes_mean",
            "Suffix-route composition over seen primitives",
            "Accuracy",
        ),
        (
            "exp13_2_route_table_accuracy.png",
            "baseline_comparison",
            "route_table_accuracy_all_mean",
            "One-step route-table accuracy",
            "Accuracy",
        ),
        (
            "exp13_2_first_step_context_accuracy.png",
            "baseline_comparison",
            "first_step_context_accuracy_mean",
            "First-step context disambiguation accuracy",
            "Accuracy",
        ),
    ]
    for filename, phase, metric, title, ylabel in specs:
        path = plots_dir / filename
        save_plot_bar(
            summary,
            out_path=path,
            phase=phase,
            metric_mean_col=metric,
            title=f"{title} (worlds={selected_wc}, length={selected_len})",
            ylabel=ylabel,
            route_length=selected_len,
            world_count=selected_wc,
        )
        if path.exists():
            plot_paths.append(str(path))
    capacity_path = plots_dir / "exp13_2_capacity_pressure.png"
    save_capacity_plot(summary, capacity_path)
    if capacity_path.exists():
        plot_paths.append(str(capacity_path))
    retention_path = plots_dir / "exp13_2_sequential_retention.png"
    save_retention_plot(summary, retention_path)
    if retention_path.exists():
        plot_paths.append(str(retention_path))
    return plot_paths


def device_metadata() -> Dict[str, Any]:
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "machine": platform.machine(),
        "cpu_count": os.cpu_count(),
        "numpy_version": np.__version__,
        "pandas_version": pd.__version__,
        "matplotlib_version": matplotlib.__version__,
        "gpu_used": False,
        "gpu_note": "This experiment is symbolic/table-based and runs on CPU; no GPU is required.",
    }


def write_sqlite(db_path: Path, df: pd.DataFrame, summary: pd.DataFrame, effects: pd.DataFrame, manifest: Mapping[str, Any]) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    with sqlite3.connect(db_path) as conn:
        df.to_sql("metrics", conn, index=False, if_exists="replace")
        summary.to_sql("summary", conn, index=False, if_exists="replace")
        effects.to_sql("effect_sizes", conn, index=False, if_exists="replace")
        manifest_df = pd.DataFrame([{"key": k, "value_json": json.dumps(v, sort_keys=True)} for k, v in manifest.items()])
        manifest_df.to_sql("manifest", conn, index=False, if_exists="replace")


def write_report(
    report_path: Path,
    *,
    config: Config,
    run_id: str,
    rows: pd.DataFrame,
    summary: pd.DataFrame,
    effects: pd.DataFrame,
    plot_paths: Sequence[str],
    sqlite_path: Optional[Path],
) -> None:
    def best_row(variant: str, metric: str, phase: str = "baseline_comparison") -> Optional[pd.Series]:
        subset = summary[(summary["phase"] == phase) & (summary["variant"] == variant)]
        if subset.empty or f"{metric}_mean" not in subset.columns:
            return None
        # choose hardest setting available
        subset = subset.sort_values(["world_count", "route_length"], ascending=[False, False])
        return subset.iloc[0]

    cirm_suffix = best_row("exp13_2_cirm_full", "composition_accuracy_suffix_routes")
    shared_seen = best_row("baseline_shared_transition_table", "composition_accuracy_seen_routes")
    shared_first = best_row("baseline_shared_transition_table", "first_step_context_accuracy")
    context_suffix = best_row("baseline_context_gated_transition_table", "composition_accuracy_suffix_routes")
    endpoint_seen = best_row("baseline_route_endpoint_memorizer", "composition_accuracy_seen_routes")
    endpoint_suffix = best_row("baseline_route_endpoint_memorizer", "composition_accuracy_suffix_routes")
    norec_seen = best_row("exp13_2_cirm_no_recurrence_at_eval", "composition_accuracy_seen_routes")
    norec_route_table = best_row("exp13_2_cirm_no_recurrence_at_eval", "route_table_accuracy_all")

    lines = [
        f"# Experiment 13.2 Report: Baseline Suite",
        "",
        "## Run identity",
        "",
        f"- Experiment: `{EXPERIMENT_NAME}`",
        f"- Run ID: `{run_id}`",
        f"- Profile: `{config.profile}`",
        f"- Seeds: `{list(config.seeds)}`",
        f"- World counts: `{list(config.world_counts)}`",
        f"- Route lengths: `{list(config.route_lengths)}`",
        f"- Routes per world: `{config.routes_per_world}`",
        f"- Metrics rows: `{len(rows)}`",
        f"- SQLite DB: `{sqlite_path}`" if sqlite_path else "- SQLite DB: not written",
        "",
        "## Executive summary",
        "",
        "This run compares the Context-Indexed Route Memory mechanism against explicit symbolic baselines under the same route-composition benchmark. It is designed to reduce the manuscript's baseline blocker, not to claim that CIRM beats an oracle lookup table.",
        "",
    ]
    if cirm_suffix is not None:
        lines.append(
            f"- CIRM suffix-composition accuracy at the hardest tested setting: "
            f"{cirm_suffix['composition_accuracy_suffix_routes_mean']:.4f}."
        )
    if context_suffix is not None:
        lines.append(
            f"- Explicit context-gated lookup suffix-composition accuracy at the hardest tested setting: "
            f"{context_suffix['composition_accuracy_suffix_routes_mean']:.4f}. This is expected to be strong and is an oracle-style control."
        )
    if shared_seen is not None and shared_first is not None:
        lines.append(
            f"- Shared no-context transition-table seen-route accuracy at the hardest tested setting: "
            f"{shared_seen['composition_accuracy_seen_routes_mean']:.4f}; first-step context disambiguation accuracy: "
            f"{shared_first['first_step_context_accuracy_mean']:.4f}. Suffix probes can be easier for this baseline because they start after the deliberately conflicting first step."
        )
    if endpoint_seen is not None and endpoint_suffix is not None:
        lines.append(
            f"- Whole-route endpoint memorizer seen-route accuracy: "
            f"{endpoint_seen['composition_accuracy_seen_routes_mean']:.4f}; suffix-route accuracy: "
            f"{endpoint_suffix['composition_accuracy_suffix_routes_mean']:.4f}."
        )
    if norec_seen is not None and norec_route_table is not None:
        lines.append(
            f"- CIRM no-recurrence-at-eval route-table accuracy: "
            f"{norec_route_table['route_table_accuracy_all_mean']:.4f}; seen-route composition accuracy: "
            f"{norec_seen['composition_accuracy_seen_routes_mean']:.4f}."
        )
    lines.extend(
        [
            "",
            "## Interpretation guardrails",
            "",
            "- If the context-gated lookup table performs as well as CIRM, that does not invalidate CIRM; it means this symbolic benchmark needs baselines and the novelty claim must be mechanistic rather than raw accuracy superiority.",
            "- If whole-route endpoint memorization solves seen routes but fails suffix routes, suffix probes support reusable primitive composition over route memorization.",
            "- If shared no-context lookup fails while context-gated lookup succeeds, this supports the need for context/world indexing under incompatible route systems.",
            "- If finite-capacity replay/isolation baselines fail gracefully or differently, those curves should be used to frame CIRM against conventional continual-learning controls.",
            "",
            "## Generated plots",
            "",
        ]
    )
    if plot_paths:
        for path in plot_paths:
            lines.append(f"- `{path}`")
    else:
        lines.append("- No plots were generated.")
    lines.extend(
        [
            "",
            "## Source artifacts",
            "",
            f"- `{ANALYSIS_ID}_metrics.csv`",
            f"- `{ANALYSIS_ID}_summary.csv`",
            f"- `{ANALYSIS_ID}_effect_sizes.csv`",
            f"- `{ANALYSIS_ID}_baseline_metrics.csv`",
            f"- `run_manifest.json`",
            f"- `progress.jsonl`",
        ]
    )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def expected_total_units(config: Config) -> int:
    baseline = len(config.seeds) * len(config.world_counts) * len(config.route_lengths)
    capacity = baseline * len(config.capacity_ratios)
    retention = len(config.seeds) * 1 * 1 * len(config.capacity_ratios)
    return baseline + capacity + retention


def run_all(
    *,
    config: Config,
    analysis_dir: Path,
    runs_dir: Path,
    run_id: str,
    write_sqlite_db: bool,
    progress_every: int,
) -> None:
    analysis_dir.mkdir(parents=True, exist_ok=True)
    plots_dir = analysis_dir / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)
    runs_dir.mkdir(parents=True, exist_ok=True)

    logger = ProgressLogger(analysis_dir / "progress.jsonl", expected_total_units(config), progress_every=progress_every)
    logger.event("run_start", config=dataclasses.asdict(config), run_id=run_id)

    start = time.time()
    baseline_rows = run_baseline_comparison(config, logger)
    capacity_rows = run_capacity_pressure(config, logger)
    retention_rows = run_sequential_retention(config, logger)
    rows = baseline_rows + capacity_rows + retention_rows
    df = pd.DataFrame(rows)

    # Normalize object/list columns before writing CSV/SQLite.
    for col in df.columns:
        if df[col].map(lambda x: isinstance(x, (list, tuple, dict))).any():
            df[col] = df[col].map(lambda x: json.dumps(x, sort_keys=True) if isinstance(x, (list, tuple, dict)) else x)

    summary = make_summary(df)
    effects = make_effect_sizes(df)
    plot_paths = generate_plots(summary, plots_dir, config)

    metrics_path = analysis_dir / f"{ANALYSIS_ID}_metrics.csv"
    summary_path = analysis_dir / f"{ANALYSIS_ID}_summary.csv"
    effects_path = analysis_dir / f"{ANALYSIS_ID}_effect_sizes.csv"
    baseline_path = analysis_dir / f"{ANALYSIS_ID}_baseline_metrics.csv"
    df.to_csv(metrics_path, index=False)
    df.to_csv(analysis_dir / "metrics.csv", index=False)
    summary.to_csv(summary_path, index=False)
    effects.to_csv(effects_path, index=False)
    df[df["phase"] == "baseline_comparison"].to_csv(baseline_path, index=False)

    manifest = {
        "experiment_name": EXPERIMENT_NAME,
        "analysis_id": ANALYSIS_ID,
        "schema_version": SCHEMA_VERSION,
        "run_id": run_id,
        "profile": config.profile,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "config": dataclasses.asdict(config),
        "artifact_paths": {
            "analysis_dir": str(analysis_dir),
            "runs_dir": str(runs_dir),
            "metrics_csv": str(metrics_path),
            "summary_csv": str(summary_path),
            "effect_sizes_csv": str(effects_path),
            "baseline_metrics_csv": str(baseline_path),
            "plots": plot_paths,
        },
        "row_counts": {
            "metrics_rows": int(len(df)),
            "summary_rows": int(len(summary)),
            "effect_size_rows": int(len(effects)),
        },
        "device": device_metadata(),
        "scientific_guardrails": [
            "Context-gated lookup is an oracle-style baseline and may match CIRM on clean symbolic composition.",
            "Whole-route memorization should be interpreted separately for seen-route and suffix-route probes.",
            "This experiment reduces the baseline blocker but does not replace neural/prior-art discussion.",
        ],
    }
    sqlite_path: Optional[Path] = None
    if write_sqlite_db:
        sqlite_path = runs_dir / f"{run_id}.sqlite3"
        manifest["artifact_paths"]["sqlite_db"] = str(sqlite_path)
        write_sqlite(sqlite_path, df, summary, effects, manifest)
    (analysis_dir / "run_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    (analysis_dir / f"{ANALYSIS_ID}_config.json").write_text(json.dumps(dataclasses.asdict(config), indent=2, sort_keys=True), encoding="utf-8")

    write_report(
        analysis_dir / "experiment_report.md",
        config=config,
        run_id=run_id,
        rows=df,
        summary=summary,
        effects=effects,
        plot_paths=plot_paths,
        sqlite_path=sqlite_path,
    )
    shutil.copyfile(analysis_dir / "experiment_report.md", analysis_dir / f"{ANALYSIS_ID}_report.md")

    logger.finish(
        metrics_rows=len(df),
        summary_rows=len(summary),
        effect_size_rows=len(effects),
        run_elapsed_seconds=round(time.time() - start, 3),
    )


def default_run_id(profile: str) -> str:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{ANALYSIS_ID}_{profile}_{stamp}"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=("smoke", "validation", "full"), default="smoke")
    parser.add_argument("--run-id", default=None, help="Run ID. Defaults to exp13_2_<profile>_<timestamp>.")
    parser.add_argument("--analysis-root", type=Path, default=Path("analysis"), help="Root directory for analysis outputs.")
    parser.add_argument("--runs-root", type=Path, default=Path("runs"), help="Root directory for SQLite outputs.")
    parser.add_argument("--no-sqlite", action="store_true", help="Do not write per-run SQLite database.")
    parser.add_argument("--progress-every", type=int, default=None, help="Console progress interval in work units.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    config = make_config(args.profile, progress_every=args.progress_every)
    run_id = args.run_id or default_run_id(args.profile)
    analysis_dir = args.analysis_root / run_id
    runs_dir = args.runs_root
    print(f"[{EXPERIMENT_NAME}] profile={config.profile} run_id={run_id}")
    print(f"[{EXPERIMENT_NAME}] analysis_dir={analysis_dir}")
    print(f"[{EXPERIMENT_NAME}] runs_dir={runs_dir}")
    run_all(
        config=config,
        analysis_dir=analysis_dir,
        runs_dir=runs_dir,
        run_id=run_id,
        write_sqlite_db=not args.no_sqlite,
        progress_every=config.progress_every,
    )
    print(f"[{EXPERIMENT_NAME}] Wrote analysis artifacts to {analysis_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
