---
name: script-promote
description: Harden a verification script from scripts/wip into a final-scripts paper directory with a clean docstring, paper cross-reference, provenance, and a lore note.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Script Promote

Promote a verification script to a hardened version in `final-scripts/<paper>/`.

`$ARGUMENTS`: a description of what the script verifies, such as
`"within-zone margin factor of 13"` or `"spectral gap \(\ge 1/2\)"`.

## Preamble

Read the current team dir's `findings.md`, `uv.md`, and relevant reports. Create
`<paper>/teams/<ts>-other-script-<slug>/` with copy-forward `findings.md` and
`uv.md`, fresh `attempts.md`, and an `agents/<ts>-promoter-<slug>/` deposit dir.

## Dispatch

When delegated teamwork is authorized, record team name `script-promote-<ts>` in
`dispatch.md`. Spawn `promoter-<slug>` with a self-contained hardening brief and
the inherited Codex model. Include the specific UV-NNN entry the script verifies,
if any. Writing discipline: docstrings and lore state what the script proves
cleanly, no overclaim.

**Edit-capable exception:** promoter may create a file under
`final-scripts/<paper>/` and a new lore file. No other canonical files.

Promoter's job:

1. Find the claim in `<paper>/<main>.tex`: exact wording, line number, math.
2. Search existing scripts under `scripts/`, `scripts/wip/`,
   `final-scripts/<paper>/`, and `<paper>/teams/*/scripts/`.
3. Produce `final-scripts/<paper>/NN_descriptive_name.py`, based on existing
   code when possible, self-contained and runnable with the repo's Python.
   Docstring includes paper line ref, `rem:wip-*`, UV-NNN if applicable, and
   provenance.
4. Run it and record stdout in `notes/run-output.txt`.
5. Write `lore/YYYYMMDD-script-<slug>.md`: claim, paper ref, provenance, result,
   issues, and team dir pointer.
6. Deposit the 9-field report under `agents/<ts>-promoter-<slug>/report.md` and
   stay available for follow-up.

## Post-cycle

Coordinator reviews the script and report by `State ledger separation`: new
findings to `findings.md`, new obligations to `uv.md`, promotion route outcome
to `attempts.md`, and synthesis to `collation.md`. Commit
`final-scripts/<paper>/NN_*.py`, lore file, and team dir by named paths.
