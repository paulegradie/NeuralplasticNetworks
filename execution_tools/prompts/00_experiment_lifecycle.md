# Experiment Lifecycle

Use this workflow for every new experiment.

Repository invariants:
- New experiments and changed successor protocols live under `experiments/<experiment_dir>/`.
- Reruns of the same scientific protocol stay inside the owning experiment directory.
- Do not create new root-level experiment directories or extend historical experiments in place for a changed protocol.
- Each experiment owns its code, runners, analysis scripts, `runs/`, `analysis/`, docs, and `README.md`.
- Completed runs are immutable. If SQLite is used, create a separate database file per completed run under the owning experiment directory.
- Active evidence paths should use current `experiments/...` prefixes, or be marked planned, missing, future, or local verification pending.
- New experiment designs should use available GPUs by default where practical and document CPU-only or partial-GPU limitations.

## Stage 1 — Design

Use `01_design_next_experiment.md`.

Output should include:
- experiment name;
- purpose;
- hypotheses;
- variants;
- metrics;
- expected outcomes;
- failure modes;
- manuscript role;
- implementation plan;
- run profiles;
- expected artifacts;
- repo update requirements.

## Stage 2 — Implement

Use `02_implement_experiment_locally.md`.

Output should create a new experiment directory under `experiments/`.

New experiments should not mutate old experiment directories.

## Stage 3 — Run

Run locally.

Expected run profiles:
- smoke
- standard
- full

Every run should produce:
- a unique run ID;
- generated report;
- metrics CSVs;
- summary CSVs;
- plots;
- validation report;
- run manifest.

Store run artifacts under the owning experiment directory, for example:
- `experiments/<experiment_dir>/runs/<run_id>.sqlite3` if SQLite is used;
- `experiments/<experiment_dir>/analysis/<run_id>/metrics.csv`;
- `experiments/<experiment_dir>/analysis/<run_id>/run_manifest.json`.

After each completed run, update the experiment `README.md` completed-runs/results section.

## Stage 4 — Analyze in ChatGPT

Upload the analysis artifacts to ChatGPT and use `03_analyze_uploaded_results.md`.

## Stage 5 — Extract thread analysis

Once analysis is complete, use `04_extract_thread_analysis_digest.md`.

Save the digest into:

```text
docs/threads/<YYYY-MM-DD>_expNN_<short_name>_analysis.md
```

## Stage 6 — Import analysis into repo

Use `05_import_analysis_into_repo.md`.

This updates:
- owning experiment README run/results section if needed;
- experiment summary;
- experiment registry;
- claims/evidence;
- figure plan;
- limitations;
- TODOs;
- synthesis docs.

## Stage 7 — QA

Use `07_repo_update_qa.md`.

## Stage 8 — Decide next experiment

Use `08_design_next_experiment_from_arch.md`.

Important:
No experiment is complete until Stage 6 and Stage 7 pass.
