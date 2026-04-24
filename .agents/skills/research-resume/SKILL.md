---
name: research-resume
description: Continue a full research-team cycle from an existing <paper>/teams/<ts>-<slug>/ directory. Same 3+3+2 workflow as research-team; the only difference is that it reuses the existing team dir and creates only new agent subdirs.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Resume (3+3+2 In Place)

Resume is `research-team` run in an existing team dir. Same roster, briefing,
capture, long-lived-agent behavior, autoresearch loop, and promotion discipline.
The only difference: do not create a sibling team dir. Reuse the supplied team
dir and create fresh `agents/<resume-ts>-<agent-slug>/` subdirs.

`$ARGUMENTS`: existing `<paper>/teams/<ts>-<slug>/` path; optional focus text
such as `UV-NNN`, `rem:wip-*`, or a route name. If no focus is given, choose the
most blocking frontier from the existing dir without asking for approval.

## Preamble (resume in place first)

1. Resolve the existing team dir. It must be the working team snapshot for this
   cycle. Do not create a new team dir.
2. Read `findings.md`, `uv.md`, `attempts.md` if present, `dispatch.md`,
   `collation.md`, `paper-updates.md` if present, current `rem:wip-*` labels,
   and the last 2-3 relevant lore entries.
3. Walk every `agents/*/report.md`, plus cited `notes/` and `scripts/`, before
   dispatch. Anything useful stranded only in an agent report is a capture miss:
   update `findings.md`, `uv.md`, `attempts.md`, or `collation.md` first.
4. Initialize missing stubs only inside the existing team dir. `attempts.md`
   gets the standard attempts table and `Frontier summaries` block if absent.
5. Append `## Resume dispatch <timestamp>` to `dispatch.md` with the current
   commit, roster, targets, exact in-scope files/lines/reports, protected
   surfaces, non-goals, fixed-harness criteria, ground-truth checks, and any run
   budgets/timeouts. Commit the resume checkpoint by named paths.

## Dispatch

When delegated teamwork is authorized, record team name
`research-resume-<existing-ts-or-slug>-<resume-ts>` in `dispatch.md`. Spawn the
same balanced roster as `research-team`: 3 gap-closers, 3 explorers, and 2
verifiers. Use the inherited Codex model by default. Each fresh teammate gets a
new work dir:

`<existing-team-dir>/agents/<resume-ts>-<agent-slug>/`

Never reuse an old agent dir. Keep all existing team files authoritative.

Every briefing gets the full `.agents/references/agents/_autoresearch.md`
metaprompt, the team dir's full `findings.md`, the 9-field report schema
(`Report schema`), non-goals, the agent's exact deposit path, self-deposit
checklist, and the `Writing discipline` reminder.

Role-specific idioms match `research-team`:

- **Gap-closers** receive their specific UV entry verbatim from `uv.md`, routes
  A/B/C, "What is the cleanest target here?", and fallback to minimal finite
  reduction.
- **Explorers** receive no `uv.md` content by default; they return observations
  and candidate findings tagged `[confirmed]`, `[conditional]`, or `[candidate]`.
- **Verifiers** wait for the research reports, then attack; adversarial/source
  exceptions receive only the specific UV entries they need.

Do not ask for approval. Pick the roster and targets from the recovered
frontier, then proceed.

## Continuing Cycle

Same as `research-team`, but all capture stays in the existing team dir.

1. Verify every returning agent deposited `report.md` plus cited `scripts/` and
   `notes/`. Chase missing deposits via `send_input`; record unanswered gaps in
   `collation.md`.
2. Walk each report. Process through `Claim lifecycle (git-as-archive)`:
   promote, demote, file new UV-NNNs in this team dir's `uv.md`, append findings
   bullets, reject with negative capture, or mark "no action" in `collation.md`.
3. Append an `attempts.md` row for every substantial route with `keep`,
   `discard`, or `crash`; refresh `Frontier summaries` periodically.
4. Respond to each agent with a concrete follow-up, adversarial challenge, or
   next adjacent task. Use `send_input`, not a fresh `spawn_agent`, when that
   teammate's context is useful.
5. Write `paper-updates.md` only for paper-ready edits. No direct `<main>.tex`
   edits here.
6. Commit logical units by named paths, citing the existing team dir and new
   agent subdir when applicable.

Do not shut down agents at ordinary cycle boundaries. Keep the resumed team
alive for continuity. Use `close_agent` only at a terminal condition, explicit
user halt, stale long-idle team, or when replacement is clearly better.
