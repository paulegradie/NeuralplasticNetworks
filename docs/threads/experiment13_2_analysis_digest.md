# Thread Digest: Experiment 13.2 Baseline Suite Analysis

Digest filename: `experiment13_2_analysis_digest.md`
Intended repository path: `docs/threads/experiment13_2_analysis_digest.md`
Import package expected at: `docs/imports/experiment13_2_analysis_digest.zip`

## 1. Thread scope

This thread analyzed the completed Experiment 13.2 baseline-suite run in the context of the Context-Indexed Route Memory research program and the first publishable manuscript. The thread focused on whether Exp13.2 reduces the manuscript's external-baseline blocker, how to interpret the baseline outcomes without overclaiming, what repository documents should be updated, and what the next scientific action should be after baseline integration.

The thread also produced a recommendation for a future successor experiment, Experiment 14: Latent Context Inference, but that was a design/implementation proposal rather than completed Exp13.2 evidence. Exp14 should not be imported as evidence for Exp13.2.

## 2. Experiment analyzed or designed

- Experiment ID: Exp13.2
- Experiment name: Baseline Suite
- Experiment directory: `experiments/experiment13_2_baseline_suite/`
- Run profile: `full`
- Run ID: `exp13_2_full_20260507_165813`
- Uploaded artifact bundle: `exp13_2_full_20260507_165813.zip`
- Main local artifact paths, if known:
  - Expected repo-relative analysis directory after import: `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_metrics.csv`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/metrics.csv`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_effect_sizes.csv`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_baseline_metrics.csv`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_report.md`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/experiment_report.md`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/run_manifest.json`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/progress.jsonl`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_results.json`
- Per-run database path, if applicable:
  - Reported by run manifest and validation report as `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3`.
  - Important caveat: the uploaded `exp13_2_full_20260507_165813.zip` inspected in this thread contained the analysis directory files but did not contain the SQLite database file itself. Codex should verify whether `runs/exp13_2_full_20260507_165813.sqlite3` exists locally in the working tree before citing the database as an imported artifact.

## 3. Experimental design discussed

### Original purpose

Exp13.2 was designed as a manuscript-facing baseline suite. Its purpose was to compare the Context-Indexed Route Memory mechanism against simpler baseline families on the same symbolic route-composition benchmark. The central goal was to reduce the repository's external-baseline blocker, not to claim that CIRM beats an oracle context-gated lookup table.

### Hypotheses / questions

- A context-gated transition table with oracle world/context labels should solve the clean symbolic benchmark.
- A shared no-context transition table should fail when incompatible worlds require different first transitions from the same shared start and mode.
- A route-endpoint memorizer should solve seen full-route queries but fail suffix-route probes that require reusable transition primitives rather than whole-route endpoint memorization.
- A no-recurrence-at-eval CIRM ablation should preserve route-table memory while failing multi-step composition.
- A no-structural-plasticity CIRM ablation should fail route-table storage and composition.
- Recurrent non-plastic rules should not explain the result by recurrence alone.
- Superposition/hash baselines should show compact context-conditioned storage behavior with collision-sensitive degradation.
- Bounded LRU/replay and parameter-isolation baselines should provide conventional finite-capacity controls.

### Variants / baselines

The uploaded metrics include the following major variants:

- `exp13_2_cirm_full`
- `exp13_2_cirm_no_recurrence_at_eval`
- `exp13_2_cirm_no_structural_plasticity`
- `baseline_shared_transition_table`
- `baseline_context_gated_transition_table`
- `baseline_route_endpoint_memorizer`
- `baseline_recurrent_non_plastic_rule`
- `baseline_superposition_hash_slots_1`
- `baseline_superposition_hash_slots_2`
- `baseline_superposition_hash_slots_4`
- `baseline_superposition_hash_slots_8`
- `baseline_superposition_hash_slots_16`
- `baseline_superposition_hash_slots_32`
- `baseline_bounded_lru_no_replay_capacity_1p0`
- `baseline_bounded_lru_with_replay_capacity_1p0`
- `baseline_parameter_isolation_capacity_1p0`
- `baseline_bounded_lru_no_replay_capacity_0p75`
- `baseline_bounded_lru_with_replay_capacity_0p75`
- `baseline_parameter_isolation_capacity_0p75`
- `baseline_bounded_lru_no_replay_capacity_0p5`
- `baseline_bounded_lru_with_replay_capacity_0p5`
- `baseline_parameter_isolation_capacity_0p5`
- `baseline_bounded_lru_no_replay_capacity_0p25`
- `baseline_bounded_lru_with_replay_capacity_0p25`
- `baseline_parameter_isolation_capacity_0p25`

