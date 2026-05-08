# Next Step Prompt: Post-Exp15 Manuscript Hardening

Use this prompt with a local coding agent for the next manuscript-finalization pass.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: Harden the manuscript documentation and final figure/table plan after the completed Experiment 15 import.

Context:

Experiment 15 is no longer implementation-only. The imported run is:

- run ID: exp15_full_20260508_092811
- experiment directory: experiments/experiment15_neural_baseline_comparator/
- digest: docs/threads/experiment15_analysis_digest.md
- import report: docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md
- validation: experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/validation_report.md
- summary CSV: experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv

Important constraints:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not invent conclusions.
- Do not strengthen claims beyond Exp15 digest and local artifacts.
- Do not claim broad CIRM superiority over neural models.
- Do not treat Exp15 as exhaustive neural benchmarking.
- Do not interpret the Exp15 replay variant scientifically unless an audit is performed.
- Preserve the provenance caveat: run_manifest.json was reconstructed after a final SQLite manifest-write failure, and the SQLite run_manifest table may be empty. Treat CSV artifacts as authoritative unless a later audit says otherwise.
- Do not commit or push unless explicitly asked.

Primary goal:

Move the manuscript docs from post-import alignment to final manuscript hardening:

1. Decide or clearly queue whether Exp15 belongs as:
   - a compact main-text neural comparator table; or
   - a supplementary neural comparator table/figure.
2. Ensure C1, C2, C4, and C12 language remains conservative:
   - C1: Exp15 does not support structural plasticity as required for all route-memory systems.
   - C2: context/world indexing is necessary for incompatible first-step/full-route disambiguation, not every suffix transition.
   - C4: Exp15 strengthens the route-table/composition/endpoint-memorization dissociation.
   - C12: minimal neural comparator completed, but non-exhaustive and prior-art/novelty import remains incomplete.
3. Prepare final source-data-backed figure/table work without using analysis plots as final figures.
4. Keep broad neural-superiority claims out of the manuscript.

Start by inspecting:

- docs/manuscript/finalization/MANUSCRIPT_FINALIZATION_PLAN.md
- docs/manuscript/finalization/FINALIZATION_CHECKLIST.md
- docs/manuscript/CLAIMS_AND_EVIDENCE.md
- docs/manuscript/FIGURE_PLAN.md
- docs/manuscript/MANUSCRIPT_TODO.md
- docs/manuscript/BASELINE_REQUIREMENTS.md
- docs/synthesis/PUBLICATION_READINESS.md
- docs/source_data/SOURCE_DATA_MANIFEST.csv
- docs/threads/experiment15_analysis_digest.md
- docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md

Recommended edits:

- Update `docs/manuscript/FIRST_MANUSCRIPT_CLAIM_FREEZE.md` or create a post-Exp15 claim-freeze addendum.
- If Exp15 is retained as a table/figure, create source-data-backed table inputs from existing Exp15 CSVs and update `docs/source_data/SOURCE_DATA_MANIFEST.csv`.
- Update `docs/manuscript/tables/` only if a concrete table is generated from existing source artifacts.
- Update `docs/manuscript/MANUSCRIPT_SPINE.md` only after the post-Exp15 claim posture is settled.
- Keep all new claims in Claim -> Evidence -> Caveat -> Source path form.

Exp15 hard-slice facts available for conservative citation:

- `neural_transition_mlp_context`: 1.0000 on all hard-slice metrics.
- `neural_transition_mlp_world_heads_context`: 1.0000 on all hard-slice metrics.
- `neural_gru_endpoint_context`: seen-route composition about 0.9990, suffix-route composition about 0.4040, transition accuracy about 0.0232, retention about 0.7015.
- `neural_gru_rollout_context`: first-step context conflict about 0.8794, transition accuracy about 0.5122, suffix-route composition about 0.0777, retention about 0.0612.
- `neural_transformer_sequence_context`: seen-route composition about 0.5435, suffix-route composition about 0.1184, retention about 0.3309.
- `neural_transition_mlp_no_context`: first-step context conflict about 0.0312, seen-route composition about 0.0312, suffix-route composition 1.0000, transition accuracy about 0.9193, retention about 0.5156.
- `neural_transition_mlp_replay_context`: near-zero hard-slice performance; audit before interpretation.

Definition of done:

- Finalization docs no longer say Exp15 still needs to be designed/run/imported.
- Remaining Exp15 work is framed as manuscript placement, source-data-backed figure/table generation, optional memory-augmented neural baseline decision, and replay audit only if cited.
- `python scripts/verify_doc_source_paths.py` passes.
- Final response summarizes changed files, claim posture, unresolved decisions, and verification result.
```
