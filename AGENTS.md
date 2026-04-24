# Coordinator Policy

Main chat is the coordinator / team lead. Delegates research, exploration, and
verification; collates; edits canonical files. Delegates are expected to create
their own provenance artifacts (see below) but are read-only by default with respect
to files they do not own (unless otherwise specified). Every agent is briefed with
this file.

## Files

| Path | Role |
|---|---|
| `<paper>/<main>.tex` | Canonical draft (e.g. `proof_of_rh.tex`). Coordinator-only edits. |
| `<paper>/teams/YYYYMMDD-HHMMSS-<team-slug>/` | Per-dispatch team dir. `<paper>` \(\in\) `paper \| grh \| quantum \| ...`. `<team-slug>` typically encodes intent (`attack-gap-uv017-mixed4pt`, `audit-sec3`, `verify-tau`). |
| `<paper>/teams/.../findings.md` | In-cycle knowledge base (Structural / Negative / Goodies / Open-gaps). \(\le 200\) lines. Pasted in full into every delegation in that cycle. |
| `<paper>/teams/.../uv.md` | In-cycle UV ledger (markdown). UV-NNN entries ("UV" = "unverified") linked to `rem:wip-*` labels in the paper. UV-NNN is globally unique across cycles. |
| `<paper>/teams/.../attempts.md` | Mechanical route ledger. One row per substantial route with `keep` / `discard` / `blocked` / `terminal` / `crash`, evidence, action, and one-line reason. |
| `<paper>/teams/.../paper-updates.md` | Team-lead-authored staged edits for `<paper>/<main>.tex`. Created when the team has paper-ready changes; applied by the coordinator then deleted or archived. |
| `<paper>/teams/.../agents/YYYYMMDD-HHMMSS-<agent-slug>/` | Per-agent work dir — nested inside the team dir. Each agent writes its own report, scripts, and notes here. |
| `lore/` | Workflow plans, syntheses, decisions. Permanent. |
| `<paper>/chats/` | Historical ChatGPT/Codex exports. Read-only. |
| `scripts/` + `scripts/wip/` | Computation. `final-scripts/<paper>/` for hardened ones. |

**Authoritative state lives in the most recent team dir.** There is no
top-level `<paper>/findings.md` or `<paper>/unverified.tex`; those were
migrated into per-cycle files under `teams/`. Cross-cycle persistence is
achieved by *forward-carry*: `Capture before shutdown, forward-carry at dispatch` describes the mechanic.

Optional grep indexes (`findings-in-paper.md`, `unverified-rejected.md`) are
lazy-created on first use. Not authoritative — git log is.

Canonical paper paths live at `C:\workspace\riemann2\<paper>\<main>.tex`
(WSL `/mnt/c/workspace/riemann2/<paper>/<main>.tex`). Each paper is a
monolithic `amsart` with a frozen macro namespace.

## State ledger separation

Keep team-dir state files non-overlapping:

- `uv.md` is the live proof-obligation ledger: precise missing
  sub-statements, open `rem:wip-*` obligations, dependencies, and promotion
  conditions. It is not route history.
- `findings.md` is the briefable knowledge base: durable Structural /
  Negative / Goodie / Open-gap bullets that future agents should see. It is
  not a per-attempt log and stays at briefing size.
- `attempts.md` is the mechanical route ledger for the current cycle. It
  records what was tried, by whom, against which target, with status,
  evidence, action, and the one-line reason. It prevents blind retries; it is
  not authoritative proof state and is not pasted wholesale into briefings.
- `collation.md` is the team-lead narrative: synthesis, no-action rationales,
  rolling verifier queue, one-ahead research lane, and decisions as reports
  land. It may summarize `attempts.md`, but does not replace `uv.md` or
  `findings.md`.
- `paper-updates.md` is staged paper text only.

