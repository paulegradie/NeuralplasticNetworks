# Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems

[DRAFT STATUS NOTE]

This is `MANUSCRIPT_V2`, captured after Experiment 15 import and post-Exp15 claim hardening.

This draft is intentionally conservative. It frames the repository as a controlled symbolic/mechanistic benchmark and evidence map. It does not claim solved continual learning, broad neural-network superiority, raw sensory latent-world discovery, end-to-end perception, broad biological validation, or inference of unseen primitive transitions.

Controlling repository artifacts:

- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/threads/experiment15_analysis_digest.md`
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md`

Main post-Exp15 posture:

- Exp15 is a minimal fixed-profile neural comparator, not an exhaustive neural benchmark.
- A context-conditioned neural transition MLP and a world-head transition MLP solve the clean hard slice at ceiling.
- This narrows the manuscript away from broad CIRM-over-neural-model claims.
- Endpoint neural baselines help separate endpoint memorization from reusable transition composition.
- No-context neural results support a conflict-specific context-indexing claim, not a blanket claim that context is required for every suffix transition.
- Exp15 replay collapse is not interpreted scientifically unless audited.

---

## Title

**Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems**

Alternative shorter title:

**A Controlled Benchmark for Context-Indexed Route Memory and Recurrent Transition Composition**

---

## Abstract

Learning systems that operate across contexts can encounter incompatible local transition rules: the same state and action may imply different successors in different worlds. In such settings, a system can appear competent by memorizing endpoints or preserving one-step transitions while still failing to compose multi-step routes, separate conflicting worlds, or retain prior transition systems under pressure. We study this problem in a controlled symbolic route-memory benchmark designed to separate storage, context indexing, recurrent execution, capacity pressure, symbolic context selection, and endpoint memorization.

We evaluate a context-indexed structural route-memory mechanism in which one-step transitions are stored in world-indexed route structures and executed recurrently to produce multi-step routes. Across the manuscript-relevant experiments, internal ablations show that removing structural route storage collapses route-table formation and route execution; removing recurrence can preserve one-step route-table access while reducing multi-step composition to near chance; and removing context/world separation causes failures on deliberately incompatible local transitions. Clean supplied-context scaling reaches ceiling through the tested world counts, while finite structural-budget experiments expose degradation under capacity pressure rather than an unbounded capacity law.

Symbolic and neural controls narrow the claim. An oracle context-gated lookup table matches the full model on the clean supplied-context benchmark, so clean accuracy under supplied context is not itself the contribution. Experiment 14 shows that the active symbolic world can be selected from partial transition-cue evidence before route execution, reducing but not eliminating the oracle-context limitation. Experiment 15 adds a minimal fixed-profile neural comparator: context-conditioned neural transition learners solve the clean symbolic transition task, endpoint neural models dissociate seen-route endpoint performance from suffix-route and transition composition, and no-context neural variants fail conflict-sensitive first-step/full-route disambiguation. These results support a narrow mechanistic thesis: context-indexed storage, recurrent execution, symbolic context selection, and endpoint memorization are separable in this benchmark. The contribution is a traceable benchmark and evidence map, not a broad claim that ordinary neural networks cannot solve route memory.

[TODO before submission: replace citation placeholders with verified bibliography entries; add final manuscript-grade confidence intervals/effect sizes for retained claims; finalize main-vs-supplement placement for Exp14 and Exp15.]

---

## 1. Introduction

Continual learning and memory systems face a recurring interference problem. New information can conflict with prior information, and a learner must decide whether to update an existing representation, preserve an older one, retrieve a task-specific memory, or infer that the current situation belongs to a different context. In neural-network terms, this appears as catastrophic forgetting, task interference, routing, replay, parameter isolation, and memory augmentation. In cognitive and computational-neuroscience terms, it appears as context indexing, pattern separation, sequence memory, cognitive maps, and rapid memory allocation.

The route-memory problem studied here isolates one version of that pressure. A world defines a transition system over symbolic states. The same local cue can be compatible in one world and incompatible in another. For example, the tuple `(state=s0, action=a0)` may transition to `s1` in one world and `s7` in another. A shared transition table without context will overwrite or collapse these incompatible mappings. A full-route endpoint memorizer may succeed on routes seen during training but fail when asked to execute suffixes or demonstrate reusable one-step transition structure. A model with one-step transition access may still fail if it cannot recurrently apply those transitions to execute a route.

This benchmark therefore separates four questions that are often blurred together:

1. Can a system store local one-step transitions?
2. Can it select the correct context or world for a conflicting local cue?
3. Can it recurrently compose stored transitions into multi-step routes?
4. Can it do so under scaling, capacity pressure, and baseline controls?

