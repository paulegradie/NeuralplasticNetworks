# Thread Digest: Persistent Plastic Graph Networks and Successor Traversal Experiments

## 1. Thread scope

This thread developed and tested a biologically inspired learning-machine idea: replacing or augmenting dense static parameter matrices with a **persistent sparse plastic graph** of adaptive neuron-like units and synapse-like edges.

The thread moved through four major activities:

1. **Theory formation**
   We discussed why biological neurons are not static weighted functions, why long-context prompting is an imperfect substitute for persistent adaptation, and why sparse recurrent structural plasticity may be a better computational abstraction.

2. **Prototype implementation**
   A Python experimental framework was generated for a sparse plastic graph model trained on MNIST, with SQLite/SQLAlchemy persistence and analysis scripts.

3. **Experimental analysis**
   MNIST results, recurrent MNIST ablations, and Experiment 4 successor traversal results were analyzed.

4. **Roadmap consolidation**
   A structured handoff document and future experiment plan were created for manuscript preparation and continuation in a new thread.

---

## 2. Experiments discussed

| Experiment                                             | Status in this thread    | Short description                                                                                                                                                          |
| ------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Experiment 1/2, initial sparse plastic MNIST prototype | Implemented and analyzed | Sparse input-to-hidden plastic graph with local plasticity, traces, thresholds, reward/confidence modulation, and online MNIST learning.                                   |
| Experiment 3, recurrent MNIST suite                    | Implemented and analyzed | Added hidden-to-hidden recurrent edges, recurrent drive metrics, and ablations including no recurrence, frozen input projection, no homeostasis, and no reward modulation. |
| Experiment 4, successor traversal                      | Implemented and analyzed | Shifted from MNIST to symbolic successor learning. Trained local transitions such as `0 -> 1`, then tested compositional addition by repeated recurrent traversal.         |
| Experiment 5, contextual successor world               | Proposed only            | Planned next experiment with multiple context-dependent transition systems, noisy feedback, delayed reward, and rule reversal.                                             |
| Experiment 6, multimodal number grounding              | Proposed only            | Planned structured moonshot using MNIST images, digit tokens, number words, dot patterns, and arithmetic operators.                                                        |
| Experiment 7, gridworld / embodied reward environment  | Proposed only            | Planned future environment to test delayed reward, online learning, planning, reward relocation, and adaptation.                                                           |

---

## 3. Experimental designs created or modified here

### Experiment 1/2: Initial sparse plastic MNIST prototype

* **Experiment number:** Experiment 1/2, though initially created as an unnumbered prototype.
* **Purpose:** Test whether a sparse plastic graph-like model could learn MNIST through online local updates rather than standard backprop.
* **Hypothesis:** A sparse, threshold-stabilized, locally plastic model can learn a real classification task and show stable improvement.
* **Model variants:** Initial package primarily focused on a single sparse plastic graph model; later comparison variants were added in Experiment 3.
* **Metrics:**

  * `train/window_accuracy`
  * `test/accuracy`
  * `train/average_confidence`
  * `test/average_confidence`
  * checkpoint summaries of hidden thresholds, traces, input weights, output weights
* **Expected outcomes:**

  * Rising train and test accuracy.
  * Confidence rising with accuracy rather than pathological overconfidence.
  * Stable checkpoint statistics.
* **Implementation notes:**

  * Python package generated as `plastic_graph_mnist.zip`.
  * Later updated with `analyze_results.py` in `plastic_graph_mnist_with_analysis.zip`.
  * Used `torchvision` MNIST loading.
  * Used SQLite/SQLAlchemy persistence.
  * Used sparse input-to-hidden connectivity and top-k active hidden units.
* **Known risks:**

  * MNIST may be too easy.
  * Model may behave like a sparse random-feature classifier rather than a fundamentally new architecture.
  * Without proper baselines, performance cannot be interpreted as superior to conventional ML.

---

### Experiment 3: Recurrent MNIST suite

