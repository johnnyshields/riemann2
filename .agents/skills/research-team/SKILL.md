---
name: research-team
description: Primary workhorse. Dispatches a 3+3+2 roster (3 gap-closers + 3 explorers + 2 verifiers) via Codex subagents when delegated teamwork is authorized, with one team dir and eight agent subdirs under <paper>/teams/. Use for a full balanced research cycle.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Team (3+3+2)

Balanced research dispatch: 3 gap-closers + 3 explorers + 2 verifiers via
Codex subagents when delegated teamwork is authorized. One long-lived team dir with eight agent subdirs. Follows `Dispatch`
long-lived-agent rules, `.agents/references/agents/_autoresearch.md`, `Briefing rule`,
`Writing discipline`, `Team dirs and agent self-deposit` deposit structure, and `Capture before shutdown, forward-carry at dispatch`.

`$ARGUMENTS`: empty â†’ general balance (coordinator picks most-blocking
UV items + three broad explorer topics); topic phrase â†’ oriented around
it; UV-NNN â†’ at least one gap-closer locked on it.

## Preamble (forward-carry first â€” `Capture before shutdown, forward-carry at dispatch`)

1. Read the most recent team dir's `findings.md`, `uv.md`, and current
   `rem:wip-*` labels, plus the last 2â€“3 lore entries.
2. Create the new team dir `<paper>/teams/<ts>-<team-slug>/`. Copy the
   prior team dir's `findings.md`, `uv.md`, and open `attempts.md` context in;
   prune dead entries; add anything from the just-closed cycle not yet
   captured. Initialize `attempts.md` with a markdown attempts table and
   `Frontier summaries` block. Commit.
3. Confirm no existing team dir has the same timestamp/slug. Pick the roster.
   Write `dispatch.md` with the originating commit, roster, targets, exact
   in-scope files/lines/reports, protected surfaces, non-goals, fixed-harness
   criteria, ground-truth checks, and any run budgets/timeouts.

## Dispatch

When delegated teamwork is authorized, record team name `research-team-<ts>` in `dispatch.md`. Spawn 8 named Codex subagents
(e.g. `gap-closer-mixed4pt`, `explorer-deriv-geo`, `verifier-source`), and
use the inherited Codex model by default. Each agent's slug gets its own
`agents/<ts>-<agent-slug>/` subdir.

Keep those teammates alive after their first deposit. Treat idle notifications
as availability for the next assignment, not as completion. When a follow-up or
adjacent task depends on an agent's context, send it to the same named teammate
with `send_input` instead of spawning a fresh agent. Use new agents only for a
new role, an independence check, a blocked teammate, or a stale long-idle team.
The team lead should keep a running dialogue: clarify weak points, ask for
sharper reductions, redirect routes, and redelegate the next task before any
shutdown.

Every briefing gets: the full `.agents/references/agents/_autoresearch.md` metaprompt,
the team dir's full `findings.md`, the 9-field report schema (`Report schema`), non-goals,
the agent's `agents/<slug>/` path + the self-deposit checklist, and the `Writing discipline`
writing-discipline reminder (three-bin proved/conditional/missing, gap
reduction over closure, scoped negation, caution-labeled synthesis,
honest-verdict closure).
Role-specific idioms:

- **Gap-closers** â€” their specific UV entry verbatim from `uv.md`
  (narrow exception per `Briefing rule`); "What is the cleanest target here?"; "If
  full closure is too hard, reduce to the smallest list of concrete
  unresolved sub-statements"; routes A/B/C; fallback to minimal finite
  reduction.
- **Explorers** â€” no `uv.md` content (spoiler risk); mandate is
  observations + candidate goodies + candidate negative findings, each
  pre-tagged `[confirmed]` / `[conditional]` / `[candidate]`; "Label
  each claim with a confidence tag before merging."
- **Verifiers** â€” wait for the 6 research reports, then attack. The
  adversarial verifier may see specific UV entries cited in the
  reports; the source auditor may see UV entries whose labels appear in
  the audited sections. "Give me the honest verdict." "Qualify any
  impossibility claim with 'from [scope] alone.'"

Every agent is told: `unsupported` / `blocked` / `no progress` are
acceptable returns. Synthesize non-goals from context â€” an unscoped
agent drifts.

## Continuing cycle (capture, redelegate, keep alive â€” `Capture before shutdown, forward-carry at dispatch`)

1. Verify each returning agent's `agents/<agent-slug>/report.md` +
   `scripts/` exists. Chase missing deposits via `send_input`; if
   unanswered, note in `collation.md` under "missing deposits". Do not
   shut down silently.
2. Walk each report. Process through `Claim lifecycle (git-as-archive)` â€” promote, demote, file new
   UV-NNN in this team dir's `uv.md`, append findings bullets, reject
   with negative capture, or explicitly mark "no action" in
   `collation.md`. Append an `attempts.md` row for every substantial route
   with `keep`, `discard`, or `crash`; periodically summarize counts and the
   current frontier in `collation.md`. Commit per deposit where possible
   (`Git workflow`).
3. Respond to the agent. Ask one concrete follow-up, adversarial challenge,
   or clarification when the report has a live thread; otherwise assign the
   next adjacent task to the same named teammate. Use `send_input`, not a new
   `spawn_agent`, when the existing teammate's context is useful.
4. Write `paper-updates.md` if the cycle produced paper-ready edits;
   otherwise skip.
5. One lore entry at `lore/<yyyymmdd>-research-team-<slug>.md` for major
   shifts in direction or team-level decisions.
6. No direct `<main>.tex` edits here â€” promotion is a separate deliberate
   step after review.

Do not shut down agents at ordinary cycle boundaries. Keep the delegated Codex
team alive for a good while so the lead and teammates maintain continuity.
Only use `close_agent` at a terminal condition, explicit user halt, stale
long-idle team, or when a replacement team is clearly better than continued
redelegation.


