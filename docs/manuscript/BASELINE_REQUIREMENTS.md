# Baseline Requirements

## Evidence status

This is a planning document, not evidence of baseline performance. All baseline rows below are planned until a baseline experiment is implemented, run, analyzed, and linked from the canonical evidence map.

Claim: Baselines are required before submission-readiness can be claimed.
Evidence: Local thread digests repeatedly flag external comparisons as a manuscript blocker.
Caveat: The thread-referenced novelty artifact named `Pasted text.txt` is not present locally; local verification pending. Do not treat this document as a substitute for prior-art review or baseline results.
Source path: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`; `docs/manuscript/CLAIMS_AND_EVIDENCE.md`

## Why baselines are required

Internal ablations are not enough to establish manuscript-ready novelty. The current experiments show that the proposed mechanism has separable internal components, but reviewers can still ask whether a simpler transition table, conventional context gating, recurrence alone, replay, task masks, parameter isolation, or context-conditioned weights would solve the same benchmark.

Novelty should not rest on context gating, recurrence, or structural plasticity individually. The defensible contribution is narrower: the tested conjunction of context-indexed structural route memory plus recurrent execution on a continual compositional route-memory benchmark.

## Minimum baseline suite for first manuscript

| Baseline ID | Baseline name | Purpose | Minimal implementation | Input/output contract | Metrics | Expected strength | Expected weakness | Manuscript role | Implementation status | Source path / rationale |
|---|---|---|---|---|---|---|---|---|---|---|
| B1 | Shared transition table | Test whether explicit structural lookup without context separation is sufficient. | One global table keyed by `(source_node, mode)` with sequential updates; no per-world index. | Input: same worlds, nodes, modes, train/eval routes as Exp12/Exp13 slices. Output: predicted final node and optional one-step table prediction. | Composition accuracy; one-step route-table accuracy; retention; failure curves under capacity pressure. | Simple, transparent, strong when worlds are compatible or only the newest world matters. | Expected to collide under incompatible worlds because all contexts share the same transition key. | Minimal lower bound and reviewer sanity check. | planned | Rationale from internal no-world-context failures. Source path: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `docs/threads/experiment12to13_export.md`. |
| B2 | Context-gated transition table / task mask | Test whether supplied context labels plus task-specific masks explain the result. | Per-world transition table or masked table selected by oracle world/context label; no learned structural route-memory dynamics beyond lookup. | Input: same benchmark with oracle context label. Output: predicted final node, table accuracy, selected world if modeled. | Composition accuracy; route-table accuracy; retention; world/context selection if applicable; capacity usage. | Should be strong when context is clean and capacity is unconstrained. | May not test endogenous context selection and may require explicit per-task allocation. | Separates context indexing from the proposed structural/recurrent implementation. | planned | Thread-derived requirement for gating/task-mask comparators. Source path: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`. |
| B3 | Recurrent non-plastic executor | Test whether recurrence alone can execute routes without structural memory updates. | Fixed recurrent transition executor with no structural plasticity; trained or configured under the same one-step exposure budget. | Input: one-step training sequence and multi-step evaluation routes. Output: final-node prediction and optional hidden-state diagnostics. | Composition accuracy; one-step accuracy; retention after sequential worlds; route-length sensitivity. | Should reveal whether recurrence can compose when route memory is supplied or learned elsewhere. | Expected to fail when local transition storage is absent or overwritten. | Fair comparator for the recurrence claim. | planned | Internal no-structural-plasticity and no-recurrence ablations motivate this baseline. Source path: `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`. |
| B4 | Replay-based continual learner | Test whether replay can preserve route knowledge across sequential worlds. | Maintain a replay buffer of previous world transitions or routes; train a simple learner/table model sequentially with current plus replay samples. | Input: same sequential world stream plus a documented replay budget. Output: predictions and replay/resource metadata. | Composition accuracy; route-table accuracy; retention; replay memory size; runtime/resource footprint if easy. | Strong retention control under sufficient replay budget. | May trade storage or replay cost for retention; may not expose structural capacity pressure the same way. | External continual-learning style retention comparator. | planned | Thread-derived replay requirement; no replay result exists locally. Source path: `docs/threads/experiment11_export`; `docs/threads/experiment12to13_export.md`. |
| B5 | Parameter-isolation / mask-based baseline | Test whether isolated capacity explains retention and composition. | Allocate task/world-specific masks, subnetworks, or table partitions with documented capacity limits. | Input: same worlds/routes plus oracle task/world ID. Output: final-node prediction, mask/capacity usage, and retention metrics. | Composition accuracy; route-table accuracy; retention; capacity usage; failure curves under pressure. | Strong when each world gets isolated capacity. | May require task identity and grow with number of worlds; capacity fairness must be explicit. | Tests whether the proposed mechanism is just parameter isolation. | planned | Thread-derived task-mask/parameter-isolation requirement. Source path: `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md`. |
| B6 | Hypernetwork or context-conditioned weights baseline | Test whether compact context-conditioned storage can match route memory. | Use context/world embedding to generate or select transition weights/table entries; keep training and evaluation benchmark identical. | Input: world context plus route query. Output: final-node prediction, one-step prediction, and parameter/resource metadata. | Composition accuracy; route-table accuracy; retention; world-count scaling; runtime/resource footprint if easy. | Natural comparator for context-conditioned storage. | May rely heavily on oracle context and may generalize poorly to unseen primitive transitions. | Distinguishes structural route memory from context-conditioned parameter generation. | planned | Thread-derived hypernetwork/superposition requirement; no local baseline artifact exists. Source path: `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md`. |
| B7 | Optional CSCG / cloned-state cognitive-map comparator | Test relationship to cloned-state or cognitive-map style representations. | Implement a minimal cloned-state map over observed transitions, or document why implementation is out of scope for the first manuscript. | Input: observed state/action/world trajectories. Output: inferred cloned states or transition map plus route predictions. | Route-table accuracy where applicable; composition accuracy; world/context selection; failure modes. | Conceptually close to context-specific state splitting. | May require different assumptions and a larger implementation scope. | Optional positioning comparator or discussion anchor. | planned | Thread-level planning mentions CSCG/cloned-state comparators; no local comparison exists. Source path: `docs/threads/experiment12to13_export.md`; `docs/synthesis/NEXT_EXPERIMENTS.md`. |

