# Prompt For ChatGPT: Analyze Experiment 14 Results and Prepare Repository Import

```text
I have uploaded the analysis artifacts for Experiment 14: Latent Context Inference.

Repository: GradieResearch/context-indexed-route-memory
Owning experiment directory: experiments/experiment14_latent_context_inference/

Please analyze the uploaded Experiment 14 results and, in the same response, create:
1. the scientific analysis;
2. a downloadable repository-import digest zip;
3. a ready-to-paste Codex prompt to import the staged digest into the repository.

Core scientific question:
Does route memory still work when the world/context is inferred from partial transition evidence instead of being supplied as an oracle label?

Framing:
- Exp14 addresses the oracle context/world-label limitation.
- It is symbolic latent context inference from partial route evidence, not full sensory world discovery.
- Treat it as a bridge between supplied-context route memory and future non-symbolic context inference.

Do not update GitHub directly.
Do not invent local artifact paths.
Do not assume implementation correctness without checking artifacts.
Do not strengthen claims beyond uploaded artifacts and current repository evidence.
Use current repo-relative `experiments/...` paths.
If a path is absent or only represented by the upload bundle, mark it `local verification pending`.

Inspect:
- report, validation report, metrics/summary/effect-size CSVs, plots, manifest/config, progress logs, SQLite DB/raw record if supplied, README if supplied, runtime/device metadata, warnings/failures.

Analysis structure:
# Experiment 14 Analysis: Latent Context Inference
## 1. Executive summary
## 2. Run integrity and artifact audit
## 3. Primary hypotheses
Assess:
- H1 latent context selection recovers correct world from partial cue evidence in clean conditions.
- H2 composition accuracy tracks world-selection accuracy.
- H3 corruption/noise creates graded degradation.
- H4 oracle context-gated lookup remains an upper-bound baseline.
- H5 random/recency/shared/endpoint/hash baselines reveal distinct failure modes.
## 4. Key results
## 5. Mechanism, ablation, and baseline analysis
## 6. Statistical and metric critique
## 7. Figure interpretation
## 8. Relationship to existing claims
Map to C2, C3, C4, C10, C12, and decide whether a new conservative latent-context claim is justified.
## 9. Manuscript implications
## 10. Problems, flaws, or rerun requirements
## 11. Recommended repository updates
## 12. Recommended next action

End with a claim/evidence/caveat table.

Repository-import digest:
- Create a zip with exactly one markdown digest at root.
- Preferred digest filename: experiment14_latent_context_inference_analysis_digest.md
- Expected staging path: docs/imports/experiment14_latent_context_inference_analysis_digest.zip
- Expected final path: docs/threads/experiment14_latent_context_inference_analysis_digest.md
- Do not include generated repo updates or Codex prompt in the zip.

Digest sections:
# Thread Digest: Experiment 14 Latent Context Inference
Digest filename:
Intended repository path:
Import package expected at:
## 1. Thread scope
## 2. Experiment analyzed or designed
## 3. Experimental design discussed
## 4. Results analyzed
## 5. Key scientific conclusions supported by this thread
## 6. Important flaws, mistakes, or implementation concerns identified
## 7. Figures or artifacts referenced
## 8. Decisions made
## 9. Open questions
## 10. Relationship to first manuscript
## 11. Claims-and-evidence rows contributed by this thread
## 12. Required repository updates
## 13. Recommended next action
## 14. Import package checklist

Final response must include:
1. Brief Exp14 analysis outcome.
2. Download link to digest zip.
3. Expected staging path.
4. Full ready-to-paste Codex import prompt.
5. Local artifact paths needing verification.

The Codex prompt must tell Codex to:
- import docs/imports/experiment14_latent_context_inference_analysis_digest.zip;
- extract to docs/threads/experiment14_latent_context_inference_analysis_digest.md;
- inspect experiments/experiment14_latent_context_inference/;
- update README, THREAD_INDEX, EXPERIMENT_REGISTRY, exp14_summary, CLAIMS_AND_EVIDENCE, FIGURE_PLAN, LIMITATIONS_AND_THREATS, MANUSCRIPT_TODO, synthesis docs, conflict log, and EXP14_ANALYSIS_IMPORT_REPORT;
- use Claim -> Evidence -> Caveat -> Source path;
- cite digest and local artifact paths;
- record missing artifacts as local verification pending;
- run python scripts/verify_doc_source_paths.py;
- not modify code, rerun experiments, delete artifacts, commit, or push.
```
