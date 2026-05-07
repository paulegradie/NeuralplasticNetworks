# Baseline Requirements

## Evidence status

This document now mixes baseline planning with the completed Exp13.2 symbolic/algorithmic baseline result. Rows marked completed cite Exp13.2 artifacts; rows marked planned remain planning only.

Claim: Exp13.2 partially resolves the baseline blocker by adding a symbolic/algorithmic baseline suite.
Evidence: The completed Exp13.2 full run includes shared lookup, oracle context-gated lookup, endpoint memorization, recurrent non-plastic, superposition/hash, bounded LRU/replay, and parameter-isolation controls with validation PASS 28, WARN 0, FAIL 0.
Caveat: The thread-referenced novelty artifact named `Pasted text.txt` is not present locally; local verification pending. Exp13.2 does not replace neural baselines or prior-art review, and CIRM does not beat the oracle context-gated table in the clean supplied-context benchmark.
Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `docs/threads/experiment12to13_export.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`

## Why baselines are required

Internal ablations are not enough to establish manuscript-ready novelty. Exp13.2 now answers several simple-comparator questions directly, including whether a simpler transition table, conventional context gating, recurrence alone, replay-style finite memory, parameter isolation, or compact superposition-style lookup can solve or fail parts of the same benchmark.

Novelty should not rest on context gating, recurrence, or structural plasticity individually. Exp13.2 strengthens this discipline because oracle context-gated lookup matches CIRM on the clean supplied-context benchmark. The defensible contribution is narrower: the tested conjunction of context-indexed structural route memory plus recurrent execution, interpreted through distinct failure modes on a continual compositional route-memory benchmark.

## Minimum baseline suite for first manuscript

| Baseline ID | Baseline name | Purpose | Minimal implementation | Input/output contract | Metrics | Expected strength | Expected weakness | Manuscript role | Implementation status | Source path / rationale |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 | Shared transition table | Test whether explicit structural lookup without context separation is sufficient. | One global table keyed by `(source_node, mode)` with sequential updates; no per-world index. | Input: same worlds, nodes, modes, train/eval routes as Exp13.2. Output: predicted final node and one-step table prediction. | Composition accuracy; one-step route-table accuracy; retention; conflict-sensitive first-step accuracy. | Simple, transparent, strong when suffix probes avoid the conflict point. | Fails incompatible first-step/seen-route context probes. | Minimal lower bound and reviewer sanity check. | completed in Exp13.2 | Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`. |
| B2 | Context-gated transition table / task mask | Test whether supplied context labels plus task-specific masks explain the result. | Per-world transition table selected by oracle world/context label; no learned structural route-memory dynamics beyond lookup. | Input: same benchmark with oracle context label. Output: predicted final node, table accuracy, and capacity usage. | Composition accuracy; route-table accuracy; first-step context accuracy; capacity usage. | Solves the clean supplied-context benchmark. | Does not test endogenous context selection and uses explicit oracle labels. | Separates context indexing from the proposed structural/recurrent implementation. | completed in Exp13.2 | Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`. |
| B3 | Recurrent non-plastic executor | Test whether recurrence alone can execute routes without structural memory updates. | Fixed recurrent transition executor with no structural plasticity. | Input: one-step training sequence and multi-step evaluation routes. Output: final-node prediction and table metrics. | Composition accuracy; one-step accuracy; retention after sequential worlds; route-length sensitivity. | Tests whether recurrence alone explains the result. | Fails when local transition storage is absent. | Fair comparator for the recurrence claim. | completed in Exp13.2 | Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`. |
| B4 | Replay-based continual learner | Test whether replay can preserve route knowledge across sequential worlds. | Bounded LRU table with and without replay-like refresh under documented capacity ratios. | Input: same sequential world stream plus capacity ratios. Output: predictions and replay/resource metadata. | Composition accuracy; route-table accuracy; retention; capacity use; evictions. | Conventional finite-memory control under sufficient capacity. | Trades storage/replay assumptions against retention and may not expose the same structural mechanism. | Continual-learning style retention comparator. | completed symbolically in Exp13.2 | Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_baseline_metrics.csv`. |
| B5 | Parameter-isolation / mask-based baseline | Test whether isolated capacity explains retention and composition. | Allocate world-specific table partitions with documented capacity limits. | Input: same worlds/routes plus oracle world ID. Output: final-node prediction, capacity usage, and retention metrics. | Composition accuracy; route-table accuracy; retention; capacity usage; failure curves under pressure. | Strong when each world gets isolated capacity. | Requires task/world identity and explicit capacity allocation. | Tests whether the proposed mechanism is just parameter isolation. | completed in Exp13.2 | Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`. |
| B6 | Hypernetwork or context-conditioned weights baseline | Test whether compact context-conditioned storage can match route memory. | Exp13.2 implements a superposition/hash-slot context-conditioned storage baseline rather than a learned hypernetwork. | Input: world context plus route query. Output: final-node prediction, one-step prediction, collision counts, and capacity metadata. | Composition accuracy; route-table accuracy; retention; world-count scaling; hash collisions. | Natural compact-storage comparator. | Collision-sensitive and still oracle-context conditioned; not a full neural hypernetwork. | Distinguishes structural route memory from compact context-conditioned storage. | partially completed in Exp13.2 | Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_baseline_metrics.csv`. |
| B7 | Optional CSCG / cloned-state cognitive-map comparator | Test relationship to cloned-state or cognitive-map style representations. | Implement a minimal cloned-state map over observed transitions, or document why implementation is out of scope for the first manuscript. | Input: observed state/action/world trajectories. Output: inferred cloned states or transition map plus route predictions. | Route-table accuracy where applicable; composition accuracy; world/context selection; failure modes. | Conceptually close to context-specific state splitting. | May require different assumptions and a larger implementation scope. | Optional positioning comparator or discussion anchor. | planned | Thread-level planning mentions CSCG/cloned-state comparators; no local comparison exists. Source path: `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md`. |

