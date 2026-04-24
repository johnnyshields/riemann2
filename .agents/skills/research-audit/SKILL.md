---
name: research-audit
description: N disjoint read-only audits on specified <paper>/<main>.tex subsections, each graded with the fixed proved/conditional/missing framework. Optional --adversarial pairs each auditor with a checker.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Research Audit

N disjoint read-only audits on subsections via
`Codex agent role: auditor`. Follows `.agents/references/agents/_autoresearch.md`, CLAUDE.md
`Dispatch` long-lived-agent rules, `Briefing rule`, `Team dirs and agent
self-deposit`, `Capture before shutdown, forward-carry at dispatch`. For Codex, use the inherited model by default; only override the model if the user explicitly asks or the task clearly requires it. Original Claude note: use the original Claude research model for every research auditor / checker, always.

`$ARGUMENTS`: `<subsection-list>` (e.g. `Section 12.3,`LaTeX conventions`.4,`LaTeX conventions`.5`, labels, or
line ranges); append `--adversarial` to pair each auditor with a
checker; `--non-goals: "..."` to pin specific bans.

## Preamble (forward-carry first â€” `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`.
2. Resolve each argument to a concrete line range (or `\section`
   block) in `<paper>/<main>.tex`.
3. Create `<paper>/teams/<ts>-audit-<slug>/`. Copy prior `findings.md`
   + `uv.md`; prune.

## Dispatch

`Codex subagent delegation when explicitly requested team_name: "research-audit-<ts>"`. Spawn one
`auditor-<sub>` (`Codex agent role: auditor`, the inherited Codex model by default) per subsection;
with `--adversarial`, also a paired `adversary-<sub>`
(`Codex agent role: verifier-adversarial`, the inherited Codex model by default) that reads the
auditor's report once landed.

Each auditor's briefing: current team dir's `findings.md`, the exact
subsection text, 9-field schema, writing-discipline reminder (three-
bin mandatory), self-deposit checklist, non-goals (user-supplied or
synthesized â€” at minimum "audit only, no new lemmas, no
restructuring").

Share a UV entry only when the audited range contains its matching
`rem:wip-*` label (narrow `Briefing rule` source-auditor exception). Otherwise no
`uv.md` content.

Fixed grading framework: each claim in the subsection is
`proved as written` / `conditional but honestly stated` / `still a
real gap`. Adversary checkers return `verified`, or
`rejected` / `blocked` with concrete breaks.

## Continuing cycle (capture, redelegate, keep alive â€” `Capture before shutdown, forward-carry at dispatch`)

Verify every expected `agents/<slug>/report.md` exists; chase missing
deposits. Write `collation.md` with per-subsection verdicts. Process
each auditor's findings through `Claim lifecycle (git-as-archive)` â€” append to this team dir's
`findings.md` (Negative / Goodie / Open-gap), file new UVs in
`uv.md`, or stage text-edits in `paper-updates.md`. Lore entry only
if proof state changed. No direct `<main>.tex` edits.

Keep auditors and paired adversaries alive for follow-up audits, source checks,
and adjacent ranges while their context is fresh. Use `send_input` to redelegate
instead of spawning replacements. Use `close_agent` only at a terminal condition,
explicit user halt, stale long-idle team, or when replacement is clearly better.


