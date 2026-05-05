# Thread Digest: Experiments 12–13, Novelty Assessment, and Manuscript Consolidation Plan

## 1. Thread scope

This thread covered the transition from **Experiment 12 analysis** into **Experiment 13 design, implementation, execution analysis, novelty reassessment, and repository/manuscript consolidation planning**.

The thread had five main purposes:

1. Analyze **Experiment 12** as a capacity, interference, continual-retention, held-out composition, context-noise, and consolidation-pressure stress test of the Experiment 11 mechanism.
2. Design and package **Experiment 13** as a “breaking point” experiment that deliberately pushes the model out of the ceiling regime.
3. Analyze completed **Experiment 13** results from `analysis13.zip`.
4. Consume and interpret a **novelty assessment** that positioned the work relative to continual learning, task/context gating, parameter isolation, hypernetworks, cognitive-map models, hippocampal sequence models, and neuromodulated plasticity.
5. Plan a practical repo-consolidation workflow for moving all analysis artifacts and thread digests into GitHub for manuscript preparation.

The central manuscript framing that emerged was:

> A synthetic continual compositional route-memory benchmark shows that context-indexed structural plasticity can store incompatible local transition systems without destructive overwriting, while recurrent dynamics are required to convert one-step route memories into multi-step execution.

This framing was explicitly narrowed after the novelty assessment, which warned against claiming generic novelty for context cues, task gating, or continual learning in general. The assessment judged the defensible novelty to be the combined mechanism: a structural-plastic recurrent route-memory substrate that stores mutually incompatible local transition systems, retrieves them by context/world, and still requires recurrence for multistep execution. 

---

## 2. Experiments discussed

### Experiment 11 — Context memory / incompatible world rebinding

Discussed as prior context and as the mechanism being stress-tested by Experiments 12 and 13.

Short description:

* Experiment 11 tested whether incompatible rule worlds could be learned over a shared symbolic substrate while remaining retrievable by world/context.
* The novelty assessment described Experiment 11 as the backbone of the narrower manuscript claim because it apparently showed a clean dissociation among structural storage, contextual retrieval, and recurrent execution. 

Status in this thread:

* Not reanalyzed directly from uploaded Experiment 11 artifacts.
* Used as conceptual and experimental foundation for Experiments 12 and 13.

---

### Experiment 12 — Capacity, interference, and compositional generalization

Short description:

* Full stress test of Experiment 11 mechanism.
* Scaled incompatible world count.
* Measured continual retention.
* Tested held-out multi-step compositions.
* Swept world-context noise and consolidation strength.

The uploaded Experiment 12 report defined the run as a full profile with 30 seeds, world counts `[2, 4, 8, 16, 32]`, route lengths `[1, 2, 4, 8, 12]`, 32 nodes, 3 modes, and eight variants. 

Variants:

* `exp12_full_context_separated_memory`
* `exp12_world_gated_plasticity`
* `exp12_no_consolidation`
* `exp12_no_world_context`
* `exp12_no_context_binding`
* `exp12_no_recurrence`
* `exp12_no_structural_plasticity`
* `exp12_strong_consolidation`

Status in this thread:

* Fully analyzed.
* Interpreted as strong support for the core mechanism, but with important caveats around context-noise sweeps, consolidation framing, and no-context-binding interpretation.

---

### Experiment 13 — Breaking point under capacity, context, holdout, and continuous-input pressure

Short description:

* Designed in this thread.
* Packaged as a downloadable local implementation.
* Intended to push beyond Experiment 12’s ceiling regime.
* Tested structural budget limits, local versus global capacity pressure, context corruption, primitive holdout, consolidation under pressure, and a continuous/noisy input bridge.

Artifacts generated in this thread:

* `plastic_graph_mnist_experiment13_breaking_point.zip`
* `run_experiment13.py`
* `validate_exp13.py`
* `start_exp13.ps1`
* `README.md`
* smoke-run outputs under `analysis/`

Status in this thread:

* Designed and implemented.
* User later ran it locally and uploaded `analysis13.zip`.
* Results were analyzed in detail.

---

### Experiment 13.1 — Publication hardening audit

Short description:

* Proposed but not implemented in this thread.
* Intended as a focused correction/hardening pass over Experiment 13.

Purpose:

* Fix holdout metrics.
* Rename or replace weak/no-context-binding ablation.
* Add stochastic context corruption.
* Add consolidation dose-response under finite capacity.
* Add capacity-law summaries.
* Improve publication reliability.

Status:

* Proposed only.
* No implementation was generated in this thread.

---

### Experiment 14 — Latent world inference / applied perceptual bridge

Short description:

* Proposed future direction.
* Not implemented.
* Discussed as a more novel next-wave direction after 13.1 and baselines.

Two possible directions were discussed:

1. **Latent world inference / self-indexed route memory**

   * Model infers world/context from prediction error rather than receiving oracle world labels.
2. **Visual-state contextual route memory**

   * Use images or continuous perceptual states as inputs, with route memory operating downstream of noisy/non-symbolic state decoding.

Status:

* Proposed only.
* Not implemented in this thread.

---

## 3. Experimental designs created or modified here

### Design: Experiment 13 — Breaking point / capacity-pressure regime

* **Experiment number:** 13

* **Purpose:**
  Push the Experiment 12 mechanism out of the ceiling regime and identify failure boundaries under structural capacity pressure, context corruption, primitive holdout, recurrence removal, and noisy continuous input.

* **Hypothesis:**
  The full model should succeed when structural capacity is sufficient, context identity is clean, and recurrence is available; it should fail predictably when structural capacity, world context, recurrence, or primitive coverage is degraded.

* **Model variants:**
  The generated implementation included variants corresponding to:

  * full context-separated memory;
  * no consolidation;
  * strong consolidation;
  * world-gated plasticity;
  * no world context;
  * no recurrence;
  * no structural plasticity;
  * no/weak context binding, later identified as needing clearer naming.

