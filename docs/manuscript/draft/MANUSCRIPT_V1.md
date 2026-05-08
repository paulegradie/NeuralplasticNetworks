# Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems

[DRAFT STATUS NOTE]

This is `MANUSCRIPT_V1`, generated on 2026-05-08 from `MANUSCRIPT_V0` after a live/current literature search focused on continual learning, memory-augmented architectures, fast-weight/plastic memory systems, context/task inference, modular routing, neural algorithmic reasoning, compositional generalization, and computational neuroscience.

The empirical claim set remains governed by the post-Experiment-14 claim freeze and manuscript asset pipeline for:

`https://github.com/GradieResearch/context-indexed-route-memory`

Intended repository path:

`docs/manuscript/draft/MANUSCRIPT_V1.md`

Controlling documents inspected for this V0 draft:

- `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/BASELINE_REQUIREMENTS.md`
- `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`
- `docs/manuscript/tables/table_01_claim_evidence.md`
- `docs/manuscript/tables/table_02_run_integrity.md`
- `docs/manuscript/tables/table_03_statistical_summary.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/experiments/exp13_2_summary.md`
- `docs/experiments/exp14_summary.md`

Main caveat: this manuscript is drafted as a controlled symbolic/mechanistic benchmark paper. It does **not** claim solved continual learning, broad neural-network superiority, raw perceptual latent-world discovery, broad biological proof, or inference of unseen primitive transitions. Neural baselines are absent. The generated figures and tables are candidate manuscript assets, not yet human-approved final submission figures.

Literature note: this V1 draft incorporates a targeted live literature search performed on 2026-05-08. The search located recent 2024-2026 work on continual-learning surveys, memory-augmented transformers and AI-agent memory, task-free/context-inferred continual learning, mixture-of-experts routing, hippocampal-inspired neural continual learning, latent-cause/context models, hippocampal spatial scaffolds for episodic memory, structural knowledge in AI, neural algorithmic reasoning, and compositional generalization. Citation placeholders remain manuscript-style; final submission should still verify BibTeX metadata, venues, DOIs, and recent acceptance status.

---

## Title options

1. Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems
2. Structural Route Memory Separates Storage and Execution in Synthetic Context-Switching Tasks
3. Context-Indexed Route Memory: A Synthetic Benchmark for Structural Plasticity, Recurrence, and Symbolic Context Selection
4. Recurrent Route Execution over Context-Indexed Transition Memory in Incompatible Symbolic Worlds
5. Storage, Context, and Execution in a Synthetic Route-Memory Benchmark
6. Symbolic Transition-Cue Selection for Context-Indexed Route Memory
7. A Controlled Benchmark for Context-Indexed Structural Memory and Recurrent Route Composition
8. Route-Table Storage and Recurrent Execution Dissociate under Contextual Interference

Working title chosen for V0:

**Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems**

---

## Abstract

Memory systems that must operate under contextual interference face a basic problem: the same local cue can imply different transitions in different task contexts. In a route-memory setting, this creates incompatible transition systems over a shared symbolic substrate. A model may store one-step transitions, retrieve endpoints, or preserve context labels, but still fail to execute multi-step routes when local transitions must be composed. We study this problem in a controlled symbolic benchmark designed to separate route storage, context indexing, and route execution.

We evaluate a context-indexed structural route-memory mechanism in which one-step transitions are stored in context- or world-indexed route tables and routes are executed recurrently by iterating through the stored transition structure. Across the manuscript-relevant experiments, ablations show that removing structural plasticity collapses route-table formation and route execution; removing recurrence can preserve one-step route-table accuracy while reducing multi-step composition to near-chance; and removing context separation causes interference between incompatible transition systems. Clean supplied-context scaling experiments show ceiling route-table and composition accuracy through the tested world counts, while finite structural budget experiments produce an observed degradation curve rather than an unbounded capacity law.

A symbolic/algorithmic baseline suite clarifies the claim boundary. An oracle context-gated transition table matches the full model on the clean supplied-context benchmark, so clean accuracy under supplied context is not by itself the novelty claim. However, shared no-context lookup fails conflict-sensitive first-step probes, endpoint memorization fails suffix-route composition, and no-recurrence controls dissociate one-step storage from executable multi-step composition. Experiment 14 extends the benchmark by selecting the active symbolic world from partial transition-cue evidence before recurrent route execution. In the hard clean slice, the selector reaches ceiling world selection and composition; under high cue corruption, selection and composition degrade while the oracle context-gated table remains an upper-bound control.

These results support a narrow mechanistic thesis: in this controlled symbolic setting, context-indexed structural storage and recurrent execution play separable roles in preserving and composing incompatible route systems, and symbolic transition cues can reduce—but not eliminate—the oracle-context limitation. The work does not establish broad biological validity, end-to-end perceptual context discovery, neural-network superiority, or a general solution to continual learning. Its contribution is a traceable benchmark and mechanism analysis that exposes where storage, context selection, recurrence, capacity, and memorization controls diverge.

[TODO: Replace this abstract with journal-specific word count and add final numerical confidence intervals once manuscript-grade CI/effect-size tables are human-reviewed.]

---

## 1. Introduction

Learning systems often encounter new information that conflicts with previously learned information. In continual learning, this is usually discussed as catastrophic forgetting: new updates can overwrite or interfere with old capabilities [McCloskeyCohen1989; French1999; Kirkpatrick2017]. In memory-augmented and modular systems, the same pressure appears as a storage and retrieval problem: how can a system preserve distinct memories, retrieve the relevant one, and execute behavior based on it without destructively mixing incompatible contexts [Graves2014; Graves2016; Weston2014; Sukhbaatar2015]?

The route-memory problem studied here isolates one form of this challenge. A "world" or context defines a transition system over symbolic states. The same starting symbol and action can imply one successor in world A and a different successor in world B. A system that collapses all transitions into a shared table will overwrite or average incompatible transitions. A system that stores full endpoints may succeed on seen full routes but fail when asked to execute suffixes or compose stored one-step transitions. A system with a perfect local route table may still fail multi-step behavior if it cannot iteratively apply stored transitions. This makes route memory a useful controlled setting for separating at least four mechanisms: structural storage, context indexing, recurrent execution, and context selection.

The hypothesis tested in this repository is that a context-indexed structural route memory can store incompatible local transition systems when transitions are allocated or addressed by context, and that recurrent execution is required to animate stored one-step transitions into multi-step routes. The claim is deliberately narrower than broad continual learning. The benchmark is symbolic. It does not test raw perception, natural language, autonomous world discovery from sensory streams, or biological mechanism. Instead, it asks whether a small set of mechanistic distinctions can be made empirically clear under controlled interference.

The post-Experiment-14 evidence base supports a conservative manuscript spine. Across the internal experimental sequence, removing structural plasticity collapses route-table formation and route execution; removing recurrence preserves route-table accuracy in some settings while composition collapses; context indexing separates incompatible transition systems; clean supplied-context scaling reaches ceiling performance through tested world counts; finite structural budget produces an observed degradation curve; and symbolic transition cues can select the active world before route execution in a controlled non-oracle setting.

The oracle-context issue is central. Many route-memory experiments supply the world/context label directly. This is a valid way to test whether context-indexed storage can preserve incompatible transition systems, but it does not establish latent context inference. The Experiment 13.2 baseline suite reinforces this concern: an oracle context-gated transition table matches the full model on the clean supplied-context benchmark. Therefore, this manuscript does not claim that the full model defeats oracle context gating under supplied context. Instead, the contribution is a decomposition: which controls fail under which probes, and which mechanisms are required for storage, execution, and conflict-sensitive context use.

Experiment 14 partially changes the story by replacing the supplied context label with symbolic transition-cue selection. The model receives partial evidence about transitions in the active world, selects a symbolic world/context, and then executes routes using the selected route memory. In the hard clean slice, world selection and route composition reach ceiling; under high cue corruption, performance degrades while the oracle context-gated table remains at ceiling. This reduces the oracle-context criticism within the symbolic benchmark, but it does not solve raw sensory context discovery or general latent-cause inference.

This manuscript makes the following publication-safe contributions:

- It defines a controlled symbolic route-memory benchmark for incompatible transition systems, with metrics that separate route-table storage, recurrent route execution, context conflict, suffix composition, capacity pressure, and symbolic context selection.
- It shows, within this benchmark, that structural plasticity is necessary for reliable route-table formation and route execution under the tested ablations.
- It shows that one-step route-table storage and multi-step composition can dissociate: no-recurrence controls can preserve local transition access while failing executable multi-step routes.
- It shows that context/world indexing separates incompatible transition systems under supplied context, while shared no-context lookup fails conflict-sensitive probes.
- It maps clean supplied-context capacity through the tested world counts and finite structural budget degradation under pressure, without claiming a fitted capacity law.
- It adds a symbolic transition-cue selection experiment showing that the active world can be selected from partial symbolic transition evidence before route execution, reducing but not eliminating the oracle-context limitation.
- It explicitly positions symbolic/algorithmic baselines as partial baseline coverage and identifies neural baselines, prior-art import, final figure review, and metric cleanup as remaining blockers before a stronger submission.

[Table 1 here: claim evidence summary. Source: `docs/manuscript/tables/table_01_claim_evidence.md`. Supports: C1-C7, C13, and C12 discussion posture.]

[Table 2 here: run integrity summary. Source: `docs/manuscript/tables/table_02_run_integrity.md`. Supports: provenance for Exp11, Exp12, Exp13, Exp13.1, Exp13.2, and Exp14.]

[Table 3 here: statistical summary. Source: `docs/manuscript/tables/table_03_statistical_summary.md`. Supports: figure/source-data statistical summaries; caveat: effect-size grouping still needs human review.]

---

## 2. Background and related work

### 2.1 Catastrophic forgetting and continual learning

Continual learning studies systems that acquire, update, and preserve knowledge over non-stationary data streams. Classic work identified catastrophic interference when sequential neural-network training overwrote prior associations [McCloskeyCohen1989; French1999]. Modern reviews continue to organize the field around the same core pressure: an agent must learn new tasks while preserving old capabilities, often without full access to prior data [Wang2024ComprehensiveCL; Yang2025SystematicCL; AdvancesCL2025]. Common solution families include regularization, replay, architectural expansion, parameter isolation, distillation, and combinations of these approaches [Kirkpatrick2017; Zenke2017; Rebuffi2017; LopezPaz2017; Li2025KDSurvey].

The present work is related to continual learning because it studies interference between incompatible transition systems. However, it is not a broad continual-learning solution. The benchmark is symbolic, route-based, and mechanism-focused. It does not evaluate class-incremental recognition, domain-incremental perception, large-scale data streams, or task-free real-world adaptation. This distinction matters because recent continual-learning reviews emphasize benchmark setting and task-identity assumptions as central to interpretation [Wang2024ComprehensiveCL; Yang2025SystematicCL; vanDeVenTolias2019]. The route-memory benchmark is closer to a controlled task-incremental or context-indexed memory setting, with Exp14 adding symbolic cue-based context selection.