Classify every material signal from an agent report into the narrowest live
surface: missing proof obligation -> `uv.md`; reusable lesson -> `findings.md`;
route outcome -> `attempts.md`; synthesis or no-action rationale ->
`collation.md`; paper-ready edit -> `paper-updates.md`. If one report produces
several signals, file each one in the right place with the same provenance.
Legacy `attempts.tsv` is read-only context when resuming old teams; new and
resumed work uses `attempts.md`.

Ledger invariants are hard gates:

- Every `attempts.md` row cites the producing agent report and records exactly
  one route outcome. If the same report produced a UV or finding, cite that id
  instead of restating the claim.
- Every live `uv.md` entry is a precise missing sub-statement with source label
  or source report, needed-for-promotion condition, and provenance. Presence is
  the status; do not add status tags.
- Every `findings.md` bullet is durable briefing material. Failed route logs,
  stale guesses, and per-agent summaries belong elsewhere.
- Every `collation.md` decision that chooses "no action" states why the signal
  was not filed to `uv.md`, `findings.md`, `attempts.md`, or `paper-updates.md`.
- No claim may be promoted, demoted, rejected, or forwarded into a new cycle
  while its ledger destination is ambiguous.

## Dispatch

Delegation uses Codex subagents. Use
`spawn_agent` for new teammates, `send_input` for follow-up, `wait_agent` only
when the coordinator is blocked on a result, and `close_agent` only at a real
terminal condition, explicit user halt, or stale long-idle team. Do not write
legacy team-tool names, raw-agent invocations, model-pin shims, or tmux-only
instructions into new briefs or skills.

Spawn Codex subagents only when the user explicitly asks for delegated,
parallel, or team-style work, or invokes a skill whose purpose is multi-agent
dispatch (`research-team`, `research-attack`, `research-audit`, `trifecta`,
`paper-harden`, `paper-referee`, `paper-rewrite`, `script-promote`). Otherwise
the coordinator runs the workflow locally in the main chat: read state, edit
canonical files, run checks, and write the required provenance artifacts.

**Keep Codex teammates alive.** A research team is a live research group, not a
one-shot batch. After an agent deposits a report, keep the teammate around for
follow-up questions, adversarial back-and-forth, and the next adjacent task.
Prefer redelegating to the same named agent when the new task builds on its
context or expertise; spawn a replacement only when the role changes, the agent
is blocked, or fresh independence matters. Maintain a continuous dialogue with
active agents through `send_input`: clarify reports, push back on weak claims,
ask for sharper UV reductions, then assign the next task without tearing down
the team.

**Autoresearch everywhere.** Every research workflow and every research agent
runs under the shared metaprompt `.agents/references/agents/_autoresearch.md`, adapted from
Andrei Karpathy's autoresearch pattern. Include that metaprompt in research
briefs and agent definitions. Research agents keep looping: read state, choose
the next concrete move, work, deposit, state the next step, and wait for
redelegation. They do not ask whether to continue and they do not stop at
ordinary cycle boundaries.

**Model choice.** Use the inherited Codex model by default for research
delegation. Override the model only when the user explicitly asks or a bounded
task has a clear task-specific reason; record that reason in `dispatch.md`.
Do not hard-code vendor model names in skills, briefs, or agent definitions.

**Adaptive roster.** Research teams do not have a fixed headcount. The
coordinator chooses the smallest live roster that keeps the frontier moving:
gap-closers for concrete UVs, explorers for redirects, source auditors or
adversarial verifiers when there is something specific to check, and fresh
independent agents only when independence is useful. Balance is a judgment,
not a quota.

**One-ahead verification.** Keep at least one research or exploration lane
moving while verifiers review the previous stable deposit. Verification is
risk-based: exploratory notes, failed routes, and low-impact bookkeeping do
not need an immediate verifier. Claims that would change proof state, remove a
UV, alter the paper, or become a durable finding still require an adversarial
or source pass before promotion. Do not idle researchers behind verifier work
unless their next assignment depends on that verifier's answer.

### Dispatch selector

