---
name: research-attack
description: Small-cycle variant of research-team. 1-2 gap-closers + 1 verifier for a focused push on one UV-NNN or rem:wip-* target. Cheaper than the 3+3+2 full cycle.
---

# Research Attack

Focused push on one gap. 1 gap-closer + 1 adversarial verifier by
default; `--double` for 2 gap-closers on different routes.

`$ARGUMENTS`: `UV-NNN`, `rem:wip-<label>`, or free text (coordinator
resolves to the best match). Optional `--double`.

## Preamble

Read `findings.md`, the target's UV entry, and the paper region around
the target's `rem:wip-*` label (±200 lines). Create
`<paper>/teams/<ts>-attack-gap-<slug>/` where `<slug>` = UV-ID or short
descriptor.

## Dispatch

`TeamCreate team_name: "research-attack-<ts>"`. Spawn:

- **Gap-closer(s)** — `gap-<slug>` (or `-routeA` / `-routeB` under
  `--double`). Briefing: full `findings.md`, the specific UV entry
  verbatim (narrow exception to no-`unverified.tex`-sharing), the
  target in cleanest form, routes A/B/C, 7-field schema,
  writing-discipline reminder, self-deposit checklist. Paste the
  fallback idiom: "If full closure is too hard, reduce to the smallest
  list of concrete unresolved sub-statements."
- **`verifier-adversarial`** — same briefing skeleton plus the UV entry
  (narrow adversarial exception). Waits for the gap-closer(s) to
  deposit, then attacks. Paste: "Give me the honest verdict." "Qualify
  any impossibility claim with 'from [scope] alone.'"

Non-goals (coordinator-synthesized): no adjacent UVs, no re-proving
closed lemmas, no new conjectures outside scope.

## Post-cycle

Verify every report deposited; chase missing. Read all reports,
cross-check against cited paper lines. Update the UV entry (refine
`Needed for promotion`, or close it if the verifier confirmed). Call
`research-capture` for any new findings. No `proof_of_rh.tex` edits.

Shut down, `TeamDelete`, commit with the team dir named and UV-NNN in
the subject.
