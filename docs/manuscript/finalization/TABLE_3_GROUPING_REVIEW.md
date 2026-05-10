# Table 3 Grouping / Effect-Size Review

Date: 2026-05-10

Status: started; Table 3 remains a candidate statistical-support artifact, not a final manuscript statistics table.

This review follows the human-decision integration pass and the current `docs/manuscript/finalization/NEXT_STEP_PROMPT.md` instruction to begin Table 3 grouping/effect-size review after the human decisions were recorded.

## Inputs reviewed

- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`
- `docs/manuscript/finalization/HUMAN_DECISION_INTEGRATION_STATUS.md`
- `docs/manuscript/closest_prior_art_table.md`

No experiments were rerun. No effect sizes, confidence intervals, or statistical comparisons were invented.

## Overall judgment

Table 3 is useful as a candidate statistical map, but it is not yet safe as a final manuscript statistics table.

The core issue is not that the table is wrong; it is that the table currently mixes descriptive rows, aggregate-normal confidence intervals, ceiling rows, budget slices, symbolic context-selection sweeps, and baseline/control rows without enough explicit grouping columns to make every row manuscript-final.

Before Table 3 is cited as final manuscript statistics, it should be regenerated or manually reviewed with explicit comparison families and slice-defining columns.

## Rows that are safe for manuscript use now, with caveats

### C1-C4 / Exp13.1 core ablation rows

Safe use: descriptive support for Figure 2 and qualitative claims about the tested symbolic model family.

Allowed statement type:

- Full model reaches ceiling on the reported route-table and composition metrics in the selected hard slice.
- No-context binding, no-recurrence-at-eval, and no-structural-plasticity variants dissociate route-table access, context separation, and multi-step execution.

Caveat:

- The table reports aggregate/normal-approximate intervals and `nan` effect sizes in the displayed candidate rows.
- These rows should not be used for final effect-size wording until seed-level grouping and exact comparison definitions are reviewed.
- The claim must remain benchmark/model-family-specific because Exp15 transition MLP variants solve the clean supplied-context slice.

### C5 / Exp12 clean supplied-context capacity rows

Safe use: descriptive ceiling-limited scaling through the tested world counts.

Allowed statement type:

- Clean supplied-context full-model performance reaches ceiling across the tested world counts in the selected route-length slice.

Caveat:

- These are ceiling rows and should not be presented as evidence for a fitted capacity law.
- The current candidate table repeats rows without surfacing enough slice-defining columns, so the manuscript should avoid row-by-row final statistics until the grouping is made explicit.

### C6 / Exp13 finite-budget global degradation rows

Safe use: descriptive evidence for observed finite-budget degradation.

Allowed statement type:

- Under finite structural budget pressure, composition accuracy degrades at severe budget ratios and recovers at exact/surplus budget levels in the tested setting.

Caveat:

- No fitted capacity law is present.
- Exact budget-ratio comparisons should not be treated as final until the selected budget levels and seed-level comparison groups are reviewed.

### C13 / Exp14 symbolic transition-cue context-selection rows

Safe use: narrow evidence that symbolic transition cues can select the active world/context before route execution in clean or lightly corrupted slices.

Allowed statement type:

- The CIRM latent selector reaches ceiling or near-ceiling in clean symbolic cue-selection slices, while random/shared no-context controls expose the selection boundary.

Caveat:

- Rows need explicit `cue_count`, `corruption_rate`, and variant grouping before final manuscript statistics are cited.
- The claim remains symbolic transition-cue selection only, not raw sensory latent-world discovery.
- Oracle context-gated lookup remains an upper-bound control.

## Rows or comparisons that are not yet final

### C7 local-vs-global pressure

Not final as a main statistical comparison.

Reason:

- The statistical-readiness map identifies local-vs-global pressure as boundary/supplement only and notes missing paired seed-level local/global grouping.
- Table 3 can support a descriptive figure caption but should not elevate C7 into a standalone main claim.

Required action:

- Add paired seed-level local-vs-global comparison rows before promoting C7 beyond caveated boundary wording.

### Exp14 repeated rows

Not final as currently displayed.

Reason:

- Table 3 includes repeated-looking Exp14 rows because the rendered table does not expose all slice-defining fields needed to disambiguate cue count, corruption rate, and possibly route/world settings.

Required action:

- Regenerate or revise Table 3 with explicit cue-count/corruption-rate columns and selected hard-slice rows.

### Effect sizes in displayed Table 3

Not final.

Reason:

- Many displayed effect-size cells are `nan`.
- Existing effect-size artifacts may exist for Exp13.2, Exp14, and Exp15, but Table 3 currently does not present a final human-approved grouping.

Required action:

- Define comparison families before inserting final effect sizes into the manuscript.

### Exp15 replay collapse

Not a scientific claim.

Reason:

- The statistical-readiness map marks replay collapse as non-claim pending audit.

Required action:

- Audit implementation/training regime before any scientific interpretation.

## Recommended Table 3 regeneration schema

A final Table 3 should include enough columns to prevent ambiguity:

- `claim_id`
- `experiment_id`
- `run_id`
- `comparison_family`
- `metric`
- `variant`
- `comparator`
- `world_count`
- `route_length`
- `budget_mode`
- `budget_ratio`
- `cue_count`
- `corruption_rate`
- `profile_or_slice`
- `mean`
- `ci_low`
- `ci_high`
- `effect_size`
- `effect_size_type`
- `seed_count`
- `final_status`
- `allowed_manuscript_wording`
- `caveat`
- `source_paths`

## Recommended final grouping families

| Grouping family | Rows to include | Final status |
|---|---|---|
| Figure 2 core ablation | Exp13.1 full model, no structural plasticity, no recurrence at eval, no context binding; route-table and composition metrics. | Candidate-safe for descriptive use; effect sizes pending. |
| Figure 3 clean scaling | Exp12 full context-separated memory across explicit world counts for route-table/composition metrics. | Candidate-safe as ceiling-limited descriptive evidence. |
| Figure 4 finite budget | Exp13 global budget degradation rows at explicitly named budget ratios. | Candidate-safe as observed degradation; no fitted law. |
| Figure 4 local/global pressure | Exp13 local vs global rows only if paired seed-level grouping is added. | Boundary/supplement until paired analysis exists. |
| Figure 5 symbolic context selection | Exp14 clean/corrupted cue-selection rows with explicit cue count and corruption rate. | Candidate-safe after row disambiguation. |
| Table 4 neural comparator | Keep separate from Table 3 unless a unified statistical appendix is intentionally created. | Compact main-text Table 4 remains the clearer manuscript artifact. |

## Next action

Do not cite Table 3 as final manuscript statistics yet.

The next concrete action should be either:

1. regenerate Table 3 with explicit grouping/slice columns and final-status flags; or
2. manually create a compact main-text Table 3 with only final-safe descriptive rows, moving the full statistical map to supplement.
