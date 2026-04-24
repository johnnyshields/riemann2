---
name: research-resume
description: Continue research-team from an existing paper team directory. Same adaptive roster, one-ahead verification pattern, briefing, capture, and provenance rules as research-team; the only difference is that it reuses the existing team dir and creates only new agent subdirs.
---

# Research Resume

`research-team` run in an existing team dir. Same roster, one-ahead pattern, briefing, capture, long-lived agents, autoresearch, promotion. Only difference: don't create a sibling team dir. Reuse the supplied dir and create fresh `agents/<resume-ts>-<agent-slug>/` subdirs.

`$ARGUMENTS`: existing `<paper>/teams/<ts>-<slug>/` path; optional focus (`UV-NNN`, `rem:wip-*`, route name). No focus → choose the most blocking frontier from the existing dir without asking.

## Preamble

1. Resolve the existing team dir. It must be the working snapshot for this cycle. Don't create a new dir.
2. Read `findings.md`, `uv.md`, `attempts.md` (legacy `attempts.tsv` if present), `dispatch.md`, `collation.md`, `paper-updates.md` if present, current `rem:wip-*` labels, last 2-3 relevant lore entries, every `agents/*/report.md`.
3. Capture stranded material per `Ledger separation`: UVs → `uv.md`, lessons → `findings.md`, routes → `attempts.md`, no-action → `collation.md`. `attempts.tsv` is legacy context — import only live next-actions.
4. Run the ledger gate.
5. Initialize missing stubs only inside the existing dir.
6. Append `## Resume dispatch <timestamp>` to `dispatch.md` with current commit, roster, verifier queue, targets, exact in-scope files/lines/reports, protected surfaces, non-goals, fixed-harness criteria, ground-truth checks, budgets, ledger contract. Commit by named paths.

## Dispatch

Record team name `research-resume-<existing-ts-or-slug>-<resume-ts>` in `dispatch.md`. Same dispatch rules as `research-team`: spawn the coordinator-selected live roster, keep research/exploration lanes moving, add verifiers when deposits are ready or risk demands it. Each fresh teammate gets:

`<existing-team-dir>/agents/<resume-ts>-<agent-slug>/`

Never reuse an old agent dir. Existing team files stay authoritative.

Briefings match `research-team`: full `_autoresearch.md`, full `findings.md`, 9-field schema, non-goals, deposit path, self-deposit checklist, `Writing discipline`, role-specific UV/report exceptions.

Don't ask for approval. Pick roster and targets from the recovered frontier and proceed.

## Continuing Cycle

Same as `research-team`, all capture in the existing dir.

1. Verify each returning agent deposited `report.md` + cited `scripts/` / `notes/`. Chase missing; record gaps in `collation.md`.
2. Walk each report per `Ledger separation`. Process proof-state changes through `Claim lifecycle`. `attempts.md` rows cite reports. Write `collation.md` no-action notes where needed. Refresh frontier summaries. Commit logical units by named paths.
3. One-ahead: queue verification while independent research/exploration continues. Wait only when the next move depends on the verifier.
4. Respond to each agent with a concrete follow-up, adversarial challenge, or next task.
5. `paper-updates.md` for paper-ready edits only. No direct `<main>.tex` edits.

Keep the resumed team alive. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