* **Experiment number:** Experiment 3 in the consolidated handoff.
* **Purpose:** Add recurrent hidden-to-hidden graph traversal and ablation controls to determine whether recurrence, structural dynamics, homeostasis, and reward modulation matter.
* **Hypothesis:** If the recurrent plastic graph is doing useful work, the full recurrent model should outperform no-recurrence controls or show meaningful recurrent traversal metrics.
* **Model variants:**

  * `full_recurrent_plastic_graph`
  * `no_recurrence_sparse_plastic_readout`
  * `frozen_input_projection`
  * `no_homeostasis`
  * `no_reward_modulation`
* **Metrics:**

  * Best test accuracy
  * Latest test accuracy
  * Train window accuracy
  * Generalization gap
  * Average unique active units
  * Average recurrent drive
* **Expected outcomes:**

  * Full recurrent model should beat or meaningfully differ from no recurrence.
  * No-homeostasis should reveal whether activity regulation is load-bearing.
  * Frozen input projection should test whether input-side plasticity matters.
  * No-reward-modulation should test whether reward modulation adds value.
* **Implementation notes:**

  * Generated as `plastic_graph_mnist_recurrent_suite.zip`.
  * Added suite runner and suite analyzer.
  * README diagrams were requested and included in package generation claim.
* **Known risks:**

  * MNIST does not strongly require multi-step traversal.
  * Recurrent edges may add noise rather than useful computation.
  * Reward modulation may not matter when supervised labels already provide a clean signal.
  * Duplicated rows appeared in the suite chart/report for some variants, requiring metric/report cleanup.

---

### Experiment 4: Successor traversal

* **Experiment number:** Experiment 4.
* **Purpose:** Move away from MNIST classification into a task that actually requires recurrent graph traversal.
* **Hypothesis:** A structurally plastic recurrent graph can learn local successor transitions and compose them into multi-step addition-like behavior, while no-recurrence and no-structural-plasticity controls should fail.
* **Model variants:**

  * `exp4_full_traversal`
  * `exp4_no_recurrence`
  * `exp4_no_structural_plasticity`
  * `exp4_no_homeostasis`
  * `exp4_no_reward_gate`
* **Metrics:**

  * `best_addition_accuracy`
  * `best_transition_accuracy`
  * `addition/accuracy`
  * `addition/accuracy_steps_2`
  * `addition/accuracy_steps_3`
  * `addition/accuracy_steps_4`
  * `addition/accuracy_steps_5`
  * `addition/average_confidence`
  * `addition/average_recurrent_drive`
  * `addition/average_unique_active`
  * `transition/accuracy`
  * `transition/average_recurrent_drive`
  * `transition/average_unique_active`
* **Expected outcomes:**

  * Full traversal should outperform no recurrence.
  * Full traversal should outperform no structural plasticity.
  * Recurrent drive should be nonzero and functionally meaningful in successful variants.
  * Unique active units should exceed the initial active set during traversal.
* **Implementation notes:**

  * Generated as `plastic_graph_mnist_experiment4_successor.zip`.
  * Training focused on local successor transitions.
  * Testing focused on compositional addition by repeated traversal.
* **Known risks:**

  * Task may be too clean or too easy.
  * Perfect accuracy across several variants makes reward gating and homeostasis non-discriminative.
  * It may be learning a simple explicit chain rather than more general reasoning.
  * Further stress tests are required.

---

### Experiment 5: Contextual successor world

* **Experiment number:** Experiment 5.
* **Status:** Proposed only.
* **Purpose:** Test whether the recurrent plastic graph can choose among multiple transition systems based on context.
* **Hypothesis:** Context-dependent transitions should require routing, inhibition, and context-sensitive recurrent traversal. The full model should outperform no recurrence, no structural plasticity, and no context routing.
* **Proposed modes:**

  * Mode A: `+1` successor, e.g. `0 -> 1 -> 2 -> 3`
  * Mode B: `+2` successor, e.g. `0 -> 2 -> 4 -> 6`
  * Mode C: `-1` predecessor, e.g. `5 -> 4 -> 3 -> 2`
  * Mode D: special or alternate route
* **Model variants proposed:**

  * Full model
  * No recurrence
  * No structural plasticity
  * No reward gate
  * No homeostasis
  * No inhibition / no competition
  * No context routing
