# Execution Tools

This directory contains reusable prompts and workflow instructions for running the Context-Indexed Route Memory research program.

The goal is to ensure every experiment follows the same lifecycle:

1. Design the experiment.
2. Implement it locally.
3. Run it locally.
4. Analyze results in ChatGPT.
5. Extract the analysis thread into the repository.
6. Update claims, figures, limitations, and next-experiment docs.
7. QA the repository update.
8. Decide the next experiment.

Core rule:

> No experiment is complete until its analysis has been imported into the repository and linked to claims/evidence docs.

Current repository structure guardrails:

- New experiments and successor protocols live under `experiments/<experiment_dir>/`.
- Do not create new root-level experiment directories.
- Each experiment directory owns its code, runners, analysis scripts, docs, `runs/`, `analysis/`, and `README.md`.
- Reruns of the same protocol stay inside the owning experiment directory; changed protocols get a new directory.
- Completed runs are immutable. If SQLite is used, each completed run gets its own database file, typically under `experiments/<experiment_dir>/runs/`.
- After a completed run, update the owning experiment `README.md` with the run name, database path if present, key configuration notes, and summarized results.
- Active manuscript/evidence/source paths should use current `experiments/...` paths, or be explicitly marked future/planned/missing/local verification pending.
- New experiment prompts should account for available GPUs by default. Use `check_gpu_status.py` as the local visibility reference and document CPU-only or partial-GPU limitations in the experiment `README.md`.

Canonical evidence discipline:

```text
Claim -> Evidence -> Caveat -> Source path
```

Important canonical docs:

- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

Always run the path verifier after source-path-heavy edits:

```bash
python scripts/verify_doc_source_paths.py
```

## Naming convention note

These prompts intentionally use placeholders such as `<experiment_id>`, `<experiment_dir>`, and `<THREAD_DIGEST_FILENAME>`.

Before creating or updating files, inspect `docs/experiments/EXPERIMENT_REGISTRY.md` and follow the repository's existing convention. Common examples:

- `docs/experiments/exp13_summary.md`
- `docs/experiments/exp13_1_summary.md`
- `docs/experiments/<experiment_id>_summary.md`

Do not assume a summary file already exists. If it does not, create it from `docs/experiments/EXPERIMENT_SUMMARY_TEMPLATE.md`.
