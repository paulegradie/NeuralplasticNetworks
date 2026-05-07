#!/usr/bin/env python3
"""Validate Experiment 13.2 output artifacts.

Validation is intentionally conservative: it checks artifact integrity and expected
sanity relationships, but does not turn every scientific surprise into a hard fail.
Failed sanity checks mean the run should not be imported into manuscript docs until
reviewed.
"""

from __future__ import annotations

import argparse
import json
import math
import sqlite3
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import numpy as np
import pandas as pd


ANALYSIS_ID = "exp13_2"
EXPERIMENT_NAME = "exp13_2_baseline_suite"
REQUIRED_VARIANTS = {
    "exp13_2_cirm_full",
    "exp13_2_cirm_no_recurrence_at_eval",
    "exp13_2_cirm_no_structural_plasticity",
    "baseline_shared_transition_table",
    "baseline_context_gated_transition_table",
    "baseline_route_endpoint_memorizer",
    "baseline_recurrent_non_plastic_rule",
}
REQUIRED_PHASES = {"baseline_comparison", "capacity_pressure", "sequential_retention"}
REQUIRED_COLUMNS = {
    "phase",
    "seed",
    "world_count",
    "route_length",
    "variant",
    "variant_family",
    "route_table_accuracy_all",
    "composition_accuracy_seen_routes",
    "composition_accuracy_suffix_routes",
    "first_step_context_accuracy",
    "capacity_used",
}


@dataclass
class CheckResult:
    name: str
    status: str
    detail: str


def add(results: List[CheckResult], name: str, status: str, detail: str) -> None:
    results.append(CheckResult(name=name, status=status, detail=detail))
    prefix = {"PASS": "[PASS]", "WARN": "[WARN]", "FAIL": "[FAIL]"}.get(status, "[INFO]")
    print(f"{prefix} {name}: {detail}")


def latest_run_dir(analysis_root: Path) -> Path:
    candidates = [p for p in analysis_root.iterdir() if p.is_dir() and p.name.startswith(f"{ANALYSIS_ID}_")]
    if not candidates:
        raise FileNotFoundError(f"No {ANALYSIS_ID}_* run directories found under {analysis_root}")
    return sorted(candidates, key=lambda p: p.stat().st_mtime, reverse=True)[0]


def finite_mean(df: pd.DataFrame, variant: str, metric: str, phase: str = "baseline_comparison") -> float:
    subset = df[(df["phase"] == phase) & (df["variant"] == variant)]
    if subset.empty or metric not in subset.columns:
        return float("nan")
    return float(np.nanmean(subset[metric].astype(float)))


