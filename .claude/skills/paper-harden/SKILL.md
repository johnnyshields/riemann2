---
name: paper-harden
description: Read-only 4-agent quality review of <paper>/<main>.tex — rigor, consistency, formatting, voice. Reviewers return reports only; the coordinator consolidates.
---

# Paper Harden

Four-angle read-only quality review via `subagent_type: harden-reviewer`.
Follows `.claude/agents/_autoresearch.md`, CLAUDE.md `Dispatch`
long-lived-agent rules, `Briefing rule`, `Team dirs and agent self-deposit`,
`Capture before shutdown, forward-carry at dispatch`. Use `model: "opus"` for
every reviewer unless the user explicitly overrides this dispatch.

## Preamble (forward-carry first — `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`
   (especially Negative + Open-gaps, for overclaim detection).
2. Create `<paper>/teams/<ts>-harden-<slug>/`. `<slug>` may be
   `post-referee`, `pre-submission`, or generic. Copy forward
   `findings.md` + `uv.md`; prune.
3. Write `dispatch.md` describing scope and non-goals.

## Dispatch

`TeamCreate team_name: "paper-harden-<ts>"`. Spawn four reviewers
(`subagent_type: harden-reviewer`, `model: "opus"`) with the standard briefing,
the full `.claude/agents/_autoresearch.md` metaprompt, and non-goal "report only,
do not edit the paper." Only `reviewer-rigor` additionally receives the current
`uv.md` (for overclaim detection — narrow `Briefing rule` exception); the others
do not.

- **`reviewer-rigor`** — every claim justified, every hypothesis
  present, theorem-vs-proof match, no handwaving. Cross-checks
  `findings.md` Negative for silently-retried dead ends and `uv.md`
  for claims that should be quarantined but aren't.
- **`reviewer-consistency`** — notation consistency, stale renames,
  label/ref integrity, abstract/intro/conclusion counts match,
  frozen-macro compliance.
- **`reviewer-formatting`** — compile warnings, undefined refs,
  multiply-defined labels, substantive overfull/underfull boxes,
  `\texorpdfstring` on math-in-titles, bibliography consistency.
- **`reviewer-voice`** — AI tells, templated-remark patterns, voice
  switches within paragraphs, marketing language, overclaim. Rank
  HIGH / MEDIUM / LOW.

## Continuing cycle (capture, redelegate, keep alive — `Capture before shutdown, forward-carry at dispatch`)

Verify deposits. Walk each report, process findings through `Claim lifecycle (git-as-archive)` —
append bullets to this team dir's `findings.md`, file new UVs in
`uv.md`, or stage text-edit suggestions in `paper-updates.md`. Write
`collation.md` summary ranked HIGH / MEDIUM / LOW. No direct paper
edits here.

Keep reviewers alive for follow-up passes and adjacent scopes while their context
is fresh. Use `SendMessage` to push back, ask for narrowed findings, or assign the
next review. Use `TeamDelete` only at a terminal condition, explicit user halt,
stale long-idle team, or when replacement is clearly better.
