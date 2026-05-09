# Context-Indexed Route Memory

## What this repository contains

This repository contains a research project on context-indexed route-memory experiments. It studies a controlled compositional route-memory benchmark where a model must store and execute multiple incompatible transition systems over the same symbolic state and action space.

Experiments live under `experiments/`. Each experiment directory is intended to be self-contained, with its own code, runner scripts, analysis scripts, generated reports, `runs/`, and `analysis/` outputs as needed. Generated analysis artifacts are preserved as historical evidence rather than deleted or overwritten.

Manuscript, evidence, synthesis, source-data, finalization, and repo-audit documents live under `docs/`. This is an active manuscript-preparation repository, so active source paths in evidence docs should use the current `experiments/...` prefix and should resolve locally unless they are explicitly marked planned, missing, future, or local verification pending.

## Current status

The repository is now in a **post-Exp15 / post-Manuscript-V2 finalization state**.

Completed manuscript-relevant imports and drafts:

- Exp13.2 is imported as completed symbolic/algorithmic baseline-suite evidence.
- Exp14 is imported as completed symbolic transition-cue context-selection evidence.
- Exp15 is imported as completed minimal fixed-profile neural-comparator evidence.
- `docs/manuscript/draft/MANUSCRIPT_V2.md` has been captured.
- `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md` narrows the claim posture after Exp15.
- `docs/manuscript/tables/table_04_exp15_neural_comparator.md` and `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv` provide a compact V2 Exp15 comparator table.

The repository is **not submission-ready**. Current blockers are retained-claim selection, manuscript-grade seed-level uncertainty/effect-size reporting, final source-data-backed figure/table review, prior-art/novelty import, fresh command verification, and license/citation metadata.

The strongest current manuscript posture is deliberately narrow: this is a controlled symbolic/mechanistic benchmark and evidence map. It supports claims about context-indexed storage, recurrent execution, endpoint-vs-transition composition, finite-budget boundaries, symbolic transition-cue context selection, and minimal neural comparator behavior. It does **not** support broad CIRM-over-neural-model claims or solved continual-learning claims.

## Scientific question

The central question is whether a system can store many route memories that reuse the same states and actions but require different transitions in different contexts. For example, the same symbolic action can imply different successor transitions in world A, world B, and world C.

The benchmark separates mechanisms that are easy to conflate:

- one-step route-table storage;
- selection of the right world/context;
- recurrent multi-step execution over stored transitions;
- endpoint memorization versus reusable transition composition;
- finite structural capacity and local/global budget pressure;
- supplied context versus symbolic transition-cue context selection;
- symbolic/algorithmic and minimal neural baseline contracts.

The narrow scientific question for the first manuscript is: in this controlled route-memory benchmark, how do context-indexed transition storage, recurrent execution, symbolic context selection, endpoint memorization, and neural transition learners differ under incompatible transition systems and finite-capacity pressure?

## Repository layout

```text
experiments/  self-contained experiment directories and generated artifacts
docs/         manuscript, evidence, synthesis, source-data, finalization, and repo-audit docs
scripts/      repository utilities, including documentation path verification and manuscript asset helpers
AGENTS.md     repository working rules for local agents
README.md     external-facing repository entry point
```

## Where to start

- [Documentation index](docs/README.md)
- [Source of truth](docs/manuscript/SOURCE_OF_TRUTH.md)
- [Manuscript V2 draft](docs/manuscript/draft/MANUSCRIPT_V2.md)
- [Post-Exp15 claim freeze addendum](docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md)
- [Claims and evidence](docs/manuscript/CLAIMS_AND_EVIDENCE.md)
- [Finalization checklist](docs/manuscript/finalization/FINALIZATION_CHECKLIST.md)
- [Next step prompt](docs/manuscript/finalization/NEXT_STEP_PROMPT.md)
- [Figure plan](docs/manuscript/FIGURE_PLAN.md)
- [Limitations and threats](docs/manuscript/LIMITATIONS_AND_THREATS.md)
- [Publication readiness](docs/synthesis/PUBLICATION_READINESS.md)
- [Next experiments / next work](docs/synthesis/NEXT_EXPERIMENTS.md)
- [Reproducibility audit](docs/repo_audit/REPRODUCIBILITY_AUDIT.md)
- [Experiment registry](docs/experiments/EXPERIMENT_REGISTRY.md)
- [Historical experiment tiers](docs/experiments/HISTORICAL_EXPERIMENTS.md)

## Experiment overview

