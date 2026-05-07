# Codex Prompt: Import Experiment 13.2 Analysis Digest

```text
You are working inside the local repository:

GradieResearch/context-indexed-route-memory

We completed analysis of Experiment 13.2 and staged the digest package here:

docs/imports/experiment13_2_analysis_digest.zip

The zip should contain exactly:

experiment13_2_analysis_digest.md

Extract it to:

docs/threads/experiment13_2_analysis_digest.md

Experiment:
- ID: 13.2
- Name: Baseline Suite
- Directory: experiments/experiment13_2_baseline_suite/
- Run profile: full
- Run ID: exp13_2_full_20260507_165813
- Analysis directory: experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/
- Expected DB path: experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3

Important verification note:
The uploaded bundle used for the digest included analysis outputs but not the SQLite database. Verify the DB path locally. If absent, record it as `local verification pending` or a missing raw-run artifact.

Do not modify experiment code.
Do not rerun experiments.
Do not delete generated artifacts.
Do not delete the import zip.
Do not invent conclusions.
Do not strengthen claims beyond the digest and local artifacts.
Every claim must cite:
1. docs/threads/experiment13_2_analysis_digest.md
2. local artifact path if available

If local artifact support is absent, mark `local verification pending`.
If digest and artifacts conflict, record the conflict in docs/repo_audit/THREAD_IMPORT_CONFLICTS.md.

################################################################################
# Stage digest
################################################################################
- Confirm docs/imports/experiment13_2_analysis_digest.zip exists.
- Inspect zip contents.
- Confirm exactly one markdown digest at zip root.
- Extract experiment13_2_analysis_digest.md to docs/threads/experiment13_2_analysis_digest.md.
- If that file already exists, compare before overwriting.

################################################################################
# Verify Exp13.2 artifacts
################################################################################
Check:
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_report.md
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/experiment_report.md
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_report.md
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/validation_results.json
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/run_manifest.json
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/progress.jsonl
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_metrics.csv
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/metrics.csv
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_summary.csv
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_effect_sizes.csv
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/exp13_2_baseline_metrics.csv
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_seen_route_composition_accuracy.png
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_suffix_generalization_accuracy.png
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_route_table_accuracy.png
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_first_step_context_accuracy.png
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_capacity_pressure.png
- experiments/experiment13_2_baseline_suite/analysis/exp13_2_full_20260507_165813/plots/exp13_2_sequential_retention.png
- experiments/experiment13_2_baseline_suite/runs/exp13_2_full_20260507_165813.sqlite3

################################################################################
# Update docs conservatively
################################################################################
Update as appropriate:
- experiments/experiment13_2_baseline_suite/README.md
- docs/threads/THREAD_INDEX.md
- docs/experiments/EXPERIMENT_REGISTRY.md
- docs/experiments/exp13_2_summary.md
- docs/manuscript/CLAIMS_AND_EVIDENCE.md
- docs/manuscript/FIGURE_PLAN.md
- docs/manuscript/LIMITATIONS_AND_THREATS.md
- docs/manuscript/MANUSCRIPT_TODO.md
- docs/manuscript/BASELINE_REQUIREMENTS.md
- docs/synthesis/PROJECT_STATUS.md
- docs/synthesis/PUBLICATION_READINESS.md
- docs/synthesis/NEXT_EXPERIMENTS.md
- docs/source_data/ if source-data mirrors are repo convention
- docs/repo_audit/ARTIFACT_INDEX.csv if maintained manually
- docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv if maintained
- docs/repo_audit/THREAD_IMPORT_CONFLICTS.md
- docs/repo_audit/EXP13_2_ANALYSIS_IMPORT_REPORT.md

Required framing:
- Exp13.2 partially resolves C12 by adding a symbolic/algorithmic baseline suite.
- Do not claim CIRM beats the oracle context-gated table; that baseline matches CIRM in the clean supplied-context benchmark.
- Treat this as a claim refinement: clean supplied-context symbolic route memory can be solved by oracle context-gated lookup.
- Preserve mechanistic support:
  - shared no-context lookup fails first-step/seen-route context-sensitive queries;
  - no-recurrence preserves route-table accuracy while composition fails;
  - no-structural-plasticity fails;
  - endpoint memorization solves seen full routes but fails suffix composition.
- Preserve caveats:
  - baselines are symbolic/algorithmic, not full neural baselines;
  - oracle context labels remain a limitation;
  - suffix probes can be misleading for no-context lookup;
  - DB/raw-run may require local verification;
  - Exp13.2 does not resolve Exp13.1 lesion failure;
  - prior-art/novelty import and final figure scripts may still be needed.

Run:

python scripts/verify_doc_source_paths.py

Fix active broken paths.
Do not commit.
Do not push.

Final response:
1. Files modified.
2. README/run log changed.
3. Claims changed.
4. Figures changed.
5. Limitations added.
6. TODOs changed.
7. Conflicts recorded.
8. Path verifier result.
9. Recommended next action.
```
