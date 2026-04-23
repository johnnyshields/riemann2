## Claim

The sign diagnosis is correct in the narrow adversarial sense that the current archive normalization

\[
\phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)},\qquad q(t):=\Phi'(t)
\]

does **not** imply

\[
\partial_s\log\phi\!\left(\tfrac12+it\right)=2q(t).
\]

It implies

\[
\frac{d}{dt}\log\phi\!\left(\tfrac12+it\right)=-2i q(t)
= i\,\partial_s\log\phi\!\left(\tfrac12+it\right),
\]

hence

\[
\boxed{\partial_s\log\phi\!\left(\tfrac12+it\right)=-2q(t).}
\]

So the factor of \(2\) is stable, but the sign in the archive display is wrong under the stated convention. The strongest safe patch-plan sentence now is:

`Add a front-loaded zeta-source normalization subsection that names \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\), fixes one boundary-phase orientation compatible with the manuscript variable \(q=\Phi'\), and states only conditionally that after this convention is fixed and the compact-interval source theorem is proved, the zero contribution is represented by the positive strip-edge kernel in the source split \(q=B_\zeta+S\).`

The claims that need scoped weakening are the ones that presently treat this normalization as already established rather than as a missing source theorem: the opening sentence of `\section{Zeta-side decomposition}`, the definition of `S(m)` through `q_\zeta`, the sentence calling the curvature bound the `fundamental zeta-side analytic estimate`, and downstream statements that use `S(m)` as an exact leading source scalar without an explicit conditional dependency on the source-normalization package.

## Status

proved

## Evidence

Proved.

1. The manuscript fixes the abstract phase convention `q(t):=\Phi'(t)` in the local kernel section. This is the manuscript-wide meaning of `q` before any zeta specialization.
2. The archive then states `\phi(\tfrac12+it)=e^{-2i\Phi(t)}` and also states `q=\Phi'=-\delta'`.
3. Along `s(t)=\tfrac12+it`, one has the exact chain rule
   \[
   \frac{d}{dt}\log\phi(s(t))=i\,\partial_s\log\phi(s(t)).
   \]
4. Differentiating the stated boundary law gives
   \[
   \frac{d}{dt}\log\phi\!\left(\tfrac12+it\right)=-2i\Phi'(t)=-2iq(t),
   \]
   so necessarily
   \[
   \partial_s\log\phi\!\left(\tfrac12+it\right)=-2q(t).
   \]
5. Therefore the archive sentence `\partial_s\log\phi(\tfrac12+it)=2q(t)` is incompatible with its own displayed boundary law unless one also flips the phase orientation or redefines the source variable by `q=-\Phi'`.
6. The single-zero computation itself gives only that the real part of one quotient-log-derivative term equals `2f_{\beta,\gamma}(t)`. That supports the positive strip-edge kernel at the level of real parts, but it does not by itself repair the sign mismatch in the boundary normalization.

Conditional on the missing source theorem.

7. The manuscript identity `q=B_\zeta+S` is still a reasonable target after a convention choice, but only after one theorem fixes the quotient, the boundary orientation, the level at which the single-zero formula is taken, the compact-interval summation/regularization, the background identification, and the multiplicity convention.
8. Downstream uses of `S(m)` as the exact source coefficient are therefore usable only conditionally on that package; they are not yet justified as unconditional retrospective descriptions of the present draft.

Missing.

9. The canonical paper does not yet state which orientation is intended: either `\phi(\tfrac12+it)=e^{2i\Phi(t)}` with `q=\Phi'`, or `\phi(\tfrac12+it)=e^{-2i\Phi(t)}` with source variable `q=-\Phi'`.
10. The canonical paper does not yet state whether the source formula is asserted termwise after taking real parts, or only after assembling the symmetric zero sum plus background.
11. The manuscript still mixes `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`, and still uses an isolated `q_\zeta` in the definition of `S(m)`.

Three-bin separation.

- proved: the chain-rule sign diagnosis; the stability of the factor `2`; the need to weaken route B's displayed normalization claim.
- conditional on one source-normalization theorem: the clean manuscript-facing split `q=B_\zeta+S` with positive strip-edge source kernel.
- missing: a canonical orientation choice, the correct theorem level for the single-zero formula, and unified background notation.

## Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1483-1505`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1529-1546`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2050-2087`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5519-5598`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:16-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-38`
- `/mnt/c/workspace/riemann2/tasks/20260424-003621-attack-gap-quotient-normalization/reports/gap-quotient-normalization-routeA.md:11-17,49-57,76-91,121-126`
- `/mnt/c/workspace/riemann2/tasks/20260424-003621-attack-gap-quotient-normalization/reports/gap-quotient-normalization-routeB.md:1-4,16-19,31-40,69-78`

## Dependencies

- One canonical quotient / phase normalization theorem for `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`.
- One explicit convention connecting the manuscript phase variable to the chosen boundary orientation.
- One precise source theorem saying whether the positive kernel is obtained from termwise real parts or from the full symmetric zero sum after regularization.
- One unified identification of `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`.
- One explicit multiplicity convention.

## Strongest objection

The strongest objection to promoting even the corrected sign statement into a larger manuscript conclusion is that the single-zero computation is only a real-part identity for one quotient-log-derivative term, while the manuscript wants an exact source split for `q`. Those are not interchangeable from current paper scope alone. So the sign diagnosis is solid, but the positive-kernel source formula still requires a scoped theorem statement and cannot yet be treated as already canonically installed.

## Needed for promotion

1. Pick one normalization and state it without mixing orientation conventions.
2. If the paper keeps `q=\Phi'`, replace the archive-facing boundary law by `\phi(\tfrac12+it)=e^{2i\Phi(t)}` or rename the source phase by `\Phi\mapsto-\Phi` before differentiation.
3. If the paper keeps `\phi(\tfrac12+it)=e^{-2i\Phi(t)}`, then the source variable in that theorem must be `-\Phi'`, not the manuscript's already-fixed `q=\Phi'`.
4. Weaken manuscript-facing claims meanwhile: replace unconditional wording like `Write the zeta/scattering phase derivative as ...` by scoped wording such as `Assuming the source-normalization package, write ...`, and similarly qualify the later uses of `S(m)` as depending on that package.
5. State the single-zero contribution at the correct level and then attach the compact-interval summation, background identification, and multiplicity convention in the same source subsection.

Honest verdict: the sign diagnosis is correct and route B is not safe as written. The stable conclusion now is only that one canonical source-normalization subsection is needed, and until it exists the manuscript should not speak as if the quotient-phase identification and the exact `q=B_\zeta+S` source split were already proved.
