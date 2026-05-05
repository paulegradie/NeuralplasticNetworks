# Thread Digest: Contextual Route Fields, Self-Organizing Plasticity, Robustness, and Adaptive Memory

## 1. Thread scope

This thread functioned as an analysis-and-experiment-design thread for the **Biological Neural Nets / NeuralplasticNetworks** research program. The core activity was to move from a weak contextual successor result in **Experiment 5** toward a sequence of diagnostic and mechanistic experiments testing whether a biologically inspired, recurrent, structurally plastic route-field model can:

1. learn local transition routes;
2. compose those routes recurrently;
3. keep multiple context-conditioned route families separate;
4. remain robust under context interference and noisy/delayed feedback;
5. adapt after rule reversal;
6. eventually support context-separated memory without destructive overwrite.

The thread began with the framing that the project is about **stateful, dynamically routed neural computation**, where computation is an activity-dependent path through a large population of possible latent units rather than a fixed dense forward pass. That framing is consistent with the project document, which describes the work as exploring whether dynamically routed, sparse, adaptive computation can bridge conventional artificial neural networks and biologically inspired neural systems. 

A major outcome of the thread was the design, implementation, validation, and analysis pipeline for **Experiments 7–11**, with Experiment 11 implemented but not yet locally analyzed in this thread.

---

## 2. Experiments discussed

| Experiment  | Short description                                                                                                                             | Status in this thread                                                                                                             |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Exp1 / Exp2 | Sparse plastic MNIST baseline experiments.                                                                                                    | Discussed only as project background. Not analyzed here.                                                                          |
| Exp3        | Recurrent MNIST suite; recurrence measurable but not clearly useful on MNIST.                                                                 | Discussed only as background.                                                                                                     |
| Exp4        | Successor traversal experiment showing recurrence and structural plasticity become load-bearing when traversal is required.                   | Discussed as prior motivation for Exp5.                                                                                           |
| Exp5        | Contextual successor world: choose among `plus_one`, `plus_two`, `minus_one` transition systems under context.                                | Results analyzed; judged mechanistic partial success but capability failure.                                                      |
| Exp6        | Multimodal number grounding.                                                                                                                  | Deferred; not run or designed in this thread beyond being repeatedly postponed.                                                   |
| Exp7        | Route Field Diagnostics. Tests whether clean route fields compose and which mechanisms fail when ablated.                                     | Designed, implemented, validated, run locally by user, analyzed.                                                                  |
| Exp8        | Self-Organizing Contextual Route Acquisition. Tests whether local plasticity can acquire clean route fields from one-step experience.         | Designed, implemented, validated, run locally by user, analyzed.                                                                  |
| Exp9        | Robust Adaptive Route Plasticity. Tests inhibition under context interference and reward/eligibility mechanisms under noisy/delayed feedback. | Designed, implemented, validated, run locally by user, analyzed.                                                                  |
| Exp10       | Rule Reversal, Retention, and Adaptive Rebinding. Tests adaptation, consolidation, overwrite, and preliminary dual-world memory.              | Designed, implemented, validated, run locally by user, analyzed.                                                                  |
| Exp11       | Context-Separated Memory and Non-Destructive Rebinding. Tests whether higher-order world context can preserve multiple route systems.         | Designed and implemented with logging; validation run performed by assistant; local user results not yet analyzed in this thread. |

---

## 3. Experimental designs created or modified here

### Experiment 7 — Route Field Diagnostics

**Purpose:**
Create a diagnostic follow-up to Exp5 to determine whether contextual traversal fails because of one-step transition learning, recurrent composition, context binding, final-state decoding, or route-field purity.

**Hypothesis:**
If a clean context-conditioned route field exists, recurrence should compose it across multi-step paths; without recurrence, the model may know one-step transitions but fail multi-step composition.

**Model variants:**

| Variant                         | Purpose                                                             |
| ------------------------------- | ------------------------------------------------------------------- |
| `exp7_full_route_field`         | Clean route-field model.                                            |
| `exp7_no_recurrence`            | Tests whether recurrence is required for composition.               |
| `exp7_no_context_binding`       | Tests whether route families collide without context binding.       |
| `exp7_no_structural_plasticity` | Tests whether route field formation requires structural plasticity. |
| `exp7_no_inhibition`            | Tests whether inhibition improves route purity.                     |
| `exp7_context_bleed`            | Tests margin degradation under context leakage.                     |
| `exp7_noisy_plasticity`         | Tests tolerance to plasticity noise.                                |

**Metrics:**

* transition accuracy;
* composition accuracy;
* route-table accuracy;
* mean target rank;
* correct-route margin;
* context margin;
* wrong-route activation;
* composition accuracy by mode;
* composition accuracy by path length;
* deterministic baselines.

**Expected outcomes:**

* Full route field should compose perfectly if the local route table is clean.
* No recurrence should preserve one-step transition accuracy but fail composition.
* No structural plasticity should fail route-table formation.
* No context binding should produce route collisions.
* No inhibition may still solve clean tasks but should reduce margins.

**Implementation notes:**

* Implemented as `experiment7_route_field_diagnostics.zip`.
* Included `start.ps1`.
* `start.ps1` used Python from the virtual environment one directory up: `..\.venv\Scripts\python.exe`.
* A small validation run was executed before packaging.
* A later unsaturated run was recommended with larger `max-number`, longer paths, fewer repeats, and more seeds.

**Known risks:**

* Initial saturated run had very large margins and was too easy.
* Exp7 was diagnostic, not yet proof of self-organizing route acquisition.
* The clean route table might be too scaffolded relative to the richer biological model.

---

### Experiment 8 — Self-Organizing Contextual Route Acquisition

**Purpose:**
Bridge Exp5 and Exp7 by testing whether a local plastic graph can **acquire** a context-conditioned route field from one-step transition experience, then use recurrence to solve unseen multi-step composition.

**Hypothesis:**
A recurrent graph with context-bound structural plasticity can acquire local transition routes from sparse one-step experience; once route margins are sufficient, recurrent traversal composes those routes to solve unseen multi-step queries.

**Model variants:**