### Metrics

The main metrics discussed were:

- `route_table_accuracy_all`
- `composition_accuracy_seen_routes`
- `composition_accuracy_suffix_routes`
- `first_step_context_accuracy`
- `suffix_generalization_gap`
- `route_table_composition_gap_seen`
- `route_table_composition_gap_suffix`
- `capacity_used`
- `evictions`
- `hash_collisions`
- seed-level summary statistics and confidence intervals in `exp13_2_summary.csv`
- effect-size comparisons in `exp13_2_effect_sizes.csv`

### Run profiles

The completed run used the `full` profile:

- Seeds: 20 (`0` through `19`)
- World counts: `[4, 8, 16, 32]`
- Route lengths: `[4, 8, 12, 16]`
- Routes per world: `24`
- Capacity ratios: `[1.0, 0.75, 0.5, 0.25]`
- Hash slot divisors: `[1, 2, 4, 8]`
- Metrics rows: `15040`
- Summary rows: `748`
- Effect-size rows: `624`
- Progress events: `1685`
- Planned units completed: `1680/1680`

### Expected outcomes

The thread treated the following expected outcomes as important guardrails:

- Context-gated lookup matching CIRM is expected and should be reported honestly.
- Shared no-context failures support the need for world/context indexing, but only for conflict-sensitive probes.
- Endpoint memorizer seen-vs-suffix split supports reusable primitive composition rather than whole-route memorization.
- No-recurrence route-table/composition dissociation strengthens the storage-vs-execution claim.
- Capacity-pressure curves are useful failure-mode evidence but should not be overinterpreted as biological capacity laws.

### Implementation notes

The uploaded run included:

- `run_manifest.json` with profile, artifact paths, row counts, schema version, and CPU/device metadata.
- `progress.jsonl` with structured progress events and a `run_complete` event.
- `validation_report.md` with status `PASS`, 28 pass checks, 0 warnings, 0 failures.
- Six generated plots.
- A validation check claiming the SQLite database existed at runtime, but the uploaded zip inspected in this thread did not itself include the SQLite file.

### Known risks

- The baseline suite is symbolic/algorithmic; it is not a complete neural-network baseline suite.
- The context-gated transition table is oracle-like because world/context labels are supplied.
- CIRM does not beat the oracle context-gated table on the clean symbolic task; manuscript framing must be mechanistic rather than raw accuracy superiority.
- The shared no-context table can look artificially strong on suffix probes because suffix probes start after the world-disambiguating first transition.
- Infinite or extremely large Cohen's d values appear in some effect-size rows because some comparisons have zero variance at ceiling/floor. These should be handled carefully in manuscript tables.
- The SQLite database path was reported as existing in validation but was not present in the uploaded artifact bundle inspected here.
- Exp13.2 does not resolve the Exp13.1 targeted-lesion diagnostic failure.
- Exp13.2 does not solve the oracle-context limitation.

## 4. Results analyzed

### Result 1: Run integrity and validation passed

Claim:
Exp13.2 full run appears complete enough for repository import and manuscript-level analysis, subject to local verification of the SQLite database file.

Evidence:
`validation_report.md` reports status `PASS`, with `PASS: 28`, `WARN: 0`, and `FAIL: 0`. It reports required files present, 15040 metrics rows, required metric columns present, required phases present, required variants present, 20 seeds, 748 summary rows, device metadata present, SQLite tables present, six plots generated, and `progress.jsonl` containing `run_complete`.

Caveat:
The uploaded zip inspected in this thread did not include `runs/exp13_2_full_20260507_165813.sqlite3`, even though validation reported that the database existed during the local run. Codex should verify or import the SQLite file separately before citing it as a repository artifact.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/run_manifest.json`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/progress.jsonl`

Thread status:
Strong

### Result 2: CIRM and oracle context-gated lookup both solve the clean symbolic benchmark

Claim:
The clean Exp13.2 benchmark can be solved by both `exp13_2_cirm_full` and `baseline_context_gated_transition_table`.

Evidence:
At the hard clean slice discussed in the thread (`world_count=32`, `route_length=16`, `phase=baseline_comparison`), both `exp13_2_cirm_full` and `baseline_context_gated_transition_table` report:
- `route_table_accuracy_all_mean = 1.0000`
- `composition_accuracy_seen_routes_mean = 1.0000`
- `composition_accuracy_suffix_routes_mean = 1.0000`
- `first_step_context_accuracy_mean = 1.0000`

