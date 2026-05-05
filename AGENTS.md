# Workspace Rules

This repository stores experiments as isolated, self-contained directories under `experiments/`.

## Repository Structure Rules

- Experiments live under `experiments/`.
- New experiments must be created under `experiments/`.
- Do not create new root-level experiment directories.
- Existing historical experiments remain self-contained historical records.
- Do not implement a new experiment by extending an older experiment directory in place.
- Do not rename or normalize existing experiment directories unless explicitly asked.
- Each experiment directory should contain its own code, runner scripts, analysis scripts, docs, `runs/`, and `analysis/` outputs as needed.
- Every experiment directory should include its own `README.md` with run instructions and a dedicated section for completed runs and results.
- Cross-experiment planning docs may live at the workspace root or under `docs/`.
- Shared utilities at the root should stay minimal and should not become the implementation home for a specific experiment.

## Experiment Naming

- Existing historical names may stay as-is.
- New experiments should use a clear normalized name under `experiments/`.
- Recommended examples for future work include `experiments/exp13_1_publication_hardening/` or the repository's existing style such as `experiments/experimentNN_descriptive_name/`.
- Successor protocols or corrected experimental designs should get a new experiment directory instead of modifying an older one in place.

## Reruns vs Successor Experiments

- A rerun is the same scientific protocol executed again.
- Reruns of the same protocol should stay under the owning experiment directory using that experiment's existing run or analysis convention, preferably under `runs/`, `analysis/runs/<run_id>/`, or the directory's documented output layout.
- A successor is a changed scientific protocol, corrected design, or new benchmark slice.
- Successors should get a new experiment directory under `experiments/`.
- If an experiment was started in the wrong directory, migrate it into its own directory under `experiments/` and remove the newer experiment's files from the older one.

## Run Logging And Immutability

- Experimental runs are immutable records.
- Completed generated outputs are historical evidence.
- Do not overwrite historical runs.
- Do not append multiple completed runs into a shared SQLite database for an experiment.
- Each completed run must write to its own separate SQLite database file when the experiment uses SQLite.
- Store per-run SQLite databases inside the owning experiment directory, typically under that experiment's `runs/` folder.
- Treat a completed run database as read-only historical output.
- If a new run is needed, create a new database file rather than reusing or overwriting an old one.
- After completing a run, update that experiment's `README.md` run-results section with the run name, database path, key configuration notes, and summarized results.

## Evidence Discipline

Use this structure everywhere evidence is interpreted:

```text
Claim -> Evidence -> Caveat -> Source path
```

- Do not strengthen scientific claims during cleanup work.
- If something is not yet supported, mark it as planned, pending, missing, future, or local verification pending.
- Internal ablations are not external baselines.
- Historical thread exports may preserve old conversation text, but active evidence maps and indexes should use current source paths.

## Documentation Paths

- Every active manuscript/evidence/source path must use the current `experiments/...` prefix.
- Do not cite stale paths such as `experiment12_capacity_generalization/analysis/...` in active manuscript or evidence docs.
- Every manuscript/evidence/source path cited in docs should either resolve to an existing local file or be explicitly marked as future, planned, missing, or local verification pending.
- New agents should run the path verifier after editing source-path-heavy docs.

## Path Verification

Run:

```bash
python scripts/verify_doc_source_paths.py
```

Use this before repo-readiness handoff, after manuscript/evidence path edits, and before wiring source-path-heavy documentation changes into review.

## GPU Usage

- Build new experiments to use the available GPUs on the system by default rather than assuming CPU-only execution.
- When multiple GPUs are available, design the experiment so it can make practical use of them when the workload supports it.
- Treat GPU support as part of the experiment design, not as a later optimization pass.
- Use `check_gpu_status.py` as a workspace reference when validating device visibility and runtime expectations.
- If an experiment cannot reasonably use the available GPUs, document the reason in that experiment's `README.md`.
- If GPU support is partial, document what is accelerated, what still runs on CPU, and any known limitations in the experiment `README.md`.