| Variant                                 | Purpose                                                             |
| --------------------------------------- | ------------------------------------------------------------------- |
| `exp8_full_self_organizing_route_field` | Main model.                                                         |
| `exp8_no_recurrence`                    | Tests whether one-step learning is insufficient for composition.    |
| `exp8_no_structural_plasticity`         | Tests whether rewiring is required for acquisition.                 |
| `exp8_no_context_binding`               | Tests route collision without context binding.                      |
| `exp8_no_inhibition`                    | Tests route purity/margin effects.                                  |
| `exp8_no_homeostasis`                   | Tests stability mechanism in clean setting.                         |
| `exp8_no_reward_gate`                   | Tests whether reward gating matters under clean immediate feedback. |
| `exp8_context_bleed`                    | Tests context interference and margin degradation.                  |

**Metrics:**

* transition accuracy;
* route-table accuracy;
* composition accuracy;
* composition accuracy by path length;
* composition accuracy by mode;
* mean target rank;
* correct-route margin;
* context margin;
* wrong-route activation;
* failure taxonomy;
* exposure curve outputs.

**Expected outcomes:**

* Full model should learn from one-step examples and compose unseen paths.
* No recurrence should learn transitions but fail composition.
* No structural plasticity should be near random.
* No context binding should show route collision.
* Context bleed should weaken margins and degrade composition with path length.
* No reward gate and no homeostasis may not matter under clean immediate feedback.

**Implementation notes:**

* Implemented as `experiment8_self_organizing_route_acquisition.zip`.
* Final runner: `start_exp8.ps1`.
* Local run configured with `--path-train-repeats 0`, ensuring no direct multi-step composition training.
* Validated with a small run before packaging.

**Known risks:**

* Exposure curve initially only used `exposure_repeats=1`, so it did not yet measure a true exposure threshold.
* Reward gating and homeostasis were not meaningfully stressed in the clean setting.

---

### Experiment 9 — Robust Adaptive Route Plasticity

**Purpose:**
Stress the Exp8 mechanism with context interference, noisy feedback, and delayed reward. Specifically, test whether inhibition and reward/eligibility mechanisms become load-bearing under the right stressors.

**Hypothesis:**
Inhibition protects context-bound route fields under interference; reward gating and eligibility traces protect route acquisition under noisy or delayed feedback.

**Model variants:**

| Variant                         | Purpose                                  |
| ------------------------------- | ---------------------------------------- |
| `exp9_full_interference_robust` | Full model under context bleed.          |
| `exp9_no_inhibition`            | Tests route purity under interference.   |
| `exp9_no_context_binding`       | Tests route collision.                   |
| `exp9_no_structural_plasticity` | Tests route acquisition failure.         |
| `exp9_full_reward_robust`       | Full model under noisy/delayed feedback. |
| `exp9_no_reward_gate`           | Tests feedback-noise robustness.         |
| `exp9_no_eligibility_trace`     | Tests delayed reward assignment.         |
| `exp9_no_recurrence`            | Tests composition requirement.           |

**Metrics:**

* transition accuracy;
* composition accuracy;
* route-table accuracy;
* correct-route margin;
* context margin;
* wrong-route activation;
* failure taxonomy;
* composition under context bleed;
* route-table accuracy under feedback noise;
* correct margin under feedback noise;
* composition under reward delays.

**Expected outcomes:**

* Full model should degrade more gracefully than no-inhibition under context bleed.
* No context binding should remain poor.
* Reward gating should preserve margin under noisy feedback.
* Eligibility trace should be critical under delayed feedback.
* No recurrence should learn local transitions but fail composition.
* No structural plasticity should remain random-like.

**Implementation notes:**

* Implemented as `experiment9_robust_adaptive_route_plasticity.zip`.
* Final runner: `start_exp9.ps1`.
* Local run used `--phases interference feedback`.
* Context bleed sweep: `0 0.05 0.10 0.20 0.35 0.50`.
* Feedback noise sweep: `0 0.05 0.10 0.20 0.30`.
* Reward delay sweep: `0 2 4`.
* Validated with a small run before packaging.

**Known risks:**

* `predictions.csv` generated by the run was very large, about 434 MB.
* Raw predictions were judged unnecessary for aggregate interpretation.
* A preprocessing script was recommended if detailed trajectory-level failure analysis is later needed.

---

### Experiment 10 — Rule Reversal, Retention, and Adaptive Rebinding

**Purpose:**
Test whether a learned route field can adapt when rule meanings change, and whether consolidation controls the stability-plasticity tradeoff.

**Hypothesis:**
Plastic route fields can be rebound when task contingencies change. Consolidation should preserve old routes but slow adaptation; low consolidation should adapt quickly but risk overcommitment or forgetting. Higher-level context may support multiple coexisting rule worlds.

**Model variants:**

| Variant                          | Purpose                                                               |
| -------------------------------- | --------------------------------------------------------------------- |
| `exp10_full_adaptive_reversal`   | Main adaptive reversal model.                                         |
| `exp10_no_structural_plasticity` | Tests whether adaptation requires plasticity.                         |
| `exp10_no_reward_gate`           | Mostly meaningful under noisy reversal; neutral in clean run.         |
| `exp10_no_eligibility_trace`     | Mostly meaningful under delayed reversal; neutral in clean run.       |
| `exp10_no_inhibition`            | Tests old-route interference and route purity.                        |
| `exp10_no_homeostasis`           | Tests stability.                                                      |
| `exp10_no_consolidation`         | Fast adaptation, high forgetting/overcommitment.                      |
| `exp10_strong_consolidation`     | Strong retention, slow or blocked adaptation.                         |
| `exp10_dual_context_worlds`      | Tests whether higher-level context can support multiple rule systems. |

**Metrics:**

* old-rule A composition accuracy;
* new-rule B composition accuracy;
* old-rule A route-table accuracy;
* new-rule B route-table accuracy;
* correct-route margin;
* wrong-route activation;
* final new-rule failure taxonomy;
* adaptation thresholds;
* switchback performance.

**Expected outcomes:**

* Full model should learn A, then adapt to B.
* No structural plasticity should fail.
* Strong consolidation should retain A but resist B.
* No consolidation should adapt quickly but forget or overcommit.
* Dual-context worlds may preserve or recover both A and B.
* Reward gate and eligibility trace may be neutral in clean immediate-feedback reversal.

**Implementation notes:**