Caveat:
This weakens any manuscript claim based on raw accuracy superiority over a supplied-context lookup table. It does not invalidate CIRM; it refines the contribution toward mechanism, failure modes, and the controlled conjunction of context-indexed storage plus recurrent execution. The context-gated table is an oracle-style baseline because world/context labels are supplied.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_report.md`

Thread status:
Strong

### Result 3: Shared no-context lookup fails on conflict-sensitive probes

Claim:
A shared transition table without context/world indexing fails when the task requires disambiguating incompatible world-specific first transitions.

Evidence:
At `world_count=32`, `route_length=16`, `phase=baseline_comparison`, `baseline_shared_transition_table` reports:
- `composition_accuracy_seen_routes_mean = 0.03125`
- `first_step_context_accuracy_mean = 0.03125`
- `route_table_accuracy_all_mean = 0.939453125`
- `composition_accuracy_suffix_routes_mean = 1.0000`

The low seen-route and first-step context accuracy indicate failure on the context-conflict point.

Caveat:
The high suffix-route accuracy is not evidence that no-context lookup solves context indexing. Suffix probes can begin after the world-disambiguating first transition, so they may avoid the deliberate conflict that breaks seen full-route execution. Manuscript text and figures must separate first-step/seen-route context conflict from suffix-route primitive composition.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_first_step_context_accuracy.png`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_seen_route_composition_accuracy.png`

Thread status:
Strong with metric-interpretation caveat

### Result 4: Route endpoint memorization does not explain suffix composition

Claim:
Whole-route endpoint memorization can solve seen full routes but does not explain suffix-route generalization.

Evidence:
At `world_count=32`, `route_length=16`, `phase=baseline_comparison`, `baseline_route_endpoint_memorizer` reports:
- `composition_accuracy_seen_routes_mean = 1.0000`
- `composition_accuracy_suffix_routes_mean = 0.0000`
- `route_table_accuracy_all_mean = 0.0000`
- `first_step_context_accuracy_mean = 0.0000`

Caveat:
This supports a narrow claim: suffix-route probes require reuse of stored transition primitives not memorized as whole-route endpoints. It does not prove broad abstract rule induction or inference of unseen primitive transitions.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_suffix_generalization_accuracy.png`

Thread status:
Strong

### Result 5: No-recurrence-at-eval preserves route table but destroys multi-step execution

Claim:
Exp13.2 strengthens the route-table/composition dissociation: storage of local transitions and recurrent multi-step execution are separable.

Evidence:
At `world_count=32`, `route_length=16`, `phase=baseline_comparison`, `exp13_2_cirm_no_recurrence_at_eval` reports:
- `route_table_accuracy_all_mean = 1.0000`
- `composition_accuracy_seen_routes_mean = 0.0000`
- `composition_accuracy_suffix_routes_mean = 0.0000`
- `first_step_context_accuracy_mean = 1.0000`

Caveat:
This is still an internal CIRM ablation, not an external neural recurrent baseline. It supports the benchmark-specific claim that recurrence is required for multi-step execution over stored transitions.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_route_table_accuracy.png`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_seen_route_composition_accuracy.png`

Thread status:
Strong

### Result 6: No-structural-plasticity fails completely in this suite

Claim:
The no-structural-plasticity CIRM ablation fails to store or execute the route benchmark.

Evidence:
At `world_count=32`, `route_length=16`, `phase=baseline_comparison`, `exp13_2_cirm_no_structural_plasticity` reports:
- `route_table_accuracy_all_mean = 0.0000`
- `composition_accuracy_seen_routes_mean = 0.0000`
- `composition_accuracy_suffix_routes_mean = 0.0000`
- `first_step_context_accuracy_mean = 0.0000`

Caveat:
This is an internal ablation and should be used alongside previous Exp8/Exp11/Exp12/Exp13/Exp13.1 evidence. It should not be generalized into a claim that all neural systems require structural plasticity.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

Thread status:
Strong

### Result 7: Recurrent non-plastic rule baseline does not explain the result

Claim:
A recurrent non-plastic rule baseline does not explain CIRM's successful route storage and execution in the hard clean benchmark.

Evidence:
At `world_count=32`, `route_length=16`, `phase=baseline_comparison`, `baseline_recurrent_non_plastic_rule` reports approximately:
- `route_table_accuracy_all_mean = 0.000187`
- `composition_accuracy_seen_routes_mean = 0.0000`
- `composition_accuracy_suffix_routes_mean = 0.000060`
- `first_step_context_accuracy_mean = 0.0000`

