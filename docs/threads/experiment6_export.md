# Thread Digest: Experiment 6 Route-Audit Successor Follow-Up

## 1. Thread scope

This thread revisited **Experiment 6**, an early experiment that had been run but not fully analyzed before the project moved on.

The thread focused on interpreting uploaded Experiment 6 artifacts in light of the current broader research program. The main question was whether Experiment 6 supported, weakened, or clarified the project’s emerging thesis about recurrent structural plasticity, context-indexed route selection, and compositional memory.

The core conclusion from this thread was that **Experiment 6 is a negative-but-informative result**: recurrence and structural plasticity were clearly load-bearing, but the model did **not** yet achieve reliable context-conditioned compositional traversal under an honest recurrent audit.

## 2. Experiments discussed

### Experiment 4 — Single universal successor route

Short description: Mentioned only as historical context. Experiment 4 allowed a single universal transition chain such as `2 -> 3 -> 4 -> 5`, meaning route ambiguity was limited. In this thread, it served as a contrast case for Experiment 6.

### Experiment 5 — Contextual successor rules with symbolic state reconstruction

Short description: Mentioned as the immediate predecessor to Experiment 6. Experiment 5 introduced contextual successor rules, but the traversal loop rebuilt the symbolic concept-plus-context state after each recurrent step. That made some context/routing metrics partly tautological and motivated the Experiment 6 correction. 

### Experiment 6 — Route-Audit Successor World

Short description: The main experiment analyzed in this thread. Experiment 6 tested whether the recurrent plastic graph could choose among multiple transition systems using context while being evaluated on the **raw recurrent trajectory** rather than a reconstructed symbolic state. 

The contextual modes were:

```text
plus_one:  n -> n + 1
plus_two:  n -> n + 2
minus_one: n -> n - 1
```

The key challenge was that the same start state could map to different outcomes depending on the active context, requiring the model to preserve mode, separate competing routes, and repeatedly traverse the correct route family. 

## 3. Experimental designs created or modified here

No new experiment implementation was created in this thread. The thread analyzed an already-designed and already-run Experiment 6.

### Design: Experiment 6 — Route-Audit Successor World

**Experiment number:**
Experiment 6

**Purpose:**
To test whether the recurrent plastic graph could choose among competing transition systems based on context when evaluated on the actual recurrent trajectory rather than a reconstructed symbolic endpoint.

**Hypothesis:**
If the model had learned true context-conditioned route memories, then the full model should maintain the correct mode and compose transitions across multiple recurrent steps, while audited route metrics should show the correct route beating competing routes along the actual recurrent path.

**Model variants:** 

| Variant                         | Purpose                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------- |
| `exp6_full_route_audit`         | Full recurrent contextual traversal graph with audited route metrics         |
| `exp6_no_recurrence`            | Tests whether recurrent traversal is necessary                               |
| `exp6_no_structural_plasticity` | Tests whether rewiring/growth remains load-bearing                           |
| `exp6_no_reward_gate`           | Tests whether reward modulation matters once negative correction is explicit |
| `exp6_no_homeostasis`           | Tests whether stabilization matters when routes compete                      |
| `exp6_no_context_routing`       | Tests whether persistent context bias is necessary without symbolic resets   |
| `exp6_no_inhibition`            | Tests whether suppressing competing contexts reduces route confusion         |

**Metrics:** 

Performance:

```text
transition/accuracy
composition/accuracy
composition/accuracy_mode_*
composition/accuracy_steps_*
```

Route selection:

```text
composition/average_target_route_activation
composition/average_wrong_route_activation
composition/average_route_margin
composition/average_context_margin
composition/confusion_*
```

Dynamics:

```text
composition/average_recurrent_drive
composition/average_unique_active
composition/average_path_entropy
```

**Expected outcomes:**
The design would support the thesis if the full model could maintain the correct route under context and compose it across multiple steps, with route metrics showing that correct-route activation exceeded wrong-route activation along the recurrent path. 