* Implemented as `experiment10_adaptive_reversal.zip`.
* Final runner: `start_exp10.ps1`.
* Default run used:

  * `--initial-exposure-repeats 1`;
  * `--reversal-exposure-schedule "0 1 2 3 5 8 13 21"`;
  * `--switchback-exposure-schedule "0 1 2 3 5 8 13"`;
  * `--seeds 30`;
  * `--phases reversal switchback`.
* Raw predictions were disabled by default.

**Known risks:**

* Clean run used `feedback_noise=0` and `reward_delay_steps=0`, so reward gate and eligibility trace were not stressed.
* Dual-context result was promising but ambiguous: A was not retained during B learning, but both A and B were accessible after switchback.
* Strong consolidation may have been too strong, blocking B acquisition almost entirely.

---

### Experiment 11 — Context-Separated Memory and Non-Destructive Rebinding

**Purpose:**
Test whether higher-order world context can bind route fields into separable memory worlds so that new rules can be learned without destroying old ones.

**Hypothesis:**
A higher-order context signal can bind route fields into separable memory worlds, allowing the same mode labels to have different transition semantics in different task contexts without destructive overwrite.

**Model variants:**

| Variant                               | Purpose                                                     |
| ------------------------------------- | ----------------------------------------------------------- |
| `exp11_full_context_separated_memory` | Main non-destructive memory model.                          |
| `exp11_world_gated_plasticity`        | Restricts plastic updates to active world context.          |
| `exp11_no_world_context`              | Tests whether world context is necessary.                   |
| `exp11_no_context_binding`            | Tests binding failure.                                      |
| `exp11_no_inhibition`                 | Tests wrong-world suppression.                              |
| `exp11_no_structural_plasticity`      | Tests acquisition failure.                                  |
| `exp11_no_consolidation`              | Tests fast learning / forgetting.                           |
| `exp11_strong_consolidation`          | Tests high retention / slow acquisition.                    |
| `exp11_shared_edges_only`             | Tests route collision when worlds share too much substrate. |

**Metrics:**

* per-world route-table accuracy;
* per-world composition accuracy;
* retention index;
* acquisition index;
* wrong-world activation;
* separation score;
* world-context margin;
* failure taxonomy;
* context-noise robustness;
* scaling across worlds A/B/C/D.

**Expected outcomes:**

* Full context-separated memory should learn B while retaining A.
* No world context should learn B but overwrite or collide with A.
* No structural plasticity should remain near random.
* World-gated plasticity should improve non-destructive retention.
* No inhibition should show higher wrong-world activation.
* Multi-world scaling should reveal capacity limits.

**Implementation notes:**

* Implemented as `experiment11_context_memory.zip`.
* Final runner: `start_exp11.ps1`.
* Explicit progress logging added:

  * `analysis/exp11/exp11_run.log`;
  * `analysis/exp11/progress.jsonl`.
* Default run:

  * `--phases sequential alternating scaling context_noise`;
  * `--worlds "A B C D"`;
  * `--seeds 30`;
  * `--new-world-exposure-schedule "0 1 2 3 5 8 13 21"`;
  * `--alternation-cycles 21`;
  * `--context-bleed-sweep "0 0.05 0.10 0.20 0.35"`;
  * `--context-dropout-sweep "0 0.05 0.10 0.20"`.
* Validated by assistant with a small run before packaging.
* Full local results were not analyzed in this thread.

**Known risks:**

* May reveal that multiple worlds require too much manual isolation.
* World-gated plasticity may be too engineered relative to biological plausibility.
* Scaling to C/D worlds may expose capacity collapse.
* Alternating-world training may require careful interpretation of rehearsal effects.

---

## 4. Results analyzed here

### Experiment 5 — Contextual Successor World

Claim:
Experiment 5 was a **mechanistic partial success** but not a capability success.

Evidence:
The contextual successor task required the same source number to map to different targets depending on mode: `plus_one`, `plus_two`, or `minus_one`. The design explicitly required context preservation, route separation, and repeated traversal of the active route.  The uploaded plots showed low absolute composition accuracy, with the full model around `0.147`, `no_recurrence` at `0`, `no_structural_plasticity` around `0.088`, and `no_context_routing` around `0.118`.

Caveat:
The result used small denominators and low absolute accuracy. The context confusion matrix appeared perfect, but final composition accuracy remained low, implying context identity alone was not sufficient.

Source artifact or conversation reference:
Conversation-uploaded Experiment 5 plots:

* `Experiment 5: composition accuracy by mode`
* `Experiment 5: composition accuracy by path length`
* `Experiment 5: composition accuracy over training`
* `Experiment 5: best composition accuracy`
* `Experiment 5: context confusion`
* `Experiment 5: latest recurrent drive`
* `Experiment 5: wrong-route activation`

---

### Experiment 7 — Initial saturated route-field diagnostic run

Claim:
When a clean route field existed, recurrence could compose it perfectly; without recurrence, one-step knowledge did not yield composition.

Evidence:
The initial Exp7 report showed full route field, context bleed, no inhibition, and noisy plasticity variants at `1.0` transition and composition accuracy. `exp7_no_recurrence` had `1.0` transition accuracy but `0.0` composition accuracy. `exp7_no_context_binding` and `exp7_no_structural_plasticity` degraded substantially. 

Caveat:
The initial run was saturated, with very large margins, so it was too easy to determine whether the mechanism remained valid under weaker margins.

Source artifact or conversation reference:
`exp7_report.md`; plots uploaded by user:

* `Experiment 7: composition accuracy by mode`
* `Experiment 7: composition accuracy by path length`
* `Experiment 7: mean composition accuracy`
* `Experiment 7: route-field context margin`
* `Experiment 7: correct-route margin`
* `Experiment 7: mean target rank during composition`
* `Experiment 7: mean transition accuracy`
* route-field margin heatmaps.

---

### Experiment 7 — Unsaturated scale / anti-saturation run

Claim:
The route-field result remained valid under reduced margins and larger path lengths.

Evidence:
The unsaturated Exp7 report showed `exp7_full_route_field` retained `1.0` transition accuracy, `1.0` composition accuracy, `1.0` route-table accuracy, and mean target rank `1.0`, but with smaller correct margin around `1.1498`. `exp7_no_recurrence` still had `1.0` transition accuracy and `0.0` composition accuracy. `exp7_no_context_binding` had transition accuracy around `0.3478` and composition around `0.0536`. `exp7_no_structural_plasticity` was near random. 

Caveat:
Exp7 remained diagnostic. It showed that clean route fields compose, not that the richer model can self-organize them.

