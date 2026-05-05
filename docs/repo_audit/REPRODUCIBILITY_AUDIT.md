# Reproducibility Audit

## Goal

Can a new researcher clone the repo, run key experiments, regenerate metrics, regenerate plots, and reproduce manuscript claims?

## Current summary

Current status: partially reproducible.

Existing artifacts are present for the manuscript-critical experiments, and the main launch scripts can be identified. Commands in this audit were inspected from README files and launcher scripts, but they were not executed in this P1 pass. Manuscript-critical experiments still need standardized smoke/standard/full documentation, runtime notes, and final figure-regeneration commands before submission.

## Environment

Python version: no formal repository-wide Python version is pinned. Python 3.10+ is recommended for the current utility scripts because `scripts/verify_doc_source_paths.py` uses modern type-hint syntax.

Package installation:

- There is no root-level requirements file.
- Each experiment has its own `requirements.txt`.
- Exp11 requirements: `experiments/experiment11_context_memory/requirements.txt`.
- Exp12 requirements: `experiments/experiment12_capacity_generalization/requirements.txt`.
- Exp13 requirements: `experiments/experiment13_breaking_point/requirements.txt`.
- Exp11 and Exp12 launchers can install or validate local requirements; Exp13 should be installed manually from its requirements file before running if the environment is fresh.

GPU expectations:

- The manuscript-critical Exp11-Exp13 code paths inspected here are NumPy/Pandas/Matplotlib style workloads, not PyTorch or TensorFlow GPU workloads.
- Exp13 explicitly documents that it does not require PyTorch, TensorFlow, torchvision, MNIST downloads, or internet access. Source path: `experiments/experiment13_breaking_point/README.md`.
- New future experiments should document GPU use or the reason GPU use is not appropriate, following `AGENTS.md`.

## Manuscript-critical experiments

