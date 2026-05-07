# Project Status

## Current State

This repository contains self-contained experiment directories under `experiments/` plus manuscript, synthesis, source-data, and repo-audit documentation under `docs/`. Use the docs index, source-of-truth note, and first-manuscript claim-freeze document for navigation before editing evidence-heavy files.

This status document reflects the current repository state after importing Exp13.2 and Exp14. Exp13.2 is now documented as completed symbolic/algorithmic baseline evidence. Exp14 is now documented as completed symbolic transition-cue context-selection evidence.

Source path: `docs/README.md`; `docs/manuscript/SOURCE_OF_TRUTH.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`; `docs/experiments/EXPERIMENT_REGISTRY.md`.

## Experiments Completed Or Used In Current Spine

- Exp1-Exp6: historical/exploratory and methodological precursor material.
- Exp7-Exp10: supporting mechanism-building experiments.
- Exp11: context-separated incompatible-world memory.
- Exp12: clean capacity, continual retention, and held-out composition scaling.
- Exp13: finite-capacity breaking point, context corruption, holdout boundary, and continuous bridge.
- Exp13.1: publication-hardening full run for recurrence, structural plasticity, context binding, budget/consolidation, freeze-plasticity, and lesion diagnostics.
- Exp13.2: symbolic/algorithmic baseline suite, including oracle context-gated lookup, no-context lookup, endpoint memorization, recurrent controls, replay/LRU-style controls, hash/superposition controls, and parameter-isolation controls.
- Exp14: symbolic transition-cue context selection from partial transition cues, with smoke, validation, and full runs passing validation.

Source path: `docs/experiments/HISTORICAL_EXPERIMENTS.md`; `docs/experiments/EXPERIMENT_REGISTRY.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md`.

## Main Scientific Findings So Far

Claim: Structural plasticity, world/context indexing, and recurrence form the current core mechanism inside the route-memory benchmark.
Evidence: Exp8, Exp11, Exp12, Exp13, Exp13.1, and Exp13.2 ablations/baselines align with current summaries and local artifacts.
Caveat: This remains controlled symbolic benchmark evidence; neural baselines and prior-art import remain open depending on target venue.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/experiments/exp13_2_summary.md`; `docs/threads/experiment13_1_analysis_digest.md`.

Claim: Route-table storage and multi-step execution are separable.
Evidence: No-recurrence variants preserve route-table accuracy while composition fails in Exp11-Exp13.2; endpoint memorization controls in Exp13.2/Exp14 show seen-route endpoint performance can separate from suffix composition.
Caveat: This is a route-memory benchmark claim, not a broad recurrence novelty or abstract reasoning claim.
Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `docs/experiments/exp13_2_summary.md`; `docs/threads/experiment14_analysis_digest.md`.

Claim: Exp13 and Exp13.1 turn the story from ceiling performance into boundary mapping and publication hardening.
Evidence: Global/local budget pressure, adversarial or wrong-world context corruption, true primitive holdout, continuous-noise bridge artifacts, and Exp13.1 validation artifacts are present locally.
Caveat: Exp13.1 resolves some planned hardening but leaves lesion failure, uncertainty reporting, final figure scripts, and optional stochastic corruption/holdout cleanup open depending on manuscript scope.
Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`.

Claim: Exp13.2 partially satisfies symbolic/algorithmic baseline coverage.
Evidence: The full run passed validation and includes oracle context-gated lookup, shared no-context lookup, endpoint memorization, recurrent controls, replay/LRU controls, hash/superposition controls, and parameter-isolation controls. Oracle context-gated lookup matches CIRM on the clean supplied-context benchmark.
Caveat: Exp13.2 is not a neural-baseline suite and does not replace prior-art/novelty import.
Source path: `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`.

Claim: Exp14 partially addresses the oracle context-label limitation by selecting symbolic worlds from transition cues.
Evidence: The full run passed validation and the hard clean slice reaches 1.0000 CIRM world selection and composition; the highest-corruption hard slice remains around 0.9416 while the oracle context-gated table remains an upper bound.
Caveat: This is symbolic cue inference, not raw sensory latent-world discovery or generic stochastic robustness.
Source path: `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`.

## Current Manuscript Readiness

Status: ready for claim hardening and final figure/table planning, but not submission-ready.

The strongest internal story is coherent through Exp14. The next phase should use `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` to drive final figure/table generation and manuscript drafting. The manuscript still needs prior-art positioning, uncertainty/effect-size reporting, final figure scripts, command verification, license/citation metadata, and a target-venue decision about neural baselines.

Source path: `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`.

## Largest Blockers

- Exp14 main-vs-supplement placement and final figure/source-data work are unresolved.
- Seed-level confidence intervals and effect sizes are missing or not yet human-reviewed for manuscript groupings.
- Final figures need reproducible scripts and source-data manifests.
- Prior-art/novelty source import is incomplete.
- Neural baselines are absent and must either be scoped out or added depending on target venue.
- Exp13 holdout metrics require seen/unseen cleanup if retained centrally.
- Exp13.1 targeted lesion diagnostic failed the expected pattern.
- Context corruption evidence is wrong-world/context-identity or symbolic cue-evidence sensitivity, not generic stochastic robustness.
- License and citation metadata are missing.

## Recommended Next Action

Use `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` as the controlling handoff for final figure/table generation. Do not default to another experiment unless the target venue requires neural baselines or the first manuscript intentionally elevates currently caveated claims such as C9, generic robustness, positive lesion evidence, or raw latent-world discovery.

Source path: `docs/synthesis/NEXT_EXPERIMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`.
