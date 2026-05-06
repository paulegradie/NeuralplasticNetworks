# Prompt: Extract Thread Analysis Digest

```text
I am consolidating this experiment analysis thread into the GitHub repository for manuscript preparation.

Please create a structured, forensic digest of this conversation.

Do not add new speculation unless clearly labeled.
Extract only what was actually discussed, designed, concluded, corrected, or analyzed in this thread.
Distinguish completed results from design proposals.
Use exact experiment numbers and artifact filenames when available.

Output markdown with the following structure:

# Thread Digest: Experiment <ID> <short title>

## 1. Thread scope

What was this thread mainly about?

## 2. Experiment analyzed or designed

- Experiment ID:
- Experiment name:
- Run profile:
- Uploaded artifact bundle:
- Main local artifact paths, if known:

## 3. Experimental design discussed

Include:
- purpose;
- hypotheses;
- variants/baselines;
- metrics;
- run profiles;
- expected outcomes;
- implementation notes;
- known risks.

If the thread analyzed completed results, distinguish original design from post-hoc interpretation.

## 4. Results analyzed

For each result:

### Result <N>: <title>

Claim:
Evidence:
Caveat:
Source artifact:
Thread status:

Status options:
- Strong
- Promising
- Preliminary
- Needs rerun
- Needs metric cleanup
- Needs baseline
- Historical only
- Do not use

## 5. Key scientific conclusions supported by this thread

Use:

Claim:
Evidence:
Caveat:
Experiment:
Artifact(s):
Manuscript relevance:

## 6. Important flaws, mistakes, or implementation concerns identified

Include:
- metric problems;
- artifact problems;
- validation warnings;
- suspicious results;
- seed/statistical limitations;
- naming or ablation-definition problems;
- anything requiring rerun.

## 7. Figures or artifacts referenced

List:
- filenames;
- CSVs;
- reports;
- plots;
- validation artifacts;
- run manifests.

## 8. Decisions made

List concrete decisions:
- interpretation decisions;
- manuscript framing decisions;
- whether claim statuses changed;
- whether result belongs in main/supplement;
- follow-up experiments.

## 9. Open questions

List unresolved scientific or implementation questions.

## 10. Relationship to first manuscript

Explain how this thread contributes to:
- central claim;
- supporting claim;
- limitation;
- future work;
- supplementary material.

## 11. Claims-and-evidence rows contributed by this thread

Create a markdown table:

| Claim | Evidence | Caveat | Experiment(s) | Artifact(s) | Manuscript status |
|---|---|---|---|---|---|

## 12. Required repository updates

List exact files to update:

- `docs/threads/...`
- `docs/experiments/...`
- `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- `docs/manuscript/FIGURE_PLAN.md`
- `docs/manuscript/LIMITATIONS_AND_THREATS.md`
- `docs/manuscript/MANUSCRIPT_TODO.md`
- `docs/synthesis/PROJECT_STATUS.md`
- `docs/synthesis/PUBLICATION_READINESS.md`
- `docs/synthesis/NEXT_EXPERIMENTS.md`
- `docs/repo_audit/...`

## 13. Recommended next action

State what should happen next.

Important:
This digest will be saved directly into the repository under `docs/threads/`.
It must be conservative, source-oriented, and useful to a future agent.
```
