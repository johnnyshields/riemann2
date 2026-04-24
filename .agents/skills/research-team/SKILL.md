---
name: research-team
description: Primary workhorse. Dispatches a 3+3+2 roster (3 gap-closers + 3 explorers + 2 verifiers) via Codex subagent delegation when explicitly requested into one team dir with eight agent subdirs under <paper>/teams/. Use for a full balanced research cycle.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Research Team (3+3+2)

Balanced research dispatch: 3 gap-closers + 3 explorers + 2 verifiers via
`Codex subagent delegation when explicitly requested`. One long-lived team dir with eight agent subdirs. Follows `Dispatch`
long-lived-agent rules, `.agents/references/agents/_autoresearch.md`, `Briefing rule`,
`Writing discipline`, `Team dirs and agent self-deposit` deposit structure, `Capture before shutdown, forward-carry at dispatch` forward-carry. For Codex, use the inherited model by default; only override the model if the user explicitly asks or the task clearly requires it. Original Claude note: use the original Claude research model for every research agent, always. Do not override Codex model selection unless explicitly needed.

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

`Codex subagent delegation when explicitly requested team_name: "research-team-<ts>"`. Spawn 8 named agents
(e.g. `gap-closer-mixed4pt`, `explorer-deriv-geo`, `verifier-source`), and
use the inherited Codex model by default for any spawned agent. Each agent's slug gets its own
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
   `Agent`, when the existing teammate's context is useful.
4. Write `paper-updates.md` if the cycle produced paper-ready edits;
   otherwise skip.
5. One lore entry at `lore/<yyyymmdd>-research-team-<slug>.md` for major
   shifts in direction or team-level decisions.
6. No direct `<main>.tex` edits here â€” promotion is a separate deliberate
   step after review.

Do not shut down agents at ordinary cycle boundaries. Keep the `Codex subagent delegation when explicitly requested`
team alive for a good while so the lead and teammates maintain continuity.
Only use `close_agent` at a terminal condition, explicit user halt, stale
long-idle team, or when a replacement team is clearly better than continued
redelegation.