Source artifact or conversation reference:
`exp7_report.md`; uploaded plots from the unsaturated Exp7 run.

---

### Experiment 8 — Self-organizing route acquisition

Claim:
Experiment 8 showed that a local plastic graph can acquire a context-conditioned route field from one-step transition experience and compose unseen multi-step paths recurrently.

Evidence:
`exp8_full_self_organizing_route_field` achieved `1.0` transition accuracy, `1.0` composition accuracy, `1.0` route-table accuracy, and mean target rank `1.0` across 30 seeds with `exposure_repeats=1`. `exp8_no_recurrence` had `1.0` transition accuracy but `0.0` composition accuracy. `exp8_no_structural_plasticity` was near random, and `exp8_no_context_binding` had transition accuracy around `0.3478` and composition around `0.048`. 

Caveat:
The experiment was still a controlled symbolic number world. Reward gating and homeostasis were not stressed in the clean immediate-feedback setting. The exposure curve was only a single exposure point.

Source artifact or conversation reference:
`exp8_report.md`; uploaded plots:

* `Experiment 8: composition accuracy by mode`
* `Experiment 8: composition accuracy by path length`
* `Experiment 8: mean composition accuracy`
* `Experiment 8: context margin`
* `Experiment 8: correct-route margin`
* `Experiment 8: exposure curve - composition accuracy`
* `Experiment 8: exposure curve - correct margin`
* `Experiment 8: exposure curve - route table accuracy`
* `Experiment 8: composition failure taxonomy`
* `Experiment 8: mean target rank during composition`
* `Experiment 8: mean transition accuracy`
* route-field margin heatmaps for full self-organizing route field.

---

### Experiment 9 — Context interference phase

Claim:
Inhibition became meaningfully load-bearing under context interference.

Evidence:
Experiment 9 asked whether inhibition protects context-bound routes under interference and whether reward gating/eligibility traces protect route acquisition under noisy or delayed feedback.  Under increasing context bleed, the full interference-robust model degraded more gracefully than `exp9_no_inhibition`. At context bleed `0.35`, full composition was around `0.777`, while no-inhibition was around `0.524`; at bleed `0.50`, full was around `0.230`, no-inhibition around `0.153`. Route-table accuracy and correct-route margins showed the same pattern.

Caveat:
At very high bleed, both full and no-inhibition degraded substantially. Inhibition helped but did not make the system immune to interference.

Source artifact or conversation reference:
`exp9_report.md`; uploaded plots:

* `Experiment 9A: composition accuracy under context bleed`
* `Experiment 9A: correct-route margin under context bleed`
* `Experiment 9A: route-table accuracy under context bleed`
* `Experiment 9A: wrong-route activation under context bleed`
* heatmaps for `exp9_full_interference_robust`.

---

### Experiment 9 — Feedback noise and delayed reward phase

Claim:
Reward gating preserved route margins under noisy feedback, and eligibility traces were required under delayed feedback.

Evidence:
Under feedback noise, full reward-robust and no-reward-gate variants both degraded, but the full model preserved positive correct margin longer. Under delayed reward, `exp9_no_eligibility_trace` collapsed when reward delay was introduced, while the full model remained strong under zero-noise delayed reward. The report frames these as the intended mechanisms tested by Experiment 9. 

Caveat:
Reward gating helped but did not eliminate degradation at high feedback noise. The largest clean mechanism-specific effect was eligibility trace under delay.

Source artifact or conversation reference:
`exp9_report.md`; uploaded plots:

* `Experiment 9B: composition under feedback noise, delay=0`
* `Experiment 9B: composition under feedback noise, delay=2`
* `Experiment 9B: composition under feedback noise, delay=4`
* `Experiment 9B: correct margin under feedback noise, delay=0`
* `Experiment 9B: correct margin under feedback noise, delay=2`
* `Experiment 9B: correct margin under feedback noise, delay=4`
* `Experiment 9B: route-table under feedback noise, delay=0`
* `Experiment 9B: route-table under feedback noise, delay=2`
* `Experiment 9B: route-table under feedback noise, delay=4`
* feedback heatmaps for `exp9_full_reward_robust`.

---

### Experiment 10 — Rule reversal and adaptive rebinding

Claim:
Experiment 10 demonstrated adaptive route rebinding and exposed a measurable stability-plasticity tradeoff.

Evidence:
Experiment 10 tested whether a route field learned under rule A can adapt when mode labels are remapped to rule B, and whether consolidation, inhibition, reward gating, eligibility traces, and dual-world context affect the stability-plasticity tradeoff.  The full adaptive reversal model began with rule A composition `1.0`, then after reversal reached rule B composition `0.999561` and rule B route-table accuracy `0.999638` by checkpoint 21. Old rule A fell to about `0.289474`, matching the deterministic rule-overlap baseline rather than random. 

Caveat:
The full model adapted mostly by overwrite under the same context labels. This supports adaptive rebinding, not yet non-destructive memory.

Source artifact or conversation reference:
`exp10_report.md`; uploaded plots:

* `Experiment 10: reversal composition accuracy (old A vs new B)`
* `Experiment 10: reversal correct margin (old A vs new B)`
* `Experiment 10: new-rule B composition adaptation`
* `Experiment 10: new-rule B route-table adaptation`
* `Experiment 10: old-rule A retention during reversal`
* `Experiment 10: reversal route-table accuracy (old A vs new B)`
* `Experiment 10: final new-rule B composition at ckpt=21`
* `Experiment 10: final old-rule A retention at ckpt=21`
* `Experiment 10: new-rule B failure taxonomy at final reversal checkpoint`.

---

### Experiment 10 — Consolidation tradeoff

Claim:
Strong consolidation preserved old routes but blocked new-rule acquisition; no consolidation adapted quickly but behaved poorly in switchback.

Evidence:
`exp10_strong_consolidation` retained old rule A at final reversal with composition around `0.927632` and route-table accuracy around `0.985145`, while rule B remained around `0.289724` composition and `0.359420` route-table accuracy. `exp10_no_consolidation` adapted to rule B rapidly but ended switchback with A composition only around `0.292607` while B remained high around `0.886591`. 

Caveat:
The strong-consolidation setting may be too strong. No-consolidation’s poor switchback behavior may indicate overcommitment to B, but this requires a more targeted follow-up.

