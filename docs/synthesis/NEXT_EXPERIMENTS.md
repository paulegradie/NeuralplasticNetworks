# Next Experiments

## Repository-Readiness Context

P0/P1 repository-readiness work is complete enough for Exp13.1 follow-up and baseline work: active paths use `experiments/...`, the documentation path verifier is available, README/AGENTS are aligned, and baseline/reproducibility planning docs exist.

Claim: The next operational step is Exp13.2 manuscript integration plus Exp13.1 lesion/uncertainty follow-up, not another repository-structure migration.
Evidence: P0/P1 remediation QA passed, Exp13.1 and Exp13.2 full-run artifacts were imported, and the remaining blockers are baseline framing, lesion audit/rerun, uncertainty reporting, final figures, and novelty import.
Caveat: This does not make the repository submission-ready.
Source path: `docs/repo_audit/P0_REMEDIATION_QA.md`; `docs/repo_audit/P1_REMEDIATION_QA.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/threads/experiment13_1_analysis_digest.md`; `docs/threads/experiment13_2_analysis_digest.md`

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

## Experiment 13.2 - Baseline Suite

Completed run:
- Directory: `experiments/experiment13_2_baseline_suite/`.
- Run ID: `exp13_2_full_20260507_165813`.
- Validation: PASS 28, WARN 0, FAIL 0.
- Thread digest: `docs/threads/experiment13_2_analysis_digest.md`.

Imported baseline families:
- Shared transition table.
- Oracle context-gated transition table.
- Route endpoint memorizer.
- Recurrent non-plastic rule.
- Superposition/hash slots.
- Bounded LRU with and without replay.
- Parameter isolation.

Manuscript result:
Claim -> Exp13.2 partially resolves the baseline blocker and refines the clean supplied-context claim.
Evidence -> Oracle context-gated lookup matches CIRM at ceiling in the hard clean slice; shared no-context lookup fails seen-route/first-step context probes; endpoint memorization fails suffix composition; no-recurrence preserves route-table accuracy while composition fails.
Caveat -> Baselines are symbolic/algorithmic, not full neural baselines; oracle context labels remain a limitation.
Source path -> `docs/threads/experiment13_2_analysis_digest.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`

Remaining question: decide whether additional neural/prior-art baselines are required before submission and whether Exp13.2 belongs in a main figure or supplementary table.

Source thread path: `docs/threads/experiment13_2_analysis_digest.md`; `docs/threads/experiment12to13_export.md`.
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

1. Integrate Exp13.2 into manuscript claims, figure/table planning, and baseline framing.
2. Decide whether additional neural baselines are required beyond Exp13.2.
3. Exp13.1 lesion audit/rerun only if lesion evidence is needed.
4. Exp13.1 uncertainty/effect-size outputs and final figure scripts.
5. Stochastic context corruption follow-up if generic robustness is claimed.
6. Applied visual-state bridge only after hardening and baseline framing.

Claim: This order prioritizes reviewer-critical weaknesses before new applied scope.
Evidence: Exp13.1, baselines, uncertainty, and figure regeneration are listed as submission blockers.
Caveat: The applied bridge remains useful future work, but it should not precede baseline and metric hardening.
Source path: `docs/threads/experiment13_2_analysis_digest.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`.
