# Glossary

Purpose: Standardize terminology across experiments, manuscript drafts, and thread digests. These are project-local working definitions unless a later prior-art pass documents broader usage.

## Context-indexed route memory

Definition: A route-memory mechanism where stored transitions are selected by a context or world index as well as by state and action/mode.
Plain-language interpretation: The same action can point somewhere different in different worlds, and the model uses context to choose the right stored route.
Manuscript usage: Use for the narrow benchmark mechanism tested most directly in Exp11-Exp13.
Caveat: Current evidence uses supplied or oracle context labels; latent world inference remains future work.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`

## Continual compositional route memory

Definition: A benchmark family where a system learns route transitions over time and must execute multi-step routes by composing stored one-step transitions.
Plain-language interpretation: The system keeps learning route worlds, then has to follow several stored steps in sequence.
Manuscript usage: Use for the task setting, not as a claim that broad continual learning is solved.
Caveat: The current benchmark is synthetic and symbolic.
Related docs: `README.md`; `docs/manuscript/MANUSCRIPT_SPINE.md`; `docs/synthesis/PUBLICATION_READINESS.md`

## World

Definition: A route system with its own transition semantics over the shared state/action or node/mode space.
Plain-language interpretation: World A and world B can reuse the same states and actions but require different next states.
Manuscript usage: Use when discussing incompatible route systems in Exp11-Exp13.
Caveat: Worlds are supplied benchmark conditions, not inferred environments.
Related docs: `experiments/experiment11_context_memory/EXPERIMENT_11_CONTEXT_MEMORY.md`; `experiments/experiment12_capacity_generalization/README.md`

## Context

Definition: The input signal or label used to select the intended world or route memory.
Plain-language interpretation: Context tells the model which version of the route table to use.
Manuscript usage: Use interchangeably with world context only when the surrounding experiment uses supplied world labels.
Caveat: Context signals are mostly oracle labels in the current evidence.
Related docs: `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/synthesis/NEXT_EXPERIMENTS.md`

## World/context indexing

Definition: Conditioning route storage or retrieval on a world/context identifier.
Plain-language interpretation: The model keeps incompatible memories apart by indexing them under different contexts.
Manuscript usage: Use for C2-style retention and interference claims.
Caveat: Do not claim the indexing method is novel by itself; external baselines and prior-art citations are pending.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`

## Route field

Definition: The learned or supplied set of local route preferences linking a source state and action/mode to a target state.
Plain-language interpretation: A map of "from here, under this action, go there" entries.
Manuscript usage: Use in mechanism descriptions and Exp7/Exp8 route-field diagnostics.
Caveat: The term is project-local; avoid implying a standard biological construct.
Related docs: `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_summary.csv`; `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`

## Route table

Definition: A direct tabular or summary view of the one-step route memories available to the model.
Plain-language interpretation: The stored one-step answers before asking the model to run a multi-step route.
Manuscript usage: Use when separating storage accuracy from recurrent execution accuracy.
Caveat: A perfect route table does not imply successful multi-step composition without recurrence.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png`

## Structural plasticity

Definition: The ability of the route-memory substrate to form, select, or modify discrete route-supporting connections or edges.
Plain-language interpretation: The model can create or change the structure that stores routes, rather than only adjusting a fixed readout.
Manuscript usage: Use for internal ablations where no-structural-plasticity variants fail route-table formation.
Caveat: Current evidence supports a benchmark-specific mechanism claim, not a biological necessity claim.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`

## Recurrent execution

Definition: Repeated application of stored one-step transitions to execute a multi-step route.
Plain-language interpretation: The system follows the route one hop at a time.
Manuscript usage: Use for the storage/execution dissociation in no-recurrence ablations.
Caveat: Recurrence itself is not claimed as novel.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`

## Route-table accuracy

Definition: Accuracy of direct one-step route memory, usually measured before or separately from multi-step execution.
Plain-language interpretation: Whether the stored local route entries are correct.
Manuscript usage: Use with composition accuracy to show storage/execution separation.
Caveat: Metric names differ across generated summaries; verify the exact column before citing.
Related docs: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`

## Composition accuracy

Definition: Accuracy on multi-step route execution after composing one-step transitions.
Plain-language interpretation: Whether the model gets the final destination right after several route steps.
Manuscript usage: Use for the main route execution outcome in Exp7-Exp13.
Caveat: For holdout settings, distinguish routes over seen primitives from routes requiring unseen primitive transitions.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`

## Composition-route gap

Definition: The gap between route-table accuracy and composition accuracy.
Plain-language interpretation: The model may know the one-step entries but fail to execute the route over multiple steps.
Manuscript usage: Use for C3/C4 evidence and recurrence ablation figures.
Caveat: The gap is diagnostic, not by itself a full explanation of the failure mode.
Related docs: `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_route_table_composition_gap.png`; `docs/manuscript/FIGURE_PLAN.md`

## Wrong-world activation

Definition: Activation, selection, or support assigned to a world/context other than the intended one.
Plain-language interpretation: The model is being pulled toward the wrong memory.
Manuscript usage: Use as a context-selection diagnostic in Exp11/Exp12 and boundary evidence in Exp13.
Caveat: Exp11/Exp12 wrong-world diagnostics are not the same as completed stochastic corruption evidence.
Related docs: `experiments/experiment11_context_memory/analysis/exp11/exp11_context_dropout_wrong_world_activation.png`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`

