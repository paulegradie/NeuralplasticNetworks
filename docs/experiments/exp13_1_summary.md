# Experiment 13.1: Publication-Hardening Route-Field Memory Audit

## Status

- Code present: yes, `experiments/experiment13_1_publication_hardening/`.
- Analysis artifacts present: yes, full run `exp13_1_full_20260506_214756`.
- Validation present: yes, PASS 27, WARN 0, FAIL 0.
- Thread digest present: yes, `docs/threads/experiment13_1_analysis_digest.md`.
- Manuscript relevance: publication-hardening evidence for recurrence, structural plasticity, context binding, budget pressure, freeze plasticity, and failed lesion diagnostics.

## Evidence status

- Local artifacts indexed: partial; canonical docs now cite key artifacts, but full artifact indexes should be regenerated or extended before repo-readiness handoff.
- Local artifacts checked for key claims: yes, key CSVs, plots, run manifest, validation report, and SQLite path exist locally.
- Owning experiment README completed-runs/results updated: yes.
- Thread digest imported: yes, `docs/threads/experiment13_1_analysis_digest.md`.
- Human/manuscript validation pending: yes.
- Claims fully validated for publication: no; external baselines, CIs/effect sizes, final figure scripts, and lesion audit/rerun remain required.

## Purpose

Experiment 13.1 is a successor protocol to Exp13 that audits whether the route-memory behavior depends on recurrent route-field execution, structural plasticity, context/mode binding, and capacity layout in a cleaner manuscript-facing harness.

## Experimental design

The full profile used 20 seeds, 32 nodes, 3 modes, 32 worlds for core variant comparison, route lengths 1, 2, 4, 8, 12, and 16, 48 worlds for budget tests, and 24 worlds for lesion tests. It wrote an immutable SQLite run database plus per-run analysis outputs under `experiments/experiment13_1_publication_hardening/`.

Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json`.

## Key results

### Result 1: Full model solves clean route composition

Claim: The full model solves clean route composition across tested route lengths in this controlled harness.
Evidence: `exp13_1_full_model` has composition accuracy 1.0 and route-table accuracy 1.0 across route lengths 1-16.
Caveat: This is a saturated internal benchmark result, not broad generalization or external baseline evidence.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`.
Manuscript status: supporting internal evidence.

### Result 2: Recurrence is required for composed traversal

Claim: Recurrent evaluation is required for multi-step composition even when local route-table memory remains intact.
Evidence: At route length 12, no-recurrence-at-eval has route-table accuracy 1.0 but composition accuracy about 0.0413.
Caveat: This supports evaluation-time recurrence dependence, not necessarily training-time recurrence necessity.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`.
Manuscript status: strong internal evidence, needs baselines and uncertainty.

### Result 3: Structural plasticity is required in this harness

Claim: Structural plasticity is required for route-memory behavior in this implementation.
Evidence: At route length 12, no-structural-plasticity has composition accuracy about 0.0307 and route-table accuracy about 0.0308.
Caveat: Internal ablation evidence only; external baselines are still required.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`.
Manuscript status: strong internal evidence, needs baselines.

### Result 4: Context binding supports correct route use

Claim: Context/mode binding is important for selecting the correct route memory.
Evidence: At route length 12, no-context-binding has composition accuracy about 0.0452 while the full model remains at 1.0.
Caveat: This supports context binding in the benchmark; it does not prove latent world inference or novelty of context gating.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`.
Manuscript status: supporting internal evidence.

### Result 5: Wrong-world context injection causes failure

Claim: Wrong-world context identity can collapse route execution.
Evidence: For the full model, wrong-world injection at 0.75 corruption drops composition accuracy to about 0.0317 and top-1 world accuracy to 0.0.
Caveat: Context dropout and bleed did not reduce composition accuracy in this run, so this supports wrong-world identity sensitivity more than generic noisy-context fragility.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv`.
Manuscript status: promising, with stochastic corruption still needed.

### Result 6: World-gated plasticity was not required here

Claim: The current run does not support a claim that world-gated plasticity is necessary.
Evidence: At route length 12, no-world-gated-plasticity and full-model variants both have composition accuracy 1.0.
Caveat: World-gated plasticity may matter under harder interference, more worlds, or different schedules.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`.
Manuscript status: do not use as positive support.

### Result 7: Targeted lesion diagnostic failed expected pattern

Claim: This run does not support the claim that the targeted critical-edge lesion identifies route-critical structure better than matched random lesions.
Evidence: Targeted critical-edge lesion sensitivity is about 0.0808, while random count-matched lesion sensitivity is about 0.5085.
Caveat: This likely requires implementation audit and rerun before any positive lesion claim.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`.
Manuscript status: do not use; needs rerun.