Recent work also reinforces the importance of explicitly distinguishing task-incremental, class-incremental, task-free, and domain-shift settings. Online task-free continual-learning approaches create or adapt submodels when distributional discrepancies appear [ODDL2025]. New mixture-based and sparse-adapter approaches attempt to reduce forgetting in large pretrained models by routing or isolating task-relevant capacity [MoRA2025; SplitOnShare2026]. These works are important nearest-neighbour risks for this manuscript because they address task/context uncertainty and capacity allocation directly. The current paper should therefore avoid claiming that context selection or modular routing is novel by itself.

### 2.2 Memory-augmented neural computation and AI-agent memory

Memory-augmented neural networks separate computation from storage by providing an external memory or differentiable read/write interface. Neural Turing Machines and Differentiable Neural Computers are canonical examples of differentiable external memory [Graves2014; Graves2016]. Memory Networks and End-to-End Memory Networks use memory slots and learned retrieval for reasoning over stored facts [Weston2014; Sukhbaatar2015]. Matching Networks and memory-augmented meta-learning systems show how stored examples can support rapid adaptation [Santoro2016; Vinyals2016].

Current work has broadened this literature in two directions that are relevant to CIRM. First, memory-augmented transformer surveys now classify memory by functional objective, representation type, and integration mechanism, including parameter-encoded, state-based, explicit, and hybrid memories, with core operations such as reading, writing, forgetting, and capacity management [Omidi2025MATSurvey]. Second, AI-agent memory surveys argue that memory is becoming a first-class system primitive, distinguishing token-level, parametric, and latent memories and separating agent memory from RAG and context engineering [Hu2025AgentMemory]. Evaluations of long-term memory for long-context question answering further show that memory architectures should be judged by retrieval, reasoning, and token-efficiency tradeoffs, not by the existence of memory alone [Terranova2025LongTermMemory].

CIRM is not a transformer memory architecture or an LLM-agent memory system. Its contribution is more primitive and narrower: it creates a symbolic route-memory benchmark in which storage, context indexing, recurrent execution, suffix composition, and capacity pressure can be measured separately. The recent AI-memory literature strengthens the motivation for such decomposition because "memory" now covers many distinct mechanisms. The manuscript should therefore define route memory operationally rather than relying on broad memory terminology.

### 2.3 Fast weights, Hebbian plasticity, and differentiable plasticity

Fast weights and plastic connections provide a bridge between fixed-parameter networks and rapidly updated memory. Hebbian learning introduced the idea that co-active units strengthen their connections [Hebb1949]. Hopfield networks demonstrated recurrent associative storage [Hopfield1982]. Fast-weight ideas later framed temporary connection changes as a way to store recent associations without permanently overwriting slower weights [HintonPlaut1987]. Modern differentiable plasticity optimizes plasticity rules using gradient descent [Miconi2018; Miconi2019].

A particularly relevant modern connection is the equivalence between linearized self-attention and fast weight programmers: Schlag, Irie, and Schmidhuber show that linear transformers can be interpreted as systems in which a slow network programs fast weights through key-value outer products [Schlag2021FastWeights]. This matters because it makes the boundary between attention, associative memory, and fast weights less sharp than older terminology suggests.

CIRM differs from these models because the manuscript-relevant experiments use explicit symbolic route tables rather than learned dense fast weights. Still, the fast-weight literature is a close prior-art family for any claim about rapid memory writing. The safe claim is not that dynamic memory writing is novel. The supported claim is that, within this route-memory benchmark, removing structural route storage collapses route-table formation and route execution, while recurrence and context indexing have separable effects.

### 2.4 Context, gating, modularity, and latent task inference

Context-conditioned computation and modular routing are long-standing ideas. Mixture-of-experts models use gating to select specialized modules [Jacobs1991; JordanJacobs1994]. Modern sparse mixture-of-experts systems scale this idea with learned token or input routing [Shazeer2017]. Continual-learning systems often rely on task-specific masks, adapters, architectural expansion, or parameter isolation to reduce interference [Rusu2016; Fernando2017]. Recent work continues this line through sparse mixture-of-rank adapters, task-free mixture-of-experts approaches, and routing mechanisms designed to mitigate forgetting or ambiguous task assignment [MoRA2025; SplitOnShare2026; MoB2025].

In cognitive science and computational neuroscience, latent-cause models explain how agents divide experience into inferred hidden contexts to support context-dependent learning [GershmanNiv2010; Lu2024LatentCauses]. A 2024 neural-network model of latent causes explicitly addresses how systems reconcile shared versus context-specific information when segmenting event streams [Lu2024LatentCauses]. This is highly relevant to CIRM: Exp14 selects a symbolic context from partial transition cues, but it does not learn a general latent-cause model from sensory streams.

The nearest prior-art risk is therefore substantial. Context gating, task masks, mixture-of-experts routing, and latent-cause inference are all well-established or actively developing. The manuscript should position Exp14 as a controlled symbolic transition-cue selector that reduces the oracle-label limitation in this benchmark, not as a general solution to latent task inference.

### 2.5 Compositional route execution and graph/path reasoning

Route execution overlaps with compositional generalization, graph reasoning, and neural algorithmic reasoning. Compositional generalization asks whether a model can recombine known components in novel ways [LakeBaroni2018; Hupkes2020]. Recent theoretical and benchmark work remains active: 2025 papers study necessary/sufficient conditions for compositional generalization, data coverage principles, and scalable evaluation of neural compositionality [Li2025CompositionalTheory; Chang2025Coverage; Camposampiero2025ScalableCompositional]. These works reinforce a key manuscript caveat: high performance on certain recombinations does not automatically imply broad systematic generalization.

Graph neural networks and neural algorithmic reasoning systems attempt to learn or execute graph algorithms such as shortest paths, connectivity, and traversal [Scarselli2009; Li2016; Battaglia2018; Velickovic2020]. Recent work studies transformer reasoning capabilities via graph algorithms, neural algorithmic reasoning for hypergraphs with looped transformers, and mechanistic gaps between successful predictions and faithful algorithm execution [Sanford2024GraphAlgorithms; Huang2025HypergraphNAR; MindTheGap2025]. These papers are especially relevant because they show that algorithmic or graph-like success must be interpreted through mechanism-sensitive probes, not only output accuracy.

The CIRM benchmark is narrower than general graph/path reasoning. It does not test arbitrary graph algorithms, learned shortest paths, or broad algorithmic extrapolation. Its contribution is the explicit separation between local transition storage, recurrent route execution, full-route endpoint memorization, suffix-route composition, first-step context conflicts, and finite route-memory capacity. This is a benchmark-level decomposition rather than a claim of general neural algorithmic reasoning.

### 2.6 Neuroscience motivation: indexing, recurrence, plasticity, and consolidation

The hippocampus is associated with rapid episodic memory, relational memory, spatial maps, indexing, pattern separation/completion, and sequence representation [OkeefeNadel1978; TeylerDiScenna1986; TeylerRudy2007; McClelland1995; NormanOReilly2003; Eichenbaum2017]. Complementary learning systems theory proposes that hippocampal and cortical systems solve different parts of the stability-plasticity problem [McClelland1995; Kumaran2016]. Structural plasticity and synaptic remodeling provide biological motivation for dynamic memory allocation [Chklovskii2004; HoltmaatSvoboda2009].

Recent computational neuroscience and NeuroAI work strengthens the relevance of this framing while also sharpening the boundary. Chandra, Sharma, Chaudhuri, and Fiete propose a Vector-HaSH model in which hippocampal spatial scaffolds support associative and episodic sequence memory, including high-capacity sequence memorization through low-dimensional transitions [Chandra2025VectorHaSH]. This is closely adjacent conceptually because it links scaffolded internal structure, sequence memory, and transition learning. A 2025 Nature Communications paper proposes a corticohippocampal-inspired hybrid neural network for continual learning, using dual representations of specific and generalized memories to mitigate forgetting in task- and class-incremental scenarios [Shi2025CHHNN]. A 2025 Nature Machine Intelligence perspective argues that neuroscience can inform AI learning in continuously changing environments, especially through rapid behavioural shifts and population-level transitions under changing rules [Durstewitz2025NeuroAI]. A 2025 review on structural knowledge links dynamic memory, cognitive maps, schemas, and artificial systems [Yu2025StructuralKnowledge].

These works make the biological analogy more relevant but not stronger as evidence. CIRM should be described as computationally inspired by indexing, context separation, recurrence, structural storage, and route-like transition memory. It should not be described as proving a hippocampal mechanism. The recent Vector-HaSH and corticohippocampal-inspired continual-learning papers also raise the bar for biological positioning: a biological claim would require much more than symbolic route-table experiments.

### 2.7 Positioning of this work after the current literature search

The live literature search changes the V1 posture in three ways.

First, the closest prior-art families are broader and more active than the V0 draft implied. The manuscript sits near memory-augmented computation, fast weights, task/context inference, mixture-of-experts routing, neural algorithmic reasoning, compositional generalization, and hippocampal-inspired continual learning. Any one of these could produce reviewer objections if the manuscript overclaims novelty.

Second, the work remains potentially paper-worthy only if framed as a benchmark and mechanism-decomposition paper. The likely contribution is not "new context gating," "new plasticity," "new recurrent computation," or "brain-like memory." It is the controlled route-memory benchmark plus a traceable claim set showing where route-table storage, context indexing, recurrence, endpoint memorization, finite structural budget, and symbolic transition-cue selection diverge.

Third, the literature strengthens the case for Experiment 15 if the target venue is a strong ML venue. Recent work includes neural memory architectures, neural algorithmic reasoning systems, modular continual-learning systems, and hippocampal-inspired neural continual-learning models. A reviewer could reasonably ask whether ordinary GRUs/RNNs, transformers, memory-augmented networks, or modular/task-inferred baselines show the same behavior. The manuscript can proceed as a controlled symbolic/mechanistic paper, but it should not claim neural-model superiority without a neural baseline suite.

[TODO: Add a small "closest prior-art risk" table to the final manuscript if space permits: task-gated lookup, mixture-of-experts routing, fast weights/linear attention, differentiable external memory, neural algorithmic reasoning, hippocampal scaffold memory, and symbolic graph/path algorithms.]

## 3. Problem setup: route memory under contextual interference

We define a route-memory problem over symbolic transition systems. Let there be a set of worlds or contexts:

`W = {w_1, ..., w_K}`

and a shared set of symbolic states or nodes:

`S = {s_1, ..., s_N}`.

Each world defines a transition function over states and possibly actions or route modes:

`T_w: S × A -> S`.

A context conflict occurs when two worlds assign different successors to the same local cue:

`T_{w_i}(s, a) != T_{w_j}(s, a)` for some `i != j`.

A route is a sequence generated by repeated transition application:

`r = (s_0, a_0, s_1, a_1, ..., s_L)`

where `s_{t+1} = T_w(s_t, a_t)`.

The benchmark separates several evaluation targets:

- **Route storage**: whether the model stores or retrieves one-step transition entries, measured by route-table or first-step transition accuracy.
- **Route execution**: whether the model can execute a multi-step route by iterating through stored transitions, measured by composition accuracy.
- **Seen-route composition**: performance on routes or route starts that are available during training/evaluation under the same benchmark split.
- **Suffix-route composition**: performance when the model must execute a suffix of a route rather than retrieve a memorized full-route endpoint.
- **First-step context conflict accuracy**: whether the model chooses the correct first transition when the same local cue has different successors in different worlds.
- **World/context selection**: whether the model uses the appropriate world index, either supplied by the experiment or selected from symbolic transition cues.
- **Capacity scaling**: behavior as world count, route length, or structural budget pressure increases.
- **Cue corruption or context corruption**: sensitivity to wrong-world evidence or corrupted transition cues.

In supplied-context experiments, the active world label is provided to the model. This isolates whether context-indexed storage can avoid interference, but it leaves open whether the system can infer context. In Exp14-style cue-selection experiments, the model receives partial symbolic transition evidence and selects a world before route execution. This reduces the oracle-label assumption but remains symbolic and controlled.

[Figure 1 here: conceptual route-memory schematic. Source: `docs/manuscript/figures/figure_01_conceptual_route_memory.png` and `.svg`; source data: `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv`. Supports: C1-C4 framing and C13 boundary wording. Caveat: conceptual only, not empirical evidence.]

---

## 4. Model/mechanism

The manuscript-relevant mechanism is a context-indexed structural route memory. At a high level, the model stores transitions as route-memory entries indexed by world/context. A query consists of a current symbolic state, route mode/action where relevant, and an active world/context. The active world selects the transition table or route field used to retrieve the next state. Multi-step route execution is performed recurrently: the successor from one step becomes the current state for the next step, and the process repeats until the route length is reached.

This gives three analytically separable components:

1. **Structural transition storage**: the mechanism must allocate or store one-step transitions. In the ablations, removing structural plasticity collapses route-table formation and route execution.
2. **Context/world indexing**: the mechanism must keep incompatible transitions separated across worlds. Without this, shared no-context lookup fails conflict-sensitive probes.
3. **Recurrent execution**: the mechanism must repeatedly apply stored transitions. Without recurrence, one-step route-table accuracy can remain high while multi-step composition collapses.

The "route-table" and "route field" language should be treated as symbolic/mechanistic terminology, not as a claim that the model implements a known biological field theory. In this manuscript, the important property is that route storage and route execution are measured separately. A model can have an accurate one-step route table and still fail multi-step route execution if it cannot recurrently compose transitions. Similarly, a model can memorize full-route endpoints and still fail suffix composition if it has not stored reusable transition primitives.

Exp14 adds a symbolic context-selection front end. Instead of receiving an oracle world label, the model receives partial transition cues. These cues are symbolic observations about transitions in the active world. The selector chooses a world/context, after which the same context-indexed route memory executes the route recurrently. Cue corruption means some cue evidence points away from the correct world under a synthetic corruption process. This should be described as symbolic transition-cue selection, not as raw sensory latent-world discovery.

[TODO: Add a concise pseudo-code block from the implementation after verifying exact function names and data structures in `experiments/experiment14_latent_context_inference/` and the core experiment implementations.]

### 4.1 What the model is not

The model is not a complete biological brain model. It is not an end-to-end perceptual model. It is not a general neural continual-learning solution. It is not proof of a hippocampal indexing mechanism. It is not yet benchmarked against full neural baselines such as GRU/RNN executors, transformers, neural replay systems, or differentiable external-memory networks under matched conditions.

The model also should not be described as inferring unseen primitive transitions. Current evidence supports composition over stored one-step transitions and failure of endpoint memorization on suffix probes. The seen/unseen primitive boundary remains a metric-cleanup issue if elevated centrally.

---

## 5. Experimental overview

| Experiment | Purpose | Main claim supported | Key metric(s) | Manuscript role |
|---|---|---|---|---|
| Exp11 | Test context-separated memory for incompatible worlds and early ablations. | C2, C3, C4 support | memory indices, retention, ablations | Supporting evidence for incompatible-world rebinding; historical layout lacks current validation JSON. |
| Exp12 | Test clean capacity/generalization under supplied context. | C5, plus C2/C3/C4 support | composition accuracy, route-table accuracy across world counts | Main evidence for clean supplied-context ceiling scaling through tested world counts. |
| Exp13 | Push the system under finite structural budget and failure pressure. | C6, C7 narrow/supplement | composition accuracy across global/local budget ratios | Main/narrow evidence for observed budget degradation; no fitted capacity law. |
| Exp13.1 | Publication-hardening ablations and diagnostics. | C1-C4; C7 caveated | route-table accuracy, composition accuracy, context-binding, recurrence, structural-plasticity ablations | Main evidence for Figure 2; lesion diagnostic is negative/caveated, not positive mechanism evidence. |
| Exp13.2 | Symbolic/algorithmic baseline suite. | C12 discussion; C2-C4 controls | oracle context-gated table, shared no-context lookup, endpoint memorizer, no-recurrence controls | Baseline/readiness evidence; symbolic/algorithmic only, not neural. |
| Exp14 | Select symbolic world/context from partial transition cues before route execution. | C13; narrows C2/C10 | world-selection accuracy, seen-route composition, suffix composition, first-step context accuracy, cue-count/corruption behavior | Candidate main Figure 5 or high-priority supplement; reduces oracle-context criticism only within symbolic benchmark. |

Excluded or non-central experiments: Exp1-Exp6 are exploratory/historical or methodological precursors. Exp7-Exp10 provide route-composition and plasticity/consolidation background but are not the central manuscript evidence. C8 consolidation, C9 seen/unseen primitive boundary, C10 context corruption, and C11 continuous/noisy bridge should remain supplementary/future-work unless their metric and framing gaps are resolved.

---

## 6. Results

### 6.1 Structural plasticity supports storage of incompatible route systems

The frozen C1 claim is benchmark-specific: within this symbolic route-memory benchmark, removing structural plasticity collapses route-table formation and route execution. The claim evidence table reports that the Exp13.1 no-structural-plasticity condition has route-table accuracy 0.0286 and composition accuracy 0.0317, while the full model reaches ceiling on the corresponding core ablation summary. The broader claim inventory links this pattern to earlier experiments including Exp8, Exp11, Exp12, Exp13, Exp13.1, and Exp13.2.

[Figure 2 here: structural plasticity and recurrence ablation. Source: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png` and `.svg`; source data: `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv`; source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`. Supports: C1-C4. Caveat: internal symbolic ablation; uncertainty uses aggregate normal approximation.]

This result supports the need for structural route storage in the benchmark. It does not show that all neural systems require explicit structural plasticity, nor that biological structural plasticity is the mechanism used by brains for route memory. It is an internal ablation result in a symbolic setting.

[TODO: Add final confidence intervals/effect sizes from a human-reviewed version of Table 3 before submission.]

### 6.2 Recurrent execution is required for multi-step route composition

The frozen C3 claim is that recurrent execution is required to compose stored one-step route memories into multi-step routes. Exp13.1 provides the clearest manuscript-facing ablation: no-recurrence-at-eval preserves route-table accuracy at 1.0000 but reduces composition accuracy to approximately 0.0401. Exp13.2 reinforces this boundary: no-recurrence-at-eval preserves route-table/first-step accuracy at 1.0000 in the hard clean slice while seen and suffix composition drop to 0.0000.

This dissociation is central. If the system can retrieve a local transition but cannot repeatedly feed each successor back into the transition memory, then it has storage without route execution. In this sense, recurrence is not claimed as a novel component, but as the mechanism required to animate a stored transition structure into multi-step behavior within the benchmark.

[Figure 2 here: same source as above. Panel emphasis: route-table accuracy versus composition accuracy under no-recurrence-at-eval.]

Caveat: Exp13.1 supports the need for recurrence at evaluation time in the tested route-execution regime. It should not be generalized to all forms of sequence modeling or all training regimes.

### 6.3 Route-table storage and route composition dissociate

The frozen C4 claim is that route-table storage and multi-step compositional execution are separable in this benchmark. The no-recurrence ablation is one form of evidence. Endpoint memorization controls provide another. Exp13.2 reports that an endpoint memorizer reaches 1.0000 seen-route accuracy but 0.0000 suffix-route accuracy in the hard clean slice. Exp14 repeats the same conceptual control under symbolic transition-cue selection: the endpoint memorizer can succeed on full seen-route endpoints while failing suffix composition.

This matters because a full-route endpoint can be memorized without storing reusable one-step transitions. Suffix-route probes help distinguish endpoint recall from route execution. Similarly, one-step route-table probes distinguish local storage from multi-step composition. Together, these metrics show why a single headline accuracy can hide different mechanisms.

[Table 1 here: C4 row and endpoint-memorization caveat. Source: `docs/manuscript/tables/table_01_claim_evidence.md`.]

Caveat: this dissociation does not prove abstract reasoning or unseen primitive-transition inference. It supports a narrower distinction between local transition storage, full-route endpoint memorization, and recurrent composition over stored primitives.

### 6.4 Capacity and world-scaling behavior

The frozen C5 claim is ceiling-limited: under clean supplied context, the full model maintains ceiling route-table and composition accuracy through the tested world counts. Exp12 reports route-table and composition accuracy of 1.0000 at world counts 2, 4, 8, 16, and 32 under the clean supplied-context full profile. This shows that the tested context-indexed storage regime can preserve incompatible transition systems through the tested scale.

[Figure 3 here: clean capacity scaling. Source: `docs/manuscript/figures/figure_03_capacity_scaling.png` and `.svg`; source data: `docs/manuscript/source_data/figure_03_capacity_scaling.csv`; source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`. Supports: C5. Caveat: ceiling-limited clean supplied-context result; no fitted capacity law.]

The frozen C6 claim is narrower: finite structural budget produces an observed route-execution degradation curve. Exp13 shows that, at 32 worlds and route length 12, global budget pressure yields composition accuracy increasing from approximately 0.2755 at 0.25 budget to 1.0000 at exact budget. This supports an observed degradation curve, not a formal law.

C7 local-vs-global budget behavior is currently supplement or narrow main. Table 1 reports that at 0.50 budget, Exp13 global composition is approximately 0.5173 whereas local per-world composition is approximately 0.0596. This is a strong-looking difference, but the freeze document requires paired seed-level comparison before treating it as a broad central claim.

[Figure 4 here: finite structural budget/local-global pressure. Source: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png` and `.svg`; source data: `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`; source artifacts: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` and `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`. Supports: C6-C7. Caveat: observed degradation curve only; paired seed-level local/global inference remains deferred.]

[TODO: Decide whether Figure 4 is main text or supplement. If main, add paired seed-level local-vs-global statistics and final caption language that avoids capacity-law claims.]

### 6.5 Symbolic context selection from transition evidence reduces the oracle-context criticism

The supplied-context experiments show that context-indexed storage can preserve incompatible transition systems, but they leave open a serious criticism: if the correct world label is supplied, then an oracle context-gated lookup table can solve the clean benchmark. Exp13.2 confirms this: at the hard clean slice with `world_count=32` and `route_length=16`, both the full CIRM variant and the oracle context-gated transition table report 1.0000 route-table accuracy, seen-route composition accuracy, suffix-route composition accuracy, and first-step context accuracy.

Exp14 addresses this limitation in a narrow symbolic way. The model receives partial symbolic transition cues, selects a world/context, and then executes the route recurrently. The full profile uses 20 seeds; world counts 4, 8, 16, and 32; route lengths 4, 8, 12, and 16; cue counts 1, 2, 4, and 8; and corruption rates 0.0, 0.1, 0.25, and 0.5. Comparators include an oracle context-gated table, shared no-context table, endpoint memorizer using the same latent selector, random selector, recency selector, and compact hash-slot selectors.

In the hard clean slice (`world_count=32`, `route_length=16`, `cue_count=8`, `corruption_rate=0.0`), the CIRM latent selector reaches 1.0000 seen-route world selection, seen-route composition, suffix-route composition, and first-step context accuracy. At the same hard slice under `corruption_rate=0.5`, world selection and seen-route composition are approximately 0.9416, while the oracle context-gated table remains at 1.0000. At `corruption_rate=0.25`, increasing cue count improves symbolic selection: seen-route composition rises from approximately 0.7473 with one cue to approximately 0.9992 with eight cues.

[Figure 5 here: symbolic context selection from transition cues. Source: `docs/manuscript/figures/figure_05_symbolic_context_selection.png` and `.svg`; source data: `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`; source artifact: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`. Supports: C13. Caveat: symbolic transition-cue selection only; oracle remains an upper bound.]

