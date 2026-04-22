# Riemann2 — Coordinator Policy

This file is the single authoritative policy for the Riemann Hypothesis
project. Every delegated agent is briefed with this document. Rules here
override default Claude Code behavior.

## 1. Project

Canonical paper: `C:\workspace\riemann2\paper\proof_of_rh.tex` (WSL path
`/mnt/c/workspace/riemann2/paper/proof_of_rh.tex`). Monolithic LaTeX
(\texttt{amsart}, frozen macro namespace). Treat it as the canonical source
of record.

The main chat window is the **coordinator / team lead**. It delegates
research, exploration, and verification to agent teams; collates results;
edits canonical files. Delegates are read-only by default (see §3).

## 2. File map

| Path | Role |
|---|---|
| `paper/proof_of_rh.tex` | Canonical draft. Coordinator-only edits. |
| `paper/unverified.tex` | Quarantine ledger (UV-NNN entries) for unpromoted claims. Bidirectional links to `rem:wip-*` labels in the main paper. |
| `paper/findings.md` | Active shared knowledge base (Structural / Negative / Goodies / Open-gaps). ≤200 lines. Pasted in full into every delegation prompt. |
| `lore/` | Workflow plans, cross-session syntheses, design decisions. Permanent session artifacts. |
| `tasks/yyyymmdd-hhmmss-<type>-<slug>/` | Per-dispatch work bundle where `<type>` ∈ `attack-gap \| attack-fund \| audit \| verify \| other`. Chat backup, agent reports, scripts, notes. See §5. |
| `paper/chats/` | Historical ChatGPT session archives. Read-only reference; do not edit. |
| `scripts/` and `scripts/wip/` | Computation code. |
| `final-scripts/paper/` | Hardened verification scripts promoted from `scripts/wip/` with provenance. |
| `.claude/commands/` | Active skills (slash commands). |
| `.claude/commands/archive/` | Retired skills kept for reference. |

Optional companion files may appear as grep indexes once first used:
`paper/findings-in-paper.md`, `paper/unverified-rejected.md`. Lazy-create on
first promotion/rejection; not authoritative (git log is).

## 3. Roles and dispatch

- **Coordinator** (main chat): sole editor of `paper/proof_of_rh.tex`,
  `paper/unverified.tex`, `paper/findings.md`, `CLAUDE.md`, `lore/`. Selects
  and briefs teams. Reviews handbacks. Commits.
- **Delegates**: read-only by default. *May* write to their session's
  `tasks/<dir>/` and nowhere else (§5 and §8). Must not edit canonical
  files unless a specific skill explicitly grants wider scope (e.g.,
  `fix-paper` Phase 1 fixers are scoped to edit the paper).
- **Dispatch mechanism**: every delegation goes through `TeamCreate` with
  **named teammates** (e.g., `gap-closer-mixed4pt`, `explorer-deriv-geo`,
  `verifier-adversarial`) so each agent is visible in its own tmux pane.
  Never spawn via the raw `Agent` tool. On other runtimes (OpenWork, etc.),
  use the equivalent named-teammate primitive. Communicate via
  `SendMessage`. Tear down with `TeamDelete` after graceful shutdown.

## 4. 3+3+2 roster principle

Default shape for a full research-cycle dispatch is ~8 agents, balanced:

- **3 gap-closers** — each targeting a specific UV-NNN or `rem:wip-*` item.
  Use the lemma-closure pattern: exact target statement, routes A/B/C,
  explicit non-goals, fallback to "minimal finite reduction" if closure
  fails.
- **3 explorers** — derivative geometry, fundamentals (normal forms,
  universality, invariants), and cross-cutting structural questions that
  can *redirect how gaps are attacked*. Return observations, candidate
  goodies, candidate negative findings.
- **2 verifiers** — (i) adversarial checker reading the 6 other reports
  for circularity, missing hypotheses, overclaims; (ii) source auditor
  cross-checking that cited labels/lines exist and are used as claimed.