* **Metrics proposed:**

  * Accuracy by mode
  * Accuracy by path length
  * Wrong-route activation
  * Path entropy
  * Context confusion matrix
  * Recurrent drive
  * Unique active units
  * Transition accuracy
  * Composition accuracy
* **Expected outcomes:**

  * Full model should beat no recurrence.
  * Full model should beat no structural plasticity.
  * Full model should beat no context routing.
  * Reward gating may still not matter unless feedback is noisy or delayed.
* **Implementation notes proposed:**

  * Suggested files:

    * `EXPERIMENT_5_CONTEXTUAL_SUCCESSOR.md`
    * `run_exp5_contextual_successor.py`
    * `run_exp5_suite.py`
    * `analyze_exp5_suite.py`
    * `plastic_graph_mnist/contextual_successor_task.py`
    * `plastic_graph_mnist/contextual_successor_graph.py`
    * `plastic_graph_mnist/contextual_successor_trainer.py`
    * `plastic_graph_mnist/inhibition.py`
    * `plastic_graph_mnist/context_router.py`
* **Known risks:**

  * Could still be solved through simple lookup if not designed carefully.
  * Context leakage could make the task easier than intended.
  * Reward gating needs noisy or delayed feedback to become meaningful.

---

### Experiment 5B: Noisy and delayed feedback

* **Experiment number:** Experiment 5B, proposed extension.
* **Purpose:** Force reward modulation and eligibility traces to matter.
* **Hypothesis:** Reward-gated models should outperform no-reward-gate models when feedback is noisy, misleading, delayed, or ambiguous.
* **Model variants:** Same as Experiment 5, with emphasis on `full model` versus `no_reward_gate`.
* **Metrics:**

  * Performance under noisy feedback
  * Confidence calibration
  * Recovery from misleading feedback
  * Wrong-edge reinforcement rate
  * Path stability
* **Expected outcomes:**

  * Full reward-gated model should outperform no-reward-gate under noise/delay.
* **Implementation notes:**

  * Proposed noise level: 90% correct feedback, 10% misleading feedback.
  * Proposed delayed reward: no reward after intermediate steps; reward only after final answer.
* **Known risks:**

  * Poor reward design may still fail.
  * Need to distinguish reward-gating failure from task-design failure.

---

### Experiment 5C: Rule reversal / adaptation

* **Experiment number:** Experiment 5C, proposed extension.
* **Purpose:** Test plasticity without catastrophic destruction.
* **Hypothesis:** The model should adapt to changed transition rules while either decaying old paths or preserving them if context-tagged.
* **Model variants:** Same as Experiment 5, potentially with context-tagged and non-context-tagged versions.
* **Metrics:**

  * Adaptation speed
  * Old-path decay
  * New-path formation
  * Catastrophic interference
  * Ability to preserve old mode if context-tagged
* **Expected outcomes:**

  * Full model should adapt more gracefully than controls.
* **Implementation notes:**

  * Phase 1: learn `+1` successor.
  * Phase 2: switch to `+2`, reversed, or alternate successor.
* **Known risks:**

  * Without careful context separation, reversal may overwrite rather than coexist.
  * If task is too simple, adaptation may appear successful without proving robust continual learning.

---

### Experiment 6: Multimodal number grounding

* **Experiment number:** Experiment 6.
* **Status:** Proposed only.
* **Purpose:** Test whether different modalities can bind to shared number assemblies and then use recurrent traversal for operations.
* **Hypothesis:** The model can map MNIST images, digit tokens, number words, and dot patterns onto shared number representations, then use recurrent traversal for arithmetic operations.
* **Inputs proposed:**

  * MNIST digit image
  * Arabic digit token, e.g. `"3"`
  * Number word, e.g. `"three"`
  * Dot pattern, e.g. `•••`
  * Operator token, e.g. `+`, `-`, `next`, `previous`
* **Model variants:** Not fully specified, but expected to include full model and ablations for recurrence, structural plasticity, and modality binding.
* **Metrics:**

  * Cross-modal accuracy
  * Held-out modality-combination accuracy
  * Operation accuracy
  * Shared assembly activation
  * Modality confusion