This result supports C13: the active symbolic world/context can be selected from partial transition-cue evidence before route execution. It also clarifies C2: context indexing can be supplied or symbolically selected, but these are different claims. Exp14 reduces the oracle-context criticism because the model no longer receives the world label directly in the cue-selected condition. It does not eliminate the criticism entirely because the cues are symbolic, the corruption process is synthetic, and the oracle context-gated table remains a ceiling upper-bound control.

Important metric caveat: shared no-context suffix-route metrics can be misleading if suffix probes bypass the first-step context conflict. For context-sensitive evaluation, first-step context conflict accuracy and seen-route world selection are more directly diagnostic.

[TODO: Decide whether Exp14/C13 is main text or high-priority supplement. V0 drafts it as main-narrow because the generated asset manifest includes Figure 5 and the freeze document allows C13 as main-narrow or high-priority supplement.]

### 6.6 Supplementary or negative results

Several results should remain supplementary, historical, or limitations in the first manuscript.

Consolidation (C8) should be framed as a stability-plasticity bias rather than an accuracy-rescue mechanism. Easy regimes do not require consolidation, and Exp13.1 did not show that consolidation strength materially rescues constrained-budget accuracy. This topic may be useful in discussion, but it should not be a central result without stronger dose-response or robustness analysis.

The seen-versus-unseen primitive boundary (C9) requires metric cleanup. Existing evidence suggests the model composes over stored primitives and does not infer unseen primitive transitions, but route-table accuracy requires seen/unseen/all split metrics before this becomes a central claim. The manuscript should explicitly avoid broad abstract rule-induction language.

Context corruption (C10) should be framed as wrong-world or symbolic cue-evidence sensitivity, not generic stochastic robustness. Exp13/Exp13.1 wrong-world injection and Exp14 cue corruption identify context-selection failure boundaries, but they do not establish broad robustness to realistic noise.

The continuous/noisy bridge (C11) remains preliminary. It tests whether a decoded noisy symbolic input can feed route memory; it is not end-to-end perception or learned visual representation.

Exp13.1 lesion diagnostics should not be cited as positive mechanism evidence. The targeted lesion sensitivity result was less damaging than the random count-matched lesion result, so this is either a diagnostic failure, a definition problem, or a negative result requiring audit/rerun before any positive use.

[NEEDS SUPPLEMENT DECISION: consolidation stability-plasticity bias. Expected source data: `experiments/experiment12_capacity_generalization/analysis/exp12/consolidation_pressure_summary.csv`, `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv`.]

