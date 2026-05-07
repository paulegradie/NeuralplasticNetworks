# Manuscript TODO

Purpose: Maintain a conservative work queue for turning this repository into a manuscript-grade research artifact.

## Current Next Operational Priority

Use the completed Exp13.1 publication-hardening run to audit lesion diagnostics, add uncertainty/final figure scripts, and then proceed to the external baseline suite.

Claim: Exp13.1 is completed as an internal publication-hardening run, but not as submission-ready evidence by itself.
Evidence: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md` reports PASS 27, WARN 0, FAIL 0, and `docs/threads/experiment13_1_analysis_digest.md` identifies supported internal claims and unresolved caveats.
Caveat: Targeted lesion evidence failed the expected pattern; external baselines, CIs/effect sizes, final figure scripts, and device/runtime metadata remain open.
Source path: `docs/threads/experiment13_1_analysis_digest.md`; `docs/experiments/exp13_1_summary.md`; `experiments/experiment13_1_publication_hardening/README.md`

## P0 - Required Before Manuscript Submission

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Add external baseline suite. | Current evidence is mostly internal ablations. | Exp8-Exp13 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md` | Baseline experiment directory under `experiments/`, summary CSVs, figures, and baseline evidence rows. |
| Add seed-level confidence intervals and effect sizes. | Many claims cite mean summaries without manuscript-grade uncertainty. | Exp8-Exp13 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md` | Updated analysis summaries and figure scripts. |
| Fix holdout metrics if retaining Exp13 holdout claims. | Exp13 route-table accuracy must split all, seen, and unseen primitives. | Exp13 or successor | `docs/threads/experiment12to13_export.md` | `route_table_accuracy_all`, `route_table_accuracy_seen`, `route_table_accuracy_unseen`, and split composition CSVs. |
| Keep no-context-binding wording aligned to Exp13.1. | Exp13 `no_context_binding` may be weak-binding/oracle-clean rather than a pure ablation; Exp13.1 now supplies the cleaner context-binding evidence. | Exp13, Exp13.1 | `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md` | Avoid using stale Exp13 no-context-binding as the main source for C2. |
| Import novelty assessment as local artifact and source baseline requirement claims. | C12 is currently thread-derived because `Pasted text.txt` is missing locally. | Manuscript-level | `docs/threads/experiment12to13_export.md` | Local verification pending: future `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md` or `docs/repo_audit/source_imports/NOVELTY_ASSESSMENT.md`, then update C12 and baseline requirements. |
| Create final paper figures from reproducible scripts. | Current figure plan cites generated plots, but final panels need controlled scripts. | Exp11-Exp13.1 | `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md` | `docs/manuscript/FIGURE_PLAN.md` plus figure scripts and source-data manifests. |
| Verify manuscript-critical run commands. | Repository readiness requires commands that a new researcher can actually run. | Exp11-Exp13.1 | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `docs/threads/experiment13_1_analysis_digest.md` | Verified smoke/validation/full command log with runtime and expected outputs. |
| Audit and rerun Exp13.1 lesion diagnostic before citing it. | Targeted critical-edge lesions were less damaging than random count-matched lesions in the completed Exp13.1 run. | Exp13.1 | `docs/threads/experiment13_1_analysis_digest.md` | Implementation audit, corrected critical-edge definition if needed, and rerun artifact under `experiments/experiment13_1_publication_hardening/`. |
| Add Exp13.1 device/runtime metadata to future manifests. | The completed run is table-based and CPU-oriented, but the manifest lacks explicit device/runtime metadata. | Exp13.1 | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json` | Future run manifest with CPU/GPU rationale and runtime metadata. |

