# Manuscript Finalization Plan

Purpose: convert the current limitation/threat register into a practical manuscript-finalization plan.

Controlling inputs:

- `docs/manuscript/draft/MANUSCRIPT_V1.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/experiments/exp13_2_summary.md`
- `docs/experiments/exp14_summary.md`

## Executive strategy

Do not try to solve every limitation before submission. Split the remaining work into four tracks:

| Track | Purpose | Manuscript blocking? |
|---|---|---|
| A. Claim and manuscript hygiene | Prevent overclaiming and keep the manuscript scoped as a controlled symbolic/mechanistic benchmark. | Yes |
| B. Metric/statistical cleanup | Ensure every central claim has clean seed-level uncertainty, effect-size, source-data, and figure provenance. | Yes |
| C. Experiment 15 neural comparator | Address the largest remaining baseline vulnerability: absence of ordinary neural sequence-model comparators. | Yes, if targeting a stronger ML/computational venue; highly recommended regardless. |
| D. Optional boundary experiments | Address lesion, stochastic robustness, consolidation, or applied bridge only if those claims are elevated. | No |

Recommended immediate next action: **Experiment 15: Minimal Neural Baseline Comparator**.

The manuscript should continue to avoid claims of solved continual learning, neural-network superiority, raw sensory latent-world discovery, end-to-end perception, broad biological proof, broad abstract rule induction, or unseen primitive inference.

---

## 1. Baseline coverage still incomplete

### Current risk

Exp13.2 provides a completed symbolic/algorithmic baseline suite, but does not supply neural baselines or fully close prior-art/novelty positioning.

### Associated work

- Existing evidence: Exp13.2.
- New work: **Experiment 15 — Minimal Neural Baseline Comparator**.
- Documentation work: prior-art/novelty import and related-work verification.

### Plan

Run a deliberately scoped neural comparator suite against the existing route-memory probes.

Minimum neural variants:

1. GRU/LSTM endpoint model.
2. GRU/LSTM rollout model.
3. Small Transformer sequence model.
4. Neural one-step transition model, such as MLP/embedding model for `(context, state, action) -> next_state`, rolled out recurrently.
5. Replay-trained neural baseline.
6. Parameter-isolated neural baseline using world-specific heads/adapters/masks.

Optional, only if inexpensive:

7. Neural key-value or memory-augmented lookup baseline.

Metrics must align to the manuscript vocabulary:

- one-step route-table / transition accuracy;
- seen-route composition accuracy;
- suffix-route composition accuracy;
- first-step context-conflict accuracy;
- retention after sequential worlds;
- route-length scaling;
- world-count scaling;
- train/runtime cost;
- seed-level confidence intervals and effect sizes.

### Acceptance posture

Experiment 15 does not need CIRM to beat every neural model. Its job is to clarify the comparison boundary.

| Outcome | Manuscript consequence |
|---|---|
| Neural baselines fail badly. | Strengthens the controlled-mechanism result. |
| Neural baselines solve clean supplied-context routes but fail suffix/context/retention probes. | Strong support for the storage/execution/context decomposition. |
| Neural baselines match CIRM with generous training. | Manuscript remains viable as transparent mechanism/benchmark paper, but drops performance-superiority language. |
| Neural baselines dominate CIRM. | Pivot to CIRM as interpretable diagnostic mechanism and benchmark, not superior model. |

---

## 2. Symbolic benchmark limitation

### Current risk

Most evidence is from synthetic symbolic nodes, modes, worlds, and routes.

### Plan

Do not try to solve this for the first manuscript. Keep the scope explicit.

Safe language:

> This benchmark intentionally uses symbolic route systems to isolate storage, context indexing, and recurrent execution. It is not a claim about end-to-end perceptual learning or naturalistic navigation.

No new experiment is required. A richer non-symbolic or perceptual task should be future work.

---

## 3. Oracle context / world-label limitation

### Current risk

Many experiments supply the world/context label directly. This tests context-indexed storage, not latent world inference.

### Plan

Split the manuscript story into two clearly labeled regimes:

1. **Supplied-context route memory** — tests whether context-indexed storage prevents interference.
2. **Symbolic transition-cue context selection** — Exp14 tests whether the active symbolic world can be selected from partial transition evidence before route execution.

Keep the oracle context-gated table as an upper-bound comparator, not as a defeated competitor.

No further experiment is required unless the manuscript attempts to claim raw sensory latent-world discovery, which it should not.

---

## 4. Latent context inference remains symbolic

### Current risk

Exp14 reduces the oracle-label criticism, but only inside symbolic transition-cue evidence. It does not show raw sensory latent-world discovery.

### Plan

Treat Exp14/C13 as main text or high-priority supplement. Recommended placement: **main text**, because it directly addresses the oracle-context criticism.

Required asset work:

- final figure script for Exp14/C13;
- source-data mirror for retained panels;
- implementation note explaining cue count, cue corruption, world scoring, and route execution after context selection;
- caption caveat that oracle context-gated lookup remains an upper bound.

Safe language:

> symbolic transition-cue context selection

Avoid unqualified:

> latent context discovery

---

## 5. Metric cleanup requirements

### Current risk

Central claims can be weakened if metrics combine incompatible cases, omit seed-level uncertainty, or cite candidate analysis plots instead of reproducible final assets.

### Plan

Create a manuscript statistical hardening pass. This is not a new experiment.

Required outputs:

- `docs/source_data/SOURCE_DATA_MANIFEST.csv` updated for all final panels;
- `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` updated;
- `docs/manuscript/tables/table_03_statistical_summary.md` reviewed and aligned;
- final figure source-data CSVs;
- scripts that regenerate final manuscript stats from experiment artifacts.

Acceptance criteria for every retained central claim C1-C7 and C13:

- mean;
- standard deviation or standard error;
- 95% confidence interval;
- seed count;
- effect size for direct comparisons;
- source artifact path;
- figure/table reference.

C9 must stay out of the main claim set unless seen/unseen/all route-table and composition split metrics are cleaned.

---

## 6. Exp13.1 lesion diagnostic failure

### Current risk

The targeted critical-edge lesion diagnostic does not currently support positive route-critical-structure evidence.

### Plan

Do not use positive lesion evidence in the first manuscript.

Recommended first-manuscript handling:

- Drop positive lesion claim.
- Mention only as a negative diagnostic if needed.
- Do not include in main figures.

Optional future work: **Experiment 16 — Lesion Diagnostic Audit**.

If audited, test:

1. whether critical-edge selection identifies edges used by evaluated routes;
2. whether targeted and random lesions are count-matched and degree-matched;
3. whether lesioning route-critical edges actually removes active transitions;
4. whether redundancy/multiple-path effects explain weak targeted sensitivity;
5. whether the failure is conceptual, implementation-level, or regime-specific.

Only use lesion evidence if targeted route-relevant lesions produce stronger and interpretable degradation than matched random controls.

---

## 7. No overclaiming biological theory

### Current risk

The model is biologically inspired, but the experiments do not validate a complete hippocampal or neural theory.

### Plan

Perform a language pass.

Use:

- computationally inspired by indexing, remapping, recurrence, and structural plasticity;
- mechanistically analogous to selected memory-system ideas;
- controlled symbolic benchmark.

Avoid:

- the brain does this;
- hippocampal mechanism, unless explicitly framed as inspiration;
- biologically validated;
- neural explanation.

No new experiment is required.

---

## 8. Applied bridge remains preliminary

### Current risk

Exp13 continuous/noisy input tests whether a decoded noisy start state can feed route memory. It does not show learned perception or an end-to-end applied model.

### Plan

Keep this as supplementary or discussion-only.

Do not elevate it unless running a future perceptual bridge experiment.

Optional future work: **Experiment 17 — Perceptual / Continuous Applied Bridge**.

A real applied bridge would need:

- visual or gridworld state observations;
- learned encoder;
- route-memory backend;
- ordinary neural end-to-end baselines;
- noise/occlusion tests;
- analysis separating perception failure from memory failure.