The central hypothesis is not that context gating, recurrence, or memory allocation are novel in isolation. They are not. The manuscript-safe thesis is narrower: in a controlled symbolic route-memory benchmark, context-indexed structural storage and recurrent execution play separable roles in preserving and composing incompatible transition systems, and symbolic transition cues can select the active world before route execution.

This framing matters after Experiment 15. Before neural comparator results, it would have been tempting to treat strong CIRM performance and weak symbolic controls as evidence that ordinary neural sequence models lack the relevant behavior. Exp15 makes that overclaim unsafe. A conventional context-conditioned transition MLP can solve the clean symbolic transition table when world/context identity is supplied. A parameter-isolated world-head transition MLP also solves it. The manuscript must therefore avoid broad neural-superiority language. The supported contribution is a mechanism-decomposition benchmark: it shows which storage, execution, context, endpoint, and capacity mechanisms diverge under controlled probes.

The current paper makes the following conservative contributions:

- It defines a symbolic route-memory benchmark for incompatible transition systems with metrics that separate route-table storage, seen-route composition, suffix-route composition, first-step context conflict accuracy, retention, and capacity pressure.
- It shows, within the tested model family, that structural route storage is required for reliable route-table formation and route execution.
- It shows that recurrent execution is required to compose stored one-step transitions into multi-step routes.
- It shows that context/world indexing is required for deliberately incompatible local transitions and full-route disambiguation.
- It shows that clean supplied-context performance is not enough to establish novelty, because oracle context-gated lookup and context-conditioned neural transition learning can solve the clean symbolic setting.
- It adds a symbolic transition-cue selection experiment showing that the active world can be selected from partial symbolic evidence before route execution.
- It adds a minimal neural comparator that clarifies endpoint memorization versus transition composition and narrows claims about neural baselines.

---

## 2. Related work and positioning

[TODO: convert citation placeholders to verified bibliography entries.]

This work sits near several active literatures: catastrophic forgetting and continual learning, memory-augmented neural networks, fast weights and differentiable plasticity, mixture-of-experts and modular routing, latent-cause/context inference, neural algorithmic reasoning, compositional generalization, and hippocampal-inspired memory models.

The nearest risk is overclaiming. Continual-learning methods already use replay, task isolation, masking, routing, regularization, expansion, and memory systems. Memory-augmented networks and differentiable memory systems already separate storage from computation. Mixture-of-experts and modular systems already route inputs to specialized parameters. Latent-cause models already address context inference. Neural algorithmic reasoning and graph-learning work already study path-like computation and compositional execution. The present manuscript should not claim novelty for any of these ideas in isolation.

The intended contribution is instead benchmark-level and mechanistic. The route-memory setup creates a small but traceable environment in which local transition storage, context indexing, recurrent execution, endpoint memorization, symbolic cue selection, and capacity pressure can be measured separately. The value is not that the benchmark is naturalistic or biologically complete. It is that the benchmark exposes dissociations that are easy to hide with a single endpoint accuracy number.

The biological motivation should also remain disciplined. The mechanism is inspired by ideas such as rapid storage, indexing, recurrence, route-like sequence memory, and context separation. However, the experiments are symbolic and synthetic. They do not establish a hippocampal mechanism, structural plasticity in biological tissue, or end-to-end perceptual learning.

---

## 3. Problem setup

Let there be a set of worlds or contexts:

`W = {w_1, ..., w_K}`

and a set of symbolic states:

`S = {s_1, ..., s_N}`.

Each world defines a transition function:

`T_w: S x A -> S`

where `A` is an action or route-mode set. A context conflict occurs when two worlds define different successors for the same local cue:

`T_{w_i}(s, a) != T_{w_j}(s, a)` for some `i != j`.

A route of length `L` is produced by repeated transition application:

`s_{t+1} = T_w(s_t, a_t)`.

The benchmark tracks several metrics:

- **Route-table or transition accuracy**: whether one-step transitions are stored or predicted correctly.
- **Seen-route composition accuracy**: whether full routes from the seen route set are executed correctly.
- **Suffix-route composition accuracy**: whether suffixes can be executed without relying only on full-route endpoint memorization.
- **First-step context conflict accuracy**: whether a model chooses the correct first transition when the same local cue conflicts across worlds.
- **Retention after sequential worlds**: whether learned routes remain accessible after sequential exposure to worlds.
- **World/context selection accuracy**: whether the active symbolic context can be selected from transition-cue evidence.
- **Capacity and corruption sweeps**: whether performance changes under world count, route length, structural budget, or cue corruption.

