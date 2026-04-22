# Paper Referee

Two-phase review loop on the canonical paper: Phase 1 fixers edit the paper
in response to known issues; Phase 2 fresh referees re-review. See
`CLAUDE.md` §3, §7 (briefing rule), §5 (task dirs). Phase 1 fixers are an
explicit edit-capable exception to the read-only-delegate default.

## Arguments

`$ARGUMENTS`:
- **empty** — fix `paper/proof_of_rh.tex` using the latest referee
  feedback found in `lore/` (search for recent `referee` entries).
- **file path** — fix that file instead.
- **`--no-referee`** — fix only, skip Phase 2.
- **`--referee-only`** — skip Phase 1 fixes, just run referees.
- **specific issues** (e.g. `epsilon exponent, label drift`) — fix only
  those issues.
- Combinations work.

## Mandatory preamble

1. Read the briefing packet in full:
   - `paper/findings.md`
   - `paper/unverified.tex`
   - Most recent `lore/` referee report(s)
   - The target paper (default `paper/proof_of_rh.tex`)
2. Resolve `<slug>` from the issues being addressed (e.g.
   `referee-round-3`).
3. Create the task dirs:
   - `tasks/<ts>-attack-gap-referee-<slug>/` (Phase 1 fixers — they will
     edit the paper)
   - `tasks/<ts>-verify-referee-<slug>/` (Phase 2 fresh referees)
   Subdirs `reports/`, `scripts/`, `notes/`. Announce paths upfront.

## Phase 1: Fix Team

`TeamCreate team_name: "paper-referee-fix-<ts>"`, spawn up to 3 named
fixers whose expertise matches the current issues. Examples of named
teammates (pick per content):
`fixer-local-geometry`, `fixer-finite-s-algebra`, `fixer-analysis`,
`fixer-projective-rigidity`, `fixer-endgame`.

Each fixer's briefing MUST include:
- Full `paper/findings.md`.
- Per `CLAUDE.md` §7 exception: the specific UV-NNN entries that their
  assigned issues touch, pasted verbatim. Fixers editing the paper
  need to know which nearby claims are already quarantined so they
  don't solidify a conditional claim by accident. Do not share UV
  entries unrelated to their issues.
- The specific referee issues assigned to them.
- The 7-field report schema.
- The writing-discipline reminder (`CLAUDE.md` §3a): state facts
  directly, no overclaim, no hedge, honest scope disclaimers welcome.
- The self-deposit checklist (`tasks/<fix-dir>/reports/<teammate>.md`).
- **Edit-capable exception**: fixers may edit `paper/proof_of_rh.tex`
  directly for the assigned issues. They may not edit
  `paper/unverified.tex` or `paper/findings.md` — surface new findings in
  their report for coordinator review.

Non-goals: do not rewrite beyond the assigned issues; do not introduce
new lemmas without a UV entry.

When Phase 1 completes, `SendMessage` each fixer `{type:"shutdown_request"}`
and `TeamDelete` the fix team.

## Phase 2: Referee Team (skip if `--no-referee`)

`TeamCreate team_name: "paper-referee-review-<ts>"`, spawn 2 fresh
referees:
- `referee-math` — reviews as for a pure-math journal; checks proofs,
  hypotheses, circularity, citations. Verdict: accept / minor revision
  / major revision / reject.
- `referee-general` — reviews for clarity, accessibility, narrative
  flow; flags overclaims and unexplained jargon. Same verdict set.

Referee briefing MUST include:
- Full `paper/findings.md`.
- Full `paper/unverified.tex` (referees are adversarial verifiers per
  `CLAUDE.md` §7 exception — they need to know what's conditional
  versus what's promoted).
- The 7-field report schema.
- The writing-discipline reminder (`CLAUDE.md` §3a).
- The self-deposit checklist (`tasks/<verify-dir>/reports/<referee>.md`).
- Explicit non-goals: referees do not edit the paper; they return a
  formal report with verdict and an issues list.
- Read ALL prior referee reports in `lore/` and check whether each old
  issue is now addressed.

## After completion

1. Commit the paper edits from Phase 1 (stage `paper/proof_of_rh.tex`
   by name). Cite the attack-gap task dir in the body.
2. Commit referee reports (they sit in the verify task dir). Cite the
   verify task dir in the body.
3. Summarize verdicts to the user.
