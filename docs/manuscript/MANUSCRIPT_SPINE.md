# Manuscript Spine

Purpose: Define the provisional structure of the first manuscript and keep every section tied to explicit evidence rather than thread memory.

Status: refreshed after Exp13.2, Exp14, Exp15, and `MANUSCRIPT_V2.md` capture. This is a scaffold and navigation aid; the active prose draft is `docs/manuscript/draft/MANUSCRIPT_V2.md`.

## Working title

Current V2 working title:

- Context-Indexed Structural Route Memory for Compositional Recall in Interfering Transition Systems

Conservative alternatives:

- Storage, Context, and Execution in a Synthetic Route-Memory Benchmark
- Context-Indexed Route Memory Separates Storage and Execution under Transition Interference
- Recurrent Route Execution over Context-Indexed Transition Memory
- A Controlled Benchmark for Structural Route Memory, Context Selection, and Compositional Recall

## One-sentence contribution

In a controlled symbolic route-memory benchmark, the project separates context-indexed transition storage, recurrent execution, endpoint memorization, symbolic context selection, finite-capacity pressure, and minimal neural comparator behavior under incompatible transition systems.

## Provisional abstract skeleton

- Problem: route-memory tasks can require multiple incompatible transition systems over the same state/action space.
- Gap: aggregate endpoint accuracy can hide whether a system learned reusable one-step transitions, memorized endpoints, selected context, or recurrently composed transitions.
- Method: benchmark context-indexed route memory with supplied-context experiments, symbolic transition-cue context selection, symbolic/algorithmic baselines, and minimal fixed-profile neural comparators.
- Key result: internal CIRM-family ablations support a benchmark-specific storage/context/recurrence decomposition; Exp13.2 shows oracle context-gated lookup matches the clean supplied-context benchmark; Exp14 shows symbolic transition cues can select active context; Exp15 shows context-conditioned transition MLP and world-head transition MLP variants solve the clean hard slice while endpoint neural variants expose endpoint-vs-composition dissociations.
- Boundary/limitation: no solved continual learning, no broad CIRM-over-neural-model claim, no raw sensory latent-world discovery, no end-to-end perception, no biological validation, and no general conclusion from Exp15 replay collapse without audit.
- Contribution: a conservative benchmark and evidence map for studying route-memory mechanisms under symbolic contextual interference.

## Main claim

Claim: A synthetic compositional route-memory benchmark separates storage, context indexing, recurrence, endpoint memorization, finite-capacity pressure, symbolic context selection, and minimal neural transition-learning baselines under interfering transition systems.

Evidence: C1-C7, C12, and C13 in the central evidence map are supported by Exp11, Exp12, Exp13, Exp13.1, Exp13.2, Exp14, and Exp15 artifacts.

Caveat: This is a controlled symbolic/mechanistic benchmark. Exp15 explicitly rules out broad neural-superiority wording because context-conditioned transition MLP and world-head transition MLP variants solve the clean hard slice. Prior-art import, retained-claim CI/effect-size review, final figure/table approval, command verification, and license/citation metadata remain pending.

Source path: `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md`.

## Non-claims

- The manuscript should not claim solved continual learning.
- The manuscript should not claim context gating is novel by itself.
- The manuscript should not claim broad CIRM superiority over neural models.
- The manuscript should not claim a complete hippocampal or biological theory.
- The manuscript should not claim raw sensory latent-world discovery.
- The manuscript should not claim end-to-end perceptual learning.
- The manuscript should not claim broad abstract rule induction.
- The manuscript should not claim inference of unseen primitive transitions.
- The manuscript should not cite Exp15 replay collapse as scientific evidence unless audited.

## Section outline