"8" is a target, not a cap. Preserve the **balance**: no all-gap or
all-explore cycles. Exploration exists to direct gap attack.

## 5. Per-task directory convention

Every multi-agent dispatch creates `tasks/yyyymmdd-hhmmss-<type>-<slug>/`
at repo root. The coordinator announces the task dir path upfront and
includes it in every teammate's briefing. Types:

- `attack-gap` — focused closure on a specific UV-NNN or `rem:wip-*` item.
- `attack-fund` — attacking fundamentals / derivative geometry / normal
  forms / cross-cutting structure that will redirect gap attacks.
- `audit` — read-only inspection of a paper subsection or a claim batch.
- `verify` — adversarial or source-auditing pass over prior work.
- `other` — catch-all (e.g., tooling, maintenance, reorganization).

A full `research-team` cycle (the 3+3+2 roster; §4) typically creates
**three sibling task dirs with the same `yyyymmdd-hhmmss-` prefix**: one
`attack-gap-<slug>/` for the 3 gap-closers, one `attack-fund-<slug>/` for
the 3 explorers, and one `verify-<slug>/` for the 2 verifiers. The shared
timestamp ties them together without a nesting layer.

Minimum contents per task dir:

```
tasks/20260423-020000-attack-gap-mixed-4-point/
├── chat.md                          # periodic backup of this session
├── reports/
│   ├── gap-closer-mixed4pt.md       # 7-field report per teammate
│   └── ...
├── scripts/                          # any .py / .sh produced
└── notes/                            # optional per-teammate scratch
```

Every commit made during the session names the task dir(s) in its commit
body. This is the primary provenance anchor (§6 and §10).

## 6. Claim lifecycle (git-as-archive)

Six states: **intake → quarantine → research → adversarial → promote |
demote | reject**.

- **Intake**: idea, repair, objection from coordinator / agent / paper.
- **Quarantine**: coordinator adds a UV-NNN entry to `unverified.tex` with
  all six fields (Title / Status / Source / Claim / Why unverified /
  Needed for promotion), OR a bullet to the appropriate section of
  `findings.md`.
- **Research**: delegates work the item in read-only mode.
- **Adversarial**: a different agent (or the coordinator) attacks the
  claim looking for circularity, missing hypotheses, numerics
  masquerading as proof, stale citations.
- **Promote**: coordinator edits `proof_of_rh.tex` AND deletes the
  `unverified.tex` / `findings.md` entry **in the same commit**. Commit
  subject: `promote UV-NNN: <one-line>` (or `promote <finding>: ...`).
- **Demote**: coordinator edits `proof_of_rh.tex` (remove or weaken) AND
  reinstates entry in `unverified.tex` in the same commit. Subject:
  `demote <label>: <reason>`.
- **Reject**: coordinator deletes the `unverified.tex` entry in a commit
  whose body explains rejection. Subject: `reject UV-NNN: <reason>`.
  If the rejection produced a reusable negative lesson, a
  `capture-finding negative` edit is included in the same commit.

**No status annotations in active files.** Active files stay small and
fully brief-able. Git log is the audit trail.

## 7. Downstream-briefing rule (non-negotiable)

Every delegation prompt MUST include:

1. Full `paper/findings.md` (pasted verbatim).
2. The relevant slice of `paper/unverified.tex` (full file by default; a
   narrower subset only when `$ARGUMENTS` is narrow).
3. The 7-field agent report schema (§8).
4. Explicit non-goals for this teammate.
5. The task dir path (from §5) and the self-deposit checklist (§8).

A skill that dispatches without these is broken. Fix the skill.

## 8. Agent report schema + self-deposit

Every teammate returns a report with these **7 fields**:

- **Claim**
- **Status** ∈ `proved | computational | heuristic | open | rejected`
- **Evidence**
- **Exact refs** — file paths, line numbers, `rem:wip-*` labels, chat
  paths, script paths + commit SHA, UV-NNN IDs
- **Dependencies**
- **Strongest objection** — not optional, not empty, not "none"
- **Needed for promotion**

