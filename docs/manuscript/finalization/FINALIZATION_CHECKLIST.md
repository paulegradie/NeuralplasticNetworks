# Manuscript Finalization Checklist

Purpose: working checklist for moving the Context-Indexed Route Memory manuscript from V1 draft to a submission-ready package after Exp15 import.

Use this as the operational tracker. Check items only when the repository contains the corresponding artifact or the manuscript has been explicitly updated.

Legend:

- `[ ]` not started
- `[~]` in progress / partial
- `[x]` complete
- `[!]` blocked or requires human decision

---

## Phase 0 - Finalization Control Docs

- [x] Create `docs/manuscript/finalization/`.
- [x] Add finalization plan.
- [x] Add finalization checklist.
- [x] Replace the old Exp15 implementation prompt with a post-Exp15 hardening prompt.
- [ ] Link finalization folder from `docs/README.md` or manuscript index if desired.

---

## Phase 1 - Experiment 15 Neural Comparator

### Design and implementation

- [x] Create planned directory `experiments/experiment15_neural_baseline_comparator/`.
- [x] Add experiment README with purpose, hypotheses, variants, metrics, and expected outputs.
- [x] Implement shared dataset/probe generation aligned to Exp13.2/Exp14 route-memory metrics.
- [x] Implement GRU endpoint baseline.
- [x] Implement GRU rollout baseline.
- [x] Implement small Transformer sequence baseline.
- [x] Implement neural one-step transition model rolled out recurrently.
- [x] Implement replay-trained neural baseline.
- [x] Implement parameter-isolated neural baseline.
- [x] Decide optional neural key-value / memory-augmented lookup baseline: omitted from Exp15 for scope control.
- [x] Add runtime/hardware manifest capture.
- [x] Add progress logging with seed, variant, slice, elapsed time, and estimated remaining work.
- [x] Add deterministic seed handling.
- [x] Add smoke, validation, and full profiles.
- [x] Add `start_exp15_validation.ps1`.
- [x] Add `start_exp15_full.ps1`.
- [x] Add analysis script.
- [x] Add validation script.

### Validation, full run, and analysis

- [~] Run smoke profile locally. Full/validation artifacts are present; no separate smoke artifact was verified in the Exp15 import pass.
- [x] Run validation/full profile locally for `exp15_full_20260508_092811`.
- [x] Confirm all required variants execute.
- [x] Confirm suffix-route probes are separated from seen full-route probes.
- [x] Confirm no-context/context variants are distinguishable in config columns.
- [x] Confirm replay/parameter-isolation configs are explicitly recorded.
- [x] Confirm all metrics are finite and in valid ranges.
- [x] Confirm validation report reports PASS/WARN/FAIL counts.
- [x] Preserve full run artifacts under `analysis/exp15_full_20260508_092811/`.
- [x] Generate `exp15_summary.csv`.
- [x] Generate `exp15_seed_metrics.csv`.
- [x] Generate `exp15_effect_sizes.csv`.
- [x] Generate `exp15_model_runtime.csv`.
- [x] Generate route-length scaling plot.
- [x] Generate world-count scaling plot.
- [x] Generate seen-vs-suffix composition plot.
- [x] Generate context-conflict accuracy plot.
- [x] Generate retention-after-sequential-worlds plot.
- [x] Generate validation report.
- [x] Review whether Exp15 changes the manuscript claim posture.

### Import

- [x] Import digest to `docs/threads/experiment15_analysis_digest.md`.
- [x] Update `docs/experiments/exp15_summary.md`.
- [x] Update `docs/experiments/EXPERIMENT_REGISTRY.md`.
- [x] Update `docs/manuscript/BASELINE_REQUIREMENTS.md`.
- [x] Update `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.
- [x] Update `docs/manuscript/LIMITATIONS_AND_THREATS.md`.
- [x] Update `docs/manuscript/FIGURE_PLAN.md`.
- [x] Update `docs/manuscript/MANUSCRIPT_TODO.md`.
- [x] Update `docs/synthesis/PUBLICATION_READINESS.md`.
- [x] Update `docs/synthesis/NEXT_EXPERIMENTS.md`.
- [x] Create `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.
- [x] Record Exp15 conflicts/caveats in `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`.
- [!] Update `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` or create a post-Exp15 claim freeze.

---

## Phase 2 - Prior-Art And Novelty Positioning

- [!] Locate/import the missing novelty/prior-art source artifact referenced as `Pasted text.txt`, if still relevant.
- [ ] Verify all V1 citation placeholders against real BibTeX metadata.
- [ ] Add or update bibliography file if repository conventions include one.
- [ ] Separate prior-art families clearly: continual learning, memory-augmented neural networks, fast weights/differentiable plasticity, mixture-of-experts/modular routing, latent-cause/context inference, neural algorithmic reasoning, and compositional generalization.
- [ ] Ensure the manuscript does not claim novelty for context gating, recurrence, replay, task isolation, or memory augmentation in isolation.
- [ ] Ensure novelty is framed as the controlled route-memory decomposition and evidence map.

