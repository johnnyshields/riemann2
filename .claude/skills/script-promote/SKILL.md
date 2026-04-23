---
name: script-promote
description: Harden a verification script from scripts/wip/ into final-scripts/<paper>/ with a clean docstring, paper cross-reference, and a lore note.
---

# Script Promote

Promote a verification script to a hardened version in
`final-scripts/<paper>/`.

`$ARGUMENTS`: a description of what the script verifies (e.g.
`"within-zone margin factor of 13"`, `"spectral gap \(\ge 1/2\)"`,
`"rectangle identity"`).

## Preamble

Read `findings.md` (cross-reference with any relevant goodie). Create
`<paper>/teams/<ts>-other-script-<slug>/` with `reports/`, `scripts/`, `notes/`.

## Dispatch

`TeamCreate team_name: "script-promote-<ts>"`. Spawn `promoter-<slug>`.
Standard briefing plus the specific UV-NNN entry the script verifies,
if any (narrow exception). Writing discipline: docstrings and lore
state what the script proves cleanly, no overclaim.

**Edit-capable exception**: promoter may create a file under
`final-scripts/<paper>/` and a new lore file. No other canonical files.

Promoter's job:

1. Find the claim in `<paper>/<main>.tex` — exact wording, line number,
   math.
2. Search the repo for existing scripts: `scripts/`, `scripts/wip/`,
   `final-scripts/<paper>/`, `<paper>/teams/*/scripts/`. Grep with keywords; check
   docstrings.
3. Produce the hardened script at
   `final-scripts/<paper>/NN_descriptive_name.py` (next available NN).
   Base it on any existing script found; else write from scratch.
   Self-contained, runnable via `python3`. Use `final-scripts/<paper>/lib/`
   for shared utilities. Docstring includes paper line reference,
   `rem:wip-*` label, UV-NNN if applicable.
4. Run it; record stdout in `notes/run-output.txt`.
5. Write a lore file `lore/YYYYMMDD-script-<slug>.md` — claim, paper
   ref, provenance (base script or scratch), pass/fail, any issues,
   team dir pointer.
6. Deposit the 7-field report and `SendMessage` team-lead; stay idle.

## Post-cycle

Coordinator reviews the script and report. If execution surfaced a new
finding, call `research-capture`. Shut down, `TeamDelete`. Commit
`final-scripts/<paper>/NN_*.py` + lore file + team dir; stage by name,
cite the dir.
