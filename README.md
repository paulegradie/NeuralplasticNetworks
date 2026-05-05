# Context-Indexed Route Memory

This repository contains the experimental code, generated analysis artifacts, and manuscript-preparation materials for a research program on **neuroplastic memory systems**.

The first manuscript being developed from this repository studies a synthetic benchmark for **Continual Compositional Route Memory**: a setting where a model must store and execute multiple incompatible transition systems over the same state/action space without destructive overwriting.

The central working hypothesis is:

> Context-indexed structural plasticity can store incompatible local transition systems without destructive overwriting, while recurrent dynamics are required to convert one-step route memories into multi-step execution.

This is an active research repository. The internal experimental evidence is promising, but the manuscript is **not yet submission-ready**. Current blockers include Experiment 13.1 publication hardening, external baselines, uncertainty reporting, final reproducible figure scripts, and tighter prior-art positioning.

---

## Repository status

Current status: **promising internal research artifact; not yet manuscript-ready.**

The repository currently supports a narrow, benchmark-specific manuscript spine:

- structural plasticity is required for reliable route-memory storage in the benchmark;
- world/context indexing prevents destructive interference between incompatible route systems;
- recurrence is required for multi-step composition even when one-step route memory is intact;
- finite structural capacity reveals breaking behavior;
- current evidence supports composition over stored primitives, not inference of unseen primitive transitions.

The current evidence does **not** claim:

- solved continual learning;
- novelty of context gating by itself;
- a complete hippocampal or biological theory;
- end-to-end perceptual learning;
- broad abstract rule induction;
- inference of unseen primitive transitions.

See:

- [`docs/manuscript/CLAIMS_AND_EVIDENCE.md`](docs/manuscript/CLAIMS_AND_EVIDENCE.md)
- [`docs/manuscript/LIMITATIONS_AND_THREATS.md`](docs/manuscript/LIMITATIONS_AND_THREATS.md)
- [`docs/synthesis/PUBLICATION_READINESS.md`](docs/synthesis/PUBLICATION_READINESS.md)

---

## Scientific framing

The project investigates a controlled memory problem:

> Can a single learning system acquire multiple incompatible route worlds, preserve older worlds while learning newer ones, and execute multi-step routes compositionally?

Each “world” defines a different transition system over the same underlying states and actions. The same state/action pair may require different next states depending on context. This creates a controlled form of interference and rebinding pressure.

The model family explored here decomposes the problem into three interacting mechanisms:

| Function | Mechanism |
|---|---|
| Store local transitions | Structural plasticity / route fields |
| Select the relevant transition system | World/context indexing |
| Execute multi-step behavior | Recurrence |

The current strongest internal result is the dissociation between **route-table memory** and **multi-step composition**: no-recurrence variants can preserve local one-step route memory while failing multi-step execution.

---

## Repository layout

