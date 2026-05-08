# Post-Exp15 Claim Freeze Addendum

Status: placeholder artifact for post-Exp15 claim hardening.

This file exists so finalization documents can reference the post-Exp15 claim-freeze path without breaking documentation path verification. The next manuscript-finalization pass should replace this placeholder with the final Claim -> Evidence -> Caveat -> Source path addendum.

## Required addendum scope

The addendum should record the following post-Exp15 changes:

### C1 - Structural route storage

Claim -> Structural route storage remains supported only as a benchmark/model-family claim.

Evidence -> CIRM ablations and symbolic baselines show collapse when structural route storage is removed.

Caveat -> Exp15 shows a context-conditioned neural transition MLP and world-head transition MLP can solve the clean hard slice, so C1 must not be worded as a universal requirement for all route-memory systems.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

### C2 - Context/world indexing

Claim -> Context/world indexing is required for incompatible local transitions and first-step/full-route disambiguation in this benchmark.

Evidence -> No-context variants fail conflict-sensitive first-step/full-route probes.

Caveat -> No-context transition MLP can solve suffix composition where suffix probes bypass the conflicting first transition, so context should not be framed as necessary for every suffix transition.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

### C4 - Storage, endpoint memorization, and composition dissociation

Claim -> Exp15 strengthens the separation between endpoint memorization and reusable transition composition.

Evidence -> Endpoint neural models can perform well on seen full routes while showing weak suffix-route composition and low transition accuracy.

Caveat -> Exact retained numbers should be sourced from the final Exp15 table/source-data artifact.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`.

### C12 - Baseline coverage

Claim -> Minimal neural comparator coverage is now present.

Evidence -> Exp15 completed a fixed-profile neural comparator suite.

Caveat -> Exp15 is not exhaustive neural benchmarking and omits memory-augmented/key-value neural baselines.

Source path -> `docs/experiments/exp15_summary.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.

### Non-claim: Exp15 replay collapse

Claim -> None retained pending audit.

Evidence -> The replay variant shows near-zero hard-slice performance.

Caveat -> Treat as requiring implementation/training-regime audit before scientific interpretation.

Source path -> `docs/threads/experiment15_analysis_digest.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`.
