# Project Status

## Current State

The repository contains thirteen completed experiment directories under `experiments/` plus manuscript, synthesis, source-data, and repo-audit documentation under `docs/`. Thread digests from exported ChatGPT analysis have been imported into experiment summaries, manuscript evidence documents, synthesis docs, and the thread index.

Source path: `docs/threads/THREAD_INDEX.md`; `docs/experiments/EXPERIMENT_REGISTRY.md`.

## Experiments Completed

- Exp1-Exp3: early MNIST/plastic-graph exploration; historical only for the route-memory manuscript.
- Exp4: first traversal-oriented successor task; route composition foundation.
- Exp5-Exp6: contextual successor attempts; caveated predecessors and route-audit correction.
- Exp7-Exp8: clean route-field diagnostic and self-organizing route acquisition.
- Exp9-Exp10: robustness, noisy/delayed feedback, adaptive reversal, and consolidation tradeoff.
- Exp11: context-separated incompatible-world memory.
- Exp12: clean capacity, continual retention, and held-out composition scaling.
- Exp13: finite-capacity breaking point, context corruption, holdout boundary, and continuous bridge.

Source path: `docs/experiments/EXPERIMENT_REGISTRY.md`.

## Main Scientific Findings So Far

Claim: Structural plasticity, world/context indexing, and recurrence form the current core mechanism inside the route-memory benchmark.
Evidence: Exp8, Exp11, Exp12, and Exp13 ablations align with the thread digests and local summaries.
Caveat: Internal ablations only; external baselines are still missing.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/threads/experiment12to13_export.md`.

Claim: Route-table storage and multi-step execution are separable.
Evidence: No-recurrence variants preserve route-table accuracy while composition fails in Exp11-Exp13.
Caveat: This is a route-memory benchmark claim, not a broad recurrence novelty claim.
Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.

Claim: Exp13 turns the story from ceiling performance into boundary mapping.
Evidence: Global/local budget pressure, adversarial context corruption, true primitive holdout, and continuous-noise bridge artifacts are present locally.
Caveat: Exp13 needs metric cleanup, true no-context-binding, stochastic context corruption, consolidation dose-response, and uncertainty reporting.
Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`.

## Current Manuscript Readiness

Status: promising but not submission-ready.

The strongest internal story is coherent, but the manuscript still needs Exp13.1 hardening, external baselines, uncertainty reporting, final reproducible figure scripts, and prior-art positioning before submission.

Source path: `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/MANUSCRIPT_SPINE.md`.

## Largest Blockers

- External baselines are missing.
- Exp13 holdout metrics require seen/unseen cleanup.
- Exp13 no-context-binding is not a clean ablation.
- Consolidation needs dose-response before becoming a central result.
- Context corruption needs stochastic/graded testing.
- Final figures need reproducible scripts and source-data tables.
- Manuscript-critical run commands need smoke/full verification on a fresh checkout.

## Operational Plan After P0/P1 Cleanup

1. Create a new future Exp13.1 directory under `experiments/` for publication hardening.
2. Standardize Exp13.1 launch profiles from the beginning.
3. Run smoke validation before any full Exp13.1 run.
4. Add seed-level uncertainty and metric-cleanup artifacts.
5. Implement the minimum external baseline suite in a new experiment directory under `experiments/`.
6. Regenerate final manuscript figures from documented scripts and source-data manifests.
7. Re-run `python scripts/verify_doc_source_paths.py` before readiness handoff.

## Recommended Next Action

Proceed to Exp13.1 design and implementation as a new self-contained experiment under `experiments/`, then implement the minimum external baseline suite.

Source path: `docs/synthesis/NEXT_EXPERIMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`.
