# Thread Digest: Experiment 15 Neural Baseline Comparator

Status: **placeholder / pending local run analysis**.

This digest exists so repository documentation references resolve while Experiment 15 is implemented but not yet executed locally. It should be replaced or substantially updated after Paul uploads the generated Experiment 15 analysis artifacts in a dedicated analysis thread.

## 1. Thread scope

Pending.

The future analysis thread should cover the local execution, validation, analysis, and manuscript interpretation of:

```text
experiments/experiment15_neural_baseline_comparator/
```

Expected uploaded input after local execution:

```text
experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_<timestamp>/
```

## 2. Experiments discussed

### Experiment 15 — Minimal Neural Baseline Comparator

Purpose:

Test whether standard neural sequence models trained under comparable symbolic route-memory conditions reproduce, fail, or partially reproduce the storage, context separation, retention, suffix-route composition, and first-step context-conflict behavior observed in Context-Indexed Route Memory.

Current state:

- Implementation exists.
- Local result artifacts have not yet been imported.
- No manuscript claims should cite Exp15 result evidence yet.

## 3. Experimental designs created or modified here

Pending final analysis-thread details.

Implemented design currently includes:

- GRU endpoint model with context;
- GRU endpoint model without context;
- GRU rollout model with context;
- GRU rollout model without context;
- small attention/Transformer-style endpoint model with context;
- one-step transition MLP with context;
- one-step transition MLP without context;
- sequential-world replay transition MLP;
- parameter-isolated transition MLP with world-specific heads.

Key metrics planned:

- one-step transition accuracy;
- seen-route composition accuracy;
- suffix-route composition accuracy;
- first-step context-conflict accuracy;
- retention after sequential worlds;
- route-length scaling;
- world-count scaling;
- train/runtime cost;
- seed-level confidence intervals and effect sizes.

## 4. Results analyzed here

Pending.

Use this format after results exist:

Claim:
Evidence:
Caveat:
Source artifact or conversation reference:

## 5. Key scientific conclusions supported by this thread

Pending.

No scientific conclusions are currently supported by this placeholder document.

## 6. Important flaws, mistakes, or implementation concerns identified

Pending.

The future analysis thread should explicitly check:

- whether all required variants completed;
- whether context and no-context variants differ only by context availability;
- whether suffix routes were withheld as full-route endpoint training examples;
- whether replay and parameter-isolation metadata are explicit;
- whether metrics are finite and in valid ranges;
- whether neural models are undertrained, overfit, or capacity-limited in ways that affect interpretation;
- whether runtime makes the full profile practical;
- whether the optional neural key-value / memory-augmented baseline remains safely out of scope.

## 7. Repository/manuscript follow-up after results exist

After Experiment 15 results are analyzed, update:

- `docs/experiments/exp15_summary.md`;
- this digest;
- `docs/experiments/EXPERIMENT_REGISTRY.md`;
- `docs/manuscript/BASELINE_REQUIREMENTS.md`;
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`;
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`;
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` or a post-Exp15 claim freeze;
- `docs/synthesis/PUBLICATION_READINESS.md`;
- `docs/synthesis/NEXT_EXPERIMENTS.md`;
- finalization checklist entries.
