---
name: script-promote
description: Harden a verification script from scripts/wip/ into final-scripts/<paper>/ with a clean docstring, paper cross-reference, and a lore note.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

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

`Codex subagent delegation when explicitly requested team_name: "script-promote-<ts>"`. Spawn `promoter-<slug>` with
`Codex agent role: general-purpose` and the inherited Codex model by default, always. Standard briefing plus the specific UV-NNN entry the script verifies,
if any (narrow exception). Writing discipline: docstrings and lore
state what the script proves cleanly, no overclaim.

**Edit-capable exception**: promoter may create a file under
`final-scripts/<paper>/` and a new lore file. No other canonical files.

Promoter's job:

1. Find the claim in `<paper>/<main>.tex` â€” exact wording, line number,
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
5. Write a lore file `lore/YYYYMMDD-script-<slug>.md` â€” claim, paper
   ref, provenance (base script or scratch), pass/fail, any issues,
   team dir pointer.
6. Deposit the 9-field report and `send_input` team-lead; stay idle.

## Post-cycle

Coordinator reviews the script and report. If execution surfaced a new
finding, call `research-capture`. Shut down, `close_agent`. Commit
`final-scripts/<paper>/NN_*.py` + lore file + team dir; stage by name,
cite the dir.