| Experiment | Directory | Role | Status / manuscript relevance |
|---|---|---|---|
| Exp1 | `experiments/experiment1/` | Early MNIST plastic-graph prototype. | Historical; not central to route-memory claims. |
| Exp2 | `experiments/experiment2/` | Persistent plastic-graph MNIST exploration. | Historical/local evidence only. |
| Exp3 | `experiments/experiment3/` | Recurrent MNIST and controlled variants. | Historical context for recurrence exploration. |
| Exp4 | `experiments/experiment4_successor/` | Successor traversal and route-composition foundation. | Precursor evidence; not the main context-memory result. |
| Exp5 | `experiments/experiment5_contextual_successor/` | Contextual successor attempt. | Caveated predecessor; useful for failure history. |
| Exp6 | `experiments/experiment6_route_audit_successor/` | Route-audit correction of contextual successor task. | Methodological precursor; caveated. |
| Exp7 | `experiments/experiment7_route_field_diagnostics/` | Clean route-field diagnostic. | Supports route-table versus execution distinction as diagnostic evidence. |
| Exp8 | `experiments/experiment8_self_organizing_route_acquisition/` | Self-organizing route acquisition. | Important internal ablation evidence; now framed with baseline caveats. |
| Exp9 | `experiments/experiment9_robust_adaptive_route_plasticity/` | Robustness, context bleed, delayed/noisy feedback. | Supporting stress-test evidence; claims remain narrow. |
| Exp10 | `experiments/experiment10_adaptive_reversal/` | Adaptive reversal and consolidation tradeoff. | Supporting evidence for stability/plasticity caveats. |
| Exp11 | `experiments/experiment11_context_memory/` | Context-separated incompatible-world memory. | Manuscript-critical internal evidence. |
| Exp12 | `experiments/experiment12_capacity_generalization/` | Capacity, retention, and held-out composition scaling. | Manuscript-critical internal evidence; ceiling-limited. |
| Exp13 | `experiments/experiment13_breaking_point/` | Breaking point, context corruption, holdout boundary, continuous bridge. | Manuscript-critical boundary evidence; holdout and context-corruption caveats remain. |
| Exp13.1 | `experiments/experiment13_1_publication_hardening/` | Publication-hardening ablations and mechanism audit. | Manuscript-critical internal evidence; lesion diagnostic failed expected pattern and must not be used as positive evidence without audit/rerun. |
| Exp13.2 | `experiments/experiment13_2_baseline_suite/` | Symbolic/algorithmic baseline suite. | Imported completed evidence; oracle context-gated lookup matches CIRM in the clean supplied-context benchmark, narrowing novelty claims. |
| Exp14 | `experiments/experiment14_latent_context_inference/` | Symbolic transition-cue context selection. | Imported completed evidence; supports symbolic context selection, not raw sensory latent-world discovery. |
| Exp15 | `experiments/experiment15_neural_baseline_comparator/` | Minimal neural baseline comparator. | Imported completed evidence; fixed-profile and non-exhaustive. Context-conditioned transition MLP and world-head MLP solve the clean hard slice. |

## Current claim map

The canonical claim table is [CLAIMS_AND_EVIDENCE.md](docs/manuscript/CLAIMS_AND_EVIDENCE.md). The post-Exp15 narrowing layer is [POST_EXP15_CLAIM_FREEZE_ADDENDUM.md](docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md). At a high level:

| Claim IDs | Current interpretation | Status |
|---|---|---|
| C1-C4 | Structural route storage, world/context indexing, recurrence, and route-table/execution separation are supported inside the route-memory benchmark, with Exp15 narrowing any universal wording. | Strong but benchmark-specific; no broad neural-superiority claim. |
| C5-C7 | Exp12 shows clean supplied-context scaling; Exp13 and Exp13.1 map finite-capacity/local-budget failure. | Promising but needs retained-claim statistical hardening and final figure/table review. |
| C8 | Consolidation is best framed as a stability/plasticity bias. | Preliminary/supplementary. |
| C9 | The model composes stored primitives but does not infer unseen primitive transitions. | Keep out of the main claim set unless metric cleanup is completed. |
| C10 | Wrong-world context evidence or corrupted symbolic cues can break execution when selection flips. | Narrow boundary claim, not generic stochastic robustness. |
| C11 | Continuous/noisy inputs can feed route memory through a simple decoded bridge. | Preliminary or supplementary. |
| C12 | Symbolic/algorithmic and minimal neural baselines are now present, but prior-art import and broader neural-baseline decisions remain open. | Partially satisfied; still a submission-readiness blocker. |
| C13 | Symbolic transition cues can select the active world/context before route execution. | Promising; main-vs-supplement placement still needs human decision. |

Every manuscript-facing use should retain the discipline: Claim -> Evidence -> Caveat -> Source path.

## Non-claims

This repository does not show:

- solved continual learning;
- broad CIRM superiority over neural models;
- that context gating is novel by itself;
- a complete hippocampal or biological theory;
- raw sensory latent-world discovery;
- end-to-end perceptual learning;
- broad abstract rule induction;
- inference of unseen primitive transitions;
- a general scientific conclusion from the Exp15 replay collapse without audit.

## Reproducibility

See [REPRODUCIBILITY_AUDIT.md](docs/repo_audit/REPRODUCIBILITY_AUDIT.md). Commands are being standardized, but early experiments may not follow the final `smoke` / `validation` / `full` interface. Manuscript-critical experiments have clearer launch paths than historical experiments, but fresh command verification and runtime/hardware logs are still required before submission.

To check active documentation source paths, run:

```bash
python scripts/verify_doc_source_paths.py
```

## Planned next work

The next planned manuscript-readiness step is **Analysis Pass 15A: retained-claim and statistical hardening**. Use:

```text
docs/manuscript/finalization/NEXT_STEP_PROMPT.md
```

That pass should decide retained main claims, map each retained claim to exact source CSVs, update manuscript-grade CI/effect-size readiness, and harden final source-data-backed figures/tables. Do not start another experiment by default.

Optional follow-up experiments or audits should only be started if the retained claim set or target venue requires them: memory-augmented/key-value neural baseline, Exp15 replay audit, Exp13.1 lesion audit, C9 metric cleanup, stochastic context corruption, consolidation dose-response, or a non-symbolic applied bridge.

## License / citation

TODO: Add a license and citation instructions. Until a license is added, reuse rights are not formally granted.