The distinction between supplied-context and selected-context experiments is essential. In supplied-context experiments, the world label is given. This isolates context-indexed storage but does not test context inference. In Experiment 14, the active context is selected from partial symbolic transition cues before route execution. This is stronger than oracle context supply but still narrower than raw sensory latent-world discovery.

---

## 4. Mechanism

The tested mechanism stores one-step route transitions in context-indexed structural route memory. A query provides the current symbolic state, route/action information where relevant, and either a supplied or selected world/context. The selected context determines which stored transition structure is read. Multi-step execution is recurrent: the output state at time `t` becomes the input state for time `t+1`.

This creates a mechanistic decomposition:

- **Structural storage**: the system must write and preserve local transition entries.
- **Context indexing**: incompatible transitions must be separated by world/context.
- **Recurrent execution**: stored transitions must be iterated to produce routes.
- **Context selection**: when context is not supplied, symbolic evidence must select the active world.
- **Capacity management**: finite memory budgets create pressure and degradation.

The benchmark is designed so that each component can fail independently. A no-structural-plasticity condition can fail to form the route table. A no-recurrence-at-evaluation condition can preserve local transition access while failing multi-step composition. A no-context condition can learn many non-conflicting transitions while failing deliberately incompatible first-step mappings. An endpoint memorizer can solve seen full routes while failing suffix probes.

---

## 5. Experimental evidence base

The manuscript-relevant evidence base is currently organized around Experiments 11-15.

| Experiment | Manuscript role | Conservative interpretation |
|---|---|---|
| Exp11 | Early context-separated memory and ablation evidence | Supports incompatible-world memory framing, with older artifact-layout caveats. |
| Exp12 | Clean supplied-context capacity scaling | Shows ceiling route-table/composition through tested world counts under supplied context. |
| Exp13 | Finite-capacity breaking pressure | Shows observed degradation under structural budget pressure; no fitted capacity law. |
| Exp13.1 | Publication-hardening ablations | Supports structural storage, recurrence, and context-binding dissociations; lesion diagnostic is not positive evidence. |
| Exp13.2 | Symbolic/algorithmic baseline suite | Shows oracle context-gated lookup solves clean supplied-context benchmark and endpoint/no-recurrence/no-context controls fail in distinct ways. |
| Exp14 | Symbolic transition-cue context selection | Shows active symbolic world selection from partial transition cues before route execution; not raw latent-world discovery. |
| Exp15 | Minimal neural comparator | Shows fixed-profile neural baselines, including ceiling context-conditioned transition MLPs and endpoint-vs-transition dissociations; not exhaustive neural benchmarking. |

---

## 6. Results

### 6.1 Structural storage is required within the benchmark

The core structural-storage claim is benchmark-specific. In the current evidence map, removing structural route storage collapses route-table formation and route execution. Exp13.1 is the clearest manuscript-facing source: the no-structural-plasticity condition is reported with route-table accuracy around 0.0286 and composition accuracy around 0.0317, while the corresponding full condition reaches ceiling in the core ablation summary.

This supports the claim that structural transition storage is required for this model family and task setup. It does not support the universal claim that every route-memory-capable system must implement explicit symbolic structural plasticity. Exp15 narrows the claim further: a context-conditioned neural transition MLP can solve the clean symbolic transition problem when trained directly on the transition objective and supplied with context.

[Figure 2 candidate: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; source data: `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv`.]

### 6.2 Recurrent execution dissociates one-step storage from multi-step composition

The recurrence claim is one of the strongest mechanistic dissociations. Exp13.1 reports that a no-recurrence-at-evaluation condition can preserve route-table accuracy at 1.0000 while reducing multi-step composition to approximately 0.0401. Exp13.2 reinforces the same logic: no-recurrence controls preserve local transition access while failing full route composition.

This result explains why route-table accuracy alone is insufficient. A system can know the next step but fail to animate that knowledge through a multi-step route. In this benchmark, recurrence is the execution mechanism that turns stored local transitions into route behavior.

The claim should remain operational: recurrence is required for the tested route-execution protocol. It should not be generalized to every sequence-modeling architecture or training objective.

### 6.3 Context indexing resolves incompatible local transitions

World/context indexing separates incompatible local transition systems. In supplied-context experiments, the active context is given. In those settings, context-indexed route memory preserves otherwise conflicting mappings. Shared no-context lookup fails conflict-sensitive probes because the same local cue maps to different successors in different worlds.