Acceptable returns also include `unsupported`, `blocked`, `no progress` —
these are honest signals, not failures.

**Self-deposit checklist** (every teammate executes before shutdown):

- Write the final 7-field report to
  `tasks/<dir>/reports/<teammate-name>.md`.
- Put any scripts you created or used in `tasks/<dir>/scripts/`.
- Put any intermediate notes in `tasks/<dir>/notes/<teammate-name>/`
  (optional).
- Do NOT write to `proof_of_rh.tex`, `unverified.tex`, `findings.md`,
  `CLAUDE.md`, or `lore/`.

## 9. Adversarial pass requirement

Any claim that would change proof state requires at least one independent
adversarial checker before promotion. No exceptions.

## 10. Provenance is non-negotiable, everywhere

Every entry in `findings.md`, every UV entry, every agent report, every
commit message, every lore entry, every task dir carries explicit
provenance to its source: `paper/chats/<file>`, `rem:wip-*` label,
`proof_of_rh.tex` line number, script path + commit SHA, UV-NNN,
`tasks/<dir>/reports/<teammate>.md`. A claim without provenance is a
defect — adversarial reviewers must flag it.

## 11. Git workflow

- **Auto-commit after each major edit.** A "major edit" is a finished
  logical unit (a remark rewrite, a new proof block, a structural
  reorganization, a task-dir creation with reports). Minor in-progress
  touches during an ongoing edit do not each need their own commit.
- **Stage files by name.** Never `git add -A` or `git add .`.
- Commit messages: imperative-mood subject. On promote/demote/reject,
  cite UV-NNN in the subject and explain in the body. When a session
  worked inside a task dir, mention the dir in the body.
- **Commit only**; never push unless the user asks.
- Do not skip hooks (`--no-verify`), do not amend without explicit
  instruction, do not force-push.

## 12. LaTeX conventions

- LaTeX-native math delimiters EVERYWHERE: `\(...\)` inline and
  `\[...\]` display — in `.tex`, `.md`, `.txt`, commit messages, lore,
  and any other prose. Do **not** convert to `$...$` / `$$...$$` for
  GitHub rendering.
- When extracting/cleaning prose from external sources (ChatGPT exports,
  agent transcripts), preserve `\(...\)` / `\[...\]` as-is.
- Frozen macro namespace in `proof_of_rh.tex` preamble (30 custom
  `\newcommand`s). Do not redefine or invent new macros without
  coordinator approval.
- `rem:wip-*` label convention marks in-paper WIP items that should have
  a matching UV-NNN in `unverified.tex`.

## 13. Skill index

| Skill | Purpose |
|---|---|
| `research-team` | Primary workhorse: dispatches 3+3+2 roster (gap-closers / explorers / verifiers) via `TeamCreate` into sibling `tasks/<dir>/`s. |
| `research-audit` | N disjoint read-only audits on specified paper subsections; optional `--adversarial` pairs each with a checker. |
| `research-capture` | Coordinator-only synchronous append to `paper/findings.md` (section ∈ structural / negative / goodie / gap). Commits. |
| `trifecta` | 3-agent post-work synthesis (deep insights / literature / hidden connections). |
| `paper-referee` | Referee-issue fix loop (Phase 1 fixers edit the paper; Phase 2 new referees). |
| `paper-harden` | 4-agent read-only quality review (rigor / consistency / formatting / voice). |
| `paper-biblio` | Alphabetize, de-dupe, verify the bibliography. |
| `paper-dedupe` | Remove duplicated content while preserving meaning. |
| `paper-cut` | Move a passage to `paper/cut-for-time.md` with provenance. |
| `script-promote` | Harden a `scripts/wip/` verification script into `final-scripts/paper/` with a lore note. |

Retired skills live in `.claude/commands/archive/`.

## 14. When not to use a skill

Small / obvious edits, single-file tweaks, and specific user-directed
commands should go directly — not through a multi-agent skill. Skills
are for multi-agent dispatch or repeatable multi-step procedures where
their structure pays off.
