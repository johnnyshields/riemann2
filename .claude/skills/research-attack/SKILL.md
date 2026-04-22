---
name: research-attack
description: Small-cycle variant of research-team. 1-2 gap-closers + 1 verifier for a focused push on one UV-NNN or rem:wip-* target. Cheaper than the 3+3+2 full cycle.
---

# Research Attack (small cycle)

Focused push on a single gap. Dispatches 1-2 gap-closers plus one
adversarial verifier via `TeamCreate`. Use when you want to drive a
specific UV-NNN to closure (or to minimal finite reduction) without
spinning up the full 3+3+2 roster. See `CLAUDE.md` §3, §4, §5, §7.

## Arguments

`$ARGUMENTS` — the target:

- `UV-NNN` — attack that quarantined claim.
- `rem:wip-<label>` — attack the paper's WIP remark at that label.
- free text (e.g. `mixed 4-point`) — coordinator picks the best-matching
  UV-NNN or `rem:wip-*`.

Optional flags:
- `--double` — spawn 2 gap-closers on different routes instead of 1.
  Default is 1 gap-closer + 1 verifier.

## Mandatory preamble

1. Read the briefing packet:
   - `paper/findings.md`.
   - The target's `unverified.tex` entry (paste verbatim into the
     gap-closer's briefing per `CLAUDE.md` §7 exception).
   - The paper region around the target: read `rem:wip-*` label line
     \(\pm 200\) lines.
2. Create a single task dir:
   `tasks/<ts>-attack-gap-<slug>/` with `reports/`, `scripts/`, `notes/`.
   `<ts>` = `date +%Y%m%d-%H%M%S`; `<slug>` = the UV-ID or a short
   descriptor of the target (e.g. `uv002-pairlike-finitecore`).
   Announce the path.

## Dispatch

`TeamCreate team_name: "research-attack-<ts>"`, then spawn:

- **Gap-closer(s)**: 1 by default, 2 with `--double`.
  Names: `gap-<target-slug>` (or `gap-<target>-routeA`, `-routeB`).
  Briefing MUST include:
  - Full `paper/findings.md`.
  - The specific UV entry (verbatim).
  - Target statement in its cleanest form (see `CLAUDE.md` §7a:
    "What is the cleanest target here?").
  - Routes A/B/C (closer picks one; coordinator may suggest a split
    when `--double` is set).
  - Fallback instruction: "If full closure is too hard, reduce to the
    smallest list of concrete unresolved sub-statements" (§7a idiom).
  - 7-field report schema.
  - Writing-discipline reminder (`CLAUDE.md` §3a).
  - Self-deposit checklist: `tasks/<dir>/reports/<teammate>.md`.
  - Non-goals synthesized by coordinator (`CLAUDE.md` §3 autonomy):
    typically "do not attack adjacent UV entries; do not re-prove
    already-closed lemmas; do not propose new conjectures outside the
    target's scope."

- **Adversarial verifier**: 1. Name: `verifier-adversarial`.
  Waits for gap-closer(s) to deposit, then reads their report(s) and
  attacks. Briefing MUST include:
  - Full `paper/findings.md`.
  - The specific UV entry (per §7 exception, adversarial reviewer).
  - 7-field schema.
  - §3a + §7a idioms, especially "Qualify any impossibility claim with
    'from [scope] alone.'" and "Give me the honest verdict."
  - Self-deposit checklist.
  - Non-goals: "do not rewrite the closure attempt; return a verdict
    with concrete breaks if any."

## Post-cycle audit (coordinator)

1. Verify every expected report file exists in `tasks/<dir>/reports/`:
   `ls tasks/<dir>/reports/` should show one entry per spawned
   teammate. If any are missing, do NOT proceed — chase the teammate
   via `SendMessage` or record the miss in a lore note.
2. Read all reports.
3. Cross-check closure claim against cited paper lines / labels.
4. Update `paper/unverified.tex` (refine "Needed for promotion" on the
   target; close it if the verifier confirmed).
5. Update `paper/findings.md` via `research-capture` if new
   Goodies / Negative / Gap surfaced.
6. **No edits to `paper/proof_of_rh.tex`** from this skill. Promotion is
   a separate deliberate coordinator step after review.
7. `SendMessage` each teammate `{type:"shutdown_request"}`,
   `TeamDelete`. Commit the task dir. Subject cites UV-NNN; body
   references the dir path.
