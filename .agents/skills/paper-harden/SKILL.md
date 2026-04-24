---
name: paper-harden
description: Read-only 4-agent quality review of <paper>/<main>.tex â€” rigor, consistency, formatting, voice. Reviewers return reports only; the coordinator consolidates.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Paper Harden

Four-angle read-only quality review via `Codex agent role: harden-reviewer`.
Follows `.agents/references/agents/_autoresearch.md`, CLAUDE.md `Dispatch`
long-lived-agent rules, `Briefing rule`, `Team dirs and agent self-deposit`,
`Capture before shutdown, forward-carry at dispatch`. Use the inherited Codex model by default for
every reviewer, always.

## Preamble (forward-carry first â€” `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`
   (especially Negative + Open-gaps, for overclaim detection).
2. Create `<paper>/teams/<ts>-harden-<slug>/`. `<slug>` may be
   `post-referee`, `pre-submission`, or generic. Copy forward
   `findings.md` + `uv.md`; prune.
3. Write `dispatch.md` describing scope and non-goals.

## Dispatch

`Codex subagent delegation when explicitly requested team_name: "paper-harden-<ts>"`. Spawn four reviewers
(`Codex agent role: harden-reviewer`, the inherited Codex model by default) with the standard briefing,
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