**Implementation notes:**
Experiment 6 changed the evaluation contract from Experiment 5. Traversal advanced using the actual recurrently selected active set instead of replacing each step with `activate_state(predicted, mode)`. Route metrics were measured from the per-step recurrent trajectory, and structural rewiring distinguished positive consolidation from negative corrective rewrites. 

**Known risks:**

* The task is harder than a single successor chain because the same source state can imply different next states under different modes.
* Context identity may be preserved while actual route dynamics remain weak.
* Endpoint accuracy may be noisy and insufficient without route-margin diagnostics.
* A high recurrent-drive value may reflect excitation rather than correct route control.
* Because this thread did not inspect the implementation files, code-level causes of failure remain unresolved.

## 4. Results analyzed here

### Result: Full model did not achieve reliable context-conditioned composition

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_report.md`
* `exp6_comparison.csv`
* `exp6_best_composition_accuracy.png`
* `exp6_accuracy_by_mode.png`
* `exp6_accuracy_by_path_length.png`
* `exp6_adaptation_curve.png`

**Key metrics:**

For `exp6_full_route_audit`:

```text
best_composition_accuracy = 0.151639
best_transition_accuracy  = 0.193651
composition/accuracy      = 0.0737705
```

**Interpretation:**
The full route-audit model showed nonzero performance, but far below what would count as successful context-conditioned compositional traversal.

**Caveats:**
This was interpreted from the uploaded summary/report and figures. The implementation files were not reviewed in this thread.

**Claim:**
Experiment 6 does not validate robust context-conditioned compositional route traversal.

**Evidence:**
The full model reached only ~15.2% best composition accuracy and ~19.4% best transition accuracy. 

**Caveat:**
The result is not a total failure of the architecture because ablations show recurrence and structural plasticity were load-bearing.

**Source artifact or conversation reference:**
`exp6_report.md`; assistant analysis in this thread.

---

### Result: Recurrence was load-bearing

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_report.md`
* `exp6_best_composition_accuracy.png`
* `exp6_recurrent_drive.png`

**Key metrics:**

For `exp6_no_recurrence`:

```text
best_composition_accuracy = 0
best_transition_accuracy  = 0
composition/accuracy      = 0
composition/average_recurrent_drive = 0
```

**Interpretation:**
Removing recurrence eliminated task performance. This supports the idea that the task depends on recurrent traversal rather than static readout alone.

**Caveats:**
This supports recurrence as necessary in this implementation, but does not prove that the recurrent dynamics were correctly organized in the full model.

**Claim:**
Recurrent traversal was necessary for Experiment 6 performance.

**Evidence:**
The `exp6_no_recurrence` ablation collapsed to 0% composition and transition accuracy. 

**Caveat:**
Necessity of recurrence does not imply sufficiency for robust compositional memory.

**Source artifact or conversation reference:**
`exp6_report.md`; `exp6_recurrent_drive.png`; assistant analysis in this thread.

---

### Result: Structural plasticity was load-bearing

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_report.md`
* `exp6_best_composition_accuracy.png`
* `exp6_wrong_route_activation.png`
* `exp6_recurrent_drive.png`

**Key metrics:**

For `exp6_no_structural_plasticity`:

```text
best_composition_accuracy = 0.0409836
best_transition_accuracy  = 0.047619
composition/accuracy      = 0.0286885
composition/average_recurrent_drive = 139.854
composition/average_target_route_activation = 0.00629649
composition/average_wrong_route_activation  = 0.00785804
```

**Interpretation:**
Removing structural plasticity caused a major performance collapse compared with the full model and other high-performing ablations. This indicates that rewiring/growth contributed real signal.

**Caveats:**
The structural-plasticity ablation did not go fully to zero, so there may be residual structure or chance-level endpoint hits. It does not prove that the learned plastic structure was sufficiently organized for robust composition.

**Claim:**
Structural plasticity contributed materially to Experiment 6 performance.

**Evidence:**
`exp6_no_structural_plasticity` reached only ~4.1% best composition accuracy, far below the full model’s ~15.2% and the best ablation’s ~16.4%. 

**Caveat:**
The route-margin and endpoint metrics still show that structural plasticity alone was not enough to produce clean route control.

**Source artifact or conversation reference:**
`exp6_report.md`; assistant analysis in this thread.

---

### Result: Correct route did not dominate wrong routes

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_report.md`
* `exp6_route_margin.png`
* `exp6_wrong_route_activation.png`