* **Expected outcomes:**

  * Inputs representing the same number should converge onto shared assemblies.
  * Recurrent traversal should perform operations regardless of input modality.
* **Implementation notes:**

  * Train on some modality pairings, test on held-out pairings.
  * Example train: image + token, word + dot.
  * Example test: dot + image, word + image.
* **Known risks:**

  * Random dataset mixing was rejected as too chaotic.
  * The task should be structured around shared latent number concepts rather than arbitrary multimodal data.

---

### Experiment 7: Gridworld / embodied reward environment

* **Experiment number:** Experiment 7.
* **Status:** Proposed only.
* **Purpose:** Test online learning, delayed reward, planning, state, reward relocation, and adaptation.
* **Hypothesis:** A recurrent plastic graph with reward modulation should learn and adapt in an environment with delayed outcomes.
* **Model variants:** Not fully specified.
* **Metrics proposed:**

  * Episodes to solve
  * Adaptation after reward relocation
  * Path reuse
  * Exploration/exploitation
  * Catastrophic forgetting
  * Recurrent planning traces
* **Expected outcomes:**

  * Reward modulation should become more meaningful in embodied or sequential environments.
* **Implementation notes:**

  * MiniGrid-like or symbolic maze environments were suggested.
* **Known risks:**

  * May be too large a jump before Experiments 5 and 6 clarify reward gating and context routing.

---

## 4. Results analyzed here

### Result: Initial sparse plastic MNIST prototype

Claim:
The sparse plastic graph prototype learned MNIST to a nontrivial level.

Evidence:
The run reached best test accuracy of **0.9225** at step `27500`, latest test accuracy of **0.9190**, latest train/window accuracy of **0.9820**, latest test confidence of **0.8309**, and latest train confidence of **0.8979**. 

Caveat:
This does not prove the architecture is fundamentally different from standard neural networks. The model may be operating like a sparse random-feature classifier with online plastic readout.

Source artifact or conversation reference:
`analysis_report.md`, `metrics.csv`, `test_accuracy.png`, `train_window_accuracy.png`, `test_average_confidence.png`, `train_average_confidence.png`.

---

### Result: Initial checkpoint inspection

Claim:
The initial model was small and sparse enough that its performance was meaningful but not necessarily architecturally radical.

Evidence:
The checkpoint included `4096` hidden units, `input_indices` and `input_weights` shaped `(4096, 64)`, and `output_weights` shaped `(4096, 10)`. This implies roughly `262,144` sparse input weights and `40,960` output weights. 

Caveat:
The scale and structure are consistent with a sparse feature model; deeper recurrent or structural reasoning was not yet demonstrated.

Source artifact or conversation reference:
`latest_checkpoint_summary.json`.

---

### Result: Recurrent MNIST suite

Claim:
The recurrent MNIST model did not clearly outperform simpler controls.

Evidence:
The analysis reported best test accuracy of **0.9285** for `no_reward_modulation`, **0.9255** for `no_recurrence_sparse_plastic_readout`, **0.9230** for `full_recurrent_plastic_graph`, and **0.9225** for `frozen_input_projection`. 

Caveat:
MNIST may not require recurrent traversal. The failure of recurrence to help on MNIST does not falsify the broader recurrent-graph thesis.

Source artifact or conversation reference:
`suite_report.md`, `suite_comparison.csv`, `suite_best_accuracy.png`.

---

### Result: Homeostasis mattered in recurrent MNIST

Claim:
Homeostatic regulation was load-bearing for recurrent stability in the MNIST recurrent suite.

Evidence:
The `no_homeostasis` variant had best test accuracy **0.8875** but latest test accuracy around **0.7555–0.7595**, with recurrent drive around **153–154**, compared with full recurrent drive around **2.5558**. 

Caveat:
This result applied to the recurrent MNIST setting; homeostasis was not proven necessary in Experiment 4’s cleaner symbolic successor task.

Source artifact or conversation reference:
`suite_report.md`, `suite_comparison.csv`, `suite_best_accuracy.png`.

---

### Result: Experiment 4 successor traversal

Claim:
Experiment 4 provided the strongest support so far for recurrent structural plasticity.

