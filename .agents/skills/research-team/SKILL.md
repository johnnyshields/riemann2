---
name: research-team
description: Primary workhorse. Dispatches a coordinator-selected live roster via Codex subagents when delegated teamwork is authorized, with one team dir and per-agent subdirs under paper teams. Uses a one-ahead pattern where researchers keep attacking while verifiers review prior stable deposits.
---

# Research Team

Adaptive research dispatch via Codex subagents. The coordinator picks the live roster from the frontier: gap-closers for concrete UVs, explorers for redirects, verifiers when there's something specific to check. Verification is one step behind the research lane. See `Dispatch`, `Briefing`, `Team dirs`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: empty → coordinator picks the most useful frontier; topic phrase → orient around it; `UV-NNN` → assign at least one gap-closer.

## Preamble

1. Read the most recent team dir's `findings.md`, `uv.md`, current `rem:wip-*` labels, last 2-3 lore entries, and recent agent reports.
2. Create `<paper>/teams/<ts>-<team-slug>/`. Copy prior `findings.md` / `uv.md`, prune dead entries, add uncaptured material, initialize a fresh `attempts.md`, carry only open next-actions into `dispatch.md` or `collation.md`. Commit.
3. Run the ledger gate: every prior landed report is filed correctly or has a `collation.md` no-action note.
4. Pick the initial roster and one-ahead cadence. Write `dispatch.md` with originating commit, roster, verifier queue, targets, exact in-scope files/lines/reports, protected surfaces, non-goals, fixed-harness criteria, ground-truth checks, budgets/timeouts, ledger contract.

## Dispatch

Record team name `research-team-<ts>` in `dispatch.md`. Spawn the coordinator-selected initial roster — not a fixed quota. Start enough research/exploration lanes to keep work moving; add verifiers when a deposit is ready to check or risk demands it. Each agent's slug gets its own `agents/<ts>-<agent-slug>/`.

Keep teammates alive after first deposit. Idle ≠ done. Use `send_input` to reuse context; spawn fresh agents for new roles, independence, blocked teammates, or stale long-idle teams.

Every brief includes the full `_autoresearch.md`, the team dir's full `findings.md`, the 9-field schema, non-goals, exact deposit path, self-deposit checklist, and `Writing discipline`.

Role-specific:

- **Gap-closers** receive their UV entry verbatim from `uv.md`; brief with "What is the cleanest target?", smallest concrete unresolved sub-statements, routes A/B/C, fallback.
- **Explorers** receive no `uv.md` content by default; return observations tagged `[confirmed]` / `[conditional]` / `[candidate]`.
- **Verifiers / source auditors** review specific prior deposits, not the whole frontier. If no target is ready, don't spawn yet. Give only the UV entries and reports needed for the check.

`unsupported` / `blocked` / `no progress` are acceptable returns.

## Continuing Cycle

1. Verify each returning agent deposited `report.md` plus cited `scripts/` and `notes/`. Chase missing deposits via `send_input`; log gaps in `collation.md`.
2. Walk each report. Classify per `Ledger separation`: UV candidates → `uv.md`, reusable lessons → `findings.md`, route outcomes → `attempts.md`, synthesis/no-action → `collation.md`, paper-ready → `paper-updates.md`. Every substantial route gets either an `attempts.md` row citing the report or a `collation.md` no-action note. Process proof-state changes through `Claim lifecycle`. Refresh frontier summaries. Commit per deposit where possible.
3. Maintain one-ahead: queue verifier work for stable claims; immediately redelegate independent next moves to research. Wait only when the next move depends on the verifier.
4. Respond to each agent with one concrete follow-up, challenge, clarification, or next adjacent task.
5. Write `paper-updates.md` only for paper-ready edits. No direct `<main>.tex` edits — promotion is a separate deliberate step.
6. Lore entry only for major direction changes or team-level decisions.

Don't shut down at ordinary cycle boundaries. Keep the team alive. Use `close_agent` only at terminal condition, explicit halt, stale long-idle team, or clear better replacement.