Caveat:
This is a simple symbolic recurrent non-plastic control, not a trained neural recurrent model with a large parameter budget. It is useful as a local sanity baseline but should not be represented as a comprehensive recurrent-neural baseline.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`

Thread status:
Promising

### Result 8: Superposition/hash baselines show collision-sensitive context storage behavior

Claim:
Superposition/hash lookup baselines partially bridge context-conditioned storage and compactness, with performance depending on effective slot/collision budget.

Evidence:
At the hard clean slice:
- `baseline_superposition_hash_slots_4` reports seen composition `0.125`, suffix composition `1.000`, first-step context `0.125`, and 672 hash collisions.
- `baseline_superposition_hash_slots_8` reports seen composition `0.250`, suffix composition `1.000`, first-step context `0.250`, and 576 hash collisions.
- `baseline_superposition_hash_slots_16` reports seen composition `0.500`, suffix composition `1.000`, first-step context `0.500`, and 384 hash collisions.
- `baseline_superposition_hash_slots_32` reports route table, seen composition, suffix composition, and first-step context all at `1.000`, with 0 hash collisions.

Caveat:
The same suffix caveat applies: suffix queries can avoid the world-conflicting first step. These baselines should be used to discuss compact context-conditioned storage and collision pressure, not to claim broad neural superposition behavior.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_capacity_pressure.png`

Thread status:
Promising

### Result 9: Capacity-limited replay/LRU and parameter-isolation baselines produce interpretable failure curves

Claim:
Finite-capacity baseline controls show expected degradation as capacity ratio decreases.

Evidence:
At `world_count=32`, `route_length=16`, `phase=capacity_pressure`:
- Bounded LRU no-replay and with-replay baselines show route-table, seen composition, suffix composition, and first-step context at 1.00, 0.75, 0.50, and 0.25 for capacity ratios 1.0, 0.75, 0.5, and 0.25 respectively.
- Parameter-isolation at capacity ratio 1.0 solves all metrics, while lower ratios preserve route-table/suffix proportions but show seen composition and first-step context collapse to 0.0 in the inspected hard slice.

Caveat:
These are symbolic capacity controls. They are useful for reviewer-facing failure-mode comparison but are not capacity-law evidence for CIRM and should not be treated as biological plausibility evidence.

Source artifact:
`experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv`; `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_capacity_pressure.png`

Thread status:
Promising

### Result 10: Exp13.2 motivates latent-context inference as the next conceptual experiment

Claim:
After Exp13.2, the next conceptual experiment should test whether route memory can infer context/world from partial evidence rather than receiving oracle world labels.

Evidence:
The baseline suite shows that an oracle context-gated table solves the clean symbolic benchmark. Therefore, the next reviewer-facing limitation is not baseline absence alone; it is the oracle context/world-label assumption.

Caveat:
This is a design decision, not completed Exp13.2 evidence. The proposed Exp14 latent-context inference experiment should be tracked separately and only become evidence after a completed run and analysis.

Source artifact:
Thread discussion and Exp13.2 analysis; no Exp14 completed artifact should be cited from this digest.

Thread status:
Preliminary design decision

## 5. Key scientific conclusions supported by this thread

Claim:
Exp13.2 reduces the external-baseline blocker for the first manuscript.

Evidence:
The full run includes oracle context-gated, shared no-context, endpoint memorization, recurrent non-plastic, superposition/hash, bounded replay/LRU, and parameter-isolation baselines with 20 seeds, summary statistics, effect sizes, validation, and figures.

Caveat:
The baseline suite is symbolic/algorithmic. It does not replace prior-art discussion, neural baselines, or the missing novelty-assessment import.

Experiment:
Exp13.2

Artifact(s):
`exp13_2_metrics.csv`; `exp13_2_summary.csv`; `exp13_2_effect_sizes.csv`; `exp13_2_baseline_metrics.csv`; `validation_report.md`; `run_manifest.json`

Manuscript relevance:
Strengthens C12 and should change the manuscript from "baselines are missing" to "symbolic baseline suite completed; oracle context-gated lookup matches CIRM in clean settings; remaining novelty requires careful framing and/or latent-context experiments."

Claim:
The clean route-memory benchmark is solvable by oracle context-gated lookup.

Evidence:
`baseline_context_gated_transition_table` matches `exp13_2_cirm_full` at ceiling on the hard clean slice.

Caveat:
This constrains the manuscript's novelty claim. The contribution cannot be "CIRM uniquely solves the clean supplied-context symbolic benchmark."

Experiment:
Exp13.2

Artifact(s):
`exp13_2_summary.csv`; `exp13_2_report.md`

Manuscript relevance:
Main text limitation or reviewer-risk discussion; may also be shown in a baseline comparison panel.

Claim:
Context/world indexing is necessary for incompatible first-step route systems.

Evidence:
`baseline_shared_transition_table` fails seen-route composition and first-step context accuracy at the hard clean slice, while context-gated lookup and CIRM solve the same slice.