Source artifact or conversation reference:
`exp10_report.md`; reversal and switchback plots.

---

### Experiment 10 — Dual-context worlds

Claim:
Dual-context worlds hinted at context-separated memory but did not yet cleanly prove non-destructive retention.

Evidence:
`exp10_dual_context_worlds` learned B to `1.0` composition and route-table accuracy. During reversal, A collapsed to `0.0379073` composition and `0.19058` route-table accuracy. After switchback, A returned to `0.987281` composition and `0.989493` route-table accuracy while B remained at `1.0` composition and route-table accuracy. 

Caveat:
A was not retained during the initial B-learning phase; it returned after switchback. This is promising but ambiguous. It may indicate latent recoverability, context-access issues, or retraining rather than true non-destructive retention.

Source artifact or conversation reference:
`exp10_report.md`; uploaded dual-rule plots.

---

### Experiment 11 — Implementation and validation only

Claim:
Experiment 11 was implemented to directly test context-separated route memory and non-destructive rebinding.

Evidence:
The assistant implemented `experiment11_context_memory.zip` and `start_exp11.ps1`, added explicit progress logging via `exp11_run.log` and `progress.jsonl`, and validated the suite with a small run. The intended phases were `sequential`, `alternating`, `scaling`, and `context_noise`.

Caveat:
No full local Experiment 11 results were analyzed in this thread. Any claims about Exp11 remain design/validation only.

Source artifact or conversation reference:
Generated artifacts:

* `experiment11_context_memory.zip`
* `start_exp11.ps1`

---

## 5. Key scientific conclusions supported by this thread

Claim:
A clean context-conditioned route table can be composed recurrently.

Evidence:
Experiment 7 full route field achieved `1.0` transition and composition accuracy; no-recurrence achieved `1.0` transition but `0.0` composition. 

Caveat:
Experiment 7 was diagnostic and did not by itself prove route-field acquisition.

---

Claim:
Local structural plasticity can acquire a context-conditioned route field from one-step transition experience.

Evidence:
Experiment 8 full self-organizing route field achieved `1.0` transition, composition, and route-table accuracy across 30 seeds; no-structural-plasticity collapsed near random. 

Caveat:
The task was a controlled symbolic number world, not a naturalistic or multimodal task.

---

Claim:
Recurrence is necessary for multi-step route composition but not for one-step route-table knowledge.

Evidence:
Across Experiments 7, 8, and 9, no-recurrence variants learned one-step transitions or route tables but failed composition.   

Caveat:
The no-recurrence ablation must remain fair in future richer tasks; it should not be structurally incapable of any alternative composition baseline unless clearly framed as such.

---

Claim:
Context binding is required to keep multiple route families from colliding.

Evidence:
Experiment 8 no-context-binding had transition accuracy around `0.347826` and composition around `0.047995`, with near-zero or negative correct margin.  Similar route-collision behavior was observed in Experiment 7 and Experiment 9.

Caveat:
The exact mechanism of context binding remains engineered and should be compared against alternative context-separation mechanisms.

---

Claim:
Inhibition is not required in clean deterministic tasks but protects route margins under context interference.

Evidence:
Experiment 8 no-inhibition retained `1.0` accuracy but had weaker margins. Experiment 9 showed no-inhibition degraded earlier than full under context bleed.  

Caveat:
Inhibition’s effect is mostly visible under stress; clean-task claims should not overstate its necessity.

---

Claim:
Reward gating and eligibility traces become meaningful under noisy or delayed feedback.

Evidence:
Experiment 9 was explicitly designed to test reward gating and eligibility traces under noisy/delayed feedback. The no-eligibility-trace variant collapsed under delayed feedback, and no-reward-gate lost margin more severely under feedback noise. 

Caveat:
Reward gating did not fully solve high-noise training; its strongest result was margin preservation, not immunity to noise.

---

Claim:
Route fields can adapt after rule reversal.

Evidence:
Experiment 10 full adaptive reversal learned rule A, then reached near-perfect rule B route-table and composition accuracy after reversal exposures. 

Caveat:
The full model mostly overwrote A under the same context labels; this is adaptive rebinding, not yet non-destructive memory.

---

Claim:
Consolidation creates a measurable stability-plasticity tradeoff.

Evidence:
Experiment 10 strong consolidation preserved A but blocked B; no consolidation adapted quickly but behaved poorly in switchback. 

Caveat:
The precise consolidation settings may need tuning and additional baselines.

---

Claim:
Higher-level world context may support multiple rule systems, but this remains unresolved.

Evidence:
Experiment 10 dual-context worlds eventually recovered A and retained B after switchback, but did not retain A during initial B training. 

Caveat:
This is promising but not conclusive. It motivated Experiment 11.

---

## 6. Important flaws, mistakes, or implementation concerns identified

1. **Experiment 5 had low absolute composition accuracy.**
   It was treated as a mechanistic partial success, not a capability success. Full composition accuracy around `0.147` was too low for a strong positive claim.

2. **Experiment 5 context confusion was misleadingly strong.**
   Perfect context confusion did not imply correct traversal. The model could preserve mode identity but still fail final-number composition.

3. **Experiment 5 evaluation likely had small denominators.**
   Values like `0.147059` suggested small evaluation counts, so small absolute differences should not be overinterpreted.

4. **Experiment 7 initial run was too saturated.**
   Very high margins made it difficult to know whether the result was robust. This led to the unsaturated follow-up settings.

5. **Experiment 7 was diagnostic, not a learning result.**
   It established that clean route fields compose, but not that route fields self-organize.

6. **Experiment 8 exposure curve was not a real curve.**
   The run used `exposure_repeats=1`, so it did not yet determine exposure thresholds.

7. **Experiment 8 did not stress reward gating or homeostasis.**
   Clean immediate-feedback conditions made those mechanisms mostly neutral.

8. **Experiment 9 generated a very large `predictions.csv`.**
   The file was about 434 MB. It was judged unnecessary for aggregate analysis. A preprocessing script was suggested for future detailed trajectory-level summaries.

9. **Experiment 10 did not test noisy/delayed reversal.**
   Reward gate and eligibility trace were neutral because feedback was clean and immediate.

10. **Experiment 10 full model overwrote old A.**
    The model adapted, but did not preserve old rule A under the same context labels.

