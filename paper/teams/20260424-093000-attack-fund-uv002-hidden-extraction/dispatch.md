# Dispatch

Date: 2026-04-24
Team slug: `uv002-hidden-extraction`

## Active queue

Primary queue is `UV-002`-first.

Current theorem order:

1. Exact fixed-shear / quotient-diagonal package theorem on the residual corner
   `\{S=0\}\cap\{K_v=0\}`.
2. Actual corrected edge-law theorem on good patches
   `J\Subset\{c\neq0, M\neq0\}`.
3. Reduced-`\widehat\Psi` coincidence / same reduced image germ at coincidence.
4. Hidden extraction theorem from finite-core package data to the first surviving
   odd coefficient of `H_m` or first nonzero `\Xi_{\zeta,\le H}^{(N)}`.
5. Full finite-core contradiction theorem.

## Non-goals

- Do not restart from the whole paper and summarize it.
- Do not drift into pair-like quantitative cleanup (`UV-009 -> UV-001 -> UV-008`).
- Do not search for a second primitive explicit pointwise highest-new field.
- Do not reopen queue-order conflicts unless you find a genuinely new theorem-level dependency.
- Do not spend effort on planar-only / endpoint-gap / three-run overlap work unless it directly supports one of the active theorem fronts.

## Self-deposit rule

Write your own provenance to your own agent dir under:

`paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/agents/<your-slug>/`

Required files:

- `report.md` using the 7-field schema from `CLAUDE.md`
- `scripts/` for anything you compute or test
- `notes/` for any scratch worth keeping

Do not write outside your own agent dir.

## Canonical context files to read first

- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/findings.md`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/uv.md`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md`
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md`
- `paper/tasks/20260424-090000-other-uv002-fundamental/reports/coordinator-current-convergence.md`

## Report reminder

Return exactly these fields in `report.md`:

- Claim
- Status
- Evidence
- Exact refs
- Dependencies
- Strongest objection
- Needed for promotion

End with `Honest verdict:`.