* **Metrics:**
  Discussed and/or analyzed metrics included:

  * composition accuracy;
  * route-table accuracy;
  * composition-route gap;
  * world margin;
  * wrong-world activation;
  * top-1 world accuracy;
  * retention matrices;
  * budget-breaking curves;
  * local versus global budget performance;
  * primitive holdout accuracy;
  * unseen primitive accuracy;
  * continuous decode accuracy;
  * composition accuracy under noisy continuous decoding.

* **Expected outcomes:**
  Expected failure boundaries:

  * no recurrence: one-step route-table memory preserved, multi-step composition fails;
  * no world context: destructive interference across incompatible worlds;
  * no structural plasticity: near-chance storage;
  * finite memory: performance drops as available structure falls below exact capacity;
  * local budget pressure: long-route composition should be especially brittle;
  * primitive holdout: seen-transition composition should survive better than unseen primitive inference;
  * continuous noise: route memory should degrade with upstream decoding quality.

* **Implementation notes:**
  A downloadable implementation package was created:

  * `plastic_graph_mnist_experiment13_breaking_point.zip`
  * local run commands:

    * `powershell -ExecutionPolicy Bypass -File .\start_exp13.ps1 -Profile smoke -Clean`
    * `powershell -ExecutionPolicy Bypass -File .\start_exp13.ps1 -Profile standard -Clean`
    * `powershell -ExecutionPolicy Bypass -File .\start_exp13.ps1 -Profile full -Clean`

* **Known risks:**

  * Initial smoke run was too small to strongly evaluate consolidation.
  * Later analysis showed no-context-binding was not a pure ablation.
  * Primitive holdout metrics needed cleanup.
  * Context corruption was partly deterministic/threshold-like.
  * Continuous-input bridge was not yet an end-to-end perceptual learning demonstration.

---

### Design: Experiment 13.1 — Publication hardening audit

* **Experiment number:** 13.1

* **Purpose:**
  Correct, harden, and publishably analyze Experiment 13’s most important boundary results.

* **Hypothesis:**
  Cleaner metrics and harder context/capacity tests should preserve the major conclusions while removing obvious reviewer attack surfaces.

* **Model variants:**
  Proposed:

  * full model;
  * no consolidation;
  * graded consolidation strengths;
  * strong consolidation;
  * true no-context-binding;
  * renamed weak-context-binding/oracle-clean variant;
  * no recurrence;
  * no world context;
  * no structural plasticity;
  * world-gated plasticity.

* **Metrics:**
  Proposed additions:

  * `route_table_accuracy_all`;
  * `route_table_accuracy_seen`;
  * `route_table_accuracy_unseen`;
  * `composition_accuracy_seen_routes`;
  * `composition_accuracy_unseen_required_routes`;
  * `constraint_satisfied_fraction`;
  * stochastic context selection accuracy;
  * retention center of mass;
  * early-world retention;
  * late-world retention;
  * edge age distribution;
  * memory per retained world;
  * active edge coverage per world and node.

* **Expected outcomes:**

  * Consolidation should show an old-memory versus new-memory retention bias under finite capacity.
  * Stochastic context corruption should produce graded degradation rather than only a hard threshold.
  * True no-context-binding should reveal behavioral or mechanistic consequences more cleanly than the current weak-binding/oracle-clean variant.
  * Holdout metrics should clarify that the model composes stored primitives but does not infer missing primitive transitions.

* **Implementation notes:**
  No implementation was produced in this thread.

* **Known risks:**

  * Could become too broad if not kept focused.
  * Must remain a hardening audit rather than a new uncontrolled experiment.
  * Needs enough seeds for publication-grade confidence.

---

### Design: Experiment 14 — Latent world inference / applied bridge

* **Experiment number:** 14

* **Purpose:**
  Proposed future direction to push novelty beyond oracle world labels and purely symbolic states.

* **Hypothesis:**
  A more novel neuroplastic-network direction would allow the model to infer latent world/context from prediction error or partial evidence, allocate/retrieve route fields, and operate downstream of noisy perceptual inputs.

* **Model variants:**
  Not specified in implementation-level detail.

* **Metrics:**
  Proposed:

  * latent world inference accuracy;
  * prediction-error-triggered allocation;
  * context retrieval from partial evidence;
  * multi-step route composition after inferred context;
  * visual/noisy state decoding accuracy;
  * route execution accuracy from perceptual inputs;
  * retention across sequentially learned latent worlds.

* **Expected outcomes:**
  A successful model would reduce dependence on explicit task/world labels and move closer to biological indexing/remapping questions.

* **Implementation notes:**
  Suggested applied bridge:

  * Fashion-MNIST, EMNIST, CIFAR-10, or rendered gridworld states;
  * images map to latent states;
  * worlds define incompatible transitions over same perceptual state/action space;
  * route memory executes multi-step transitions after decoding image-derived state.

* **Known risks:**

  * Too ambitious before 13.1 and baselines.
  * Could distract from manuscript consolidation.
  * Must avoid claiming end-to-end perception unless truly demonstrated.

---

### Design: Repository/manuscript consolidation workflow

* **Experiment number:** Not an experiment.

* **Purpose:**
  Move scattered analysis from ChatGPT threads and local artifacts into a canonical GitHub repository structure for manuscript preparation.

* **Hypothesis:**
  A strict documentation and evidence architecture will prevent loss of context, reduce overclaiming, and make the manuscript defensible.

* **Model variants:**
  Not applicable.

* **Metrics:**
  Documentation completeness:

  * experiment registry complete;
  * artifact index complete;
  * thread digests imported;
  * claims linked to evidence;
  * missing artifacts identified;
  * figure plan created;
  * reproducibility audit created.

* **Expected outcomes:**
  A repository that supports manuscript writing with:

  * `CLAIMS_AND_EVIDENCE.md`;
  * `EXPERIMENT_REGISTRY.md`;
  * per-experiment summaries;
  * thread digests;
  * figure plan;
  * baseline requirements;
  * reproducibility audit.

* **Implementation notes:**
  A verbose Codex/local-agent prompt was created to:

  * create the `docs/` scaffold;
  * inventory artifacts;
  * create experiment summary stubs;
  * build manuscript evidence scaffolds;
  * define thread-digest workflow;
  * avoid inventing conclusions.

