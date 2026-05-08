# Manuscript Finalization Plan

Purpose: convert the current limitation/threat register into a practical post-Exp15 manuscript-finalization plan.

Controlling inputs:

- `docs/manuscript/draft/MANUSCRIPT_V1.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/experiments/exp13_2_summary.md`
- `docs/experiments/exp14_summary.md`
- `docs/experiments/exp15_summary.md`
- `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`

## Executive Strategy

Do not try to solve every limitation before submission. Split the remaining work into four tracks:

| Track | Purpose | Manuscript blocking? |
|---|---|---|
| A. Claim and manuscript hygiene | Prevent overclaiming and keep the manuscript scoped as a controlled symbolic/mechanistic benchmark. | Yes |
| B. Metric/statistical cleanup | Ensure every central claim has clean seed-level uncertainty, effect-size, source-data, and figure provenance. | Yes |
| C. Exp15 neural comparator integration | Integrate the completed minimal neural comparator without overclaiming it as exhaustive neural benchmarking. | Yes for manuscript posture; broader neural experiments remain venue-dependent. |
| D. Optional boundary experiments | Address lesion, stochastic robustness, consolidation, applied bridge, or memory-augmented neural baselines only if those claims are elevated. | No |

Recommended immediate next action: **post-Exp15 manuscript hardening and final figure/table planning**.

The manuscript should continue to avoid claims of solved continual learning, broad neural-network superiority, raw sensory latent-world discovery, end-to-end perception, broad biological proof, broad abstract rule induction, or unseen primitive inference.

## 1. Baseline Coverage

Claim -> Baseline coverage is no longer absent, but remains incomplete for broad ML-comparison or submission-readiness claims.
Evidence -> Exp13.2 provides symbolic/algorithmic baselines. Exp15 provides a completed minimal neural comparator with validation PASS, 10 seeds, 9 variants, 5,400 seed metric rows, and 1,080 runtime rows.
Caveat -> Exp15 is fixed-profile and non-exhaustive, omits memory-augmented/key-value neural baselines, and includes replay/provenance caveats.
Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

Observed Exp15 consequences:

| Result | Manuscript consequence |
|---|---|
| Context-conditioned transition MLP and world-head transition MLP solve the clean hard slice. | Drop broad neural-superiority language; frame CIRM as interpretable mechanism and benchmark decomposition. |
| Endpoint GRU/Transformer variants show endpoint-vs-composition dissociation. | Supports route-table/composition/endpoint-memorization separation. |
| No-context transition MLP solves suffix composition but fails first-step/full-route disambiguation. | Narrow context-necessity wording to incompatible local transitions and first-step/full-route conflict. |
| Replay transition MLP collapses in the hard slice. | Treat as requiring implementation/training-regime audit before scientific interpretation. |

Required next decisions:

- Decide whether Exp15 should be a compact main-text baseline table or a supplementary neural comparator table/figure.
- Decide whether a memory-augmented/key-value neural baseline is required for the target venue.
- Keep broad CIRM-over-neural-model claims out of the manuscript.

## 2. Symbolic Benchmark Limitation

Claim -> The benchmark remains synthetic and symbolic.
Evidence -> Exp11-Exp15 use symbolic nodes, modes, worlds, routes, contexts, or transition cues.
Caveat -> This is not end-to-end perceptual learning or naturalistic navigation.
Source path -> `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/threads/experiment15_analysis_digest.md`.

Safe language:

> This benchmark intentionally uses symbolic route systems to isolate storage, context indexing, and recurrent execution. It is not a claim about end-to-end perceptual learning or naturalistic navigation.

No new experiment is required unless the manuscript attempts to make applied or perceptual claims.

## 3. Oracle Context And Symbolic Context Selection

Claim -> Exp14 partially reduces the oracle-world-label limitation by selecting symbolic context from transition cues.
Evidence -> Exp14 validation and summary artifacts support symbolic transition-cue context selection; Exp13.2 oracle context-gated lookup remains a clean supplied-context upper bound.
Caveat -> Exp14 is not raw sensory latent-world discovery, and oracle context gating should not be described as a defeated competitor.
Source path -> `docs/threads/experiment14_analysis_digest.md`; `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.

Required asset work:

- Decide main-text vs supplement placement for Exp14.
- Create final source-data-backed Exp14 figure/table if retained.
- Caption it as symbolic transition-cue context selection.

## 4. Metric And Statistical Hardening

Claim -> Central claims still need final manuscript-grade statistics and source-data-backed figures/tables.
Evidence -> Current docs have candidate assets and many generated analysis summaries, but not all retained claims have final figure scripts, reviewed effect-size groupings, or source-data manifests.
Caveat -> Candidate analysis plots are not final manuscript figures.
Source path -> `docs/manuscript/FIGURE_PLAN.md`; `docs/source_data/STATISTICAL_REPORTING_READINESS.csv`; `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`.

Required outputs:

- `docs/source_data/SOURCE_DATA_MANIFEST.csv` updated for every final panel/table.
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` updated.
- `docs/manuscript/tables/table_03_statistical_summary.md` reviewed and aligned.
- Final figure/table scripts or documented generation path.
- Final source-data CSVs for retained panels.