## World margin

Definition: A margin metric comparing support for the correct world against competing worlds.
Plain-language interpretation: How clearly the model prefers the right world.
Manuscript usage: Use in context-corruption and context-noise diagnostics.
Caveat: A positive margin is useful evidence for selection, but downstream composition still needs to be checked.
Related docs: `experiments/experiment13_breaking_point/analysis/plots/exp13_context_adversarial_mixture_world_margin.png`; `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`

## Context bleed

Definition: A diagnostic condition where information from an incorrect context is blended into the context signal.
Plain-language interpretation: The context cue is contaminated by another world.
Manuscript usage: Use for Exp8/Exp9/Exp11/Exp12 stress diagnostics.
Caveat: Prior context-bleed sweeps are not sufficient for the final context-robustness claim; Exp13.1 stochastic corruption remains planned.
Related docs: `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_composition_by_bleed.png`

## Context dropout

Definition: A diagnostic condition where part of the context signal is removed or weakened.
Plain-language interpretation: The model gets less context information than normal.
Manuscript usage: Use as supplementary context-selection diagnostics.
Caveat: Current dropout artifacts should not be overstated as realistic context-noise robustness.
Related docs: `experiments/experiment12_capacity_generalization/analysis/exp12/plots/exp12_context_dropout_composition.png`; `docs/manuscript/FIGURE_PLAN.md`

## Adversarial context corruption

Definition: A context-corruption test that deliberately shifts evidence toward an incorrect world.
Plain-language interpretation: The context cue is pushed toward the wrong answer until selection flips.
Manuscript usage: Use for Exp13 threshold-like context failure evidence.
Caveat: It is deterministic and adversarial; stochastic graded corruption remains pending.
Related docs: `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `docs/synthesis/NEXT_EXPERIMENTS.md`

## Consolidation

Definition: A mechanism or setting that biases learned routes toward stability after acquisition.
Plain-language interpretation: The model is made less willing to change what it already learned.
Manuscript usage: Frame as a stability-plasticity bias unless dose-response evidence supports stronger wording.
Caveat: Current evidence does not show consolidation is universally required.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment10_adaptive_reversal/analysis/exp10/exp10_adaptation_thresholds.csv`; `experiments/experiment13_breaking_point/analysis/validation_report.md`

## Stability-plasticity bias

Definition: A tradeoff where settings that preserve old routes may reduce adaptation to new routes, and settings that adapt quickly may lose old routes.
Plain-language interpretation: The model has to balance remembering and changing.
Manuscript usage: Use for Exp10 and cautious Exp13 consolidation framing.
Caveat: Do not present as a complete theory of continual learning.
Related docs: `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`

## Local capacity pressure

Definition: A finite-capacity condition where constraints apply locally to route-supporting structure.
Plain-language interpretation: Individual parts of the route memory run out of room.
Manuscript usage: Use for Exp13 local-budget boundary results.
Caveat: Current local-vs-global comparison is aggregate-only and needs paired seed-level analysis.
Related docs: `docs/experiments/exp13_local_vs_global_budget_comparison.md`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`

## Global capacity pressure

Definition: A finite-capacity condition where the total available route-memory budget is constrained.
Plain-language interpretation: The whole memory system has less room than the full task wants.
Manuscript usage: Use for Exp13 observed degradation curves under budget ratios.
Caveat: Capacity-law fitting remains planned; current evidence is an observed curve.
Related docs: `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `docs/manuscript/FIGURE_PLAN.md`

## Primitive holdout

Definition: A test that withholds some one-step primitive transitions and checks whether the model can handle routes involving them.
Plain-language interpretation: Some basic route entries were never learned, so the model should not be credited for inventing them unless it succeeds on that split.
Manuscript usage: Use for the Exp13 generalization boundary.
Caveat: Current metrics need all/seen/unseen splits before publication-level wording.
Related docs: `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`; `docs/manuscript/MANUSCRIPT_TODO.md`

## Seen primitive

