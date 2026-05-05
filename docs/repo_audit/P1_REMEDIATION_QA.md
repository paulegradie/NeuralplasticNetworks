# P1 Remediation QA

## Summary

Scoped QA found the P1 remediation suitable for handoff to Exp13.1 planning. The reviewed docs now orient external readers, keep new experiment work under `experiments/`, distinguish reruns from successor protocols, and preserve the active readiness status: promising but not submission-ready.

The documentation path verifier was run locally and passed with zero missing active paths. The remaining skipped paths were explicitly marked planned/future or missing/local-verification-pending. The reproducibility audit gives useful Exp11-Exp13 commands while clearly saying those commands were inspected, not executed, in the P1 pass.

## Checklist

| Check | Result | Evidence | Notes |
|---|---|---|---|
| README is useful to an external reader. | Pass | `README.md` explains purpose, status, scientific question, layout, start docs, experiment overview, claim map, non-claims, reproducibility, next work, and license caveat. | External reuse remains caveated because license/citation are TODO, but this is stated plainly. |
| README links resolve. | Pass | README links point to existing docs under `docs/manuscript/`, `docs/synthesis/`, `docs/repo_audit/`, and `docs/experiments/`. | Checked local markdown links; no broken README links found. |
| AGENTS.md aligns with the `experiments/` structure. | Pass | `AGENTS.md` says experiments live under `experiments/`, new experiments must be created there, and root-level experiment directories should not be created. | Matches current repository organization. |
| AGENTS.md distinguishes reruns from successor experiments. | Pass | `AGENTS.md` has a dedicated "Reruns vs Successor Experiments" section. | Reruns remain under the owning experiment; changed protocols get a new directory under `experiments/`. |
| REPRODUCIBILITY_AUDIT.md gives useful commands for Exp11-Exp13. | Pass | `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` lists Exp11 `-ValidationOnly`, Exp12 `-Profile validate/full -OutDir ...`, and Exp13 `-Profile smoke/standard/full -Clean`. | Launcher parameters were cross-checked against `start_exp11.ps1`, `start_exp12.ps1`, and `start_exp13.ps1`. |
| REPRODUCIBILITY_AUDIT.md does not claim unexecuted commands were tested. | Pass | The audit summary and command table state commands were inspected but not executed in P1. | This is appropriately conservative. |
| BASELINE_REQUIREMENTS.md is actionable but does not pretend baselines have been run. | Pass | `docs/manuscript/BASELINE_REQUIREMENTS.md` marks all baseline rows as planned and includes contracts, metrics, acceptance criteria, and organization guidance. | It explicitly says the document is planning, not evidence of baseline performance. |
| MANUSCRIPT_SPINE.md is a real manuscript architecture but does not overclaim. | Pass | `docs/manuscript/MANUSCRIPT_SPINE.md` includes title options, abstract skeleton, main claim, non-claims, section outline, storyboard, caveats, and blockers. | Claims remain benchmark-specific and repeatedly caveat missing baselines, uncertainty, Exp13.1 cleanup, and citations. |
| Synthesis docs use current structure and current readiness status. | Pass | `docs/synthesis/PROJECT_STATUS.md`, `PUBLICATION_READINESS.md`, and `NEXT_EXPERIMENTS.md` direct future work to new directories under `experiments/` and state not submission/manuscript-ready. | No stale active root-level experiment plan found in the reviewed synthesis docs. |
| P1 remediation report accurately describes what changed. | Pass | `docs/repo_audit/P1_REMEDIATION_REPORT.md` matches staged changes: README, AGENTS, reproducibility audit, baseline requirements, manuscript spine/TODO, synthesis docs, supporting audit docs, and CI workflow. | The report also preserves remaining caveats rather than claiming scientific completion. |
| Path verifier passes or reports only intentional/future/pending paths. | Pass | Ran `python scripts/verify_doc_source_paths.py`: missing active paths 0; skipped planned/future paths 15; skipped local-verification-pending paths 34. | Skipped examples include planned Exp13.1/baseline dirs and missing `Pasted text.txt`, all explicitly marked. |
| No scientific claims were strengthened during cleanup. | Pass | Reviewed README, manuscript spine, baseline requirements, synthesis docs, and P1 report wording against the canonical evidence stance. | Wording remains limited to internal/benchmark-specific evidence and keeps external baselines, Exp13.1, uncertainty, and final figures as blockers. |

## Problems found

No P0, P1, or P2 problems were found in the scoped P1 remediation review.

Residual caveats are already documented in the remediation work: Exp11-Exp13 commands still need fresh-checkout execution, baselines have not been run, Exp13.1 is not implemented, uncertainty reporting is pending, and final manuscript figures are not yet reproducible paper outputs.

## Final recommendation

ready to proceed to Exp13.1 planning;
