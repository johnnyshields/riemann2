---
name: research-audit
description: N disjoint read-only audits on specified paper subsections, each graded with the fixed proved/conditional/missing framework. Optional --adversarial pairs each auditor with a checker.
---

# Research Audit

N disjoint read-only audits on subsections via `role: auditor`. See `Dispatch` (long-lived agents), `Briefing`, `Team dirs`, `Ledger separation`, `Capture / Forward-carry`, and `_autoresearch.md`.

`$ARGUMENTS`: `<subsection-list>` (sections, labels, line ranges); `--adversarial` to pair each auditor with a checker; `--non-goals: "..."` to pin specific bans.

## Preamble

1. Read the most recent team dir's `findings.md` / `uv.md`.
2. Resolve each argument to a concrete line range or `\section` block in `<paper>/<main>.tex`.
3. Create `<paper>/teams/<ts>-audit-<slug>/`. Copy prior `findings.md` / `uv.md`, initialize `attempts.md`, prune, run the ledger gate, write `dispatch.md` with the ledger contract.

## Dispatch

Record team name `research-audit-<ts>` in `dispatch.md`. Spawn one `auditor-<sub>` per subsection; with `--adversarial`, also spawn paired `adversary-<sub>` that reads the auditor's report once it lands.

Each auditor's brief: current `findings.md`, exact subsection text, 9-field schema, writing-discipline reminder with three-bin grading, self-deposit checklist, synthesized non-goals. Share a UV entry only when the audited range contains its matching `rem:wip-*`.

Grading framework: each claim is `proved as written`, `conditional but honestly stated`, or `still a real gap`. Adversary checkers return `verified`, or `rejected` / `blocked` with concrete breaks.

## Continuing Cycle

Verify every expected `report.md` exists; chase missing. Write `collation.md` with per-subsection verdicts. Process each report per `Ledger separation`: lessons → `findings.md`, new obligations → `uv.md`, outcomes → `attempts.md`, paper-ready → `paper-updates.md`. Every audit/verifier verdict gets a route row citing the report or a `collation.md` no-action note. Apply `Claim lifecycle` to proof-state changes. Lore entry only if proof state changed. No direct `<main>.tex` edits.

Keep auditors and paired adversaries alive for follow-up audits, source checks, adjacent ranges. Use `send_input` rather than spawning replacements. `close_agent` only at terminal condition, halt, stale team, or clear better replacement.
