# Riemann2 — Coordinator Policy

Main chat is the coordinator / team lead. Delegates research, exploration, and
verification; collates; edits canonical files. Delegates are read-only by
default. Every agent is briefed with this file.

## 1. Files

| Path | Role |
|---|---|
| `paper/proof_of_rh.tex` | Canonical draft. Coordinator-only edits. |
| `paper/unverified.tex` | Quarantine ledger — UV-NNN entries ("UV" = "unverified") linked to `rem:wip-*` labels in the paper. |
| `paper/findings.md` | Shared knowledge base (Structural / Negative / Goodies / Open-gaps). \(\le 200\) lines. Pasted in full into every delegation. |
| `lore/` | Workflow plans, syntheses, decisions. Permanent. |
| `tasks/yyyymmdd-hhmmss-<type>-<slug>/` | Per-dispatch bundle. `<type>` \(\in\) `attack-gap \| attack-fund \| audit \| verify \| other`. |
| `paper/chats/` | Historical ChatGPT archives. Read-only. |
| `scripts/` + `scripts/wip/` | Computation. `final-scripts/paper/` for hardened ones. |

Optional grep indexes (`findings-in-paper.md`, `unverified-rejected.md`) are
lazy-created on first use. Not authoritative — git log is.

Canonical paper path: `C:\workspace\riemann2\paper\proof_of_rh.tex` (WSL
`/mnt/c/workspace/riemann2/...`). Monolithic `amsart`, frozen macro namespace.

## 2. Dispatch

Every delegation goes through `TeamCreate` with named teammates
(e.g. `gap-closer-mixed4pt`) so each is tmux-visible. Never the raw `Agent`
tool. Communicate via `SendMessage`; `TeamDelete` on shutdown.

**3+3+2 roster** for a balanced cycle: 3 gap-closers (each on a specific
UV-NNN / `rem:wip-*`, with routes A/B/C and fallback to minimal finite
reduction) + 3 explorers (derivative geometry, fundamentals, cross-cutting
structure that *redirects* how gaps are attacked) + 2 verifiers (adversarial
+ source auditor). 8 is a target, not a cap — preserve the balance.

### Dispatch selector

| Intent | Skill |
|---|---|
| balanced cycle, no fixed target | `research-team` |
| focused push on one UV / label | `research-attack` |
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

## 3. Coordinator autonomy

The coordinator decides roster sizes, UV targets, explorer topics, non-goals
(synthesized from adjacent in-flight work and recent lore), task-dir slugs,
commit messages, subsection selection, demote timing, `findings.md` slicing
— without asking. `AskUserQuestion` is for architectural or irreversible
decisions only. Never interrupt over research-direction minutia.

## 3a. Auto-run — default for research work

Research work (gap-closing, exploration, verification, synthesis,
audit cycles) runs in a continuous auto-loop. The coordinator does not
ask "should I keep going?" or "is this a good stopping point?" between
cycles. The user is likely away and expects work to continue
indefinitely until a real terminal condition is hit or the user
manually interrupts.

**Loop:**

1. Read state — recent `lore/`, `findings.md`, `unverified.tex`, the
   last task dir, the last cycle's verdicts and commits.
2. Pick the next move — a UV target, an explorer topic, a redirect, an
   audit, a synthesis. Default to `research-attack` over `research-team`
   per §2.
3. Dispatch via the §2 selector. Brief per §5.
4. Collate returns. Promote / demote / quarantine / reject per §8.
   Commit by logical unit; auto-push per §10.
5. Go to 1.

**Decide without asking:** which UV, which explorer topic, roster size,
task-dir slug, commit wording, whether to redirect, when to synthesize.
§3 autonomy covers this.

**Pause only for:** architectural or irreversible decisions (macro
namespace changes, canonical-file reorgs, abandoning a proof strategy
wholesale); a hard blocker the coordinator cannot work around; explicit
user interruption.

**Terminal conditions** (stop the loop): zero open UV entries and no
outstanding `rem:wip-*` labels; or the targeted synthesis fully closes
with `paper-harden` / `paper-referee` clean; or explicit user halt.
If context is compacted or a handoff occurs, immediately resume the
active agenda from the last recorded state — do not treat that as a
terminal condition.

**When stuck (out of obvious moves), think harder — do not stop.**
Re-read `findings.md` and recent `lore/` for a missed angle. Combine
previous near-misses; two open UVs with related structure often admit a
hybrid attack. Try a more radical redirect — different function space,
different local model, structurally different route. Consult
`paper/chats/` for historical threads that were parked. Spin up
`trifecta` for fresh literature and cross-discipline pointers.
"No progress this cycle" is an acceptable report; "I ran out of ideas"
is not — the archive has the ideas.

