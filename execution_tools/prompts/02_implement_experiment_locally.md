# Prompt: Implement Experiment Locally

```text
You are working inside the local repository:

GradieResearch/context-indexed-route-memory

Your task is to implement the new experiment described below as a new self-contained experiment directory under `experiments/`.

Do not modify previous experiment directories except to reference them in docs if needed.
Do not mutate historical analysis artifacts.
Do not overwrite prior runs.
Do not change manuscript claims in this implementation pass unless explicitly requested.
Do not implement extra features beyond the design unless they are necessary for correctness.

Repository rules:
- Experiments live under `experiments/`.
- Do not create a new root-level experiment directory.
- New scientific protocols get new experiment directories.
- Reruns of the same protocol belong inside the owning experiment directory.
- Each experiment directory should contain its own code, runner scripts, analysis scripts, docs, `runs/`, and `analysis/` outputs as needed.
- Every experiment must include a README with reproducible run commands and a completed-runs/results section.
- Completed generated outputs are immutable historical records.
- If SQLite is used, each completed run must write to its own database file under the owning experiment directory, typically `runs/<run_id>.sqlite3`.
- Generated outputs must be traceable.
- Evidence discipline: Claim -> Evidence -> Caveat -> Source path.
- Active evidence/source paths must use current `experiments/...` prefixes, or be explicitly marked planned/missing/future/local verification pending.
- Build for available GPUs by default where practical. Use `check_gpu_status.py` as the workspace reference and document CPU-only or partial-GPU limitations in the experiment README.

Experiment design to implement:

<PASTE FINAL EXPERIMENT DESIGN HERE>

Create a directory:

```text
experiments/<experiment_id>_<short_name>/
```

The directory should include:

- `README.md`
- main experiment runner, for example `run_<experiment_id>.py`
- PowerShell launcher, for example `start_<experiment_id>.ps1`
- optional shell launcher if useful
- `requirements.txt` if new dependencies are required
- `runs/` for per-run databases or raw run records
- `analysis/` for per-run analysis outputs
- analysis output structure
- validation script or validation mode
- generated report writer
- plotting code
- run manifest generation
- GPU/device selection and logging where practical

Required run profiles:

- `smoke`: small, fast, sanity-check profile
- `standard`: analysis-grade local run
- `full`: manuscript-grade or near-manuscript-grade run, if feasible

The implementation should produce:

- `experiments/<experiment_dir>/runs/<run_id>.sqlite3` if SQLite is used
- `experiments/<experiment_dir>/analysis/<run_id>/metrics.csv`
- summary CSVs specific to the experiment
- plots under `experiments/<experiment_dir>/analysis/<run_id>/plots/`
- `experiments/<experiment_dir>/analysis/<run_id>/experiment_report.md`
- `experiments/<experiment_dir>/analysis/<run_id>/validation_report.md`
- `experiments/<experiment_dir>/analysis/<run_id>/run_manifest.json`

The README should include:

1. Purpose
2. Hypotheses
3. Design
4. Variants
5. Metrics
6. Run commands
7. Expected outputs
8. Validation
9. Known caveats
10. How to interpret results
11. How to import results into repo docs after analysis
12. GPU support: what is accelerated, what remains CPU, and limitations
13. Completed runs and results: run name, database path if present, config notes, and summarized results

Validation:
Implement lightweight validation checks that emit PASS/WARN/FAIL.

Examples:
- full/reference model behaves as expected;
- critical ablation fails as expected;
- metric columns exist;
- no NaNs;
- plots generated;
- expected run counts present;
- failure boundary observed if relevant.

After implementation:
1. Run the smoke profile only, unless I explicitly ask for standard/full.
2. Generate smoke outputs.
3. Confirm validation report exists.
4. Update the experiment README completed-runs/results section for the smoke run if it completed.
5. Do not run long profiles automatically.
6. Do not commit.

Final response:
- files created;
- smoke command run;
- smoke result;
- generated artifacts;
- warnings/errors;
- next command to run for standard/full.
```
