# Documentation Index

Purpose: Make the `docs/` tree navigable for humans and future local agents.

## Start here

Recommended reading order:

1. `../README.md`
2. `docs/manuscript/SOURCE_OF_TRUTH.md`
3. `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
4. `docs/synthesis/PUBLICATION_READINESS.md`
5. `docs/manuscript/LIMITATIONS_AND_THREATS.md`
6. `docs/experiments/EXPERIMENT_REGISTRY.md`
7. `docs/manuscript/FIGURE_PLAN.md`
8. `docs/synthesis/NEXT_EXPERIMENTS.md`

## Manuscript docs

| Document | Purpose | Status | When to edit |
|---|---|---|---|
| `docs/manuscript/SOURCE_OF_TRUTH.md` | Rules for resolving conflicts between docs, artifacts, and thread exports. | Active handoff note | Edit when canonical-document ownership or experiment integration status changes. |
| `docs/manuscript/CLAIMS_AND_EVIDENCE.md` | Canonical claim map using Claim -> Evidence -> Caveat -> Source path. | Active source of truth | Edit whenever claim wording, status, evidence, caveat, or source paths change. |
| `docs/manuscript/MANUSCRIPT_SPINE.md` | Provisional manuscript architecture and section plan. | Active draft scaffold; needs final claim freeze before prose drafting | Edit when manuscript structure changes after claim-freeze, figure, or baseline decisions. |
| `docs/manuscript/MANUSCRIPT_TODO.md` | Conservative work queue for manuscript readiness. | Active work queue | Edit when work status changes or a blocker is completed with local evidence. |
| `docs/manuscript/FIGURE_PLAN.md` | Candidate main and supplementary figure map. | Active planning doc | Edit whenever a figure, panel, source artifact, or caveat changes. |
| `docs/manuscript/LIMITATIONS_AND_THREATS.md` | Reviewer-risk and non-claim tracker. | Active caveat doc | Edit when a limitation is resolved or a new risk appears. |
| `docs/manuscript/BASELINE_REQUIREMENTS.md` | Baseline suite contracts, completed Exp13.2 symbolic baselines, and remaining baseline/prior-art gaps. | Active baseline-readiness doc | Edit when baseline artifacts, neural-baseline decisions, or prior-art requirements change. |
| `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` | Proposed first-manuscript claim freeze created after Exp13.2/Exp14 consistency cleanup. | Active draft freeze | Edit only through explicit claim-freeze/hardening passes. |

## Experiment docs

| Document | Purpose | Status |
|---|---|---|
| `docs/experiments/EXPERIMENT_REGISTRY.md` | Conservative index of experiment directories, thread digests, artifacts, roles, and follow-up needs. | Active registry |
| `docs/experiments/HISTORICAL_EXPERIMENTS.md` | Separates manuscript-critical, supporting, and historical experiments. | Active navigation aid |
| `docs/experiments/exp*_summary.md` | Per-experiment summaries imported from local artifacts and thread digests. | Active summaries with human/manuscript validation pending |
| `docs/experiments/exp13_local_vs_global_budget_comparison.md` | Docs-only aggregate comparison for Exp13 local-vs-global pressure. | Preliminary; paired seed-level analysis pending |
| `EXPERIMENT_ARTIFACTS_INDEX.csv` | Index of detected experiment artifacts. | Review aid |
| `EXPERIMENT_CLAIMS_MATRIX.csv` | Experiment-to-claim mapping aid. | Review aid |

## Repo audit docs

| Document | Purpose | Status |
|---|---|---|
| `docs/repo_audit/P0_REMEDIATION_REPORT.md` | Documents P0 fixes for paths, docs CSV reviewability, and path verification. | Completed repo-readiness record |
| `docs/repo_audit/P0_REMEDIATION_QA.md` | QA result for P0 remediation. | Completed QA record |
| `docs/repo_audit/P1_REMEDIATION_REPORT.md` | Documents P1 onboarding, reproducibility, baseline planning, and manuscript-spine cleanup. | Completed repo-readiness record |
| `docs/repo_audit/P1_REMEDIATION_QA.md` | QA result for P1 remediation. | Completed QA record |
| `docs/repo_audit/P2_REMEDIATION_REPORT.md` | Documents this P2 polish pass. | Active during P2, then completed record |
| `docs/repo_audit/REPRODUCIBILITY_AUDIT.md` | Run-interface and reproducibility map. | Active audit; commands inspected, not fully rerun in P1/P2 |
| `docs/repo_audit/PATH_VERIFICATION_REPORT.md` | Records path-verifier expectations and prior results. | Active audit support |
| `docs/repo_audit/MISSING_ARTIFACTS.md` | Tracks missing or local-verification-pending artifacts. | Active caveat tracker |
| `docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md` | Records Exp13.2 baseline-suite import and caveats. | Completed import record |
| `docs/repo_audit/EXP14_ANALYSIS_IMPORT_REPORT.md` | Records Exp14 latent-context import and caveats. | Completed import record |

## Source-data docs

| Document | Purpose | Status |
|---|---|---|
| `docs/source_data/README.md` | Describes review-friendly mirrors and authoritative experiment sources. | Active source-data guide |
| `docs/source_data/SOURCE_DATA_MANIFEST.csv` | Tracks which source-data mirrors support candidate figures/claims. | Active manifest; final figure scripts still missing |
| `docs/source_data/STATISTICAL_REPORTING_READINESS.csv` | Tracks seed-level uncertainty and effect-size readiness by claim. | Active readiness checklist |

## Theory docs

| Document | Purpose | Status |
|---|---|---|
| `docs/theory/GLOSSARY.md` | Project-specific terminology definitions. | Active terminology guide |
| `docs/theory/CORE_THEORY.md` | Early core-theory scaffold. | Framing only |
| `docs/theory/BIOLOGICAL_FRAMING.md` | Biological-inspiration caveats. | Framing only |
| `docs/theory/PRIOR_ART_MAP.md` | Prior-art map scaffold. | Planned; citation import pending |

## Thread imports

Thread exports under `docs/threads/` are source material. They may preserve historical wording, old paths, or exploratory interpretations from earlier conversations.

Active claims live in `docs/manuscript/CLAIMS_AND_EVIDENCE.md`. Use thread exports as historical context unless their interpretation has been imported into current evidence docs with a local source path and caveat.

## Rule for future edits

- Update `docs/manuscript/CLAIMS_AND_EVIDENCE.md` when a claim changes.
- Update `docs/manuscript/FIGURE_PLAN.md` when a figure changes.
- Update `docs/manuscript/MANUSCRIPT_TODO.md` when work status changes.
- Update `docs/source_data/SOURCE_DATA_MANIFEST.csv` when a retained figure/table needs a source-data mirror.
- Run `python scripts/verify_doc_source_paths.py` after source-path-heavy edits.