---

## Phase 3 - Statistical Hardening

- [!] Decide retained main claims after Exp15.
- [ ] For each retained main claim, identify exact source CSV(s).
- [ ] Generate manuscript-grade seed-level summaries.
- [ ] Generate 95% confidence intervals.
- [ ] Generate effect sizes for direct comparisons.
- [ ] Review effect-size grouping for Exp13.2.
- [ ] Review effect-size grouping for Exp14.
- [ ] Review effect-size grouping for Exp15.
- [ ] Update `docs/manuscript/tables/table_03_statistical_summary.md`.
- [ ] Update `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`.
- [ ] Ensure C9 remains out of the main claim set unless seen/unseen metrics are cleaned.
- [ ] Avoid fitted capacity-law language unless capacity-law fitting is added.

---

## Phase 4 - Final Figure And Source-Data Pipeline

- [!] Decide final main figure set.
- [ ] Create final Figure 1 schematic or provide source instructions for human-drawn schematic.
- [ ] Generate final Figure 2 core ablation script/source data.
- [ ] Generate final Figure 3 clean capacity/retention script/source data.
- [ ] Generate final Figure 4 finite-budget/local-vs-global script/source data, if retained.
- [ ] Generate final Figure 5 Exp14 symbolic context-selection script/source data, if retained.
- [!] Decide whether Exp15 is a compact main-text table or supplementary neural comparator figure/table.
- [ ] Generate final Exp15 neural comparator figure/table, if retained.
- [ ] Add source-data files for every final panel/table.
- [ ] Update `docs/source_data/SOURCE_DATA_MANIFEST.csv`.
- [ ] Ensure candidate analysis plots are not cited as final manuscript figures unless regenerated by final figure scripts.
- [ ] Add figure captions with explicit caveats.

---

## Phase 5 - Manuscript Update

- [ ] Update abstract after Exp15 and statistical hardening.
- [ ] Update introduction to reflect final claim posture.
- [ ] Update related work with verified citations.
- [ ] Update methods with Exp15 neural baseline details if Exp15 is retained.
- [ ] Update results with final figures/tables.
- [ ] Update discussion to reflect final limitations.
- [ ] Update limitations section to distinguish closed risks from retained scope boundaries.
- [ ] Update non-claims.
- [ ] Ensure oracle context-gated table is described as an upper-bound comparator.
- [ ] Ensure Exp14 is described as symbolic transition-cue context selection, not raw latent-world discovery.
- [ ] Ensure Exp15 is not overinterpreted as exhaustive neural benchmarking.
- [ ] Ensure Exp15 replay collapse is not interpreted scientifically unless audited.
- [ ] Ensure broad CIRM-over-neural-model claims are absent.
- [ ] Remove or clearly mark all TODOs before submission.

---

## Phase 6 - Reproducibility And Repository Hygiene

- [ ] Fresh clone or clean-environment command verification.
- [x] Run documentation source-path verifier after Exp15 import.
- [x] Confirm all requested Exp15 artifacts exist locally.
- [ ] Confirm all manuscript-cited artifacts exist locally after final figure/table decisions.
- [ ] Add runtime/hardware metadata standard to future experiment template or docs.
- [x] Document Exp15 runtime/hardware metadata and reconstructed-manifest caveat.
- [ ] Add `LICENSE` after human license choice.
- [ ] Add `CITATION.cff`.
- [ ] Update README current-status section after Exp13.2/Exp14/Exp15 state is final.
- [ ] Add final reproducibility instructions.
- [ ] Decide whether to tag a release.
- [ ] Decide whether to archive on Zenodo after preprint/manuscript stabilization.

---

## Phase 7 - Optional Follow-Up Experiments Only If Needed

Do not start these by default. Revisit them only after post-Exp15 claim and figure/table decisions.

- [!] Optional neural-baseline successor - memory-augmented/key-value neural comparator, only if target venue or reviewers require broader neural coverage.
- [ ] Experiment 16 - Lesion Diagnostic Audit, only if positive lesion evidence is desired.
- [ ] Experiment 17 - Perceptual / Continuous Applied Bridge, only if applied bridge becomes central.
- [ ] Experiment 18 - Stochastic Context Corruption and Selection Margins, only if generic robustness is claimed.
- [ ] Experiment 19 - Consolidation Dose-Response Under Interference Pressure, only if consolidation becomes central.
- [ ] Experiment 20 or analysis-only pass - Seen-vs-Unseen Primitive Metric Cleanup, only if C9 becomes central.

---

## Current Recommended Next Checkbox

- [!] Decide retained post-Exp15 claim set and Exp15 placement: compact main-text baseline table vs supplementary neural comparator figure/table.
