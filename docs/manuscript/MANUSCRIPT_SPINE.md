# Manuscript Spine

Purpose: Define the provisional structure of the first manuscript and keep every section tied to explicit evidence rather than thread memory.

## Working title

Conservative title options:

- Context-Indexed Structural Plasticity for Continual Compositional Route Memory
- Context-Indexed Route Memory in a Continual Compositional Benchmark

## One-sentence contribution

In a controlled symbolic route-memory benchmark, context-indexed structural plasticity stores incompatible local transition systems while recurrent execution composes stored one-step transitions into multi-step routes.

## Provisional abstract skeleton

- Problem: continual route-memory tasks require multiple incompatible transition systems to be retained over the same state/action space.
- Gap: internal ablations alone do not establish broad continual-learning novelty, but they can isolate storage, context selection, recurrence, capacity, and primitive-holdout failure modes.
- Method: benchmark context-indexed structural route memory with recurrent execution across Exp11-Exp13 and planned Exp13.1 hardening.
- Key result: internal evidence supports non-destructive benchmark-specific storage under clean context and a route-table/composition dissociation when recurrence is removed.
- Boundary/limitation: the model does not infer unseen primitive transitions, does not learn perception end to end, and still needs baselines, confidence intervals, and final figure regeneration.
- Contribution: a conservative benchmark and evidence map for studying context-indexed structural route memory under continual compositional pressure.

## Main claim

Claim: A synthetic continual compositional route-memory benchmark shows that context-indexed structural plasticity can store incompatible local transition systems without destructive overwriting, while recurrent dynamics are required to convert one-step route memories into multi-step execution.

