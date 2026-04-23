## Claim

The clean canonical source theorem candidate is:

> Let
> \[
> \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}
> \]
> and let \(I\subset \mathbb R\) be compact and avoid the real singularities coming from the gamma factor, trivial zeros, and pole terms. Choose a continuous phase branch \(\Phi\) on \(I\) such that
> \[
> \phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)},
> \qquad q(t):=\Phi'(t).
> \]
> Then for every \(t\in I\),
> \[
> q(t)=B_{\Aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t),
> \]
> where the sum runs over nontrivial zeros \(\rho=\beta_\rho+i\gamma_\rho\) of \(\xi\), counted with multiplicity, and
> \[
> f_{\beta,\gamma}(t)=
> \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
> +
> \frac{\beta}{\beta^2+(2t-\gamma)^2}.
> \]
> In particular, after identifying \(B_\zeta=B_{\Aut}\), the manuscript split
> \[
> q(t)=B_\zeta(t)+S(t)
> \]
> is justified with
> \[
> S(t)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(t).
> \]

This is the smallest canonical theorem that upgrades the archive quotient formula into paper-level language. It says exactly what object the manuscript phase comes from, what the background term is, and what the zero source term is.

## Status

open

## Evidence

Proved in the paper now:

- The manuscript already fixes the abstract phase-kernel setup with \(q(t)=\Phi'(t)\).
- The manuscript already states the decomposition \(q(t)=B_\zeta(t)+S(t)\).
- The kernel profile
  \[
  f_{\beta,\gamma}(t)=
  \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
  +
  \frac{\beta}{\beta^2+(2t-\gamma)^2}
  \]
  already appears in the tail-curvature section.
- The manuscript also uses the zero-sum formula
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)
  \]
  as a standalone source-level input.

Archive provenance:

- The chat archive gives the exact quotient candidate
  \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\).
- It also gives the phase convention
  \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\), the single-zero pole/zero bookkeeping, and the factor-of-\(2\) identity
  \(\partial_s\log\phi(\tfrac12+it)=2q(t)\).
- From that archived calculation one gets the exact source decomposition
  \(q(t)=B_{\Aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)\)
  on compact singularity-free intervals.

Missing in the canonical paper:

- The paper does not yet identify its own phase derivative \(q\) with the specific quotient \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\).
- The branch, sign, and factor-of-\(2\) normalization are not yet proved in the canonical draft.
- The paper has not yet unified the background names \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\) into one theorem-level object.
- The convergence / regularization statement needed to pass from single-zero contributions to the full compact-interval sum is not yet presented as a theorem.

The safe boundary is therefore: kernel theorem proved; source theorem still conditional.

## Exact refs

- `paper/proof_of_rh.tex:149-160` defines the phase kernel and \(q(t)=\Phi'(t)\).
- `paper/proof_of_rh.tex:273-287` states \(q(t)=B_\zeta(t)+S(t)\) and \(S(m)=q_\zeta(m)-B_\zeta(m)\).
- `paper/proof_of_rh.tex:345-355` gives the single-zero kernel profile \(f_{\beta,\gamma}(t)\).
- `paper/proof_of_rh.tex:1471-1490` uses the background notation \(B_{\bg}\) inside the local/far decomposition.
- `paper/proof_of_rh.tex:26301-26314` states \(S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)\) as an input formula.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-40` gives the current safe boundary and the conditional checklist.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:32-63` records essentially the same candidate theorem in working-note form.
- `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598` gives the quotient object, phase convention, single-zero calculation, and exact source decomposition.

## Dependencies

- A canonical definition of the zeta/scattering quotient \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\).
- A proof that the manuscript phase satisfies \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\) on compact singularity-free intervals, with the correct branch/sign normalization.
- A theorem turning the single-zero logarithmic-derivative calculation into the full compact-interval sum, including multiplicities and regularity away from singularities.
- A notation identification showing which background object in the paper equals the quotient-side background term.

## Strongest objection

The candidate theorem is not promotable yet because the canonical draft still treats the source split as abstract manuscript notation, not as a proved consequence of the specific quotient \(\Lambda(2s-1)/\Lambda(2s)\). The archive calculation is strong provenance, but until that identification and normalization are written in the paper, the theorem-facing statement remains conditional. A second obstruction is notation drift: \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\) are not yet theorem-level unified objects, and even \(q_\zeta\) appears in the definition of \(S(m)\) without a nearby canonical source theorem fixing that symbol.

## Needed for promotion

- State the quotient object and phase convention canonically: \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\), \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\), \(q=\Phi'\).
- Prove the branch/sign/factor-of-\(2\) identity \(\partial_s\log\phi(\tfrac12+it)=2q(t)\).
- Promote the single-zero source identity with multiplicity convention, then sum it on compact intervals avoiding singularities.
- Identify the background term canonically so that \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\) are one theorem-level object or are explicitly related.

Honest verdict: there is a clean paper-level source theorem candidate, and the archive already supplies a credible derivation template. But the canonical gap is real: the missing step is the quotient-phase identification theorem itself, not merely cleanup of gamma or trivial-zero bookkeeping.
