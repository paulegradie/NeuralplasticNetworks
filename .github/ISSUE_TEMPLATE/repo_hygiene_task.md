# Repo Hygiene Task

## Goal

Describe the maintenance, organization, or documentation hygiene task.

## Related experiment/docs

- Files or directories:
- Affected docs:

## Evidence/source paths

- Claim:
- Evidence:
- Caveat:
- Source path:

## Acceptance criteria

- No experiment logic is changed unless explicitly in scope.
- Historical artifacts and thread exports are not rewritten.
- New docs use current `experiments/...` paths for active source references.

## Non-goals

- Do not rerun experiments.
- Do not delete generated artifacts.
- Do not rename historical experiment directories unless explicitly approved.

## Validation/QA checklist

- Run `python scripts/verify_doc_source_paths.py` after source-path-heavy edits.
- Check docs CSV files are not Git LFS pointer text if docs CSVs changed.
- Check `git status` before handoff.