Caveat:
Suffix metrics for the shared table are misleadingly high because suffix probes can start after the disambiguating first transition.

Experiment:
Exp13.2

Artifact(s):
`exp13_2_summary.csv`; `plots/exp13_2_first_step_context_accuracy.png`; `plots/exp13_2_seen_route_composition_accuracy.png`

Manuscript relevance:
Strengthens/refines C2.

Claim:
Reusable primitive composition is distinct from whole-route endpoint memorization.

Evidence:
`baseline_route_endpoint_memorizer` reaches seen-route composition accuracy 1.0 but suffix-route composition accuracy 0.0 at the hard clean slice.

Caveat:
This does not prove unseen primitive inference.

Experiment:
Exp13.2

Artifact(s):
`exp13_2_summary.csv`; `plots/exp13_2_suffix_generalization_accuracy.png`

Manuscript relevance:
Strengthens C4 and refines C9 wording toward seen-primitives only.

Claim:
Route-table storage and recurrent execution are separable.

Evidence:
`exp13_2_cirm_no_recurrence_at_eval` preserves route-table accuracy and first-step context accuracy at 1.0 while seen/suffix composition accuracies fall to 0.0 at the hard clean slice.

Caveat:
Internal ablation only; should be paired with baseline and prior-art discussion.

Experiment:
Exp13.2

Artifact(s):
`exp13_2_summary.csv`; `plots/exp13_2_route_table_accuracy.png`; `plots/exp13_2_seen_route_composition_accuracy.png`

Manuscript relevance:
Strengthens C3 and C4.

Claim:
The oracle-context limitation is now the next conceptual blocker.

Evidence:
The context-gated oracle table solves the clean benchmark, so the manuscript must either frame this as expected or add a latent-context inference experiment.

Caveat:
Exp14 was proposed but not completed in this thread.

Experiment:
Exp13.2 plus proposed Exp14

Artifact(s):
No completed Exp14 evidence in this digest.

Manuscript relevance:
Limitation and next experiment.

## 6. Important flaws, mistakes, or implementation concerns identified

- The uploaded artifact bundle did not contain the SQLite database file, despite validation reporting that `runs/exp13_2_full_20260507_165813.sqlite3` existed locally. Codex should verify/import the database separately or mark the DB as local verification pending.
- The shared no-context baseline's suffix-route performance is not a valid measure of context indexing because suffix probes can start after the disambiguating conflict point.
- The context-gated transition table is oracle-like and matches CIRM on the clean symbolic benchmark. This must be treated as a framing constraint, not hidden.
- Some effect-size rows contain infinite or extremely large Cohen's d values due to floor/ceiling results with zero variance. These are mathematically understandable but manuscript tables should handle them carefully.
- Exp13.2 baselines are symbolic/algorithmic. They do not fully satisfy requests for neural baselines or prior-art comparison.
- Exp13.2 does not resolve the Exp13.1 targeted-lesion diagnostic failure.
- Exp13.2 does not resolve the Exp13 holdout seen/unseen primitive metric cleanup issue.
- Exp13.2 does not remove the oracle world/context-label limitation.
- Capacity-pressure baseline results should not be described as CIRM capacity laws.
- If final manuscript figures are generated, they should be produced by reproducible figure scripts or documented source-data mirrors, not ad hoc plot copying.

## 7. Figures or artifacts referenced

### Uploaded bundle

- `exp13_2_full_20260507_165813.zip`

### CSVs

- `exp13_2_metrics.csv`
- `metrics.csv`
- `exp13_2_summary.csv`
- `exp13_2_effect_sizes.csv`
- `exp13_2_baseline_metrics.csv`

### Reports

- `exp13_2_report.md`
- `experiment_report.md`
- `validation_report.md`

### Manifests and validation artifacts

- `run_manifest.json`
- `exp13_2_config.json`
- `validation_results.json`
- `progress.jsonl`

### Plots

- `plots/exp13_2_seen_route_composition_accuracy.png`
- `plots/exp13_2_suffix_generalization_accuracy.png`
- `plots/exp13_2_route_table_accuracy.png`
- `plots/exp13_2_first_step_context_accuracy.png`
- `plots/exp13_2_capacity_pressure.png`
- `plots/exp13_2_sequential_retention.png`

### SQLite

- Reported path: `runs/exp13_2_full_20260507_165813.sqlite3`
- Status: validation report says it existed locally; uploaded zip inspected in this thread did not include it. Local verification pending.

## 8. Decisions made