Acceptance criteria for every retained central claim:

- mean;
- standard deviation or standard error;
- 95% confidence interval;
- seed count;
- effect size for direct comparisons where appropriate;
- source artifact path;
- figure/table reference.

C9 must stay out of the main claim set unless seen/unseen/all route-table and composition split metrics are cleaned.

## 5. Known Retained Scope Boundaries

Keep these as explicit limitations unless new evidence is added:

| Boundary | Posture |
|---|---|
| Exp13.1 lesion diagnostic | Do not use as positive mechanism evidence unless audited/rerun. |
| Consolidation | Frame as preliminary stability/plasticity bias, not required or accuracy-rescuing. |
| Context corruption | Frame as symbolic wrong-world/cue-evidence sensitivity, not generic stochastic robustness. |
| Continuous/noisy input bridge | Keep preliminary or supplementary; not end-to-end perception. |
| Biological framing | Computational inspiration only, not a validated hippocampal theory. |
| Exp15 replay variant | Audit before citing as scientific evidence about replay. |
| Exp15 neural scope | Minimal fixed-profile comparator, not architecture search. |

## 6. Reproducibility And Provenance

Claim -> Exp15 includes runtime/hardware metadata, but has a manifest/SQLite provenance caveat.
Evidence -> `run_manifest.json` records runtime/hardware fields and `recovered_after_failed_sqlite_tail: true`; local SQLite inspection found an empty `run_manifest` table.
Caveat -> Treat CSV artifacts as authoritative unless a later audit says otherwise.
Source path -> `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/run_manifest.json`; `experiments/experiment15_neural_baseline_comparator/runs/exp15_full_20260508_092811.sqlite3`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.

Future manifests should preserve explicit runtime/hardware metadata:

```json
{
  "python_version": "...",
  "platform": "...",
  "processor": "...",
  "cpu_count": "...",
  "ram_gb": "...",
  "gpu_available": true,
  "gpu_name": "...",
  "cuda_version": "...",
  "torch_version": "...",
  "numpy_version": "...",
  "start_time_utc": "...",
  "end_time_utc": "...",
  "duration_seconds": "...",
  "git_commit": "...",
  "git_branch": "...",
  "command": "...",
  "profile": "validation|full"
}
```

## 7. License, Citation, And Release Metadata

Before public release or manuscript submission:

1. Choose a license.
2. Add `LICENSE`.
3. Add `CITATION.cff`.
4. Add repository citation instructions.
5. Optionally archive a release with Zenodo after manuscript/preprint stabilization.

License selection must remain a human decision.

## Recommended Work Order

1. Decide retained post-Exp15 main and supplementary claims.
2. Decide whether Exp15 is a compact main-text baseline table or supplementary neural comparator figure/table.
3. Run manuscript statistical hardening.
4. Generate final figure/table scripts and source-data manifests.
5. Import prior-art/novelty sources and verify related-work citations.
6. Add runtime metadata standards, license, and citation metadata.
7. Revisit whether optional memory-augmented neural baseline or Exp16-Exp20 work is still necessary.

## Numbering Posture

| Work item | Name | Required now? | Notes |
|---|---|---|---|
| Experiment 15 | Minimal Neural Baseline Comparator | Completed minimal evidence | Integrated with non-exhaustive, replay, and provenance caveats. |
| Analysis Pass 15A | Manuscript Statistical Hardening | Yes | Next analysis/documentation item; not a new experiment. |
| Repository Pass 15B | Submission Metadata and Reproducibility Hardening | Yes | Not a new experiment. |
| Optional neural baseline successor | Memory-augmented/key-value neural comparator | Venue-dependent | Only if target venue/reviewer posture requires broader neural coverage. |
| Experiment 16 | Lesion Diagnostic Audit | No | Only if positive lesion evidence is desired. |
| Experiment 17 | Perceptual / Continuous Applied Bridge | No | Future applied bridge. |
| Experiment 18 | Stochastic Context Corruption and Selection Margins | Optional | Only if generic robustness is elevated. |
| Experiment 19 | Consolidation Dose-Response Under Interference Pressure | No | Only if consolidation becomes central. |
| Experiment 20 or analysis-only pass | Seen-vs-Unseen Primitive Metric Cleanup | Optional | Needed only if C9 becomes central. |

## Bottom Line

Exp15 is complete as minimal neural evidence. Do not start additional new experiments by default. Most remaining limitations should be handled as scope discipline, statistical hardening, final source-data-backed figures/tables, prior-art import, and future-work framing rather than new experimental obligations.
