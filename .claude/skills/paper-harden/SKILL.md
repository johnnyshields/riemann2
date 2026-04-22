---
name: paper-harden
description: Read-only 4-agent quality review of paper/proof_of_rh.tex — rigor, consistency, formatting, voice. Reviewers return reports only; the coordinator consolidates.
---

# Paper Harden

Four-angle read-only quality review.

## Preamble

Read `findings.md` (especially Negative + Recurring-open-gaps, for
overclaim detection). Create `tasks/<ts>-audit-harden-<slug>/` with
`reports/`, `scripts/`, `notes/`. `<slug>` may be `post-referee`,
`pre-submission`, or generic.

## Dispatch

`TeamCreate team_name: "paper-harden-<ts>"`. Spawn four reviewers with
the standard briefing and non-goal "report only, do not edit the
paper." Only `reviewer-rigor` additionally receives full
`unverified.tex` (for overclaim detection — narrow exception); the
others do not.

- **`reviewer-rigor`** — every claim justified, every hypothesis
  present, theorem-vs-proof match, no handwaving. Cross-checks
  `findings.md` Negative for silently-retried dead ends and
  `unverified.tex` for claims that should be quarantined but aren't.
- **`reviewer-consistency`** — notation consistency, stale renames,
  label/ref integrity, abstract/intro/conclusion counts match, frozen-
  macro compliance.
- **`reviewer-formatting`** — compile warnings, undefined refs,
  multiply-defined labels, substantive overfull/underfull boxes,
  `\texorpdfstring` on math-in-titles, bibliography consistency.
- **`reviewer-voice`** — AI tells ("it is worth noting,"
  "interestingly," "we leverage / utilize / employ"), templated-remark
  patterns, voice switches within paragraphs, marketing language,
  overclaims. Rank HIGH / MEDIUM / LOW.

## Post-cycle

Verify deposits. Write `reports/_summary.md` ranked HIGH / MEDIUM /
LOW. Issue reusable observations into `findings.md` via
`research-capture`; otherwise keep in the task dir. No paper edits.
Shut down, `TeamDelete`, commit with the task dir named.
