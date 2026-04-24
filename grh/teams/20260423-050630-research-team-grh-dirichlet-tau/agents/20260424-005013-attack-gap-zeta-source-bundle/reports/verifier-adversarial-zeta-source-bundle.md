## Claim

The post-bridge source-bundle conclusion is only partially safe as currently phrased. After the quotient / phase normalization bridge is repaired, the paper-facing package should be stated at **two theorem-level layers**, not three independent theorem-level components:

1. a quotient / phase normalization theorem;
2. one localized zeta-source theorem on singularity-free compact intervals, with explicit internal clauses for:
   - the one-zero source kernel;
   - compact-interval summation / regularization;
   - identification of the background term in the scope actually used;
   - the zero multiplicity convention.

So the theorem bundling is **not yet stated at the right granularity** if it is described as three theorem-level parts plus two convention items. The one-zero piece is a valid atomic ingredient, but it is not yet a safely independent paper-facing theorem because the draft first uses the source package through
\[
q(t)=B_\zeta(t)+S(t),\qquad S(m):=q_\zeta(m)-B_\zeta(m),
\]
and those uses already depend on background identification and on a summed source theorem, not merely on the atomic kernel formula.

The strongest safe patch-plan sentence now is:

> After the quotient / phase normalization theorem, insert one localized zeta-source theorem on singularity-free compact intervals that concludes the manuscript-facing split \(q=B_\zeta+S\) and includes, as explicit clauses, the one-zero source formula, the compact-interval summation / regularization step, the identification of the background term, and the zero multiplicity convention.

Claims that need scoped weakening:

- `three theorem-level components plus two explicit identification/convention items` should be weakened to `five required ingredients, but only two safe theorem-level units`;
- any sentence suggesting the post-bridge remainder is only notation or bookkeeping should be ruled out from this scope alone;
- the route-A statement that the one-zero theorem is `clear and stable once normalization is fixed` should be weakened to the atomic algebraic kernel identity being clear, while the paper-facing source theorem remains blocked by summation / regularization and background identification;
- any statement that the bundled theorem already yields the manuscript's exact `S(m)` channel should be scoped as conditional on proving the compact-interval source theorem and the background identification in the same package.

Honest verdict: keep the bridge separate, but bundle everything downstream of it into one localized source theorem. The present three-part theorem-level wording is still too fragmented for the actual dependency structure.

## Status

conditional

## Evidence

Proved:

- The draft first enters zeta-specific source data at `paper/proof_of_rh.tex:273-299`, where it already writes `q=B_\zeta+S`, introduces `g_{\sm}:=B_{\Aut}+T_{\far}`, and defines `S(m):=q_\zeta(m)-B_\zeta(m)`. This means the first paper-facing use is not a bare one-zero formula; it already mixes the source sum with background subtraction and naming (`paper/proof_of_rh.tex:273-299`).
- Later the same bookkeeping reappears with `B_{\bg}` in the fixed-core decomposition, confirming that the background term is not yet theorem-level unified in the draft (`paper/proof_of_rh.tex:1471-1490`).
- The zeta-source package note already says only quotient / phase normalization is cleanly first and that the single-zero formula, compact-interval summation, background identification, and multiplicity are safer proved together after that bridge is fixed (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:20-30`).
- The patch-plan note places the needed insertion exactly at the start of `\section{Zeta-side decomposition}` and lists five required ingredients there (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-12,23-31`).

Conditional on the bridge repair:

- The quotient note shows the factor-of-2 is not the issue; the real issue is the sign / phase convention, and until that package is fixed, statements around `q=B_\zeta+S` should be treated as manuscript notation rather than a normalized source theorem (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-22,41-49`).
- Route A safely isolates the atomic kernel identity
\[
\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)=f_{\beta,\gamma}(t),
\]
but its own `Missing` section still requires the normalization package, compact-interval summation / regularization, background identification, and multiplicity convention before promotion (`tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeA.md:53-72,125-142`).
- Route B correctly observes that the draft's actual `S(m)` channel is only paper-usable after the sum, background term, and multiplicity are stated together; otherwise the one-zero theorem does not yet justify the object later used (`tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeB.md:37-43,67-75`).

Missing:

- A canonical theorem proving the manuscript's own `q` is the phase derivative attached to the corrected quotient / phase normalization.
- A compact-interval summation or regularized source theorem that turns the atomic one-zero contribution into the paper-facing summed source term.
- A theorem-facing identification of `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` in the scope needed by the draft.
- An explicit multiplicity convention inside the same source theorem package.

## Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1471-1490`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26326`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeA.md:53-72`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeA.md:125-142`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeB.md:37-43`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeB.md:67-75`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:617-657`

## Dependencies

- Corrected quotient declaration `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`.
- Corrected boundary phase convention and exact bridge between `(\phi'/\phi)(1/2+it)` and `q(t)`.
- Compact-interval summation or regularization of the one-zero source contributions.
- Explicit identification of the background term in the scope actually used by the draft.
- Explicit zero multiplicity convention.

## Strongest objection

The strongest objection is that the current `three theorem-level components plus two convention items` language still describes the package by ingredients rather than by actual proof dependencies. From the draft's own first use of zeta-source data, the one-zero formula is not independently paper-usable: the manuscript immediately needs a background-subtracted summed source object. So treating the one-zero formula and the summation / regularization step as separate theorem-level units would overstate independence from this scope alone.

## Needed for promotion

- State the quotient / phase normalization theorem first and fix the sign convention there.
- Immediately follow it with one localized zeta-source theorem on singularity-free compact intervals.
- Make that theorem conclude the manuscript-facing identity `q=B_\zeta+S` with exact scope.
- Include explicit clauses for the one-zero contribution, compact-interval summation / regularization, background identification, and multiplicity convention.
- Weaken existing paper-facing summary language so that the one-zero formula is described only as an atomic ingredient unless and until the full bundled theorem is proved.
