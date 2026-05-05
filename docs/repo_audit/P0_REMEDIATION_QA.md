# P0 Remediation QA

## Summary

QA result: pass.

The P0 remediation appears to have fixed the repository-structure and docs-CSV issues it targeted. Active documentation source paths now resolve through `experiments/...`, docs CSVs are plain text rather than Git LFS pointers, and the path verifier exists and passes with zero missing active paths.

The remaining unresolved paths are explicitly marked as planned/future or local-verification-pending. They are not active evidence paths. I found no evidence that scientific claims were strengthened during the cleanup; the manuscript claim rows retain their statuses and caveats, while the remediation diff is dominated by path-prefix changes and docs-CSV/source-data handling.

## Pass/fail checklist

| Check | Result | Evidence | Notes |
|---|---|---|---|
| 1. Active docs source paths now use `experiments/...` and resolve locally. | Pass | `python scripts/verify_doc_source_paths.py` scanned 58 files, found 4,266 OK paths and 0 missing active paths. | Source paths in `CLAIMS_AND_EVIDENCE.md`, `FIGURE_PLAN.md`, `PUBLICATION_READINESS.md`, and `REPRODUCIBILITY_AUDIT.md` use the current prefix. |
| 2. No active manuscript/evidence/source path points to old root-level experiment directories. | Pass | `rg --pcre2` found only three legacy-root mentions: `AGENTS.md`, `PATH_VERIFICATION_REPORT.md`, and `P0_REMEDIATION_REPORT.md`. | All three are explicitly stale-path examples in "do not cite" or verification-report text, not active source paths. |
| 3. Path verifier exists and has been run. | Pass | `scripts/verify_doc_source_paths.py` exists and was run during this QA. | `PATH_VERIFICATION_REPORT.md` also records the same verifier command. |
| 4. Path verifier passes or clearly reports only intentional/future/local-verification-pending missing paths. | Pass with caveat | Verifier output: 0 missing active paths, 8 planned/future skips, 27 local-verification-pending skips. | Skips include future Exp13.1 docs and missing novelty-assessment artifact `Pasted text.txt`, both explicitly labeled. |
| 5. `docs/**/*.csv` files are not Git LFS pointer files. | Pass | `rg -n "version https://git-lfs.github.com/spec/v1\|oid sha256:\|size [0-9]+" docs --glob "*.csv"` returned no matches. First-line spot checks show CSV headers. | Checked all docs CSVs currently present under `docs/`. |
| 6. `.gitattributes` keeps docs CSVs as plain text. | Pass | `.gitattributes` contains `docs/**/*.csv text eol=lf`. `git check-attr` reports docs CSVs as `text: set` and `eol: lf`. | Experiment analysis/run CSVs remain LFS intentionally. |
| 7. `AGENTS.md` no longer tells agents to create top-level experiment directories. | Pass | `AGENTS.md` says all experiment directories must live under `experiments/` and gives planned naming examples such as `experiments/expNN_descriptive_name/`. | No conflicting root-level experiment instruction found. |
| 8. `REPRODUCIBILITY_AUDIT.md` commands use `experiments/...`. | Pass | The audit command table uses paths such as `python ./experiments/experiment12_capacity_generalization/...` and expected outputs under `experiments/...`. | The recommended generic pattern uses `.\start_exp<N>.ps1` as an example, not an active per-experiment command. |
| 9. `README.md` gives a useful entry point into the repo. | Pass | README now explains repo purpose, detected experiment directories, manuscript status, where to start, path-verifier command, non-claims, and working rules. | It is concise but sufficient for orientation. |
| 10. No scientific claims were strengthened during this cleanup. | Pass | `git diff HEAD^ HEAD -- docs/manuscript/CLAIMS_AND_EVIDENCE.md` shows claim rows changed by adding `experiments/` prefixes to artifact paths while retaining claim text, statuses, caveats, and follow-ups. | README was shortened and retains benchmark-specific caveats and explicit non-claims. |

## Remaining problems

No blocking P0 remediation problems found.

- Severity: non-blocking known gap.
- File: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/repo_audit/PATH_VERIFICATION_REPORT.md`; related manuscript/audit docs.
- Issue: The novelty-assessment artifact `Pasted text.txt` remains missing/local verification pending.
- Recommended fix: Import the novelty assessment as a local artifact and update the affected source references before manuscript-readiness handoff.

- Severity: non-blocking planned work.
- File: `docs/repo_audit/PATH_VERIFICATION_REPORT.md`; `docs/manuscript/MANUSCRIPT_TODO.md`.
- Issue: Exp13.1 and related future docs are intentionally not present yet.
- Recommended fix: Create a new self-contained future `experiments/exp13_1_publication_hardening/` or similarly named directory when starting Exp13.1, then update docs after the run.

## Final recommendation

Ready for the next step: Exp13.1 design/run.

No additional cleanup pass is required for the verified P0 remediation items. Keep the local-verification-pending novelty artifact and future Exp13.1 docs on the follow-up list, but they do not block moving into the Exp13.1 protocol.
