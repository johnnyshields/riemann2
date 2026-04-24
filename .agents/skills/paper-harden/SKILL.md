---
name: paper-harden
description: Read-only 4-agent quality review of <paper>/<main>.tex â€” rigor, consistency, formatting, voice. Reviewers return reports only; the coordinator consolidates.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Paper Harden

Four-angle read-only quality review via `role prompt: harden-reviewer`.
Follows `.agents/references/agents/_autoresearch.md`, AGENTS.md `Dispatch`
long-lived-agent rules, `Briefing rule`, `Team dirs and agent self-deposit`,
`Capture before shutdown, forward-carry at dispatch`. Use the inherited Codex model by default.

## Preamble (forward-carry first â€” `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`
   (especially Negative + Open-gaps, for overclaim detection).
2. Create `<paper>/teams/<ts>-harden-<slug>/`. `<slug>` may be
   `post-referee`, `pre-submission`, or generic. Copy forward
   `findings.md` + `uv.md`; prune.
3. Write `dispatch.md` describing scope and non-goals.

## Dispatch

When delegated teamwork is authorized, record team name `paper-harden-<ts>` in `dispatch.md`. Spawn four reviewers
(`role prompt: harden-reviewer`, inherited Codex model) with the standard briefing,
the full `.agents/references/agents/_autoresearch.md` metaprompt, and non-goal "report only,
do not edit the paper." Only `reviewer-rigor` additionally receives the current
`uv.md` (for overclaim detection â€” narrow `Briefing rule` exception); the others
do not.

- **`reviewer-rigor`** â€” every claim justified, every hypothesis
  present, theorem-vs-proof match, no handwaving. Cross-checks
  `findings.md` Negative for silently-retried dead ends and `uv.md`
  for claims that should be quarantined but aren't.
- **`reviewer-consistency`** â€” notation consistency, stale renames,
  label/ref integrity, abstract/intro/conclusion counts match,
  frozen-macro compliance.
- **`reviewer-formatting`** â€” compile warnings, undefined refs,
  multiply-defined labels, substantive overfull/underfull boxes,
  `\texorpdfstring` on math-in-titles, bibliography consistency.
- **`reviewer-voice`** â€” AI tells, templated-remark patterns, voice
  switches within paragraphs, marketing language, overclaim. Rank
  HIGH / MEDIUM / LOW.

## Continuing cycle (capture, redelegate, keep alive â€” `Capture before shutdown, forward-carry at dispatch`)

Verify deposits. Walk each report, process findings through `Claim lifecycle (git-as-archive)` â€”
append bullets to this team dir's `findings.md`, file new UVs in
`uv.md`, or stage text-edit suggestions in `paper-updates.md`. Write
`collation.md` summary ranked HIGH / MEDIUM / LOW. No direct paper
edits here.

Keep reviewers alive for follow-up passes and adjacent scopes while their context
is fresh. Use `send_input` to push back, ask for narrowed findings, or assign the
next review. Use `close_agent` only at a terminal condition, explicit user halt,
stale long-idle team, or when replacement is clearly better.


