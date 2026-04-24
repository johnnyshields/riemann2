---
name: research-resume
description: Resume or recover an existing research team dir in place after a crash or interruption. Reuses the existing team dir, mines prior deposits, and spawns new Codex subagents into new agents/<ts>-<slug>/ subdirs without creating a new team dir.
---

## Codex workflow

Follow `AGENTS.md` for coordinator policy, provenance, dispatch, and git rules. Work locally unless the user requested a delegated/team workflow or invoked a multi-agent skill. For delegated work, use Codex subagents (`spawn_agent`, `send_input`, `wait_agent`, `close_agent`) with concrete ownership, bounded prompts, and on-disk report/deposit requirements. Use the inherited Codex model by default; override only when the user asks or the task clearly requires it. Keep canonical paper edits coordinator-owned unless this skill explicitly grants an edit-capable phase.

# Research Resume

Recover an existing team attack in place. Use this when the user gives an
existing `<paper>/teams/<ts>-<slug>/` path and asks to continue, resume, recover,
or take over. Do **not** create a new team dir. Spawn only new agent subdirs
inside the existing team dir. Use the inherited Codex model by default.

`$ARGUMENTS`: existing team dir path; optional extra context paths; optional
focus text such as `UV-NNN`, `rem:wip-*`, or a route name.

## Recovery preflight

1. Resolve the existing team dir and confirm it contains `findings.md`, `uv.md`,
   `dispatch.md` or `collation.md`, and `agents/`. If a file is missing,
   reconstruct only the minimum stub inside the same team dir and record the
   recovery action in `collation.md`.
2. Record the originating commit and current commit in `collation.md` under a
   `## Resume checkpoint <timestamp>` heading. Do not create a new team dir.
3. Mine the team dir thoroughly before dispatch: read `findings.md`, `uv.md`,
   `attempts.md` if present, `dispatch.md`, `collation.md`, `paper-updates.md`
   if present, and every `agents/*/report.md`, `agents/*/notes/**`, and cited
   `agents/*/scripts/**` output.
4. Mine any extra context paths supplied by the user, especially prior adjacent
   team dirs. Pull forward only live next-actions, sharp obstructions, reusable
   negatives, and verified keep routes.
5. Update the existing team dir's `findings.md`, `uv.md`, `attempts.md`, and
   `collation.md` for missed captures before launching new agents. `attempts.md`
   stays markdown; initialize it with an attempts table and `Frontier summaries`
   block if absent.

## Resume plan

Write or append to `dispatch.md` a `## Resume dispatch <timestamp>` block with:

- current baseline/frontier;
- exact in-scope paper lines, team files, prior reports, notes, and scripts;
- protected surfaces;
- target UVs / labels / routes;
- non-goals;
- ground-truth checks and pinned objections;
- roster and why each role is needed.

Prefer a focused `research-attack`-sized roster unless the recovered state shows
multiple independent frontiers. A balanced recovery may use 3 gap-closers + 3
explorers + 2 verifiers. All agents receive the full `.agents/references/agents/_autoresearch.md`
metaprompt and the current `findings.md`; targeted agents receive only the
relevant UV entries per `Briefing rule`.

## Dispatch in place

When delegated teamwork is authorized, record team name `research-resume-<existing-ts-or-slug>-<resume-ts>` in `dispatch.md`.
Spawn new named Codex subagents with the inherited Codex model by default. Each agent's
work dir is a new subdir under the existing team dir:

`<existing-team-dir>/agents/<resume-ts>-<agent-slug>/`

Never reuse an old agent dir. Never write a new sibling team dir. Brief each
agent with its exact new deposit path and require the 9-field report plus
**Autoresearch next step**.

## Continuing cycle

As reports land, process them in the existing team dir:

1. Verify `report.md`, scripts, and notes exist under each new agent subdir.
2. Append one row to `attempts.md` per concrete route and refresh `Frontier summaries`.
3. Capture through `Claim lifecycle (git-as-archive)`: promote, demote,
   quarantine new UVs, append findings, reject scoped negatives, or mark no-action
   in `collation.md`.
4. Commit by logical unit and cite the existing team dir plus new agent subdir.
5. Keep the resumed agents alive for follow-up dialogue and redelegation.
   `close_agent` only at terminal condition, explicit user halt, stale long-idle
   team, or when a replacement team is clearly better.

## Crash recovery rule

If the system crashes again, the next coordinator reruns `research-resume` on the
same team dir, mines all reports and notes, captures anything stranded only in
agent subdirs, and continues from the latest `Resume checkpoint` without asking
whether to proceed.


