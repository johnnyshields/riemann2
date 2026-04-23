---
name: research-team
description: Primary workhorse. Dispatches a 3+3+2 roster (3 gap-closers + 3 explorers + 2 verifiers) via TeamCreate into one team dir with eight agent subdirs under <paper>/teams/. Use for a full balanced research cycle.
---

# Research Team (3+3+2)

Balanced research dispatch: 3 gap-closers + 3 explorers + 2 verifiers via
`TeamCreate`. One team dir with eight agent subdirs. Follows §5 briefing
rule, §4 writing discipline, §6 deposit structure, §8a forward-carry.

`$ARGUMENTS`: empty → general balance (coordinator picks most-blocking
UV items + three broad explorer topics); topic phrase → oriented around
it; UV-NNN → at least one gap-closer locked on it.

## Preamble (forward-carry first — §8a)

1. Read the most recent team dir's `findings.md`, `uv.md`, and current
   `rem:wip-*` labels, plus the last 2–3 lore entries.
2. Create the new team dir `<paper>/teams/<ts>-<team-slug>/`. Copy the
   prior team dir's `findings.md` and `uv.md` in; prune dead entries;
   add anything from the just-closed cycle not yet captured. Commit.
3. Pick the roster. Write `dispatch.md` with roster, targets, non-goals.

## Dispatch

`TeamCreate team_name: "research-team-<ts>"`. Spawn 8 named agents
(e.g. `gap-closer-mixed4pt`, `explorer-deriv-geo`, `verifier-source`).
Each agent's slug gets its own `agents/<ts>-<agent-slug>/` subdir.

Every briefing gets: the team dir's full `findings.md`, the 7-field
report schema (§7), non-goals, the agent's `agents/<slug>/` path + the
self-deposit checklist, and the §4 writing-discipline reminder
(three-bin proved/conditional/missing, gap reduction over closure,
scoped negation, caution-labeled synthesis, honest-verdict closure).
Role-specific idioms:

- **Gap-closers** — their specific UV entry verbatim from `uv.md`
  (narrow exception per §5); "What is the cleanest target here?"; "If
  full closure is too hard, reduce to the smallest list of concrete
  unresolved sub-statements"; routes A/B/C; fallback to minimal finite
  reduction.
- **Explorers** — no `uv.md` content (spoiler risk); mandate is
  observations + candidate goodies + candidate negative findings, each
  pre-tagged `[confirmed]` / `[conditional]` / `[candidate]`; "Label
  each claim with a confidence tag before merging."
- **Verifiers** — wait for the 6 research reports, then attack. The
  adversarial verifier may see specific UV entries cited in the
  reports; the source auditor may see UV entries whose labels appear in
  the audited sections. "Give me the honest verdict." "Qualify any
  impossibility claim with 'from [scope] alone.'"

Every agent is told: `unsupported` / `blocked` / `no progress` are
acceptable returns. Synthesize non-goals from context — an unscoped
agent drifts.

## Post-cycle (capture before shutdown — §8a)

1. Verify every `agents/<agent-slug>/report.md` + `scripts/` exists.
   Chase missing deposits via `SendMessage`; if unanswered, note in
   `collation.md` under "missing deposits". Do not shut down silently.
2. Walk each report. Process through §8 — promote, demote, file new
   UV-NNN in this team dir's `uv.md`, append findings bullets, reject
   with negative capture, or explicitly mark "no action" in
   `collation.md`. Commit per deposit where possible (§10).
3. Write `paper-updates.md` if the cycle produced paper-ready edits;
   otherwise skip.
4. One lore entry at `lore/<yyyymmdd>-research-team-<slug>.md`.
5. No direct `<main>.tex` edits here — promotion is a separate
   deliberate step after review.

Shut down agents, `TeamDelete`, final commit naming the team dir.