## P1 - Strongly Recommended

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Add stochastic context corruption beyond wrong-world injection. | Exp13 adversarial corruption and Exp13.1 wrong-world injection are identity/selection tests, not generic graded-noise robustness. | Exp13.1 or successor | `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md` | Context corruption summary and plots with stochastic corruption probability. |
| Refine consolidation analysis beyond accuracy rescue. | Exp13.1 did not show constrained-budget accuracy rescue from consolidation strength. | Exp13.1 or successor | `docs/threads/experiment13_1_analysis_digest.md` | Margin/robustness summaries or a caveated decision to keep consolidation supplementary. |
| Fit capacity laws. | Exp13 shows observed degradation curves but no fitted capacity model. | Exp13.1 | `docs/threads/experiment12to13_export.md` | Capacity-law summaries and figure panel. |
| Upgrade local-vs-global comparison. | The current Exp13 comparison is docs-only and aggregate-level. | Exp13.1 | `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `docs/threads/experiment12to13_export.md` | Paired seed-level local-vs-global table with confidence intervals. |
| Maintain artifact and evidence indexes as new outputs are created. | Manuscript claims must remain traceable to source paths. | All future runs | `docs/threads/experiment12to13_export.md` | Updated `docs/repo_audit/ARTIFACT_INDEX.csv`, summaries, and conflict log as new artifacts are created. |
| Design latent world inference. | Oracle world labels limit the current manuscript. | Future Exp14 | `docs/threads/experiment12to13_export.md` | Experiment 14 design doc after P0/P1 scientific hardening. |
| Build applied visual-state bridge. | Continuous/noisy input is preliminary and not end-to-end perception. | Future Exp14 | `docs/threads/experiment12to13_export.md` | Applied bridge experiment plan after Exp13.1 and baselines. |

## P2 - Future Work

| TODO | Reason | Related experiment | Source thread | Target output |
|---|---|---|---|---|
| Richer non-symbolic tasks. | Move beyond synthetic symbolic route memory. | Future | `docs/threads/experiment12to13_export.md` | New experiment directory under `experiments/`. |
| Learned perceptual encoders. | Test whether route memory can operate downstream of learned perception. | Future | `docs/threads/experiment12to13_export.md` | Applied bridge experiment. |
| Larger-scale continual learning variants. | Determine whether mechanisms survive larger workloads. | Future | `docs/threads/experiment12to13_export.md` | Scaling design and baseline comparison. |
| Biological mapping expansion. | Keep biological claims disciplined while exploring inspiration. | Future | `docs/threads/experiment12to13_export.md` | Theory note or discussion section. |

## Completed Repository-Readiness Work

| Completed item | Result | Source path |
|---|---|---|
| P0 path migration and docs CSV reviewability. | Active source paths now use `experiments/...`; docs CSV files are plain text rather than Git LFS pointer text. | `docs/repo_audit/P0_REMEDIATION_REPORT.md`; `docs/repo_audit/P0_REMEDIATION_QA.md` |
| P0 path verification. | The path verifier exists and passed during P0/P1 QA with zero missing active paths. | `scripts/verify_doc_source_paths.py`; `docs/repo_audit/PATH_VERIFICATION_REPORT.md` |
| README external-facing entry point. | README now explains repository purpose, status, structure, starting points, experiment overview, claim map, non-claims, reproducibility, planned next work, and license caveat. | `README.md` |
| AGENTS structure alignment. | Agent rules now explicitly require new experiments under `experiments/`, distinguish reruns from successors, and document path verification. | `AGENTS.md` |
| Reproducibility audit upgrade. | Audit now maps environment, manuscript-critical commands, historical launchers, target run interface, artifact regeneration, and submission requirements. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` |
| Baseline requirements planning. | Baseline requirements now specify planned baseline IDs, contracts, metrics, organization, and acceptance criteria without claiming results. | `docs/manuscript/BASELINE_REQUIREMENTS.md` |
| Manuscript spine expansion. | Manuscript spine now includes title options, contribution, abstract skeleton, section architecture, figure storyboard, non-claims, and blockers. | `docs/manuscript/MANUSCRIPT_SPINE.md` |
| Synthesis cleanup. | Synthesis docs now refer to experiment directories under `experiments/` and retain not-submission-ready language. | `docs/synthesis/PROJECT_STATUS.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/synthesis/NEXT_EXPERIMENTS.md` |
| Path verifier workflow. | Documentation path verification is part of the regular workflow and CI path check. | `scripts/verify_doc_source_paths.py`; `.github/workflows/verify-doc-paths.yml` |
| Exp13.1 publication-hardening run imported. | Full run artifacts were validated and imported into thread index, experiment summary, README completed-run log, claims, figure plan, limitations, TODOs, synthesis docs, source-data mirrors, conflict log, and import report. | `docs/threads/experiment13_1_analysis_digest.md`; `docs/experiments/exp13_1_summary.md`; `docs/repo_audit/EXP13_1_ANALYSIS_IMPORT_REPORT.md` |
