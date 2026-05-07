# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## Current Next Operational Priority

Freeze the first-manuscript claim set and decide figure/table placement for Exp13.2 and Exp14. Do not default to a new experiment before documentation, uncertainty, prior-art, and final-figure hardening are complete.

Claim: Exp13.2 partially resolves the symbolic/algorithmic baseline blocker, and Exp14 partially reduces the oracle-context limitation by showing symbolic context selection from transition cues.

Evidence: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md` reports PASS 28, WARN 0, FAIL 0. `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md` reports PASS 27, WARN 0, FAIL 0.

Caveat: Exp13.2 is not a full neural baseline suite or prior-art import, and Exp14 is symbolic transition-cue selection rather than raw sensory latent-world discovery. Final figures, CI/effect-size tables, command verification, and license/citation metadata remain open.

Source path: `docs/threads/experiment13_2_analysis_digest.md`; `docs/threads/experiment14_analysis_digest.md`; `docs/experiments/exp13_2_summary.md`; `docs/experiments/exp14_summary.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`

## P0 - Required Before Manuscript Draft

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Create and review `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`. | The first manuscript needs a frozen main/supplement/drop/future-work claim set before prose drafting. | Manuscript-level | `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/manuscript/FIGURE_PLAN.md` | Frozen claim set with Claim -> Evidence -> Caveat -> Source path entries. |
| Decide whether Exp14 C13 is main text or supplement. | Exp14 is promising symbolic context-selection evidence, but final manuscript placement is unresolved. | Exp14 | `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/manuscript/FIGURE_PLAN.md` | Main/supplement decision plus final figure/source-data requirements. |
| Decide whether Exp13.2 baseline suite is main text, supplement, or table-only. | Exp13.2 narrows the clean supplied-context claim and should be visible somewhere in the manuscript. | Exp13.2 | `docs/threads/experiment13_2_analysis_digest.md`; `docs/experiments/exp13_2_summary.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md` | Baseline placement decision and final table/figure plan. |
| Add source-data/statistical readiness rows for retained Exp14 panels. | C13 is now a claim but source-data readiness needs to identify its authoritative sources and final-figure gaps. | Exp14 | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_effect_sizes.csv` | Updated source-data and statistical-readiness manifests. |

## P1 - Required Before Submission

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Decide whether additional neural baselines are required beyond Exp13.2. | Exp13.2 partially resolves C12 with symbolic/algorithmic baselines, but stronger venues may still require neural comparators. | Exp13.2 and manuscript-level | `docs/threads/experiment13_2_analysis_digest.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md` | Venue-specific baseline decision and, if needed, a new experiment plan. |
| Import novelty/prior-art assessment as a local artifact. | C12 still depends on prior-art positioning and the thread-referenced novelty source is missing locally. | Manuscript-level | `docs/threads/experiment12to13_export.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md` | Future `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` or equivalent cited artifact. |
| Add seed-level confidence intervals and effect sizes. | Many claims cite aggregate means without manuscript-grade uncertainty. | Exp11-Exp14 | `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `scripts/compute_seed_metric_summary.py` | Human-reviewed CI/effect-size tables tied to explicit claim groupings. |
| Create final paper figures from reproducible scripts. | Current figure plan cites generated plots, not final panel scripts. | Exp11-Exp14 | `docs/manuscript/FIGURE_PLAN.md`; `docs/source_data/SOURCE_DATA_MANIFEST.csv` | Figure scripts plus source-data manifests for every retained panel. |
| Verify manuscript-critical run commands. | Repository readiness requires commands that a new researcher can actually run. | Exp11-Exp14 | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Verified smoke/validation/full command log with runtime and expected outputs. |
| Fix holdout metrics if retaining Exp13 holdout claims centrally. | Exp13 route-table accuracy must split all, seen, and unseen primitives. | Exp13 or successor analysis | `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | `route_table_accuracy_all`, `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and matching composition splits. |
| Audit/rerun Exp13.1 lesion diagnostic before citing positive lesion evidence. | Targeted critical-edge lesions were less damaging than random count-matched lesions. | Exp13.1 | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md` | Corrected lesion diagnostic or explicit decision not to cite lesion evidence. |
| Add license and citation metadata. | Public reuse and citation terms are unclear. | Repository-level | `README.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Human-chosen `LICENSE` and `CITATION.cff`. |

## P2 - Useful Polish

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Add stochastic context corruption beyond wrong-world injection. | Current context corruption evidence supports identity/selection sensitivity, not generic stochastic robustness. | Exp13.1 or successor | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | Stochastic corruption table with top-1 world selection, margins, and composition if robustness is claimed. |
| Refine consolidation analysis beyond accuracy rescue. | Exp13.1 did not show constrained-budget accuracy rescue from consolidation strength. | Exp13.1 or successor | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Margin/robustness summaries or a caveated decision to keep consolidation supplementary. |
| Fit capacity laws. | Exp13 shows observed degradation curves but no fitted capacity model. | Exp13/Exp13.1 | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Capacity-law summaries and final figure panel if retained. |
| Upgrade local-vs-global comparison. | The current Exp13 comparison is docs-only and aggregate-level. | Exp13/Exp13.1 | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | Paired seed-level local-vs-global table with confidence intervals. |
| Maintain artifact and evidence indexes as outputs change. | Manuscript claims must remain traceable to source paths. | All future runs | `docs/repo_audit/ARTIFACT_INDEX.csv`; `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv` | Updated indexes after any new run or source-data import. |

## Future Work Only

| TODO | Reason | Related experiment | Source path | Target output |
|---|---|---|---|---|
| Richer non-symbolic latent-world inference. | Exp14 covers symbolic transition-cue selection but not raw sensory or learned perceptual context discovery. | Future successor | `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/threads/experiment14_analysis_digest.md` | New experiment directory only if the manuscript needs a stronger non-symbolic bridge. |
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | Future | `docs/threads/experiment12to13_export.md` | Applied bridge experiment. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | Future | `docs/theory/BIOLOGICAL_FRAMING.md` | Theory note or discussion section with citations. |

## Completed Repository-Readiness Work

| Completed item | Result | Source path |
|---|---|---|
| Path verifier and CI workflow. | Active documentation paths can be checked locally and in GitHub Actions. | `scripts/verify_doc_source_paths.py`; `.github/workflows/verify-doc-paths.yml` |
| Exp13.1 publication-hardening import. | Exp13.1 artifacts are documented with caveats; lesion diagnostic remains non-positive. | `docs/experiments/exp13_1_summary.md`; `docs/repo_audit/EXP13_1_ANALYSIS_IMPORT_REPORT.md` |
| Exp13.2 baseline-suite import. | Exp13.2 symbolic/algorithmic baselines are documented; C12 is partially satisfied but neural/prior-art decisions remain open. | `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment13_2_analysis_digest.md` |
| Exp14 latent-context digest import. | Exp14 full, validation, and smoke runs are documented; C13 is added as promising symbolic context-selection evidence. | `docs/experiments/exp14_summary.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`; `docs/threads/experiment14_analysis_digest.md` |
