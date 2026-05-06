# Experiment Completion Checklist

An experiment is not complete until every item below is checked.

## Design

- [ ] Experiment design exists.
- [ ] Hypotheses are explicit.
- [ ] Metrics are defined.
- [ ] Variants/baselines are defined.
- [ ] Expected failure modes are listed.
- [ ] Manuscript relevance is stated.

## Implementation

- [ ] Experiment has its own directory under `experiments/`.
- [ ] README exists.
- [ ] Smoke/standard/full profiles are documented or intentionally omitted.
- [ ] Run manifest is produced.
- [ ] Validation report is produced.
- [ ] Summary CSVs are produced.
- [ ] Plots are produced.
- [ ] Smoke run passes.

## Run

- [ ] Standard/full run completed.
- [ ] Artifacts are committed or staged appropriately.
- [ ] Run profile, seeds, and config are recorded.
- [ ] Validation report checked.

## Analysis

- [ ] Artifacts uploaded to ChatGPT.
- [ ] Analysis completed.
- [ ] Caveats identified.
- [ ] Claims classified conservatively.
- [ ] Figures assessed.

## Thread digest

- [ ] Analysis digest generated.
- [ ] Digest saved under `docs/threads/`.
- [ ] Digest indexed in `docs/threads/THREAD_INDEX.md`.

## Repository import

- [ ] Experiment summary updated.
- [ ] Experiment registry updated.
- [ ] Claims/evidence updated.
- [ ] Figure plan updated.
- [ ] Limitations updated.
- [ ] TODOs updated.
- [ ] Synthesis docs updated.
- [ ] Conflict log updated if needed.
- [ ] Path verifier passes.

## QA

- [ ] Repo update QA completed.
- [ ] No claims overstrengthened.
- [ ] No planned results treated as completed.
- [ ] No missing active source paths.
- [ ] Next action decided.