11. **Experiment 10 dual-context result was ambiguous.**
    A returned after switchback while B remained high, but A did not stay accessible during initial B training.

12. **Strong consolidation may have been too strong in Experiment 10.**
    It preserved A but largely blocked B.

13. **No-consolidation may have overcommitted to B.**
    It adapted quickly but switchback to A was poor.

14. **Experiment 11 remains unvalidated locally.**
    It was implemented and assistant-validated, but no full user-run results were analyzed in this thread.

15. **Manuscript risk: overclaiming biological realism.**
    The project framing explicitly cautions that the immediate goal is not to prove biological realism or a new learning paradigm, but to build an experimental framework for dynamically routed adaptive computation. 

---

## 7. Figures or artifacts referenced

### Project / tracker artifacts

* `Experiment.md`
* `EXPERIMENT_TRACKER.md`
* `EXPERIMENT_TRACKER_UPDATED.md`
* `Experiment_UPDATED.md`
* `updated_experiment_docs.zip`

### Experiment 5 artifacts / plots

* `EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`
* `Experiment 5: composition accuracy by mode`
* `Experiment 5: composition accuracy by path length`
* `Experiment 5: composition accuracy over training`
* `Experiment 5: best composition accuracy`
* `Experiment 5: context confusion`
* `Experiment 5: latest recurrent drive`
* `Experiment 5: wrong-route activation`

### Experiment 7 generated artifacts

* `experiment7_route_field_diagnostics.zip`
* `start.ps1`
* `exp7_report.md`
* `runs.csv`
* `metrics.csv`
* `predictions.csv`
* `route_diagnostics.csv`
* `baselines.csv`
* `Experiment 7: composition accuracy by mode`
* `Experiment 7: composition accuracy by path length`
* `Experiment 7: mean composition accuracy`
* `Experiment 7: route-field context margin`
* `Experiment 7: correct-route margin`
* `Experiment 7: mean target rank during composition`
* `Experiment 7: mean transition accuracy`
* route-field margin heatmaps for `minus_one`, `plus_one`, `plus_two`

### Experiment 8 generated artifacts

* `experiment8_self_organizing_route_acquisition.zip`
* `start_exp8.ps1`
* `exp8_report.md`
* `exp8_summary.csv`
* `exp8_route_summary.csv`
* `exp8_baseline_summary.csv`
* `metrics.csv`
* `metrics_wide.csv`
* `predictions.csv`
* `route_diagnostics.csv`
* `Experiment 8: composition accuracy by mode`
* `Experiment 8: composition accuracy by path length`
* `Experiment 8: mean composition accuracy`
* `Experiment 8: context margin`
* `Experiment 8: correct-route margin`
* `Experiment 8: exposure curve - composition accuracy`
* `Experiment 8: exposure curve - correct margin`
* `Experiment 8: exposure curve - route table accuracy`
* `Experiment 8: composition failure taxonomy`
* `Experiment 8: mean target rank during composition`
* `Experiment 8: mean transition accuracy`
* route-field margin heatmaps for full self-organizing route field

### Experiment 9 generated artifacts

* `experiment9_robust_adaptive_route_plasticity.zip`
* `start_exp9.ps1`
* `exp9_report.md`
* `exp9_summary.csv`
* `exp9_route_summary.csv`
* `metrics.csv`
* `metrics_wide.csv`
* `route_diagnostics.csv`
* `runs.csv`
* `baselines.csv`
* `predictions.csv` — not uploaded because too large
* `Experiment 9: clean-point transition accuracy`
* `Experiment 9: clean-point composition accuracy`
* `Experiment 9: composition failure taxonomy at strongest stress`
* `Experiment 9A: composition accuracy under context bleed`
* `Experiment 9A: correct-route margin under context bleed`
* `Experiment 9A: route-table accuracy under context bleed`
* `Experiment 9A: wrong-route activation under context bleed`
* `Experiment 9B: composition under feedback noise, delay=0`
* `Experiment 9B: composition under feedback noise, delay=2`
* `Experiment 9B: composition under feedback noise, delay=4`
* `Experiment 9B: correct margin under feedback noise, delay=0`
* `Experiment 9B: correct margin under feedback noise, delay=2`
* `Experiment 9B: correct margin under feedback noise, delay=4`
* `Experiment 9B: route-table under feedback noise, delay=0`
* `Experiment 9B: route-table under feedback noise, delay=2`
* `Experiment 9B: route-table under feedback noise, delay=4`
* heatmaps:

  * `route_margin_heatmap_feedback_exp9_full_reward_robust_minus_one.png`
  * `route_margin_heatmap_feedback_exp9_full_reward_robust_plus_one.png`
  * `route_margin_heatmap_feedback_exp9_full_reward_robust_plus_two.png`
  * `route_margin_heatmap_interference_exp9_full_interference_robust_minus_one.png`
  * `route_margin_heatmap_interference_exp9_full_interference_robust_plus_one.png`
  * `route_margin_heatmap_interference_exp9_full_interference_robust_plus_two.png`

### Experiment 10 generated artifacts

* `experiment10_adaptive_reversal.zip`
* `start_exp10.ps1`
* `exp10_report.md`
* `exp10_summary.csv`
* `exp10_route_summary.csv`
* `failure_taxonomy.csv`
* `metrics.csv`
* `metrics_wide.csv`
* `route_diagnostics.csv`
* `runs.csv`
* `baselines.csv`
* `exp10_adaptation_thresholds.csv`
* `exp10_baseline_summary.csv`
* `exp10_reversal_composition_dual_rule.png`
* `exp10_reversal_correct_margin_dual_rule.png`
* `exp10_reversal_new_rule_composition.png`
* `exp10_reversal_new_rule_route_table.png`
* `exp10_reversal_old_rule_retention.png`
* `exp10_reversal_route_table_dual_rule.png`
* `exp10_failure_taxonomy_final_new_rule.png`
* `exp10_final_new_rule_composition.png`
* `exp10_final_old_rule_retention.png`

### Experiment 11 generated artifacts

* `experiment11_context_memory.zip`
* `start_exp11.ps1`
* expected future outputs:

  * `exp11_report.md`
  * `exp11_summary.csv`
  * `exp11_memory_indices.csv`
  * `metrics_wide.csv`
  * `route_diagnostics.csv`
  * `failure_taxonomy.csv`
  * `exp11_*.png`
  * `exp11_run.log`
  * `progress.jsonl`