| Experiment | Directory | Primary launcher | Smoke/validation command | Standard/full command | Expected outputs | Validation/report artifact | Status | Caveat |
|---|---|---|---|---|---|---|---|---|
| Exp11 | `experiments/experiment11_context_memory/` | `experiments/experiment11_context_memory/start_exp11.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment11_context_memory\start_exp11.ps1 -ValidationOnly` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment11_context_memory\start_exp11.ps1` | `experiments/experiment11_context_memory/analysis/exp11_validation/`; `experiments/experiment11_context_memory/analysis/exp11/` | `experiments/experiment11_context_memory/analysis/exp11_validation/exp11_report.md`; `experiments/experiment11_context_memory/analysis/exp11/exp11_report.md` | Launcher and README inspected; command not executed in P1. | Uses `-ValidationOnly` rather than `-Profile smoke`; full command runs validation before full run. |
| Exp12 | `experiments/experiment12_capacity_generalization/` | `experiments/experiment12_capacity_generalization/start_exp12.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment12_capacity_generalization\start_exp12.ps1 -Profile validate -OutDir analysis/exp12_validation` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment12_capacity_generalization\start_exp12.ps1 -Profile full -OutDir analysis/exp12` | `experiments/experiment12_capacity_generalization/analysis/exp12_validation/`; `experiments/experiment12_capacity_generalization/analysis/exp12/` | `experiments/experiment12_capacity_generalization/analysis/exp12_validation/exp12_report.md`; `experiments/experiment12_capacity_generalization/analysis/exp12/exp12_report.md` | Launcher and README inspected; command not executed in P1. | Actual profiles are `validate`, `full`, and `custom`, not the final target `smoke` / `standard` / `full` set. |
| Exp13 | `experiments/experiment13_breaking_point/` | `experiments/experiment13_breaking_point/start_exp13.ps1` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile smoke -Clean` | `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile standard -Clean`; `powershell -ExecutionPolicy Bypass -File .\experiments\experiment13_breaking_point\start_exp13.ps1 -Profile full -Clean` | `experiments/experiment13_breaking_point/analysis/metrics.csv`; summary CSVs; `experiments/experiment13_breaking_point/analysis/plots/` | `experiments/experiment13_breaking_point/analysis/exp13_report.md`; `experiments/experiment13_breaking_point/analysis/validation_report.md` | Launcher and README inspected; command not executed in P1. | Current generated artifact is a `standard` run; Exp13.1 is still needed for metric cleanup and hardening. |

## Historical experiments

| Experiment | Launchers found | Role | Reproducibility status | Caveat |
|---|---|---|---|---|
| Exp1 | `experiments/experiment1/start.ps1`; `experiments/experiment1/start.sh`; `experiments/experiment1/run_mnist_experiment.py` | Early MNIST prototype. | Runnable entry points found; not executed in P1. | Historical only for the route-memory manuscript. |
| Exp2 | `experiments/experiment2/start.ps1`; `experiments/experiment2/start.sh`; `experiments/experiment2/run_mnist_experiment.py` | Persistent plastic-graph MNIST exploration. | Entry points and artifacts found; not executed in P1. | No standardized validation profile. |
| Exp3 | `experiments/experiment3/start.ps1`; `experiments/experiment3/start.sh`; `experiments/experiment3/run_experiment_suite.py`; `experiments/experiment3/run_mnist_experiment.py` | Recurrent MNIST variants. | Entry points and suite artifacts found; not executed in P1. | Historical context, not central evidence. |
| Exp4 | `experiments/experiment4_successor/start.ps1`; `experiments/experiment4_successor/start.sh`; `experiments/experiment4_successor/run_exp4_suite.py`; `experiments/experiment4_successor/run_exp4_successor_experiment.py` | Successor traversal foundation. | Entry points and artifacts found; not executed in P1. | Multiple legacy launchers; canonical command still needs confirmation. |
| Exp5 | `experiments/experiment5_contextual_successor/start.ps1`; `experiments/experiment5_contextual_successor/start.sh`; `experiments/experiment5_contextual_successor/run_exp5_suite.py`; `experiments/experiment5_contextual_successor/run_exp5_contextual_successor.py` | Contextual successor predecessor. | Entry points and smoke artifacts found; not executed in P1. | Caveated precursor, not final evidence. |
| Exp6 | `experiments/experiment6_route_audit_successor/start.ps1`; `experiments/experiment6_route_audit_successor/start.sh`; `experiments/experiment6_route_audit_successor/run_exp6_suite.py`; `experiments/experiment6_route_audit_successor/run_exp6_route_audit_successor.py` | Route-audit correction. | Entry points and artifacts found; not executed in P1. | README/result cleanup may still be useful before citing exact numbers. |
| Exp7 | `experiments/experiment7_route_field_diagnostics/start.ps1`; `experiments/experiment7_route_field_diagnostics/start.sh`; `experiments/experiment7_route_field_diagnostics/run_exp7_suite.py`; `experiments/experiment7_route_field_diagnostics/run_exp7_route_field_diagnostics.py` | Route-field diagnostic. | Entry points and artifacts found; not executed in P1. | Validation is nonstandard. |
| Exp8 | `experiments/experiment8_self_organizing_route_acquisition/start_exp8.ps1`; `experiments/experiment8_self_organizing_route_acquisition/start.ps1`; `experiments/experiment8_self_organizing_route_acquisition/run_exp8_suite.py` | Self-organizing route acquisition. | Entry points and validation-named outputs found; not executed in P1. | No single canonical `validation_report.md`. |
| Exp9 | `experiments/experiment9_robust_adaptive_route_plasticity/start_exp9.ps1`; `experiments/experiment9_robust_adaptive_route_plasticity/start.ps1`; `experiments/experiment9_robust_adaptive_route_plasticity/run_exp9_suite.py` | Robust adaptive route plasticity. | Entry points and validation-named outputs found; not executed in P1. | Stress-test evidence only. |
| Exp10 | `experiments/experiment10_adaptive_reversal/start_exp10.ps1`; `experiments/experiment10_adaptive_reversal/start.ps1`; `experiments/experiment10_adaptive_reversal/run_exp10_suite.py` | Adaptive reversal and consolidation tradeoff. | Entry points and validation-named outputs found; not executed in P1. | Not non-destructive memory evidence. |

## Canonical run interface target

Future manuscript-critical experiments should aim for a consistent interface:

```powershell
powershell -ExecutionPolicy Bypass -File .\experiments\<experiment>\start_exp<N>.ps1 -Profile smoke -Clean
powershell -ExecutionPolicy Bypass -File .\experiments\<experiment>\start_exp<N>.ps1 -Profile standard -Clean
powershell -ExecutionPolicy Bypass -File .\experiments\<experiment>\start_exp<N>.ps1 -Profile full -Clean
```

This is a target interface. It should not be read as a claim that every historical experiment already supports it.

## Artifact regeneration

Generated artifacts are committed or preserved in the owning experiment directories as historical records. They should not be overwritten to make documentation tidier.

Final paper figures should eventually be regenerated from scripts with fixed input paths and documented source-data tables. Review-friendly source-data mirrors may exist under `docs/source_data/`, but the original `experiments/...` artifacts remain authoritative unless a future document explicitly says otherwise.

## Path verification

Run:

```bash
python scripts/verify_doc_source_paths.py
```

This verifier checks active local source paths in documentation and skips paths explicitly marked planned, future, missing, or local verification pending.

## Required before manuscript submission

- Verify Exp11, Exp12, and Exp13 smoke or validation commands on a fresh checkout.
- Document runtime, expected outputs, seed counts, and hardware expectations for manuscript-critical runs.
- Add final figure regeneration commands and source-data manifests.
- Add seed-level confidence intervals and effect sizes for core claims.
- Standardize Exp13.1 from the beginning using the target run interface.
- Keep completed generated outputs immutable and create new run files for reruns.
