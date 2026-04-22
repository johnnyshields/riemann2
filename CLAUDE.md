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
| `paper/unverified.tex` | Quarantine ledger (UV-NNN entries — "UV" = "unverified") for unpromoted claims. Bidirectional links to `rem:wip-*` labels in the main paper. |
| `paper/findings.md` | Active shared knowledge base (Structural / Negative / Goodies / Open-gaps). ≤200 lines. Pasted in full into every delegation prompt. |
| `lore/` | Workflow plans, cross-session syntheses, design decisions. Permanent session artifacts. |
| `tasks/yyyymmdd-hhmmss-<type>-<slug>/` | Per-dispatch work bundle where `<type>` ∈ `attack-gap \| attack-fund \| audit \| verify \| other`. Chat backup, agent reports, scripts, notes. See §5. |
| `paper/chats/` | Historical ChatGPT session archives. Read-only reference; do not edit. |
| `scripts/` and `scripts/wip/` | Computation code. |
| `final-scripts/paper/` | Hardened verification scripts promoted from `scripts/wip/` with provenance. |

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
- **Coordinator autonomy.** The coordinator is expected to do the right
  thing by default and NOT ask the user about the minutia of research
  directions. Autonomously: pick roster sizes, choose UV targets for
  gap-closers, choose explorer topics, synthesize non-goals from context
  (active UV entries, adjacent in-flight work, recent lore, the cycle's
  focus), pick task-dir slugs, draft commit messages, decide which
  subsection to audit next, decide when to demote, decide which `findings.md`
  sections to paste where. `AskUserQuestion` is reserved for **major
  decisions**: architectural choices about the project itself,
  irreversible actions (deletions beyond the task dir, force-ops),
  or moments where the user has materially diverging reasonable
  options with meaningfully different consequences. Never ask for
  permission on routine research direction, scope, or drafting-level
  judgment.

## 3a. Coordinator writing discipline

When the coordinator edits `paper/proof_of_rh.tex`, apply a
**quasi-referee** standard to the coordinator's own text. Not a hardass
— just the same caution a good referee would apply. Share this
discipline with every delegated agent in their briefing.

**State facts directly.**
No AI tells ("it is worth noting," "we leverage / utilize / employ,"
"to the best of our knowledge," "interestingly," "remarkable").

**Do not overclaim.**
If a result is only computationally verified, say so. If a theorem
holds "for tested configurations," do not write "for all." If a bound
is effective, say so; if it isn't, do not imply it.

**Three-bin separation is mandatory.**
On any audit, synthesis, or status memo, explicitly separate claims
into: `proved` / `conditional on [hypothesis X]` / `missing`. Never blur
these. Never write a stronger conclusion than the hypotheses support.

**Gap reduction over closure.**
When a proof has gaps, do not patch with "further analysis needed."
Reduce to the smallest concrete list of missing sub-statements — each
stated as a precise missing theorem, identity, or estimate. Vague
gaps become UV entries, not paragraph cover.

**Scoped negation.**
Never state impossibility without scope. "Ruled out" must always
carry a "from [scope] alone" qualifier. Example: "The topological
route is exhausted from intrinsic one-pair affine geometry alone"
— NOT "the topological route is exhausted." This preserves room for
non-obvious breakthroughs via a different path.

**Caution-labeled synthesis.**
When merging outputs from multiple agents, chats, or sessions, pre-label
each source with `[confirmed]`, `[conditional on X]`, or `[candidate,
not yet verified]`. Only `[confirmed]` items may be written into the
paper; others go to `unverified.tex` or `findings.md`.

**Honest-verdict closure.**
End audits and status memos with a "Honest verdict:" line stating what
is and isn't closed. This licenses candor and prevents sycophantic drift
at chat end.

**Scope-disclaimer welcome, not timid.**
"This closes the pair-like branch; the finite-core branch remains open"
beats "this closes the pair-like branch (modulo some subtleties)."

**When in doubt, quarantine.**
UV entry first, promote later.

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
2. The 7-field agent report schema (§8).
3. Explicit non-goals for this teammate.
4. The task dir path (from §5) and the self-deposit checklist (§8).

**`paper/unverified.tex` is NOT included in the default briefing.**
Sharing tentative claims broadly spoils, poisons, or distracts
independent agents — exploration and audit should happen against the
*verified* state of the proof, not the hopeful state. Wait until
verification is complete before circulating a claim.

