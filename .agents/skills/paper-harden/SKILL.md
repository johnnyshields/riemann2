---
name: paper-harden
description: Adaptive read-only quality review of a paper main TeX file across rigor, consistency, formatting, and voice axes. Researchers run audit mode on one axis each; coordinator consolidates.
---

# Paper Harden

Read-only quality review via researchers in `audit` mode, one per axis. See `Dispatch`, `Briefing`, `Team dirs`, `Ledger separation`, `Capture / Forward-carry`, and `_autoresearch.md`.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md`, especially Negative and Open-gaps for overclaim detection.
2. Create `<paper>/teams/<ts>-harden-<slug>/`; copy forward `findings.md` / `uv.md`, initialize `attempts.md`, prune, run the ledger gate, write `dispatch.md` with the ledger contract.

## Dispatch

Record team name `paper-harden-<ts>` in `dispatch.md`. Spawn only the axes the scope needs; a full pass uses all four. Each researcher gets `audit` mode plus an axis tag in the brief, and `agents/<ts>-axis-<name>/`. All briefs include `_autoresearch.md`, full `findings.md`, the 9-field schema, the self-deposit checklist, and the non-goal "report only, do not edit the paper." Only the rigor axis receives current `uv.md`.

Axes (one researcher each):

- **rigor** — claim justification, hypotheses, theorem/proof match, handwaving, overclaim against `findings.md` / `uv.md`.
- **consistency** — notation, stale renames, labels and refs, abstract/intro/conclusion counts, frozen macros.
- **formatting** — compile warnings, undefined refs, duplicate labels, meaningful bad boxes, title math, bibliography consistency.
- **voice** — AI tells, templated remarks, voice switches, marketing language, overclaim. Rank HIGH / MEDIUM / LOW.

## Continuing Cycle

Verify deposits. Walk each report per `Ledger separation`: durable issues → `findings.md`, obligations → `uv.md`, outcomes → `attempts.md`, suggestions → `paper-updates.md`, ranked synthesis → `collation.md`. Every reviewer issue gets a route row citing the report or a `collation.md` no-action note. Apply `Claim lifecycle` to proof-state changes. No direct paper edits.

Keep reviewers alive for follow-up passes and adjacent scopes. `send_input` to push back, narrow findings, assign the next axis or scope. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
