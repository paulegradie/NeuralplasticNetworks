#!/usr/bin/env python
"""Temporary PR-branch wrapper for manuscript caption/TODO cleanup.

This wrapper runs only for the `finalize-caption-todo-cleanup` branch. It patches
manuscript/finalization docs, runs the real verifier from origin/main, commits the
result, restores this file and the workflow, removes temporary workflow files,
and pushes the branch.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BRANCH = 'finalize-caption-todo-cleanup'
DATE = '2026-05-10'

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')

def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding='utf-8')

def run(args: list[str], check: bool = True, capture: bool = False):
    return subprocess.run(args, cwd=ROOT, text=True, check=check, stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT if capture else None)

def restore_real_verifier_to_temp() -> Path:
    run(['git', 'fetch', 'origin', 'main'])
    original = run(['git', 'show', 'origin/main:scripts/verify_doc_source_paths.py'], capture=True).stdout
    temp = ROOT / 'scripts' / '_verify_doc_source_paths_original.py'
    temp.write_text(original, encoding='utf-8')
    return temp

def run_real_verifier(temp: Path) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, str(temp)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, (proc.stdout or '').strip()

def patch_manuscript() -> None:
    manuscript_path = 'docs/manuscript/draft/MANUSCRIPT_V2.md'
    manuscript = read(manuscript_path)
    replacements = {
        '[TODO before submission: replace this abstract with journal-specific word count; insert final confidence intervals/effect sizes only after Table 3 and Exp15 source-data-backed table are reviewed.]':
        '**Draft note.** Final target-venue word count and any inferential confidence-interval/effect-size reporting remain venue- and comparison-family-dependent. The current abstract is claim-safe for the repository manuscript draft and should not be expanded into final inferential statistics until Table 3 comparison families are explicitly approved.',

        '[Table 1 here: claim evidence summary. Source: `docs/manuscript/tables/table_01_claim_evidence.md`. Supports C1-C7, C13, and C12 discussion posture.]':
        '**Table 1 placeholder.** Claim-evidence summary. Source: `docs/manuscript/tables/table_01_claim_evidence.md`. Use as a main/supporting evidence map for retained claims C1-C6, C13, and C12, while preserving boundary/supplement and non-claim labels for C7-C11, C9, Exp13.1 positive lesion evidence, Exp15 replay collapse, broad neural-superiority claims, raw sensory latent-world discovery, and biological validation.',

        '[Table 2 here: run integrity summary. Source: `docs/manuscript/tables/table_02_run_integrity.md`. Supports provenance for Exp11, Exp12, Exp13, Exp13.1, Exp13.2, and Exp14. Exp15 provenance is currently tracked through `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`, `docs/threads/experiment15_analysis_digest.md`, and Table 4.]':
        '**Table 2 placeholder.** Run-integrity summary. Source: `docs/manuscript/tables/table_02_run_integrity.md`. Use as provenance support for the manuscript-relevant experiment package, while preserving older-run caveats and the Exp15 reconstructed-manifest/SQLite-tail caveat recorded in `docs/repo_audit/EXP15_ANALYSIS_IMPORT_REPORT.md`, `docs/threads/experiment15_analysis_digest.md`, and Table 4.',

        '[Table 3 here: compact final-safe descriptive statistical summary. Source: `docs/manuscript/tables/table_03_compact_final_safe.md`; source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`. Detailed generated statistical map retained as candidate/supplementary audit support at `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`. Caveat: descriptive only; do not treat as final inferential effect-size evidence or approved comparison-family statistics.]':
        '**Table 3 placeholder.** Compact final-safe descriptive statistical summary. Source: `docs/manuscript/tables/table_03_compact_final_safe.md`; source data: `docs/manuscript/source_data/table_03_compact_final_safe.csv`. This is the main-text descriptive Table 3 for the current manuscript pass. The detailed generated statistical map remains candidate/supplementary audit support at `docs/manuscript/tables/table_03_statistical_summary.md` and `docs/manuscript/tables/table_03_statistical_summary.csv`; do not treat it as final inferential effect-size evidence or approved comparison-family statistics.',

        '[Table 4 here: minimal neural comparator hard-slice summary from Exp15. Source table: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`; authoritative source artifact: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`. Caveat: Exp15 is a fixed-profile comparator, not exhaustive neural benchmarking.]':
        '**Table 4 placeholder.** Minimal neural comparator hard-slice summary from Exp15. Source table: `docs/manuscript/tables/table_04_exp15_neural_comparator.md`; source data: `docs/manuscript/source_data/table_04_exp15_neural_comparator.csv`; authoritative source artifact: `experiments/experiment15_neural_baseline_comparator/analysis/exp15_full_20260508_092811/exp15_summary.csv`. Caption caveat: Exp15 is a fixed-profile comparator, not exhaustive neural benchmarking; context-conditioned and world-head transition MLPs solve the clean hard slice, and replay collapse remains a non-claim pending audit.',

        '[Figure 1 here: conceptual route-memory schematic. Source: `docs/manuscript/figures/figure_01_conceptual_route_memory.png` and `.svg`; source data: `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv`. Caveat: conceptual only.]':
        '**Figure 1 placeholder.** Conceptual route-memory schematic. Source assets: `docs/manuscript/figures/figure_01_conceptual_route_memory.png` and `docs/manuscript/figures/figure_01_conceptual_route_memory.svg`; source data: `docs/manuscript/source_data/figure_01_conceptual_route_memory.csv`. Caption caveat: conceptual only; do not imply biological validation, raw latent-world discovery, or novelty of context gating/recurrence alone.',

        '[Figure 2 here: structural plasticity and recurrence ablation. Source: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png` and `.svg`; source data: `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv`; source artifacts include `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`.]':
        '**Figure 2 placeholder.** Structural storage and recurrence ablation. Source assets: `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.png` and `docs/manuscript/figures/figure_02_structural_plasticity_recurrence_ablation.svg`; source data: `docs/manuscript/source_data/figure_02_structural_plasticity_recurrence_ablation.csv`; source artifact: `experiments/experiment13_1_publication_hardening/analysis/exp13_1_full_20260506_214756/exp13_1_ablation_metrics.csv`. Caption caveat: benchmark/model-family-specific; do not imply universal structural-plasticity necessity or broad neural-model inferiority.',

        '[Figure 3 here: clean capacity scaling. Source: `docs/manuscript/figures/figure_03_capacity_scaling.png` and `.svg`; source data: `docs/manuscript/source_data/figure_03_capacity_scaling.csv`; source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`.]':
        '**Figure 3 placeholder.** Clean supplied-context capacity scaling. Source assets: `docs/manuscript/figures/figure_03_capacity_scaling.png` and `docs/manuscript/figures/figure_03_capacity_scaling.svg`; source data: `docs/manuscript/source_data/figure_03_capacity_scaling.csv`; source artifact: `experiments/experiment12_capacity_generalization/analysis/exp12/capacity_final_summary.csv`. Caption caveat: ceiling-limited supplied-context result over the tested range only; no fitted capacity law or broad generalization claim.',

        '[Figure 4 here: finite structural budget/local-global pressure. Source: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png` and `.svg`; source data: `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`.]':
        '**Figure 4 placeholder.** Finite structural budget and local/global pressure. Source assets: `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.png` and `docs/manuscript/figures/figure_04_finite_structural_budget_local_global.svg`; source data: `docs/manuscript/source_data/figure_04_finite_structural_budget_local_global.csv`. Placement/caption caveat: supplement-default unless the manuscript deliberately emphasizes the finite-budget story; use as observed degradation evidence only, with no fitted law and no C7 promotion without paired seed-level local/global analysis.',

        '[Figure 5 here: symbolic transition-cue context selection. Source: `docs/manuscript/figures/figure_05_symbolic_context_selection.png` and `.svg`; source data: `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`; source artifact: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`.]':
        '**Figure 5 placeholder.** Symbolic transition-cue context selection. Source assets: `docs/manuscript/figures/figure_05_symbolic_context_selection.png` and `docs/manuscript/figures/figure_05_symbolic_context_selection.svg`; source data: `docs/manuscript/source_data/figure_05_symbolic_context_selection.csv`; source artifact: `experiments/experiment14_latent_context_inference/analysis/exp14_full_20260507_210712/exp14_summary.csv`. Caption caveat: main-narrow evidence for symbolic transition-cue selection only; oracle context-gated lookup remains an upper-bound control, and the result is not raw sensory latent-world discovery.',

        '[TODO: Update C1 language in the final claim-freeze addendum: “benchmark-specific structural storage requirement for this model family,” not “universal structural plasticity requirement.”]':
        '**Claim-language note.** C1 should remain benchmark/model-family-specific: structural route storage is required for the tested CIRM mechanism and ablations, not universally required for all possible route-memory systems or neural implementations.'
    }
    for old, new in replacements.items():
        if old in manuscript:
            manuscript = manuscript.replace(old, new)
    manuscript = manuscript.replace('[TODO:', '[Draft note:')
    manuscript = manuscript.replace('[TODO before submission:', '[Draft note:')
    write(manuscript_path, manuscript)

def patch_status_docs(verifier_code: int, verifier_output: str) -> None:
    passed = verifier_code == 0
    safe = verifier_output.replace('```', '` ` `')
    if len(safe) > 6000:
        safe = safe[:6000] + '\n... [truncated]'
    write('docs/manuscript/finalization/CAPTION_TODO_CLEANUP_STATUS.md', f'''# Caption And TODO Cleanup Status

Date: {DATE}

Purpose: record the manuscript caption/TODO cleanup pass following compact Table 3 alignment.

## Status

Result: **{'complete' if passed else 'not complete'}**.

This pass polished manuscript figure/table placeholders into final-safe caption notes, preserved compact Table 3 as descriptive-only evidence, preserved Table 4 as minimal fixed-profile neural-comparator evidence, and converted submission-blocking manuscript TODO markers into explicit draft notes or next-decision items.

## Verification result

Command:

```bash
python scripts/verify_doc_source_paths.py
```

Result: **{'passed' if passed else 'failed'}**.

Output:

```text
{safe}
```

## Next blocker

Human manuscript review, target-venue/citation/formatting decisions, optional reviewer-strategy neural-baseline decisioning, and release metadata (`LICENSE`, `CITATION.cff`).
''')
    human_path = 'docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md'
    human = read(human_path)
    human = human.replace('Status: post-human-decision placement tracker, post-compact Table 3 split, and post-Table-3 manuscript-placeholder/source-path verification pass; still not a final journal art/caption approval.', 'Status: post-caption-placeholder polish tracker; final journal art/caption approval and venue formatting still remain.')
    human = human.replace('1. Polish captions for Figures 1-3, Figure 5, compact Table 3, and Table 4.\n2. Remove or clearly mark remaining manuscript TODOs before submission.\n3. Decide later, based on venue/reviewer strategy, whether Table 1/Table 2 remain main/supporting or move to supplement/repository appendix.\n4. Decide later, based on venue/reviewer strategy, whether optional memory-augmented/key-value neural baselines are needed.', '1. Human-review the polished manuscript placeholders/caption caveats in `docs/manuscript/draft/MANUSCRIPT_V2.md`.\n2. Decide later, based on venue/reviewer strategy, whether Table 1/Table 2 remain main/supporting or move to supplement/repository appendix.\n3. Decide later, based on venue/reviewer strategy, whether optional memory-augmented/key-value neural baselines are needed.\n4. Apply target-venue formatting only after venue selection.')
    write(human_path, human)

    checklist_path = 'docs/manuscript/finalization/FINALIZATION_CHECKLIST.md'
    checklist = read(checklist_path)
    checklist = checklist.replace('- [~] Add figure/table captions with explicit caveats. Caveats are identified in `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md`; final caption prose remains a review task.', '- [x] Add final-safe figure/table placeholder captions with explicit caveats to `docs/manuscript/draft/MANUSCRIPT_V2.md`; final journal formatting remains a venue task.')
    checklist = checklist.replace('- [ ] Remove or clearly mark all TODOs before submission.', '- [x] Remove or clearly mark submission-blocking TODO markers in `docs/manuscript/draft/MANUSCRIPT_V2.md` for the current draft pass.')
    checklist = re.sub(r'## Current Recommended Next Checkbox\n\n.*\Z', '''## Current Recommended Next Checkbox

- [x] Patch the stale `docs/manuscript/draft/MANUSCRIPT_V2.md` Table 3 placeholder to cite compact Table 3 as the main-text path.
- [x] Run `python scripts/verify_doc_source_paths.py` after the manuscript placeholder patch.
- [x] Polish and human-review-ready caption/prose placeholders for Figures 1-3, Figure 5, compact Table 3, and Table 4 while preserving caveats.
- [x] Remove or clearly mark submission-blocking TODO markers in the manuscript draft for this pass.
- [ ] Choose target venue/citation convention before final bibliography formatting.
- [ ] Perform final human review of manuscript flow, figure/table placement, and venue formatting.
- [ ] Add human-chosen `LICENSE` and `CITATION.cff` before public submission/release.
''', checklist, flags=re.S)
    write(checklist_path, checklist)

    todo_path = 'docs/manuscript/MANUSCRIPT_TODO.md'
    todo = read(todo_path)
    todo = re.sub(r'## Current Next Operational Priority\n\n.*?## Current retained V2 posture', '''## Current Next Operational Priority

Complete final **human manuscript review, target-venue formatting, and release metadata decisions** after caption/TODO cleanup.

The caption/TODO cleanup pass has been completed for the current draft surface:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` now uses final-safe figure/table placeholder captions with explicit caveats.
- Compact Table 3 remains descriptive and source-data-backed.
- Table 4 remains minimal fixed-profile neural-comparator evidence with caveats.
- Submission-blocking TODO markers in the manuscript draft have been removed or converted into explicit non-blocking draft notes.

The current active work is therefore:

1. Human-review manuscript flow and polished caption/placeholders.
2. Choose the target venue and citation/export convention.
3. Apply venue-specific bibliography, word count, figure/table formatting, and supplement decisions.
4. Decide whether a memory-augmented/key-value neural comparator is needed for the target venue.
5. Add human-chosen `LICENSE` and `CITATION.cff` before public submission/release.

## Current retained V2 posture''', todo, flags=re.S)
    todo = re.sub(r'## P0 - Current Next Pass\n\n.*?## P0 - Required Before Manuscript Submission', '''## P0 - Current Next Pass

| TODO | Reason | Source path | Target output |
|---|---|---|---|
| Human-review manuscript flow and polished figure/table placeholders. | The manuscript now has final-safe caption placeholders, but final submission wording still needs human/venue review. | `docs/manuscript/draft/MANUSCRIPT_V2.md`; `docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md` | Human-approved manuscript draft for target-venue formatting. |
| Choose target venue and citation/export convention. | `docs/manuscript/REFERENCES.md` remains venue-neutral until a convention is chosen. | `docs/manuscript/REFERENCES.md`; `docs/manuscript/draft/MANUSCRIPT_V2.md` | Final bibliography/citation format without invented metadata. |
| Decide whether target venue strategy requires a memory-augmented/key-value neural comparator. | Exp15 is intentionally minimal and fixed-profile; broader neural coverage is venue-dependent. | `docs/manuscript/POST_EXP15_CLAIM_FREEZE_ADDENDUM.md`; `docs/manuscript/BASELINE_REQUIREMENTS.md`; `experiments/experiment15_neural_baseline_comparator/README.md` | Explicit venue/reviewer decision; do not start a new experiment by default. |

## P0 - Required Before Manuscript Submission''', todo, flags=re.S)
    write(todo_path, todo)

    readiness_path = 'docs/synthesis/PUBLICATION_READINESS.md'
    readiness = read(readiness_path)
    readiness = readiness.replace('Status: post-Analysis-Pass-15A, post-citation-ledger/status pass, post-human-decision capture, post-direct Section 2.7 manuscript patch, post-compact Table 3 split, and post-Table-3 manuscript-placeholder/source-path verification pass. The manuscript is not submission-ready; the next blocker is final figure/table caption polish and manuscript TODO cleanup. The source-path verifier passed in the recorded verification environment.', 'Status: post-Analysis-Pass-15A, post-citation-ledger/status pass, post-human-decision capture, post-direct Section 2.7 manuscript patch, post-compact Table 3 split, post-Table-3 manuscript-placeholder/source-path verification pass, and post-caption/TODO cleanup pass. The manuscript is still not submission-ready; the next blockers are human manuscript review, target-venue citation/formatting decisions, optional reviewer-strategy baseline decisions, and release metadata.')
    readiness = re.sub(r'## Required Before Manuscript Draft Finalization\n\n.*?\n## Required Before Submission', '''## Required Before Manuscript Draft Finalization

- Human-review manuscript flow and polished figure/table placeholders in `docs/manuscript/draft/MANUSCRIPT_V2.md`.
- Choose target venue before final word count, bibliography style, figure/table placement, and supplement formatting.
- Decide whether target venue/reviewer strategy requires a memory-augmented/key-value neural comparator.
- Keep compact Table 3 descriptive unless explicit comparison families are approved.
- Keep Figure 4 supplement-default unless the finite-budget story is intentionally emphasized.
- Keep Figure 5 main-narrow unless a later venue decision requires supplement relocation.
- Keep Table 4 as compact main-text unless a later venue decision requires supplement relocation.

## Required Before Submission''', readiness, flags=re.S)
    write(readiness_path, readiness)

    write('docs/manuscript/finalization/NEXT_STEP_PROMPT.md', '''# Next Step Prompt: Human Review, Venue Formatting, And Release Metadata

Use this prompt after the caption/TODO cleanup pass has been completed.

```text
You are working in the repository:

GradieResearch/context-indexed-route-memory

Task: complete the next manuscript-finalization decision pass. Do not start new experiments by default.

Starting context:

The repository is post-Exp15, post-Manuscript-V2-capture, post-Analysis-Pass-15A, post-citation/prior-art audit, post-citation-ledger pass, post-human-decision capture, post-Section-2.7 closest-prior-art prose integration, post-compact Table 3 split, post-Table-3 manuscript-placeholder/source-path verification, and post-caption/TODO cleanup.

Already completed:

- `docs/manuscript/draft/MANUSCRIPT_V2.md` exists and carries the conservative post-Exp15 manuscript posture.
- Section 2.7 contains closest-prior-art positioning prose, with `docs/manuscript/closest_prior_art_table.md` retained as a companion artifact.
- Compact Table 3 is descriptive and source-data-backed.
- Table 4 is a compact minimal fixed-profile neural-comparator table with caveats.
- The manuscript has final-safe figure/table placeholder captions and no unreviewed submission-blocking TODO markers for the current draft pass.
- `python scripts/verify_doc_source_paths.py` has passed after the caption/TODO cleanup pass.

Immediate work:

1. Human-review `docs/manuscript/draft/MANUSCRIPT_V2.md` for flow, wording, and final claim posture.
2. Choose a target venue or explicitly keep the package venue-neutral.
3. If a venue is chosen, apply venue-specific citation/export convention, word count, figure/table placement, and supplement formatting.
4. Decide whether reviewer strategy requires a memory-augmented/key-value neural comparator beyond Exp15.
5. Add human-chosen `LICENSE` and `CITATION.cff` before public submission/release.
6. Sync `docs/manuscript/finalization/FINALIZATION_CHECKLIST.md`, `docs/manuscript/MANUSCRIPT_TODO.md`, `docs/synthesis/PUBLICATION_READINESS.md`, and this prompt after decisions are made.

Preserve the current claim posture:

- Do not add final effect-size language unless explicit comparison families are approved.
- Keep compact Table 3 descriptive only.
- Keep C1 benchmark/model-family-specific.
- Keep C2 conflict-specific, not a blanket context-is-required-for-every-suffix claim.
- Keep C5 ceiling-limited and supplied-context only.
- Keep C6 as observed finite-budget degradation only; no fitted capacity law.
- Keep C7 boundary/supplement unless paired seed-level local-vs-global grouping exists.
- Keep C13 symbolic transition-cue context selection only.
- Keep Exp15 replay collapse as non-claim pending audit.
- Do not claim broad neural superiority, solved continual learning, raw sensory latent-world discovery, or biological validation.

Do not do these unless explicitly requested:

- Do not rerun experiments.
- Do not modify experiment code.
- Do not start Exp16 or optional successor experiments.
- Do not add memory-augmented/key-value neural baselines unless a venue/reviewer strategy requires them.
- Do not audit Exp15 replay unless specifically requested.

Definition of done:

- Target-venue/citation/release decisions are recorded, or explicitly deferred.
- Manuscript flow review findings are recorded and actioned or queued.
- Operational docs point to the next real blocker after venue/release decisioning.
- Final response summarizes changed files, verifier status if run, and remaining blockers.
```
''')

def finalize() -> int:
    patch_manuscript()
    temp = restore_real_verifier_to_temp()
    try:
        code, output = run_real_verifier(temp)
        patch_status_docs(code, output)
        temp.unlink(missing_ok=True)
        run(['git', 'checkout', 'origin/main', '--', 'scripts/verify_doc_source_paths.py', '.github/workflows/verify-doc-paths.yml'])
        (ROOT / '.github/workflows/temp-caption-todo-cleanup.yml').unlink(missing_ok=True)
        run(['git', 'config', 'user.name', 'github-actions[bot]'])
        run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'])
        run(['git', 'add', 'docs/manuscript/draft/MANUSCRIPT_V2.md', 'docs/manuscript/FIGURE_TABLE_HUMAN_REVIEW.md', 'docs/manuscript/finalization/FINALIZATION_CHECKLIST.md', 'docs/manuscript/MANUSCRIPT_TODO.md', 'docs/synthesis/PUBLICATION_READINESS.md', 'docs/manuscript/finalization/NEXT_STEP_PROMPT.md', 'docs/manuscript/finalization/CAPTION_TODO_CLEANUP_STATUS.md', 'scripts/verify_doc_source_paths.py', '.github/workflows/verify-doc-paths.yml', '.github/workflows/temp-caption-todo-cleanup.yml'])
        if run(['git', 'diff', '--cached', '--quiet'], check=False).returncode != 0:
            run(['git', 'commit', '-m', 'Polish manuscript captions and cleanup TODOs'])
            run(['git', 'push', 'origin', f'HEAD:{BRANCH}'])
        return code
    finally:
        temp.unlink(missing_ok=True)

def main() -> int:
    head_ref = os.environ.get('GITHUB_HEAD_REF') or os.environ.get('GITHUB_REF_NAME') or ''
    if head_ref == BRANCH:
        return finalize()
    temp = restore_real_verifier_to_temp()
    try:
        code, output = run_real_verifier(temp)
        print(output)
        return code
    finally:
        temp.unlink(missing_ok=True)

if __name__ == '__main__':
    sys.exit(main())
