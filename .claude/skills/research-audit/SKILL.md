---
name: research-audit
description: N disjoint read-only audits on specified <paper>/<main>.tex subsections, each graded with the fixed proved/conditional/missing framework. Optional --adversarial pairs each auditor with a checker.
---

# Research Audit

N disjoint read-only audits on subsections via
`subagent_type: auditor`. Follows CLAUDE.md `Briefing rule`, `Team dirs and agent self-deposit`, `Capture before shutdown, forward-carry at dispatch`.

`$ARGUMENTS`: `<subsection-list>` (e.g. `Section 12.3,`LaTeX conventions`.4,`LaTeX conventions`.5`, labels, or
line ranges); append `--adversarial` to pair each auditor with a
checker; `--non-goals: "..."` to pin specific bans.

## Preamble (forward-carry first — `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md` and `uv.md`.
2. Resolve each argument to a concrete line range (or `\section`
   block) in `<paper>/<main>.tex`.
3. Create `<paper>/teams/<ts>-audit-<slug>/`. Copy prior `findings.md`
   + `uv.md`; prune.

## Dispatch

`TeamCreate team_name: "research-audit-<ts>"`. Spawn one
`auditor-<sub>` (`subagent_type: auditor`) per subsection; with
`--adversarial`, also a paired `adversary-<sub>`
(`subagent_type: verifier-adversarial`) that reads the auditor's
report once landed.

Each auditor's briefing: current team dir's `findings.md`, the exact
subsection text, 7-field schema, writing-discipline reminder (three-
bin mandatory), self-deposit checklist, non-goals (user-supplied or
synthesized — at minimum "audit only, no new lemmas, no
restructuring").

Share a UV entry only when the audited range contains its matching
`rem:wip-*` label (narrow `Briefing rule` source-auditor exception). Otherwise no
`uv.md` content.

Fixed grading framework: each claim in the subsection is
`proved as written` / `conditional but honestly stated` / `still a
real gap`. Adversary checkers return `verified`, or
`rejected` / `blocked` with concrete breaks.

## Post-cycle (capture before shutdown — `Capture before shutdown, forward-carry at dispatch`)

Verify every expected `agents/<slug>/report.md` exists; chase missing
deposits. Write `collation.md` with per-subsection verdicts. Process
each auditor's findings through `Claim lifecycle (git-as-archive)` — append to this team dir's
`findings.md` (Negative / Goodie / Open-gap), file new UVs in
`uv.md`, or stage text-edits in `paper-updates.md`. Lore entry only
if proof state changed. No direct `<main>.tex` edits.

Shut down, `TeamDelete`, commit with the team dir named.