def validate(analysis_dir: Path) -> Dict[str, Any]:
    results: List[CheckResult] = []

    required_files = [
        analysis_dir / f"{ANALYSIS_ID}_metrics.csv",
        analysis_dir / "metrics.csv",
        analysis_dir / f"{ANALYSIS_ID}_summary.csv",
        analysis_dir / f"{ANALYSIS_ID}_effect_sizes.csv",
        analysis_dir / f"{ANALYSIS_ID}_baseline_metrics.csv",
        analysis_dir / "run_manifest.json",
        analysis_dir / "progress.jsonl",
        analysis_dir / "experiment_report.md",
    ]
    for path in required_files:
        add(results, f"file exists: {path.name}", "PASS" if path.exists() else "FAIL", str(path))

    if not (analysis_dir / f"{ANALYSIS_ID}_metrics.csv").exists():
        return finalize(analysis_dir, results)

    df = pd.read_csv(analysis_dir / f"{ANALYSIS_ID}_metrics.csv")
    summary = pd.read_csv(analysis_dir / f"{ANALYSIS_ID}_summary.csv") if (analysis_dir / f"{ANALYSIS_ID}_summary.csv").exists() else pd.DataFrame()

    add(results, "metrics row count", "PASS" if len(df) > 0 else "FAIL", f"{len(df)} rows")
    missing_cols = sorted(REQUIRED_COLUMNS - set(df.columns))
    add(results, "required metric columns", "PASS" if not missing_cols else "FAIL", "missing=" + json.dumps(missing_cols))

    phases = set(df["phase"].dropna().unique()) if "phase" in df else set()
    missing_phases = sorted(REQUIRED_PHASES - phases)
    add(results, "required phases present", "PASS" if not missing_phases else "FAIL", "missing=" + json.dumps(missing_phases))

    variants = set(df["variant"].dropna().unique()) if "variant" in df else set()
    missing_variants = sorted(REQUIRED_VARIANTS - variants)
    add(results, "required variants present", "PASS" if not missing_variants else "FAIL", "missing=" + json.dumps(missing_variants))

    seed_count = int(df["seed"].nunique()) if "seed" in df else 0
    add(results, "seed count nonzero", "PASS" if seed_count > 0 else "FAIL", f"seed_count={seed_count}")

    if not summary.empty:
        add(results, "summary row count", "PASS" if len(summary) > 0 else "FAIL", f"{len(summary)} rows")
    else:
        add(results, "summary row count", "FAIL", "summary missing or empty")

    manifest_path = analysis_dir / "run_manifest.json"
    manifest: Dict[str, Any] = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        add(results, "manifest experiment name", "PASS" if manifest.get("experiment_name") == EXPERIMENT_NAME else "FAIL", str(manifest.get("experiment_name")))
        device = manifest.get("device", {})
        add(results, "device metadata present", "PASS" if device.get("python_version") and "gpu_used" in device else "WARN", json.dumps(device, sort_keys=True)[:400])
        sqlite_path = manifest.get("artifact_paths", {}).get("sqlite_db")
        if sqlite_path:
            p = Path(sqlite_path)
            add(results, "sqlite db exists", "PASS" if p.exists() else "FAIL", sqlite_path)
            if p.exists():
                try:
                    with sqlite3.connect(p) as conn:
                        tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", conn)["name"].tolist()
                    expected_tables = {"metrics", "summary", "effect_sizes", "manifest"}
                    add(results, "sqlite tables", "PASS" if expected_tables.issubset(set(tables)) else "FAIL", json.dumps(tables))
                except Exception as exc:  # pragma: no cover - defensive validation path
                    add(results, "sqlite readable", "FAIL", repr(exc))
        else:
            add(results, "sqlite db path", "WARN", "manifest does not include sqlite_db path")

    # Scientific sanity checks.
    cirm_seen = finite_mean(df, "exp13_2_cirm_full", "composition_accuracy_seen_routes")
    cirm_suffix = finite_mean(df, "exp13_2_cirm_full", "composition_accuracy_suffix_routes")
    ctx_suffix = finite_mean(df, "baseline_context_gated_transition_table", "composition_accuracy_suffix_routes")
    shared_seen = finite_mean(df, "baseline_shared_transition_table", "composition_accuracy_seen_routes")
    shared_first = finite_mean(df, "baseline_shared_transition_table", "first_step_context_accuracy")
    endpoint_seen = finite_mean(df, "baseline_route_endpoint_memorizer", "composition_accuracy_seen_routes")
    endpoint_suffix = finite_mean(df, "baseline_route_endpoint_memorizer", "composition_accuracy_suffix_routes")
    no_rec_table = finite_mean(df, "exp13_2_cirm_no_recurrence_at_eval", "route_table_accuracy_all")
    no_rec_suffix = finite_mean(df, "exp13_2_cirm_no_recurrence_at_eval", "composition_accuracy_suffix_routes")
    no_struct_table = finite_mean(df, "exp13_2_cirm_no_structural_plasticity", "route_table_accuracy_all")

    add(results, "CIRM full solves seen routes", "PASS" if cirm_seen >= 0.99 else "FAIL", f"mean={cirm_seen:.4f}")
    add(results, "CIRM full solves suffix routes", "PASS" if cirm_suffix >= 0.99 else "FAIL", f"mean={cirm_suffix:.4f}")
    add(results, "context-gated table solves suffix routes", "PASS" if ctx_suffix >= 0.99 else "FAIL", f"mean={ctx_suffix:.4f}")
    add(results, "shared no-context table underperforms on context-conflict probes", "PASS" if shared_seen < 0.90 and shared_first < 0.90 else "WARN", f"seen={shared_seen:.4f}; first_step={shared_first:.4f}")
    add(results, "endpoint memorizer seen-vs-suffix split", "PASS" if endpoint_seen > 0.95 and endpoint_suffix < 0.25 else "WARN", f"seen={endpoint_seen:.4f}; suffix={endpoint_suffix:.4f}")
    add(results, "no-recurrence route-table preserved", "PASS" if no_rec_table >= 0.99 else "FAIL", f"mean={no_rec_table:.4f}")
    add(results, "no-recurrence composition impaired", "PASS" if no_rec_suffix < 0.50 else "WARN", f"mean={no_rec_suffix:.4f}")
    add(results, "no-structural-plasticity route table low", "PASS" if no_struct_table < 0.10 else "WARN", f"mean={no_struct_table:.4f}")

    plot_dir = analysis_dir / "plots"
    plots = sorted(plot_dir.glob("*.png")) if plot_dir.exists() else []
    add(results, "plots generated", "PASS" if len(plots) >= 4 else "WARN", f"{len(plots)} png files")

    progress_path = analysis_dir / "progress.jsonl"
    if progress_path.exists():
        lines = progress_path.read_text(encoding="utf-8").strip().splitlines()
        has_complete = any('"event": "run_complete"' in line for line in lines)
        add(results, "progress has run_complete", "PASS" if has_complete else "WARN", f"events={len(lines)}")

    return finalize(analysis_dir, results)


