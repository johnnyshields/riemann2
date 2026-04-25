---
name: research-resume
description: Continue research-attack or research-team from an existing paper team directory. Same dispatch rules — tight roster, mode-assigned researchers, lazy verifier, cross-audit — but reuses the existing team dir and creates only new agent subdirs.
---

# Research Resume

Resume work in an existing team dir. Same dispatch rules as `research-attack` (default tight pattern) or `research-team` (broader fallback): mode-assigned researchers, coordinator-led synthesis, lazy verifier, cross-audit via redelegation. Only difference: don't create a sibling team dir — reuse the supplied dir and create fresh `agents/<resume-ts>-<agent-slug>/` subdirs.

`$ARGUMENTS`: existing `<paper>/teams/<ts>-<slug>/` path; optional focus (`UV-NNN`, `rem:wip-*`, route name). No focus → choose the most blocking frontier from the existing dir without asking.

## Preamble

1. Resolve the existing team dir. It must be the working snapshot for this cycle. Don't create a new dir.
2. Read `findings.md`, `uv.md`, `attempts.md` (legacy `attempts.tsv` if present), `dispatch.md`, `collation.md`, `paper-updates.md` if present, current `rem:wip-*` labels, last 2-3 relevant lore entries, every `agents/*/report.md`.
3. Capture stranded material per `Ledger separation`: UVs → `uv.md`, lessons → `findings.md`, routes → `attempts.md`, no-action → `collation.md`. `attempts.tsv` is legacy context — import only live next-actions.
4. Run the ledger gate.
5. Initialize missing stubs only inside the existing dir.
6. Append `## Resume dispatch <timestamp>` to `dispatch.md` with current commit, roster + per-lane mode, targets, exact in-scope files/lines/reports, protected surfaces, non-goals, fixed-harness criteria, ground-truth checks, budgets, ledger contract. Commit by named paths.

## Dispatch

Record team name `research-resume-<existing-ts-or-slug>-<resume-ts>` in `dispatch.md`. Spawn the coordinator-selected tight roster (typically 1-3 researchers with assigned modes from `attack` / `explore` / `audit` / `synthesis`). Cross-audit via `verify`-mode redelegation when a candidate exists. Spawn a fresh independent verifier only when independence matters. Each fresh teammate gets:

`<existing-team-dir>/agents/<resume-ts>-<agent-slug>/`

Never reuse an old agent dir. Existing team files stay authoritative.

Briefings match `research-attack` / `research-team`: full `_autoresearch.md`, full `findings.md`, 9-field schema, non-goals, deposit path, self-deposit checklist, `Writing discipline`, mode-specific UV/report exceptions per `Briefing`.

Don't ask for approval. Pick roster, modes, and targets from the recovered frontier and proceed.

## Continuing Cycle

All capture in the existing dir.

1. Verify each returning researcher deposited `report.md` + cited `scripts/` / `notes/`. Chase missing; record gaps in `collation.md`.
2. Walk each report per `Ledger separation`. Process proof-state changes through `Claim lifecycle`. `attempts.md` rows cite reports. Write `collation.md` no-action notes where needed. Refresh frontier summaries. Commit logical units by named paths.
3. Coordinator owns synthesis: theorem formulation, ledger filing, paper integration. Don't delegate this to a subagent.
4. Cross-audit: redelegate an existing researcher in `verify` mode to a sibling's deposit once it's stable. Spawn a fresh verifier only when independence matters.
5. Respond to each researcher with a concrete follow-up, sharper objection, or next bounded lane.
6. `paper-updates.md` for paper-ready edits only. Direct `<main>.tex` edits stay coordinator-owned.

Keep the resumed team alive. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
