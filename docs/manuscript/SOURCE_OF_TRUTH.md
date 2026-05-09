# Source of Truth

Purpose: Explain which documents are authoritative when repository docs disagree.

## Canonical docs

- Claim freeze for the first manuscript: `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- Post-Exp15 claim narrowing: `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- Current manuscript draft: `docs/manuscript/draft/MANUSCRIPT_V2.md`
- Claims: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- Figures: `docs/manuscript/FIGURE_PLAN.md`
- Submission readiness: `docs/synthesis/PUBLICATION_READINESS.md`
- Experiment list: `docs/experiments/EXPERIMENT_REGISTRY.md`
- Next work: `docs/manuscript/finalization/NEXT_STEP_PROMPT.md`; `docs/manuscript/MANUSCRIPT_TODO.md`
- Reproducibility: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

## Non-authoritative docs

- Thread exports are source material, not final claims.
- Generated reports are local artifacts, not manuscript prose.
- Historical experiment notes may contain outdated framing.
- Roadmaps and issue templates are handoff aids, not evidence.

## Rule

If there is a conflict:

1. Generated artifact/source data wins for numeric claims.
2. `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` wins for post-Exp15 narrowing when it is stricter than earlier claim-freeze language.
3. `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` wins for first-manuscript inclusion/exclusion decisions once present.
4. `docs/manuscript/CLAIMS_AND_EVIDENCE.md` wins for current claim wording outside the frozen first-manuscript subset and post-Exp15 addendum.
5. `docs/manuscript/LIMITATIONS_AND_THREATS.md` wins for caveats.
6. Thread exports are used only as historical context unless imported.

## Current Scope Note

The repository is now in a post-Exp15 and post-Manuscript-V2-capture finalization state. Exp13.2 has been imported as completed symbolic/algorithmic baseline-suite evidence, Exp14 has been imported as completed symbolic transition-cue context-selection evidence, and Exp15 has been imported as completed minimal fixed-profile neural-comparator evidence.

`docs/manuscript/draft/MANUSCRIPT_V2.md` has been captured. `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` narrows the first-manuscript claim posture after Exp15, and `docs/manuscript/tables/table_04_exp15_neural_comparator.md` / `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` capture the V2 Exp15 compact comparator table.

This does **not** make the repository submission-ready. Remaining active work is retained-claim selection, manuscript-grade uncertainty/effect-size tables, final source-data-backed figure/table review, prior-art/novelty import, fresh command verification, and license/citation metadata.

Use `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` for the next phase: Analysis Pass 15A, retained-claim and statistical hardening.
