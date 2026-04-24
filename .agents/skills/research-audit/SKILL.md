---
name: research-audit
description: N disjoint read-only audits on specified <paper>/<main>.tex subsections, each graded with the fixed proved/conditional/missing framework. Optional --adversarial pairs each auditor with a checker.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Audit

N disjoint read-only audits on subsections via
`role prompt: auditor`. Follows `.agents/references/agents/_autoresearch.md`, AGENTS.md
`Dispatch` long-lived-agent rules, `Briefing rule`, `Team dirs and agent
self-deposit`, and `Capture before shutdown, forward-carry at dispatch`. Use the inherited Codex model by default.

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

When delegated teamwork is authorized, record team name `research-audit-<ts>` in `dispatch.md`. Spawn one
`auditor-<sub>` (`role prompt: auditor`, inherited Codex model) per subsection;
with `--adversarial`, also a paired `adversary-<sub>`
(`role prompt: verifier-adversarial`, inherited Codex model) that reads the
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


