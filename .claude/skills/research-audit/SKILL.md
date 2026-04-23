---
name: research-audit
description: N disjoint read-only audits on specified <paper>/<main>.tex subsections, each graded with the fixed proved/conditional/missing framework. Optional --adversarial pairs each auditor with a checker.
---

# Research Audit

N disjoint read-only audits on subsections.

`$ARGUMENTS`: `<subsection-list>` (e.g. `§12.3,§12.4,§12.5` or label /
line ranges); append `--adversarial` to pair each auditor with a
checker; `--non-goals: "..."` to pin specific bans.

## Preamble

Read `findings.md`. Resolve each argument to a concrete line range (or
`\section` block) in `proof_of_rh.tex`. Create
`<paper>/teams/<ts>-audit-<slug>/` with `reports/`, `scripts/`, `notes/`.

## Dispatch

`TeamCreate team_name: "research-audit-<ts>"`. Spawn one
`auditor-<sub>` per subsection; with `--adversarial`, also a paired
`adversary-<sub>` that reads the auditor's report once landed.

Each auditor's briefing: full `findings.md`, the exact subsection text,
the 7-field report schema, the writing-discipline reminder (three-bin
mandatory), the self-deposit checklist, and non-goals (user-supplied or
synthesized — at minimum "audit only, no new lemmas, no restructuring").

Share a UV entry only when the audited range contains its matching
`rem:wip-*` label (narrow source-auditor exception). Otherwise no
`unverified.tex` content.

Paste these idioms: "Separate three things: proved / conditional /
missing." "Give me the honest verdict" as the closing line. And
"`unsupported`/`blocked`/`no progress` are acceptable returns."

The fixed grading framework: each claim in the subsection is
`proved as written` / `conditional but honestly stated` / `still a real
gap`.

Adversary checkers return a 7-field report: `verified`, or
`rejected`/`blocked` with concrete breaks.

## Post-cycle

Verify every expected report exists; chase missing deposits. Write
`reports/_summary.md` with per-subsection verdicts. Call
`research-capture` for any surfaced Negative / Goodie / Open-gap. Lore
entry only if proof state changed. No `proof_of_rh.tex` edits.

Shut down, `TeamDelete`, commit with the team dir named.
