---
name: research-resume
description: Resume or recover an existing research team dir in place after a crash or interruption. Reuses the existing team dir, mines prior deposits, and spawns new the original Claude research model agents into new agents/<ts>-<slug>/ subdirs without creating a new team dir.
---

## Codex adaptation

This skill was adapted from the workspace Claude skill of the same name and should now be used as a Codex skill. Use it as procedural guidance inside Codex.

- Prefer doing coordinator work directly in this thread: read files, edit with `apply_patch`, run focused checks, and summarize outcomes.
- When the original skill calls for Claude-only mechanisms such as `TeamCreate`, `SendMessage`, `TeamDelete`, `subagent_type`, or `model: the original Claude research model`, translate that into Codex behavior. Spawn Codex subagents only when the user explicitly asks for delegation, parallel agents, or team-style work; otherwise run the workflow locally.
- For any spawned Codex worker/explorer, give a concrete, bounded task, an owned work area, the relevant files to read, and the same report/deposit expectations the skill describes.
- Preserve repository policy from `CLAUDE.md` where it describes paper state, team directories, UV ledgers, findings, writing discipline, and provenance. Treat Claude-specific tool names as historical wording, not callable tools.
- Keep canonical paper edits coordinator-owned unless this skill explicitly authorizes an edit-capable phase.

# Research Resume

Recover an existing team attack in place. Use this when the user gives an
existing `<paper>/teams/<ts>-<slug>/` path and asks to continue, resume, recover,
or take over. Do **not** create a new team dir. Spawn only new agent subdirs
inside the existing team dir. For Codex, use the inherited model by default; only override the model if the user explicitly asks or the task clearly requires it. Original Claude note: use the original Claude research model for every research agent,
always. Do not override Codex model selection unless explicitly needed.

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
explorers + 2 verifiers. All agents receive the full `.codex/references/agents/_autoresearch.md`
metaprompt and the current `findings.md`; targeted agents receive only the
relevant UV entries per `Briefing rule`.

## Dispatch in place

`Codex subagent delegation when explicitly requested team_name: "research-resume-<existing-ts-or-slug>-<resume-ts>"`.
Spawn new named agents with the inherited Codex model by default on every `Agent` call. Each agent's
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


