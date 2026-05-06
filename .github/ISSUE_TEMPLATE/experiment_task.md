# Experiment Task

## Goal

Describe the experiment task and the specific question it addresses.

## Related experiment/docs

- Experiment directory:
- Planning docs:

## Evidence/source paths

- Claim:
- Evidence:
- Caveat:
- Source path:

## Acceptance criteria

- New work lives under `experiments/` if it is a new experiment or successor protocol.
- Completed runs write immutable per-run outputs.
- README/run-results documentation is updated after completed runs.

## Non-goals

- Do not overwrite historical runs.
- Do not modify unrelated experiment logic.
- Do not strengthen manuscript claims without source evidence.

## Validation/QA checklist

- Run the documented smoke or validation command if this task includes execution.
- Record runtime, profile, seeds, and output paths.
- Run `python scripts/verify_doc_source_paths.py` after source-path-heavy doc edits.
