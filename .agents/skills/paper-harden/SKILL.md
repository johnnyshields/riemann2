---
name: paper-harden
description: Adaptive read-only quality review of a paper main TeX file for rigor, consistency, formatting, and voice. Reviewers return reports only; the coordinator consolidates.
---

# Paper Harden

Read-only quality review via `role: harden-reviewer`. See `Dispatch` (long-lived agents), `Briefing`, `Team dirs`, `Ledger separation`, `Capture / Forward-carry`, and `_autoresearch.md`.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md`, especially Negative and Open-gaps for overclaim detection.
2. Create `<paper>/teams/<ts>-harden-<slug>/`; copy forward `findings.md` / `uv.md`, initialize `attempts.md`, prune, run the ledger gate, write `dispatch.md` with the ledger contract.

## Dispatch

Record team name `paper-harden-<ts>` in `dispatch.md`. Spawn only the reviewer angles the scope needs; a full pass uses rigor, consistency, formatting, voice. All reviewers get: full `_autoresearch.md`, full `findings.md`, 9-field schema, self-deposit checklist, non-goal "report only, do not edit the paper." Only the rigor reviewer receives current `uv.md`.

- **`reviewer-rigor`** — claim justification, hypotheses, theorem/proof match, handwaving, overclaim against `findings.md` / `uv.md`.
- **`reviewer-consistency`** — notation, stale renames, labels and refs, abstract/intro/conclusion counts, frozen macros.
- **`reviewer-formatting`** — compile warnings, undefined refs, duplicate labels, meaningful bad boxes, title math, bibliography consistency.
- **`reviewer-voice`** — AI tells, templated remarks, voice switches, marketing language, overclaim. Rank HIGH / MEDIUM / LOW.

## Continuing Cycle

Verify deposits. Walk each report per `Ledger separation`: durable issues → `findings.md`, obligations → `uv.md`, outcomes → `attempts.md`, suggestions → `paper-updates.md`, ranked synthesis → `collation.md`. Every reviewer issue gets a route row citing the report or a `collation.md` no-action note. Apply `Claim lifecycle` to proof-state changes. No direct paper edits.

Keep reviewers alive for follow-up passes and adjacent scopes. `send_input` to push back, narrow findings, or assign the next review. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
