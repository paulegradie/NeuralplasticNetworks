# Experiment 13.1 Analysis Import Report

## Summary

Imported `docs/imports/experiment13_1_analysis_digest.zip` into the canonical docs system. The package contained one root-level digest, which was staged as `docs/threads/experiment13_1_analysis_digest.md`. Local Exp13.1 artifacts were present, including the SQLite run database, validation report, run manifest, CSV summaries, and plots.

## Import package reviewed

- Zip path: `docs/imports/experiment13_1_analysis_digest.zip`.
- Contents: one required markdown digest, `experiment13_1_analysis_digest.md`, at zip root.
- Checklist: digest begins with `# Thread Digest:` and includes an import package checklist.
- Original zip retained.

## Thread digest imported

Source thread path: `docs/threads/experiment13_1_analysis_digest.md`.

## Local artifacts reviewed

- Run ID: `exp13_1_full_20260506_214756`.
- SQLite database: `experiments/experiment13_1_publication_hardening/runs/exp13_1_full_20260506_214756.sqlite3`.
- Validation: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/validation_report.md`, PASS 27, WARN 0, FAIL 0.
- Run manifest: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/run_manifest.json`.
- Key CSVs: `exp13_1_variant_metrics.csv`, `exp13_1_context_corruption.csv`, `exp13_1_lesion_metrics.csv`, `exp13_1_budget_consolidation.csv`, `exp13_1_freeze_plasticity.csv`.
- Key plots: `exp13_1_recurrence_ablation.png`, `exp13_1_composition_accuracy.png`, `exp13_1_context_confusion.png`, `exp13_1_lesion_sensitivity.png`, `exp13_1_budget_consolidation.png`.

## Docs updated

- `docs/threads/THREAD_INDEX.md`
- `docs/experiments/exp13_1_summary.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `experiments/experiment13_1_publication_hardening/README.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/source_data/README.md`
- `docs/repo_audit/THREAD_IMPORT_CONFLICTS.md`

## Claims changed

| Claim ID | Change | Reason | Source |
|---|---|---|---|
| C1 | Added Exp13.1 structural-plasticity ablation support. | No-structural-plasticity failed in the completed full run. | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` |
| C2 | Added Exp13.1 context-binding support and latent-world caveat. | No-context-binding failed while the full model solved clean composition. | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` |
| C3 | Added Exp13.1 no-recurrence-at-eval support. | Route-table accuracy stayed 1.0 while composition collapsed. | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` |
| C4 | Added Exp13.1 route-table/composition dissociation support. | Same no-recurrence result sharpens separability evidence. | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_variant_metrics.csv` |
| C7 | Promoted from preliminary to promising internal evidence. | Exp13.1 directly reports constrained local budget much worse than constrained global budget. | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` |
| C8 | Refined consolidation caveat. | Exp13.1 did not support constrained-budget accuracy rescue from consolidation strength. | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_budget_consolidation.csv` |
| C10 | Added Exp13.1 wrong-world context-injection support and dropout/bleed caveat. | Wrong-world injection collapsed composition, while dropout/bleed did not. | `docs/threads/experiment13_1_analysis_digest.md`; `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_context_corruption.csv` |
| C12 | Added Exp13.1 as internal-only evidence requiring baselines. | Completed run did not include external baselines. | `docs/threads/experiment13_1_analysis_digest.md` |

## Figures changed

Updated candidate Figure 2, Figure 4, Figure 5, Figure 7, and supplementary figure entries to cite Exp13.1 source CSVs/plots. Lesion plot is explicitly marked negative/diagnostic only.

## Limitations added

- Exp13.1 targeted lesion diagnostic failure.
- Exp13.1 reproducibility metadata gap.
- Context-corruption caveat refined toward wrong-world identity sensitivity, not generic noise robustness.
- Consolidation caveat refined because Exp13.1 did not show accuracy rescue.

## TODOs added or resolved

- Resolved: Exp13.1 is no longer listed as a future unimplemented directory.
- Added: audit/rerun Exp13.1 lesion diagnostic before citing positive lesion evidence.
- Added: add seed-level CIs/effect sizes, final figure scripts, external baselines, stochastic context corruption if generic robustness is claimed, and future device/runtime metadata.

## Conflicts or caveats

- Targeted lesion expected pattern failed.
- External baselines remain missing.
- Seed-level confidence intervals/effect sizes remain pending.
- The run manifest lacks explicit GPU/device/runtime metadata.
- Source-data mirrors are convenience copies only; authoritative artifacts remain under `experiments/...`.

## Path verification result

Ran `python scripts/verify_doc_source_paths.py` after import edits. Result: 76 files scanned, 5017 OK paths, 0 missing active paths, 12 skipped planned/future paths, and 38 skipped local-verification-pending paths.