---

## 8. Decisions made

1. **Adopted the role of analysis agent.**
   The assistant would evaluate experiments through capability, mechanistic necessity, routing quality, plasticity/adaptation, novelty relevance, and next-experiment recommendations.

2. **Experiment 5 was not treated as a solved result.**
   It was considered a useful diagnostic failure/partial success.

3. **Moved away from immediate multimodal grounding.**
   Experiment 6 was deferred repeatedly until contextual routing, route acquisition, robustness, and memory were clearer.

4. **Designed Experiment 7 as a diagnostic bridge.**
   Purpose: determine whether clean route fields can compose.

5. **Changed Experiment 7 settings after saturated run.**
   Reduced training repeats, increased number range/path length, increased seeds.

6. **Designed Experiment 8 as self-organizing route acquisition.**
   Purpose: test whether route fields can be learned from one-step experience.

7. **Used `--path-train-repeats 0` in Experiment 8.**
   This ensured composition was not directly trained.

8. **Designed Experiment 9 as robustness stress test.**
   Focused on context bleed, inhibition, feedback noise, reward gating, reward delay, and eligibility traces.

9. **Decided not to upload raw `predictions.csv` for Experiment 9.**
   It was too large and not needed for aggregate analysis.

10. **Designed Experiment 10 as rule reversal/adaptive rebinding.**
    Focused on overwrite, retention, consolidation, and switchback.

11. **Interpreted Experiment 10 as adaptive rebinding, not yet non-destructive memory.**

12. **Designed Experiment 11 as context-separated memory.**
    Focused on true dual-world acquisition, alternating worlds, multi-world scaling, and context noise.

13. **Added explicit run logging to Experiment 11.**
    Required terminal progress plus `exp11_run.log` and `progress.jsonl`.

14. **Updated tracker and experiment documents.**
    Generated updated docs for repository placement:

    * `EXPERIMENT_TRACKER_UPDATED.md`
    * `Experiment_UPDATED.md`
    * `updated_experiment_docs.zip`

15. **Manuscript framing decision:**
    The strongest current story is not “biological realism proven,” but rather: explicit, analyzable, stateful computational paths can support route acquisition, recurrence-based composition, robustness under interference, and adaptive rebinding.

---

## 9. Open questions created by this thread

1. Can Experiment 11 show true non-destructive memory: B learned while A remains accessible without retraining?

2. Does world-gated plasticity solve the ambiguity exposed by Experiment 10 dual-context worlds?

3. How many route worlds can coexist before capacity collapses?

4. Does multi-world interference degrade smoothly or catastrophically?

5. Does wrong-world activation predict failures better than raw accuracy?

6. Can old route fields become dormant but recoverable without full retraining?

7. Does switchback speed exceed first-learning speed under controlled comparisons?

8. Can inhibition meaningfully suppress wrong-world activation in alternating/multi-world conditions?

9. Can the system retain A and B without manual substrate isolation?

10. What is the correct balance of consolidation for retaining old routes while still allowing new learning?

11. Can noisy/delayed rule reversal reproduce the Experiment 9 reward-gating and eligibility-trace effects?

12. Are current context-binding and world-gated-plasticity mechanisms biologically plausible analogies, engineering mechanisms, or both?

13. How much of the result depends on symbolic number-world structure?

14. When should multimodal grounding be reintroduced?

15. What dense/static baselines are needed before manuscript claims are defensible?

16. Are route-field margins sufficient as mechanistic evidence, or do we need trajectory-level path traces?

17. Should the large `predictions.csv` files be replaced permanently with precomputed compact trajectory summaries?

---

## 10. Relationship to the first manuscript

### Central claim

This thread substantially contributes to the central manuscript claim that a recurrent, structurally plastic, context-sensitive route-field system can support analyzable adaptive computation.

The strongest supported formulation is:

> Local structural plasticity can form context-conditioned transition routes, recurrence can compose those routes, and higher-level control mechanisms modulate robustness and adaptation.

### Supporting claim

Experiments 7–10 provide a staged causal decomposition:

```text
Exp7: clean route fields compose.
Exp8: local plasticity can self-organize route fields.
Exp9: inhibition, reward gating, and eligibility traces become load-bearing under specific stressors.
Exp10: route fields can adapt after rule reversal, and consolidation controls the stability-plasticity tradeoff.
```

### Limitation

All completed results in this thread are symbolic number-world experiments. They do not yet establish biological realism, naturalistic perception, or broad machine-learning competitiveness. The project’s own framing warns against overclaiming novelty or biological realism and positions the work as an experimental framework for analyzable stateful dynamic routing. 

### Future work

Experiment 11 is the immediate future-work bridge: context-separated memory and non-destructive rebinding. After that, multimodal grounding can be revisited.

### Supplementary material

Experiments 7–10 are well suited for supplementary material because they provide:

* ablation matrices;
* route-field heatmaps;
* deterministic baselines;
* margin analyses;
* failure taxonomies;
* run scripts and reproducible result directories.

Experiment 5 should likely be presented as a motivating failure/diagnostic result rather than a positive core result.

---

## 11. Claims-and-evidence rows contributed by this thread

