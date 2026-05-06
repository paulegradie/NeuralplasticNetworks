# Prompt: Design Next Experiment

```text
You are helping design the next experiment in the Context-Indexed Route Memory research program.

Repository context:
- Experiments live under `experiments/`.
- New protocols or successor designs must get a new normalized directory under `experiments/`.
- Reruns of the same protocol stay inside the owning experiment directory.
- Do not create new root-level experiment directories.
- Each experiment should own its code, runners, analysis scripts, `runs/`, `analysis/`, docs, and `README.md`.
- Manuscript/evidence docs live under `docs/`.
- Current canonical claim map: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`.
- Current limitations: `docs/manuscript/LIMITATIONS_AND_THREATS.md`.
- Current next experiments: `docs/synthesis/NEXT_EXPERIMENTS.md`.
- Current manuscript status: promising but not submission-ready.
- Evidence discipline: Claim -> Evidence -> Caveat -> Source path.
- Active source paths should use current `experiments/...` prefixes, or be explicitly marked planned, missing, future, or local verification pending.
- Completed runs are immutable. If SQLite is used, plan one database file per completed run under the owning experiment directory.
- New experiments should use available GPUs by default where practical; use `check_gpu_status.py` as the local visibility reference and document CPU-only or partial-GPU limitations.
- Before choosing documentation names, inspect `docs/experiments/EXPERIMENT_REGISTRY.md` and existing summaries.

Your task:
Design the next experiment as a rigorous scientific protocol.

Do not write implementation code unless explicitly asked.
Do not overclaim expected results.
Do not assume prior results beyond the provided repo context.
Design the experiment so that it can be implemented as a new self-contained directory under `experiments/`.
State whether this is a new protocol, a successor protocol, or a rerun of an existing protocol.

The experiment should include:

# Experiment <ID>: <short descriptive title>

Proposed directory: `experiments/<experiment_dir>/`

## 1. Purpose

What precise scientific or manuscript-readiness problem does this experiment solve?

## 2. Background and motivation

Explain how this experiment follows from the current research arc.

Reference the relevant current claims:
- structural plasticity;
- world/context indexing;
- recurrence;
- route-table/composition dissociation;
- capacity pressure;
- consolidation/stability-plasticity;
- primitive holdout;
- context corruption;
- baselines or applied bridge if relevant.

## 3. Primary hypothesis

State the main testable hypothesis.

## 4. Secondary hypotheses

List secondary hypotheses.

## 5. What would falsify or weaken the hypothesis?

Be explicit. Include results that would force us to revise the theory.

## 6. Model variants / baselines

For each variant:

| Variant | Purpose | Expected behavior | Relevant claim | Caveat |
|---|---|---|---|---|

## 7. Experimental conditions

Include:
- world counts;
- route lengths;
- nodes;
- modes;
- seeds;
- GPU/device plan and expected CPU/GPU split;
- memory budget / capacity conditions if relevant;
- context corruption conditions if relevant;
- train/test splits;
- holdout definitions;
- run profiles: smoke, standard, full.

## 8. Metrics

For each metric:

| Metric | Meaning | Why it matters | Expected pattern | Caveat |
|---|---|---|---|---|

Include where relevant:
- composition accuracy;
- route-table accuracy;
- route-table accuracy all/seen/unseen;
- composition accuracy seen routes;
- composition accuracy unseen-required routes;
- composition-route gap;
- top-1 world accuracy;
- world margin;
- wrong-world activation;
- retention by world age;
- capacity law / failure threshold;
- confidence intervals / effect sizes.

## 9. Required plots

List plots and what claim each supports.

## 10. Generated artifacts

The implementation should produce:
- `experiments/<experiment_dir>/runs/<run_id>.sqlite3` if SQLite is used;
- `experiments/<experiment_dir>/analysis/<run_id>/metrics.csv`;
- summary CSVs;
- plots under `experiments/<experiment_dir>/analysis/<run_id>/plots/`;
- `experiments/<experiment_dir>/analysis/<run_id>/experiment_report.md`;
- `experiments/<experiment_dir>/analysis/<run_id>/validation_report.md`;
- `experiments/<experiment_dir>/analysis/<run_id>/run_manifest.json` or equivalent.

## 11. Validation checks

Define pass/warn/fail checks.

## 12. Manuscript relevance

Which claims could this experiment support, weaken, or modify?

## 13. Risks and interpretation hazards

Include:
- ceiling effects;
- oracle context;
- ambiguous baselines;
- metric leakage;
- insufficient seeds;
- overclaiming biological relevance.

## 14. Repository integration plan

After analysis, which docs must be updated?

Include:
- owning experiment `README.md`, especially completed runs/results;
- `docs/experiments/<experiment_id>_summary.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`

## 15. Implementation handoff

End with a concise implementation checklist suitable for a local Codex agent.

Important:
Keep the design narrow enough to execute locally.
Prefer scientifically decisive experiments over sprawling experiments.
```