## Benchmark contract for baselines

Baselines should run on the same route-memory benchmark slices used for the core Exp12/Exp13 claims and report:

- composition accuracy;
- route-table / one-step accuracy where applicable;
- retention after sequential worlds;
- world/context selection if applicable;
- capacity usage;
- failure curves under pressure;
- seed-level uncertainty;
- runtime/resource footprint if easy.

Every baseline result should be recorded with the same discipline:

```text
Claim -> Evidence -> Caveat -> Source path
```

## Baseline experiment organization

Completed organization:

- Baseline suite directory: `experiments/experiment13_2_baseline_suite/`.
- Full run ID: `exp13_2_full_20260507_165813`.
- Summary doc: `docs/experiments/exp13_2_summary.md`.

Keep any successor baseline protocol in a new experiment directory under `experiments/`.

## Acceptance criteria

The symbolic/algorithmic baseline suite is complete enough for first-pass claim refinement because Exp13.2 includes:

- shared-table, context-gated table, recurrent non-plastic, endpoint memorization, superposition/hash, bounded LRU/replay, and parameter-isolation baselines;
- the same Exp13.2 benchmark slices across 20 seeds;
- summary CSVs, effect sizes, validation outputs, and six generated plots;
- capacity/resource assumptions and run metadata;
- links from `docs/manuscript/CLAIMS_AND_EVIDENCE.md` and `docs/experiments/exp13_2_summary.md`;
- limitations recorded for symbolic scope, oracle context labels, and suffix-probe interpretation.

Remaining manuscript decisions:

- whether to add neural baselines beyond Exp13.2;
- how to cite prior art after importing the missing novelty assessment;
- whether Exp13.2 should be a main figure, supplementary figure, or table.

## Internal controls already represented

These are internal ablations, not external baselines.

| Control | Local evidence path | Caveat |
|---|---|---|
| No recurrence | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Supports storage/execution dissociation within the benchmark only. |
| No structural plasticity | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Internal ablation; not an external literature comparator. |
| No context binding or no world context | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/validation_report.md` | Exp13 no-context-binding variant definition remains caveated in the conflict log. |
| Capacity or memory-budget controls | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `docs/experiments/exp13_local_vs_global_budget_comparison.md` | Observed aggregate curves only; fitted capacity-law analysis is pending. |
| Context noise/corruption controls | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/context_bleed_summary.csv` | Exp13 adversarial corruption is failure evidence; Exp12 bleed/dropout is diagnostic only. |
