# Experiment 13.2 Analysis Import Report

## Summary

Imported `docs/imports/experiment13_2_analysis_digest.zip` into the canonical docs system. The package contained one root-level digest, staged as `docs/threads/experiment13_2_analysis_digest.md`. Local Exp13.2 artifacts were present, including the SQLite run database, validation report, run manifest, CSV summaries, and plots.

## Import package reviewed

- Zip path: `docs/imports/experiment13_2_analysis_digest.zip`.
- Contents: one required markdown digest, `experiment13_2_analysis_digest.md`, at zip root.
- Original zip retained.

## Thread digest imported

Source thread path: `docs/threads/experiment13_2_analysis_digest.md`.

## Local artifacts reviewed

- Run ID: `exp13_2_full_20260507_165813`.
- SQLite database: `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3`.
- Validation: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`, PASS 28, WARN 0, FAIL 0.
- Run manifest: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/run_manifest.json`.
- Key CSVs: `exp13_2_summary.csv`, `exp13_2_effect_sizes.csv`, `exp13_2_baseline_metrics.csv`, `exp13_2_metrics.csv`, `metrics.csv`.
- Key plots: `exp13_2_seen_route_composition_accuracy.png`, `exp13_2_suffix_generalization_accuracy.png`, `exp13_2_route_table_accuracy.png`, `exp13_2_first_step_context_accuracy.png`, `exp13_2_capacity_pressure.png`, `exp13_2_sequential_retention.png`.

## Docs updated

- `docs/threads/THREAD_INDEX.md`
- `docs/experiments/exp13_2_summary.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `experiments/experiment13_2_baseline_suite/README.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/source_data/README.md`
- `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`

## Claims changed

| Claim ID | Change | Reason | Source |
|---|---|---|---|
| C1 | Added Exp13.2 no-structural-plasticity support. | No-structural-plasticity fails route-table and composition metrics in the completed baseline suite. | `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` |
| C2 | Added shared no-context baseline support and suffix-probe caveat. | Shared no-context lookup fails seen-route and first-step context probes at the hard clean slice. | `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` |
| C3 | Added Exp13.2 no-recurrence-at-eval support. | Route-table accuracy stays at 1.0 while seen/suffix composition is 0.0. | `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` |
| C4 | Added endpoint-memorizer and no-recurrence support. | Endpoint memorization solves seen routes but fails suffix composition; no-recurrence separates storage from execution. | `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv` |
| C12 | Changed from missing baselines to partially satisfied. | Exp13.2 supplies symbolic/algorithmic baselines, while prior-art import and possible neural baselines remain open. | `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md` |

## Figures changed

Added a candidate Exp13.2 baseline-suite figure/table entry and supplementary plot row. The figure plan explicitly says not to frame Exp13.2 as CIRM outperforming oracle context-gated lookup.

## Limitations added

- Symbolic/algorithmic baseline scope.
- Oracle context-gated lookup matches CIRM in the clean supplied-context benchmark.
- Shared no-context suffix probes can be misleading.
- Exp13.2 does not resolve the Exp13.1 lesion failure.
- Prior-art/novelty import and final figure scripts remain needed.

## TODOs added or resolved

- Resolved: minimum symbolic/algorithmic baseline suite has a completed Exp13.2 run.
- Added: decide whether additional neural baselines are required.
- Added: decide whether Exp13.2 appears as a main figure, supplementary figure, or table.
- Retained: import novelty assessment, audit Exp13.1 lesion diagnostic if lesion evidence is used, and create reproducible final figure scripts.

## Conflicts or caveats

- The uploaded digest bundle lacked the SQLite database, but the DB exists locally and was cited as a locally verified artifact.
- No direct digest/artifact conflict was found for Exp13.2 metrics.
- The oracle context-gated baseline matching CIRM is an active manuscript caveat and claim refinement.

## Path verification result

Ran `python scripts/verify_doc_source_paths.py` after import edits. Result: 83 files scanned, 5303 OK paths, 0 missing active paths, 9 skipped planned/future paths, and 43 skipped local-verification-pending paths.