**Exceptions** (narrow, named, and logged):

- A gap-closer attacking a specific UV-NNN entry receives that one
  entry verbatim.
- An adversarial verifier reviewing a specific claim (either a UV
  entry or prior teammate output) receives exactly what they're
  verifying.
- A source auditor whose assigned subsection contains a `rem:wip-*`
  label tied to a UV entry receives that entry.
- Phase-1 paper fixers whose assigned issues touch a UV entry receive
  those entries.

In every exception, share only the individual UV entries involved —
never the full ledger. Generic explorers, content auditors, formatters,
voice reviewers, literature searchers, and "under-the-nose" analysts
receive **findings.md only**.

A skill that dispatches without the required fields, or that
over-shares `unverified.tex` against this rule, is broken. Fix the
skill.

### 7a. Briefing idioms that license candor

These phrases should appear in agent briefings; they have an outsized
effect on honest output (distilled from the prior manual ChatGPT
workflow):

- **"Separate three things: proved / conditional / missing."** Open
  audit briefings with this. Forces the three-bin discipline from §3a.
- **"What is the cleanest target here?"** Before pivoting mid-audit,
  restate the theorem in its cleanest form. Prevents drift to adjacent
  questions.
- **"Give me the honest verdict."** Use at closure time to license
  "this does not yet close" answers.
- **"If full closure is too hard, reduce to the smallest list of
  concrete unresolved sub-statements."** For lemma-closure briefings.
- **"Qualify any impossibility claim with 'from [scope] alone.'"**
  Required for negative findings and adversarial reports.
- **"Label each claim with a confidence tag before merging."** For
  synthesis roles.
- **"`unsupported`, `blocked`, and `no progress` are acceptable
  returns."** Explicit anti-sycophancy. Re-state in every briefing.

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

### 9a. Broadcast-correction duty

When the coordinator discovers that something already in
`paper/proof_of_rh.tex` is false, imprecise, or over-claimed, it is an
IMMEDIATE coordinator responsibility to:

1. `SendMessage` every active teammate with a brief correction notice
   so they stop working under the flawed assumption. Broadcast across
   all active teams (`to: "*"` where available).
2. Demote the offending claim per §6: edit the paper to remove or weaken
   and reinstate a UV entry in `unverified.tex` in the same commit.
3. If the correction produces a reusable negative lesson, call
   `research-capture negative` in the same commit with `Do-not-retry:`
   describing the specific flawed move.
4. In the commit body, use `correction:` or `demote:` as the subject
   prefix so the audit trail is obvious. Cite any active task dirs.

The cost of a delayed correction — teammates running hours on a false
premise and writing it into new findings — is much higher than the cost
of a brief interruption. Broadcast first, explain later.

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
- **Auto-push every ~3 commits.** This project specifically wants the
  coordinator to periodically commit AND push without asking. Cadence:
  roughly one `git push` per 3 commits (drift to 2-4 is fine). At the
  end of a session, push any trailing commits so the remote is current.
  This reverses the usual "commit only, never push" default — it applies
  ONLY to this project.
- **Never** force-push (`--force`, `+refspec`), even under the
  auto-push rule. If push is rejected as non-fast-forward, fetch and
  investigate — do not clobber.
- Do not skip hooks (`--no-verify`), do not amend without explicit
  instruction, do not force-push.

### 11a. Compile-check before committing paper edits

Every commit that modifies `paper/proof_of_rh.tex` goes through a
compile-check. Enforced by `.githooks/pre-commit`:

```sh
# One-time setup per clone:
git config core.hooksPath .githooks
```

The hook runs `pdflatex -interaction=nonstopmode -draftmode` on the
paper when it's staged and aborts the commit if any of these patterns
appear in the log:

- lines beginning with `!`
- `Undefined`, `Error`
- `Warning: ... undefined`, `Warning: ... multiply`

Catches LaTeX syntax errors, undefined `\ref{}` / `\cite{}`, and
multiply-defined labels — failure modes that would otherwise not
surface until `paper-harden`.

Bypass (`--no-verify`) is discouraged. Use only with an explicit
justification — the coordinator should NOT bypass routinely even if
the auto-push rule creates pressure to ship.

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

