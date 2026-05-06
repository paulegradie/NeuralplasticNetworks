# Prompt: Analyze Uploaded Results

```text
I have uploaded the analysis artifacts for Experiment <ID>: <name>.

Please analyze these results in the context of the current Context-Indexed Route Memory research program and the first manuscript.

Be scientific, rigorous, realistic, and explicit.

Do not overclaim.
Do not assume the implementation is correct without checking artifacts.
Do not treat planned hypotheses as completed results.
Separate actual evidence from interpretation and speculation.
Use current repo-relative source paths under `experiments/...` when paths are known.
If an artifact path is absent, stale, or only present in an upload bundle, mark the source path as `local verification pending`.
Do not cite bare `analysis/...` paths unless they are explicitly relative to an owning experiment directory.

Please review:
- generated report;
- validation report;
- metrics CSVs;
- summary CSVs;
- plots;
- run manifest/config;
- per-run database path if SQLite was used;
- owning experiment README completed-runs/results section if available;
- GPU/device information if available;
- any warnings or failed validation checks.

Output the analysis with the following structure:

# Experiment <ID> Analysis: <short title>

## 1. Executive summary

State the main result in 3–6 paragraphs.

## 2. Run integrity and artifact audit

Check:
- run profile;
- run ID and output directory;
- seed count;
- expected phases;
- expected variants;
- expected metrics;
- expected plots;
- per-run SQLite database or other raw run record if applicable;
- whether paths use current `experiments/...` prefixes;
- validation PASS/WARN/FAIL;
- missing artifacts;
- suspicious artifacts.

## 3. Primary hypotheses

For each hypothesis:

Hypothesis:
Result:
Evidence:
Caveat:
Status: supported / partially supported / not supported / unclear

## 4. Key results

Use this format for each result:

### Result <N>: <title>

Claim:
Evidence:
Caveat:
Source artifact:
Manuscript status:

Status options:
- Strong
- Promising
- Preliminary
- Needs rerun
- Needs metric cleanup
- Needs baseline
- Historical only
- Do not use

## 5. Ablation and mechanism analysis

Discuss what each model variant/baseline shows mechanistically.

Focus on:
- storage;
- context/world selection;
- recurrence;
- structural plasticity;
- consolidation;
- capacity;
- generalization boundary;
- failure modes.

## 6. Statistical and metric critique

Assess:
- seed count;
- confidence intervals;
- effect sizes;
- aggregation;
- whether metrics match claims;
- whether any metric hides failure modes;
- whether additional splits are required.

## 7. Figure interpretation

For each plot:
- what it appears to show;
- what claim it might support;
- what caveat applies;
- whether it belongs in main figures or supplement.

## 8. Relationship to existing claims

Map results to existing claims if applicable:

- C1 structural plasticity
- C2 world/context indexing
- C3 recurrence
- C4 route-table/composition dissociation
- C5 clean capacity scaling
- C6 finite-budget degradation
- C7 local-vs-global budget
- C8 consolidation stability-plasticity
- C9 seen primitive vs unseen primitive boundary
- C10 context corruption
- C11 continuous/noisy bridge
- C12 baselines required

For each claim:
- strengthens;
- weakens;
- refines;
- no change;
- requires new claim.

## 9. Manuscript implications

Explain:
- where this result belongs in the paper;
- whether it changes the manuscript spine;
- whether it should be main figure, supplement, limitation, or future work.

## 10. Problems, flaws, or rerun requirements

Be explicit about anything that might require:
- rerun;
- metric cleanup;
- implementation audit;
- figure regeneration;
- baseline comparison;
- revised interpretation.

## 11. Recommended repository updates

List exact docs that should be updated:
- owning experiment README completed-runs/results section;
- experiment summary;
- experiment registry;
- claims/evidence;
- figure plan;
- limitations;
- manuscript TODO;
- synthesis docs;
- source data;
- reproducibility audit.

## 12. Recommended next experiment or next action

State whether the next step should be:
- rerun;
- metric cleanup;
- baseline suite;
- manuscript draft;
- next conceptual experiment.

Important:
End with a concise "claim/evidence/caveat table" suitable for import into the repository.
```
