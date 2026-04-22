# Research Audit

N disjoint read-only audits on specified paper subsections. Captures the
manual "parallel independent audit" pattern with a fixed grading framework
and explicit non-goals. See `CLAUDE.md` §5, §7, §8.

## Arguments

`$ARGUMENTS` formats:
- `<subsection-list>` e.g. `§12.3,§12.4,§12.5` or label/line ranges.
- `<subsection-list> --adversarial` to pair each auditor with an
  `adversary-<sub>` checker.
- `<subsection-list> --non-goals: "..."` to forbid specific moves
  (e.g., `"no new lemmas, audit only"`).

## Mandatory preamble

1. Read `paper/findings.md` and `paper/unverified.tex` in full.
2. For each subsection argument, resolve to a concrete line range (or
   `rem:wip-*` label or `\section{...}` block) in
   `paper/proof_of_rh.tex`. Record the ranges — they go into each
   teammate's briefing.
3. Create one task dir:
   `tasks/<ts>-audit-<slug>/` with `reports/`, `scripts/`, `notes/`.
   Announce it upfront.

## Spawn protocol

`TeamCreate team_name: "research-audit-<ts>"`, spawn one `auditor-<sub>`
per subsection, in parallel. With `--adversarial`, also spawn
`adversary-<sub>` pairing each.

Each auditor's briefing MUST include:
- Full `paper/findings.md`.
- The exact subsection text from `paper/proof_of_rh.tex` (read and paste
  or paste a path + line range).
- **UV entries only under `CLAUDE.md` §7 exceptions**: include a UV-NNN
  verbatim ONLY when the audited subsection contains its matching
  `rem:wip-*` label (source-auditor exception). Otherwise, do not share
  `unverified.tex` content — spoiler risk per §7.
- The **fixed grading framework** (per claim in the subsection):
  1. `proved as written`,
  2. `conditional but honestly stated`,
  3. `still a real gap`.
- The **7-field report schema** (`CLAUDE.md` §8).
- The **writing-discipline reminder** (`CLAUDE.md` §3a): state
  findings directly; no overclaim; no hedge; honest scope disclaimers
  welcome; three-bin separation mandatory.
- The **briefing idioms** (`CLAUDE.md` §7a):
  - "Separate three things: proved / conditional / missing."
  - "Give me the honest verdict" as the closing line of the report.
  - "`unsupported`, `blocked`, `no progress` are acceptable returns."
- The **self-deposit checklist**.
- Explicit non-goals from `$ARGUMENTS` (or the default: "audit only, do
  not propose new lemmas or restructure the subsection").

Adversary checkers read the corresponding auditor's report once landed
and return a 7-field report whose `Status` is `rejected` or `blocked` if
they can break the audit's verdicts, otherwise `verified`.

## Collation

1. Read every report from `tasks/<dir>/reports/*.md`.
2. Write a consolidated audit summary at
   `tasks/<dir>/reports/_summary.md` listing per-subsection verdicts.
3. If any finding surfaces that should be added to `paper/findings.md`
   (new Negative / Goodie / Open-gap), call `research-capture`.
4. Lore entry only if the audit materially changes proof state
   (otherwise, task dir alone is sufficient audit trail).
5. **No edits to `paper/proof_of_rh.tex`** from this skill.

## Shutdown

`SendMessage` each teammate `{type:"shutdown_request"}`, then
`TeamDelete`. Commit task dir contents + any `findings.md` edits.
Commit body names the task dir.