Evidence:
`exp4_full_traversal` reached **1.0** transition accuracy and **1.0** addition accuracy. `exp4_no_recurrence` reached **0.0** transition and addition accuracy. `exp4_no_structural_plasticity` reached only about **0.0417** transition accuracy and **0.0349** addition accuracy. 

Caveat:
The task may be too clean or too easy. Perfect accuracy across full traversal, no-reward-gate, and no-homeostasis variants means reward gating and homeostasis were not tested discriminatively.

Source artifact or conversation reference:
`exp4_report.md`, `exp4_comparison.csv`, `exp4_best_addition_accuracy.png`.

---

### Result: Experiment 4 recurrent drive and active units

Claim:
Successful Experiment 4 variants showed strong recurrent traversal dynamics.

Evidence:
The successful variants had addition recurrent drive around **811–826** and addition average unique active units around **407**, while `exp4_no_recurrence` had recurrent drive **0** and average unique active units **96**. 

Caveat:
High recurrent drive alone is not sufficient: `exp4_no_structural_plasticity` had nonzero recurrent drive around **128.721** but still failed. Structural shaping was required.

Source artifact or conversation reference:
`exp4_recurrent_drive.png`, `exp4_unique_active.png`, `exp4_report.md`.

---

## 5. Key scientific conclusions supported by this thread

### Claim 1: Sparse plastic online learning can learn MNIST, but that alone does not prove the deeper thesis.

Evidence:
Initial MNIST prototype reached best test accuracy **0.9225** and latest test accuracy **0.9190**. 

Caveat:
The mechanism may be similar to sparse random features plus online readout.

---

### Claim 2: MNIST is not a sufficient task to demonstrate recurrent graph traversal.

Evidence:
In the recurrent MNIST suite, `no_recurrence_sparse_plastic_readout` slightly outperformed `full_recurrent_plastic_graph`: **0.9255** versus **0.9230** best test accuracy. 

Caveat:
This does not show recurrence is useless; it shows MNIST does not strongly pressure recurrence.

---

### Claim 3: Homeostasis can be necessary for recurrent stability.

Evidence:
In recurrent MNIST, removing homeostasis led to large recurrent drive around **153–154** and a late test accuracy collapse to around **0.7555–0.7595**. 

Caveat:
Experiment 4 did not require homeostasis to solve the clean successor traversal task.

---

### Claim 4: Recurrent structural plasticity became load-bearing in Experiment 4.

Evidence:
`exp4_full_traversal` achieved **1.0** addition accuracy, while `exp4_no_recurrence` achieved **0.0** and `exp4_no_structural_plasticity` achieved about **0.0349**. 

Caveat:
The task may have exposed an easy chain-building solution.

---

### Claim 5: Structural plasticity mattered more than recurrent activity alone in Experiment 4.

Evidence:
`exp4_no_structural_plasticity` had nonzero recurrent drive but failed on transition and addition accuracy. 

Caveat:
The implementation details of structural plasticity should be inspected to ensure the task was not too directly encoded.

---

### Claim 6: Reward gating has not yet been shown to be load-bearing.

Evidence:
In Experiment 4, `exp4_no_reward_gate` achieved **1.0** transition and addition accuracy, matching the full traversal model.  In recurrent MNIST, `no_reward_modulation` was the best-performing variant. 

Caveat:
Current tasks used clean feedback. Reward gating may require noisy, delayed, ambiguous, or conflicting feedback to matter.

---

## 6. Important flaws, mistakes, or implementation concerns identified

1. **MNIST is too weak as a recurrent traversal test**
   It allows sparse feature/readout models to perform well without needing path composition.

2. **Initial prototype may be a sparse random-feature classifier**
   The checkpoint structure and performance do not prove deep biological-style computation.

3. **Recurrent MNIST results weakened the recurrence claim**
   No-recurrence slightly outperformed full recurrence on MNIST.

4. **Reward modulation was not validated**
   In both MNIST recurrent suite and Experiment 4, reward removal did not hurt and sometimes improved performance.

5. **Experiment 4 may be too easy**
   Perfect accuracy in multiple variants suggests it may not discriminate reward gating or homeostasis.

