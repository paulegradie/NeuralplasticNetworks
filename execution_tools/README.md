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
