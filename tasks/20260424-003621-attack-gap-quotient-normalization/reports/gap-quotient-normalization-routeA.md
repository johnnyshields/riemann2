## Claim

The exact quotient/phase bridge is this.

Let

\[
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},\qquad s(t)=\tfrac12+it,
\]

and let \(I\subset\mathbb R\) avoid the real singularities of the quotient. If one chooses a continuous boundary phase by

\[
\phi(s(t))=e^{\sigma 2i\Phi(t)},\qquad \sigma\in\{+1,-1\},
\]

with manuscript variable \(q(t):=\Phi'(t)\), then

\[
\frac{d}{dt}\log \phi(s(t))=i\,\frac{\phi'}{\phi}(s(t))=\sigma 2i q(t),
\]

hence

\[
\boxed{\frac{\phi'}{\phi}\!\left(\tfrac12+it\right)=\sigma 2 q(t).}
\]

So:

1. if \(\phi(\tfrac12+it)=e^{2i\Phi(t)}\), then \((\phi'/\phi)(\tfrac12+it)=2q(t)\);
2. if \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\), then \((\phi'/\phi)(\tfrac12+it)=-2q(t)\).

For one zero \(\rho=\beta+i\gamma\), the quotient-log-derivative contribution is

\[
D_\rho(t):=\frac{1}{s(t)-\rho/2}-\frac{1}{s(t)-(1+\rho)/2},
\]

and

\[
\Re D_\rho(t)=2\left[
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+
\frac{\beta}{\beta^2+(2t-\gamma)^2}
\right]=2f_{\beta,\gamma}(t).
\]

Therefore the manuscript-positive kernel formula \(q=B_\zeta+\sum_\rho f_{\beta_\rho,\gamma_\rho}\) matches either of the following theorem-facing normalizations:

1. Manuscript-matching option: \(\phi(\tfrac12+it)=e^{2i\Phi(t)}\), \(q=\Phi'\), so \((\phi'/\phi)(\tfrac12+it)=2q(t)\).
2. Equivalent scattering-orientation option: keep \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\), but define manuscript \(q=-\Phi'\). Then again \((\phi'/\phi)(\tfrac12+it)=2q(t)\).

The current archive wording \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\) together with manuscript \(q=\Phi'\) does not give the claimed \(+2q\); it gives \(-2q\). The sign issue is therefore real. The factor-of-\(2\) is stable; the unresolved point is phase orientation.

The cleanest manuscript-facing choice is option 1, because `paper/proof_of_rh.tex` already fixes \(q=\Phi'\) in the abstract phase-kernel section and later uses the positive decomposition \(q=B_\zeta+S\).

## Status

open

## Evidence

Proved from current sources.

1. The manuscript fixes the abstract phase variable and defines \(q(t):=\Phi'(t)\).
2. The archive and `grh/` notes fix the quotient candidate \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\) and a boundary phase law on \(s=\tfrac12+it\).
3. The chain-rule bridge above is exact: along \(s(t)=\tfrac12+it\), one always has \(d_t\log\phi(s(t))=i(\phi'/\phi)(s(t))\).
4. For a single nontrivial zero \(\rho\), the quotient-log-derivative term is exactly
   \[
   D_\rho(t)=\frac{1}{\frac{1-\beta}{2}+i(t-\gamma/2)}-\frac{1}{-\frac{\beta}{2}+i(t-\gamma/2)},
   \]
   whose real part is \(2f_{\beta,\gamma}(t)\).
5. The manuscript kernel used later in the tail-curvature and `S(m)` formulas is precisely that positive strip-edge kernel \(f_{\beta,\gamma}\).

Conditional on the missing source theorem.

6. To conclude the manuscript identity \(q(t)=B_\zeta(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)\), one still needs the compact-interval source theorem that identifies manuscript \(q\) with the quotient phase, fixes the background term, and states the summation/regularization and multiplicity convention.
7. The archive's displayed `+2q` formula is consistent only after a sign flip in the phase convention or in the definition of \(q\).

Missing.

8. The canonical draft does not yet state which phase orientation is intended for the quotient source theorem.
9. The canonical draft does not yet state whether the single-zero formula is taken at the level of real parts of individual terms, or only after the symmetric zero sum is assembled.
10. The canonical draft does not yet unify the background names \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\) in this quotient normalization.

Three-bin separation.

- proved: the chain-rule sign/factor relation; the single-zero real-part kernel identity; the manuscript's abstract convention \(q=\Phi'\);
- conditional on the quotient source theorem: the full decomposition of manuscript \(q\) as background plus positive zero kernel;
- missing: a canonically fixed phase orientation and its theorem-level promotion.

## Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-372`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26314`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:64-80,153-162`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:14-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:26-63,81-123`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeA.md:60-109`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeB.md:42-93`

## Dependencies

- One canonical quotient-phase theorem fixing \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\) and the intended boundary orientation.
- One explicit convention relating the quotient phase variable to the manuscript phase variable \(\Phi\).
- One compact-interval summed log-derivative theorem, including multiplicities and regularization away from real singularities.
- One theorem-level identification of the residual background term.

## Strongest objection

The main objection is that the single-zero computation in the archive is written at the level of `real part`, while the advertised bridge is written as an identity for \((\phi'/\phi)(\tfrac12+it)\). Those are not interchangeable until the summation convention and symmetry of the zero set are stated carefully. So the present report resolves the sign/factor issue for the boundary normalization itself, but it does not by itself close the full source theorem.

## Needed for promotion

1. Choose one canonical normalization and state it without mixing sign conventions.
2. If the paper keeps \(q=\Phi'\), replace the archived boundary law by \(\phi(\tfrac12+it)=e^{2i\Phi(t)}\), or equivalently rename the boundary phase by \(\Phi\mapsto-\Phi\).
3. If the paper keeps the archived boundary law \(e^{-2i\Phi}\), then redefine the manuscript source variable as \(q=-\Phi'\) in the source theorem statement.
4. State the single-zero formula at the correct level: either `real part per zero` or `full symmetric sum`, then attach multiplicity and background conventions.

Honest verdict: the factor-of-\(2\) survives. The sign does not. With the archive's current boundary law `e^{-2i\Phi}` and the manuscript's current definition `q=\Phi'`, the exact bridge is `(\phi'/\phi)(1/2+it)=-2q(t)`, not `+2q(t)`. The cleanest manuscript-facing repair is to flip the boundary phase orientation and keep `q=\Phi'`.
