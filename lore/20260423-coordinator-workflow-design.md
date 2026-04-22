# Coordinator Workflow Design

Date: 2026-04-23
Commits: `3ed917a` \(\to\) `049a73a` (7 commits)

## Context

Replacing the manual ChatGPT dispatch workflow (~2 weeks of 38 chats in
`paper/chats/`) with an automated coordinator model. The main chat window
is the team lead; delegated agents handle research, exploration, and
verification; the canonical paper (`paper/proof_of_rh.tex`) and
quarantine ledger (`paper/unverified.tex`) stay cleanly separated.

The prior lore note `20260422-opencode-research-workflow.md` sketched
this but wasn't operationalized. This session makes it concrete.

## Architectural principles

1. **Provenance everywhere.** Every finding, UV entry, agent report,
   commit, and task dir carries explicit provenance to its source —
   chat path, `rem:wip-*` label, line number, script + SHA, UV-NNN,
   or `tasks/<dir>/reports/<teammate>.md`.
2. **Single active knowledge base.** `paper/findings.md`, one file,
   four sections (Structural / Negative / Goodies / Recurring-open-gaps),
   \(\le 200\) lines, pasted in full into every agent briefing. Seeded
   from prior chat syntheses at 77 lines.
3. **Git-as-archive.** Promoted / rejected items are deleted from the
   active files in the same commit that changes the paper; commit
   messages and diffs are the audit trail. No status annotations inside
   the active files.
4. **3+3+2 roster shape.** Default dispatch is \(\approx 8\) agents:
   3 gap-closers + 3 explorers + 2 verifiers. Balance matters — no
   all-gap or all-explore cycles.
5. **Downstream-briefing rule.** Every delegation pastes full
   `findings.md` + the 7-field report schema + explicit non-goals +
   task-dir path. `unverified.tex` is NOT in the default briefing —
   narrow, named §7 exceptions only (gap-closer on their UV, adversarial
   verifier, source auditor on matching `rem:wip-*`, Phase-1 fixer).
   Generic explorers, content auditors, formatters, voice reviewers,
   trifecta analysts, literature searchers, and "under-the-nose"
   analysts receive findings.md only — spoiler / poisoning risk.
6. **TeamCreate with named teammates.** All delegation goes through
   named-teammate primitives so each agent is tmux-visible. Never the
   raw `Agent` tool.
7. **Per-task directory.** Every dispatch creates
   `tasks/yyyymmdd-hhmmss-<type>-<slug>/` where `<type>` \(\in\)
   `attack-gap | attack-fund | audit | verify | other`. Agents
   self-deposit reports and scripts there. A 3+3+2 cycle creates three
   sibling task dirs with the same timestamp prefix.
8. **Coordinator writing discipline.** Quasi-referee standard on the
   coordinator's own paper edits. Three-bin separation (proved /
   conditional / missing), gap reduction over closure, scoped negation
   ("from [scope] alone"), caution-labeled synthesis, honest-verdict
   closure. This discipline is shared with every agent in their
   briefing.
9. **Broadcast-correction duty.** When the coordinator discovers
   something false already in the paper, `SendMessage` all active
   teammates immediately, demote in the same commit, optionally capture
   a negative finding with `Do-not-retry:`.

## Skill inventory

### Active (10)
- `research-team` — primary workhorse, 3+3+2 dispatch.
- `research-audit` — N disjoint read-only subsection audits.
- `research-capture` — coordinator-only append to `findings.md`.
- `trifecta` — 3-agent post-work synthesis (deep insights /
  literature / hidden connections). No UV sharing.
- `paper-referee` — 2-phase referee review + fix loop.
- `paper-harden` — 4-agent read-only quality review.
- `paper-biblio` — bibliography housekeeping (canonical path
  hardcoded).
- `paper-cut` — move passage to `cut-for-time.md` with provenance.
- `paper-dedupe` — remove duplicate content.
- `script-promote` — harden a verification script into
  `final-scripts/paper/`.

### Archived (2)
- `archive/coordinate-paper.md` — policy content merged into
  CLAUDE.md.
- `archive/research-team.md` — prior 6-prestige-role version,
  replaced by new 3+3+2 `research-team`.

### Deleted (3)
- `proof-team.md`, `proof-team-innovate.md`, `proof-team-prune.md` —
  tied to the retired `fannes-proof` team. Git log preserves.

## Implicit patterns operationalized (from chat-archive mining)

Five high-leverage habits the user applied manually, now policy:

1. **Three-bin separation** on every audit / synthesis / status memo.
2. **Gap reduction** to concrete unresolved sub-statements, never
   "further work needed" as paragraph cover.
3. **Scoped negation** on impossibility claims.
4. **Caution-labeled synthesis** with `[confirmed]` / `[conditional]`
   / `[candidate]` tags before merging.
5. **Honest-verdict closure** at end of audits and status memos.

New `CLAUDE.md` §7a lists seven briefing idioms that license candor,
distilled from recurring user phrasing in the chats:

- "Separate three things: proved / conditional / missing."
- "What is the cleanest target here?"
- "Give me the honest verdict."
- "If full closure is too hard, reduce to the smallest list of concrete
  unresolved sub-statements."
- "Qualify any impossibility claim with 'from [scope] alone.'"
- "Label each claim with a confidence tag before merging."
- "`unsupported`, `blocked`, `no progress` are acceptable returns."

`research-team`, `research-audit`, and `trifecta` now paste the
relevant subset into every teammate's briefing.

## Smoke test (not yet run)

1. Pick 3 short subsections of `proof_of_rh.tex` that don't touch any
   UV entry. Verify via `grep -n '\\(sub\\)*section'`.
2. Run `/research-audit §<a>,§<b>,§<c> --non-goals: "audit only"`.
3. Inspect each auditor's incoming briefing — must contain full
   `findings.md`, the 7-field schema, §7a idioms, non-goals, task dir
   path; must NOT contain `unverified.tex` content (unless a `rem:wip-*`
   label appears in the audited range).
4. Inspect each handback — 7 fields present, Status \(\in\) allowed
   values, `Strongest objection` non-empty, audit verdicts in the
   three-bin form.
5. `git diff paper/proof_of_rh.tex` must be empty after the run.
6. Every teammate must be visible as a named tmux pane; `TeamDelete`
   cleans up on cycle end.
7. Follow-up: `/research-team` (no args) → 8 agents in 3+3+2 across 3
   sibling task dirs.

## Files of record

- `CLAUDE.md` (355 lines) — authoritative policy.
- `paper/findings.md` (77 lines) — active knowledge base.
- `paper/unverified.tex` — quarantine ledger (unchanged this session).
- `.claude/commands/*.md` — 10 active skills.
- `.claude/commands/archive/*.md` — 2 retired.
- `lore/20260423-coordinator-workflow-design.md` (this file).

Git range for the full redesign: 7 commits from `3ed917a` (findings
seed) through `049a73a` (implicit patterns).
