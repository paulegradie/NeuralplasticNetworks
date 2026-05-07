# Publication Readiness

## Summary Judgment

Status: promising, but not manuscript-ready.

The internal evidence now supports a narrow manuscript spine: context-indexed structural plasticity stores incompatible local route systems, and recurrence is required to execute those stored routes compositionally. Exp13.1 strengthens that internal spine but also exposes a failed lesion diagnostic. Exp13.2 partially resolves the baseline blocker with symbolic/algorithmic comparators and also narrows the claim because oracle context-gated lookup matches CIRM in the clean supplied-context benchmark. Submission readiness is still blocked by prior-art import, a decision on additional neural baselines, lesion audit/rerun if lesion evidence is needed, statistical reporting, and final reproducible figures.

Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`; `docs/threads/experiment13_2_analysis_digest.md`.

## Strongest Evidence

- Exp11 A/B context-separated retention and ablations. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `docs/threads/experiment11_export`.
- Exp12 clean scaling to 32 worlds with no-recurrence/no-world-context/no-structural-plasticity contrasts. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13 finite-capacity breaking and no-recurrence route-table/composition dissociation. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13.1 publication-hardening ablations: no-recurrence-at-eval preserves route-table accuracy while composition collapses, no-structural-plasticity fails, no-context-binding fails, and local budget pressure is much more damaging than global budget pressure. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`; `docs/threads/experiment13_1_analysis_digest.md`.
- Exp13.2 symbolic baseline suite: oracle context-gated lookup matches CIRM in the clean supplied-context benchmark; shared no-context lookup fails first-step/seen-route context queries; endpoint memorization fails suffix composition; no-recurrence preserves route-table accuracy while composition fails. Source path: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `docs/threads/experiment13_2_analysis_digest.md`.

## Weakest Evidence

- Consolidation as a stability-plasticity bias is preliminary because Exp13 validation shows only a small finite-pressure delta. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`.
- Exp13.1 targeted lesion evidence failed the expected pattern and should not be used as positive mechanism evidence. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md`.
- Primitive holdout needs metric cleanup. Source path: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
- Continuous/noisy input is only a front-end bridge, not end-to-end perception. Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`.
- Neural baseline and prior-art evidence remain incomplete. Exp13.2 supplies symbolic/algorithmic baselines but not a full neural baseline suite or imported novelty assessment. Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/threads/experiment13_2_analysis_digest.md`.

## Required Before Submission

- Audit/rerun Exp13.1 lesion diagnostic if route-critical lesion evidence is needed.
- Decide whether additional neural baselines are required beyond Exp13.2 and import prior-art/novelty evidence.
- Add seed-level confidence intervals and effect sizes.
- Fix holdout metrics and no-context-binding ablation naming/design.
- Create final paper figures from reproducible scripts.
- Keep biological and novelty claims narrow.
- Verify manuscript-critical smoke/validation commands and document runtimes.
- Run `python scripts/verify_doc_source_paths.py` before readiness handoff.

Source path: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `scripts/verify_doc_source_paths.py`.

## Operational Readiness

Claim: The repository is more navigable after P0/P1 cleanup but remains scientifically not submission-ready.
Evidence: The README, docs index, manuscript spine, baseline requirements, and reproducibility audit now provide a clearer external-facing map.
Caveat: This is documentation readiness, not new scientific evidence.
Source path: `README.md`; `docs/README.md`; `docs/manuscript/MANUSCRIPT_SPINE.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`.

## Reviewer-Risk Matrix

| Reviewer criticism | Why they might say it | Current answer | Required fix |
|---|---|---|---|
| This is just context gating/task masks. | Context labels are supplied and the oracle context-gated baseline matches CIRM in Exp13.2. | Current claim is narrower: clean supplied-context lookup is solvable by oracle gating; CIRM contribution is mechanism and failure-mode decomposition, not raw superiority over oracle lookup. | Keep oracle-gating caveat central; add latent-context inference only if needed. |
| Internal ablations are not enough. | Most claims compare only model variants. | Exp13.2 adds symbolic/algorithmic baselines with effect-size tables and validation. | Decide whether additional neural baselines are required and report final figure/table scripts. |
| Generalization is overstated. | Exp13 unseen primitive transitions fail. | The manuscript should claim composition over stored primitives, not unseen transition inference. | Fix seen/unseen/all holdout metrics and wording. |
| Consolidation claim is weak. | Easy regimes do not need consolidation; Exp13 delta is small. | Current claim is bias/tradeoff, not necessity. | Run consolidation dose-response under finite capacity. |
| Context noise result is artificial. | Exp13 adversarial corruption is threshold-like. | It is useful as a selection-boundary test. | Add stochastic graded context corruption. |
| Targeted lesion claim fails. | Exp13.1 targeted lesion is less damaging than random count-matched lesion. | Do not use the lesion diagnostic as positive mechanism evidence. | Audit critical-edge selection and rerun if lesion evidence is needed. |
| Biological framing overreaches. | The task is symbolic and synthetic. | Frame as computational inspiration only. | Tighten related work and limitations language. |
| Applied bridge is not applied learning. | Continuous front-end is decoded/noisy, not learned perception. | Keep it preliminary or supplementary. | Build a real visual-state route-memory bridge later. |