```text
.
├── experiments/
│   ├── experiment1/
│   ├── experiment2/
│   ├── experiment3/
│   ├── experiment4_successor/
│   ├── experiment5_contextual_successor/
│   ├── experiment6_route_audit_successor/
│   ├── experiment7_route_field_diagnostics/
│   ├── experiment8_self_organizing_route_acquisition/
│   ├── experiment9_robust_adaptive_route_plasticity/
│   ├── experiment10_adaptive_reversal/
│   ├── experiment11_context_memory/
│   ├── experiment12_capacity_generalization/
│   └── experiment13_breaking_point/
│
├── docs/
│   ├── experiments/
│   ├── manuscript/
│   ├── repo_audit/
│   ├── source_data/
│   ├── synthesis/
│   ├── theory/
│   └── threads/
│
├── scripts/
│   └── verify_doc_source_paths.py
│
├── AGENTS.md
├── README.md
└── .gitattributes
````

### `experiments/`

Each experiment is intended to be self-contained, with its own code, run scripts, generated artifacts, and local documentation.

Generated outputs are preserved because the repository is being used not only as code, but also as a manuscript evidence archive.

### `docs/`

The `docs/` directory contains the manuscript preparation system:

| Path                                                                                       | Purpose                                        |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| [`docs/manuscript/CLAIMS_AND_EVIDENCE.md`](docs/manuscript/CLAIMS_AND_EVIDENCE.md)         | Canonical claim/evidence/caveat map            |
| [`docs/manuscript/FIGURE_PLAN.md`](docs/manuscript/FIGURE_PLAN.md)                         | Candidate manuscript figure plan               |
| [`docs/manuscript/LIMITATIONS_AND_THREATS.md`](docs/manuscript/LIMITATIONS_AND_THREATS.md) | Reviewer risks, caveats, and non-claims        |
| [`docs/manuscript/MANUSCRIPT_TODO.md`](docs/manuscript/MANUSCRIPT_TODO.md)                 | P0/P1/P2 manuscript work queue                 |
| [`docs/experiments/EXPERIMENT_REGISTRY.md`](docs/experiments/EXPERIMENT_REGISTRY.md)       | Experiment index and manuscript role           |
| [`docs/synthesis/PROJECT_STATUS.md`](docs/synthesis/PROJECT_STATUS.md)                     | Current project synthesis                      |
| [`docs/synthesis/PUBLICATION_READINESS.md`](docs/synthesis/PUBLICATION_READINESS.md)       | Readiness assessment and reviewer-risk matrix  |
| [`docs/synthesis/NEXT_EXPERIMENTS.md`](docs/synthesis/NEXT_EXPERIMENTS.md)                 | Planned Exp13.1, baselines, and applied bridge |
| [`docs/repo_audit/REPRODUCIBILITY_AUDIT.md`](docs/repo_audit/REPRODUCIBILITY_AUDIT.md)     | Current reproducibility status                 |
| [`docs/threads/THREAD_INDEX.md`](docs/threads/THREAD_INDEX.md)                             | Imported ChatGPT analysis thread map           |

---

## Experiment overview

| Experiment | Directory                                                                                                                | Current manuscript role                                            |
| ---------: | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
|       Exp1 | [`experiments/experiment1`](experiments/experiment1)                                                                     | Early exploratory / historical                                     |
|       Exp2 | [`experiments/experiment2`](experiments/experiment2)                                                                     | Early exploratory / historical                                     |
|       Exp3 | [`experiments/experiment3`](experiments/experiment3)                                                                     | Early recurrent MNIST/plastic-graph background                     |
|       Exp4 | [`experiments/experiment4_successor`](experiments/experiment4_successor)                                                 | Route composition foundation                                       |
|       Exp5 | [`experiments/experiment5_contextual_successor`](experiments/experiment5_contextual_successor)                           | Caveated contextual predecessor                                    |
|       Exp6 | [`experiments/experiment6_route_audit_successor`](experiments/experiment6_route_audit_successor)                         | Negative/informative route-audit correction                        |
|       Exp7 | [`experiments/experiment7_route_field_diagnostics`](experiments/experiment7_route_field_diagnostics)                     | Route-field diagnostic foundation                                  |
|       Exp8 | [`experiments/experiment8_self_organizing_route_acquisition`](experiments/experiment8_self_organizing_route_acquisition) | Self-organizing route acquisition                                  |
|       Exp9 | [`experiments/experiment9_robust_adaptive_route_plasticity`](experiments/experiment9_robust_adaptive_route_plasticity)   | Robustness / inhibition / feedback stress tests                    |
|      Exp10 | [`experiments/experiment10_adaptive_reversal`](experiments/experiment10_adaptive_reversal)                               | Adaptive reversal and consolidation tradeoff                       |
|      Exp11 | [`experiments/experiment11_context_memory`](experiments/experiment11_context_memory)                                     | Incompatible-world context memory                                  |
|      Exp12 | [`experiments/experiment12_capacity_generalization`](experiments/experiment12_capacity_generalization)                   | Capacity scaling, retention, held-out composition                  |
|      Exp13 | [`experiments/experiment13_breaking_point`](experiments/experiment13_breaking_point)                                     | Boundary mapping: capacity, corruption, holdout, continuous bridge |

The current candidate main-result spine primarily comes from **Experiments 11–13**, with Experiments 7–10 providing mechanism-building and historical context.

---

## Current claim map

The active manuscript claim map is maintained in:

[`docs/manuscript/CLAIMS_AND_EVIDENCE.md`](docs/manuscript/CLAIMS_AND_EVIDENCE.md)

Each claim is tracked using the pattern:

```text
Claim -> Evidence -> Caveat -> Source path
```

Current claim-status labels include:

* `Strong`
* `Promising`
* `Preliminary`
* `Needs baseline`
* `Needs metric cleanup`
* `Needs rerun`
* `Unsupported`
* `Framing only`

The most important current claims are:

1. Structural plasticity is required for reliable route-memory storage in this symbolic benchmark family.
2. World/context indexing prevents destructive interference between incompatible route systems.
3. Recurrence is required for multi-step composition even when one-step route memory is intact.
4. Route-table memory and compositional execution are separable.
5. Capacity scaling remains stable under clean context up to the tested world counts.
6. Finite structural budget produces an observed performance degradation curve.
7. Local structural budget pressure appears more damaging to long-route execution than global budget pressure.
8. Consolidation acts as a stability-plasticity bias rather than a universally necessary accuracy mechanism.
9. The model composes seen primitives but does not infer unseen primitive transitions.
10. Adversarial context corruption can collapse route execution when world selection flips to the wrong context.
11. Continuous/noisy input decoding can feed the route-memory mechanism, but remains preliminary.
12. External baselines and prior-art comparison are required before submission-readiness can be claimed.

---

## Key current findings

### Structural plasticity stores route memories

Ablations that remove structural plasticity fail to acquire reliable route-table memories in the current benchmark family.

This supports a benchmark-specific claim: structural plasticity is necessary for the route-memory substrate used here.

It does **not** prove that structural plasticity is universally necessary for all neural learning systems.

### World/context indexing prevents interference

When incompatible route worlds are trained sequentially, world/context indexing prevents the transition systems from collapsing into a shared interfering route table.

No-world-context variants degrade as the number of incompatible worlds increases.

### Recurrence executes composition

No-recurrence variants can preserve one-step route-table accuracy while failing multi-step route execution.

This is one of the project’s cleanest internal dissociations:

> local transition memory and recurrent compositional execution are separable.

### Capacity pressure reveals breaking behavior

Experiment 13 pushes the model out of the Experiment 12 ceiling regime by imposing structural memory pressure.

Global capacity pressure produces an observed degradation curve. Local capacity pressure appears more damaging to long-route composition, though formal paired comparison and confidence intervals remain required.

### Generalization boundary

The model composes over stored primitives. It does not currently infer unseen primitive transitions.

This distinction is central to the manuscript framing.

### Continuous-input bridge is preliminary

Experiment 13 includes a noisy continuous front-end bridge. This shows that route memory can operate downstream of degraded state decoding, but it does not show end-to-end perceptual learning.

---

## Reproducing experiments

The repository currently contains experiment-specific launch scripts. The reproducibility audit is maintained in:

[`docs/repo_audit/REPRODUCIBILITY_AUDIT.md`](docs/repo_audit/REPRODUCIBILITY_AUDIT.md)

The long-term target run interface is:

```powershell
powershell -ExecutionPolicy Bypass -File .\experiments\<experiment-directory>\start_exp<N>.ps1 -Profile smoke -Clean
powershell -ExecutionPolicy Bypass -File .\experiments\<experiment-directory>\start_exp<N>.ps1 -Profile standard -Clean
powershell -ExecutionPolicy Bypass -File .\experiments\<experiment-directory>\start_exp<N>.ps1 -Profile full -Clean
```

Not every historical experiment currently follows this exact interface. Some early experiments have older launcher names or historical run conventions.

Before using any experiment result in a manuscript, confirm:

* the run command;
* the profile;
* the seed count;
* the generated output path;
* the validation status;
* whether the output is historical, diagnostic, or manuscript-candidate evidence.

---

## Path and evidence verification

The repository includes or is expected to include a documentation path verifier:

```bash
python scripts/verify_doc_source_paths.py
```

The purpose of this script is to ensure that active source paths cited in manuscript and evidence documents resolve to real local files.

Generated path verification reports should live under:

```text
docs/repo_audit/
```

---

## Current P0/P1 work

The current manuscript work queue is maintained in:

[`docs/manuscript/MANUSCRIPT_TODO.md`](docs/manuscript/MANUSCRIPT_TODO.md)

### P0 before manuscript submission

* Complete Experiment 13.1 publication-hardening audit.
* Add external baseline suite.
* Add seed-level confidence intervals and effect sizes.
* Fix holdout metrics.
* Rename or rerun the no-context-binding ablation.
* Import the novelty assessment as a local artifact.
* Consolidate all analysis artifacts and thread digests.
* Create final paper figures from reproducible scripts.

### P1 strongly recommended

* Add stochastic context corruption.
* Run consolidation dose-response.
* Fit capacity laws.
* Upgrade local-vs-global comparison.
* Design latent world inference experiment.
* Build applied visual-state route-memory bridge.

---

## Planned next experiments

### Experiment 13.1 — Publication hardening

Experiment 13.1 should be implemented as a new experiment directory, not by modifying Experiment 13 in place.

Primary goals:

* split route-table accuracy into all/seen/unseen metrics;
* add seed-level confidence intervals and effect sizes;
* clean up the no-context-binding ablation;
* add stochastic context corruption;
* run consolidation dose-response under finite capacity;
* create publication-grade summary tables and figure panels.

See:

[`docs/synthesis/NEXT_EXPERIMENTS.md`](docs/synthesis/NEXT_EXPERIMENTS.md)

### Baseline suite

External baselines are required before submission-readiness can be claimed.

Planned baseline families include:

* context-dependent gating / XdG-style comparator;
* synaptic stabilization / stabilization-plus-gating comparator;
* replay comparator;
* task masks / HAT-style comparator;
* parameter isolation / PackNet-style comparator;
* task-conditioned weights / hypernetwork comparator;
* superposition comparator;
* cognitive-map / CSCG / TEM-style comparator.

See:

[`docs/manuscript/BASELINE_REQUIREMENTS.md`](docs/manuscript/BASELINE_REQUIREMENTS.md)

### Applied bridge

A future applied bridge should test visual-state or perceptually grounded route memory.

The current continuous/noisy front-end in Experiment 13 is preliminary and should not be framed as end-to-end perception.

---

## Working with this repository

See [`AGENTS.md`](AGENTS.md) for workspace rules.

Core principles:

* Experiments live under `experiments/`.
* Each experiment is self-contained.
* Historical experiment outputs should be treated as immutable records.
* New scientific protocols should get new experiment directories.
* Reruns of the same protocol should be recorded under the owning experiment’s run/analysis convention.
* Manuscript claims must cite source artifacts.
* Do not strengthen claims without evidence.
* Use `Claim -> Evidence -> Caveat -> Source path`.

---

## Research program

This repository is the first manuscript-oriented repository in a broader research direction on **neuroplastic memory systems**.

The long-term direction includes:

* latent world inference;
* self-indexed memory allocation;
* perceptually grounded route memory;
* stronger baseline comparisons;
* biologically inspired but carefully bounded memory models;
* structural plasticity as an explicit computational substrate for context-specific memory.

---

## Citation

No formal citation is available yet. This repository is under active manuscript preparation.

If referencing the work informally, use:

```text
Context-Indexed Route Memory, GradieResearch, GitHub repository.
```

A formal citation will be added if and when a preprint or manuscript is released.

---

## License

TODO: Add license.

Until a license is added, reuse rights are not formally granted. Add an explicit license before public reuse, external collaboration, or publication-linked release.
