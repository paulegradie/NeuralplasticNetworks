# Source of Truth

Purpose: Explain which documents are authoritative when repository docs disagree.

## Canonical docs

- Claims: `docs/manuscript/CLAIMS_AND_EVIDENCE.md`
- Figures: `docs/manuscript/FIGURE_PLAN.md`
- Submission readiness: `docs/synthesis/PUBLICATION_READINESS.md`
- Experiment list: `docs/experiments/EXPERIMENT_REGISTRY.md`
- Next work: `docs/manuscript/MANUSCRIPT_TODO.md`
- Reproducibility: `docs/repo_audit/REPRODUCIBILITY_AUDIT.md`

## Non-authoritative docs

- Thread exports are source material, not final claims.
- Generated reports are local artifacts, not manuscript prose.
- Historical experiment notes may contain outdated framing.
- Roadmaps and issue templates are handoff aids, not evidence.

## Rule

If there is a conflict:

1. Generated artifact/source data wins for numeric claims.
2. `docs/manuscript/CLAIMS_AND_EVIDENCE.md` wins for current claim wording.
3. `docs/manuscript/LIMITATIONS_AND_THREATS.md` wins for caveats.
4. Thread exports are used only as historical context unless imported into current docs with local artifacts.

## Current Scope Note

Exp13.2 and Exp14 have now both been imported into repository-native documentation.

- Exp13.2 is canonical as a completed symbolic/algorithmic baseline-suite result. It partially addresses the baseline blocker by showing that an oracle context-gated transition table matches CIRM on the clean supplied-context benchmark and by adding shared no-context, endpoint-memorization, recurrence, compact-storage, replay/LRU, and parameter-isolation style controls. It does **not** complete prior-art positioning, neural baseline coverage, or submission readiness by itself.
- Exp14 is canonical as a completed symbolic latent-context result. It shows that the active world/context can be selected from partial symbolic transition cues before route execution. It does **not** show raw sensory latent-world discovery, end-to-end perception, or superiority over the oracle context-gated upper bound.

For manuscript preparation, use Exp13.2 to refine baseline/framing claims and Exp14 to refine the oracle-context limitation, while keeping all broad biological, continual-learning, neural-superiority, perception, and novelty claims narrow until final prior-art, uncertainty, and figure work is complete.
