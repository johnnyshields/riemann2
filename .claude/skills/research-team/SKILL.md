---
name: research-team
description: Primary workhorse. Dispatches a 3+3+2 roster (3 gap-closers + 3 explorers + 2 verifiers) via TeamCreate into three sibling task dirs under tasks/. Use for a full balanced research cycle on the RH project.
---

# Research Team (3+3+2)

Balanced research dispatch: 3 gap-closers + 3 explorers + 2 verifiers via
`TeamCreate`. Follows the project's briefing rule and writing discipline.

`$ARGUMENTS`: empty → general balance (coordinator picks most-blocking UV
items + three broad explorer topics); topic phrase → oriented around it;
UV-NNN → at least one gap-closer locked on it.

## Preamble

Read `findings.md`, `unverified.tex`, current `rem:wip-*` labels, and the
last 2–3 lore entries. Pick roster. Create three sibling dirs sharing
one `yyyymmdd-hhmmss` prefix: `tasks/<ts>-attack-gap-<slug>/`,
`-attack-fund-<slug>/`, `-verify-<slug>/`, each with `reports/`,
`scripts/`, `notes/`. Announce paths.

## Dispatch

`TeamCreate team_name: "research-team-<ts>"`. Spawn 8 named teammates
(e.g. `gap-closer-mixed4pt`, `explorer-deriv-geo`, `verifier-source`).
Every briefing gets: full `findings.md`, the 7-field report schema,
non-goals, the task-dir path + self-deposit checklist, the writing-
discipline reminder (three-bin proved/conditional/missing, gap reduction
over closure, scoped negation, caution-labeled synthesis,
honest-verdict closure), and role-specific idioms:

- **Gap-closers** — their specific UV entry verbatim (narrow exception
  to the no-`unverified.tex`-sharing rule); "What is the cleanest target
  here?"; "If full closure is too hard, reduce to the smallest list of
  concrete unresolved sub-statements"; routes A/B/C; fallback to minimal
  finite reduction.
- **Explorers** — no `unverified.tex` content (spoiler risk); mandate is
  observations + candidate goodies + candidate negative findings,
  each pre-tagged `[confirmed]`/`[conditional]`/`[candidate]`; "Label
  each claim with a confidence tag before merging."
- **Verifiers** — wait for the 6 research reports, then attack. The
  adversarial verifier may see specific UV entries cited in the reports;
  the source auditor may see UV entries whose labels appear in the
  audited sections. "Give me the honest verdict." "Qualify any
  impossibility claim with 'from [scope] alone.'"

Every teammate is also told: `unsupported` / `blocked` / `no progress`
are acceptable returns. Synthesize non-goals from context (adjacent UV
entries, in-flight work, deferred topics). Never dispatch without
non-goals — an unscoped teammate drifts.

## Post-cycle

Before anything: verify every `reports/<teammate>.md` exists across the
three dirs. Chase missing deposits via `SendMessage`; if unanswered, note
at `notes/_missing-deposit.md`. Do not commit with silent misses.

Then: cross-check handbacks against cited paper lines, emit
`findings.md` deltas via `research-capture`, refine `unverified.tex`
(add new UV entries where surfaced), write one lore entry
`lore/<yyyymmdd>-research-team-<slug>.md`. No `proof_of_rh.tex` edits —
promotion is a separate deliberate step after review.

Shut down teammates, `TeamDelete`, commit with all three task dirs named
in the body.