- Treat Exp13.2 as a valid full baseline-suite result after validation, with the SQLite packaging caveat.
- Do not claim that CIRM beats an oracle context-gated lookup table on the clean symbolic benchmark.
- Use Exp13.2 to refine the manuscript spine: CIRM is not uniquely accurate against oracle lookup; the contribution is the controlled conjunction of context-indexed storage, structural route memory, and recurrent execution, plus interpretable failure modes.
- Treat the context-gated table's ceiling performance as expected and manuscript-important.
- Treat shared no-context failures as evidence for context/world indexing only in conflict-sensitive metrics such as first-step context and seen full-route composition.
- Treat endpoint memorizer seen-vs-suffix split as evidence against whole-route memorization explaining suffix composition.
- Treat no-recurrence-at-eval as strengthened evidence for route-table/composition dissociation.
- Treat finite-capacity baselines as supplementary failure-mode comparisons unless a final figure plan elevates them.
- Recommend Exp14 latent-context inference as the next conceptual experiment, because Exp13.2 leaves oracle context/world labels as the central limitation.
- Keep Exp14 separate from Exp13.2 repository integration.

## 9. Open questions

- Is `runs/exp13_2_full_20260507_165813.sqlite3` present in Paul's local repository, and should it be imported into the public repo or omitted due to size?
- Should C12 status move from `Needs baseline` to a more nuanced status such as `Promising` or `Partially satisfied`, while retaining prior-art/neural-baseline caveats?
- Should the manuscript include the context-gated oracle table in a main figure or a supplementary baseline table?
- How should infinite/zero-variance effect sizes be rendered in final manuscript tables?
- Should final figure scripts regenerate the six Exp13.2 plots or produce new paper-specific panels from `exp13_2_summary.csv`?
- Should Exp13.2 trigger a future planned `docs/manuscript/BASELINE_RESULTS.md` file, or should results be integrated directly into `CLAIMS_AND_EVIDENCE.md` and `FIGURE_PLAN.md`?
- How much additional neural baseline work is required beyond symbolic baselines before submission?
- Should Exp14 latent-context inference be run before manuscript drafting, or treated as post-baseline future work depending on scope?
- Should capacity-pressure baseline curves be included only as supplement to avoid overextending the manuscript?
- Should the shared no-context table suffix success be explicitly documented as a metric caveat in `LIMITATIONS_AND_THREATS.md`?

## 10. Relationship to first manuscript

### Central claim

Exp13.2 does not replace the central CIRM claim. It refines it. The central claim should not be that CIRM is uniquely accurate on clean symbolic route composition. Instead, the manuscript should claim that context-indexed structural route memory plus recurrent execution creates a mechanism whose components fail in distinct, interpretable ways under controlled baselines.

### Supporting claim

Exp13.2 strengthens:

- C2 world/context indexing, by showing shared no-context lookup fails on conflict-sensitive probes.
- C3 recurrence, by showing no-recurrence preserves route table but fails execution.
- C4 route-table/composition dissociation, by separating local transition storage from recurrent multi-step execution and by showing endpoint memorization fails suffix probes.
- C12 baseline requirement, by converting the baseline suite from planned blocker to completed symbolic baseline evidence.

### Limitation

Exp13.2 strengthens the oracle-context limitation. The context-gated table solves the benchmark when world labels are supplied. This should be openly stated.

### Future work

The thread recommended Exp14 latent-context inference as the next experiment to test whether context can be inferred from partial transition evidence rather than supplied as an oracle label.

### Supplementary material

Capacity-pressure baselines, replay/LRU controls, parameter-isolation curves, hash-slot/superposition curves, and sequential-retention plots are likely good candidates for supplement unless the final figure plan has space for a baseline comparison panel.

## 11. Claims-and-evidence rows contributed by this thread

