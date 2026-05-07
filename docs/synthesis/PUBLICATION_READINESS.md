# Publication Readiness

## Summary Judgment

Status: improved and close to claim-freeze readiness, but not submission-ready.

The internal evidence now supports a narrow manuscript spine: in a controlled symbolic route-memory benchmark, context-indexed structural plasticity stores incompatible local route systems, recurrence is required to execute stored routes compositionally, Exp13.2 supplies symbolic/algorithmic baselines that narrow the clean supplied-context claim, and Exp14 shows that the active symbolic world can be selected from partial transition cues.

This is not yet a submission-ready manuscript. Remaining blockers are final claim-freeze, prior-art/novelty import, a decision on additional neural baselines, seed-level uncertainty/effect-size reporting, final reproducible figures/tables, command verification, license/citation metadata, and cleanup of central boundary claims such as Exp13 holdout metrics if retained.

Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/threads/experiment12to13_export.md`; `docs/threads/experiment13_1_analysis_digest.md`; `docs/threads/experiment13_2_analysis_digest.md`; `docs/threads/experiment14_analysis_digest.md`.

## Strongest Evidence

- Exp11 A/B context-separated retention and ablations. Source path: `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `docs/threads/experiment11_export`.
- Exp12 clean scaling to 32 worlds with no-recurrence/no-world-context/no-structural-plasticity contrasts. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13 finite-capacity breaking and no-recurrence route-table/composition dissociation. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `docs/threads/experiment12to13_export.md`.
- Exp13.1 publication-hardening ablations: no-recurrence-at-eval preserves route-table accuracy while composition collapses, no-structural-plasticity fails, no-context-binding fails, and local budget pressure is much more damaging than global budget pressure. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`; `docs/threads/experiment13_1_analysis_digest.md`.
- Exp13.2 symbolic baseline suite: oracle context-gated lookup matches CIRM in the clean supplied-context benchmark; shared no-context lookup fails first-step/seen-route context queries; endpoint memorization fails suffix composition; no-recurrence preserves route-table accuracy while composition fails. Source path: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `docs/threads/experiment13_2_analysis_digest.md`.
- Exp14 symbolic latent-context/cue-selection result: full run validation passed, clean hard-slice CIRM selection/composition reaches 1.0000, and cue corruption/cue-count sweeps quantify the symbolic context-selection boundary. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/validation_report.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.

## Weakest Evidence

- Consolidation as a stability-plasticity bias is preliminary because Exp13 validation shows only a small finite-pressure delta and Exp13.1 did not show a constrained-budget accuracy rescue. Source path: `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.
- Exp13.1 targeted lesion evidence failed the expected pattern and should not be used as positive mechanism evidence. Source path: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_lesion_metrics.csv`; `docs/threads/experiment13_1_analysis_digest.md`.
- Primitive holdout needs metric cleanup. Source path: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`.
- Continuous/noisy input is only a front-end bridge, not end-to-end perception. Source path: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`.
- Exp14 is symbolic transition-cue inference, not raw sensory latent-world discovery; the oracle context-gated table remains an upper bound. Source path: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`.
- Neural baseline and prior-art evidence remain incomplete. Exp13.2 supplies symbolic/algorithmic baselines but not a full neural baseline suite or imported novelty assessment. Source path: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/threads/experiment13_2_analysis_digest.md`.

## Required Before Submission

- Freeze the first-manuscript claim set and decide which claims are main, narrow-main, supplement, or future work.
- Decide whether additional neural baselines are required beyond Exp13.2 and import prior-art/novelty evidence.
- Decide whether Exp14 C13 is main text or supplement, and add final source-data/figure artifacts if retained.
- Add seed-level confidence intervals and effect sizes for retained claims.
- Create final paper figures from reproducible scripts with source-data manifests.
- Fix Exp13 holdout metrics if C9 remains central.
- Audit/rerun Exp13.1 lesion diagnostic only if positive route-critical lesion evidence will be cited.
- Verify manuscript-critical smoke/validation/full commands and document runtimes/hardware.
- Add human-chosen `LICENSE` and `CITATION.cff`.
- Keep biological, novelty, continual-learning, perception, and generalization claims narrow.
- Run `python scripts/verify_doc_source_paths.py` before readiness handoff.

Source path: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `scripts/verify_doc_source_paths.py`; `docs/manuscript/MANUSCRIPT_TODO.md`.

## Operational Readiness

Claim: The repository is more navigable after Exp13.2 and Exp14 integration but remains scientifically not submission-ready.

Evidence: The README, docs index, source-of-truth note, claim map, baseline requirements, figure plan, limitation tracker, and reproducibility audit now describe the integrated baseline and symbolic context-selection state.

Caveat: This is documentation readiness, not new scientific evidence.

Source path: `README.md`; `docs/README.md`; `docs/manuscript/SOURCE_OF_TRUTH.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`.

## Reviewer-Risk Matrix

| Reviewer criticism | Why they might say it | Current answer | Required fix |
|---|---|---|---|
| This is just context gating/task masks. | Context labels are supplied in most experiments and the oracle context-gated baseline matches CIRM in Exp13.2. | Current claim is narrower: clean supplied-context lookup is solvable by oracle gating; CIRM contribution is mechanism and failure-mode decomposition, not raw superiority over oracle lookup. Exp14 adds symbolic transition-cue selection but not raw context discovery. | Keep oracle-gating caveat central; use Exp14 only as symbolic cue-selection evidence. |
| Internal ablations are not enough. | Most claims compare only model variants. | Exp13.2 adds symbolic/algorithmic baselines with effect-size tables and validation. | Decide whether additional neural baselines are required and report final figure/table scripts. |
| Latent-context claim overreaches. | Exp14 uses symbolic transition cues and synthetic corruption. | C13 is limited to symbolic cue selection; oracle context gating remains an upper bound. | Keep wording narrow and add final source-data-backed figures only if retained. |
| Generalization is overstated. | Exp13 unseen primitive transitions fail. | The manuscript should claim composition over stored primitives, not unseen transition inference. | Fix seen/unseen/all holdout metrics and wording. |
| Consolidation claim is weak. | Easy regimes do not need consolidation; Exp13 delta is small. | Current claim is bias/tradeoff, not necessity. | Keep supplementary or add stronger dose-response/robustness evidence. |
| Context noise result is artificial. | Exp13 adversarial corruption and Exp13.1 wrong-world injection are identity tests. | It is useful as a selection-boundary test. | Add stochastic graded context corruption only if robustness is claimed. |
| Targeted lesion claim fails. | Exp13.1 targeted lesion is less damaging than random count-matched lesion. | Do not use the lesion diagnostic as positive mechanism evidence. | Audit critical-edge selection and rerun if lesion evidence is needed. |
| Biological framing overreaches. | The task is symbolic and synthetic. | Frame as computational inspiration only. | Tighten related work and limitations language. |
| Applied bridge is not applied learning. | Continuous front-end is decoded/noisy, not learned perception. | Keep it preliminary or supplementary. | Build a real visual-state route-memory bridge later. |
