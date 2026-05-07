# Next Experiments

## Repository-Readiness Context

P0/P1 repository-readiness work is complete enough for Exp13.1 follow-up and baseline work: active paths use `experiments/...`, the documentation path verifier is available, README/AGENTS are aligned, and baseline/reproducibility planning docs exist.

Claim: The next operational step is Exp13.1 lesion/uncertainty follow-up and external baselines, not another repository-structure migration.
Evidence: P0/P1 remediation QA passed, Exp13.1 full-run artifacts were imported, and the remaining blockers are lesion audit/rerun, baselines, uncertainty reporting, final figures, and novelty import.
Caveat: This does not make the repository submission-ready.
Source path: `docs/repo_audit/P0_REMEDIATION_QA.md`; `docs/repo_audit/P1_REMEDIATION_QA.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/threads/experiment13_1_analysis_digest.md`

## Experiment 13.1 - Publication Hardening

Purpose: Correct and harden the main Exp13 boundary claims before manuscript submission. A first full Exp13.1 run has completed and is imported; follow-up should focus on caveats exposed by that run.

Completed run:
- Directory: `experiments/experiment13_1_publication_hardening/`.
- Run ID: `exp13_1_full_20260506_214756`.
- Validation: PASS 27, WARN 0, FAIL 0.
- Thread digest: `docs/threads/experiment13_1_analysis_digest.md`.

Follow-up goals:
- Audit targeted critical-edge lesion selection and rerun if lesion evidence is needed.
- Add seed-level confidence intervals, effect sizes, and final figure scripts.
- Add explicit device/runtime metadata to future manifests, with CPU-only rationale if applicable.
- Preserve the main boundary questions: finite capacity, local capacity, recurrence dissociation, wrong-world context corruption, and consolidation pressure.

Metric fixes:
- Add `route_table_accuracy_all`.
- Add `route_table_accuracy_seen`.
- Add `route_table_accuracy_unseen`.
- Add `composition_accuracy_seen_routes`.
- Add `composition_accuracy_unseen_required_routes`.
- Add seed-level confidence intervals and effect sizes.

Stochastic context corruption:
- Exp13.1 wrong-world injection supports identity/selection sensitivity, while dropout/bleed did not reduce composition accuracy.
- Replace or supplement hard adversarial/wrong-world thresholds with stochastic corruption if generic robustness is claimed.
- Report top-1 world selection, world margin, wrong-world activation, and downstream composition.

Consolidation dose-response:
- Exp13.1 did not show constrained-budget accuracy rescue from consolidation strength.
- Report margin/robustness effects if using consolidation centrally.
- Treat results as stability-plasticity bias unless behavioral necessity is clear.

Expected outputs:
- New rerun database(s), if needed, under the Exp13.1 directory.
- CSV summaries for corrected lesion diagnostics, uncertainty/effect sizes, stochastic context corruption if run, and final figure source data.
- Finalized figure panels for Figure 4, Figure 5, and Figure 6.

Source thread path: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`.
Operational source path: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `docs/manuscript/MANUSCRIPT_TODO.md`.

## Baseline Suite

Minimum baseline families:
- Shared transition table: tests whether explicit structural plasticity adds anything over simple lookup.
- Context-gated table or task mask: tests whether world/context indexing is just conventional gating.
- Replay-based continual learner: tests retention under sequential worlds.
- Parameter-isolation baseline such as PackNet/HAT-inspired masks: tests whether isolated capacity explains retention.
- Hypernetwork or superposition-style baseline: tests compact context-conditioned storage.
- Recurrent non-plastic baseline: tests whether recurrence alone can compose routes.
- Optional CSCG/cloned-state cognitive-map baseline: tests relation to latent-state map models.

Why each is needed: The novelty assessment in the thread warns that no individual ingredient is novel; the defensible claim is the controlled conjunction of structural plasticity, context-indexed storage, and recurrent execution.

Expected comparison: Report accuracy, route-table memory, composition, retention, capacity use, and failure modes under the same route-memory benchmark.

Recommended future organization: create a new baseline experiment directory under `experiments/`, for example `experiments/exp13_2_baseline_suite/` or `experiments/exp14_baseline_suite/`.

Source thread path: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment11_export`.
Planning source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`.

## Applied Bridge

Visual-state route memory:
- Replace the decoded/noisy symbolic start-state bridge with a learned or semi-learned perceptual state encoder.
- Keep the task modest: noisy visual states feed a route-memory system, not a full general vision agent.

Modest claim:
- Continuous/noisy inputs can be made compatible with context-indexed route memory.

Limitations:
- Current Exp13 bridge is not end-to-end perception.
- Applied bridge should wait until Exp13.1 and baseline work are complete.

Source thread path: `docs/threads/experiment12to13_export.md`.

## Immediate Order Of Operations

1. Exp13.1 lesion audit/rerun only if lesion evidence is needed.
2. Exp13.1 uncertainty/effect-size outputs and final figure scripts.
3. External baseline suite.
4. Stochastic context corruption follow-up if generic robustness is claimed.
5. Applied visual-state bridge only after hardening and baselines.

Claim: This order prioritizes reviewer-critical weaknesses before new applied scope.
Evidence: Exp13.1, baselines, uncertainty, and figure regeneration are listed as submission blockers.
Caveat: The applied bridge remains useful future work, but it should not precede baseline and metric hardening.
Source path: `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`.