Definition: A one-step transition primitive included in training or acquisition.
Plain-language interpretation: A basic route step the model has already had evidence for.
Manuscript usage: Use when saying the model composes stored primitives.
Caveat: Composition over seen primitives is not unseen primitive inference.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment13_breaking_point/analysis/true_holdout_generalization_summary.csv`

## Unseen primitive

Definition: A one-step transition primitive withheld from training or acquisition.
Plain-language interpretation: A basic route step the model did not learn directly.
Manuscript usage: Use to state the boundary that the current model does not infer missing primitive transitions.
Caveat: Do not describe failure on unseen primitives as a failure of all compositional execution.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `experiments/experiment13_breaking_point/analysis/plots/exp13_holdout_one_step_unseen_primitives.png`

## Continuous front-end bridge

Definition: A preliminary setup where noisy continuous inputs are decoded into symbolic route-memory inputs.
Plain-language interpretation: A noisy front end feeds the route-memory system, but perception is not learned end to end.
Manuscript usage: Use only as preliminary bridge or supplement.
Caveat: Not a full applied or visual learning demonstration.
Related docs: `experiments/experiment13_breaking_point/analysis/continuous_frontend_bridge_summary.csv`; `docs/manuscript/LIMITATIONS_AND_THREATS.md`

## Oracle context

Definition: A context/world label supplied directly to the model by the benchmark.
Plain-language interpretation: The model is told which world it is in.
Manuscript usage: Use in limitations and method caveats for Exp11-Exp13.
Caveat: Oracle context means the current evidence does not solve latent context inference.
Related docs: `docs/manuscript/LIMITATIONS_AND_THREATS.md`; `docs/synthesis/NEXT_EXPERIMENTS.md`

## Latent world inference

Definition: A future capability where the model infers the active world from evidence rather than receiving an oracle label.
Plain-language interpretation: The model figures out which world it is in.
Manuscript usage: Keep as future work, not current evidence.
Caveat: Not implemented in the current manuscript-critical experiments.
Related docs: `docs/synthesis/NEXT_EXPERIMENTS.md`; `docs/synthesis/ROADMAP.md`

## Baseline suite

Definition: A planned set of external comparison methods evaluated on the same route-memory benchmark slices.
Plain-language interpretation: Fair comparators that show whether the proposed mechanism adds anything beyond known alternatives.
Manuscript usage: Use for submission-readiness requirements.
Caveat: Baseline requirements are planned; no external baseline results are currently present.
Related docs: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/synthesis/PUBLICATION_READINESS.md`

## External baseline

Definition: A comparator method outside the proposed model's internal ablation family.
Plain-language interpretation: A different method that should get a fair shot at the same task.
Manuscript usage: Use for planned context-gated, replay, task-mask, parameter-isolation, hypernetwork, superposition, recurrent, or cognitive-map comparisons.
Caveat: External baselines must not be confused with internal ablations.
Related docs: `docs/manuscript/BASELINE_REQUIREMENTS.md`; `docs/manuscript/MANUSCRIPT_TODO.md`

## Internal ablation

Definition: A variant of the project model with one mechanism removed or changed.
Plain-language interpretation: A test of what parts of this model matter.
Manuscript usage: Use for no-recurrence, no-world-context, no-structural-plasticity, consolidation, and related variants.
Caveat: Internal ablations can support mechanism claims but do not replace external baselines.
Related docs: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`; `docs/synthesis/PUBLICATION_READINESS.md`

## Context binding

Definition: Associating route memories with a context or world signal during storage and retrieval.
Plain-language interpretation: Tying the route to the context that makes it correct.
Manuscript usage: Use as a mechanism description when the experiment uses `no_context_binding` or related ablations.
Caveat: Exp13 `no_context_binding` may not be a clean pure ablation and needs Exp13.1 cleanup.
Related docs: `docs/manuscript/MANUSCRIPT_TODO.md`; `experiments/experiment13_breaking_point/analysis/validation_report.md`

## Correct margin

Definition: A score margin for the correct target over the strongest incorrect target.
Plain-language interpretation: How confidently the model prefers the right next state.
Manuscript usage: Use as a diagnostic metric in route-field and robustness summaries.
Caveat: Margin diagnostics should be paired with actual route-table and composition accuracy.
Related docs: `experiments/experiment7_route_field_diagnostics/analysis/exp7.unsaturated/exp7_route_summary.csv`; `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_route_summary.csv`

## Wrong route activation

Definition: Activation assigned to route alternatives that should not be selected.
Plain-language interpretation: How much the model lights up the wrong route.
Manuscript usage: Use as a route-control diagnostic, especially in historical/supporting experiments.
Caveat: Wrong-route activation is diagnostic and should not be used alone as a success metric.
Related docs: `experiments/experiment6_route_audit_successor/analysis/exp6/exp6_wrong_route_activation.png`; `experiments/experiment9_robust_adaptive_route_plasticity/analysis/exp9/exp9_interference_wrong_route_by_bleed.png`
