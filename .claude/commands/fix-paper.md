# Fix Paper

Two-phase process to fix proof gaps and get referee review on a paper draft.

## Arguments

The user's arguments are: $ARGUMENTS

Parse the arguments as follows:
- If empty: fix `paper/paper9-petz-rh.tex` using the latest referee feedback in lore
- If a file path (e.g., `paper/paper1-nine-faces.tex`): fix that paper instead
- If `--no-referee`: fix only, skip Phase 2 referee review
- If `--referee-only`: skip Phase 1 fixes, just run referees on current state
- If specific issues listed (e.g., `epsilon exponent, GORZ remark, Paulsen citations`): fix only those issues
- Combinations work: `paper/paper3-grand-unification.tex epsilon exponent --no-referee`

## Context

Read ALL lore files in `/mnt/c/workspace/riemann/lore/`, especially:
- `20260319-referee-reports-and-next-fixes.md` — latest referee feedback and fix list
- `20260319-paper9-referee-readiness.md` — known issues
- `20260319-paper9-honest-reassessment.md` — honest assessment of claims

## Phase 1: Fix Team (3 agents)

Create a team called `paper-fix` and spawn three agents:

### 1. Operator Algebraist (`operator-algebraist`)
Expert in von Neumann algebras, CP maps, Schur multipliers, Bost-Connes system, Takesaki duality.
Handles: proof rigor for CP semigroup, trace positivity, spectral projection, Petz recovery arguments.
Reads the referee reports and fixes all operator algebra issues.

### 2. Analyst (`analyst`)
Expert in Riemann zeta, Mellin transforms, de Bruijn-Newman constant, explicit formula, zero-counting.
Handles: Mellin transform calculations, forward/backward heat flow, zero-free region bounds, analytical estimates.
Reads the referee reports and fixes all analytic number theory issues.

### 3. QI Expert (`qi-expert`)
Expert in Petz recovery, quantum Markov chains, SDP methods, entanglement, Fawzi-Renner.
Handles: SDP hierarchy computation, quantum Markov section, approximate recovery bounds, QI correctness.
Reads the referee reports and fixes all quantum information issues.

### Fix team instructions

Each agent should:
1. Read the paper and ALL lore files (especially referee reports)
2. Claim their tasks from the task list
3. Edit the paper directly using the Edit tool
4. Mark tasks complete when done
5. Send a summary to team-lead

Create tasks from the referee reports and/or user arguments. Common issues:
- Mathematical errors (wrong exponents, incorrect inequalities)
- Proof gaps (missing steps, unjustified claims)
- Incorrect citations
- Missing definitions
- Claims that need to be weakened or made conditional
- Missing numerical computations
- Notation inconsistencies

### Critical: Forward/backward heat flow

The CP semigroup S_t is FORWARD heat (smoothing, t > 0). De Bruijn's theorem applies to BACKWARD heat (dBN Ξ_λ, λ > 0). The correspondence is λ = -t/2. Any proof that cites de Bruijn for the forward-evolved ζ_t is WRONG. The Petz recovery map bridges forward to backward.

## Phase 2: Referee Team (2 agents)

After ALL fix tasks are complete, shut down the fix team and spawn two referees:

### 4. Pure Math Referee (`referee-math`)
Reviews as a referee for Communications in Mathematical Physics. Checks every proof, identifies gaps, circular reasoning, incorrect citations. Writes a formal referee report with verdict: accept, minor revision, major revision, reject.

### 5. Physics Referee (`referee-physics`)
Reviews as a referee for Letters in Mathematical Physics. Checks physical meaning, QI correctness, accessibility to both communities, computational actionability. Writes a formal referee report with verdict.

### Referee instructions

Each referee should:
1. Read the FULL paper after fixes
2. Read the previous referee reports in lore (to check if issues were addressed)
3. Write a complete referee report
4. Send the report to team-lead
5. Be ruthless but fair

## After completion

1. Commit the fixed paper
2. Write referee reports to lore
3. Summarize the verdicts to the user
