# Manuscript Finalization

Purpose: collect the final manuscript-readiness plan, working checklist, status reports, and handoff prompts for the Context-Indexed Route Memory manuscript.

This folder is the operating area for the finalization phase after `MANUSCRIPT_V2.md`, Exp13.2 import, Exp14 import, Exp15 import, Analysis Pass 15A retained-claim hardening, citation/prior-art audit, checked citation-ledger pass, human decision capture, Section 2.7 closest-prior-art prose integration, and the compact Table 3 split.

## Files

- [`MANUSCRIPT_FINALIZATION_PLAN.md`](MANUSCRIPT_FINALIZATION_PLAN.md) - limitation-by-limitation plan for closing or explicitly retaining reviewer-risk items.
- [`FINALIZATION_CHECKLIST.md`](FINALIZATION_CHECKLIST.md) - practical checklist for tracking manuscript finalization work.
- [`NEXT_STEP_PROMPT.md`](NEXT_STEP_PROMPT.md) - current agent-ready prompt for documentation/source-path verification plus manuscript/caption alignment for the compact Table 3 path.
- [`HUMAN_DECISION_INTEGRATION_STATUS.md`](HUMAN_DECISION_INTEGRATION_STATUS.md) - record of human decisions for citation/export convention, closest-prior-art placement, and figure/table placement.
- [`TABLE_3_GROUPING_REVIEW.md`](TABLE_3_GROUPING_REVIEW.md) - record of the Option B compact Table 3 split and remaining caveats.
- [`CITATION_PRIOR_ART_INSERTION_REPORT.md`](CITATION_PRIOR_ART_INSERTION_REPORT.md) - report from the checked citation-ledger and closest-prior-art table creation pass.
- [`CITATION_LEDGER_INTEGRATION_STATUS.md`](CITATION_LEDGER_INTEGRATION_STATUS.md) - status of citation-ledger integration after the follow-up pass.
- [`NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md`](NEXT_STEP_PROMPT_AFTER_CITATION_LEDGER.md) - historical handoff prompt used after the citation-ledger pass; retained as an audit trail and superseded by `NEXT_STEP_PROMPT.md`.

## Current Finalization Posture

The first manuscript remains a controlled symbolic/mechanistic benchmark paper. `MANUSCRIPT_V2.md` has been captured, Exp15 is imported as completed minimal fixed-profile neural-comparator evidence, Table 4 is present as a compact source-data-backed comparator table, and `docs/manuscript/RETAINED_CLAIMS_STATISTICAL_HARDENING.md` records the post-15A retained claim posture.

The human-decision and Table 3 cleanup stages are no longer open blockers:

- `docs/manuscript/REFERENCES.md` remains the checked venue-neutral citation ledger until a target venue/convention is chosen.
- `docs/manuscript/closest_prior_art_table.md` remains the closest-prior-art companion artifact.
- Section 2.7 of `docs/manuscript/draft/MANUSCRIPT_V2.md` contains closest-prior-art prose derived from that companion artifact.
- `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md` records the citation/export, closest-prior-art, and figure/table placement decisions.
- `docs/manuscript/finalization/TABLE_3_GROUPING_REVIEW.md` records the compact Table 3 outcome.
- `docs/manuscript/tables/table_03_compact_final_safe.md` and `docs/manuscript/source_data/table_03_compact_final_safe.csv` are the compact descriptive main-text Table 3 path.
- `docs/manuscript/tables/table_03_statistical_summary.md` and `.csv` remain detailed candidate/supplementary statistical-map artifacts, not final main-text inferential statistics.

Current retained V2 posture:

- Main scientific spine: C1, C2, C3, C4, C5, C6, and C13.
- Discussion/table baseline claim: C12.
- Boundary or supplement only: C7, C8, C10, and C11.
- Out of the main claim set or non-claims: C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad CIRM-over-neural claims, raw sensory latent-world discovery, and biological validation.

## Current Next Action

Use `NEXT_STEP_PROMPT.md` for the next phase.

The next step is not another citation-audit pass, human-decision checkpoint, Analysis Pass 15A, Table 3 grouping decision, or new experiment. Those stages have already been recorded.

The current blocker is:

1. Run `python scripts/verify_doc_source_paths.py` in a clean checkout or CI-capable environment.
2. If it passes, record the pass in the relevant finalization/readiness docs.
3. If it cannot run, document the exact reason and do not guess.
4. If it fails, fix broken active paths only; do not change scientific claims.
5. Polish manuscript/caption prose so compact descriptive Table 3 is the main-text Table 3 path and the detailed generated statistical map remains candidate/supplementary support.

Do not start new experiments by default.
