# Prompt: Import Staged Analysis Digest Into Repository

```text
You are working inside the local repository:

GradieResearch/context-indexed-route-memory

A ChatGPT experiment-analysis thread produced this staged digest package:

docs/imports/<THREAD_DIGEST_FILENAME>.zip

It should contain exactly one markdown digest:

<THREAD_DIGEST_FILENAME>.md

After validation, extract it to:

docs/threads/<THREAD_DIGEST_FILENAME>.md

Experiment:
- ID: <ID>
- Name: <EXPERIMENT_NAME>
- Directory: experiments/<EXPERIMENT_DIR>/
- Run ID(s): <RUN_ID_OR_IDS>
- Profile(s): <PROFILE_OR_PROFILES>
- Main analysis directory/directories: experiments/<EXPERIMENT_DIR>/analysis/<RUN_ID>/
- Database/raw record path if applicable: experiments/<EXPERIMENT_DIR>/runs/<RUN_ID>.sqlite3

Do not modify experiment code.
Do not rerun experiments.
Do not delete generated artifacts.
Do not delete the import zip unless explicitly asked.
Do not invent conclusions.
Do not strengthen claims beyond the thread digest and local artifacts.
Do not treat design proposals as completed results.
If digest and artifacts conflict, record the conflict.

Evidence discipline:
Claim -> Evidence -> Caveat -> Source path

Every claim must cite:
1. docs/threads/<THREAD_DIGEST_FILENAME>.md
2. local artifact path if available

If local artifact support is absent, mark `local verification pending`.

Source path discipline:
- Active evidence paths must use `experiments/...`.
- Do not cite stale root-level experiment paths.
- Missing artifacts must be marked missing/future/planned/local verification pending.
- Run outputs remain inside the owning experiment directory.

Canonical docs to inspect/update:
- experiments/<EXPERIMENT_DIR>/README.md
- docs/threads/THREAD_INDEX.md
- docs/experiments/EXPERIMENT_REGISTRY.md
- docs/experiments/<experiment_id>_summary.md
- docs/manuscript/CLAIMS_AND_EVIDENCE.md
- docs/manuscript/FIGURE_PLAN.md
- docs/manuscript/LIMITATIONS_AND_THREATS.md
- docs/manuscript/MANUSCRIPT_TODO.md
- docs/manuscript/BASELINE_REQUIREMENTS.md if relevant
- docs/synthesis/PROJECT_STATUS.md
- docs/synthesis/PUBLICATION_READINESS.md
- docs/synthesis/NEXT_EXPERIMENTS.md
- docs/source_data/ if repo convention
- docs/repo_audit/ARTIFACT_INDEX.csv if maintained
- docs/experiments/EXPERIMENT_ARTIFACTS_INDEX.csv if maintained
- docs/repo_audit/THREAD_IMPORT_CONFLICTS.md

################################################################################
# Phase 0 — Stage digest
################################################################################
- Confirm import zip exists.
- Inspect zip contents.
- Confirm exactly one required markdown digest at zip root.
- Extract only the digest to docs/threads/.
- If digest already exists, compare; do not silently overwrite.
- Confirm it begins with `# Thread Digest:` and has an import checklist.

################################################################################
# Phase 1 — Inspect artifacts
################################################################################
Inspect experiment directory and outputs:
- run ID(s);
- database/raw record;
- reports;
- validation report;
- metrics/summary/effect-size CSVs;
- plots;
- manifest/config;
- progress logs;
- README;
- run scripts.

Record missing, renamed, stale, or non-`experiments/...` paths.

################################################################################
# Phase 2 — Update docs
################################################################################
- Update THREAD_INDEX.
- Create/update experiment summary.
- Update owning README completed-runs/results.
- Update EXPERIMENT_REGISTRY.
- Update CLAIMS_AND_EVIDENCE conservatively.
- Update FIGURE_PLAN; generated plots are not final paper figures unless final scripts exist.
- Update LIMITATIONS_AND_THREATS.
- Update MANUSCRIPT_TODO and synthesis docs.
- Copy small source-data mirrors only if repo convention and source paths remain preserved.
- Update artifact indexes only if manually maintained; otherwise note regeneration needed.

################################################################################
# Phase 3 — Conflict log and import report
################################################################################
Update or create:
- docs/repo_audit/THREAD_IMPORT_CONFLICTS.md
- docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_REPORT.md

Import report sections:
# Experiment <ID> Analysis Import Report
## Summary
## Import package reviewed
## Thread digest imported
## Local artifacts reviewed
## Docs updated
## Claims changed
| Claim ID | Change | Reason | Source |
|---|---|---|---|
## Figures changed
## Limitations added
## TODOs added or resolved
## Conflicts or caveats
## Path verification result

################################################################################
# Phase 4 — Verification
################################################################################
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
9. Recommended QA prompt or next action.
```