Not recommended before first manuscript submission.

---

## 9. Context corruption is not fully realistic yet

### Current risk

Existing corruption tests are useful failure evidence but do not establish generic stochastic robustness.

### Plan

Keep as supplement unless generic robustness is claimed.

Optional future work: **Experiment 18 — Stochastic Context Corruption and Selection Margins**.

If run, include:

- random missing context cues;
- random wrong-world cue injection;
- mixed true/wrong/noise cues;
- ambiguous cues shared across worlds;
- increasing world counts;
- increasing route lengths.

Metrics:

- top-1 world selection;
- top-2 margin;
- entropy over world scores;
- composition accuracy;
- first-step context-conflict accuracy;
- corruption probability curve;
- seed-level confidence intervals.

Safe current wording:

> The model is sensitive to corrupted symbolic cue evidence, especially when wrong-world evidence dominates.

Avoid:

> generic stochastic robustness

unless Experiment 18 is run.

---

## 10. Consolidation claim is fragile

### Current risk

The evidence supports consolidation as a possible stability/plasticity bias, not as a universally necessary or accuracy-rescuing mechanism.

### Plan

Keep consolidation supplementary.

Safe wording:

> Consolidation-like mechanisms may bias stability/plasticity tradeoffs under some regimes.

Avoid:

> Consolidation is required.

Avoid:

> Consolidation rescues capacity pressure.

Optional future work: **Experiment 19 — Consolidation Dose-Response Under Interference Pressure**.

Not recommended before first manuscript submission.

---

## 11. Exp13.1 reproducibility metadata gap

### Current risk

Earlier runs passed validation but do not always capture explicit runtime/hardware metadata.

### Plan

Add runtime/hardware metadata to all future run manifests, beginning with Experiment 15.

Minimum manifest fields:

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

For older experiments, add a documentation note rather than trying to reconstruct unavailable runtime metadata.

---

## 12. License and citation metadata missing

### Current risk

The repository lacks formal reuse/citation metadata.

### Plan

Before public release or manuscript submission:

1. choose license;
2. add `LICENSE`;
3. add `CITATION.cff`;
4. add repository citation instructions;
5. optionally archive a release with Zenodo after manuscript/preprint stabilization.

License selection must remain a human decision. Candidate default: Apache-2.0 if a permissive license with explicit patent language is desired.

---

## Recommended work order

1. Design and implement Experiment 15 without executing the full run.
2. Run Exp15 smoke/validation locally.
3. Run Exp15 full profile only after validation passes.
4. Import Exp15 analysis into manuscript docs.
5. Run manuscript statistical hardening pass.
6. Generate final figure scripts and source-data manifests.
7. Add runtime metadata standards, license, and citation metadata.
8. Revisit whether optional Exp16-Exp19 are still necessary.

## Numbering posture

| Work item | Name | Required now? | Notes |
|---|---|---|---|
| Experiment 15 | Minimal Neural Baseline Comparator | Yes / highly recommended | Next scientific item. |
| Analysis Pass 15A | Manuscript Statistical Hardening | Yes | Not a new experiment. |
| Repository Pass 15B | Submission Metadata and Reproducibility Hardening | Yes | Not a new experiment. |
| Experiment 16 | Lesion Diagnostic Audit | No | Only if positive lesion evidence is desired. |
| Experiment 17 | Perceptual / Continuous Applied Bridge | No | Future applied bridge. |
| Experiment 18 | Stochastic Context Corruption and Selection Margins | Optional | Only if generic robustness is elevated. |
| Experiment 19 | Consolidation Dose-Response Under Interference Pressure | No | Only if consolidation becomes central. |
| Experiment 20 or analysis-only pass | Seen-vs-Unseen Primitive Metric Cleanup | Optional | Needed only if C9 becomes central. |

## Bottom line

Run Experiment 15 next. Do not start additional new experiments until Exp15 has been analyzed and the manuscript claim posture has been updated. Most remaining limitations should be handled as scope discipline, statistical hardening, or future work rather than as new experimental obligations.