| Claim | Evidence | Caveat | Experiment(s) | Artifact(s) | Manuscript status |
|---|---|---|---|---|---|
| Symbolic external baselines have now been run for the first manuscript benchmark. | Full Exp13.2 run reports 20 seeds, 15040 metric rows, 748 summary rows, 624 effect-size rows, six plots, and validation PASS 28 / WARN 0 / FAIL 0. | Baselines are symbolic/algorithmic, not a full neural or prior-art comparison. SQLite file was reported but not present in the uploaded zip. | Exp13.2 | `validation_report.md`; `run_manifest.json`; `exp13_2_metrics.csv`; `exp13_2_summary.csv`; `exp13_2_effect_sizes.csv` | Strong for symbolic baseline requirement; still caveated |
| Oracle context-gated lookup solves the clean symbolic benchmark. | `baseline_context_gated_transition_table` equals `exp13_2_cirm_full` at 1.0 on route-table, seen composition, suffix composition, and first-step context in the hard clean slice. | This prevents raw superiority claims over oracle context-gated lookup. | Exp13.2 | `exp13_2_summary.csv`; `exp13_2_report.md` | Strong; claim-refining |
| Context/world indexing is required for incompatible first-step route systems. | `baseline_shared_transition_table` has seen-route and first-step context accuracy 0.03125 at the hard clean slice while CIRM and context-gated lookup are 1.0. | Suffix-route accuracy for shared no-context is misleadingly high because suffix probes can start after the disambiguating conflict. | Exp13.2 | `exp13_2_summary.csv`; `plots/exp13_2_first_step_context_accuracy.png` | Strong with metric caveat |
| Whole-route memorization does not explain suffix composition. | Endpoint memorizer seen-route accuracy is 1.0 but suffix-route accuracy is 0.0 at the hard clean slice. | Supports reusable seen-primitive composition only, not unseen primitive inference. | Exp13.2 | `exp13_2_summary.csv`; `plots/exp13_2_suffix_generalization_accuracy.png` | Strong |
| Recurrence is required for multi-step execution over stored route tables. | No-recurrence-at-eval route-table accuracy is 1.0 while seen and suffix composition are 0.0 at the hard clean slice. | Internal ablation; should be framed benchmark-specifically. | Exp13.2 | `exp13_2_summary.csv`; `plots/exp13_2_route_table_accuracy.png`; `plots/exp13_2_seen_route_composition_accuracy.png` | Strong |
| Structural plasticity remains necessary inside the CIRM ablation family. | No-structural-plasticity route table, seen composition, suffix composition, and first-step context are all 0.0 at the hard clean slice. | Internal ablation, not a broad biological claim. | Exp13.2 | `exp13_2_summary.csv` | Strong internally |
| Compact hash/superposition baselines show collision-sensitive context storage behavior. | Hash-slot variants improve as collisions decrease; slots 32 reaches ceiling, smaller slot settings degrade first-step and seen-route composition. | Still symbolic; suffix success can be confounded by suffix construction. | Exp13.2 | `exp13_2_summary.csv`; `plots/exp13_2_capacity_pressure.png` | Promising / supplemental |
| Finite-capacity replay/LRU and parameter-isolation controls provide interpretable baseline curves. | Capacity-ratio baselines degrade as capacity ratios decrease in the hard capacity-pressure slice. | Do not use as CIRM capacity-law evidence. | Exp13.2 | `exp13_2_summary.csv`; `plots/exp13_2_capacity_pressure.png` | Promising / supplement |
| The next conceptual blocker is oracle context labels. | Context-gated oracle lookup solves the clean symbolic task, so latent context inference becomes the natural next experiment. | Exp14 was only proposed/implemented as a design follow-up; no completed Exp14 evidence in this digest. | Exp13.2; proposed Exp14 | Thread discussion only for Exp14 | Future work / next experiment |

## 12. Required repository updates

Codex should update the repository conservatively and verify paths after import.

### Experiment directory

- `experiments/experiment13_2_baseline_suite/README.md`
  - Add completed run section for `exp13_2_full_20260507_165813`.
  - Include validation status PASS 28 / WARN 0 / FAIL 0.
  - Include profile, seeds, world counts, route lengths, routes per world, and row counts.
  - Include key claim/evidence/caveat bullets.
  - Explicitly state that context-gated lookup matches CIRM and that this refines the claim.
  - Note whether SQLite DB is present locally or mark it local verification pending.

### Thread digest

- `docs/threads/experiment13_2_analysis_digest.md`
  - Import this digest from `docs/imports/experiment13_2_analysis_digest.zip`.

### Experiment summary / registry

- `docs/experiments/EXPERIMENT_REGISTRY.md`
  - Add or update Exp13.2 row.
  - Suggested role: external/symbolic baseline suite.
  - Suggested evidence status: local + thread evidence aligned after artifacts are imported and paths verified.
  - Required follow-up: prior-art/neural baseline framing, oracle-context limitation / Exp14 latent context inference, SQLite verification.

- `docs/experiments/exp13_2_summary.md`
  - Create if absent, or update if already created.
  - Include run identity, artifact list, key results, caveats, and claim/evidence/caveat table.

### Manuscript docs

- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
  - Update C12 to indicate the symbolic baseline suite has been completed.
  - Do not mark all baseline requirements fully closed if neural/prior-art baselines remain absent.
  - Add Exp13.2 support to C2, C3, C4, and C12.
  - Add caveat that context-gated oracle lookup matches CIRM in the clean symbolic task.
  - Add caveat that shared no-context suffix success is not context-indexing evidence.