6. **No-homeostasis result differs by task**
   No-homeostasis collapsed in recurrent MNIST but succeeded perfectly in Experiment 4. This indicates task dependence and requires careful framing.

7. **Suite report/plot contained duplicated variants**
   The recurrent MNIST suite report listed duplicated rows for variants such as `no_reward_modulation`, `no_recurrence_sparse_plastic_readout`, `full_recurrent_plastic_graph`, and others. This requires metric/report cleanup before manuscript use.

8. **No standard baselines yet**
   Logistic regression, small MLP, small CNN, reservoir computing, echo state networks, and random-feature baselines were discussed as necessary but not yet completed in this thread.

9. **No formal statistical replication yet**
   Runs appear to be single or duplicated-run comparisons, not replicated across seeds with confidence intervals.

10. **Interpretability metrics are not yet sufficient**
    The thread proposed but did not complete path visualizations, edge utilization histograms, path entropy, wrong-route activation, and learned-chain inspection.

11. **Structural plasticity needs code-level audit**
    Because Experiment 4 shows perfect performance, implementation should be reviewed to ensure no direct leakage or overly deterministic task shortcut.

---

## 7. Figures or artifacts referenced

### Generated packages

* `plastic_graph_mnist.zip`
* `plastic_graph_mnist_with_analysis.zip`
* `plastic_graph_mnist_recurrent_suite.zip`
* `plastic_graph_mnist_experiment4_successor.zip`
* `biological_neural_nets_experimental_handoff.md`

### Initial MNIST analysis artifacts

* `metrics.csv`
* `analysis_report.md`
* `latest_checkpoint_summary.json`
* `train_window_accuracy.png`
* `test_average_confidence.png`
* `train_average_confidence.png`
* `test_accuracy.png`

### Recurrent MNIST suite artifacts

* `suite_best_accuracy.png`
* `suite_comparison.csv`
* `suite_report.md`

### Experiment 4 artifacts

* `exp4_best_addition_accuracy.png`
* `exp4_comparison.csv`
* `exp4_recurrent_drive.png`
* `exp4_report.md`
* `exp4_unique_active.png`

---

## 8. Decisions made

1. **Adopt persistent plastic graph framing**
   The central architecture was framed as sparse adaptive graph traversal rather than dense static matrices.

2. **Do not literally simulate biology**
   The project will abstract biological principles rather than reproduce biochemical detail.

3. **Use array-backed runtime representation**
   Neurons and synapses may be conceptual objects, but should be represented as compact arrays in the hot path.

4. **Use SQLite/SQLAlchemy persistence**
   Experimental runs, metrics, and checkpoints should be persisted.

5. **Use MNIST only as an initial proof-of-life**
   MNIST is not sufficient for the core recurrent traversal claim.

6. **Move from MNIST to successor traversal**
   Experiment 4 was created because MNIST did not pressure recurrence.

7. **Treat Experiment 4 as first strong recurrent-structural evidence**
   The no-recurrence and no-structural-plasticity failures made it more relevant to the core thesis.

8. **Do not overclaim Experiment 4**
   Perfect accuracy across several variants means the task is likely too clean.

9. **Next experiment should be contextual successor world**
   Experiment 5 should introduce multiple transition systems selected by context.

10. **Reward gating must be tested with noisy/delayed feedback**
    Clean supervised feedback is insufficient to validate reward gating.

11. **Multimodal moonshot should be structured, not random dataset mixing**
    Proposed Experiment 6 should use shared number concepts across images, tokens, words, and dot patterns.

12. **Gridworld should come later**
    Embodied reward environments were deferred until after context routing and reward-gating mechanisms are better understood.

13. **Manuscript framing should be cautious**
    Current evidence supports sparse plastic learning and recurrent structural composition in a synthetic task, not general biological intelligence.

---

## 9. Open questions created by this thread

