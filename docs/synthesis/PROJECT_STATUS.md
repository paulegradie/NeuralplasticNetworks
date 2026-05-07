# Project Status

## Current State

The repository contains fourteen completed experiment directories under `experiments/` plus manuscript, synthesis, source-data, and repo-audit documentation under `docs/`. Thread digests from exported ChatGPT analysis have been imported into experiment summaries, manuscript evidence documents, synthesis docs, and the thread index. Use the docs index and source-of-truth note for navigation before editing evidence-heavy files.

Source path: `docs/README.md`; `docs/manuscript/SOURCE_OF_TRUTH.md`; `docs/threads/THREAD_INDEX.md`; `docs/experiments/EXPERIMENT_REGISTRY.md`.

## Experiments Completed

- Exp1-Exp3: early MNIST/plastic-graph exploration; historical only for the route-memory manuscript.
- Exp4: first traversal-oriented successor task; route composition foundation.
- Exp5-Exp6: contextual successor attempts; caveated predecessors and route-audit correction.
- Exp7-Exp8: clean route-field diagnostic and self-organizing route acquisition.
- Exp9-Exp10: robustness, noisy/delayed feedback, adaptive reversal, and consolidation tradeoff.
- Exp11: context-separated incompatible-world memory.
- Exp12: clean capacity, continual retention, and held-out composition scaling.
- Exp13: finite-capacity breaking point, context corruption, holdout boundary, and continuous bridge.
- Exp13.1: publication-hardening full run for recurrence, structural plasticity, context binding, budget/consolidation, freeze-plasticity, and lesion diagnostics.
- Exp13.2: symbolic/algorithmic baseline suite and clean supplied-context claim refinement.

Source path: `docs/experiments/EXPERIMENT_REGISTRY.md`.

## Main Scientific Findings So Far

Claim: Structural plasticity, world/context indexing, and recurrence form the current core mechanism inside the route-memory benchmark.
Evidence: Exp8, Exp11, Exp12, Exp13, and Exp13.1 ablations align with the thread digests and local summaries; Exp13.2 adds symbolic baseline failure modes for shared no-context lookup, endpoint memorization, no-recurrence, and no-structural-plasticity.
Caveat: Exp13.2 baselines are symbolic/algorithmic and do not establish neural-baseline or prior-art sufficiency.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`; `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`.

Claim: Clean supplied-context symbolic route memory can be solved by oracle context-gated lookup.
Evidence: In Exp13.2, the oracle context-gated transition table matches CIRM at `1.0000` route-table, seen-route composition, suffix-route composition, and first-step context accuracy at the hard clean slice.
Caveat: This is a claim refinement, not a negative result for CIRM; it means the manuscript should not claim raw accuracy superiority over supplied-context lookup.
Source path: `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`.

Claim: Route-table storage and multi-step execution are separable.
Evidence: No-recurrence variants preserve route-table accuracy while composition fails in Exp11-Exp13.
Caveat: This is a route-memory benchmark claim, not a broad recurrence novelty claim.
Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`.

Claim: Exp13 and Exp13.1 turn the story from ceiling performance into boundary mapping and publication hardening.
Evidence: Global/local budget pressure, adversarial or wrong-world context corruption, true primitive holdout, continuous-noise bridge artifacts, and Exp13.1 validation artifacts are present locally.
Caveat: Exp13.1 resolves some planned hardening but leaves lesion failure, baselines, uncertainty reporting, stochastic corruption, and final figure scripts open.
Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`.

## Current Manuscript Readiness

Status: promising but not submission-ready.

The strongest internal story is coherent, Exp13.1 has completed a first publication-hardening run, and Exp13.2 has partially resolved the baseline blocker with symbolic/algorithmic comparators. The manuscript still needs lesion audit/rerun if lesion evidence is used, prior-art positioning, a decision on additional neural baselines, uncertainty/final figure scripts, and careful oracle-context framing before submission.

Source path: `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/MANUSCRIPT_SPINE.md`.

## Largest Blockers

- Symbolic/algorithmic baselines are now present, but additional neural/prior-art comparators may still be required.
- Exp13 holdout metrics require seen/unseen cleanup if retained from Exp13.
- Exp13.1 targeted lesion diagnostic failed the expected pattern.
- Consolidation needs dose-response before becoming a central result.
- Context corruption needs stochastic/graded testing.
- Final figures need reproducible scripts and source-data tables.
- Manuscript-critical run commands need smoke/full verification on a fresh checkout.

## Operational Plan After P0/P1 Cleanup

1. Audit and rerun the Exp13.1 lesion diagnostic if the manuscript needs route-critical lesion evidence.
2. Add seed-level uncertainty and final figure scripts for Exp13.1-supported claims.
3. Integrate Exp13.2 into manuscript figures/tables and decide whether additional neural baselines are needed.
4. Add stochastic context corruption or explicitly limit context claims to wrong-world identity selection.
5. Regenerate final manuscript figures from documented scripts and source-data manifests.
6. Re-run `python scripts/verify_doc_source_paths.py` before readiness handoff.

## Recommended Next Action

Proceed to Exp13.2 manuscript integration and baseline-figure decisions, then run an Exp13.1 lesion audit/rerun and uncertainty pass if those claims remain in scope.

Source path: `docs/synthesis/NEXT_EXPERIMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`.
