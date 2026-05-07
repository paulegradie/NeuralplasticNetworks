# Next Action Recommendation

## 1. Current state

The latest repository state records Experiment 13.1 as a completed internal publication-hardening run. It strengthened the recurrence/composition dissociation, structural-plasticity ablation, context-binding evidence, local-vs-global budget distinction, and freeze/plasticity diagnostic. It also exposed important caveats: the targeted-lesion diagnostic failed the expected pattern, external baselines remain absent, confidence intervals/effect sizes and final figure scripts remain open, and future manifests need explicit device/runtime metadata.

## 2. Manuscript blockers

- External baseline suite: still required before submission-readiness.
- Seed-level confidence intervals and effect sizes: required for manuscript-grade statistical reporting.
- Final figure scripts: required for reproducible paper figures.
- Exp13.1 lesion audit/rerun: required only if route-critical lesion evidence will be cited.
- Holdout metric cleanup: required if retaining seen/unseen primitive claims.
- Prior-art/novelty source import: required for a source-backed novelty section.
- Applied bridge: useful future work, but not the next blocker.

## 3. Candidate next actions

| Option | Description | Pros | Cons | Manuscript value | Risk |
|---|---|---|---|---|---|
| Exp13.1 lesion audit/rerun | Fix targeted critical-edge lesion diagnostic. | Repairs a suspicious result. | Optional if lesion evidence is not cited; may consume time without changing central spine. | Medium | Medium |
| Exp13.1 metric/figure cleanup | Add CIs/effect sizes and final plots. | Makes existing evidence cleaner. | Still leaves missing baselines. | High | Low |
| Experiment 13.2 baseline suite | Compare CIRM against explicit lookup, context-gated, memorization, replay, isolation, superposition, and non-plastic recurrence baselines. | Directly addresses C12, the largest reviewer blocker. | Symbolic baselines are not full neural baselines. | Very high | Medium |
| Manuscript draft v0 | Start writing the paper. | Helps narrative discipline. | Risks drafting around unsupported baseline claims. | Medium | Medium |
| Applied visual bridge | Move toward non-symbolic inputs. | Good future scope. | Premature before baselines. | Low for first manuscript | High |

## 4. Recommendation

Implement `experiments/experiment13_2_baseline_suite/` as the next experiment.

## 5. Why this is the next best action

External baselines are mandatory for the manuscript; lesion evidence is optional; applied bridge work is premature. A baseline suite lets the manuscript state clearly which aspects of CIRM are not explained by no-context lookup, whole-route memorization, recurrence alone, or finite-capacity conventional controls. It also honestly includes the oracle-like context-gated table baseline, which is important for reviewer trust.

## 6. Proposed design or task plan

- Proposed path: `experiments/experiment13_2_baseline_suite/`
- Purpose: run baseline comparison on the route-composition benchmark.
- Hypotheses:
  - H1: CIRM and explicit context-gated lookup solve clean seen/suffix composition.
  - H2: Shared no-context lookup fails at context-conflict route starts.
  - H3: Whole-route endpoint memorization solves seen routes but fails suffix routes composed of seen primitives.
  - H4: Recurrence-disabled CIRM preserves route-table accuracy but fails composed execution.
  - H5: Superposition/hash and finite-capacity baselines show collision/capacity degradation curves.
- Variants: CIRM full, CIRM no recurrence at eval, CIRM no structural plasticity, shared transition table, context-gated transition table, route endpoint memorizer, recurrent non-plastic rule, superposition hash tables, bounded LRU replay/no-replay, parameter-isolation table.
- Metrics: route-table accuracy, seen-route composition, suffix-route composition, first-step context accuracy, capacity used, evictions, hash collisions, seed-level CIs, effect sizes.
- Outputs: CSVs, SQLite DB, plots, manifest, progress JSONL, validation report.
- GPU/device plan: CPU-only symbolic experiment; manifest records device/runtime metadata and explicitly states no GPU is required.

## 7. Risks

- Context-gated lookup may match CIRM, requiring careful framing.
- Symbolic baselines may not satisfy reviewers asking for neural baselines.
- Suffix-route probes must be interpreted carefully because they test recomposition of seen primitives, not unseen primitive inference.
- Capacity baselines may need follow-up if they produce unexpected curves.

## 8. Success criteria

- Smoke, validation, and full scripts run without errors.
- Validation report has zero FAIL checks.
- CIRM full and context-gated table solve clean composition.
- Shared no-context baseline underperforms on context-conflict probes.
- Endpoint memorizer has a seen/suffix split.
- No-recurrence-at-eval preserves route-table accuracy while failing composition.
- Summary CSV contains CIs/effect-size outputs suitable for manuscript import.

## 9. Prompt for local agent

```text
Implement and run Experiment 13.2 as a self-contained baseline suite under `experiments/experiment13_2_baseline_suite/`.

Use the supplied implementation package as the source. First run:

powershell -ExecutionPolicy Bypass -File .\start_exp13_2_smoke.ps1

If smoke passes, run:

powershell -ExecutionPolicy Bypass -File .\start_exp13_2_validation.ps1

If validation passes, run:

powershell -ExecutionPolicy Bypass -File .\start_exp13_2_full.ps1

Do not modify prior experiment artifacts. Each run must create a new `analysis/<run_id>/` directory and a new `runs/<run_id>.sqlite3` database. After the full run, upload the full analysis directory for review. Do not import claims into manuscript docs until the run has been analyzed.
```
