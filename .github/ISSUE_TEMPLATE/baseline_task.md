# Baseline Task

## Goal

Describe the baseline family and the benchmark slice it will test.

## Related experiment/docs

- Baseline planning doc:
- Related experiment:
- Related claim IDs:

## Evidence/source paths

- Claim:
- Evidence:
- Caveat:
- Source path:

## Acceptance criteria

- Baseline runs use the same key route-memory benchmark slices as the model comparison.
- Metrics include route-table accuracy, composition accuracy, retention, and relevant failure modes.
- Results are clearly marked as external baselines, not internal ablations.

## Non-goals

- Do not treat planned baselines as completed evidence.
- Do not modify Exp13 in place for successor protocols.
- Do not collapse internal ablations and external baselines into one claim category.

## Validation/QA checklist

- Record run profile, seeds, command, and output paths.
- Add or update baseline summary docs only after local artifacts exist.
- Run `python scripts/verify_doc_source_paths.py` after source-path-heavy doc edits.
