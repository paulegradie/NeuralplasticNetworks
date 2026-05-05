# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## P0 - Required Before Manuscript Submission

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Complete Exp13.1 publication-hardening audit. | Exp13 has metric and ablation caveats that reviewers can attack. | Exp13, planned Exp13.1 | `docs/threads/experiment12to13_export.md` | New top-level Exp13.1 directory and `docs/experiments/exp13_1_summary.md` or equivalent. |
| Add external baseline suite. | Current evidence is mostly internal ablations. | Exp8-Exp13 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | `docs/manuscript/BASELINE_REQUIREMENTS.md`; baseline experiment directory. |
| Add seed-level confidence intervals and effect sizes. | Many claims cite mean summaries without manuscript-grade uncertainty. | Exp8-Exp13 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | Updated analysis summaries and figure scripts. |
| Fix holdout metrics. | Exp13 route-table accuracy must split all, seen, and unseen primitives. | Exp13, planned Exp13.1 | `docs/threads/experiment12to13_export.md` | `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and split composition CSVs. |
| Rename or rerun no-context-binding ablation. | Exp13 `no_context_binding` may be weak-binding/oracle-clean rather than a pure ablation. | Exp13, planned Exp13.1 | `docs/threads/experiment12to13_export.md` | Clean variant definitions and updated evidence rows. |
| Import novelty assessment as local artifact and source baseline requirement claims. | C12 is currently thread-derived because `Pasted text.txt` is missing locally. | Manuscript-level | `docs/threads/experiment12to13_export.md` | `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` or `docs/repo_audit/source_imports/NOVELTY_ASSESSMENT.md`, then update C12 and baseline requirements. |
| Consolidate all analysis artifacts and thread digests. | Manuscript claims must remain traceable to source paths. | All | `docs/threads/experiment12to13_export.md` | Updated `docs/repo_audit/ARTIFACT_INDEX.csv`, summaries, and conflict log. |
| Create final paper figures from reproducible scripts. | Current figure plan cites generated plots, but final panels need controlled scripts. | Exp11-Exp13 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | `docs/manuscript/FIGURE_PLAN.md` plus figure scripts. |

## P1 - Strongly Recommended

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Add stochastic context corruption. | Exp13 adversarial corruption is a hard threshold, not a graded noise model. | Exp13.1 | `docs/threads/experiment12to13_export.md` | Context corruption summary and plots. |
| Run consolidation dose-response. | Consolidation is currently a preliminary stability-plasticity bias claim. | Exp13.1 | `docs/threads/experiment12to13_export.md` | Dose-response CSV, retention heatmaps, and caveated claim update. |
| Fit capacity laws. | Exp13 shows observed degradation curves but no fitted capacity model. | Exp13.1 | `docs/threads/experiment12to13_export.md` | Capacity-law summaries and figure panel. |
| Upgrade local-vs-global comparison. | The current Exp13 comparison is docs-only and aggregate-level. | Exp13.1 | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `docs/threads/experiment12to13_export.md` | Paired seed-level local-vs-global table with confidence intervals. |
| Design latent world inference. | Oracle world labels limit the current manuscript. | Future Exp14 | `docs/threads/experiment12to13_export.md` | Experiment 14 design doc after P0 work. |
| Build applied visual-state bridge. | Continuous/noisy input is preliminary and not end-to-end perception. | Future Exp14 | `docs/threads/experiment12to13_export.md` | Applied bridge experiment plan. |

## P2 - Future Work

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | Future | `docs/threads/experiment12to13_export.md` | New experiment directory. |
| Learned perceptual encoders. | Test whether route memory can operate downstream of learned perception. | Future | `docs/threads/experiment12to13_export.md` | Applied bridge experiment. |
| Larger-scale continual learning variants. | Determine whether mechanisms survive larger workloads. | Future | `docs/threads/experiment12to13_export.md` | Scaling design and baseline comparison. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | Future | `docs/threads/experiment12to13_export.md` | Theory note or discussion section. |
