---
name: research-team
description: Broader-cycle dispatch for when the frontier lacks a focused target. Researchers are assigned modes (attack / explore / audit / synthesis) per lane. Prefer `research-attack` whenever a concrete target exists.
---

# Research Team

Broader cycle when the frontier lacks focus and needs scoping work. Default to `research-attack` whenever a concrete UV target exists — `research-team` is the secondary tool. See `Dispatch`, `Briefing`, `Team dirs`, `Capture / Forward-carry`, and `_autoresearch.md`.

Coordinator owns theorem formulation and ledger/paper integration directly. Subagents take bounded technical lanes — coordinator-assigned modes from `attack`, `explore`, `audit`, `synthesis`.

`$ARGUMENTS`: empty → coordinator picks the most useful frontier; topic phrase → orient around it; `UV-NNN` → assign at least one researcher in `attack` mode to it.

## Preamble

1. Read the most recent team dir's `findings.md`, `uv.md`, current `rem:wip-*` labels, last 2-3 lore entries, recent reports.
2. Create `<paper>/teams/<ts>-<team-slug>/`. Copy prior `findings.md` / `uv.md`, prune, add uncaptured material, initialize fresh `attempts.md`, carry only open next-actions into `dispatch.md` or `collation.md`. Commit.
3. Run the ledger gate.
4. Pick the initial roster (typically 2-3) and assign modes per lane. Write `dispatch.md` with originating commit, roster + per-lane mode, targets, exact in-scope files/lines/reports, protected surfaces, non-goals, fixed-harness criteria, ground-truth checks, budgets, ledger contract.

## Dispatch

Record team name `research-team-<ts>` in `dispatch.md`. Spawn the coordinator-selected initial roster — small, not broad. Each researcher gets `agents/<ts>-<lane-slug>/` and a brief naming exactly one mode:

- `attack` — bounded gap; UV entry verbatim if relevant
- `explore` — adjacent structure; no `uv.md` content
- `audit` — read-only grading of a subsection
- `synthesis` — internal/external/under-the-nose axis (one per researcher)

Every brief includes `_autoresearch.md`, the team dir's full `findings.md`, the 9-field schema, non-goals, deposit path, self-deposit checklist, `Writing discipline`. Per-mode UV-content rules per `Briefing`.

Keep teammates alive after first deposit. `send_input` to redelegate to the next lane or switch the mode (typically to `verify` for cross-audit). Spawn fresh researchers when the new lane needs independence from the existing pool.

Verification is lazy: don't spawn `verify`-mode work until a concrete deposit exists to attack. Cross-audit via redelegation by default; fresh verifier only when independence matters.

`unsupported` / `blocked` / `no progress` are acceptable returns.

## Continuing Cycle

1. Verify each returning agent deposited `report.md` plus cited `scripts/` / `notes/`. Chase missing via `send_input`; log gaps in `collation.md`.
2. Walk each report per `Ledger separation`. Process proof-state changes through `Claim lifecycle`. Refresh frontier summaries. Commit per deposit where possible.
3. Coordinator owns synthesis: theorem formulation, ledger filing, paper integration. Don't delegate this to a subagent.
4. Maintain one-ahead: queue cross-audit for stable claims; immediately redelegate independent next moves to research lanes. Wait only when the next move depends on the audit.
5. `paper-updates.md` for paper-ready edits only. Direct `<main>.tex` edits stay coordinator-owned.
6. Lore entry only for major direction changes or team-level decisions.

Don't shut down at ordinary cycle boundaries. Keep the team alive. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
