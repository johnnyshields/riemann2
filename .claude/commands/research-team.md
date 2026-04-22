# Research Team (3+3+2)

Primary workhorse for a balanced research dispatch. Spawns \(\approx 8\)
named teammates via `TeamCreate` in a \(3+3+2\) roster: 3 gap-closers,
3 explorers, 2 verifiers. See `CLAUDE.md` §4 for the rationale; §5 for
task-dir conventions; §7 for the non-negotiable briefing rule.

## Arguments

The focus is: `$ARGUMENTS`

Parse:
- **empty** — general balance; coordinator picks 3 most-blocking UV items +
  3 broad explorer topics + 2 standard verifiers.
- **topic phrase** (e.g., `mixed 4-point`) — all gap-closers and at least
  one explorer oriented around the theme.
- **UV-NNN** — at least one gap-closer locked on that ID.

## Mandatory preamble (every run)

1. **Read the briefing packet** in full:
   - `paper/findings.md`
   - `paper/unverified.tex`
   - Current WIP labels: `grep -n 'rem:wip-' paper/proof_of_rh.tex`
   - Most recent 2–3 entries in `lore/`
2. **Choose the roster**. Write down upfront:
   - 3 gap-closers: each assigned a specific UV-NNN or `rem:wip-*` item,
     with target statement and routes A/B/C + fallback to "minimal finite
     reduction."
   - 3 explorers: each assigned one of {derivative geometry,
     fundamentals/normal forms, cross-cutting structure}.
   - 2 verifiers: `verifier-adversarial`, `verifier-source`.
3. **Create 3 sibling task dirs** with same timestamp prefix:
   - `tasks/<ts>-attack-gap-<slug>/`
   - `tasks/<ts>-attack-fund-<slug>/`
   - `tasks/<ts>-verify-<slug>/`
   where `<ts>` = `date +%Y%m%d-%H%M%S` and `<slug>` is the cycle theme
   (e.g., `mixed-4-point` or `general-<yyyymmdd>`). Inside each, create
   `reports/`, `scripts/`, `notes/` subdirs.
4. **Announce the task dir paths** before spawning any teammate.

## Spawn protocol

Use `TeamCreate` with `team_name: "research-team-<ts>"`, then spawn 8
named teammates. Each teammate's spawn prompt MUST contain:

- The full contents of `paper/findings.md` (pasted verbatim).
- The **7-field report schema** from `CLAUDE.md` §8.
- The **self-deposit checklist**: write the final report to
  `tasks/<role-dir>/reports/<teammate-name>.md`; scripts to
  `tasks/<role-dir>/scripts/`; do not write elsewhere.
- The **writing-discipline reminder** from `CLAUDE.md` §3a (three-bin
  separation, gap reduction over closure, scoped negation, caution-
  labeled synthesis, honest-verdict closure).
- The **briefing idioms** from `CLAUDE.md` §7a — paste the subset
  relevant to the teammate's role. In particular:
  - Every teammate: "`unsupported`, `blocked`, `no progress` are
    acceptable returns."
  - Gap-closers: "If full closure is too hard, reduce to the smallest
    list of concrete unresolved sub-statements." + "What is the
    cleanest target here?"
  - Explorers: "Separate observations into [confirmed] / [conditional]
    / [candidate] before merging."
  - Verifiers: "Give me the honest verdict." + "Qualify any
    impossibility claim with 'from [scope] alone.'"
- Explicit **non-goals** for this teammate (what NOT to pursue).
- The teammate's specific assignment:
  - Gap-closers: target label/UV-NNN, routes A/B/C, fallback to
    minimal finite reduction. **Per `CLAUDE.md` §7 exception**, paste
    the *specific* UV-NNN entry the closer is attacking — but no other
    UV entries. Do not share the full ledger.
  - Explorers: topic scope, reusable-artifact mandate (observations +
    candidate goodies + candidate negative findings). **No
    `unverified.tex` content at all** — explorers work against the
    verified state only.
  - Verifiers: read the 6 research reports once they land; flag
    circularity / missing hypotheses / overclaims / stale citations.
    The adversarial verifier may be shown specific UV entries that
    directly correspond to a reviewed report's claim; the source
    auditor may be shown UV entries whose `rem:wip-*` labels appear
    in the audited sections.

Teammate names (examples):
`gap-closer-uv002`, `gap-closer-mixed4pt`, `gap-closer-uv005`,
`explorer-deriv-geo`, `explorer-fundamentals`, `explorer-crosscut`,
`verifier-adversarial`, `verifier-source`.

## Collation (coordinator)

After teammates report:

1. Read every report from `tasks/<role-dir>/reports/*.md`.
2. Cross-check handbacks against the paper source they cite (open the
   `rem:wip-*` label or line range before trusting the claim).
3. Draft a **findings delta**:
   - New `Negative` entries from ruled-out routes (with `Do-not-retry:`).
   - New `Goodies` from reusable artifacts with exact `Location:`.
   - New `Open gaps` discovered.
4. Apply the delta via the `research-capture` skill (one call per entry)
   or by direct edit to `paper/findings.md`.
5. Update `paper/unverified.tex` (refine "Needed for promotion" fields,
   add new UV-NNN entries for newly surfaced claims).
6. Write a single lore entry: `lore/<yyyymmdd>-research-team-<slug>.md`
   summarizing the cycle outcome, which roles moved proof state, and
   which follow-ups are queued.
7. **Do not edit `paper/proof_of_rh.tex`** from this skill. Promotion is
   a separate deliberate coordinator step after review.

## Shutdown

`SendMessage` each teammate `{type:"shutdown_request"}`, then
`TeamDelete`. Commit the task dir contents + `findings.md` /
`unverified.tex` edits + lore entry in logical commits. Commit bodies
must name all three task dirs.
