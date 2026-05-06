# P2 Remediation Report

## Summary

This P2 pass added navigation, terminology, historical-vs-active separation, issue/roadmap scaffolding, and light summary/TODO polish without modifying experiment logic, rerunning experiments, implementing Exp13.1, implementing baselines, deleting generated artifacts, or rewriting thread exports.

Path verifier status after remediation: pass with zero missing active paths.

## Initial inspection

What appeared already clean:

- P0 and P1 remediation reports and QA agreed that active source paths now use the `experiments/...` structure.
- `README.md` and `AGENTS.md` already described the current experiment-directory rules and path-verification workflow.
- Manuscript-facing evidence docs already preserved the core discipline: Claim -> Evidence -> Caveat -> Source path.
- The active readiness stance remained conservative: promising internal evidence, but not submission-ready until Exp13.1, external baselines, uncertainty reporting, and final figures are complete.

Minor inconsistencies remaining at the start of P2:

- `docs/README.md` was missing, so the documentation tree lacked a single navigation index.
- `docs/theory/GLOSSARY.md` was still a TODO scaffold.
- Historical, supporting, and manuscript-critical experiments were described across several files but not separated in one dedicated document.
- Exp1-Exp10 summary files used older evidence-status wording that was less clear than the Exp11-Exp13 blocks.
- P0/P1 repository-readiness completion was not summarized in one completed-work section in the active work queue.
- GitHub issue templates, a short roadmap, and a manuscript source-of-truth note were not present.

What this pass addressed:

- Added a documentation index for future readers and local agents.
- Replaced the glossary scaffold with conservative project-specific definitions.
- Added a historical-vs-active experiment separation document and linked it from the registry.
- Lightly normalized experiment-summary evidence status blocks and manuscript roles.
- Cleaned up TODO navigation so Exp13.1 and baselines remain the next operational priorities.
- Added simple issue templates, a short roadmap, and a source-of-truth note.
- Ran the documentation path verifier and recorded the result.

What this pass deliberately deferred:

- Exp13.1 design, implementation, or runs.
- External baseline implementation.
- Confidence intervals, effect sizes, final figure scripts, and new manuscript results.
- Novelty assessment import if the missing source artifact is still absent.
- Rewriting historical thread exports or generated experiment artifacts.

## Items addressed

### Docs navigation

Action taken:

Created a docs index with a recommended reading order, document tables, thread-export guidance, and future-edit rules.

Files changed:

- `docs/README.md`
- `README.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`

Remaining caveat:

The index is a navigation aid. Canonical evidence still lives in `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.

### Glossary

Action taken:

Replaced the scaffold glossary with project-local definitions for recurring route-memory, context, capacity, holdout, baseline, and ablation terms. Each term includes definition, plain-language interpretation, manuscript usage, caveat, and related docs.

Files changed:

- `docs/theory/GLOSSARY.md`

Remaining caveat:

Definitions are project-local unless a later prior-art pass documents broader literature usage.

### Historical-vs-active evidence separation

Action taken:

Added a tiered historical/supporting/manuscript-critical experiment guide and linked it from the experiment registry.

Files changed:

- `docs/experiments/HISTORICAL_EXPERIMENTS.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`

Remaining caveat:

Exp1-Exp10 can still support background or supplementary context, but they should not be upgraded to central manuscript evidence without renewed validation.

### Experiment summary polish

Action taken:

Lightly normalized evidence-status blocks in Exp1-Exp13 summaries. Exp1-Exp6 are marked historical/exploratory, Exp7-Exp10 mechanism-building/supporting, and Exp11-Exp13 manuscript-critical but not publication-validated.

Files changed:

- `docs/experiments/exp1_summary.md`
- `docs/experiments/exp2_summary.md`
- `docs/experiments/exp3_summary.md`
- `docs/experiments/exp4_summary.md`
- `docs/experiments/exp5_summary.md`
- `docs/experiments/exp6_summary.md`
- `docs/experiments/exp7_summary.md`
- `docs/experiments/exp8_summary.md`
- `docs/experiments/exp9_summary.md`
- `docs/experiments/exp10_summary.md`
- `docs/experiments/exp11_summary.md`
- `docs/experiments/exp12_summary.md`
- `docs/experiments/exp13_summary.md`

Remaining caveat:

Long imported summary bodies still contain unresolved TODOs where human/manuscript validation is genuinely pending.

### TODO hygiene

Action taken:

Added a current next-operational-priority section, kept scientific P0 blockers active, moved ongoing artifact-index maintenance out of the submission-critical P0 table, and grouped completed P0/P1 repository-readiness work.

Files changed:

- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`

Remaining caveat:

Open scientific blockers remain unchanged: Exp13.1, external baselines, uncertainty reporting, final figures, and novelty import.

### Issue templates / roadmap

Action taken:

Added simple issue templates for experiment, manuscript, repo hygiene, and baseline tasks. Added a short roadmap that points back to the canonical work queue instead of duplicating it.

Files changed:

- `.github/ISSUE_TEMPLATE/experiment_task.md`
- `.github/ISSUE_TEMPLATE/manuscript_task.md`
- `.github/ISSUE_TEMPLATE/repo_hygiene_task.md`
- `.github/ISSUE_TEMPLATE/baseline_task.md`
- `docs/synthesis/ROADMAP.md`

Remaining caveat:

Templates and roadmap are handoff scaffolds, not evidence.

### Source-of-truth docs

Action taken:

Added a manuscript source-of-truth note that explains which docs win when artifacts, evidence maps, limitations, generated reports, and thread exports disagree.

Files changed:

- `docs/manuscript/SOURCE_OF_TRUTH.md`

Remaining caveat:

If future work changes canonical ownership, this file should be updated in the same pass.

### Style cleanup

Action taken:

Kept changes light: normalized status-label availability, root-relative docs paths in `docs/README.md`, and summary role wording. No generated reports or thread exports were rewritten.

Files changed:

- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/README.md`
- experiment summary files listed above

Remaining caveat:

No markdown/table linter was found locally, so formatting validation was limited to review plus path verification.

## Verification

- Path verifier command: `python scripts/verify_doc_source_paths.py`
- Path verifier result: pass; 66 files scanned, 4536 OK paths, 0 missing active paths, 17 skipped planned/future paths, 35 skipped local-verification-pending paths.
- Remaining missing paths, if any: none active. Known skipped items include planned Exp13.1/baseline paths and the missing/local-verification-pending novelty artifact `Pasted text.txt`.

Additional checks:

- Docs CSV LFS pointer scan: no matches for Git LFS pointer text under `docs/**/*.csv`.
- Stale old-root experiment path scan: only explicit "do not cite stale paths" examples remained.
- Thread exports were not edited.
- Experiment logic was not edited and experiments were not rerun.

## Deferred items

List:

- Exp13.1
- external baselines
- novelty assessment import if still missing
- manuscript draft
- final figures
- applied bridge

## Final recommendation

Ready for Exp13.1 design/implementation: yes, as a new experiment directory under `experiments/`.

Ready for baseline suite planning: yes, using `docs/manuscript/BASELINE_REQUIREMENTS.md` and the new issue template.

Ready for manuscript draft v0: partially. The repository is easier to navigate and ready for a conservative outline/prose scaffold, but a results-complete manuscript draft should wait for Exp13.1, external baselines, uncertainty reporting, final figures, and novelty import.