## Benchmark contract for baselines

Baselines should run on the same route-memory benchmark slices used for the core Exp12/Exp13 claims and report:

- composition accuracy;
- route-table / one-step accuracy where applicable;
- retention after sequential worlds;
- world/context selection if applicable;
- capacity usage;
- failure curves under pressure;
- seed-level uncertainty;
- runtime/resource footprint if easy.

Every baseline result should be recorded with the same discipline:

```text
Claim -> Evidence -> Caveat -> Source path
```

## Baseline experiment organization

Recommended future organization:

- Future planned option: `experiments/exp13_2_baseline_suite/`, if the suite is framed as a direct follow-on from Exp13/Exp13.1.
- Future planned option: `experiments/exp14_baseline_suite/`, if the suite becomes the next numbered experiment.

Do not create either directory until baseline implementation is explicitly started. Keep baseline results out of older experiment directories.

## Acceptance criteria

The baseline suite is complete enough for a first manuscript when:

- at least the shared-table, context-gated table/task-mask, recurrent non-plastic, and replay baselines are implemented;
- each baseline runs on the same key Exp12/Exp13 or Exp13.1 benchmark slices;
- each baseline reports summary CSVs, figures, and seed-level uncertainty;
- capacity/resource assumptions are documented clearly enough for reviewer comparison;
- baseline artifacts are linked from `docs/manuscript/CLAIMS_AND_EVIDENCE.md` or a future planned `docs/manuscript/BASELINE_RESULTS.md`;
- limitations are recorded for any optional baseline that is deferred.

## Internal controls already represented

These are internal ablations, not external baselines.

| Control | Local evidence path | Caveat |
|---|---|---|
| No recurrence | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Supports storage/execution dissociation within the benchmark only. |
| No structural plasticity | `experiments/experiment8_self_organizing_route_acquisition/analysis/exp8/exp8_summary.csv`; `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv` | Internal ablation; not an external literature comparator. |
| No context binding or no world context | `experiments/experiment11_context_memory/analysis/exp11/exp11_memory_indices.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`; `experiments/experiment13_breaking_point/analysis/validation_report.md` | Exp13 no-context-binding variant definition remains caveated in the conflict log. |
| Capacity or memory-budget controls | `experiments/experiment13_breaking_point/analysis/capacity_pressure_summary.csv`; `experiments/experiment13_breaking_point/analysis/local_capacity_pressure_summary.csv`; `docs/experiments/exp13_local_vs_global_budget_comparison.md` | Observed aggregate curves only; fitted capacity-law analysis is pending. |
| Context noise/corruption controls | `experiments/experiment13_breaking_point/analysis/context_corruption_summary.csv`; `experiments/experiment12_capacity_generalization/analysis/exp12/context_bleed_summary.csv` | Exp13 adversarial corruption is failure evidence; Exp12 bleed/dropout is diagnostic only. |