Exp15 sharpens this claim. At the hard slice (`world_count=32`, `route_length=12`, `n_seeds=10`), no-context neural variants fail first-step conflict probes: the no-context transition MLP has first-step context conflict accuracy 0.0312, and no-context GRU variants are at or near floor. However, the no-context transition MLP reaches 1.0000 suffix-route composition and 0.9193 transition accuracy. This means context is not required for every suffix transition. It is required for deliberately incompatible local mappings and full-route disambiguation where the route begins with a conflicting transition.

This is an important V2 correction. The manuscript should not state that context is universally required for all route composition. The safe statement is that context/world identity is required when local transition cues are incompatible across worlds.

### 6.4 Endpoint memorization is separable from reusable transition composition

Endpoint memorization can look strong under seen-route metrics while failing transition-composition probes. Exp13.2 shows this symbolically: endpoint memorization can solve seen endpoints while failing suffix-route composition. Exp15 shows a neural version of the same dissociation. At the hard slice, `neural_gru_endpoint_context` reaches 0.9990 seen-route composition but only 0.4040 suffix-route composition and 0.0232 transition accuracy. The sequence Transformer baseline reaches 0.5435 seen-route composition but only 0.1184 suffix-route composition and 0.0070 transition accuracy.

This supports the benchmark’s decomposition. Seen-route endpoint success is not the same as reusable transition structure. Suffix and transition probes are required to distinguish endpoint memorization from route execution.

### 6.5 Clean supplied-context scaling is ceiling-limited

Exp12 reports ceiling route-table and composition accuracy through the tested world counts under clean supplied context. This supports a clean scaling claim, but the claim is ceiling-limited. It does not establish an unbounded capacity law, nor does it by itself demonstrate novelty relative to oracle context-gated lookup.

Exp13.2 makes that caveat central: an oracle context-gated transition table matches the full model on the clean supplied-context benchmark. Therefore, clean supplied-context ceiling performance is necessary evidence for the mechanism but not sufficient as the manuscript’s novelty claim.

[Figure 3 candidate: `docs/manuscript/figures/figure_03_capacity_scaling.png`; source data: `docs/manuscript/source_data/figure_03_capacity_scaling.csv`.]

### 6.6 Finite structural budget exposes degradation under pressure

Exp13 and Exp13.1 introduce finite structural-budget pressure. The manuscript-safe claim is that finite structural budget produces an observed route-execution degradation curve. The current evidence should not be described as a fitted capacity law unless a capacity-law analysis is later added. Local-vs-global budget comparisons are promising but still need paired seed-level analysis if elevated centrally.

[Figure 4 candidate: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; source data: `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`.]

### 6.7 Symbolic transition cues can select the active world before execution

Exp14 reduces the oracle-context limitation within the symbolic benchmark. Instead of receiving the world label directly, the model receives partial symbolic transition-cue evidence and selects the active world before route execution. In the hard clean slice, CIRM world selection and route composition reach 1.0000. Under high cue corruption, the relevant selection/composition metrics degrade to roughly 0.94 while the oracle context-gated table remains an upper-bound control.

This supports a new narrow claim: the active symbolic context can be selected from partial symbolic transition cues before route execution. It does not support raw sensory latent-world discovery, end-to-end perception, or general latent-cause inference.

[Figure 5 candidate: `docs/manuscript/figures/figure_05_symbolic_context_selection.png`; source data: `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`.]

### 6.8 Minimal neural comparator narrows, rather than inflates, the claims

Exp15 is retained in this V2 draft as a compact main-text neural comparator table, currently Table 4. This is a placement decision for V2 drafting, not a final journal-layout decision.