- `docs/manuscript/FIGURE_PLAN.md`
  - Add Exp13.2 baseline comparison figure candidates:
    - route table accuracy;
    - seen-route composition;
    - suffix composition;
    - first-step context accuracy;
    - capacity pressure;
    - sequential retention.
  - Decide which are main vs supplement.
  - Prefer final figure scripts/source-data mirrors rather than directly using auto-generated plots.

- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
  - Add or update limitation: oracle context-gated lookup solves the clean supplied-context symbolic benchmark.
  - Add limitation: Exp13.2 symbolic baselines do not replace neural/prior-art baselines.
  - Add metric caveat: suffix probes can avoid first-step context conflict, especially for shared no-context and hash baselines.
  - Preserve existing Exp13.1 lesion limitation.

- `docs/manuscript/MANUSCRIPT_TODO.md`
  - Move "add baseline suite" from unsatisfied blocker to completed/partially satisfied, depending on repo policy.
  - Keep remaining TODOs:
    - prior-art/novelty import;
    - neural baseline/prior-art comparison if required;
    - final figure scripts;
    - Exp13 holdout metric cleanup if still central;
    - Exp13.1 lesion audit if lesion evidence is desired;
    - oracle-context/latent-context follow-up.

- `docs/manuscript/BASELINE_REQUIREMENTS.md`
  - Add a completed-results section or link to `docs/experiments/exp13_2_summary.md`.
  - Mark B1/B2/B3/B4/B5/B6-style symbolic controls as completed where appropriate.
  - Keep B7 CSCG/cognitive-map comparator optional or planned unless implemented.

- Potential future planned file: `docs/manuscript/BASELINE_RESULTS.md`
  - Optional. If created, keep it as a concise baseline-results index and cite authoritative experiment artifacts.

### Synthesis docs

- `docs/synthesis/PROJECT_STATUS.md`
  - Update current state to say Exp13.2 full baseline suite completed and analyzed.
  - State that the project is stronger but still not submission-ready until final figure scripts, prior-art/novelty import, and oracle-context framing are handled.

- `docs/synthesis/PUBLICATION_READINESS.md`
  - Move "external baseline evidence is absent" to "symbolic baseline evidence exists; remaining risk is oracle context gating and neural/prior-art framing."
  - Keep summary judgment conservative.

- `docs/synthesis/NEXT_EXPERIMENTS.md`
  - Mark Exp13.2 full baseline suite completed.
  - Recommend Exp14 latent-context inference as the next conceptual experiment if manuscript scope permits.
  - Preserve Exp13.1 lesion audit as conditional if lesion evidence will be cited.

### Repo audit and source data

- `docs/repo_audit/ARTIFACT_INDEX.csv`
  - Add Exp13.2 full-run artifacts and plots.
  - Mark SQLite DB as present or local verification pending after checking the working tree.

- `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md` or equivalent conflict/audit log if present
  - Add caveat that uploaded artifact bundle lacked SQLite DB even though validation reported it.
  - Add caveat that suffix metrics for shared no-context require careful interpretation.

- `docs/source_data/`
  - Add review-friendly mirrors for selected Exp13.2 summary/effect-size tables if repository convention supports this.
  - Suggested mirrors:
    - Exp13.2 hard-slice baseline comparison table.
    - Exp13.2 capacity-pressure baseline table.
    - Exp13.2 effect-size comparison table with special handling for infinite values.

### Verification

- `scripts/verify_doc_source_paths.py`
  - Run after updating docs.
  - Fix any missing `experiments/...` paths before committing.

## 13. Recommended next action

1. Import the full Exp13.2 analysis artifacts into `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/`.
2. Verify whether `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3` exists locally. If it does not, either copy it from the local run machine or mark it `local verification pending` in docs.
3. Import this thread digest to `docs/threads/experiment13_2_analysis_digest.md`.
4. Update README, registry, experiment summary, claims/evidence, figure plan, limitations, TODO, synthesis docs, source-data mirrors, and artifact index.
5. Run `python scripts/verify_doc_source_paths.py`.
6. After Exp13.2 is integrated, decide whether to proceed with Exp14 latent-context inference before manuscript drafting. The scientific rationale is strong because Exp13.2 shows oracle context-gated lookup solves the clean supplied-context benchmark.

## 14. Import package checklist

- Zip filename: `experiment13_2_analysis_digest.zip`
- Digest filename inside zip: `experiment13_2_analysis_digest.md`
- Digest is at zip root, not nested: yes
- Digest final path after repo import: `docs/threads/experiment13_2_analysis_digest.md`
- Digest contains only thread-derived analysis, not direct repo edits: yes
- Any local artifact paths needing verification:
  - `experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/` should be verified after artifact import.
  - `experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3` is local verification pending because validation reported it but the uploaded artifact zip inspected in this thread did not include it.
