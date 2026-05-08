# Experiment 15 Summary: Minimal Neural Baseline Comparator

Status: **planned / implemented, awaiting local execution and result import**.

This document exists so repository documentation references resolve before Experiment 15 has been run locally. It must not be cited as result evidence until the generated Exp15 artifacts have been imported and reviewed.

## Purpose

Experiment 15 implements a minimal neural baseline comparator for the Context-Indexed Route Memory manuscript.

The experiment asks whether ordinary neural sequence models trained under matched symbolic route-memory conditions reproduce, fail, or partially reproduce the same storage, context separation, retention, and compositional execution behavior observed in CIRM.

## Current implementation status

Implementation directory:

```text
experiments/experiment15_neural_baseline_comparator/
```

Implemented files:

- `experiments/experiment15_neural_baseline_comparator/README.md`
- `experiments/experiment15_neural_baseline_comparator/run_experiment15.py`
- `experiments/experiment15_neural_baseline_comparator/analyze_experiment15.py`
- `experiments/experiment15_neural_baseline_comparator/validate_experiment15.py`
- `experiments/experiment15_neural_baseline_comparator/start_exp15_validation.ps1`
- `experiments/experiment15_neural_baseline_comparator/start_exp15_full.ps1`

## Baseline variants

The implementation includes:

- GRU endpoint model with context;
- GRU endpoint model without context;
- GRU rollout model with context;
- GRU rollout model without context;
- small attention/Transformer-style endpoint model with context;
- one-step transition MLP with context;
- one-step transition MLP without context;
- sequential-world replay transition MLP;
- parameter-isolated transition MLP with world-specific heads.

The optional neural key-value / memory-augmented lookup baseline is intentionally omitted for scope control.

## Planned metrics

Expected generated metrics after local execution:

- one-step transition accuracy;
- seen-route composition accuracy;
- suffix-route composition accuracy;
- first-step context-conflict accuracy;
- retention after sequential worlds;
- route-length scaling;
- world-count scaling;
- runtime/training cost;
- seed-level summaries suitable for confidence intervals and effect sizes.

## Expected local artifacts after execution

After Paul runs the validation or full profile, the latest run directory should contain:

```text
analysis/exp15_<profile>_<timestamp>/
  validation_report.md
  validation_results.json
  run_manifest.json
  exp15_config.json
  progress.jsonl
  metrics.csv
  exp15_seed_metrics.csv
  exp15_summary.csv
  exp15_effect_sizes.csv
  exp15_model_runtime.csv
  exp15_report.md
  experiment_report.md
  plots/
    exp15_seen_vs_suffix_composition.png
    exp15_context_conflict_accuracy.png
    exp15_retention_after_sequential_worlds.png
    exp15_route_length_scaling.png
    exp15_world_count_scaling.png
```

## How to run locally

From the experiment directory:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp15_validation.ps1
```

If validation passes:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_exp15_full.ps1
```

## Result summary

Pending. No Experiment 15 local validation or full-run results have been imported into the repository yet.

Do not use this document as evidence for neural-baseline performance until it is replaced or updated after the generated `analysis/exp15_full_*` artifacts have been reviewed.

## Post-run import checklist

After the full run is analyzed, update this document with:

- run ID and profile;
- validation PASS/WARN/FAIL counts;
- row counts for `exp15_seed_metrics.csv`, `exp15_summary.csv`, `exp15_effect_sizes.csv`, and `exp15_model_runtime.csv`;
- key hard-slice results;
- Claim -> Evidence -> Caveat entries;
- source artifact paths;
- manuscript consequence for baseline and limitation language.