**Key metrics:**

For `exp6_full_route_audit`:

```text
composition/average_target_route_activation = 0.173116
composition/average_wrong_route_activation  = 0.199278
composition/average_route_margin            = -0.0261622
```

**Interpretation:**
The full model’s correct route was weaker than the strongest competing wrong route on average. This was interpreted as the key mechanistic failure: the model could represent context, but could not make the selected context causally dominate recurrent route evolution.

**Caveats:**
Route-margin interpretation depends on correctness of the audit metric implementation. The implementation was not inspected in this thread.

**Claim:**
The full model did not create a route-selection field where the correct route reliably beat competing routes.

**Evidence:**
For the full model, wrong-route activation exceeded target-route activation, producing a negative average route margin. 

**Caveat:**
The model’s nonzero endpoint accuracy means some partial transition behavior existed, but it was not cleanly route-dominant.

**Source artifact or conversation reference:**
`exp6_report.md`; `exp6_route_margin.png`; `exp6_wrong_route_activation.png`; assistant analysis in this thread.

---

### Result: Context identity could be preserved while route traversal still failed

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_context_confusion.png`
* `exp6_report.md`

**Key metrics:**

For `exp6_full_route_audit`, the context confusion matrix shown in `exp6_context_confusion.png` was perfectly diagonal:

```text
minus_one -> minus_one = 1.00
plus_one  -> plus_one  = 1.00
plus_two  -> plus_two  = 1.00
off-diagonal entries   = 0.00
```

**Interpretation:**
This thread interpreted that result as an important distinction: the model appeared able to preserve or classify high-level mode identity, but this did not translate into reliable mode-conditioned state transition.

**Caveats:**
The context-confusion plot alone can overstate success if treated as equivalent to route correctness. The more important route-margin and endpoint metrics remained weak.

**Claim:**
Experiment 6 distinguishes context recognition from context-conditioned compositional control.

**Evidence:**
The full model preserved mode identity in the context confusion plot, while best composition accuracy remained low and average route margin was negative.

**Caveat:**
This conclusion should be presented carefully because it depends on the context-confusion plot and summary route metrics, not a step-by-step trajectory audit.

**Source artifact or conversation reference:**
`exp6_context_confusion.png`; `exp6_report.md`; assistant analysis in this thread.

---

### Result: Composition degraded with path length

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_accuracy_by_path_length.png`
* `exp6_report.md`

**Key metrics:**

For `exp6_full_route_audit`:

```text
composition/accuracy_steps_2 = 0.164179
composition/accuracy_steps_3 = 0.0634921
composition/accuracy_steps_4 = 0.0169492
composition/accuracy_steps_5 = 0.0363636
```

**Interpretation:**
The model sometimes achieved short local transitions, especially at two steps, but multi-step composition degraded sharply. This was interpreted as recurrent drift or route contamination accumulating across steps.

**Caveats:**
Step-5 accuracy being slightly higher than step-4 may reflect sampling noise or task distribution effects; the overall trend is still weak multi-step composition.

**Claim:**
Experiment 6 suggests that local recurrent transition traces did not scale into stable multi-step composition.

**Evidence:**
Composition accuracy dropped from ~16.4% at two steps to ~6.3% at three steps and ~1.7% at four steps in the full model. 

**Caveat:**
This does not prove the architecture cannot compose; it shows this implementation and training regime did not robustly compose under the audit.

**Source artifact or conversation reference:**
`exp6_accuracy_by_path_length.png`; `exp6_report.md`; assistant analysis in this thread.

---

