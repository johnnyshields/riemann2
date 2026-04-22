# Script Promote

Promote a computation or verification script to a hardened version in
`final-scripts/paper/`. See `CLAUDE.md` §3, §5, §8.

**Argument:** `$ARGUMENTS` — a description of the proposition, claim, or
paper section the script verifies (e.g. `"within-zone margin factor of
13"`, `"spectral gap \(\ge 1/2\)"`, `"rectangle identity"`).

## Mandatory preamble

1. Read `paper/findings.md` and `paper/unverified.tex` (so the promoted
   script is cross-referenced against any relevant UV entry or goodie).
2. Create task dir `tasks/<ts>-other-script-<slug>/` with `reports/`,
   `scripts/`, `notes/`. Announce it.

## Dispatch

`TeamCreate team_name: "script-promote-<ts>"` and spawn one teammate
`promoter-<slug>`. Its briefing MUST include:
- Full `paper/findings.md`.
- Per `CLAUDE.md` §7 exception: the specific UV-NNN entry the script
  verifies (if one exists) — pasted verbatim. Do not share other UV
  entries.
- The 7-field report schema.
- The writing-discipline reminder (`CLAUDE.md` §3a): docstrings and
  lore should state what the script proves cleanly, no overclaim.
- The self-deposit checklist (intermediate work goes in
  `tasks/<dir>/scripts/`, final report in
  `tasks/<dir>/reports/promoter-<slug>.md`).
- **Edit-capable exception for this session**: the promoter may create
  a new file under `final-scripts/paper/` and a new lore file. No other
  canonical files.
- The checklist below (Steps 1–6).

### Step 1: Find the claim in the paper

Search `paper/proof_of_rh.tex` for the relevant claim. Note exact
wording, line number, and mathematical content.

### Step 2: Find existing scripts

Search the repo for related Python scripts:
- `scripts/` and `scripts/wip/`
- `computation/` (if present)
- `final-scripts/paper/`
- `tasks/*/scripts/` (prior task-dir scripts)
- `.claude/worktrees/*/` (old worktree copies)

Use `Grep` with keywords from the claim. Check docstrings and comments.

### Step 3: Create the hardened script

- If an existing script is found, use it as the base. Clean up, add a
  docstring with paper reference (line number, `rem:wip-*` label if
  present, UV-NNN if relevant), add clear pass/fail output, follow the
  style of existing `final-scripts/paper/` files.
- If none found, write from scratch.
- Name it `final-scripts/paper/NN_descriptive_name.py` where `NN` is the
  next available number.
- Script must be self-contained and runnable via `python3 script.py`.
- Use `final-scripts/paper/lib/` for shared utilities if applicable.

### Step 4: Run the script

Confirm it passes. Record stdout in `tasks/<dir>/notes/run-output.txt`.

### Step 5: Write a lore file

Create `lore/YYYYMMDD-script-<slug>.md` documenting:
- What claim the script verifies (paper line reference + `rem:wip-*` +
  UV-NNN).
- Provenance (which existing script it came from, or "written from
  scratch").
- Results (pass/fail counts).
- Any issues found (does the paper's claim hold?).
- Pointer to the task dir.

### Step 6: Report

Send a 7-field report via `SendMessage` to `team-lead`, then stay idle
(do NOT self-shutdown — coordinator shuts down).

## After completion

1. Coordinator reviews the report and the promoted script.
2. If the script execution surfaced a new finding, call
   `research-capture` (goodie or negative or gap, as appropriate).
3. `SendMessage` promoter `{type:"shutdown_request"}`, `TeamDelete`.
4. Commit `final-scripts/paper/NN_*.py` + the lore file + the task dir.
   Cite task dir in the body. Stage by name.
