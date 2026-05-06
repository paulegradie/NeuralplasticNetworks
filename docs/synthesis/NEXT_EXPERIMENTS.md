# Next Experiments

## Repository-Readiness Context

P0/P1 repository-readiness work is complete enough for Exp13.1 planning: active paths use `experiments/...`, the documentation path verifier is available, README/AGENTS are aligned, and baseline/reproducibility planning docs exist.

Claim: The next operational step is scientific hardening, not another repository-structure migration.
Evidence: P0/P1 remediation QA passed and the remaining blockers are Exp13.1, baselines, uncertainty reporting, final figures, and novelty import.
Caveat: This does not make the repository submission-ready.
Source path: `docs/repo_audit/P0_REMEDIATION_QA.md`; `docs/repo_audit/P1_REMEDIATION_QA.md`; `docs/synthesis/PUBLICATION_READINESS.md`

## Experiment 13.1 - Publication Hardening

Purpose: Correct and harden the main Exp13 boundary claims before manuscript submission.

Design goals:
- Keep Exp13 as historical output; create a new future Exp13.1 directory under `experiments/` if implemented.
- Preserve the main boundary questions: finite capacity, local capacity, recurrence dissociation, context corruption, primitive holdout, and consolidation pressure.
- Make the ablation definitions reviewer-proof.
- Use the standardized run-interface target from `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` from the beginning where practical.

Metric fixes:
- Add `route_table_accuracy_all`.
- Add `route_table_accuracy_seen`.
- Add `route_table_accuracy_unseen`.
- Add `composition_accuracy_seen_routes`.
- Add `composition_accuracy_unseen_required_routes`.
- Add seed-level confidence intervals and effect sizes.

Stochastic context corruption:
- Replace or supplement the hard adversarial threshold with stochastic corruption.
- Report top-1 world selection, world margin, wrong-world activation, and downstream composition.

Consolidation dose-response:
- Sweep graded consolidation strengths under finite sequential capacity.
- Report old-vs-new retention heatmaps and summary curves.
- Treat results as stability-plasticity bias unless behavioral necessity is clear.

Expected outputs:
- New run database(s) under the Exp13.1 directory.
- CSV summaries for capacity law, context corruption, holdout splits, and consolidation dose-response.
- Finalized figure panels for Figure 4, Figure 5, and Figure 6.

Source thread path: `docs/threads/experiment12to13_export.md`.
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

1. Exp13.1 design and smoke implementation under `experiments/`.
2. Exp13.1 metric cleanup and uncertainty outputs.
3. External baseline suite.
4. Final reproducible manuscript figures.
5. Applied visual-state bridge only after hardening and baselines.

Claim: This order prioritizes reviewer-critical weaknesses before new applied scope.
Evidence: Exp13.1, baselines, uncertainty, and figure regeneration are listed as submission blockers.
Caveat: The applied bridge remains useful future work, but it should not precede baseline and metric hardening.
Source path: `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`.