### Result: More recurrent drive did not imply better composition

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_recurrent_drive.png`
* `exp6_report.md`

**Key metrics:**

```text
exp6_no_reward_gate composition/average_recurrent_drive = 810.056
exp6_full_route_audit composition/average_recurrent_drive = 631.713
exp6_no_context_routing composition/average_recurrent_drive = 538.361
```

`exp6_no_reward_gate` had the highest recurrent drive but did not clearly outperform all other variants on meaningful route control.

**Interpretation:**
The thread concluded that recurrent drive by itself is not equivalent to route correctness. Excitation must be shaped into route-specific attractor dynamics.

**Caveats:**
This is an interpretation of metric relationships, not a direct causal proof.

**Claim:**
High recurrent drive is not sufficient for reliable compositional traversal.

**Evidence:**
`exp6_no_reward_gate` had the highest recurrent drive but only ~15.6% best composition accuracy and negative route margin. 

**Caveat:**
Recurrent drive may still be useful if paired with stronger route selection, inhibition, or attractor stabilization.

**Source artifact or conversation reference:**
`exp6_recurrent_drive.png`; `exp6_report.md`; assistant analysis in this thread.

---

### Result: Some ablations did not reduce performance as expected

**Experiment number:**
Experiment 6

**Uploaded artifacts or plot names if mentioned:**

* `exp6_best_composition_accuracy.png`
* `exp6_accuracy_by_mode.png`
* `exp6_report.md`

**Key metrics:**

```text
exp6_no_context_routing best_composition_accuracy = 0.163934
exp6_no_reward_gate best_composition_accuracy     = 0.155738
exp6_no_inhibition best_composition_accuracy      = 0.155738
exp6_full_route_audit best_composition_accuracy   = 0.151639
exp6_no_homeostasis best_composition_accuracy     = 0.147541
```

**Interpretation:**
The full model was not clearly superior to several ablations. The assistant interpreted this as evidence that the named control mechanisms were not yet strongly causal organizers of route selection.

**Caveats:**
The `no_context_routing` variant’s higher endpoint score should not be interpreted as proof that context routing is harmful. Its route margin and confusion behavior were weaker, suggesting endpoint accuracy may be noisy or partially accidental.

**Claim:**
Reward gating, inhibition, homeostasis, and context routing were not yet decisive causal control mechanisms in this implementation.

**Evidence:**
Multiple ablations clustered near or slightly above the full model in best composition accuracy. 

**Caveat:**
This may require rerun or deeper statistical treatment before making strong claims.

**Source artifact or conversation reference:**
`exp6_best_composition_accuracy.png`; `exp6_report.md`; assistant analysis in this thread.

## 5. Key scientific conclusions supported by this thread

### Claim → Evidence → Caveat

**Claim:**
Experiment 6 should be treated as a negative-but-informative result for context-conditioned compositional route memory.

**Evidence:**
The full model achieved nonzero but weak best composition accuracy of ~15.2%, and route metrics showed wrong-route activation exceeding target-route activation.

**Caveat:**
The result does not invalidate the broader research program; recurrence and structural plasticity ablations show important load-bearing mechanisms.

---

**Claim:**
Recurrence is necessary for this task family in the tested model.

**Evidence:**
The `exp6_no_recurrence` ablation collapsed to 0% transition and composition accuracy. 

**Caveat:**
Necessary does not mean sufficient. The full model still failed robust multi-step composition.

---

**Claim:**
Structural plasticity contributes real functional signal.

**Evidence:**
The `exp6_no_structural_plasticity` ablation fell to ~4.1% best composition accuracy, far below the full model and several other ablations. 

**Caveat:**
The learned structure was not sufficiently route-specific to generate robust composition.

---

**Claim:**
Context identity and route execution are separable failure modes.

**Evidence:**
The full model’s context confusion plot was perfectly diagonal, while route margin remained negative and endpoint accuracy remained low.

**Caveat:**
This should be framed as a diagnostic insight rather than a complete mechanistic explanation.

---

**Claim:**
The current generation of the model had local recurrent/plastic signals but not stable reusable compositional operators.

**Evidence:**
Shorter path lengths performed better than longer path lengths, recurrence and structural plasticity mattered, but route margin stayed negative.

**Caveat:**
This conclusion is limited to the Experiment 6 implementation and training configuration reviewed here.

## 6. Important flaws, mistakes, or implementation concerns identified

1. **Experiment 5 methodological flaw carried into the motivation for Experiment 6**
   Experiment 5 reconstructed the symbolic concept-plus-context state after each recurrent step, weakening claims about recurrent route selection. Experiment 6 corrected this by auditing raw recurrent traversal. 

2. **Experiment 6 full model did not outperform all major ablations**
   `exp6_no_context_routing`, `exp6_no_reward_gate`, and `exp6_no_inhibition` had best composition scores close to or slightly above the full model. This weakens claims that the named mechanisms were decisively causal in this generation.

3. **Negative route margins across major variants**
   The full model’s average route margin was negative, meaning correct-route activation did not dominate wrong-route activation. This is a central mechanistic failure.

4. **Endpoint accuracy may be noisy or misleading**
   `exp6_no_context_routing` had the highest best composition score but worse route-margin behavior and mixed confusion patterns. This suggests endpoint accuracy alone is insufficient.

5. **Context confusion can overstate success**
   The full model preserved context identity, but this did not produce correct route traversal. Context classification should not be treated as equivalent to context-conditioned execution.

6. **Path-length degradation indicates recurrent drift**
   Composition accuracy degraded sharply with path length, suggesting accumulated recurrent error, attractor contamination, or weak route stabilization.

7. **No code-level audit was performed in this thread**
   The implementation files were not reviewed. Any claim about exact implementation causes is uncertain.

8. **No statistical reruns or seed analysis were discussed**
   The thread did not assess variance across random seeds. Some comparisons between close ablation scores should be considered preliminary.

9. **README/result status inconsistency**
   The uploaded `README.md` still states “Pending first Experiment 6 run,” while `exp6_report.md` contains completed results. This should be cleaned up in the repository. 

## 7. Figures or artifacts referenced

Uploaded or discussed artifacts:

```text
exp6_accuracy_by_mode.png
exp6_accuracy_by_path_length.png
exp6_adaptation_curve.png
exp6_best_composition_accuracy.png
exp6_comparison.csv
exp6_context_confusion.png
exp6_recurrent_drive.png
exp6_report.md
exp6_route_margin.png
exp6_wrong_route_activation.png
EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md
README.md
```

Important artifact roles:

| Artifact                                | Role in thread                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------------- |
| `exp6_report.md`                        | Primary numerical summary and interpretation framework                                |
| `exp6_comparison.csv`                   | Uploaded comparison table, not deeply inspected beyond plotted/report-derived metrics |
| `EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md` | Design and rationale for Experiment 6                                                 |
| `README.md`                             | Repository-level description of Experiment 6; contains stale “pending run” note       |
| `exp6_context_confusion.png`            | Used to identify preserved context identity in the full model                         |
| `exp6_route_margin.png`                 | Used to diagnose weak/negative route dominance                                        |
| `exp6_wrong_route_activation.png`       | Used to compare wrong-route activation across variants                                |
| `exp6_recurrent_drive.png`              | Used to interpret recurrent excitation vs correctness                                 |
| `exp6_accuracy_by_path_length.png`      | Used to diagnose degradation across traversal length                                  |
| `exp6_best_composition_accuracy.png`    | Used to compare full model and ablations                                              |
| `exp6_accuracy_by_mode.png`             | Used to observe low performance across contextual modes                               |
| `exp6_adaptation_curve.png`             | Used to observe low/unstable composition accuracy during training                     |

## 8. Decisions made

### Experiment design choices

* Treat Experiment 6 as the corrected successor to Experiment 5’s contextual-successor design.
* Evaluate raw recurrent traversal rather than reconstructed symbolic endpoints.
* Include route-level diagnostics, not just endpoint accuracy.
* Keep optional stressors off in the baseline suite so the route-audit question remains interpretable.

### Abandoned or weakened approaches

* Do not rely on symbolic state reconstruction as evidence of recurrent compositional traversal.
* Do not treat context-confusion success as equivalent to route-selection success.
* Do not treat higher recurrent drive as automatically better.

### Naming decisions

No new naming decisions were made in this thread.

Existing names retained:

```text
Experiment 6
Route-Audit Successor World
exp6_full_route_audit
exp6_no_recurrence
exp6_no_structural_plasticity
exp6_no_reward_gate
exp6_no_homeostasis
exp6_no_context_routing
exp6_no_inhibition
```

### Manuscript framing decisions

* Frame Experiment 6 as a **negative-but-informative result**.
* Use Experiment 6 to support the limitation that the current model generation did not yet achieve robust context-conditioned composition.
* Use Experiment 6 to support the narrower claim that recurrence and structural plasticity are load-bearing.
* Present route-margin failure as a mechanistic diagnostic.

### Follow-up experiments

No formal follow-up experiment was designed in this thread, but a follow-up direction was identified:

> build or test mechanisms that make selected routes causally dominate recurrent state evolution.

## 9. Open questions created by this thread

1. Why did `exp6_no_context_routing` slightly outperform the full model on best composition accuracy?

2. Is the endpoint accuracy difference between variants meaningful, or mostly noise?

3. Are the negative route margins caused by insufficient inhibition, weak context binding, poor route assembly separation, excessive active-set overlap, or implementation details?

4. Does the full model preserve context identity because of genuine recurrent context maintenance, or because the context assembly remains trivially detectable?

5. Would stronger route-specific inhibition improve route margin?

6. Would explicit separation between state assemblies, context assemblies, route assemblies, and target assemblies improve composition?

7. Would longer training, larger hidden-unit count, altered assembly size, or lower active-set overlap improve route margin?

8. Does Experiment 6 need multi-seed reruns before being included in the manuscript?

9. Should `exp6_no_context_routing` be rerun or audited manually because its endpoint performance and route metrics tell different stories?

10. Are the current route metrics correctly implemented and sufficient to support mechanistic claims?

11. Should Experiment 6 be placed in the main manuscript as a limitation or in supplementary material as a diagnostic predecessor to later experiments?

12. Does the README need to be updated to remove the stale “Pending first Experiment 6 run” text?

## 10. Relationship to the first manuscript

### Central claim

Experiment 6 does **not** strongly support the central manuscript claim if the central claim is stated as:

> The current-generation model robustly performs context-conditioned compositional route memory.

Experiment 6 weakens that version of the claim.

### Supporting claim

Experiment 6 supports narrower claims:

* Recurrent dynamics are necessary for the tested contextual traversal task.
* Structural plasticity contributes meaningful functional signal.
* Raw recurrent audit is a better standard than reconstructed symbolic traversal.
* Context identity can be preserved while route execution fails, showing the importance of mechanistic route diagnostics.

### Limitation

Experiment 6 is highly useful as a limitation:

> The tested model could represent context and showed load-bearing recurrent/plastic mechanisms, but it did not reliably bind context, current state, and next-state transformation into a reusable compositional operator.

### Future work

Experiment 6 motivates future work on:

* stronger route separation;
* explicit route-selection mechanisms;
* better inhibition of incompatible routes;
* attractor stabilization;
* route-margin optimization;
* multi-seed validation;
* delayed reward and rule reversal stressors.

### Supplementary material

Experiment 6 is a strong candidate for supplementary material if the main manuscript focuses on later successful experiments. It can be used as a methodological correction and diagnostic failure case showing why raw recurrent audit matters.

## 11. Claims-and-evidence rows contributed by this thread

| Claim                                                                               | Evidence                                                                                                                   | Caveat                                                                       | Experiment(s) | Artifact(s)                                                                     | Manuscript status    |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------- | -------------------- |
| Raw recurrent audit is necessary to avoid overclaiming route selection.             | Experiment 5 rebuilt symbolic state after each step; Experiment 6 corrected traversal to use actual recurrent active sets. | This thread did not reanalyze Experiment 5 artifacts directly.               | 5, 6          | `EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md`                                         | Strong               |
| The full Experiment 6 model did not robustly solve context-conditioned composition. | `exp6_full_route_audit` best composition accuracy was ~0.151639.                                                           | Needs seed variance and baseline comparison before final quantitative claim. | 6             | `exp6_report.md`, `exp6_best_composition_accuracy.png`                          | Preliminary          |
| Recurrence was load-bearing.                                                        | `exp6_no_recurrence` had 0 transition and 0 composition accuracy.                                                          | Shows necessity in this setup, not sufficiency.                              | 6             | `exp6_report.md`, `exp6_recurrent_drive.png`                                    | Strong               |
| Structural plasticity was load-bearing.                                             | `exp6_no_structural_plasticity` fell to ~0.0409836 best composition accuracy.                                              | Does not prove learned structure was well organized.                         | 6             | `exp6_report.md`, `exp6_best_composition_accuracy.png`                          | Promising            |
| Correct-route activation did not dominate wrong-route activation.                   | Full model target-route activation ~0.173116; wrong-route activation ~0.199278; route margin ~-0.0261622.                  | Depends on route metric implementation; code not audited here.               | 6             | `exp6_report.md`, `exp6_route_margin.png`, `exp6_wrong_route_activation.png`    | Strong               |
| Context identity preservation is not equivalent to route execution.                 | Full model context confusion plot was diagonal, but composition accuracy was low and route margin negative.                | Context-confusion metric may itself need audit.                              | 6             | `exp6_context_confusion.png`, `exp6_report.md`                                  | Promising            |
| Multi-step composition degraded with traversal length.                              | Full model accuracy dropped from ~0.164179 at 2 steps to ~0.0634921 at 3 steps and ~0.0169492 at 4 steps.                  | Step-5 value slightly rebounds, so the curve is not perfectly monotonic.     | 6             | `exp6_accuracy_by_path_length.png`, `exp6_report.md`                            | Promising            |
| Higher recurrent drive does not imply better route control.                         | `exp6_no_reward_gate` had highest recurrent drive but did not achieve clean route dominance or strong composition.         | Correlational interpretation only.                                           | 6             | `exp6_recurrent_drive.png`, `exp6_report.md`                                    | Preliminary          |
| Endpoint accuracy alone is insufficient for evaluating this model family.           | `exp6_no_context_routing` had the highest best composition score but poor route margin and more confused route behavior.   | Needs deeper audit of trajectories and seeds.                                | 6             | `exp6_best_composition_accuracy.png`, `exp6_route_margin.png`, `exp6_report.md` | Needs metric cleanup |
| Experiment 6 should be framed as a negative-but-informative result.                 | Load-bearing recurrence/plasticity coexisted with failure of robust route dominance.                                       | Manuscript placement depends on later experiment narrative.                  | 6             | All Experiment 6 artifacts                                                      | Strong               |
| Repository docs need cleanup.                                                       | `README.md` says completed runs are pending, while `exp6_report.md` contains completed results.                            | Simple documentation mismatch; not a scientific flaw.                        | 6             | `README.md`, `exp6_report.md`                                                   | Needs metric cleanup |

## 12. Recommended follow-up actions

1. Update `README.md` to replace the stale “Pending first Experiment 6 run” section with the completed result summary.

2. Add this digest to the Experiment 6 directory, likely as:

```text
analysis/exp6/thread_digest.md
```

or:

```text
EXPERIMENT_6_THREAD_DIGEST.md
```

3. Add a short “Interpretation” section to `EXPERIMENT_6_ROUTE_AUDIT_SUCCESSOR.md` stating that the experiment produced a negative-but-informative result.

4. Preserve the distinction between:

```text
context identity preserved
```

and:

```text
context-conditioned route execution successful
```

5. Do not claim Experiment 6 demonstrates robust compositional route memory.

6. Use Experiment 6 as evidence that recurrence and structural plasticity are load-bearing.

7. Use Experiment 6 as evidence that route-margin metrics are essential.

8. Consider rerunning Experiment 6 with multiple random seeds before using exact numeric comparisons in the manuscript.

9. Audit `exp6_no_context_routing` trajectories because it had the highest endpoint score but poor route metrics.

10. Inspect the implementation files before making any code-level causal claim about why route margin failed.

11. Consider a successor experiment focused specifically on making route selection causally dominate recurrent state evolution.

12. In the manuscript, place Experiment 6 either as:

* a limitation/diagnostic result in the main text; or
* a supplementary methodological correction motivating later experiments.