| Section | Purpose | Key claims | Source docs/artifacts | Caveats | Missing work |
|---|---|---|---|---|---|
| 1. Introduction | Motivate interfering symbolic route-memory systems and the need for mechanism-sensitive evaluation. | Benchmark-specific route-memory problem; narrow contribution. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Do not imply broad continual-learning solution or neural superiority. | Final polish after retained-claim/statistical hardening. |
| 2. Related work / positioning | Position context gating, recurrence, structural plasticity, replay, masks, memory-augmented systems, and cognitive maps without inventing novelty. | C12: baselines and prior art are required. | `docs/theory/PRIOR_ART_MAP.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | Novelty assessment artifact is local verification pending. | Import novelty assessment and add verified citations/BibTeX. |
| 3. Benchmark: route memory under contextual interference | Define worlds, nodes, modes, one-step transitions, route execution, suffix probes, first-step conflict, and retention. | Benchmark separates storage, context, endpoint memorization, and execution. | `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`; `experiments/experiment13_breaking_point/README.md`; `experiments/experiment15_neural_baseline_comparator/README.md` | Synthetic symbolic benchmark. | Final notation cleanup. |
| 4. Model and mechanism | Describe context-indexed structural route memory, recurrent execution, supplied context, and symbolic cue-selected context. | C1-C4 and C13 mechanism decomposition. | `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/theory/CORE_THEORY.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` | Mechanism description must not become biological proof or universal neural claim. | Final method diagrams and implementation summary. |
| 5. Experimental regime | Explain Exp11-Exp15 roles, seeds, profiles, outputs, and validation. | Evidence organized by incompatible worlds, scaling, boundary mapping, baselines, symbolic context selection, and neural comparators. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `docs/experiments/EXPERIMENT_REGISTRY.md`; `docs/experiments/exp15_summary.md` | Commands inspected/imported historically; fresh command verification pending. | Fresh command verification and runtime documentation. |
| 6. Results: storage/context/recurrence decomposition | Present core ablations and route-table/composition dissociation. | C1-C4. | `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png` | Benchmark-specific; not universal structural-plasticity proof. | CI/effect-size review and final captions. |
| 7. Results: capacity and boundary mapping | Present clean scaling, finite structural budget degradation, and local/global pressure if retained. | C5-C7. | `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` | No fitted capacity law; local/global paired analysis still pending. | Retained-claim statistical hardening. |
| 8. Results: symbolic context selection | Present Exp14 as symbolic transition-cue context selection. | C13, C2/C10 caveats. | `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`; `docs/threads/experiment14_analysis_digest.md`; candidate Figure 5 assets | Not raw sensory latent-world discovery; oracle context-gated table remains upper bound. | Decide main vs supplement and finalize caption/source data. |
| 9. Results: symbolic and neural baselines | Present Exp13.2 symbolic/algorithmic baselines and Exp15 minimal neural comparator table. | C12 plus C1/C2/C4 narrowing. | `docs/experiments/exp13_2_summary.md`; `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md`; `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`; `docs/manuscript/tables/table_04_exp15_neural_comparator.md` | Exp15 is fixed-profile and non-exhaustive; no memory-augmented/key-value neural baseline. | Decide whether target venue requires optional successor neural baseline. |
| 10. Limitations | State reviewer-risk boundaries clearly. | Non-claims; symbolic benchmark; oracle context; minimal neural comparator; no end-to-end perception; failed lesion diagnostic. | `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/synthesis/PUBLICATION_READINESS.md`; `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` | Must remain explicit in abstract and discussion. | Update after retained-claim decisions. |
| 11. Discussion | Interpret mechanism decomposition, failure modes, baseline implications, and future scope. | Narrow contribution plus failure map. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/FIGURE_PLAN.md`; `docs/synthesis/NEXT_EXPERIMENTS.md` | Avoid strengthening beyond evidence. | Final polish after statistics and citations. |
| 12. Future work | Define optional memory-augmented neural baseline, replay audit, lesion audit, stochastic corruption, applied bridge, and richer context inference. | Future directions only. | `docs/synthesis/NEXT_EXPERIMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`; `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md` | Future work is not evidence. | Prioritize only after retained-claim/statistical hardening. |

## Results storyboard

| Figure/table | Story role | Source path | Current status | Caveat |
|---|---|---|---|---|
| Figure 1 conceptual architecture/task | Define benchmark, context index, one-step route table, and recurrent execution. | `docs/manuscript/figures/figure_01_conceptual_route_memory.png`; `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv` | Generated candidate schematic. | Conceptual only; not empirical evidence. |
| Figure 2 ablations/core mechanism | Show structural storage, context indexing, and recurrence as separable internal components. | `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png`; `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv` | Generated candidate main figure. | Internal symbolic ablation; uncertainty/effect-size review pending. |
| Figure 3 clean capacity scaling | Show clean supplied-context scaling through tested world counts. | `docs/manuscript/figures/figure_03_capacity_scaling.png`; `docs/manuscript/source_data/figure_03_capacity_scaling.csv` | Generated candidate main figure. | Ceiling-limited; no fitted capacity law. |
| Figure 4 finite budget/local-global pressure | Show observed finite-budget degradation and possible local/global pressure difference. | `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png`; `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv` | Generated candidate narrow-main/supplement figure. | Paired seed-level local/global inference remains deferred. |
| Figure 5 symbolic context selection | Show Exp14 symbolic transition-cue context selection. | `docs/manuscript/figures/figure_05_symbolic_context_selection.png`; `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv` | Generated candidate main-or-supplement figure. | Symbolic cues only; oracle upper bound remains. |
| Table 1 claim evidence | Compact evidence map for retained claims. | `docs/manuscript/tables/table_01_claim_evidence.md` | Generated candidate table. | Needs final retained-claim review. |
| Table 2 run integrity | Provenance summary for manuscript-relevant runs. | `docs/manuscript/tables/table_02_run_integrity.md` | Generated candidate table. | Older runs lack uniform manifests. |
| Table 3 statistical summary | Statistical source table for figure/baseline claims. | `docs/manuscript/tables/table_03_statistical_summary.md` | Present but needs hardening. | Effect-size grouping and retained-claim mapping need review. |
| Table 4 Exp15 neural comparator | Minimal neural hard-slice comparator table. | `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` | Present for V2. | Fixed-profile comparator; replay row not interpreted without audit. |

## Submission blockers

- Retained main-claim decision after V2 and post-Exp15 narrowing.
- Manuscript-grade seed-level confidence intervals and effect sizes.
- Human review of generated candidate figures/tables and captions.
- Final source-data manifests for every retained panel/table.
- Prior-art/novelty import and verified citations/BibTeX.
- Fresh command verification with runtime/hardware logs.
- License and citation metadata.
- Optional venue-dependent decisions: memory-augmented neural baseline, Exp15 replay audit, Exp13.1 lesion audit, C9 metric cleanup, stochastic context corruption, consolidation dose-response, or non-symbolic applied bridge.