Evidence: C1-C5 in the central evidence map are supported by Exp8/Exp11/Exp12/Exp13 internal ablation and capacity artifacts.
Caveat: External baselines, statistical hardening, Exp13.1 metric cleanup, and prior-art source import remain pending.
Source path: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`

## Non-claims

- The manuscript should not claim solved continual learning.
- The manuscript should not claim context gating is novel by itself.
- The manuscript should not claim a complete hippocampal or biological theory.
- The manuscript should not claim end-to-end perceptual learning.
- The manuscript should not claim broad abstract rule induction.
- The manuscript should not claim inference of unseen primitive transitions.

## Section outline

| Section | Purpose | Key claims | Source docs/artifacts | Caveats | Missing work |
|---|---|---|---|---|---|
| 1. Introduction | Motivate continual compositional route memory and the need for careful evidence boundaries. | Benchmark-specific route-memory problem; narrow contribution. | `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Do not imply broad continual-learning solution. | Final framing after baselines and prior-art import. |
| 2. Related work / positioning | Position context gating, recurrence, structural plasticity, replay, masks, and cognitive maps without inventing novelty. | C12: baselines and prior art are required. | `docs/manuscript/NOVELTY_POSITIONING.md`; `docs/theory/PRIOR_ART_MAP.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md` | Novelty assessment artifact is local verification pending. | Import novelty assessment and add actual citations. |
| 3. Benchmark: Continual Compositional Route Memory | Define worlds, nodes, modes, one-step transitions, held-out routes, and incompatibility. | Route-memory benchmark separates storage, context, and execution. | `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`; `experiments/experiment13_breaking_point/README.md` | Synthetic symbolic benchmark. | Clean benchmark spec and final notation. |
| 4. Model: context-indexed structural plasticity and recurrent execution | Describe mechanism components and ablation dimensions. | C1-C4 mechanism decomposition. | `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/theory/CORE_THEORY.md` | Mechanism description must not become biological proof. | Final method diagrams and implementation summary. |
| 5. Experimental regime | Explain Exp11-Exp13 roles, seeds, profiles, outputs, and validation. | Internal evidence is organized by incompatible worlds, scaling, and boundary mapping. | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`; `docs/experiments/EXPERIMENT_REGISTRY.md` | Commands inspected but not executed in P1. | Smoke/full command verification and runtime documentation. |
| 6. Results | Present core ablations, capacity, retention, and route-table/composition dissociation. | C1-C5 with conservative wording. | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Internal ablations only. | Confidence intervals, effect sizes, and final figures. |
| 7. Boundary mapping and failure modes | Show finite capacity, context corruption, holdout boundary, and continuous bridge. | C6-C11 as promising/preliminary boundary claims. | `experiments/experiment13_breaking_point/analysis/validation_report.md`; `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`; `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv` | Exp13 needs metric cleanup and stochastic corruption. | Exp13.1. |
| 8. Baselines and comparisons | Compare against simpler and external alternatives. | C12; planned baseline suite. | `docs/manuscript/BASELINE_REQUIREMENTS.md` | Planning document only; no baseline results yet. | Implement baseline suite and add baseline results artifacts. |
| 9. Biological framing | Keep indexing/remapping/recurrent/structural-plasticity language as computational inspiration. | Biological framing is limited and caveated. | `docs/theory/BIOLOGICAL_FRAMING.md`; `docs/manuscript/LIMITATIONS_AND_THREATS.md` | No complete hippocampal theory. | Prior-art citations and careful discussion language. |
| 10. Limitations | State reviewer-risk boundaries clearly. | Non-claims; symbolic benchmark; oracle context; no end-to-end perception. | `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/synthesis/PUBLICATION_READINESS.md` | Must remain explicit in abstract and discussion. | Update after baselines and Exp13.1. |
| 11. Discussion | Interpret mechanism conjunction, failure modes, and why boundaries matter. | Narrow contribution plus failure map. | `docs/manuscript/RESULTS_STORYBOARD.md`; `docs/manuscript/FIGURE_PLAN.md` | Avoid strengthening beyond evidence. | Draft after final figures and baselines. |
| 12. Future work | Define latent context inference, applied visual-state bridge, scaling, and richer tasks. | Future directions only. | `docs/synthesis/NEXT_EXPERIMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md` | Future work is not evidence. | Prioritize after Exp13.1 and baselines. |

## Results storyboard

| Figure | Story role | Source path | Current status | Caveat |
|---|---|---|---|---|
| Figure 1 conceptual architecture/task | Define benchmark, context index, one-step route table, and recurrent execution. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md` | Framing. | Must not imply biological completeness or latent-world inference. |
| Figure 2 ablations/core mechanism | Show structural plasticity, world context, and recurrence as separable internal components. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png` | Strong internal evidence. | Needs external baselines. |
| Figure 3 capacity/retention | Show Exp12 clean-context scaling and retention before failure pressure. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv` | Strong but ceiling-limited. | Needs uncertainty reporting. |
| Figure 4 breaking point | Show Exp13 global/local finite-budget degradation. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv` | Promising. | Needs Exp13.1 capacity-law and paired local/global cleanup. |
| Figure 5 consolidation | Present consolidation as stability/plasticity bias. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment13_breaking_point/analysis/validation_report.md` | Preliminary. | Dose-response pending. |
| Figure 6 held-out composition boundary | Separate composition over stored primitives from unseen primitive-transition inference. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv` | Needs metric cleanup. | Seen/unseen route-table splits pending. |
| Figure 7 context corruption | Show context-selection failure under adversarial corruption. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv` | Promising. | Stochastic graded corruption pending. |
| Figure 8 continuous bridge / supplement | Show noisy continuous decoding feeding route memory. | `docs/manuscript/FIGURE_PLAN.md`; `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv` | Preliminary or supplementary. | Not end-to-end perception. |

## Submission blockers

- Exp13.1 publication-hardening audit.
- External baseline suite.
- Seed-level confidence intervals and effect sizes.
- Final reproducible figures and source-data manifests.
- Novelty assessment import.
- Prior-art citations and positioning.
- Verified smoke/standard/full or validation/full commands for manuscript-critical experiments.
