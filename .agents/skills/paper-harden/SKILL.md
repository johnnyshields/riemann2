---
name: paper-harden
description: Adaptive read-only quality review of a paper main TeX file for rigor, consistency, formatting, and voice. Reviewers return reports only; the coordinator consolidates.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Harden

Read-only quality review via `role prompt: harden-reviewer`. Follow
`.agents/references/agents/_autoresearch.md`, AGENTS.md `Dispatch`
long-lived-agent rules, `Briefing rule`, `Team dirs and agent self-deposit`,
`State ledger separation`, and `Capture before shutdown, forward-carry at
dispatch`. Use the inherited Codex model by default.

## Preamble

1. Read the most recent team dir's `findings.md` and `uv.md`, especially
   Negative and Open-gaps for overclaim detection.
2. Create `<paper>/teams/<ts>-harden-<slug>/`; copy forward `findings.md` and
   `uv.md`, initialize `attempts.md`, prune, and write `dispatch.md`.

## Dispatch

When delegated teamwork is authorized, record team name `paper-harden-<ts>` in
`dispatch.md`. Spawn only the reviewer angles the scope needs; a full pass uses
rigor, consistency, formatting, and voice. All reviewers get the standard
briefing, full autoresearch metaprompt, full `findings.md`, 9-field schema,
self-deposit checklist, and non-goal "report only, do not edit the paper."
Only the rigor reviewer receives current `uv.md`.

- **`reviewer-rigor`** - claim justification, hypotheses, theorem/proof match,
  handwaving, overclaim against `findings.md` and `uv.md`.
- **`reviewer-consistency`** - notation consistency, stale renames, labels and
  refs, abstract/intro/conclusion counts, frozen macros.
- **`reviewer-formatting`** - compile warnings, undefined refs, duplicate
  labels, meaningful bad boxes, title math, bibliography consistency.
- **`reviewer-voice`** - AI tells, templated remarks, voice switches,
  marketing language, overclaim. Rank HIGH / MEDIUM / LOW.

## Continuing Cycle

Verify deposits. Walk each report by `State ledger separation`: durable issues
to `findings.md`, proof obligations to `uv.md`, review outcomes to
`attempts.md`, paper-ready suggestions to `paper-updates.md`, and ranked
synthesis to `collation.md`. Apply `Claim lifecycle (git-as-archive)` to any
proof-state change. No direct paper edits here.

Keep reviewers alive for follow-up passes and adjacent scopes while their
context is fresh. Use `send_input` to push back, ask for narrowed findings, or
assign the next review. Use `close_agent` only at a terminal condition, explicit
user halt, stale long-idle team, or when replacement is clearly better.