* **Known risks:**

  * Agent sprawl.
  * Duplicate or conflicting summaries.
  * Claims becoming detached from source artifacts.
  * Old analysis being imported without caveats.

---

## 4. Results analyzed here

### Result 1: Experiment 12 scales cleanly under full context-separated memory

Claim:
The full Experiment 12 model preserved perfect composition and route-table accuracy up to 32 incompatible worlds under the tested symbolic regime.

Evidence:
The Experiment 12 capacity snapshot showed `exp12_full_context_separated_memory` at composition accuracy `1.0` and route-table accuracy `1.0` for world counts 2, 4, 8, 16, and 32. 

Caveat:
This was a controlled synthetic symbolic route-memory regime. It does not prove general continual learning or biological memory.

Source artifact or conversation reference:
`exp12_report.md`; `capacity_final_summary.csv`; `plots/exp12_capacity_composition_accuracy.png`; `plots/exp12_capacity_route_table_accuracy.png`.

---

### Result 2: Experiment 12 no-recurrence dissociates one-step storage from multi-step composition

Claim:
Recurrence is required for multi-step composition even when one-step route-table knowledge is intact.

Evidence:
In Experiment 12, `exp12_no_recurrence` preserved route-table accuracy at `1.0` across tested world counts but had composition accuracy around `0.05–0.06`, including `0.0565755` at 32 worlds. 

Caveat:
This supports a storage/execution dissociation in the synthetic route-memory task; it does not by itself prove a general theory of recurrent biological planning.

Source artifact or conversation reference:
`exp12_report.md`; `capacity_final_summary.csv`; `plots/exp12_route_table_composition_gap.png`.

---

### Result 3: Experiment 12 no-structural-plasticity remains near chance

Claim:
Structural plasticity is required for reliable route-memory storage in this experimental regime.

Evidence:
In Experiment 12, `exp12_no_structural_plasticity` stayed near chance, with composition accuracy around `0.036–0.039` and route-table accuracy around `0.030–0.033` across world counts. 

Caveat:
The chance baseline reflects the 32-node symbolic setting. The result establishes necessity within this implementation, not a universal biological claim.

Source artifact or conversation reference:
`exp12_report.md`; `capacity_final_summary.csv`; `plots/exp12_capacity_composition_accuracy.png`.

---

### Result 4: Experiment 12 no-world-context shows destructive interference as worlds accumulate

Claim:
World/context indexing is required to prevent incompatible transition systems from collapsing into a shared interfering route table.

Evidence:
In Experiment 12, `exp12_no_world_context` composition accuracy dropped from about `0.519444` at 2 worlds to `0.0706055` at 32 worlds, with route-table accuracy similarly declining. 

Caveat:
This is strong internal evidence against a shared route table in this benchmark, but external baselines are still needed to show how known continual-learning methods compare.

Source artifact or conversation reference:
`exp12_report.md`; `capacity_final_summary.csv`; `plots/exp12_capacity_composition_accuracy.png`.

---

### Result 5: Experiment 12 consolidation is better framed as pressure/modulation, not essential storage

Claim:
Consolidation was not required for perfect accuracy in Experiment 12’s low-pressure/full-capacity regime, but it modulated separation margins.

Evidence:
`exp12_no_consolidation`, `exp12_full_context_separated_memory`, and `exp12_strong_consolidation` all achieved perfect composition and route-table accuracy across world counts in the Experiment 12 capacity snapshot. The report’s interpretation checklist explicitly stated that consolidation should be interpreted as a pressure/modulation study, not assumed to be essential. 

Caveat:
Experiment 12 did not place enough pressure on the system to make consolidation behaviorally necessary. Experiment 13 later suggested consolidation matters more under finite sequential capacity.

Source artifact or conversation reference:
`exp12_report.md`; `consolidation_pressure_summary.csv`; `plots/exp12_consolidation_pressure_accuracy.png`; `plots/exp12_consolidation_pressure_world_margin.png`.

---

### Result 6: Experiment 12 context-bleed and context-dropout sweeps were considered inconclusive

Claim:
The flat context-bleed/dropout curves in Experiment 12 should not be used as strong evidence of context-noise robustness without further validation.

Evidence:
In this thread, the context-bleed and dropout plots were interpreted as too flat: composition accuracy and world margins appeared essentially unchanged across tested bleed/dropout settings.

Caveat:
Possible explanations included genuine robustness, perturbation not affecting the decision path, or perturbation levels being too weak. The thread concluded that the result required follow-up context corruption tests.

Source artifact or conversation reference:
`context_bleed_summary.csv`; `context_dropout_summary.csv`; `plots/exp12_context_bleed_composition.png`; `plots/exp12_context_dropout_composition.png`; conversation analysis of Experiment 12.

---

### Result 7: Experiment 12 held-out composition was promising but should be described carefully

Claim:
Experiment 12 supported held-out multi-step composition over stored one-step transitions, but not broad abstract generalization.

Evidence:
The uploaded report included `heldout_generalization_summary.csv` and `plots/exp12_heldout_generalization_by_length.png` as generated files. The thread analysis interpreted the result as evidence for held-out route execution from known primitives rather than inference of unseen transitions. 

Caveat:
The term “generalization” should be used carefully. The safer phrase is “held-out multi-step compositional execution over learned one-step transitions.”

Source artifact or conversation reference:
`heldout_generalization_summary.csv`; `plots/exp12_heldout_generalization_by_length.png`; conversation analysis of Experiment 12.

---

### Result 8: Experiment 13 global budget pressure created a breaking curve

Claim:
Under global memory pressure, the full model degraded as available structural budget decreased and recovered at exact/surplus capacity.

Evidence:
The analysis of `analysis13.zip` stated that at 32 worlds and route length 12, full-model composition accuracy was approximately:

* `0.2755` at budget ratio `0.25`;
* `0.5173` at `0.50`;
* `0.7579` at `0.75`;
* `1.0` at `1.0`;
* `1.0` at `1.25`.