### Result 8: Local budget is more damaging than global budget

Claim: Local route-field budget pressure is much more damaging to composed traversal than global budget pressure in this run.
Evidence: Under constrained settings, local budget composition is about 0.0589 while constrained global budget composition is about 0.5161.
Caveat: Budget settings and uncertainty need explicit manuscript documentation; this is still internal benchmark evidence.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
Manuscript status: promising/supplementary.

### Result 9: Consolidation strength did not rescue budget accuracy

Claim: In this run, consolidation strength did not materially improve accuracy under constrained budgets.
Evidence: Constrained-global composition is about 0.516 for none/default/weak/aggressive consolidation, and constrained-local composition is about 0.0589 across those settings.
Caveat: Consolidation may affect margins or other robustness measures; this result does not support an accuracy-rescue claim.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
Manuscript status: refines C8 conservatively.

### Result 10: Freezing plasticity preserves old worlds but blocks new acquisition

Claim: Freezing plasticity after consolidation preserves old worlds while blocking a new-world acquisition attempt.
Evidence: Old-world retention after freeze is 1.0, while new-world adaptation after freeze is about 0.0257.
Caveat: Internal stability/plasticity diagnostic only; not solved continual learning.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_freeze_plasticity.csv`.
Manuscript status: supplementary/promising.

### Result 11: Artifact-level validation passed

Claim: The local Exp13.1 run artifacts passed the experiment validator.
Evidence: Validation reports PASS 27, WARN 0, FAIL 0, 3000 raw metric rows, expected tables, phases, variants, plots, progress log, and SQLite database.
Caveat: The manifest does not include GPU/device/runtime metadata, and validation passing does not make the scientific claims submission-ready.
Source thread: `docs/threads/experiment13_1_analysis_digest.md`.
Source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`.
Manuscript status: strong artifact integrity.

## What this experiment supports

- Recurrent execution is necessary for composed traversal in this benchmark.
- Route-table accuracy and composed traversal can dissociate.
- Structural plasticity and context/mode binding are important internal mechanisms.
- Local budget constraints are more damaging than global constraints in the tested setting.
- Freeze-plasticity diagnostics separate old-world retention from new-world acquisition.

## What this experiment does not prove

- It does not provide external baseline comparisons.
- It does not prove broad abstract reasoning, latent world inference, or biological memory.
- It does not support a positive targeted-lesion mechanism claim.
- It does not show world-gated plasticity is necessary under the tested settings.
- It does not show consolidation strength rescues constrained-budget accuracy.

## Known caveats

- Targeted lesion diagnostic reversed the expected pattern and needs audit/rerun.
- External baselines remain missing.
- Seed-level confidence intervals and effect sizes are not yet manuscript-grade.
- GPU acceleration is not used because the implementation is table-based; device metadata is absent from the run manifest.
- Generated plots are analysis outputs, not final reproducible paper figures.

## Candidate manuscript figures

| Figure idea | Source image/data | Claim supported | Caveat |
|---|---|---|---|
| Recurrence route-table/composition dissociation | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_recurrence_ablation.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` | C3, C4 | Needs final figure script, baselines, and uncertainty. |
| Structural/context ablation panel | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_composition_accuracy.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` | C1, C2 | Internal ablation only. |
| Context wrong-world failure boundary | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_context_confusion.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` | C10 | Dropout/bleed did not reduce composition; stochastic corruption still needed. |
| Local/global budget comparison | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_budget_consolidation.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | C7, C8 | Consolidation rescue not supported as an accuracy claim. |
| Lesion diagnostic failure | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/plots/exp13_1_lesion_sensitivity.png`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv` | Negative diagnostic only | Do not use as positive mechanism evidence. |

## Required follow-up

- Audit targeted lesion implementation and rerun before citing lesion mechanism claims.
- Add external baseline suite.
- Add seed-level CIs/effect sizes and final reproducible figure scripts.
- Add or document GPU/device/runtime metadata for run manifests, even if the experiment remains CPU-only.
- Keep source-data mirrors under `docs/source_data/` synchronized with authoritative experiment artifacts if figures use them.
