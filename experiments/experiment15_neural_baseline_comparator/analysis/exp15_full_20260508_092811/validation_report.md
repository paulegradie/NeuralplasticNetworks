# Experiment 15 Validation Report

Status: PASS

## Counts

- PASS: 42
- WARN: 0
- FAIL: 0

## Checks

- **PASS** `source_file:README.md` — Found README.md.
- **PASS** `source_file:run_experiment15.py` — Found run_experiment15.py.
- **PASS** `source_file:analyze_experiment15.py` — Found analyze_experiment15.py.
- **PASS** `source_file:validate_experiment15.py` — Found validate_experiment15.py.
- **PASS** `source_file:start_exp15_validation.ps1` — Found start_exp15_validation.ps1.
- **PASS** `source_file:start_exp15_full.ps1` — Found start_exp15_full.ps1.
- **PASS** `artifact:run_manifest.json` — Found run_manifest.json.
- **PASS** `artifact:exp15_config.json` — Found exp15_config.json.
- **PASS** `artifact:progress.jsonl` — Found progress.jsonl.
- **PASS** `artifact:exp15_seed_metrics.csv` — Found exp15_seed_metrics.csv.
- **PASS** `artifact:metrics.csv` — Found metrics.csv.
- **PASS** `artifact:exp15_summary.csv` — Found exp15_summary.csv.
- **PASS** `artifact:exp15_effect_sizes.csv` — Found exp15_effect_sizes.csv.
- **PASS** `artifact:exp15_model_runtime.csv` — Found exp15_model_runtime.csv.
- **PASS** `artifact:exp15_report.md` — Found exp15_report.md.
- **PASS** `artifact:experiment_report.md` — Found experiment_report.md.
- **PASS** `artifact:plots/exp15_seen_vs_suffix_composition.png` — Found plots/exp15_seen_vs_suffix_composition.png.
- **PASS** `artifact:plots/exp15_context_conflict_accuracy.png` — Found plots/exp15_context_conflict_accuracy.png.
- **PASS** `artifact:plots/exp15_retention_after_sequential_worlds.png` — Found plots/exp15_retention_after_sequential_worlds.png.
- **PASS** `artifact:plots/exp15_route_length_scaling.png` — Found plots/exp15_route_length_scaling.png.
- **PASS** `artifact:plots/exp15_world_count_scaling.png` — Found plots/exp15_world_count_scaling.png.
- **PASS** `manifest:required_fields` — Runtime/hardware manifest fields are present.
- **PASS** `metrics:required_variants` — All required variants are present in seed metrics.
- **PASS** `metrics:required_metric_names` — All required metric names are present.
- **PASS** `metrics:valid_range` — All metric values are finite and within [0, 1].
- **PASS** `seeds:all_requested_completed` — All requested seeds completed and are present in metrics.
- **PASS** `split_metadata:split_id` — Split metadata column split_id exists and is populated.
- **PASS** `split_metadata:train_eval_split_metadata_present` — Split metadata column train_eval_split_metadata_present exists and is populated.
- **PASS** `split_metadata:suffix_holdout_protocol` — Split metadata column suffix_holdout_protocol exists and is populated.
- **PASS** `probe_type:seen_suffix_distinguishable` — Seen full-route and suffix probes are explicitly distinguishable.
- **PASS** `config:context_vs_no_context` — Context and no-context variants are distinguishable in config columns.
- **PASS** `config:replay_recorded` — replay_enabled explicitly records true for at least one variant.
- **PASS** `config:parameter_isolation_recorded` — parameter_isolated explicitly records true for at least one variant.
- **PASS** `summary:nonempty` — Summary contains 540 rows.
- **PASS** `summary:statistical_columns` — Summary contains mean/sd/sem/ci95/n_seeds columns.
- **PASS** `runtime:nonempty` — Runtime table contains 1080 rows.
- **PASS** `runtime:training_seconds` — Runtime column training_seconds exists.
- **PASS** `runtime:evaluation_seconds` — Runtime column evaluation_seconds exists.
- **PASS** `runtime:runtime_seconds` — Runtime column runtime_seconds exists.
- **PASS** `runtime:device` — Runtime column device exists.
- **PASS** `config:suffix_protocol_documented` — Config documents suffix holdout protocol.
- **PASS** `config:optional_kv_decision_recorded` — Optional neural key-value baseline omission is explicitly recorded.