Caveat:
The global-budget failure appeared route-length independent, suggesting it may reflect retaining/dropping coherent world-level transition systems rather than random edge-level damage.

Source artifact or conversation reference:
`analysis13.zip`; conversation analysis of Experiment 13; plot `exp13_budget_breaking_curve_full_vs_consolidation.png`.

---

### Result 9: Experiment 13 local budget pressure was more damaging to long-route composition than global pressure

Claim:
Local structural capacity pressure revealed that multi-step route execution requires locally coherent transition coverage, not merely partial one-step table accuracy.

Evidence:
The analysis of `analysis13.zip` stated that at 32 worlds, route length 12:

* local budget `0.25`: route-table accuracy `~0.2721`, composition accuracy `~0.0417`;
* local budget `0.50`: route-table accuracy `~0.5148`, composition accuracy `~0.0596`;
* local budget `0.75`: route-table accuracy `~0.7575`, composition accuracy `~0.1379`;
* local budget `1.00`: both `1.0`.

Caveat:
This result is from the uploaded Experiment 13 analysis as discussed in the conversation; the exact source CSV should be cited from the repo once imported.

Source artifact or conversation reference:
`analysis13.zip`; Experiment 13 summary CSVs; conversation analysis of Experiment 13.

---

### Result 10: Experiment 13 confirmed no-recurrence storage/execution dissociation

Claim:
Experiment 13 replicated the key finding that recurrence is necessary for multi-step execution even when one-step route-table memory is intact.

Evidence:
The analysis stated that at 32 worlds, route length 12, and budget `1.0`, the no-recurrence variant had route-table accuracy `1.0` but composition accuracy around `0.0449`.

Caveat:
Still a symbolic route-memory benchmark; external recurrent baselines are needed.

Source artifact or conversation reference:
`analysis13.zip`; conversation analysis of Experiment 13.

---

### Result 11: Experiment 13 showed consolidation as a stability-plasticity bias

Claim:
Under finite capacity, consolidation appeared to protect older worlds, while no-consolidation favored more recent worlds.

Evidence:
The analysis of Experiment 13 retention heatmaps stated that at final checkpoint with 32 worlds and budget `0.5`, the consolidated/full model preferentially preserved early worlds, while the no-consolidation model preferentially preserved later worlds.

Caveat:
The thread explicitly stated this needs a consolidation dose-response audit before becoming a strong manuscript claim.

Source artifact or conversation reference:
`analysis13.zip`; `exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.5.png`; `exp13_retention_heatmap_exp13_no_consolidation_budget_0.5.png`; conversation analysis of Experiment 13.

---

### Result 12: Experiment 13 adversarial context corruption produced a hard selection threshold

Claim:
The model remained correct when the correct context signal dominated and collapsed when the wrong context signal exceeded it.

Evidence:
The thread analysis reported full-model top-1 world accuracy and composition accuracy at `1.0` through adversarial mixture `0.49`, then top-1 world accuracy `0.0` and composition near chance at `0.51` and above.

Caveat:
This is a deterministic argmax-like threshold, not a graded realistic context-noise robustness result. Stochastic context corruption was proposed for 13.1.

Source artifact or conversation reference:
`analysis13.zip`; conversation analysis of Experiment 13.

---

### Result 13: Experiment 13 true holdout clarified that the model composes seen primitives but does not infer unseen primitives

Claim:
The model performs composition over stored local transitions but does not infer missing primitive transitions.

Evidence:
The thread analysis reported that full-model composition over seen primitives remained `1.0` through holdout rates up to `0.4`, then dropped to about `0.6773` at `0.6`, while one-step unseen primitive accuracy stayed near chance, around `0.027–0.035`.

Caveat:
The thread identified a metric issue: route-table accuracy appeared to be computed over all transitions rather than separated into seen and unseen subsets. Metric cleanup was proposed for Experiment 13.1.

Source artifact or conversation reference:
`analysis13.zip`; conversation analysis of Experiment 13.

---

### Result 14: Experiment 13 continuous front-end bridge was promising but preliminary

Claim:
The route-memory mechanism can operate downstream of noisy continuous state decoding, but this does not yet prove end-to-end perceptual learning.

Evidence:
The thread analysis reported full-model continuous decode/composition degradation as noise increased:

* noise `0.00–0.10`: decode and composition near `1.0`;
* noise `0.20`: decode `~0.9920`, composition `~0.9911`;
* noise `0.35`: decode `~0.7586`, composition `~0.7924`;
* noise `1.00`: decode `~0.1719`, composition `~0.3471`.

Caveat:
The continuous front-end was described as a prototype-vector or noisy decoder bridge, not an end-to-end learned perceptual system.

Source artifact or conversation reference:
`analysis13.zip`; conversation analysis of Experiment 13.

---

### Result 15: Novelty assessment narrowed the publication claim

Claim:
The work is potentially publishable, but the novelty should be framed narrowly around structural-plastic recurrent route memory rather than broad claims about context gating, continual learning, or hippocampal theory.

Evidence:
The novelty assessment stated that the story is “novel enough to justify publication pursuit” but not yet strong enough for a well-known journal in its current evidentiary form. It identified the defensible claim as a structural-plastic recurrent route-memory substrate that stores mutually incompatible local transition systems, retrieves them by world/context, and requires recurrence for multistep composition. 

Caveat:
External baselines, capacity/failure laws, seed-level reporting, and careful biological framing remain required.

Source artifact or conversation reference:
`Pasted text.txt`; novelty assessment.

---

## 5. Key scientific conclusions supported by this thread

### Conclusion 1: The core mechanism is structural plasticity + world/context indexing + recurrence

Claim:
The most defensible mechanistic decomposition is: structural plasticity stores local route transitions, context/world indexing selects the relevant route field, and recurrence executes multi-step composition.

Evidence:
Experiment 12 showed no-structural-plasticity near chance, no-world-context destructive degradation with increasing worlds, and no-recurrence preserving route-table accuracy while failing composition.  Experiment 13 replicated and extended these dissociations under capacity pressure.

