# Experiment Completion Checklist

An experiment is not complete until every item below is checked.

## Design

- [ ] Experiment design exists.
- [ ] Rerun vs successor/new protocol is explicitly classified.
- [ ] Hypotheses are explicit.
- [ ] Metrics are defined.
- [ ] Variants/baselines are defined.
- [ ] Expected failure modes are listed.
- [ ] Manuscript relevance is stated.
- [ ] GPU/device plan is stated, including any CPU-only or partial-GPU caveat.

## Implementation

- [ ] Experiment has its own directory under `experiments/`.
- [ ] No new root-level experiment directory was created.
- [ ] Experiment directory contains its own code, runner scripts, analysis scripts, `runs/`, `analysis/`, and docs as needed.
- [ ] README exists with run instructions and a completed-runs/results section.
- [ ] Smoke/standard/full profiles are documented or intentionally omitted.
- [ ] Run manifest is produced.
- [ ] Validation report is produced.
- [ ] Summary CSVs are produced.
- [ ] Plots are produced.
- [ ] SQLite outputs, if used, are written as one database file per run under the owning experiment directory.
- [ ] GPU visibility/support was checked or documented using `check_gpu_status.py` as the workspace reference.
- [ ] Smoke run passes.

## Run

- [ ] Standard/full run completed.
- [ ] Completed run artifacts are stored under the owning `experiments/<experiment_dir>/runs/` or `experiments/<experiment_dir>/analysis/<run_id>/` convention.
- [ ] Historical run outputs were not overwritten or appended into a shared completed-run database.
- [ ] Owning experiment README completed-runs/results section was updated.
- [ ] Artifacts are committed or staged appropriately.
- [ ] Run profile, seeds, and config are recorded.
- [ ] Validation report checked.

## Analysis

- [ ] Artifacts uploaded to ChatGPT.
- [ ] Analysis completed.
- [ ] Caveats identified.
- [ ] Claims classified conservatively.
- [ ] Figures assessed.

## Thread digest

- [ ] Analysis digest generated.
- [ ] Digest saved under `docs/threads/`.
- [ ] Digest indexed in `docs/threads/THREAD_INDEX.md`.

## Repository import

- [ ] Experiment summary updated.
- [ ] Owning experiment README updated if run results changed.
- [ ] Experiment registry updated.
- [ ] Claims/evidence updated.
- [ ] Figure plan updated.
- [ ] Limitations updated.
- [ ] TODOs updated.
- [ ] Synthesis docs updated.
- [ ] Conflict log updated if needed.
- [ ] Path verifier passes.

## QA

- [ ] Repo update QA completed.
- [ ] No claims overstrengthened.
- [ ] No planned results treated as completed.
- [ ] No missing active source paths.
- [ ] Active source paths use current `experiments/...` prefixes or are explicitly marked planned/missing/local verification pending.
- [ ] No stale root-level experiment paths are cited in active manuscript/evidence docs.
- [ ] Next action decided.