1. Does reward gating help under noisy, delayed, or ambiguous feedback?
2. Can the graph learn context-sensitive transitions without route collapse?
3. Can homeostasis and inhibition prevent route explosion in multi-path symbolic tasks?
4. Can the model adapt after rule reversal without catastrophic overwriting?
5. Can old routes decay while reusable reasoning pathways remain stable?
6. Can learned pathways be visualized and interpreted directly?
7. Does structural plasticity produce reusable abstractions or only task-specific chains?
8. Would a no-structural-plasticity baseline fail under all reasonable hyperparameters?
9. Are Experiment 4 results partly caused by implementation leakage or overly direct task encoding?
10. How does the model compare against standard baselines such as logistic regression, MLPs, CNNs, reservoir computing, and graph neural networks?
11. How robust are results across random seeds?
12. Can multimodal inputs converge onto shared assemblies?
13. Can the architecture handle larger, noisier, naturalistic datasets?
14. What is the correct mathematical formulation of the reward/modulatory system?
15. Should future experiments introduce explicit inhibition, local competition, or energy budgets?

---

## 10. Relationship to the first manuscript

### Central claim

This thread contributes to the central manuscript claim that **static dense parameter fields are not the only viable abstraction for learning systems**, and that sparse recurrent structural plasticity may support compositional behavior.

Current support:

* MNIST shows sparse plastic online learning can work.
* Experiment 4 shows recurrence and structural plasticity can be necessary for a compositional traversal task.

### Supporting claim

The thread supports a narrower claim:

> A recurrent structurally plastic graph can learn local transitions and compose them into multi-step behavior in a controlled symbolic successor task.

This is the strongest manuscript-relevant result from this thread.

### Limitation

The thread also establishes important limitations:

* MNIST results are not enough to prove recurrent graph reasoning.
* Reward gating has not yet been validated.
* Experiment 4 may be too clean.
* Baselines and repeated seeds are still needed.
* No broad naturalistic dataset has yet been tested.

### Future work

The thread directly motivates:

* Experiment 5 contextual successor world.
* Noisy/delayed feedback.
* Rule reversal and adaptation.
* Multimodal number grounding.
* Gridworld reward environments.

### Supplementary material

This thread contributes useful supplementary material:

* model architecture diagrams,
* ablation tables,
* metric definitions,
* checkpoint summaries,
* run scripts,
* analysis scripts,
* synthetic successor task design,
* future experimental roadmap.

---

## 11. Claims-and-evidence rows contributed by this thread

| Claim                                                         | Evidence                                                                                             | Caveat                                                                          | Experiment(s)    | Artifact(s)                                              | Manuscript status |
| ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------- | -------------------------------------------------------- | ----------------- |
| Sparse plastic online learning can learn MNIST.               | Best test accuracy **0.9225**, latest **0.9190**.                                                    | May be sparse random features plus plastic readout.                             | Experiment 1/2   | `analysis_report.md`, `metrics.csv`, `test_accuracy.png` | Promising         |
| Confidence increased with performance in initial MNIST.       | Latest test confidence **0.8309**, train confidence **0.8979**.                                      | Does not prove calibration beyond this task.                                    | Experiment 1/2   | `analysis_report.md`, confidence plots                   | Preliminary       |
| Initial model was small and sparse.                           | `input_weights` shape `(4096, 64)`, `output_weights` shape `(4096, 10)`.                             | Small model may not demonstrate deeper architecture.                            | Experiment 1/2   | `latest_checkpoint_summary.json`                         | Historical only   |
| Recurrence did not improve MNIST.                             | `no_recurrence_sparse_plastic_readout` best **0.9255**, full recurrent **0.9230**.                   | MNIST may not need recurrence.                                                  | Experiment 3     | `suite_report.md`, `suite_comparison.csv`                | Needs baseline    |
| Homeostasis stabilized recurrent MNIST.                       | No-homeostasis latest test collapsed to about **0.7555–0.7595**, recurrent drive around **153–154**. | Not required in Experiment 4.                                                   | Experiment 3     | `suite_report.md`, `suite_best_accuracy.png`             | Promising         |
| Reward modulation was not helpful in current tests.           | `no_reward_modulation` best MNIST variant; `exp4_no_reward_gate` matched full traversal.             | Clean feedback may make reward modulation irrelevant.                           | Experiments 3, 4 | `suite_report.md`, `exp4_report.md`                      | Needs rerun       |
| Experiment 4 required recurrence.                             | `exp4_no_recurrence` got **0.0** transition and addition accuracy.                                   | Need audit for task leakage and more complex tasks.                             | Experiment 4     | `exp4_report.md`                                         | Strong            |
| Experiment 4 required structural plasticity.                  | `exp4_no_structural_plasticity` got about **0.0349** addition accuracy.                              | Hyperparameter sensitivity not yet known.                                       | Experiment 4     | `exp4_report.md`                                         | Strong            |
| Recurrent drive tracked successful traversal in Experiment 4. | Successful variants had recurrent drive around **811–826**.                                          | High drive alone is not sufficient; no-structural had nonzero drive and failed. | Experiment 4     | `exp4_recurrent_drive.png`, `exp4_report.md`             | Promising         |
| Unique active units expanded during successful traversal.     | Successful variants had addition unique active around **407**, no recurrence had **96**.             | Need path-level visualization.                                                  | Experiment 4     | `exp4_unique_active.png`, `exp4_report.md`               | Promising         |
| Experiment 4 task may be too easy.                            | Full, no-reward-gate, and no-homeostasis all reached **1.0** accuracy.                               | Requires harder contextual/noisy variants.                                      | Experiment 4     | `exp4_report.md`                                         | Needs rerun       |
| Contextual successor world is the next required test.         | Proposed to force mode-dependent routing.                                                            | Not yet implemented or run.                                                     | Experiment 5     | Handoff plan                                             | Preliminary       |
| Multimodal number grounding is a structured moonshot.         | Proposed modalities share number latent space.                                                       | Not yet implemented or run.                                                     | Experiment 6     | Handoff plan                                             | Preliminary       |
| Gridworld should come later.                                  | Proposed for delayed reward and embodied adaptation.                                                 | Not yet designed in detail.                                                     | Experiment 7     | Handoff plan                                             | Preliminary       |