def finalize(analysis_dir: Path, results: List[CheckResult]) -> Dict[str, Any]:
    pass_count = sum(1 for r in results if r.status == "PASS")
    warn_count = sum(1 for r in results if r.status == "WARN")
    fail_count = sum(1 for r in results if r.status == "FAIL")
    payload = {
        "experiment_name": EXPERIMENT_NAME,
        "analysis_id": ANALYSIS_ID,
        "analysis_dir": str(analysis_dir),
        "status": "FAIL" if fail_count else "PASS_WITH_WARNINGS" if warn_count else "PASS",
        "pass_count": pass_count,
        "warn_count": warn_count,
        "fail_count": fail_count,
        "checks": [asdict(r) for r in results],
    }
    (analysis_dir / "validation_results.json").write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    lines = [
        f"# Experiment 13.2 Validation Report",
        "",
        f"- Analysis directory: `{analysis_dir}`",
        f"- Status: **{payload['status']}**",
        f"- PASS: {pass_count}",
        f"- WARN: {warn_count}",
        f"- FAIL: {fail_count}",
        "",
        "## Checks",
        "",
        "| Status | Check | Detail |",
        "|---|---|---|",
    ]
    for r in results:
        safe_detail = str(r.detail).replace("|", "\\|")
        lines.append(f"| {r.status} | {r.name} | {safe_detail} |")
    (analysis_dir / "validation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return payload


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis-dir", type=Path, default=None, help="Specific analysis run directory to validate.")
    parser.add_argument("--analysis-root", type=Path, default=Path("analysis"), help="Root directory for latest-run discovery.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    analysis_dir = args.analysis_dir or latest_run_dir(args.analysis_root)
    print(f"[{EXPERIMENT_NAME}] Validating {analysis_dir}")
    payload = validate(analysis_dir)
    print(
        f"[{EXPERIMENT_NAME}] validation status={payload['status']} "
        f"PASS={payload['pass_count']} WARN={payload['warn_count']} FAIL={payload['fail_count']}"
    )
    return 1 if payload["fail_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