| Claim                                                                     | Evidence                                                                                                         | Caveat                                                                      | Experiment(s)     | Artifact(s)                                           | Manuscript status    |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------- | -------------------- |
| Contextual successor traversal is harder than single successor traversal. | Exp5 full model reached only low composition accuracy while recurrence/context mechanisms showed partial signal. | Small denominators and low absolute accuracy.                               | Exp5              | Exp5 plots; `EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`    | Preliminary          |
| Clean route fields can be composed recurrently.                           | Exp7 full route field achieved `1.0` transition and composition accuracy.                                        | Diagnostic scaffold; not yet self-organizing.                               | Exp7              | `exp7_report.md`; Exp7 plots                          | Strong               |
| Recurrence is required for multi-step composition.                        | Exp7/8/9 no-recurrence variants preserved transition knowledge but had near-zero composition.                    | Ensure future no-recurrence baselines are fair.                             | Exp7, Exp8, Exp9  | `exp7_report.md`; `exp8_report.md`; `exp9_report.md`  | Strong               |
| Structural plasticity is required for route-field acquisition.            | Exp8 and Exp9 no-structural-plasticity variants remained near random.                                            | Symbolic task; mechanism still engineered.                                  | Exp8, Exp9, Exp10 | `exp8_report.md`; `exp9_report.md`; `exp10_report.md` | Strong               |
| Context binding prevents route-family collision.                          | No-context-binding variants showed ~one-mode-like transition behavior and poor composition.                      | Need compare against alternative binding mechanisms.                        | Exp7, Exp8, Exp9  | `exp7_report.md`; `exp8_report.md`; `exp9_report.md`  | Strong               |
| Local plasticity can self-organize route fields from one-step experience. | Exp8 full model achieved `1.0` transition, composition, and route-table accuracy with one exposure repeat.       | Controlled symbolic number world.                                           | Exp8              | `exp8_report.md`; Exp8 heatmaps                       | Strong               |
| Inhibition protects route margins under interference.                     | Exp9 full degraded more gracefully than no-inhibition under context bleed.                                       | Effect is stress-dependent, not required in clean setting.                  | Exp8, Exp9        | `exp9_report.md`; interference plots                  | Strong               |
| Reward gating preserves margin under noisy feedback.                      | Exp9 no-reward-gate lost margin faster under feedback noise.                                                     | Accuracy gap smaller than margin gap; high noise still degraded full model. | Exp9              | `exp9_report.md`; feedback plots                      | Promising            |
| Eligibility traces are required under delayed reward.                     | Exp9 no-eligibility-trace collapsed with reward delay.                                                           | Needs confirmation under richer delayed tasks.                              | Exp9              | `exp9_report.md`                                      | Strong               |
| Route fields can adapt after rule reversal.                               | Exp10 full adaptive reversal reached near-perfect B after reversal.                                              | Mostly overwrote A under same labels.                                       | Exp10             | `exp10_report.md`; reversal plots                     | Strong               |
| Consolidation controls stability-plasticity tradeoff.                     | Strong consolidation retained A but blocked B; no consolidation adapted quickly but switchback was poor.         | Consolidation levels may need tuning.                                       | Exp10             | `exp10_report.md`                                     | Strong               |
| Higher-level context may support separable rule memories.                 | Exp10 dual-context worlds recovered A while retaining B after switchback.                                        | A was not retained during initial B learning; ambiguous.                    | Exp10             | `exp10_report.md`; dual-context plots                 | Promising            |
| Non-destructive multi-world memory is not yet proven.                     | Exp11 designed specifically to test it; no local results analyzed yet.                                           | Pending experiment.                                                         | Exp11             | `experiment11_context_memory.zip`; `start_exp11.ps1`  | Needs rerun          |
| Multimodal grounding should wait.                                         | Repeated decision to defer Exp6 until route memory is understood.                                                | Could be revisited after Exp11.                                             | Exp6, Exp11       | Tracker updates; conversation decisions               | Preliminary          |
| Raw prediction logs are useful but too large.                             | Exp9 `predictions.csv` was ~434 MB and not needed for aggregate analysis.                                        | Trajectory-level summaries may still be needed.                             | Exp9              | `predictions.csv`; proposed preprocessing script      | Needs metric cleanup |

---

## 12. Recommended follow-up actions

1. **Run Experiment 11 locally.**
   Upload `analysis/exp11/`, especially:

   * `exp11_report.md`;
   * `exp11_summary.csv`;
   * `exp11_memory_indices.csv`;
   * `metrics_wide.csv`;
   * `route_diagnostics.csv`;
   * `failure_taxonomy.csv`;
   * `exp11_*.png`;
   * `exp11_run.log`;
   * `progress.jsonl`.

2. **Analyze whether Experiment 11 demonstrates true non-destructive retention.**
   Specifically check:

   * A accuracy after B training without A retraining;
   * B acquisition after A;
   * wrong-world activation;
   * retention index;
   * separation score;
   * world-gated plasticity vs full model.

3. **Add compact prediction-summary generation to all future experiments.**
   Avoid uploading raw `predictions.csv` unless necessary. Produce:

   * accuracy by mode/path/stressor;
   * failure taxonomy by condition;
   * margin summaries;
   * representative failures;
   * boundary-failure counts.

4. **Update `EXPERIMENT_TRACKER.md` after Experiment 10 and before/after Experiment 11.**
   The tracker should record:

   * Exp10 as completed;
   * Exp11 as implemented/pending local run;
   * Exp6/multimodal grounding as deferred.

5. **Add a manuscript evidence table.**
   Include rows for:

   * route acquisition;
   * recurrence/composition;
   * context binding;
   * inhibition/interference;
   * reward/eligibility;
   * reversal/consolidation;
   * context-separated memory pending.

6. **Prepare Experiment 5 as a motivating failure.**
   Do not present it as a successful contextual traversal result. Use it to motivate Exp7/Exp8 diagnostics.

7. **Prepare Experiment 7 as a diagnostic control.**
   Present it as: clean route fields compose, so Exp5 failure was likely route-field acquisition/binding rather than recurrence impossibility.

8. **Prepare Experiment 8 as the first core positive result.**
   It is the cleanest “local plasticity forms route fields; recurrence composes them” result.

9. **Prepare Experiment 9 as robustness mechanism evidence.**
   Use it to support mechanism-specific claims about inhibition, reward gating, and eligibility traces.

10. **Prepare Experiment 10 as adaptive rebinding evidence.**
    Present it as route adaptation and stability-plasticity tradeoff, not full non-destructive memory.

11. **Do not yet claim biological realism.**
    Use careful language: biologically inspired, computational analogy, route-field mechanism, plastic adaptive substrate.

12. **Delay multimodal grounding until after Experiment 11.**
    Multimodal grounding becomes more meaningful if the system can first maintain multiple context-separated rule worlds.

13. **Add dense/static baselines in future manuscript work.**
    For defensibility, include:

    * lookup oracle;
    * feed-forward MLP over `(world, mode, start, steps)`;
    * static transition table;
    * non-recurrent context-conditioned decoder;
    * random and most-frequent baselines.

14. **Consider a metric-cleanup pass.**
    Standardize:

    * route-table accuracy;
    * composition accuracy;
    * target rank;
    * correct-route margin;
    * context/world margin;
    * wrong-route activation;
    * failure taxonomy labels;
    * retention/acquisition/interference indices.

15. **After Experiment 11, decide whether Experiment 12 should be multi-world scaling, noisy context memory, or multimodal grounding.**