[Table 4 candidate: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`.]

At the hard slice (`world_count=32`, `route_length=12`, `n_seeds=10`), the context-conditioned transition MLP and the world-head transition MLP reach 1.0000 on all reported metrics. This directly prevents broad claims that ordinary neural models cannot solve the clean symbolic benchmark. It also clarifies the benchmark: if the model is trained as a supervised one-step transition learner with explicit context, the clean symbolic transition-composition task is easy for this neural baseline.

Other neural variants expose useful dissociations. The endpoint GRU memorizes seen routes but has weak transition accuracy. The rollout GRU with context learns some conflict-sensitive one-step behavior but fails long-route rollout/composition in the fixed profile. The no-context transition MLP solves suffix composition while failing first-step/full-route disambiguation. The replay variant collapses in this run but is explicitly not retained as a scientific claim until audited.

The manuscript consequence is clear: Exp15 closes a minimal neural-baseline gap while narrowing the interpretation. CIRM should be presented as an interpretable route-memory mechanism and benchmark decomposition, not as a globally superior alternative to neural networks.

---

## 7. Discussion

The evidence supports a controlled route-memory decomposition. Structural storage, context indexing, recurrence, endpoint memorization, finite capacity, and symbolic context selection can be experimentally separated. This is useful because many memory claims are ambiguous when only endpoint accuracy is reported. A model can memorize full routes, learn local transitions, select contexts, or recurrently execute transitions; these are not equivalent.

The strongest current story is not that CIRM uniquely solves a task no neural model can solve. Exp15 disproves that overstatement for the clean transition setting. The strongest story is instead that the benchmark clarifies how different mechanisms fail. Oracle context-gated lookup solves supplied-context clean routes. Context-conditioned neural transition learning solves the clean symbolic transition table. Endpoint models can memorize seen routes without reusable transition structure. No-recurrence controls can preserve one-step access while failing route execution. No-context models fail deliberately incompatible first transitions. Capacity pressure produces degradation boundaries. Symbolic transition cues can select a world, but only in a controlled symbolic setting.

This puts the manuscript in a defensible but narrow category: a mechanistic benchmark and evidence map for context-indexed route memory.

---

## 8. Limitations

The current manuscript has several important limitations.

First, the benchmark is symbolic and synthetic. It does not test naturalistic navigation, raw perception, language, or learned sensory representations.

Second, many experiments supply the context label. Exp14 partially addresses this through symbolic transition-cue selection, but it does not solve raw latent-world discovery.

Third, Exp15 is a minimal neural comparator. It uses fixed small model profiles and does not include architecture search, large recurrent/attention models, memory-augmented/key-value neural baselines, or a route-length-16 neural profile.

Fourth, Exp15 includes a provenance caveat: the manifest was reconstructed after a final SQLite manifest-write failure, and the SQLite `run_manifest` table may be empty. The imported CSV artifacts are treated as authoritative unless a later audit says otherwise.

Fifth, the replay neural variant collapsed in Exp15. This should not be interpreted scientifically until the implementation and training regime are audited.

Sixth, Exp13.1 lesion diagnostics should not be cited as positive mechanism evidence because the targeted critical-edge lesion result did not show the expected pattern.

Seventh, capacity results should be described as observed degradation curves, not fitted capacity laws.

Eighth, biological framing should remain inspiration-level. The experiments do not establish a hippocampal mechanism or biological structural plasticity.

---

## 9. Current figure and table plan

Candidate main-text assets for V2:

| Asset | Current role | Caveat |
|---|---|---|
| Figure 1 | Conceptual route-memory schematic | Framing only; not empirical evidence. |
| Figure 2 | Structural plasticity and recurrence ablation | Internal symbolic ablation; final uncertainty review pending. |
| Figure 3 | Clean capacity scaling | Ceiling-limited; no fitted capacity law. |
| Figure 4 | Finite structural budget/local-global pressure | Narrow main or supplement; paired seed-level local/global analysis pending. |
| Figure 5 | Exp14 symbolic context selection | Main or supplement decision remains human-facing; symbolic cues only. |
| Table 1 | Claim/evidence map | Headline values require caption/prose review. |
| Table 2 | Run integrity | Older experiments have layout/provenance caveats. |
| Table 3 | Statistical summary | Effect-size grouping still needs review. |
| Table 4 | Exp15 minimal neural comparator | Current V2 placement is compact main-text table; can move to supplement if venue/space requires. |

---

## 10. Provisional conclusion

This repository is close to supporting a conservative first manuscript, but not yet submission-ready. The defensible contribution is a controlled symbolic benchmark and mechanistic evidence map for context-indexed route memory. The work shows that structural storage, recurrent execution, context indexing, endpoint memorization, symbolic context selection, and neural transition learning have different signatures under carefully separated probes.

The post-Exp15 conclusion is narrower and stronger than the pre-Exp15 posture. Neural baselines are no longer absent, but their results prevent broad neural-superiority claims. The paper should argue that CIRM is interpretable and diagnostically useful within the benchmark, while acknowledging that simple context-conditioned neural transition learning can solve the clean symbolic transition task.

---

## 11. Remaining work before submission

- Verify and finalize all citation metadata.
- Finalize Exp14 placement: main Figure 5 versus supplement.
- Finalize Exp15 placement: current V2 uses compact main-text Table 4; human may move it to supplement.
- Add manuscript-grade confidence intervals/effect sizes for retained claims.
- Human-review generated figures, captions, and table text.
- Audit Exp15 replay before interpreting it scientifically.
- Add optional memory-augmented/key-value neural baseline only if the target venue or reviewers require broader neural coverage.
- Run fresh command/path verification before submission handoff.
- Add `LICENSE` and `CITATION.cff` after human license choice.