[NEEDS METRIC CLEANUP: seen/unseen primitive boundary. Expected source data: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`, but route-table seen/unseen/all splits are pending.]

---

## 7. Discussion

The results support a narrow mechanistic interpretation. In a controlled symbolic route-memory benchmark, structural storage, context indexing, and recurrent execution play distinct roles. Structural plasticity supports formation of route-table entries. Context/world indexing prevents incompatible local transition systems from collapsing into a shared table. Recurrence turns stored one-step transitions into executable multi-step routes. Symbolic transition-cue selection can choose an active world before execution, reducing the reliance on directly supplied oracle context labels.

The strongest conceptual point is the separation between route storage and route execution. A system can store local transitions but fail to execute multi-step routes. A system can memorize endpoints but fail suffix composition. A system can solve clean supplied-context route memory with an oracle context-gated table, but fail when context must be inferred or when conflict-sensitive first-step decisions are tested. These distinctions are difficult to see if the benchmark uses only one aggregate accuracy metric.

The results also clarify the role of baselines. Exp13.2 is important because it prevents overclaiming. The oracle context-gated transition table matches CIRM under clean supplied context, showing that clean accuracy with supplied labels is not enough. Shared no-context lookup fails conflict-sensitive probes, showing that context separation matters where local transitions conflict. Endpoint memorization fails suffix composition, showing that full-route recall is not equivalent to compositional route execution. These are symbolic/algorithmic baselines, not full neural baselines.

Experiment 14 changes the manuscript from a purely oracle-context story to a partially cue-selected context story. The active symbolic world can be selected from transition cues before recurrent execution. Multiple cues improve selection under corruption. However, the result remains symbolic and controlled. It does not establish perception, open-ended latent-cause discovery, or a general inference algorithm.

The relationship to continual learning should be stated carefully. The benchmark shares the stability-plasticity and interference concerns of continual learning, but it is not a class-incremental or domain-incremental neural benchmark. It is closer to a controlled task-incremental memory setting with explicit or symbolically selected context. It may be useful for future memory architectures because it exposes which metrics separate storage, routing, and execution, but it does not replace standard continual-learning evaluation.

The biological interpretation should also remain bounded. Hippocampal indexing, cognitive maps, pattern separation/completion, recurrence, and structural plasticity motivate the work, but the experiments are synthetic and symbolic. The manuscript can say that the mechanism is computationally inspired by these ideas. It should not claim that the brain uses this exact mechanism or that the benchmark validates a biological theory.

### 7.1 Why this is not yet a neural benchmark result

The current evidence does not include matched GRU/RNN, transformer, neural replay, differentiable-memory, or neural parameter-isolation baselines. Exp13.2 provides symbolic/algorithmic controls, including shared no-context lookup, oracle context-gated lookup, endpoint memorization, recurrent non-plastic rules, bounded LRU/replay variants, superposition/hash-slot controls, and parameter-isolation controls. These are valuable for mechanism decomposition, but they do not answer whether ordinary neural sequence models trained under comparable conditions show the same retention, composition, and context-sensitivity behavior.

For a controlled symbolic/mechanistic paper, this limitation can be acknowledged and may be acceptable. For a stronger ML venue, a minimal neural baseline suite is likely required before submission.

### 7.2 Biological interpretation boundary

The project’s terminology overlaps with neuroscience: indexing, route fields, recurrence, consolidation, inhibition, structural plasticity, and context separation. These analogies are useful for generating hypotheses and explaining why the benchmark is interesting. They are not evidence that the model is biologically implemented or biologically sufficient. The manuscript should avoid phrases such as "the model discovers worlds like the hippocampus" or "brain-like memory is solved." Appropriate phrasing includes: "computationally inspired by indexing and recurrence" and "a synthetic benchmark that isolates mechanisms relevant to memory interference."

---

## 8. Limitations

1. **Synthetic symbolic tasks.** The benchmark uses symbolic states, worlds, routes, and transition cues. This supports controlled mechanistic analysis but limits claims about natural data.

2. **Limited perceptual grounding.** The manuscript-relevant experiments do not learn from raw sensory input. Exp13’s continuous/noisy bridge is a decoded symbolic front end, not end-to-end perception.

3. **Oracle context assumptions.** Many experiments supply the world/context label directly. Exp14 reduces this limitation using symbolic transition cues, but does not eliminate it.

4. **Symbolic latent context selection.** Exp14 cues are symbolic transition evidence. Cue corruption is synthetic. The result does not establish general latent-cause inference or raw sensory world discovery.

5. **Baseline limitations.** Exp13.2 supplies symbolic/algorithmic baselines only. Neural baselines are absent.

6. **Prior-art/novelty import incomplete.** The repository still lacks a local prior-art/novelty assessment artifact. Citation verification and recent literature search remain required before submission.

7. **Metric cleanup remains.** Seen-versus-unseen primitive transition claims require cleaned route-table and composition splits. Suffix metrics can be misleading when they bypass first-step context conflicts.

8. **Uncertainty and effect-size review.** Candidate statistical tables exist, but effect-size groupings and confidence intervals require human review before exact manuscript citation.

9. **Generated figures are candidates.** Figures 1-5 have been generated by a reproducible asset pipeline, but they are not final journal figures. Captions, panel choices, and main-vs-supplement placement require review.

10. **Capacity law not established.** Finite-budget results show observed degradation curves. No fitted capacity law is claimed.

11. **Consolidation claim is preliminary.** Current evidence supports at most a stability-plasticity bias, not necessity or robust accuracy rescue.

12. **Lesion diagnostic failure.** Exp13.1 targeted lesion results should not be cited positively without audit/rerun.

13. **Biological interpretability is limited.** The work is biologically inspired, but the evidence is not biological.

14. **Reproducibility metadata gaps.** Older Exp11/Exp12 layouts lack validation JSON and SQLite manifests. Fresh command verification and hardware/runtime logs are still required before submission.

15. **License/citation metadata missing.** A human-selected license and `CITATION.cff` remain needed before formal public release or submission.

---

## 9. Conclusion

This manuscript establishes a cautious first result from the context-indexed route-memory research program. In a controlled symbolic benchmark, context-indexed structural storage can preserve incompatible local transition systems, recurrent execution is required to compose stored one-step transitions into multi-step routes, and route-table storage can dissociate from executable composition. Clean supplied-context scaling reaches ceiling through tested world counts, while finite structural budget produces an observed degradation curve. Symbolic transition-cue selection can choose the active world before route execution, reducing the oracle-context limitation within the benchmark.

The work should be read as a mechanism-focused benchmark and evidence map, not as a complete continual-learning solution, biological theory, or neural benchmark result. Its immediate value is to make failure modes visible: no structural storage, no context separation, no recurrence, endpoint memorization, finite capacity, and corrupted symbolic context evidence fail in different ways. The next step is not to broaden the claim, but to harden it: verify citations, finalize figures and statistics, decide the target venue, and add neural baselines if the venue requires them.

---

## 10. Methods

### 10.1 Route-memory task generation

The benchmark generates symbolic worlds containing transition systems over shared state symbols. Routes are generated by applying world-specific one-step transitions over a fixed route length. Context conflict arises when the same local cue has different successors in different worlds. The key manipulated variables across experiments include world count, route length, structural budget, local/global budget pressure, cue count, and cue corruption.

[TODO: Fill exact task-generation parameters and pseudocode from the implementation files in `experiments/experiment11_context_memory/`, `experiments/experiment12_capacity_generalization/`, `experiments/experiment13_breaking_point/`, `experiments/experiment13_1_publication_hardening/`, `experiments/experiment13_2_baseline_suite/`, and `experiments/experiment14_latent_context_inference/`.]

### 10.2 Model variants and controls

The full mechanism uses context-indexed structural route memory with recurrent route execution. Manuscript-relevant controls include:

- no structural plasticity;
- no context binding or shared no-context lookup;
- no recurrence at evaluation;
- oracle context-gated transition table;
- endpoint memorizer;
- recurrent non-plastic rules;
- bounded LRU/replay variants;
- parameter-isolation controls;
- superposition/hash-slot symbolic controls;
- random and recency selectors in Exp14;
- compact hash-slot selectors in Exp14.

The oracle context-gated table is an upper-bound supplied-context control, not a defeated competitor.

### 10.3 Metrics

Primary metrics include:

- `route_table_accuracy`: accuracy of one-step transition storage/retrieval.
- `composition_accuracy`: accuracy of multi-step route execution.
- `composition_accuracy_seen_route`: composition on seen route probes.
- `suffix_route_composition_accuracy` or equivalent suffix metric: composition on route suffixes to test primitive reuse rather than endpoint memorization.
- `first_step_context_accuracy`: correctness of conflict-sensitive first-step transitions.
- `world_selection_accuracy_seen_route`: Exp14 world/context selection from symbolic transition cues.
- capacity/budget metrics: composition accuracy across global and local budget ratios.
- validation integrity: pass/warn/fail counts, metrics rows, summary rows, effect-size rows, plot counts, manifest/database presence.

[VERIFY: Metric names should be made exact against CSV headers before submission.]

### 10.4 Experimental profiles and seeds

The run-integrity table reports:

- Exp11: historical full run, 673,920 metrics rows and 720 summary rows, no validation JSON in the historical layout.
- Exp12: historical full run, 477,360 metrics rows and 200 summary rows, no validation JSON in the historical layout.
- Exp13: full aggregate finite-budget source, validation PASS with 8 pass, 1 warn, 0 fail; 47,015 metrics rows and 640 summary rows.
- Exp13.1: full run `exp13_1_full_20260506_214756`, validation PASS with 27 pass, 0 warn, 0 fail; 20 seeds; 3,000 metrics rows; 78 summary rows; SQLite and manifest present.
- Exp13.2: full run `exp13_2_full_20260507_165813`, validation PASS with 28 pass, 0 warn, 0 fail; 20 seeds; 15,040 metrics rows; 748 summary rows; 624 effect-size rows; SQLite and manifest present.
- Exp14: full run `exp14_full_20260507_210712`, validation PASS with 27 pass, 0 warn, 0 fail; 20 seeds; 46,080 metrics rows; 2,304 summary rows; 12,288 effect-size rows; SQLite and manifest present.

Source: `docs/manuscript/tables/table_02_run_integrity.md`.

### 10.5 Validation and artifact generation

Validation reports are available for Exp13, Exp13.1, Exp13.2, and Exp14. Older Exp11/Exp12 layouts lack validation JSON and SQLite manifests, so they should be cited with appropriate provenance caveats. The manuscript asset pipeline was generated with:

`python scripts/manuscript_assets/build_manuscript_assets.py`

This produced candidate figures, source-data CSVs, tables, `docs/manuscript/MANUSCRIPT_ASSET_MANIFEST.md`, and `docs/repo_audit/MANUSCRIPT_ASSET_GENERATION_REPORT.md`.

### 10.6 Figure and source-data generation

Generated candidate figure assets:

- Figure 1: `docs/manuscript/figures/figure_01_conceptual_route_memory.png`; `.svg`; source data `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv`.
- Figure 2: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; `.svg`; source data `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv`.
- Figure 3: `docs/manuscript/figures/figure_03_capacity_scaling.png`; `.svg`; source data `docs/manuscript/source_data/figure_03_capacity_scaling.csv`.
- Figure 4: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; `.svg`; source data `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`.
- Figure 5: `docs/manuscript/figures/figure_05_symbolic_context_selection.png`; `.svg`; source data `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`.

Generated manuscript tables:

- Table 1: `docs/manuscript/tables/table_01_claim_evidence.md` and `.csv`.
- Table 2: `docs/manuscript/tables/table_02_run_integrity.md` and `.csv`.
- Table 3: `docs/manuscript/tables/table_03_statistical_summary.md` and `.csv`.

[TODO: Before submission, human-review each generated panel and caption; decide whether Figure 5 is main or supplement; ensure every numerical claim in the final prose maps to source data and human-reviewed confidence intervals.]

---

## 11. Data and code availability

The source repository is:

`https://github.com/GradieResearch/context-indexed-route-memory`

Manuscript-relevant generated assets are currently organized under:

- `docs/manuscript/source_data/`
- `docs/manuscript/tables/`
- `docs/manuscript/figures/`

Experiment artifacts are under:

- `experiments/experiment11_context_memory/`
- `experiments/experiment12_capacity_generalization/`
- `experiments/experiment13_breaking_point/`
- `experiments/experiment13_1_publication_hardening/`
- `experiments/experiment13_2_baseline_suite/`
- `experiments/experiment14_latent_context_inference/`

[TODO: Add final data/code availability statement once the repository license, citation metadata, release tag, and archival DOI/Zenodo decision are finalized.]

---

## 12. Author contributions / acknowledgements / funding / conflicts

Author contributions: [TODO]

Acknowledgements: [TODO]

Funding: [TODO]

Conflicts of interest: [TODO]

Use of AI tools: [TODO: Add a transparent statement if required by target venue, including use of AI assistance in drafting, code review, or manuscript preparation.]

---

## Live literature search audit trail

Search performed: 2026-05-08.

Purpose: update the V0 related-work scaffold with current 2024-2026 literature and identify prior-art risks before drafting V1.

Search themes and incorporation decisions:

| Theme | Representative sources found | Manuscript consequence |
|---|---|---|
| Continual-learning surveys and settings | [Wang2024ComprehensiveCL], [Yang2025SystematicCL], [AdvancesCL2025], [Li2025KDSurvey] | Keep CIRM scoped as a symbolic/mechanistic benchmark; do not claim broad continual-learning solution. |
| Task-free/context-inferred continual learning | [ODDL2025], [MoRA2025], [SplitOnShare2026], [MoB2025] | Treat context/task routing as active prior art; avoid novelty claims for gating or capacity isolation. |
| Memory-augmented transformers and AI-agent memory | [Omidi2025MATSurvey], [Hu2025AgentMemory], [Terranova2025LongTermMemory] | Define route memory operationally; do not conflate CIRM with LLM/agent memory systems. |
| Fast weights and dynamic memory | [Schlag2021FastWeights] plus classic fast-weight/plasticity work | Acknowledge rapid memory writing as established prior art. |
| Latent causes/context inference | [Lu2024LatentCauses] | Frame Exp14 as symbolic transition-cue context selection, not general latent-cause discovery. |
| Neural algorithmic reasoning and graph/path reasoning | [Sanford2024GraphAlgorithms], [Huang2025HypergraphNAR], [MindTheGap2025] | Emphasize mechanism-sensitive probes and avoid broad graph-algorithm claims. |
| Compositional generalization | [Li2025CompositionalTheory], [Chang2025Coverage], [Camposampiero2025ScalableCompositional] | Keep C9 out of main claims unless metric cleanup is completed; do not claim broad systematicity. |
| Computational neuroscience and NeuroAI | [Chandra2025VectorHaSH], [Shi2025CHHNN], [Durstewitz2025NeuroAI], [Yu2025StructuralKnowledge] | Biological motivation is more relevant, but biological proof remains unsupported. |

[TODO: Before submission, export this audit into a local repository artifact such as `docs/manuscript/PRIOR_ART_LIVE_SEARCH_20260508.md` or `docs/manuscript/NOVELTY_ASSESSMENT_IMPORTED.md`, then cite it from `BASELINE_REQUIREMENTS.md` / `MANUSCRIPT_TODO.md`.]

---

## References to resolve


### New/current references added in V1 from live search

[Wang2024ComprehensiveCL]  
Full title: A Comprehensive Survey of Continual Learning: Theory, Method and Application  
Authors: Liyuan Wang; Xingxing Zhang; Hang Su; Jun Zhu  
Year: 2024  
Venue: IEEE Transactions on Pattern Analysis and Machine Intelligence  
URL/DOI: https://doi.org/10.1109/TPAMI.2024.3367329  
Why it is relevant: Current high-quality survey of continual-learning theory, methods, and applications.  
Where it should be cited: Related work 2.1; limitations around continual-learning scope.

[Yang2025SystematicCL]  
Full title: Continual learning: A systematic literature review  
Authors: Qinwen Yang; Liyuan Wang; Joerg Wicker; Gillian Dobbie  
Year: 2025/2026 issue  
Venue: Neural Networks 195:108226  
URL/DOI: https://doi.org/10.1016/j.neunet.2025.108226  
Why it is relevant: Covers continual-learning literature from 2010 to 2025 and provides refined taxonomy/settings.  
Where it should be cited: Related work 2.1; discussion of target-venue expectations.

[AdvancesCL2025]  
Full title: Advances in continual learning: A comprehensive review  
Authors: [VERIFY]  
Year: 2025  
Venue: Expert Systems with Applications 294:128739  
URL/DOI: https://doi.org/10.1016/j.eswa.2025.128739  
Why it is relevant: Recent review of continual-learning algorithms, benchmarks, metrics, and directions.  
Where it should be cited: Related work 2.1.

[Li2025KDSurvey]  
Full title: Continual Learning With Knowledge Distillation: A Survey  
Authors: Songze Li; Tonghua Su; Xu-Yao Zhang; Zhongjie Wang  
Year: 2025  
Venue: IEEE Transactions on Neural Networks and Learning Systems  
URL/DOI: https://doi.org/10.1109/TNNLS.2024.3476068  
Why it is relevant: Current survey of distillation-based continual-learning approaches.  
Where it should be cited: Related work 2.1.

[ODDL2025]  
Full title: Online task-free continual learning via discrepancy mechanism  
Authors: [VERIFY]  
Year: 2025  
Venue: Knowledge-Based Systems  
URL/DOI: https://doi.org/10.1016/j.knosys.2025.113688  
Why it is relevant: Task-free continual-learning approach with dynamic submodel creation.  
Where it should be cited: Context/task inference and baseline-risk discussion.

[MoRA2025]  
Full title: Little By Little: Continual Learning via Self-Activated Sparse Mixture-of-Rank Adaptive Learning  
Authors: Haodong Lu; Chongyang Zhao; Jason Xue; Lina Yao; Kristen Moore; Dong Gong  
Year: 2025  
Venue: arXiv:2506.21035  
URL/DOI: https://arxiv.org/abs/2506.21035  
Why it is relevant: Recent sparse mixture/adaptive-rank continual-learning method for large pretrained models.  
Where it should be cited: Context/gating/modularity and Experiment 15 motivation.

[SplitOnShare2026]  
Full title: Split-on-Share: Mixture of Sparse Experts for Task-Agnostic Continual Learning  
Authors: Fatema Siddika; Md Anwar Hossen; Tanwi Mallick; Ali Jannesari  
Year: 2026  
Venue: arXiv:2601.17616  
URL/DOI: https://arxiv.org/abs/2601.17616  
Why it is relevant: Very recent task-agnostic continual-learning approach using sparse experts.  
Where it should be cited: Context/gating/modularity and neural-baseline rationale.

[MoB2025]  
Full title: MoB: Mixture of Bidders  
Authors: Dev Vyas [VERIFY complete authorship]  
Year: 2025  
Venue: arXiv:2512.10969  
URL/DOI: https://arxiv.org/abs/2512.10969  
Why it is relevant: Reframes expert routing for continual learning and explicitly addresses gating forgetting.  
Where it should be cited: Context/gating/modularity and prior-art-risk section.

[Omidi2025MATSurvey]  
Full title: Memory-Augmented Transformers: A Systematic Review from Neuroscience Principles to Technical Solutions  
Authors: Parsa Omidi; Xingshuai Huang; Axel Laborieux; Bahareh Nikpour; Tianyu Shi; Armaghan Eshaghi  
Year: 2025  
Venue: arXiv:2508.10824  
URL/DOI: https://arxiv.org/abs/2508.10824  
Why it is relevant: Current memory-augmented transformer survey linking neuroscience principles and technical memory systems.  
Where it should be cited: Memory-augmented neural computation; positioning of route memory.

[Hu2025AgentMemory]  
Full title: Memory in the Age of AI Agents  
Authors: Yuyang Hu; Shichun Liu; Yanwei Yue; Guibin Zhang; Boyang Liu; Fangyi Zhu; Jiahang Lin; Honglin Guo; Shihan Dou; Zhiheng Xi; Senjie Jin; Jiejun Tan; Yanbin Yin; Jiongnan Liu; Zeyu Zhang; Zhongxiang Sun; Yutao Zhu; Hao Sun; Boci Peng; Zhenrong Cheng; Xuanbo Fan; Jiaxin Guo; Xinlei Yu; Zhenhong Zhou; Zewen Hu; Jiahao Huo; Junhao Wang; Yuwei Niu; Yu Wang; Zhenfei Yin; Xiaobin Hu; Yue Liao; Qiankun Li; Kun Wang; Wangchunshu Zhou; Yixin Liu; Dawei Cheng; Qi Zhang; Tao Gui; Shirui Pan; Yan Zhang; Philip Torr; Zhicheng Dou; Ji-Rong Wen; Xuanjing Huang; Yu-Gang Jiang; Shuicheng Yan  
Year: 2025  
Venue: arXiv:2512.13564  
URL/DOI: https://arxiv.org/abs/2512.13564  
Why it is relevant: Current survey/taxonomy of memory as a first-class capability in AI agents.  
Where it should be cited: Memory-augmented computation; discussion of memory terminology.

[Terranova2025LongTermMemory]  
Full title: Evaluating Long-Term Memory for Long-Context Question Answering  
Authors: Alessandra Terranova; Björn Ross; Alexandra Birch  
Year: 2025  
Venue: arXiv:2510.23730  
URL/DOI: https://arxiv.org/abs/2510.23730  
Why it is relevant: Evaluates memory-augmented methods for long-context QA and emphasizes memory architecture tradeoffs.  
Where it should be cited: Memory-augmented computation and benchmark positioning.

[Lu2024LatentCauses]  
Full title: Reconciling shared versus context-specific information in a neural network model of latent causes  
Authors: Qihong Lu; Tan T. Nguyen; Qiong Zhang; Uri Hasson; Thomas L. Griffiths; Jeffrey M. Zacks; Samuel J. Gershman; Kenneth A. Norman  
Year: 2024  
Venue: Scientific Reports 14, 16782  
URL/DOI: https://doi.org/10.1038/s41598-024-64272-5  
Why it is relevant: Closely related context/latent-cause model for shared versus context-specific memory.  
Where it should be cited: Context inference; Exp14 boundary.

[Schlag2021FastWeights]  
Full title: Linear Transformers Are Secretly Fast Weight Programmers  
Authors: Imanol Schlag; Kazuki Irie; Jürgen Schmidhuber  
Year: 2021  
Venue: ICML / PMLR 139:9355-9366  
URL/DOI: https://proceedings.mlr.press/v139/schlag21a.html  
Why it is relevant: Shows equivalence between linear attention and fast-weight programming.  
Where it should be cited: Fast weights and memory systems.

[Sanford2024GraphAlgorithms]  
Full title: Understanding Transformer Reasoning Capabilities via Graph Algorithms  
Authors: Clayton Sanford; Bahare Fatemi; Ethan Hall; Anton Tsitsulin; Mehran Kazemi; Jonathan Halcrow; Bryan Perozzi; Vahab Mirrokni  
Year: 2024  
Venue: arXiv:2405.18512  
URL/DOI: https://arxiv.org/abs/2405.18512  
Why it is relevant: Studies transformer graph-algorithm reasoning and scaling regimes.  
Where it should be cited: Graph/path reasoning and neural-baseline motivation.

[Huang2025HypergraphNAR]  
Full title: Neural Algorithmic Reasoning for Hypergraphs with Looped Transformers  
Authors: Zekai Huang; Yingyu Liang; Zhenmei Shi; Zhao Song; Zhen Zhuang  
Year: 2025  
Venue: arXiv:2501.10688  
URL/DOI: https://arxiv.org/abs/2501.10688  
Why it is relevant: Recent neural algorithmic reasoning work on hypergraphs and looped transformers.  
Where it should be cited: Graph/path reasoning.

[MindTheGap2025]  
Full title: Mind The Gap: Quantifying Mechanistic Gaps in Algorithmic Reasoning via Neural Compilation  
Authors: [VERIFY]  
Year: 2025  
Venue: arXiv:2505.18623  
URL/DOI: https://arxiv.org/abs/2505.18623  
Why it is relevant: Shows output accuracy can diverge from mechanistic faithfulness in neural algorithmic reasoning.  
Where it should be cited: Results/discussion around mechanism-sensitive probes.

[Li2025CompositionalTheory]  
Full title: A Theoretical Analysis of Compositional Generalization in Neural Networks: A Necessary and Sufficient Condition  
Authors: Yuanpeng Li  
Year: 2025  
Venue: arXiv:2505.02627  
URL/DOI: https://arxiv.org/abs/2505.02627  
Why it is relevant: Recent theoretical treatment of compositional generalization conditions.  
Where it should be cited: Compositional route execution and generalization caveats.

[Chang2025Coverage]  
Full title: The Coverage Principle: A Framework for Understanding Compositional Generalization  
Authors: Hoyeon Chang; Jinho Park; Hanseul Cho; Sohee Yang; Miyoung Ko; Hyeonbin Hwang; Seungpil Won; Dohaeng Lee; Youbin Ahn; Minjoon Seo  
Year: 2025  
Venue: arXiv:2505.20278  
URL/DOI: https://arxiv.org/abs/2505.20278  
Why it is relevant: Data-centric framework for compositional generalization and coverage limits.  
Where it should be cited: Compositional generalization caveats.

[Camposampiero2025ScalableCompositional]  
Full title: Scalable Evaluation and Neural Models for Compositional Generalization  
Authors: Giacomo Camposampiero; Pietro Barbiero; Michael Hersche; Roger Wattenhofer; Abbas Rahimi  
Year: 2025  
Venue: arXiv:2511.02667  
URL/DOI: https://arxiv.org/abs/2511.02667  
Why it is relevant: Recent scalable evaluation framework for compositional generalization.  
Where it should be cited: Compositional route execution and benchmark positioning.

[Chandra2025VectorHaSH]  
Full title: Episodic and associative memory from spatial scaffolds in the hippocampus  
Authors: Sarthak Chandra; Sugandha Sharma; Rishidev Chaudhuri; Ila Fiete  
Year: 2025  
Venue: Nature 638, 739-751  
URL/DOI: https://doi.org/10.1038/s41586-024-08392-y  
Why it is relevant: Recent hippocampal model linking spatial scaffolds, high-capacity associative memory, and sequence/episodic memory.  
Where it should be cited: Neuroscience motivation and biological-boundary discussion.

[Shi2025CHHNN]  
Full title: Hybrid neural networks for continual learning inspired by corticohippocampal circuits  
Authors: Qianqian Shi; Faqiang Liu; Hongyi Li; Guangyu Li; Luping Shi; Rong Zhao  
Year: 2025  
Venue: Nature Communications 16, 1272  
URL/DOI: https://doi.org/10.1038/s41467-025-56405-9  
Why it is relevant: Recent hippocampal/corticohippocampal-inspired neural continual-learning model.  
Where it should be cited: Neuroscience motivation; Experiment 15/neural-baseline rationale.

[Durstewitz2025NeuroAI]  
Full title: What neuroscience can tell AI about learning in continuously changing environments  
Authors: Daniel Durstewitz; Bruno Averbeck; Georgia Koppe  
Year: 2025  
Venue: Nature Machine Intelligence 7, 1897-1912  
URL/DOI: https://doi.org/10.1038/s42256-025-01146-z  
Why it is relevant: Current NeuroAI perspective connecting continual/in-context learning with changing-rule neuroscience.  
Where it should be cited: Introduction, neuroscience motivation, and limitations.

[Yu2025StructuralKnowledge]  
Full title: Structural knowledge: from brain to artificial intelligence  
Authors: Yingchao Yu; Yuping Yan; Yaochu Jin  
Year: 2025  
Venue: Artificial Intelligence Review 58, article 264  
URL/DOI: https://doi.org/10.1007/s10462-025-11270-2  
Why it is relevant: Review connecting cognitive maps, schemas, dynamic memory, and structural knowledge in AI.  
Where it should be cited: Neuroscience motivation; structural route-memory positioning.

### Existing canonical references retained from V0

[Hebb1949]  
Full title: *The Organization of Behavior: A Neuropsychological Theory*  
Authors: Donald O. Hebb  
Year: 1949  
Venue: Wiley  
URL/DOI: book; final bibliographic details to verify  
Why relevant: Canonical origin of Hebbian plasticity.  
Where to cite: Related work on plasticity and fast weights.

[Hopfield1982]  
Full title: Neural networks and physical systems with emergent collective computational abilities  
Authors: John J. Hopfield  
Year: 1982  
Venue: Proceedings of the National Academy of Sciences  
URL/DOI: https://doi.org/10.1073/pnas.79.8.2554  
Why relevant: Recurrent attractor memory and associative storage.  
Where to cite: Fast weights/plasticity; neuroscience recurrence.

[HintonPlaut1987]  
Full title: Using fast weights to deblur old memories  
Authors: Geoffrey E. Hinton; David C. Plaut  
Year: 1987  
Venue: Proceedings of the Ninth Annual Conference of the Cognitive Science Society / Cognitive Science literature  
URL/DOI: verify final citation  
Why relevant: Classic fast-weight framing of temporary memory.  
Where to cite: Fast weights subsection.

[Ba2016]  
Full title: Using Fast Weights to Attend to the Recent Past  
Authors: Jimmy Ba; Geoffrey Hinton; Volodymyr Mnih; Joel Z. Leibo; Catalin Ionescu  
Year: 2016  
Venue: NeurIPS / arXiv  
URL/DOI: https://arxiv.org/abs/1610.06258  
Why relevant: Modern neural fast weights for sequence memory.  
Where to cite: Fast weights subsection.

[Miconi2018]  
Full title: Differentiable plasticity: training plastic neural networks with backpropagation  
Authors: Thomas Miconi; Jeff Clune; Kenneth O. Stanley  
Year: 2018  
Venue: ICML / arXiv  
URL/DOI: https://arxiv.org/abs/1804.02464  
Why relevant: Differentiable plasticity as learned online weight updates.  
Where to cite: Fast weights/plasticity subsection.

[Miconi2019]  
Full title: Backpropamine: training self-modifying neural networks with differentiable neuromodulated plasticity  
Authors: Thomas Miconi; Aditya Rawal; Jeff Clune; Kenneth O. Stanley  
Year: 2019  
Venue: ICLR / arXiv  
URL/DOI: https://arxiv.org/abs/2002.10585 or verify exact version  
Why relevant: Neuromodulated differentiable plasticity; use only after verifying exact citation.  
Where to cite: Fast weights/plasticity if retained.

[Graves2014]  
Full title: Neural Turing Machines  
Authors: Alex Graves; Greg Wayne; Ivo Danihelka  
Year: 2014  
Venue: arXiv  
URL/DOI: https://arxiv.org/abs/1410.5401  
Why relevant: Differentiable external memory.  
Where to cite: Memory-augmented neural computation.

[Graves2016]  
Full title: Hybrid computing using a neural network with dynamic external memory  
Authors: Alex Graves et al.  
Year: 2016  
Venue: Nature  
URL/DOI: https://doi.org/10.1038/nature20101  
Why relevant: Differentiable Neural Computer; graph-like memory and path reasoning.  
Where to cite: Memory-augmented computation; graph/path reasoning.

[Weston2014]  
Full title: Memory Networks  
Authors: Jason Weston; Sumit Chopra; Antoine Bordes  
Year: 2014  
Venue: arXiv / ICLR workshop lineage  
URL/DOI: https://arxiv.org/abs/1410.3916  
Why relevant: External memory over stored facts.  
Where to cite: Memory-augmented computation.

[Sukhbaatar2015]  
Full title: End-To-End Memory Networks  
Authors: Sainbayar Sukhbaatar; Arthur Szlam; Jason Weston; Rob Fergus  
Year: 2015  
Venue: NeurIPS  
URL/DOI: https://arxiv.org/abs/1503.08895  
Why relevant: Differentiable memory retrieval.  
Where to cite: Memory-augmented computation.

[Santoro2016]  
Full title: Meta-Learning with Memory-Augmented Neural Networks  
Authors: Adam Santoro et al.  
Year: 2016  
Venue: ICML  
URL/DOI: https://proceedings.mlr.press/v48/santoro16.html  
Why relevant: Memory-augmented one-shot learning.  
Where to cite: Memory-augmented computation.

[Vinyals2016]  
Full title: Matching Networks for One Shot Learning  
Authors: Oriol Vinyals et al.  
Year: 2016  
Venue: NeurIPS  
URL/DOI: https://arxiv.org/abs/1606.04080  
Why relevant: External/example memory and fast retrieval.  
Where to cite: Memory-augmented computation.

[McCloskeyCohen1989]  
Full title: Catastrophic interference in connectionist networks: The sequential learning problem  
Authors: Michael McCloskey; Neal J. Cohen  
Year: 1989  
Venue: Psychology of Learning and Motivation  
URL/DOI: verify final citation  
Why relevant: Foundational catastrophic forgetting work.  
Where to cite: Introduction; continual learning.

[French1999]  
Full title: Catastrophic forgetting in connectionist networks  
Authors: Robert M. French  
Year: 1999  
Venue: Trends in Cognitive Sciences  
URL/DOI: verify final DOI  
Why relevant: Survey/overview of catastrophic forgetting.  
Where to cite: Continual learning.

[Kirkpatrick2017]  
Full title: Overcoming catastrophic forgetting in neural networks  
Authors: James Kirkpatrick et al.  
Year: 2017  
Venue: Proceedings of the National Academy of Sciences  
URL/DOI: https://doi.org/10.1073/pnas.1611835114  
Why relevant: Elastic Weight Consolidation.  
Where to cite: Continual learning; consolidation analogy boundary.

[Zenke2017]  
Full title: Continual Learning Through Synaptic Intelligence  
Authors: Friedemann Zenke; Ben Poole; Surya Ganguli  
Year: 2017  
Venue: ICML  
URL/DOI: https://proceedings.mlr.press/v70/zenke17a.html  
Why relevant: Regularization-based continual learning.  
Where to cite: Continual learning.

[Rebuffi2017]  
Full title: iCaRL: Incremental Classifier and Representation Learning  
Authors: Sylvestre-Alvise Rebuffi et al.  
Year: 2017  
Venue: CVPR  
URL/DOI: https://doi.org/10.1109/CVPR.2017.587  
Why relevant: Replay/exemplar-based continual learning.  
Where to cite: Continual learning.

[LopezPaz2017]  
Full title: Gradient Episodic Memory for Continual Learning  
Authors: David Lopez-Paz; Marc'Aurelio Ranzato  
Year: 2017  
Venue: NeurIPS  
URL/DOI: https://arxiv.org/abs/1706.08840  
Why relevant: Episodic memory/replay constraints.  
Where to cite: Continual learning.

[Rusu2016]  
Full title: Progressive Neural Networks  
Authors: Andrei A. Rusu et al.  
Year: 2016  
Venue: arXiv  
URL/DOI: https://arxiv.org/abs/1606.04671  
Why relevant: Parameter isolation/architectural expansion.  
Where to cite: Continual learning; modularity.

[Fernando2017]  
Full title: PathNet: Evolution Channels Gradient Descent in Super Neural Networks  
Authors: Chrisantha Fernando et al.  
Year: 2017  
Venue: arXiv  
URL/DOI: https://arxiv.org/abs/1701.08734  
Why relevant: Parameter routing/path isolation across tasks.  
Where to cite: Continual learning; modularity.

[Parisi2019]  
Full title: Continual lifelong learning with neural networks: A review  
Authors: German I. Parisi et al.  
Year: 2019  
Venue: Neural Networks  
URL/DOI: https://doi.org/10.1016/j.neunet.2019.01.012  
Why relevant: Continual-learning survey.  
Where to cite: Continual learning.

[vanDeVenTolias2019]  
Full title: Three scenarios for continual learning  
Authors: Gido M. van de Ven; Andreas S. Tolias  
Year: 2019  
Venue: NeurIPS Continual Learning workshop / arXiv  
URL/DOI: https://arxiv.org/abs/1904.07734  
Why relevant: Task/domain/class-incremental distinctions.  
Where to cite: Continual learning framing.

[Jacobs1991]  
Full title: Adaptive mixtures of local experts  
Authors: Robert A. Jacobs; Michael I. Jordan; Steven J. Nowlan; Geoffrey E. Hinton  
Year: 1991  
Venue: Neural Computation  
URL/DOI: https://doi.org/10.1162/neco.1991.3.1.79  
Why relevant: Gating and modular expert selection.  
Where to cite: Context, gating, modularity.

[JordanJacobs1994]  
Full title: Hierarchical mixtures of experts and the EM algorithm  
Authors: Michael I. Jordan; Robert A. Jacobs  
Year: 1994  
Venue: Neural Computation  
URL/DOI: https://doi.org/10.1162/neco.1994.6.2.181  
Why relevant: Hierarchical gating/modular computation.  
Where to cite: Context, gating, modularity.

[Shazeer2017]  
Full title: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer  
Authors: Noam Shazeer et al.  
Year: 2017  
Venue: ICLR  
URL/DOI: https://arxiv.org/abs/1701.06538  
Why relevant: Modern sparse MoE routing.  
Where to cite: Context/gating/modularity.

[GershmanNiv2010]  
Full title: Learning latent structure: carving nature at its joints  
Authors: Samuel J. Gershman; Yael Niv  
Year: 2010  
Venue: Current Opinion in Neurobiology  
URL/DOI: verify DOI  
Why relevant: Latent causes/context inference in cognition.  
Where to cite: Context and latent task inference.

[Gershman2017]  
Full title: Context-dependent learning and causal structure  
Authors: Samuel J. Gershman and related work  
Year: verify exact paper/year  
Venue: verify  
URL/DOI: verify  
Why relevant: Latent-cause/context framing; requires final source verification.  
Where to cite: Context and latent task inference if retained.

[Scarselli2009]  
Full title: The Graph Neural Network Model  
Authors: Franco Scarselli et al.  
Year: 2009  
Venue: IEEE Transactions on Neural Networks  
URL/DOI: https://doi.org/10.1109/TNN.2008.2005605  
Why relevant: Early graph neural network formulation.  
Where to cite: Graph/path reasoning.

[Li2016]  
Full title: Gated Graph Sequence Neural Networks  
Authors: Yujia Li; Daniel Tarlow; Marc Brockschmidt; Richard Zemel  
Year: 2016  
Venue: ICLR  
URL/DOI: https://arxiv.org/abs/1511.05493  
Why relevant: Recurrent message passing over graph structure.  
Where to cite: Graph/path reasoning.

[Battaglia2018]  
Full title: Relational inductive biases, deep learning, and graph networks  
Authors: Peter W. Battaglia et al.  
Year: 2018  
Venue: arXiv  
URL/DOI: https://arxiv.org/abs/1806.01261  
Why relevant: Graph networks and relational reasoning.  
Where to cite: Graph/path reasoning.

[Vinyals2015]  
Full title: Pointer Networks  
Authors: Oriol Vinyals; Meire Fortunato; Navdeep Jaitly  
Year: 2015  
Venue: NeurIPS  
URL/DOI: https://arxiv.org/abs/1506.03134  
Why relevant: Neural algorithmic sequence/path-like outputs.  
Where to cite: Algorithmic reasoning.

[LakeBaroni2018]  
Full title: Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks  
Authors: Brenden M. Lake; Marco Baroni  
Year: 2018  
Venue: ICML  
URL/DOI: https://proceedings.mlr.press/v80/lake18a.html  
Why relevant: Compositional generalization benchmark framing.  
Where to cite: Compositional route execution.

[Keysers2020]  
Full title: Measuring compositional generalization: A comprehensive method on realistic data  
Authors: Daniel Keysers et al.  
Year: 2020  
Venue: ICLR  
URL/DOI: https://arxiv.org/abs/1912.09713  
Why relevant: Compositional generalization evaluation.  
Where to cite: Compositional route execution.

[Hupkes2020]  
Full title: Compositionality Decomposed: How do Neural Networks Generalise?  
Authors: Dieuwke Hupkes et al.  
Year: 2020  
Venue: Journal of Artificial Intelligence Research  
URL/DOI: https://doi.org/10.1613/jair.1.11674  
Why relevant: Decomposes compositional generalization concepts.  
Where to cite: Compositional route execution.

[OkeefeNadel1978]  
Full title: *The Hippocampus as a Cognitive Map*  
Authors: John O'Keefe; Lynn Nadel  
Year: 1978  
Venue: Oxford University Press  
URL/DOI: book; verify final bibliographic details  
Why relevant: Cognitive map framing.  
Where to cite: Neuroscience motivation.

[Tolman1948]  
Full title: Cognitive maps in rats and men  
Authors: Edward C. Tolman  
Year: 1948  
Venue: Psychological Review  
URL/DOI: https://doi.org/10.1037/h0061626  
Why relevant: Cognitive maps and latent spatial structure.  
Where to cite: Neuroscience/cognitive background.

[TeylerDiScenna1986]  
Full title: The hippocampal memory indexing theory  
Authors: Timothy J. Teyler; Paul DiScenna  
Year: 1986  
Venue: Behavioral Neuroscience  
URL/DOI: verify DOI  
Why relevant: Hippocampal indexing theory.  
Where to cite: Neuroscience motivation.

[TeylerRudy2007]  
Full title: The hippocampal indexing theory and episodic memory: updating the index  
Authors: Timothy J. Teyler; Jerry W. Rudy  
Year: 2007  
Venue: Hippocampus  
URL/DOI: verify DOI  
Why relevant: Updated indexing theory.  
Where to cite: Neuroscience motivation.

[McClelland1995]  
Full title: Why there are complementary learning systems in the hippocampus and neocortex: insights from the successes and failures of connectionist models of learning and memory  
Authors: James L. McClelland; Bruce L. McNaughton; Randall C. O'Reilly  
Year: 1995  
Venue: Psychological Review  
URL/DOI: https://doi.org/10.1037/0033-295X.102.3.419  
Why relevant: Complementary learning systems, catastrophic interference, consolidation.  
Where to cite: Introduction; neuroscience; continual learning.

[NormanOReilly2003]  
Full title: Modeling hippocampal and neocortical contributions to recognition memory: a complementary-learning-systems approach  
Authors: Kenneth A. Norman; Randall C. O'Reilly  
Year: 2003  
Venue: Psychological Review  
URL/DOI: https://doi.org/10.1037/0033-295X.110.4.611  
Why relevant: Pattern separation/completion and hippocampal memory.  
Where to cite: Neuroscience motivation.

[Kumaran2016]  
Full title: What learning systems do intelligent agents need? Complementary learning systems theory updated  
Authors: Dharshan Kumaran; Demis Hassabis; James L. McClelland  
Year: 2016  
Venue: Trends in Cognitive Sciences  
URL/DOI: verify DOI  
Why relevant: Updated CLS theory.  
Where to cite: Neuroscience/continual learning.

[Eichenbaum2017]  
Full title: The role of the hippocampus in navigation is memory  
Authors: Howard Eichenbaum  
Year: 2017  
Venue: Journal of Neurophysiology / verify exact venue  
URL/DOI: verify  
Why relevant: Hippocampus, memory, navigation/cognitive maps.  
Where to cite: Neuroscience motivation.

[Rolls2013]  
Full title: The mechanisms for pattern completion and pattern separation in the hippocampus  
Authors: Edmund T. Rolls  
Year: 2013  
Venue: Frontiers in Systems Neuroscience  
URL/DOI: verify DOI  
Why relevant: Pattern separation/completion mechanisms.  
Where to cite: Neuroscience motivation.

[Chklovskii2004]  
Full title: Cortical rewiring and information storage  
Authors: Dmitri B. Chklovskii; Bartlett W. Mel; Karel Svoboda  
Year: 2004  
Venue: Nature  
URL/DOI: https://doi.org/10.1038/nature03012  
Why relevant: Structural plasticity and memory storage.  
Where to cite: Neuroscience motivation.

[HoltmaatSvoboda2009]  
Full title: Experience-dependent structural synaptic plasticity in the mammalian brain  
Authors: Anthony Holtmaat; Karel Svoboda  
Year: 2009  
Venue: Nature Reviews Neuroscience  
URL/DOI: verify DOI  
Why relevant: Structural synaptic plasticity review.  
Where to cite: Neuroscience motivation.

[Dudai2004]  
Full title: The neurobiology of consolidations, or, how stable is the engram?  
Authors: Yadin Dudai  
Year: 2004  
Venue: Annual Review of Psychology  
URL/DOI: verify DOI  
Why relevant: Consolidation/reconsolidation background.  
Where to cite: Consolidation discussion.

[Velickovic2020]  
Full title: Neural execution of graph algorithms  
Authors: Petar Veličković et al.  
Year: 2020  
Venue: ICLR  
URL/DOI: https://arxiv.org/abs/1910.10593  
Why relevant: Neural graph algorithm execution; useful contrast to symbolic route execution.  
Where to cite: Graph/path reasoning.

[TODO_REVIEW_RECENT_WORK_2025_2026]  
Full title: Recent work on task inference, memory-augmented continual learning, modular routing, and neural algorithmic reasoning after the current local knowledge cutoff  
Authors: [TODO]  
Year: 2025-2026  
Venue: [TODO]  
URL/DOI: [TODO]  
Why relevant: Required before submission to avoid stale prior-art positioning.  
Where to cite: Related work and positioning.

---

## Drafting notes and blockers

### Structural manuscript risks

- The paper can sound like a general continual-learning or biological memory claim if the introduction is too ambitious.
- The clean supplied-context result is not enough because an oracle context-gated table matches CIRM on the clean benchmark.
- Exp14 makes the story stronger but must remain framed as symbolic transition-cue selection.
- The manuscript currently leans on internal ablations and symbolic/algorithmic controls; full neural baselines are absent.

### Evidence gaps

- Neural baselines are absent.
- Prior-art/novelty import is missing as a local artifact.
- Seed-level confidence intervals and effect-size groupings need human review.
- Exp11 and Exp12 historical runs lack current validation JSON/SQLite manifests.
- C9 seen/unseen primitive claims need metric cleanup.
- Exp13.1 lesion diagnostic failed expected pattern and cannot support a positive lesion claim.

### Literature gaps

- Need a current literature search for 2025-2026 work on memory-augmented continual learning, task inference, modular routing, latent context inference, and neural algorithmic reasoning.
- Need exact verification of several citation DOIs and venues.
- Need a prior-art risk section comparing CIRM to:
  - task-conditioned lookup tables;
  - oracle task masks;
  - mixture-of-experts/context gating;
  - differentiable key-value memory;
  - neural graph/path execution;
  - fast-weight or plastic recurrent networks.

### Figure/table gaps

- Figures 1-5 are generated candidate assets but require human caption review.
- Figure 4 local-vs-global budget claim requires paired seed-level comparison if central.
- Figure 5 Exp14 placement remains main-vs-supplement unresolved.
- No neural/prior-art baseline figure exists.
- Consolidation, primitive-boundary, and lesion figures should not be main in the current manuscript.

### Claims that may need narrowing

- C2 should be split into supplied context indexing versus symbolic cue-selected context.
- C5 should remain "through tested world counts" and "ceiling-limited"; no fitted capacity law.
- C6 should remain an observed degradation curve; no formal law.
- C7 should be supplementary/narrow until paired seed-level analysis exists.
- C8 should remain supplementary/preliminary.
- C9 should be excluded from main claims until metric cleanup.
- C10 should be wrong-world/cue-evidence sensitivity, not generic robustness.
- C11 should be future work/preliminary bridge only.
- C13 should be symbolic transition-cue selection, not autonomous perceptual world discovery.

### Possible reviewer objections

1. "This is just task-gated lookup."  
   Current answer: The clean supplied-context upper bound is acknowledged. The contribution is the decomposition of storage, recurrence, suffix composition, finite budget, and symbolic cue-selected context. Required fix: sharpen prior-art positioning and avoid novelty claims for context gating alone.

2. "There are no neural baselines."  
   Current answer: Correct. Exp13.2 contains symbolic/algorithmic baselines only. Required fix: decide venue; add neural baselines for stronger ML submission.

3. "The latent context claim is overclaimed."  
   Current answer: Exp14 uses symbolic transition cues only, and the oracle remains an upper bound. Required fix: keep language narrow and add final figure captions that state this clearly.

4. "Capacity scaling is trivial because it is ceiling performance."  
   Current answer: C5 is paired with finite-budget degradation C6. Required fix: do not claim a law; include failure/budget boundary.

5. "Generalization is overstated."  
   Current answer: The manuscript claims composition over stored primitives, not unseen primitive inference. Required fix: keep C9 out of main or clean metrics.

6. "Biological language is too strong."  
   Current answer: Biological concepts are motivation only. Required fix: tighten introduction and discussion if any phrase implies proof.

7. "Figures are generated but not final."  
   Current answer: V0 uses candidate callouts only. Required fix: human-review final figure scripts, captions, source data, and journal formatting.

### Conditional Experiment 15 decision

Required before V0? **No.**

Required before submission? **Maybe.**

Why: For a controlled symbolic/mechanistic manuscript, Exp13.2 provides enough symbolic/algorithmic baseline coverage to draft the first paper honestly, as long as the manuscript states that neural baselines are absent. For a stronger ML venue or any claim that CIRM improves over ordinary neural sequence models, a neural baseline suite is required.

Which claims would it affect:

- C12 baseline/prior-art readiness directly.
- C1-C4 if reviewers demand neural comparisons for mechanism necessity.
- C13 if claiming context selection is better than neural latent-task inference methods.
- C5-C7 if claiming scaling advantages over neural alternatives.

Minimal design if required:

Experiment 15: Minimal Neural Baseline Comparator

Purpose: Test whether ordinary neural sequence models trained under comparable symbolic route-memory conditions exhibit the same retention/composition behavior, interference failure modes, and context sensitivity.

Minimal variants:

- GRU/RNN sequence executor;
- small Transformer sequence model;
- optionally MLP/context-conditioned table as a non-recurrent neural-ish baseline.

Metrics:

- seen-route composition;
- suffix-route composition;
- first-step context conflict accuracy;
- retention after sequential worlds;
- route length scaling;
- world count scaling;
- seed-level confidence intervals;
- training compute/runtime.

Recommendation: Do not block V0. Before submission, decide target venue. If targeting arXiv, a workshop, or a specialized mechanism-focused venue, proceed with the current manuscript and explicitly scope out neural baselines. If targeting a stronger ML venue, run Experiment 15 before submission.

---

## V1 quality check

- Every main empirical claim remains mapped to the claim freeze and local evidence paths.
- C13/Exp14 is framed narrowly as symbolic transition-cue selection.
- Oracle context-gated lookup is treated as an upper bound, not a defeated baseline.
- Neural baseline absence is explicit.
- Biological language is motivational, not evidentiary.
- Generated figures are called out only where the asset manifest says they exist.
- C8/C9/C10/C11 and lesion diagnostics are kept supplementary, future-work, or limitations.
- Open TODOs are explicit.
- The V1 manuscript does not claim solved continual learning, end-to-end perception, broad biological proof, or broad neural-network superiority.
