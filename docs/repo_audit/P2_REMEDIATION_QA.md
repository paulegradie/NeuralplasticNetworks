# P2 Remediation QA

## Summary

The P2 remediation is ready to proceed to Exp13.1 design/implementation. The reviewed docs now provide a more navigable handoff, preserve the separation between historical/supporting experiments and manuscript-critical evidence, keep Exp13.1 as the next operational priority, and continue to mark baselines, uncertainty, final figures, and novelty import as unfinished scientific blockers.

Path verification passes with no missing active paths. The remaining skipped paths are intentionally marked planned/future or local-verification-pending. I found no active stale root-level experiment source paths, no docs CSV Git LFS pointer files, and no thread-export rewrites.

## Checklist

| Check | Result | Evidence | Notes |
|---|---|---|---|
| 1. `docs/README.md` gives a useful navigation index. | Pass | `docs/README.md` has a start-here sequence, manuscript-doc table, experiment-doc table, repo-audit table, theory-doc table, thread-import guidance, and future-edit rules. | Useful for both new humans and local agents. |
| 2. Glossary definitions are helpful, conservative, and not over-biological. | Pass | `docs/theory/GLOSSARY.md` says definitions are project-local, warns against treating route field as a standard biological construct, marks structural plasticity as benchmark-specific rather than biological necessity, and keeps latent world inference future-only. | The glossary is longer, but mostly disciplined and caveated. |
| 3. Historical vs manuscript-critical experiments are clearly separated. | Pass | `docs/experiments/HISTORICAL_EXPERIMENTS.md` defines Tier A Exp11-Exp13 plus planned Exp13.1, Tier B Exp7-Exp10, and Tier C Exp1-Exp6. | Separation is explicit and actionable. |
| 4. Experiment summaries are lightly cleaned but not rewritten into unsupported claims. | Pass | `git diff --unified=1 -- docs/experiments/exp*_summary.md` shows evidence-classification/status edits and additional "not publication-validated" caveats, not broad claim rewrites. | Exp1-Exp6 are historical/exploratory, Exp7-Exp10 supporting, Exp11-Exp13 manuscript-critical but not submission-ready. |
| 5. TODOs distinguish completed repo hygiene from active scientific blockers. | Pass | `docs/manuscript/MANUSCRIPT_TODO.md` has "Current Next Operational Priority", P0/P1/P2 open work, and "Completed Repository-Readiness Work". | Completed hygiene is separated from active manuscript blockers. |
| 6. Exp13.1 remains the next operational priority. | Pass | `docs/manuscript/MANUSCRIPT_TODO.md` says to start Exp13.1 under `experiments/`; `docs/synthesis/NEXT_EXPERIMENTS.md` lists Exp13.1 design and metric cleanup before external baselines. | `docs/synthesis/ROADMAP.md` also lists Exp13.1 under Now. |
| 7. Baselines remain required and planned, not claimed as completed. | Pass | `docs/manuscript/BASELINE_REQUIREMENTS.md` says it is a planning document, all rows are planned until implemented/run/analyzed/linked, and baseline results are absent; `docs/synthesis/PUBLICATION_READINESS.md` lists external baseline evidence as absent. | `docs/synthesis/ROADMAP.md` says planned work is not complete. |
| 8. Optional issue templates are useful and not overcomplicated. | Pass with note | `.github/ISSUE_TEMPLATE/` contains baseline, experiment, manuscript, and repo-hygiene templates with goal, evidence/source paths, acceptance criteria, non-goals, and validation checklists. | They are simple. They do not include YAML chooser metadata, which is acceptable for current repo-local handoff use. |
| 9. `SOURCE_OF_TRUTH.md` correctly identifies canonical docs. | Pass | `docs/manuscript/SOURCE_OF_TRUTH.md` names canonical docs for claims, figures, submission readiness, experiment list, next work, and reproducibility, and says artifacts win for numeric claims. | It also correctly treats thread exports, generated reports, roadmaps, and issue templates as non-authoritative. |
| 10. Path verifier passes or only reports intentional/pending paths. | Pass | `python scripts/verify_doc_source_paths.py` reported 67 files scanned, 4555 OK paths, 0 missing active paths, 17 skipped planned/future paths, and 35 skipped local-verification-pending paths after this QA report was added. | Skips include planned Exp13.1/baseline paths and missing novelty artifact references explicitly marked pending. |
| 11. No active docs use stale root-level experiment paths. | Pass | `rg --pcre2` for root-level `experiment.../` paths outside `docs/threads/**` only found explicit stale-path examples in `AGENTS.md`, `docs/repo_audit/P0_REMEDIATION_REPORT.md`, and `docs/repo_audit/PATH_VERIFICATION_REPORT.md`. | These are "do not cite stale paths" examples, not active evidence paths. |
| 12. No docs CSVs are Git LFS pointer files. | Pass | `rg -n "version https://git-lfs.github.com/spec/v1|oid sha256:|size [0-9]+" docs --glob "*.csv"` returned no matches; first-line inspection showed normal CSV headers. | CSV source-data and audit/index files are reviewable text. |
| 13. No scientific claims were strengthened. | Pass | P2 diffs add conservative status labels and caveats. `docs/manuscript/CLAIMS_AND_EVIDENCE.md` only added "Historical" and "Planned" status labels in the P2 diff. | Existing strong internal claims remain caveated by baselines, uncertainty, and benchmark-specific scope. |
| 14. Thread exports were not rewritten. | Pass | `git diff --name-only -- docs/threads` returned no files. | Thread exports remain historical source material. |
| 15. The repo is easier for a new agent/human to navigate. | Pass | README now links the docs index, source-of-truth note, and historical tiers; `docs/README.md`, `SOURCE_OF_TRUTH.md`, `HISTORICAL_EXPERIMENTS.md`, and `ROADMAP.md` provide layered navigation. | This is documentation readiness only, not new scientific evidence. |

## Problems found

No P0, P1, or P2 problems were found in the reviewed P2 remediation scope.

## Final recommendation

ready to proceed to Exp13.1 design/implementation
