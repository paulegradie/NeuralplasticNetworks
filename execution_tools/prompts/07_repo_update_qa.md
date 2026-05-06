# Prompt: Repository Update QA

```text
You are reviewing the repository update after importing Experiment <ID> analysis.

Do not rewrite broadly.
Your job is adversarial QA.

Inspect:

- new thread digest under `docs/threads/`
- experiment summary under `docs/experiments/`
- `docs/experiments/EXPERIMENT_REGISTRY.md`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- new import report under `docs/repo_audit/`
- local experiment artifacts

Verify:

1. Thread digest exists and is indexed.
2. Experiment summary cites thread and local artifacts.
3. Claims were not overstrengthened.
4. Every claim has evidence/caveat/source path.
5. Figure plan paths exist.
6. Limitations include new caveats.
7. TODOs reflect new blockers and completed work.
8. Synthesis docs reflect current status.
9. Path verifier passes.
10. No generated artifact was modified destructively.
11. No planned design is written as completed result.
12. No external baseline is implied unless actually run.
13. No biological or continual-learning overclaim was introduced.

Create:

`docs/repo_audit/EXP<ID>_ANALYSIS_IMPORT_QA.md`

Use this structure:

# Experiment <ID> Analysis Import QA

## Summary

## Checklist

| Check | Result | Evidence | Notes |
|---|---|---|---|

## Problems found

For each problem:
- severity: P0/P1/P2
- file
- issue
- why it matters
- recommended fix

## Final recommendation

Choose one:
- import passed; ready for next experiment planning;
- small cleanup required;
- major evidence-integrity issue; stop and fix before proceeding.

Do not commit.
Do not push.
```
