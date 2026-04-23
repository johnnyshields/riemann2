## Claim

The cleanest theorem-facing statement after the quotient/phase normalization subsection is one bundled compact-interval source theorem, not separate paper-facing mini-theorems.

> **Theorem (Localized zeta source theorem on a compact interval).**
> Let
> \[
> \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}
> \]
> and let \(I\subset\mathbb R\) be a compact interval avoiding the real singularities coming from the gamma factor, trivial zeros, and pole terms. Assume the quotient/phase normalization subsection has fixed the manuscript phase by
> \[
> \phi\!\left(\tfrac12+it\right)=e^{2i\Phi(t)},
> \qquad q(t):=\Phi'(t),
> \qquad
> \left(\frac{\phi'}{\phi}\right)\!\left(\tfrac12+it\right)=2q(t)
> \]
> on \(I\).
> 
> Then there is a real-analytic background term \(B_{\mathrm{src}}(t)\) on \(I\), depending only on the gamma factor, trivial zeros, and polar bookkeeping, such that for every \(t\in I\),
> \[
> q(t)=B_{\mathrm{src}}(t)+\sum_{\rho} m_\rho f_{\beta_\rho,\gamma_\rho}(t),
> \]
> where the sum runs over the nontrivial zeros \(\rho=\beta_\rho+i\gamma_\rho\) of \(\xi\), counted with multiplicity \(m_\rho\), and
> \[
> f_{\beta,\gamma}(t)=
> \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
> +
> \frac{\beta}{\beta^2+(2t-\gamma)^2}.
> \]
> Equivalently, one zero \(\rho=\beta+i\gamma\) contributes exactly
> \[
> m_\rho f_{\beta,\gamma}(t)
> \]
> to \(q(t)\), and the compact-interval zero sum is understood as the regularized sum induced by the logarithmic derivative of \(\phi\); on any compact interval where the zero sum is absolutely convergent, this agrees with the ordinary sum.
> 
> Defining
> \[
> S(t):=\sum_{\rho} m_\rho f_{\beta_\rho,\gamma_\rho}(t),
> \]
> the theorem concludes the manuscript-facing split
> \[
> q(t)=B_\zeta(t)+S(t)
> \]
> after identifying \(B_{\mathrm{src}}\) with the paper's background notation in the scope used there.

This is the cleanest theorem-facing form because the draft first uses zeta-source data through the background-subtracted object \(q=B_\zeta+S\), not through an isolated one-zero formula.

## Status

conditional

## Evidence

Proved:

- The manuscript already places the source package exactly at the start of `\section{Zeta-side decomposition}` and first uses zeta-specific notation there via
  \[
  q(t)=B_\zeta(t)+S(t),
  \qquad
  S(m):=q_\zeta(m)-B_\zeta(m).
  \]
- The single-zero kernel shape already appears canonically in the tail section:
  \[
  f_{\beta,\gamma}(t)=
  \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
  +
  \frac{\beta}{\beta^2+(2t-\gamma)^2}.
  \]
- The draft already uses the summed scalar source slot
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
  \]
  later in the paper.
- The archived quotient derivation gives the exact compact-interval source identity template:
  \[
  q(t)=B_{\rm aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)
  \]
  on singularity-free compact intervals, with the one-zero contribution computed from the pole at \(\rho/2\) and zero at \((1+\rho)/2\).
- Prior focused attacks converged on the same granularity verdict: quotient/phase normalization should be one theorem-level unit, and everything downstream of it should be bundled into one localized source theorem with explicit clauses for one-zero contribution, compact-interval summation/regularization, background identification, and multiplicity.

Conditional:

- Once the quotient/phase normalization subsection fixes the sign convention so that
  \[
  \left(\frac{\phi'}{\phi}\right)\!\left(\tfrac12+it\right)=2q(t),
  \]
  the displayed theorem is the right paper-facing compact-interval statement.
- The one-zero contribution is the atomic clause inside that theorem, but it is not the theorem-facing endpoint by itself; the draft needs the summed background-subtracted source object immediately.
- The clean background label in the theorem should be a unified term such as \(B_{\mathrm{src}}\), identified in scope with the paper's \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\).

Missing:

- A canonical proof that the manuscript's \(q\) is the phase derivative attached to the corrected quotient normalization.
- A canonical compact-interval summation or regularization statement upgrading the one-zero formula to the full summed source theorem.
- A theorem-facing identification of the background notations \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\).
- An explicit multiplicity convention inside the source theorem.

Separate three things: the atomic kernel identity is essentially settled, the bundled theorem statement is stable conditional on the bridge, and the actual canonical gap is the bridge plus the compact-interval summation/background package.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-35`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-49`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-372`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1471-1505`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26326`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeA.md:3-49,62-72,117-142`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeB.md:5-10,24-43,55-73`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/verifier-adversarial-zeta-source-bundle.md:3-29,44-60,84-94`

## Dependencies

- The corrected quotient declaration \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\).
- The corrected boundary phase convention and exact bridge from \((\phi'/\phi)(1/2+it)\) to \(q(t)\).
- A compact-interval summation or regularization theorem for the zero contributions.
- A theorem-level identification of the background term used in the draft.
- An explicit zero multiplicity convention.

## Strongest objection

The main risk is overstating independence of the one-zero clause. From the draft's own first use of zeta-side source data, the paper does not need a free-standing local summand theorem; it needs the summed, background-subtracted compact-interval source object. So a theorem package split into several adjacent paper-facing mini-theorems would make the dependency structure look cleaner than it currently is. From this scope alone, the safe theorem-facing unit is one bundled compact-interval source theorem after the quotient/phase normalization bridge.

## Needed for promotion

- State and prove the quotient/phase normalization theorem first.
- Follow it immediately with one localized zeta-source theorem in the form stated above.
- Make the theorem conclude the manuscript-facing identity \(q=B_\zeta+S\) with exact compact-interval scope.
- Include, inside that theorem or its proof, the one-zero contribution, compact-interval summation/regularization, background identification, and multiplicity convention.

Honest verdict: the clean compact theorem is clear. Conditional on the quotient/phase bridge, it should be one bundled localized source theorem. The missing mathematics is not the one-zero kernel; it is the canonical bridge and the compact-interval summation/background identification package.
