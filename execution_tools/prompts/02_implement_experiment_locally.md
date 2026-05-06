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
- New scientific protocols get new experiment directories.
- Reruns of the same protocol belong inside the owning experiment directory.
- Every experiment must include a README and reproducible run commands.
- Generated outputs must be traceable.
- Evidence discipline: Claim -> Evidence -> Caveat -> Source path.

Experiment design to implement:

<PASTE FINAL EXPERIMENT DESIGN HERE>

Create a directory:

experiments/<experiment_id>_<short_name>/

The directory should include:

- `README.md`
- main experiment runner, for example `run_<experiment_id>.py`
- PowerShell launcher, for example `start_<experiment_id>.ps1`
- optional shell launcher if useful
- `requirements.txt` if new dependencies are required
- analysis output structure
- validation script or validation mode
- generated report writer
- plotting code
- run manifest generation

Required run profiles:

- `smoke`: small, fast, sanity-check profile
- `standard`: analysis-grade local run
- `full`: manuscript-grade or near-manuscript-grade run, if feasible

The implementation should produce:

- `analysis/<profile_or_run_id>/metrics.csv`
- summary CSVs specific to the experiment
- plots under `analysis/<profile_or_run_id>/plots/`
- `experiment_report.md`
- `validation_report.md`
- `run_manifest.json`

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
4. Do not run long profiles automatically.
5. Do not commit.

Final response:
- files created;
- smoke command run;
- smoke result;
- generated artifacts;
- warnings/errors;
- next command to run for standard/full.
```