| Intent | Skill |
|---|---|
| general research cycle, no fixed target | `research-team` |
| focused push on one UV / label | `research-attack` |
| resume / recover existing team dir in place | `research-resume` |
| grade a subsection or three | `research-audit` |
| post-work synthesis, literature, hidden links | `trifecta` |
| systematic compactness rewrite | `paper-rewrite` |
| referee-issue fix loop | `paper-referee` |
| quality review (report-only) | `paper-harden` |
| UV ↔ `rem:wip-*` reconcile | `uv-sync` |
| dependency-graph validate | `dep-graph` |
| log one finding | `research-capture` |
| orient / resume | `cycle-status` |
| end-of-session writeup | `session-handoff` |
| back up transcript | `chat-backup` |
| weaken / reverse-promote | `paper-demote` |
| prune `findings.md` | `findings-prune` |
| move prose to `cut-for-time.md` | `paper-cut` |
| dedupe content | `paper-dedupe` |
| harden a script | `script-promote` |
| bibliography | `paper-biblio` |

When in doubt between `research-team` and `research-attack`, prefer
`research-attack` — cheaper to spin up and cheaper to get wrong.

## Coordinator autonomy

The coordinator decides roster sizes, UV targets, explorer topics, non-goals
(synthesized from adjacent in-flight work and recent lore), team-dir slugs,
commit messages, subsection selection, demote timing, forward-carry
filtering for findings.md / uv.md — without asking. Never interrupt over
research-direction minutia or approval checks.

## No approval prompts

Do not ask the user for approval before routine coordinator actions: choosing
the next target, dispatching or resuming agents, editing workflow files, staging
named paths, committing logical units, pushing, promoting, demoting, rejecting,
or filing UV entries. If a decision would be architectural or irreversible, do
the safest reversible action available: quarantine the claim, file a UV, record
the blocker in `collation.md` or `lore/`, and continue adjacent work. Stop only
for an explicit user halt, a hard runtime/tooling blocker, or a genuine terminal
condition.

## Auto-run — default for research work

Research work (gap-closing, exploration, verification, synthesis,
audit cycles) runs in a continuous auto-loop. The coordinator does not
ask "should I keep going?" or "is this a good stopping point?" between
cycles. The user is likely away and expects work to continue
indefinitely until a real terminal condition is hit or the user
manually interrupts.

**Loop:**

1. Read state — recent `lore/`, the most recent team dir's `findings.md`
   and `uv.md`, and that team dir's `agents/<slug>/report.md` files
   (walk *every* one, not just the collation), plus the last cycle's
   verdicts and commits. Any UV candidate, finding, or negative result
   still sitting only in an agent report is a capture miss — fix it
   (`Capture before shutdown, forward-carry at dispatch`) before dispatching the next cycle, because the next briefing
   reads the team-dir `findings.md` / `uv.md`, not 30 subdirs of
   deposits.
2. Pick the next move — a UV target, an explorer topic, a redirect, an
   audit, a synthesis. Default to `research-attack` over `research-team`
   per `Dispatch`.
3. Dispatch via the `Dispatch selector`. Brief per `Briefing rule`.
4. Collate returns as they land. Classify each material signal per `State
   ledger separation`, queue verification only for claims that need it, keep
   research agents one step ahead when their next move is independent, and
   promote / demote / quarantine / reject per `Claim lifecycle
   (git-as-archive)`. Commit by logical unit; auto-push per `Git workflow`.
5. Go to 1.

**Decide without asking:** which UV, which explorer topic, roster size,
team-dir slug, commit wording, whether to redirect, when to synthesize.
`Coordinator autonomy` covers this.

**Pause only for:** an explicit user halt, a hard blocker the coordinator
cannot work around, or a genuine terminal condition. Architectural or
irreversible choices become blockers to record, not approval prompts.

**Terminal conditions** (stop the loop): zero open UV entries and no
outstanding `rem:wip-*` labels; or the targeted synthesis fully closes
with `paper-harden` / `paper-referee` clean; or explicit user halt.
If context is compacted or a handoff occurs, immediately resume the
active agenda from the last recorded state — do not treat that as a
terminal condition.

