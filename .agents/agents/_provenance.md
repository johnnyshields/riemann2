---
name: _provenance
description: NOT INVOCABLE — provenance rules included in every agent definition.
---

# Provenance (every agent)

## Deposit dir

Your dir: `<paper>/teams/<team-dir>/agents/<your-slug>/`. Everything you produce goes there:

- `report.md` — 9-field report (`AGENTS.md` `Report schema`).
- `scripts/` — every script you ran, as a file.
- `notes/` — scratch, intermediates worth keeping.

No deposit = defect. `no progress` / `blocked` / `unsupported` is still a `report.md` with that word in Status. A chat message with nothing on disk gets sent back.

## Scripts are files

Every script lives at `agents/<your-slug>/scripts/<name>.<ext>` *before* it runs. Amend the file and rerun. **Forbidden:** inline programs (`python -c`), stdin pipes (`echo ... | python`), heredocs to interpreters, `/tmp/` throwaways for anything that produces a cited number. Cite path + output excerpt.

## Stay in your dir

Do **not** write to `<paper>/<main>.tex`, the team dir's `findings.md` / `uv.md` / `attempts.md` / `collation.md` / `dispatch.md` / `paper-updates.md`, `AGENTS.md`, `lore/`, or another agent's dir. Propose changes via `report.md`. Name the ledger destination for each material signal — don't leave the team lead to guess. Role exception (e.g. `fixer` editing the paper) is granted in your role block below if it applies.

## Chat is secondary

Codex/ChatGPT exports help reconstruct decisions but don't replace deposits. Cite an exported chat path when it explains *why*. Never let an app-only hidden thread be the sole evidence for a math/computational claim.

## Discipline

Follow `AGENTS.md` `Writing discipline` and `LaTeX conventions`. Strongest objection is never empty — if you genuinely can't find one, write "Searched in [scope]; weakest point is [X]."

## Acceptable returns

`unsupported`, `blocked`, `no progress` are honest signals, not failures. File the report; don't pad with speculation.