Caveat:
This conclusion is supported within the symbolic route-memory benchmark. External baselines are still missing.

---

### Conclusion 2: Recurrence is the strongest clean mechanistic dissociation

Claim:
The no-recurrence result is one of the strongest manuscript-grade findings because it separates one-step route storage from multi-step route execution.

Evidence:
In Experiment 12, no-recurrence preserved route-table accuracy at `1.0` across world counts but composition remained near `0.05–0.06`.  Experiment 13 showed the same pattern under exact capacity.

Caveat:
The paper should not claim recurrence itself is novel; the novelty is the specific dissociation inside a continual compositional memory benchmark.

---

### Conclusion 3: Consolidation is not essential in low-pressure regimes but becomes meaningful under finite-capacity retention

Claim:
Consolidation should be framed as a stability-plasticity bias rather than as the core memory mechanism.

Evidence:
Experiment 12 showed no-consolidation and strong-consolidation variants both reaching perfect accuracy across tested world counts.  Experiment 13 analysis suggested consolidation changes which memories survive under finite sequential capacity.

Caveat:
Experiment 13’s consolidation finding needs dose-response hardening in 13.1 before becoming a central manuscript claim.

---

### Conclusion 4: The current model composes stored primitives but does not infer unseen primitive transitions

Claim:
The architecture is currently best understood as a contextual structural memory and composition system, not an abstract rule-induction system.

Evidence:
Experiment 13 analysis reported high composition over seen primitives, but near-chance performance on unseen primitive transitions.

Caveat:
Holdout metrics need cleanup to separate all-transition, seen-transition, and unseen-transition route-table accuracy.

---

### Conclusion 5: Experiment 13 moved the project from success demonstration to failure-boundary mapping

Claim:
Experiment 13 made the research more scientifically credible by showing where and how the mechanism breaks.

Evidence:
Experiment 13 analyzed global budget failure, local capacity failure, context-corruption threshold failure, primitive-holdout failure, recurrence failure, no-world-context interference, and continuous-input degradation.

Caveat:
Some failure tests require metric cleanup or stronger stochastic variants before publication.

---

### Conclusion 6: The novelty is combinatorial, not atomic

Claim:
The work’s novelty does not lie in context gating, recurrence, structural plasticity, or continual learning individually; it lies in their controlled conjunction inside a route-memory benchmark with clean ablations.

Evidence:
The novelty assessment explicitly stated that the strongest novelty is “combinatorial, not atomic,” and identified overlap with continual-learning, parameter-isolation, hypernetwork, superposition, neuromodulated-plasticity, and cognitive-map literatures. 

Caveat:
This requires careful prior-art positioning and external baselines.

---

## 6. Important flaws, mistakes, or implementation concerns identified

### Flaw 1: Experiment 12 context-bleed/dropout sweeps were too flat

* The thread judged the flatness of the Experiment 12 context-noise plots as suspicious or inconclusive.
* The perturbation may not have affected the decision path.
* Follow-up stochastic or adversarial context corruption was required.

Status: partially addressed by Experiment 13 adversarial context corruption; still needs stochastic/graded corruption in 13.1.

---

### Flaw 2: Experiment 13 no-context-binding variant was not a pure ablation

* The thread identified that the Experiment 13 `no_context_binding` condition appeared to have `context_binding_strength = 0.15` and `query_uses_true_world_when_clean = true`.
* This makes it more like weak-context-binding or oracle-clean-context than true no-context-binding.

Status: needs renaming or replacement in 13.1.

---

### Flaw 3: Experiment 13 holdout metrics were confusing

* Route-table accuracy in true-holdout analysis appeared to be computed over all transitions.
* This made route-table accuracy look high even when unseen primitive performance was near chance.

Required fix:

* Add `route_table_accuracy_all`;
* `route_table_accuracy_seen`;
* `route_table_accuracy_unseen`;
* `composition_accuracy_seen_routes`;
* `composition_accuracy_unseen_required_routes`;
* `constraint_satisfied_fraction`.

Status: proposed for 13.1.

---

### Flaw 4: Experiment 13 context corruption used a hard threshold

* Adversarial mixture produced a clean flip around `0.49–0.51`.
* This is useful but partly artificial.
* It does not show realistic graded robustness.

Required fix:

* Add stochastic world-score noise;
* softmax temperature;
* Gumbel noise;
* per-trial dropout;
* multiple wrong-world competitors.

Status: proposed for 13.1.

---

### Flaw 5: External baselines are missing

* The novelty assessment identified this as a P0 blocker.
* Without baselines, reviewers can argue the work is a rebranding of context gating, task masks, replay, parameter isolation, hypernetworks, or cognitive-map models. 

Minimum proposed baseline families:

* XdG/SI or stabilization-plus-gating;
* replay;
* task-mask/parameter-isolation such as HAT or PackNet;
* hypernetwork or superposition;
* possible CSCG-inspired cloned-state baseline.

Status: not yet implemented.

---

### Flaw 6: Biological framing could overreach

* The novelty assessment warned against presenting the system as a solved hippocampal theory.
* The safe framing is computationally inspired by indexing/remapping/structural plasticity, not a biological explanation.

Status: must be handled in manuscript writing.

---

### Flaw 7: Repository analysis was not yet consolidated

* User noted that analysis artifacts and interpretations lived in ChatGPT threads rather than the GitHub repo.
* This created risk of losing context or making unsupported claims.

Status: repo-consolidation prompt and workflow were created in this thread.

---

## 7. Figures or artifacts referenced

### Experiment 12 uploaded/generated artifacts

Data/report files:

* `continual_retention_summary.csv`
* `exp12_final_memory_index.csv`
* `exp12_report.md`
* `heldout_generalization_summary.csv`
* `metrics.csv`
* `progress.jsonl`
* `runs.csv`
* `capacity_final_summary.csv`
* `consolidation_pressure_summary.csv`
* `context_bleed_summary.csv`
* `context_dropout_summary.csv`

Plots:

* `plots/exp12_capacity_composition_accuracy.png`
* `plots/exp12_capacity_route_table_accuracy.png`
* `plots/exp12_capacity_wrong_world_activation.png`
* `plots/exp12_consolidation_pressure_accuracy.png`
* `plots/exp12_consolidation_pressure_world_margin.png`
* `plots/exp12_context_bleed_composition.png`
* `plots/exp12_context_bleed_world_margin.png`
* `plots/exp12_context_dropout_composition.png`
* `plots/exp12_context_dropout_world_margin.png`
* `plots/exp12_continual_retention_heatmap_full_model.png`
* `plots/exp12_heldout_generalization_by_length.png`
* `plots/exp12_route_table_composition_gap.png`

The Experiment 12 report listed these generated files explicitly. 

---

### Experiment 13 generated implementation package

* `plastic_graph_mnist_experiment13_breaking_point.zip`
* `run_experiment13.py`
* `validate_exp13.py`
* `start_exp13.ps1`
* `README.md`
* `requirements.txt`
* smoke-run `analysis/` outputs
* `exp13_report.md`
* `validation_report.md`

---

### Experiment 13 uploaded result package

* `analysis13.zip`

Specific plots discussed from Experiment 13:

* `exp13_budget_breaking_curve_full_vs_consolidation.png`
* `exp13_retention_heatmap_exp13_full_context_separated_memory_budget_0.5.png`
* `exp13_retention_heatmap_exp13_no_consolidation_budget_0.5.png`

Other Experiment 13 artifacts discussed generally:

* budget summary CSVs;
* local/global capacity pressure summaries;
* context corruption summaries;
* true holdout summaries;
* continuous front-end/noisy decoding summaries;
* validation reports.

Exact filenames beyond those explicitly displayed in the thread should be verified from `analysis13.zip` during repo import.

---

### Novelty assessment artifact

* `Pasted text.txt`

Main referenced content:

* executive summary;
* prior-art overlap;
* closest threats to novelty;
* recommended citations;
* publishability gaps;
* recommended next experiments;
* safer manuscript framing.

---

### Repository consolidation artifacts proposed

Proposed docs scaffold:

