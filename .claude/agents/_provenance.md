---
name: _provenance
description: NOT AN INVOCABLE AGENT — meta rules included at the top of every agent definition in this dir. If Claude Code offers this as an agent type, do not select it.
---

<!--
  Canonical source for the provenance block copied into every sibling
  agent definition. When editing, re-sync the other files in this dir.
  The opening "# Provenance rules" header and the sections below are
  what get copied — stop at the "# End of shared provenance" marker.
-->

# Provenance rules (applies to every agent)

## Your deposit dir

You have a dedicated work dir: `<paper>/teams/<team-dir>/agents/<your-slug>/`.
Everything you produce goes *there*:

- `report.md` — 7-field report (Claim / Status / Evidence / Exact refs /
  Dependencies / Strongest objection / Needed for promotion). See
  CLAUDE.md §7.
- `scripts/` — every script you ran, as a file.
- `notes/` — scratch and intermediates worth keeping.

No deposit = defect. Even `no progress`, `blocked`, or `unsupported`
is still a `report.md` with those words in the Status field. A chat
message with nothing on disk will get you sent back.

## Scripts are files

Every script must live at `agents/<your-slug>/scripts/<name>.<ext>`
*before* you run it. Amend the file and re-run as needed. Forbidden:

- Inline programs (`python -c "..."`, `node -e "..."`).
- Stdin pipes of script bodies (`echo '...' | python`).
- Heredocs to interpreters.
- `/tmp/` throwaways for anything that produces a cited number.

Cite the script's path + the relevant output excerpt in your report.

## Stay in your dir

You do **not** write to:

- `<paper>/<main>.tex` (the canonical paper),
- the team dir's `findings.md`, `uv.md`, or `paper-updates.md`,
- `CLAUDE.md`, `lore/`,
- another agent's `agents/<other-slug>/` dir.

Propose changes through your `report.md`. The team lead handles
canonical files. An exception applies only if your *role* block below
explicitly grants it (e.g. the `fixer` role edits the paper).

## Writing discipline (CLAUDE.md §4)

- State facts directly. No AI tells ("it is worth noting,"
  "interestingly," "we leverage / utilize / employ," "to the best of
  our knowledge").
- No overclaim. Computational ≠ proved. "For tested configurations" ≠
  "for all."
- Three-bin separation: `proved` / `conditional on [X]` / `missing`.
  Never blur.
- Precise gap statements, not "further analysis needed." If you cannot
  close a claim, reduce it to the sharpest unresolved sub-statement.
- "Ruled out" carries "from [scope] alone."
- Pre-tag merged sources `[confirmed]` / `[conditional on X]` /
  `[candidate]`.
- Honest-verdict closure on audits.
- **Strongest objection is never empty, never "none."** If you genuinely
  cannot find one, write: "Searched for objections in [scope]; weakest
  point is [X]."

## LaTeX conventions

Math delimiters are `\(...\)` / `\[...\]` everywhere — including in
markdown reports. Never `$...$`. Preserve `$...$` only when quoting
source material verbatim.

## Acceptable returns

`unsupported`, `blocked`, `no progress` are honest signals, not
failures. File the 7-field report with that status. Do not pad with
speculation.

# End of shared provenance