(Loop pattern adapted from Karpathy's
[autoresearch/program.md](https://github.com/karpathy/autoresearch).)

## 4. Writing discipline

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
  prose. Deposit the script in the task dir; cite it in the report.

## 5. Briefing rule

Every delegation includes: full `findings.md`, the 7-field schema (§7),
explicit non-goals, the task-dir path + self-deposit checklist, and the §4
writing-discipline reminder.

**`unverified.tex` is NOT in the default briefing.** Sharing tentative
claims poisons independent agents. Exceptions, narrow: the gap-closer
attacking that specific UV; the adversarial verifier reviewing exactly that
claim; the source auditor whose range contains the matching `rem:wip-*`;
the Phase-1 fixer whose issue touches it. In every exception share only the
individual entries, not the ledger.

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

## 6. Task dirs and self-deposit

Every multi-agent dispatch creates `tasks/yyyymmdd-hhmmss-<type>-<slug>/`
with `reports/`, `scripts/`, `notes/`, and eventually `chat.md`. A full
`research-team` cycle creates three siblings sharing the timestamp prefix
(attack-gap, attack-fund, verify).

Teammates deposit to `tasks/<dir>/reports/<teammate>.md` (7-field report),
`scripts/` (anything created), `notes/<teammate>/` (optional scratch). They
do **not** write to `proof_of_rh.tex`, `unverified.tex`, `findings.md`,
`CLAUDE.md`, or `lore/` unless a skill grants an explicit exception
(e.g. `paper-referee` Phase 1).

## 7. Report schema

Every teammate report has seven fields:

- **Claim**
- **Status** \(\in\) `proved | computational | heuristic | open | rejected`
- **Evidence**
- **Exact refs** — file paths, line numbers, `rem:wip-*`, chat paths, scripts
  + SHAs, UV-NNN
- **Dependencies**
- **Strongest objection** — never empty, never "none"
- **Needed for promotion**

`unsupported` / `blocked` / `no progress` are honest signals, not failures.

## 8. Claim lifecycle (git-as-archive)

**Intake → quarantine → research → adversarial → promote | demote | reject.**

- **Quarantine**: add UV-NNN to `unverified.tex` or a bullet to the right
  section of `findings.md`.
- **Adversarial pass is non-negotiable** before any proof-state change.
- **Promote**: edit paper AND delete UV/findings entry in the *same* commit.
  Subject: `promote UV-NNN: <one-line>`.
- **Demote**: edit paper + reinstate UV entry in the same commit. Subject:
  `demote <label>: <reason>`.
- **Reject**: delete UV entry; commit body explains; if a reusable lesson
  surfaced, include `research-capture negative` in the same commit.
  Subject: `reject UV-NNN: <reason>`.

No status annotations in active files — they stay brief-size. Git log is
the audit trail.

**Broadcast corrections immediately.** If something already in the paper is
found false, `SendMessage` every active teammate before doing anything else,
then demote + optional negative-capture in one commit. Cost of a delayed
correction >> cost of a brief interruption.

## 9. Provenance

Every `findings.md` entry, UV entry, agent report, commit message, lore
entry, and task dir carries provenance to its source: chat path, `rem:wip-*`
label, paper line number, script + SHA, UV-NNN, or task-dir report. A claim
without provenance is a defect — reviewers must flag it.

## 10. Git workflow

- **Auto-commit** after each finished logical unit (remark rewrite, new
  proof block, structural reorg, task-dir with reports). Not every
  in-progress touch.
- **Stage by name.** Never `git add -A` / `.`. Subjects imperative-mood;
  promote/demote/reject subjects cite UV-NNN; commit bodies mention the
  task dir if the work happened inside one.
- **Auto-push ~1 per 3 commits** (drift 2–4 fine) and always at session end.
  This reverses the global default and applies only to this project.
- **Never force-push, never amend without instruction, never skip hooks.**
  On push rejection, fetch and investigate.

### Compile-check

Enforced by `.githooks/pre-commit` (bootstrap: `git config core.hooksPath
.githooks`). When `paper/proof_of_rh.tex` is staged, the hook runs
`pdflatex -interaction=nonstopmode -draftmode` and aborts on lines
matching `!` / `Undefined` / `Error` / `Warning: .* undefined` / `Warning:
.* multiply`. `--no-verify` is discouraged — don't bypass just because
auto-push creates ship pressure.

## 11. Skill authoring — "let the model cook"

Skills are pointers, not recipes. The model is capable; the skill gives it
the shape of the job, the non-negotiable invariants, and the outputs
expected. Step-by-step bash recipes, exhaustive "don't do X" lists,
duplicated writing-discipline text, and tutorial-length preambles are noise
that crowds out judgment.

When writing or revising a skill:

- Name the goal, the invariants, and the outputs. Trust the model with the
  path between them.
- Refer to CLAUDE.md sections rather than repeating their content. A skill
  saying "follow §4 writing discipline" is stronger than re-listing the
  seven bullets.
- Include a bash snippet only when the exact command is load-bearing or
  non-obvious. Otherwise describe the action.
- Anti-pattern lists are for things that would reasonably be tried and
  shouldn't be — not for restating positive rules in negative form.
- Keep each skill under ~80 lines. Skills above that are doing too much or
  explaining too much.

## 12. LaTeX conventions

- Math delimiters everywhere are `\(...\)` / `\[...\]`, including `.md`,
  commit messages, lore. Never convert to `$...$`; preserve on extraction
  from chat exports.
- Frozen macro namespace in the preamble (\(\sim 30\) `\newcommand`s). Don't
  redefine or invent without coordinator approval.
- `rem:wip-*` labels mark in-paper WIP; each should have a matching UV-NNN.