---

## 12. Recommended follow-up actions

1. **Commit current artifacts to the repository**

   * Include generated packages, reports, plots, CSVs, and this digest.
   * Preserve exact filenames.

2. **Clean up recurrent MNIST suite reporting**

   * Investigate duplicated rows in `suite_report.md` and `suite_best_accuracy.png`.
   * Ensure each variant appears once unless intentionally replicated.
   * If replicated, label seed/run number explicitly.

3. **Add standard baselines**

   * Logistic regression.
   * Small MLP with similar parameter count.
   * Small CNN for MNIST only.
   * Random-feature classifier.
   * Reservoir / echo-state baseline for traversal tasks if feasible.

4. **Run multiple seeds**

   * At least 5 seeds for key variants.
   * Report mean, standard deviation, and confidence intervals.

5. **Audit Experiment 4 implementation**

   * Check for target leakage.
   * Confirm addition examples were not directly trained.
   * Confirm no-recurrence and no-structural variants are fair.
   * Inspect whether structural plasticity directly encodes the answer.

6. **Add path-level interpretability**

   * Visualize learned successor chains.
   * Report path entropy.
   * Report edge utilization.
   * Report active pathway overlap by number and step count.
   * Report wrong-route activation.

7. **Implement Experiment 5**

   * Contextual successor world.
   * Multiple transition systems.
   * Context-dependent routing.
   * Noisy feedback option.
   * Delayed reward option.
   * Rule reversal option.
   * Ablation suite.

8. **Strengthen reward modulation testing**

   * Use noisy feedback.
   * Use delayed feedback.
   * Use confidently-wrong penalties.
   * Compare full reward gate against no-reward-gate.

9. **Add inhibition / competition**

   * Implement explicit route competition.
   * Track wrong-route suppression.
   * Compare no-inhibition ablation.

10. **Prepare manuscript framing cautiously**

* Claim strong support only for Experiment 4’s controlled traversal result.
* Treat MNIST as proof-of-life.
* Treat reward gating and multimodal grounding as future work.

11. **Create a repository-level research README**

* Include architecture diagrams.
* Include experimental timeline.
* Include ablation logic.
* Include current evidence table.
* Include limitations.

12. **Prepare Experiment 6 only after Experiment 5**

* Do not jump directly to random multimodal dataset mixing.
* Use structured multimodal number grounding instead.