**When stuck (out of obvious moves), think harder — do not stop.**
Re-read the current team's `findings.md` and recent `lore/` for a
missed angle. Combine
previous near-misses; two open UVs with related structure often admit a
hybrid attack. Try a more radical redirect — different function space,
different local model, structurally different route. Consult
`<paper>/chats/` for historical threads that were parked. Spin up
`trifecta` for fresh literature and cross-discipline pointers.
"No progress this cycle" is an acceptable report; "I ran out of ideas"
is not — the archive has the ideas.

(Loop pattern adapted from Karpathy's
[autoresearch/program.md](https://github.com/karpathy/autoresearch).)

## Writing discipline

Applies to the coordinator's paper edits and to every agent briefing. Not
a hardass — a good-referee standard.

- **State facts directly.** No AI tells ("it is worth noting," "interestingly,"
  "we leverage / utilize / employ," "to the best of our knowledge").
- **No overclaim.** Computational ≠ proved. "For tested configurations" ≠
  "for all." If a bound isn't effective, don't imply it.
- **Three-bin separation** on every audit / synthesis / status memo:
  `proved` / `conditional on [X]` / `missing`. Never blur.
- **Gap reduction over closure.** A gap is a precise missing sub-statement,
  not "further analysis needed." Vague gaps become UV entries.
- **Scoped negation.** "Ruled out" always carries a "from [scope] alone"
  qualifier.
- **Caution-labeled synthesis.** When merging sources, pre-tag each
  `[confirmed]` / `[conditional on X]` / `[candidate]`. Only `[confirmed]`
  reaches the paper.
- **Honest-verdict closure.** End audits with "Honest verdict:" + what is
  and isn't closed.
- **When in doubt, quarantine.** UV entry first, promote later.
- **Compute before asserting.** For any computational claim (bound, identity,
  inequality, convergence rate), a 10-line sympy/numpy/mpmath check beats
  prose. **Write the script to a file first, then run it** — amend and
  re-run as needed. Never pipe from stdin, pass an inline `-c` program, or
  heredoc a throwaway; there must be a cited file left behind. Deposit in
  the agent's `scripts/` dir and cite the path + relevant output in the
  report.
- **Simplicity criterion.** Between two routes with the same proof value,
  keep the one with fewer definitions, assumptions, dependencies, scripts,
  and paper edits. A tiny gain that adds awkward scaffolding is usually not
  worth promotion; an equal result with a cleaner proof is a keep.
- **Fixed-harness evaluation.** Judge each route against the same target,
  current paper state, `findings.md`, `uv.md`, and verification standard it
  was briefed with. Do not change the target mid-run to make a route look
  successful.

## Briefing rule

Every delegation includes: the full current `findings.md` from the team
dir (freshly updated per `Capture before shutdown, forward-carry at dispatch` — stale briefings are worse than late ones),
the `Report schema`, explicit non-goals, the agent's own `agents/<slug>/` path +
self-deposit checklist, and the `Writing discipline` reminder.

Every brief also names:

- the exact in-scope paper lines, team files, source files, and prior agent
  reports the agent must read before acting;
- the protected surfaces the agent must not edit (`<main>.tex`, `findings.md`,
  `uv.md`, `attempts.md`, `collation.md`, `dispatch.md`, `paper-updates.md`,
  `AGENTS.md`, `lore/`, and other agents' dirs unless an explicit role
  exception applies);
- the ground-truth check for the task: theorem statement, `rem:wip-*`, source
  reference, verifier question, pinned objection set, or script output that
  decides whether evidence counts.

**The full `uv.md` is NOT in the default briefing.** Sharing tentative
claims poisons independent agents. Exceptions — all narrow, all
*encouraged* where they apply — feed the relevant individual UV entries
(not the whole ledger) to:

- the gap-closer attacking that specific UV;
- the adversarial verifier reviewing exactly that claim;
- the source auditor whose range contains the matching `rem:wip-*`;
- the Phase-1 fixer whose issue touches it;
- any agent whose target is structurally adjacent enough that prior UV
  phrasing saves them from rediscovering the same gap.

An agent pushing on a UV should know exactly what's open on it: prior
attempted routes, the strongest objection from last cycle, the current
fallback. Paste the UV entry into the brief verbatim, plus a one-line
pointer to the agent reports that produced it.

**Ensure `findings.md` / `uv.md` are updated before launching the next
wave.** The team lead carries forward and revises these files at dispatch
time; `Capture before shutdown, forward-carry at dispatch` gives the mechanic. An out-of-date briefing is the handoff bug.

### Briefing idioms that license candor

Distilled from prior manual sessions; paste the relevant ones verbatim.

- "Separate three things: proved / conditional / missing."
- "What is the cleanest target here?"
- "Give me the honest verdict."
- "If full closure is too hard, reduce to the smallest list of concrete
  unresolved sub-statements."
- "Qualify any impossibility claim with 'from [scope] alone.'"
- "Label each claim with a confidence tag before merging."
- "`unsupported`, `blocked`, `no progress` are acceptable returns."

## Team dirs and agent self-deposit

Every multi-agent dispatch creates one team dir under the relevant paper:

```
<paper>/teams/YYYYMMDD-HHMMSS-<team-slug>/
├── findings.md                  — in-cycle knowledge base (`Capture before shutdown, forward-carry at dispatch` forward-carried + updated)
├── uv.md                        — in-cycle UV ledger, markdown (`Capture before shutdown, forward-carry at dispatch` forward-carried + updated)
├── paper-updates.md             — team-lead staged edits for <main>.tex (optional, created when ready)
├── dispatch.md                  — team-lead brief, roster, non-goals
├── attempts.md                  — route ledger: agent, target, route, status, evidence, action, reason
├── collation.md                 — team-lead synthesis as reports land
├── chat.md                      — transcript backup (chat-backup skill)
├── scripts/                     — team-lead scripts, if any
└── agents/
    ├── YYYYMMDD-HHMMSS-<agent-slug>/
    │   ├── report.md            — agent's 9-field report (`Report schema`)
    │   ├── scripts/             — every script the agent ran (written before run)
    │   └── notes/               — agent's scratch, intermediates worth keeping
    └── YYYYMMDD-HHMMSS-<other-agent-slug>/
        └── ...
```

`<paper>` is the canonical paper dir (`paper`, `grh`, `quantum`, ...). A
`research-team` cycle produces one team dir and however many agent subdirs the
coordinator selected or reused. Agent-subdir count records the live roster; it
is not a quota. Each agent gets its own timestamp in its slug so spawn order is
legible from the filesystem.

`findings.md` and `uv.md` in each team dir are the authoritative state
for that cycle. They start as forward-carries from the prior team dir
(`Capture before shutdown, forward-carry at dispatch`) and evolve as reports land. `attempts.md` is the run
ledger for the cycle. It contains a markdown attempts table plus a short
frontier summary. Do not duplicate `uv.md` entries or `findings.md` bullets
here; cite them by id or path and record the attempted route:

```
# Attempts

| Agent | Target | Route | Status | Evidence | Action | Reason |
|---|---|---|---|---|---|---|

## Frontier summaries

- **Current best:** <sharpest target / best evidence / strongest obstruction>
- **Verifier queue:** <stable deposits waiting on adversarial/source checks>
- **Research lane next:** <highest-leverage independent next move>
- **Discarded do-not-retry:** <scoped negatives that should not be repeated>
- **Blocked:** <coordinator actions or missing source checks>
```

Periodically summarize the frontier in `collation.md`: total attempts,
keep/discard/crash/blocked/terminal counts, current best kept routes, biggest
blockers, and next queued moves. `paper-updates.md` is optional: the team lead
writes it when the cycle has produced edits ready to fold into
`<paper>/<main>.tex`.

Route status meanings are fixed:

- `keep`: reusable proof step, reduction, computation, source check, or negative
  lesson worth carrying.
- `discard`: scoped route failure that should not be retried unchanged.
- `blocked`: coordinator action or missing source/check is required.
- `terminal`: the assigned target is closed, rejected, or superseded.
- `crash`: tooling or execution failure; distinguish from mathematical failure.

**Agents write their own provenance artifacts. Always.** Every agent — gap-closer,
explorer, verifier, auditor, Phase-1 fixer — writes directly to its own
`agents/<slug>/` dir: the 9-field report, every script it ran, every
scratch note worth keeping. The team lead briefs, collates, and commits;
the team lead does **not** transcribe an agent's findings into a fresh
file on the agent's behalf. If an agent returns only a chat message with
no on-disk deposit, the team lead sends it back with "deposit your report
and scripts under `agents/<your-slug>/`, then ping me" — paraphrased
provenance is laundered provenance.

Agents do **not** write outside their own `agents/<slug>/` dir, and in
particular do **not** touch `<main>.tex`, the team dir's `findings.md` /
`uv.md` / `attempts.md` / `collation.md` / `dispatch.md` /
`paper-updates.md`, `AGENTS.md`, `lore/`, or another agent's dir —
unless a skill grants an explicit exception (e.g. `paper-referee`
Phase 1). Those team-dir files belong to the team lead; agents suggest
changes and route outcomes in their reports.

## Report schema

Every agent report has nine fields:

- **Claim**
- **Status** \(\in\) `proved | computational | heuristic | open | rejected`
- **Evidence**
- **Baseline / delta** — current best route or obstruction, and whether this
  attempt improves, matches, weakens, rejects, or leaves it unchanged.
- **Attempt status** \(\in\) `keep | discard | blocked | terminal | crash`
- **Exact refs** — file paths, line numbers, `rem:wip-*`, chat paths, scripts
  + SHAs, UV-NNN
- **Dependencies**
- **Strongest objection** — never empty, never "none"
- **Needed for promotion**

`unsupported` / `blocked` / `no progress` are honest signals, not failures.

## Claim lifecycle (git-as-archive)

**Intake → quarantine → research → adversarial → promote | demote | reject.**

All operations are on the *current* team dir's `uv.md` and `findings.md`.
UV-NNN numbering is globally unique across team dirs — take `max(UV-NNN
across all `teams/*/uv.md`) + 1` when filing a new one.

- **Quarantine**: add UV-NNN to the current team dir's `uv.md`, or a
  bullet to the right section of its `findings.md`.
- **Advance / discard routes**: a route advances only if it sharpens a target,
  closes a substatement, produces a reusable negative, improves evidence, or
  reduces dependency depth. Otherwise mark it `discard` in `attempts.md`; do
  not let stale failed routes pollute `findings.md` or duplicate `uv.md`.
- **Adversarial pass is non-negotiable** before any proof-state change.
- **Promote**: edit paper (directly, or stage via `paper-updates.md`)
  AND remove the UV / findings entry from the team dir's `uv.md` /
  `findings.md` in the *same* commit. Subject: `promote UV-NNN:
  <one-line>`.
- **Demote**: edit paper + reinstate UV entry in the team dir's `uv.md`
  in the same commit. Subject: `demote <label>: <reason>`.
- **Reject**: delete UV entry from team dir's `uv.md`; commit body
  explains; if a reusable lesson surfaced, include `research-capture
  negative` in the same commit. Subject: `reject UV-NNN: <reason>`.

No status annotations in the live `uv.md` / `findings.md` — they stay
brief-size. Git log across team dirs is the audit trail.

**Broadcast corrections immediately.** If something already in the paper is
found false, `send_input` every active agent before doing anything else,
then demote + optional negative-capture in one commit. Cost of a delayed
correction >> cost of a brief interruption.

## Capture before shutdown, forward-carry at dispatch

The handoff bug is: an agent surfaces a UV candidate or finding, it
lands in `agents/<slug>/report.md`, and then it dies there — the next
cycle's briefing doesn't see it. Two mechanics prevent this.

**Capture before shutdown.** Before closing, replacing, or abandoning a team,
the team lead walks
*every* `agents/<slug>/report.md` in the cycle and processes each claim
through `Claim lifecycle (git-as-archive)` and `State ledger separation`:
promote, demote, file a new UV-NNN in the team dir's `uv.md`, add a reusable
bullet to `findings.md`, log the route in `attempts.md`, or explicitly note
"no action: reason X" in `collation.md`. Default is capture, not archive.
Material left only in an agent report is invisible to the next briefing.

Process reports as they land, not in an end-of-cycle batch. `Git workflow` already
asks for per-deposit commits; the capture edit (UV append, findings
bullet, demote) goes in the *same* commit as the report it came from
when the signal is clear enough.

Before each dispatch, resume, promotion, demotion, rejection, or shutdown, run a
ledger gate: every landed report has a corresponding route row or explicit
`collation.md` no-action note; every new UV/finding cites its source report;
every paper-ready edit is either in `paper-updates.md` or deliberately deferred.

**Be aggressive about UV creation.** A precise missing sub-statement is
a UV entry; a vague "needs more work" is not. When an agent report flags
something murky, the team lead extracts the sharpest possible sub-
statement and files it as UV-NNN rather than hoping the next cycle will
figure out what was meant. Over-quarantine is cheap; lost gaps are not.

**Forward-carry at dispatch.** Starting a new cycle, *before* briefing
agents:

1. Create the new team dir with its timestamp and slug.
2. Copy the most recent team dir's `findings.md` and `uv.md` into the
   new team dir.
3. Initialize a fresh `attempts.md` with the header row and empty frontier
   summary. Carry forward only open next-actions from the prior `attempts.md`
   into `dispatch.md` or `collation.md`; do not bulk-copy old route rows into
   the new live ledger. If resuming a legacy team with `attempts.tsv`, import
   only live/open next-actions or cite the TSV as legacy context; do not
   maintain parallel ledgers.
4. Prune dead entries (closed UVs, resolved findings). Keep the file
   briefing-size (≤ 200 lines for `findings.md`). This is the team
   lead's active judgment call — no skill needed.
5. Add anything surfaced by the just-completed prior cycle that wasn't
   yet captured (capture-before-shutdown should already have done this;
   this is the final sweep).
6. Commit the new team dir's `findings.md` / `uv.md` / `attempts.md`
   with a subject like `carry forward: <prior-ts> → <new-ts>`. *Now*
   brief the agents.

The chain of team dirs is the history — each is a snapshot in time. Git
log across them is the cross-cycle audit trail.

## Provenance

Every `findings.md` entry, `uv.md` entry, `attempts.md` row, agent report,
commit message, lore entry, `paper-updates.md` line, and team dir carries
provenance to its source: chat path, `rem:wip-*` label, paper line number,
script + SHA, UV-NNN, or agent report path. A claim without provenance is a
defect — reviewers must flag it.

**Codex chat logs are secondary provenance.** The authoritative record is still
on disk: team dirs, reports, scripts, ledgers, lore, commits, and exported chat
summaries. Use `chat-backup` to write a structured `chat.md` / `chat-N.md`
summary because Codex does not expose a stable raw-transcript API in every
runtime. If a Codex or ChatGPT export is available under `<paper>/chats/`, cite
that file path. Do not let an app-only hidden chat log be the sole support for a
mathematical or computational claim.

**Provenance is written by the agent that produced it — never by the team
lead after the fact.** When an agent finishes, its evidence must already
be on disk under `agents/<slug>/`: the report, the scripts that produced
numbers, the notes that show the reasoning trail. The team lead's job is
to brief, collate what agents deposited, and commit — not to ghost-write
a report from a chat summary. A team lead who finds themselves opening a
fresh file to transcribe an agent's finding is the symptom; the fix is to
push back to the agent and get the deposit.

**Scripts are files, not one-liners.** Any script run in service of a
computational claim must be written to `agents/<slug>/scripts/<name>.py`
(or `.sh`, `.jl`, ...) *before* execution, and its path cited in the
report alongside the relevant output. Amending the file and re-running is
the expected workflow — edits are cheap, citations must be possible. No
inline `python -c "..."`, no heredocs piped to an interpreter, no
ephemeral `/tmp/` scripts for anything that produces a cited number.

## Git workflow

- **Auto-commit** after each finished logical unit (remark rewrite, new
  proof block, structural reorg, team dir with reports). Not every
  in-progress touch.
- **Commit while agents are still working.** Team leads should land
  in-flight material as it arrives — each agent's deposit as soon as its
  `report.md` and `scripts/` are on disk, the dispatch brief when the
  team goes live, the collation draft as it fills in. Don't batch all
  agent subdirs into one end-of-cycle commit; a crash or compact erases
  everything unstaged. Cadence while agents are live: commit after each
  agent's deposit lands, or every few minutes of active collation,
  whichever comes first. Use the slack between `send_input` / `wait_agent` returns —
  that's the natural commit window.
- **Stage by name.** Never `git add -A` / `.`. Subjects imperative-mood;
  promote/demote/reject subjects cite UV-NNN; commit bodies mention the
  team dir (and agent subdir, when the deposit is from one agent) if the
  work happened inside one.
- **Auto-push ~1 per 3 commits** (drift 2–4 fine) and always at session end.
  This reverses the global default and applies only to this project.
- **Never force-push, never amend without instruction, never skip hooks.**
  On push rejection, fetch and investigate.

### Compile-check

Enforced by `.githooks/pre-commit` (bootstrap: `git config core.hooksPath
.githooks`). When `<paper>/<main>.tex` is staged, the hook runs
`pdflatex -interaction=nonstopmode -draftmode` and aborts on lines
matching `!` / `Undefined` / `Error` / `Warning: .* undefined` / `Warning:
.* multiply`. The paper no longer `\input`s an `unverified.tex` — UVs
live in team-dir `uv.md` files, outside the LaTeX build. `--no-verify`
is discouraged — don't bypass just because auto-push creates ship
pressure.

## Prompt and skill iteration

Treat `.agents/references/agents/_autoresearch.md`, research skills, and agent role files
as research-org code. After several cycles, do a short retrospective in
`collation.md` or `lore/`: which briefing clauses produced useful deposits,
which caused noise, and what should be simplified or sharpened. Keep changes
small and evidence-driven; don't accrete policy because it sounds good.

## Skill authoring — "let the model cook"

Skills are pointers, not recipes. The model is capable; the skill gives it
the shape of the job, the non-negotiable invariants, and the outputs
expected. Step-by-step bash recipes, exhaustive "don't do X" lists,
duplicated writing-discipline text, and tutorial-length preambles are noise
that crowds out judgment.

When writing or revising a skill:

- Name the goal, the invariants, and the outputs. Trust the model with the
  path between them.
- Refer to AGENTS.md sections rather than repeating their content. A skill
  saying "follow `Writing discipline`" is stronger than re-listing the
  seven bullets.
- Include a bash snippet only when the exact command is load-bearing or
  non-obvious. Otherwise describe the action.
- Anti-pattern lists are for things that would reasonably be tried and
  shouldn't be — not for restating positive rules in negative form.
- Keep each skill under ~80 lines. Skills above that are doing too much or
  explaining too much.

## LaTeX conventions

- Math delimiters everywhere are `\(...\)` / `\[...\]`, including `.md`,
  commit messages, lore. Never convert to `$...$`; preserve on extraction
  from chat exports.
- Frozen macro namespace in the preamble (\(\sim 30\) `\newcommand`s). Don't
  redefine or invent macros; quarantine any need for a new macro as a UV or
  coordinator note.
- `rem:wip-*` labels mark in-paper WIP; each should have a matching
  UV-NNN in the current team dir's `uv.md`.
