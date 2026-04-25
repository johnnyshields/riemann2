---
name: research-audit
description: N disjoint read-only audits on specified paper subsections, each graded with the fixed proved/conditional/missing framework. Optional --adversarial pairs each audit lane with a cross-audit checker.
---

# Research Audit

N disjoint read-only audits on subsections via researchers in `audit` mode. See `Dispatch` (long-lived agents, lazy verifier, cross-audit), `Briefing`, `Team dirs`, `Ledger separation`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: `<subsection-list>` (sections, labels, line ranges); `--adversarial` to pair each audit lane with a cross-audit checker; `--non-goals: "..."` to pin specific bans.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md`.
2. Resolve each argument to a concrete line range or `\section` block in `<paper>/<main>.tex`.
3. Create `<paper>/teams/<ts>-audit-<slug>/`. Copy prior `findings.md` / `uv.md`, initialize `attempts.md`, prune, run the ledger gate, write `dispatch.md` with the ledger contract.

## Dispatch

Record team name `research-audit-<ts>` in `dispatch.md`. Spawn one researcher per subsection in `audit` mode → slug `audit-<sub>`. With `--adversarial`, redelegate each auditor in `verify` mode to a sibling's deposit once it lands (cross-audit), or spawn a fresh `verify-<sub>` researcher if the lane needs independence.

Each brief: current `findings.md`, exact subsection text, 9-field schema, three-bin grading reminder, self-deposit checklist, synthesized non-goals. Share a UV entry only when the audited range contains its matching `rem:wip-*`.

Grading: each claim is `proved as written`, `conditional but honestly stated`, or `still a real gap`. Cross-audit checkers return `verified`, or `rejected` / `blocked` with concrete breaks.

## Continuing Cycle

Verify every expected `report.md`; chase missing. Write `collation.md` with per-subsection verdicts. Process per `Ledger separation`: lessons → `findings.md`, new obligations → `uv.md`, outcomes → `attempts.md`, paper-ready → `paper-updates.md`. Every audit/cross-audit verdict gets a route row citing the report or a `collation.md` no-action note. Apply `Claim lifecycle` to proof-state changes. Lore entry only if proof state changed. No direct `<main>.tex` edits.

Keep auditors alive for follow-up audits, source checks, adjacent ranges. `send_input` rather than spawning replacements; switch their mode (e.g. `audit` → `verify` for cross-audit) as needed. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