* `docs/manuscript/MANUSCRIPT_SPINE.md`
* `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
* `docs/manuscript/FIGURE_PLAN.md`
* `docs/manuscript/RESULTS_STORYBOARD.md`
* `docs/manuscript/LIMITATIONS_AND_THREATS.md`
* `docs/manuscript/NOVELTY_POSITIONING.md`
* `docs/manuscript/BASELINE_REQUIREMENTS.md`
* `docs/manuscript/MANUSCRIPT_TODO.md`
* `docs/experiments/EXPERIMENT_REGISTRY.md`
* `docs/experiments/EXPERIMENT_SUMMARY_TEMPLATE.md`
* `docs/experiments/EXPERIMENT_CLAIMS_MATRIX.csv`
* `docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv`
* `docs/theory/CORE_THEORY.md`
* `docs/theory/GLOSSARY.md`
* `docs/theory/BIOLOGICAL_FRAMING.md`
* `docs/theory/PRIOR_ART_MAP.md`
* `docs/threads/THREAD_INDEX.md`
* `docs/threads/THREAD_DIGEST_TEMPLATE.md`
* `docs/repo_audit/ARTIFACT_INDEX.csv`
* `docs/repo_audit/MISSING_ARTIFACTS.md`
* `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`
* `docs/repo_audit/NAMING_AND_STRUCTURE_AUDIT.md`
* `docs/repo_audit/REVIEWER_ATTACK_SURFACES.md`
* `docs/synthesis/PROJECT_STATUS.md`
* `docs/synthesis/PUBLICATION_READINESS.md`
* `docs/synthesis/NEXT_EXPERIMENTS.md`

---

## 8. Decisions made

### Experimental decisions

1. **Experiment 13 was designed as a breaking-point experiment**, not just another scaling run.
2. **Memory pressure was split into global and local budgets**, which later proved important because local budget pressure damaged composition much more severely.
3. **Primitive holdout was added** to distinguish composition over stored primitives from inference of unseen primitive transitions.
4. **A continuous/noisy input bridge was added** to begin moving beyond purely symbolic inputs.
5. **Context corruption was added**, including adversarial mixture, to address Experiment 12’s flat context-noise sweeps.

---

### Interpretation decisions

1. **The core model should be framed as structural plasticity + world context + recurrence.**
2. **Consolidation should not be framed as essential in the easy regime.**
3. **Consolidation should instead be framed as a stability-plasticity bias under finite capacity.**
4. **Held-out composition should not be overclaimed as broad abstract generalization.**
5. **The continuous-input bridge should be described as preliminary, not as end-to-end perception.**
6. **No-context-binding results require caution because one variant may be weak-binding/oracle-clean rather than a pure ablation.**

---

### Manuscript framing decisions

1. Avoid claiming:

   * first context-sensitive multi-world memory;
   * first non-destructive storage of incompatible worlds;
   * solved continual learning;
   * a general hippocampal theory;
   * broad abstract rule generalization;
   * end-to-end perceptual learning.

2. Prefer the safer central claim:

   > Context-indexed structural plasticity enables non-destructive rebinding of incompatible local route memories, while recurrent dynamics are required to execute those memories compositionally.

3. Treat the work as:

   * a synthetic benchmark;
   * a mechanistically interpretable route-memory model;
   * a biologically inspired but not biologically complete computational system.

---

### Follow-up experiment decisions

1. Proceed with **Experiment 13.1** as a publication-hardening audit.
2. Defer **Experiment 14** until after 13.1 and baseline work.
3. Add external baselines before considering the paper journal-ready.
4. Consider latent world inference as the next true novelty push after consolidation.

---

### Repository/process decisions

1. Create a canonical documentation scaffold under `docs/`.

2. Use the pattern:

   > Claim → Evidence → Caveat → Source path

3. Pull long ChatGPT thread analyses into repo as forensic digests.

4. Create per-experiment summaries.

5. Build `CLAIMS_AND_EVIDENCE.md` as the central manuscript spine.

6. Use Codex/local agents conservatively for indexing, summarization, and repo organization.

7. Avoid letting many agents produce divergent scientific narratives.

---

## 9. Open questions created by this thread

1. **How should Experiment 13.1 be implemented exactly?**

   * Need final run configuration, seeds, budget levels, context corruption types, and output schema.

2. **Which external baselines should be implemented first?**

   * Minimum candidates: shared transition table, context-gated table/mask, replay, hypernetwork/superposition, HAT/PackNet-inspired isolation.

3. **How should the benchmark be formalized?**

   * Needs precise definition of worlds, routes, modes, transition systems, incompatible mappings, train/test splits, and capacity budgets.

4. **Can consolidation be made a publishable stability-plasticity curve?**

   * Needs dose-response under finite sequential capacity.

5. **Can context be inferred rather than provided?**

   * Future latent world inference direction.

6. **Can the model handle non-symbolic inputs in a meaningful applied setting?**

   * Continuous bridge is preliminary; visual-state route memory remains proposed.

7. **How should no-context-binding be defined cleanly?**

   * Current variant naming/implementation may be misleading.

8. **How much statistical reporting is required before manuscript submission?**

   * Need confidence intervals, seed-level plots, possibly effect sizes.

9. **What should be main text versus supplement?**

   * Likely main: mechanism, capacity, recurrence dissociation, local budget failure, consolidation under pressure.
   * Likely supplement: some context-noise sweeps, continuous bridge if preliminary, extended ablations.

10. **How should biological language be bounded?**

    * Need biological framing doc distinguishing inspiration from demonstrated neural theory.

---

## 10. Relationship to the first manuscript

### Central claim

This thread strongly contributes to the central claim that a context-indexed structural-plastic recurrent substrate can store incompatible route memories and execute them compositionally.

Main supporting evidence:

* Experiment 12 capacity scaling and ablations;
* Experiment 13 breaking-point analysis;
* novelty assessment narrowing the claim.

---

### Supporting claims

This thread contributes to several supporting claims:

1. **Structural plasticity is required for storage.**

   * Supported by no-structural-plasticity near-chance performance.

2. **World/context indexing prevents destructive interference.**

   * Supported by no-world-context collapse as worlds accumulate.

3. **Recurrence is required for composition.**

   * Supported by no-recurrence route-table/composition dissociation.

4. **Finite capacity exposes interpretable failure laws.**

   * Supported by Experiment 13 global/local budget pressure analysis.

5. **Consolidation biases stability versus plasticity.**

   * Suggested by Experiment 13 retention heatmaps, but needs 13.1 hardening.

6. **The model composes stored primitives but does not infer unseen primitives.**

   * Suggested by Experiment 13 primitive holdout, but needs metric cleanup.

7. **The model can operate downstream of noisy continuous decoding.**

   * Preliminary bridge, likely supplementary or future-work material.

---

### Limitations

This thread explicitly identified manuscript limitations:

* external baselines missing;
* no-context-binding ablation needs cleanup;
* holdout metrics need cleanup;
* context corruption needs stochastic/graded versions;
* biological framing must be bounded;
* applied/non-symbolic evidence is preliminary;
* repository evidence was not yet consolidated.

---

### Future work

Future-work directions identified:

* Experiment 13.1 publication hardening;
* external baseline suite;
* latent world inference;
* visual/perceptual route-memory bridge;
* repo consolidation and manuscript evidence mapping.

---

### Supplementary material

Likely supplementary candidates:

* full Experiment 12 context-bleed/dropout plots;
* extended capacity plots;
* validation reports;
* Experiment 13 continuous bridge if not used as a main result;
* detailed failure-boundary tables;
* per-seed summaries;
* ablation catalogs.

---

## 11. Claims-and-evidence rows contributed by this thread

| Claim                                                                                                                                  | Evidence                                                                                                                                                                       | Caveat                                                                                          | Experiment(s)         | Artifact(s)                                                                                | Manuscript status    |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------ | -------------------- |
| Context-indexed structural plasticity enables non-destructive storage of incompatible route memories in the tested symbolic benchmark. | Experiment 12 full model and world-gated variants retain `1.0` composition and route-table accuracy across world counts up to 32.                                              | Controlled symbolic benchmark; external baselines missing.                                      | 12                    | `exp12_report.md`, `capacity_final_summary.csv`, `exp12_capacity_composition_accuracy.png` | Strong               |
| Structural plasticity is required for reliable route-memory storage.                                                                   | Experiment 12 no-structural-plasticity remains near chance across world counts.                                                                                                | Necessity shown within this implementation and benchmark.                                       | 12, 13                | `exp12_report.md`, `capacity_final_summary.csv`; `analysis13.zip`                          | Strong               |
| World/context indexing prevents destructive interference across incompatible worlds.                                                   | Experiment 12 no-world-context drops from about `0.519` at 2 worlds to about `0.071` at 32 worlds.                                                                             | Needs external baseline comparison to known context-gating methods.                             | 12, 13                | `exp12_report.md`, `capacity_final_summary.csv`; `analysis13.zip`                          | Strong               |
| Recurrence converts one-step route memory into multi-step execution.                                                                   | Experiment 12 no-recurrence route-table accuracy stays `1.0` while composition remains around `0.05–0.06`; Experiment 13 replicates under exact capacity.                      | Recurrence itself is not novel; novelty is the benchmarked dissociation.                        | 12, 13                | `exp12_report.md`, `exp12_route_table_composition_gap.png`; `analysis13.zip`               | Strong               |
| Consolidation is not essential for accuracy in the easy/full-capacity regime.                                                          | Experiment 12 no-consolidation and strong-consolidation variants both achieve perfect accuracy across tested world counts.                                                     | Does not rule out consolidation importance under pressure.                                      | 12                    | `exp12_report.md`, `consolidation_pressure_summary.csv`                                    | Strong               |
| Consolidation behaves as a stability-plasticity bias under finite capacity.                                                            | Experiment 13 retention analysis suggested consolidated model preserves older worlds while no-consolidation preserves newer worlds.                                            | Needs dose-response and seed-level hardening.                                                   | 13, proposed 13.1     | `analysis13.zip`, retention heatmaps                                                       | Promising            |
| Global capacity pressure creates a world-level breaking curve.                                                                         | Experiment 13 global budget full-model composition rises from about `0.27` at 0.25 budget to `1.0` at exact/surplus capacity.                                                  | Route-length independence suggests world-level retention/drop behavior, not random edge damage. | 13                    | `analysis13.zip`, `exp13_budget_breaking_curve_full_vs_consolidation.png`                  | Promising            |
| Local capacity pressure is especially damaging to long-route composition.                                                              | Experiment 13 local budget `0.75` retained route-table accuracy around `0.7575` but route-length-12 composition only around `0.1379`.                                          | Exact CSV path needs repo import verification.                                                  | 13                    | `analysis13.zip`                                                                           | Strong               |
| The model composes seen primitives but does not infer unseen primitive transitions.                                                    | Experiment 13 true holdout showed high seen-primitive composition but near-chance unseen primitive accuracy.                                                                   | Metric cleanup required; route-table accuracy must be split into seen/unseen/all.               | 13, proposed 13.1     | `analysis13.zip`                                                                           | Needs metric cleanup |
| Context corruption can collapse performance when wrong-world evidence dominates.                                                       | Experiment 13 adversarial context mixture caused failure after the wrong context exceeded the correct context.                                                                 | Hard deterministic threshold; needs stochastic corruption for graded robustness.                | 13, proposed 13.1     | `analysis13.zip`                                                                           | Promising            |
| Continuous/noisy input decoding can feed the route-memory mechanism.                                                                   | Experiment 13 continuous bridge degraded smoothly as decoding noise increased.                                                                                                 | Preliminary; not end-to-end perception.                                                         | 13                    | `analysis13.zip`                                                                           | Preliminary          |
| The paper’s novelty is combinatorial, not atomic.                                                                                      | Novelty assessment identified overlap with context gating, task masks, hypernetworks, superposition, plastic networks, and cognitive-map models; recommended narrower framing. | Requires external baselines and careful prior-art positioning.                                  | Manuscript-level      | `Pasted text.txt`                                                                          | Strong               |
| External baselines are required before journal-readiness.                                                                              | Novelty assessment listed external baselines as a P0 publishability gap.                                                                                                       | Baselines not implemented in this thread.                                                       | Future baseline suite | `Pasted text.txt`                                                                          | Needs baseline       |
| Repository consolidation is required before further manuscript synthesis.                                                              | User stated analyses are spread across threads; thread produced a documentation scaffold and Codex prompts.                                                                    | Must still be executed locally.                                                                 | Process/workflow      | Codex prompts in conversation                                                              | Strong               |

---

## 12. Recommended follow-up actions

1. **Save this digest into the repo**

   * Suggested path:

     * `docs/threads/<date>_exp12_exp13_novelty_and_repo_consolidation_digest.md`

2. **Run the repo-consolidation Codex prompt created in this thread**

   * Create the `docs/` scaffold.
   * Index all experiment artifacts.
   * Create per-experiment summary stubs.
   * Create `CLAIMS_AND_EVIDENCE.md`.

3. **Import Experiment 12 artifacts into the repo documentation**

   * Link:

     * `exp12_report.md`;
     * `capacity_final_summary.csv`;
     * `continual_retention_summary.csv`;
     * `heldout_generalization_summary.csv`;
     * context-noise summaries;
     * consolidation summaries;
     * all Experiment 12 plots.

4. **Import Experiment 13 artifacts from `analysis13.zip`**

   * Extract exact CSV names.
   * Extract exact plot names.
   * Add precise source paths to the Experiment 13 summary.
   * Replace conversation-only metrics with source-backed metrics.

5. **Create `docs/experiments/exp12_summary.md`**

   * Include:

     * purpose;
     * variants;
     * metrics;
     * capacity results;
     * recurrence dissociation;
     * no-world-context collapse;
     * no-structural-plasticity near-chance;
     * consolidation caveat;
     * context-noise caveat.

6. **Create `docs/experiments/exp13_summary.md`**

   * Include:

     * global budget result;
     * local budget result;
     * recurrence result;
     * no-world-context result;
     * consolidation retention asymmetry;
     * primitive holdout boundary;
     * context corruption threshold;
     * continuous bridge;
     * known metric issues.

7. **Design and implement Experiment 13.1**

   * Fix holdout metrics.
   * Rename or replace no-context-binding.
   * Add stochastic context corruption.
   * Add consolidation dose-response.
   * Add capacity-law summaries.
   * Add seed-level confidence reporting.

8. **Create `docs/manuscript/BASELINE_REQUIREMENTS.md`**

   * Include minimum external baseline families:

     * shared transition table;
     * context-gated table/mask;
     * replay;
     * task-mask/parameter-isolation;
     * hypernetwork/superposition;
     * optional CSCG-inspired clone-state baseline.

9. **Create `docs/manuscript/NOVELTY_POSITIONING.md`**

   * Use the novelty assessment.
   * Explicitly distinguish the paper from:

     * XdG;
     * HAT;
     * PackNet;
     * PathNet;
     * hypernetworks;
     * model superposition;
     * TEM;
     * CSCG;
     * sequence-centric hippocampal models;
     * neuromodulated plasticity.

10. **Create `docs/manuscript/LIMITATIONS_AND_THREATS.md`**

    * Include:

      * symbolic benchmark limitation;
      * external baselines missing;
      * biological overhang;
      * context-label/oracle-context concern;
      * primitive inference limitation;
      * continuous bridge limitation.

11. **Delay Experiment 14 until after 13.1 and baseline planning**

    * Latent world inference and perceptual route memory are promising, but should not interrupt publication hardening.

12. **Use the evidence discipline everywhere**

    * Every repo claim should follow:

      * Claim;
      * Evidence;
      * Caveat;
      * Source path.
