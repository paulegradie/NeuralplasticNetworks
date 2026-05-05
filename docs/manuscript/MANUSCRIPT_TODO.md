# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## P0 - Required Before Manuscript Submission

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Complete Exp13.1 publication-hardening audit. | Exp13 has metric and ablation caveats that reviewers can attack. | Exp13, planned Exp13.1 | `docs/threads/experiment12to13_export.md` | Future new directory under `experiments/`, for example `experiments/exp13_1_publication_hardening/`, plus planned `docs/experiments/exp13_1_summary.md` or equivalent. |
| Add external baseline suite. | Current evidence is mostly internal ablations. | Exp8-Exp13 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md` | Baseline experiment directory under `experiments/`, summary CSVs, figures, and baseline evidence rows. |
| Add seed-level confidence intervals and effect sizes. | Many claims cite mean summaries without manuscript-grade uncertainty. | Exp8-Exp13 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | Updated analysis summaries and figure scripts. |
| Fix holdout metrics. | Exp13 route-table accuracy must split all, seen, and unseen primitives. | Exp13, planned Exp13.1 | `docs/threads/experiment12to13_export.md` | `route_table_accuracy_all`, `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and split composition CSVs. |
| Rename or rerun no-context-binding ablation. | Exp13 `no_context_binding` may be weak-binding/oracle-clean rather than a pure ablation. | Exp13, planned Exp13.1 | `docs/threads/experiment12to13_export.md` | Clean variant definitions and updated evidence rows. |
| Import novelty assessment as local artifact and source baseline requirement claims. | C12 is currently thread-derived because `Pasted text.txt` is missing locally. | Manuscript-level | `docs/threads/experiment12to13_export.md` | Local verification pending: future `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` or `docs/repo_audit/source_imports/NOVELTY_ASSESSMENT.md`, then update C12 and baseline requirements. |
| Consolidate all analysis artifacts and thread digests. | Manuscript claims must remain traceable to source paths. | All | `docs/threads/experiment12to13_export.md` | Updated `docs/repo_audit/ARTIFACT_INDEX.csv`, summaries, and conflict log as new artifacts are created. |
| Create final paper figures from reproducible scripts. | Current figure plan cites generated plots, but final panels need controlled scripts. | Exp11-Exp13, planned Exp13.1 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | `docs/manuscript/FIGURE_PLAN.md` plus figure scripts and source-data manifests. |
| Verify manuscript-critical run commands. | Repository readiness requires commands that a new researcher can actually run. | Exp11-Exp13, planned Exp13.1 | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Verified smoke/validation/full command log with runtime and expected outputs. |

## P1 - Strongly Recommended

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Add stochastic context corruption. | Exp13 adversarial corruption is a hard threshold, not a graded noise model. | Exp13.1 | `docs/threads/experiment12to13_export.md` | Context corruption summary and plots. |
| Run consolidation dose-response. | Consolidation is currently a preliminary stability-plasticity bias claim. | Exp13.1 | `docs/threads/experiment12to13_export.md` | Dose-response CSV, retention heatmaps, and caveated claim update. |
| Fit capacity laws. | Exp13 shows observed degradation curves but no fitted capacity model. | Exp13.1 | `docs/threads/experiment12to13_export.md` | Capacity-law summaries and figure panel. |
| Upgrade local-vs-global comparison. | The current Exp13 comparison is docs-only and aggregate-level. | Exp13.1 | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `docs/threads/experiment12to13_export.md` | Paired seed-level local-vs-global table with confidence intervals. |
| Design latent world inference. | Oracle world labels limit the current manuscript. | Future Exp14 | `docs/threads/experiment12to13_export.md` | Experiment 14 design doc after P0/P1 scientific hardening. |
| Build applied visual-state bridge. | Continuous/noisy input is preliminary and not end-to-end perception. | Future Exp14 | `docs/threads/experiment12to13_export.md` | Applied bridge experiment plan after Exp13.1 and baselines. |

## P2 - Future Work

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | Future | `docs/threads/experiment12to13_export.md` | New experiment directory under `experiments/`. |
| Learned perceptual encoders. | Test whether route memory can operate downstream of learned perception. | Future | `docs/threads/experiment12to13_export.md` | Applied bridge experiment. |
| Larger-scale continual learning variants. | Determine whether mechanisms survive larger workloads. | Future | `docs/threads/experiment12to13_export.md` | Scaling design and baseline comparison. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | Future | `docs/threads/experiment12to13_export.md` | Theory note or discussion section. |

## Completed P1 Repo-Readiness Items

| Completed item | Result | Source path |
|---|---|---|
| README external-facing entry point. | README now explains repository purpose, status, structure, starting points, experiment overview, claim map, non-claims, reproducibility, planned next work, and license caveat. | `README.md` |
| AGENTS structure alignment. | Agent rules now explicitly require new experiments under `experiments/`, distinguish reruns from successors, and document path verification. | `AGENTS.md` |
| Reproducibility audit upgrade. | Audit now maps environment, manuscript-critical commands, historical launchers, target run interface, artifact regeneration, and submission requirements. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` |
| Baseline requirements planning. | Baseline requirements now specify planned baseline IDs, contracts, metrics, organization, and acceptance criteria without claiming results. | `docs/manuscript/BASELINE_REQUIREMENTS.md` |
| Manuscript spine expansion. | Manuscript spine now includes title options, contribution, abstract skeleton, section architecture, figure storyboard, non-claims, and blockers. | `docs/manuscript/MANUSCRIPT_SPINE.md` |
| Synthesis cleanup. | Synthesis docs now refer to experiment directories under `experiments/` and retain not-submission-ready language. | `docs/synthesis/PROJECT_STATUS.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/synthesis/NEXT_EXPERIMENTS.md` |
| Path verifier workflow. | Documentation path verification is part of the regular workflow and CI path check. | `scripts/verify_doc_source_paths.py`; `.github/workflows/verify-doc-paths.yml` |
