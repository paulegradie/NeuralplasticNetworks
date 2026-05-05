# P1 Remediation Report

## Initial inspection

Already resolved by the P0 pass:

- Experiment directories had already been moved under `experiments/`.
- Active source paths mostly used current `experiments/...` paths.
- Documentation CSVs no longer appeared to be Git LFS pointer text.
- `scripts/verify_doc_source_paths.py` existed.
- README and AGENTS already had initial `experiments/` alignment.

Remaining P1 gaps at the start of this pass:

- README was useful but too thin as an external-facing entry point.
- AGENTS needed clearer rerun/successor, evidence, and path-verification rules.
- `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` was still mostly a discovered-command inventory.
- `docs/manuscript/BASELINE_REQUIREMENTS.md` listed baseline families but lacked implementation contracts and acceptance criteria.
- `docs/manuscript/MANUSCRIPT_SPINE.md` was skeletal.
- Several active planning/synthesis docs still used stale wording such as "top-level experiment directory."
- The next-step plan after P0 was present but not yet operational enough for Exp13.1/baselines/manuscript handoff.
- The path verifier was documented but not yet wired into CI.

## Summary

This P1 pass upgraded repository-readiness, reproducibility, onboarding, baseline planning, and manuscript-organization docs without modifying experiment logic, rerunning long experiments, implementing Exp13.1, implementing baselines, deleting generated artifacts, or strengthening scientific claims.

Path verifier status after remediation: pass with zero missing active paths.

## Items addressed

### README

Action taken:

Expanded README into an external-facing entry point covering repository contents, current status, scientific question, layout, start points, experiment overview, claim map, non-claims, reproducibility, planned next work, and license/citation caveat.

Files changed:

- `README.md`

Remaining caveat:

README remains an orientation document, not the manuscript or final reproducibility protocol.

### AGENTS.md

Action taken:

Aligned agent rules with the current `experiments/` structure, added repository structure rules, experiment naming, rerun versus successor definitions, evidence discipline, documentation path rules, path verification, and GPU documentation expectations.

Files changed:

- `AGENTS.md`

Remaining caveat:

Future agents still need to run the path verifier after source-path-heavy edits.

### Reproducibility audit

Action taken:

Converted the audit from a command inventory into a reproducibility map with goal, current summary, environment, manuscript-critical Exp11/Exp12/Exp13 command table, historical experiment table, target run interface, artifact regeneration notes, path verification, and submission requirements.

Files changed:

- `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

Remaining caveat:

Commands were inspected, not executed in this pass. Exp11/Exp12/Exp13 smoke or validation commands still need fresh-checkout verification with runtime notes.

### Baseline requirements

Action taken:

Made baseline planning actionable by defining evidence status, rationale, minimum baseline suite, implementation contracts, metrics, expected strengths/weaknesses, manuscript roles, planned organization, and acceptance criteria.

Files changed:

- `docs/manuscript/BASELINE_REQUIREMENTS.md`

Remaining caveat:

All baselines remain planned. No baseline result exists yet.

### Manuscript spine

Action taken:

Expanded the manuscript spine into a real manuscript architecture with conservative title options, one-sentence contribution, abstract skeleton, main claim, non-claims, section outline, results storyboard, and submission blockers.

Files changed:

- `docs/manuscript/MANUSCRIPT_SPINE.md`

Remaining caveat:

The spine is still a drafting architecture. Baselines, Exp13.1, uncertainty, final figures, novelty assessment import, and citations remain blockers.

### Synthesis docs

Action taken:

Updated synthesis docs to avoid stale root/top-level experiment language, align with the new README/manuscript spine/baseline/reproducibility docs, and state an operational order after P0/P1 cleanup.

Files changed:

- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/repo_audit/MISSING_ARTIFACTS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/repo_audit/P0_REMEDIATION_QA.md`

Remaining caveat:

Scientific blockers remain unchanged: Exp13.1, baselines, uncertainty, and final figures.

### Path verifier CI

Action taken:

Added a lightweight GitHub Actions workflow that checks out the repository, sets up Python, and runs `python scripts/verify_doc_source_paths.py` on pushes and pull requests.

Files changed:

- `.github/workflows/verify-doc-paths.yml`

Remaining caveat:

The workflow checks documentation paths only. It intentionally does not install experiment packages or run experiments.

## Remaining P1/P2 items

- Verify manuscript-critical Exp11/Exp12/Exp13 smoke or validation commands on a fresh checkout.
- Record expected runtimes and output manifests for manuscript-critical runs.
- Import the missing novelty assessment source artifact or keep it explicitly local verification pending.
- Implement Exp13.1 in a new future experiment directory under `experiments/`.
- Implement the external baseline suite in a new future experiment directory under `experiments/`.
- Add confidence intervals, effect sizes, and final reproducible figure scripts.
- Build the applied visual-state bridge only after Exp13.1 and baselines.

## Recommended next step

The repo is ready to proceed to Exp13.1 design and implementation, not to manuscript submission. The next local-agent task should be a conservative Exp13.1 design scaffold under a new experiment directory inside `experiments/`, with smoke/standard/full or equivalent profiles defined before any full run.
