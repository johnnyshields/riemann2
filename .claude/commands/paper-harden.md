# Paper Harden

Read-only quality review of `paper/proof_of_rh.tex` from four angles:
rigor / consistency / formatting / voice. See `CLAUDE.md` §7, §8.
All reviewers are read-only and deposit reports in the task dir.

## Mandatory preamble

1. Read the briefing packet (for the coordinator):
   - `paper/findings.md` — especially **Negative** and **Recurring
     open gaps** (so reviewers can catch overclaims).
   - `paper/unverified.tex` — coordinator reference only; shared with
     `reviewer-rigor` per `CLAUDE.md` §7 (they need it to detect
     claims that should be quarantined but aren't). NOT shared with
     `reviewer-consistency`, `reviewer-formatting`, or `reviewer-voice`.
   - `paper/proof_of_rh.tex` — the target (read as needed per role).
2. Create task dir `tasks/<ts>-audit-harden-<slug>/` with `reports/`,
   `scripts/`, `notes/`. `<slug>` may be an empty string if the run is
   untargeted, or a theme like `post-referee` / `pre-submission`.
   Announce the path.

## Dispatch

`TeamCreate team_name: "paper-harden-<ts>"`, spawn 4 named reviewers.
Each briefing includes full `findings.md` + the 7-field schema + the
writing-discipline reminder (`CLAUDE.md` §3a) + the self-deposit
checklist + explicit non-goals: "report only, do not edit the paper."
`reviewer-rigor` additionally receives full `unverified.tex` per
`CLAUDE.md` §7 (overclaim detection); the other three do not.

### `reviewer-rigor`
- Read the full paper.
- For each proof: verify every claim is justified; flag handwavy
  arguments, missing hypotheses, mismatches between theorem and proof.
- Cross-check against `findings.md` Negative — flag any argument that
  silently retries a ruled-out move.
- Cross-check against `unverified.tex` — flag claims that should be
  quarantined but aren't, or promoted claims that still have UV entries.
- No hedging flagging: no "it is worth noting," "we are unaware of";
  state facts or remove.

### `reviewer-consistency`
- Read the full paper.
- Notation consistency; stale renames; label/reference integrity
  (`\label`/`\ref` pairs resolve).
- Counts that must match across abstract/intro/conclusion.
- Frozen-macro compliance (no redefinitions, no fresh
  `\newcommand`s).

### `reviewer-formatting`
- Compile via `pdflatex` (twice); report any warnings beyond cosmetic
  hyperref issues.
- Undefined references, multiply-defined labels, overfull/underfull
  boxes (substantive only).
- `\texorpdfstring` on math-in-titles.
- Blank-line and environment-pair sanity.
- Bibliography abbreviation consistency.

### `reviewer-voice`
- Read the full paper.
- AI tells ("it is worth noting," "interestingly," "we
  leverage/utilize/employ," "to the best of our knowledge"): flag each.
- Structural AI patterns (identically-templated remarks, perfectly
  parallel bullets).
- Voice switches (we/passive) within paragraphs.
- Marketing language, self-congratulation, overclaims.
- Rank HIGH / MEDIUM / LOW.

## After completion

1. Read all 4 reports from `tasks/<dir>/reports/`.
2. Write a consolidated summary at
   `tasks/<dir>/reports/_summary.md` ranked HIGH / MEDIUM / LOW.
3. Issue findings to `paper/findings.md` via `research-capture` only if
   they're reusable observations; otherwise keep inside the task dir.
4. No paper edits from this skill.
5. `SendMessage` each reviewer `{type:"shutdown_request"}` and
   `TeamDelete`. Commit the task dir. Cite it in the commit body.
