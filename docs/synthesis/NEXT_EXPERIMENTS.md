# Next Experiments

## Experiment 13.1 - Publication Hardening

Purpose: Correct and harden the main Exp13 boundary claims before manuscript submission.

Design goals:
- Keep Exp13 as historical output; create a new top-level Exp13.1 directory if implemented.
- Preserve the main boundary questions: finite capacity, local capacity, recurrence dissociation, context corruption, primitive holdout, and consolidation pressure.
- Make the ablation definitions reviewer-proof.

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

Source thread path: `docs/threads/experiment12to13_export.md`; `docs/threads/experiment11_export`.

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
