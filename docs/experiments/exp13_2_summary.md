# Experiment 13.2 Summary: Baseline Suite

Experiment directory: `experiments/experiment13_2_baseline_suite/`
Thread digest: `docs/threads/experiment13_2_analysis_digest.md`
Run ID: `exp13_2_full_20260507_165813`
Run profile: `full`
Analysis directory: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/`
SQLite database: `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3`

## Import And Validation Status

Claim -> Exp13.2 has a locally verified full baseline-suite run.
Evidence -> `validation_report.md` reports `PASS: 28`, `WARN: 0`, `FAIL: 0`; `run_manifest.json` reports 20 seeds, 15040 metrics rows, 748 summary rows, 624 effect-size rows, and the local SQLite database path exists.
Caveat -> The uploaded analysis digest bundle did not include the SQLite database itself, so the DB is verified as a local repository artifact rather than as a zip-contained artifact.
Source path -> `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/run_manifest.json`; `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3`

## Manuscript-Relevant Results

Claim -> Exp13.2 partially resolves C12 by adding a symbolic/algorithmic baseline suite.
Evidence -> The run includes CIRM variants, shared no-context lookup, oracle context-gated lookup, endpoint memorization, recurrent non-plastic rules, superposition/hash slot baselines, bounded LRU with and without replay, and parameter isolation controls.
Caveat -> These are not full neural baselines and do not replace prior-art/novelty import.
Source path -> `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_baseline_metrics.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

Claim -> CIRM does not beat the oracle context-gated transition table on the clean supplied-context benchmark.
Evidence -> At `world_count=32`, `route_length=16`, and `phase=baseline_comparison`, both `exp13_2_cirm_full` and `baseline_context_gated_transition_table` report `1.0000` route-table accuracy, seen-route composition accuracy, suffix-route composition accuracy, and first-step context accuracy.
Caveat -> This constrains the novelty claim: clean supplied-context symbolic route memory can be solved by oracle context-gated lookup.
Source path -> `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

Claim -> Exp13.2 preserves mechanistic support for context indexing, recurrent execution, structural plasticity, and primitive reuse over endpoint memorization.
Evidence -> At the hard clean slice, shared no-context lookup has seen-route and first-step context accuracy of `0.03125`; no-recurrence-at-eval keeps route-table and first-step accuracy at `1.0000` while seen/suffix composition is `0.0000`; no-structural-plasticity has route-table, seen, suffix, and first-step accuracy `0.0000`; endpoint memorization reaches seen-route accuracy `1.0000` but suffix-route accuracy `0.0000`.
Caveat -> Shared no-context suffix-route accuracy is high because suffix probes can avoid the disambiguating first-step conflict; endpoint-memorizer failure does not prove broad unseen primitive inference.
Source path -> `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

## Key Artifacts

- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/experiment_report.md`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/run_manifest.json`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_effect_sizes.csv`
- `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_baseline_metrics.csv`
- `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3`

## Caveats

- Baselines are symbolic/algorithmic, not full neural baselines.
- Oracle context labels remain a limitation.
- Suffix probes can be misleading for no-context lookup.
- Exp13.2 does not resolve the Exp13.1 lesion failure.
- Prior-art/novelty import and final paper-specific figure scripts remain needed.
