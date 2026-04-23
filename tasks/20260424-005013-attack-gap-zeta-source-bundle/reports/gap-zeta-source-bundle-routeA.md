## Claim

Assuming the quotient/phase normalization has been fixed, the cleanest theorem-facing one-zero statement is this.

Let
\[
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}
\]
and fix the manuscript-facing normalized phase convention on a compact interval \(I\subset\mathbb R\) avoiding the real singularities from the gamma factor, trivial zeros, and pole terms by
\[
\phi\!\left(\tfrac12+it\right)=e^{2 i\Phi(t)},\qquad q(t):=\Phi'(t),
\]
so that
\[
\left(\frac{\phi'}{\phi}\right)\!\left(\tfrac12+it\right)=2q(t)
\]
on \(I\).

Let \(\rho=\beta+i\gamma\) be one nontrivial zero of \(\xi\), counted with multiplicity \(m_\rho\). Then the contribution of the pole of \(\phi\) at \(\rho/2\) and the zero of \(\phi\) at \((1+\rho)/2\) to the corrected phase derivative \(q\) is exactly
\[
m_\rho f_{\beta,\gamma}(t),
\]
where
\[
f_{\beta,\gamma}(t)=
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2}.
\]

Equivalently, after inserting the corrected normalization factor/sign,
\[
q_\rho(t)=\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)=f_{\beta,\gamma}(t),
\]
and for multiplicity \(m_\rho\) the contribution is \(m_\rho q_\rho(t)\).

This is the clean single-zero theorem candidate because it is exactly the atomic statement needed before summing over zeros, and it matches the manuscript kernel already used in the \(S(m)\) slot.

How it feeds the bundled compact-interval source theorem:

On the same singularity-free compact interval \(I\), the bundled theorem should then read
\[
q(t)=B_{\mathrm{src}}(t)+\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(t),\qquad t\in I,
\]
where \(B_{\mathrm{src}}\) is the unified background term coming from the gamma factor, trivial zeros, and polar bookkeeping. After identifying \(B_{\mathrm{src}}=B_\zeta=B_{\Aut}=B_{\bg}\), this gives the paper-facing split
\[
q(t)=B_\zeta(t)+S(t),\qquad S(m)=\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(m).
\]
So the one-zero theorem is the local summand theorem; the bundled compact-interval theorem is the summation/regularization theorem that places those summands into the manuscript's exact \(S(m)\) channel.

Separate three things.

Proved:
- The strip-edge identity
  \[
  \Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)=f_{\beta,\gamma}(t)
  \]
  is already safe as an algebraic single-zero kernel identity.
- Positivity of \(f_{\beta,\gamma}(t)\) for \(0\le \beta\le 1\) is already safe.
- The manuscript already uses the summed kernel formula for \(S(m)\) as the correct scalar shape.

Conditional on the fixed quotient/phase normalization:
- The one-zero source contribution theorem above is the right theorem-facing atomic statement.
- Summing those atomic contributions over zeros on a compact interval yields the bundled source theorem for \(q=B_\zeta+S\).

Missing:
- A canonical proof that the manuscript's \(q\) is exactly the phase derivative coming from the corrected quotient normalization.
- A compact-interval convergence or regularized summation theorem justifying the passage from one-zero contributions to the full summed source theorem.
- Explicit background identification and naming unification for \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\).
- An explicit multiplicity convention in the theorem statement and proof package.

Honest verdict: the clean one-zero theorem candidate is clear and stable once normalization is fixed, but it does not by itself close the source gap. The actual remaining work is the compact-interval summation/regularization and background-identification package.

## Status

conditional

## Evidence

The archived derivation gives the exact pole/zero bookkeeping for the quotient candidate
\[
\phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}
\]
and computes one nontrivial zero's logarithmic-derivative contribution as
\[
2f_{\beta,\gamma}(t)
\]
before dividing by the corrected bridge factor between \((\phi'/\phi)(\tfrac12+it)\) and \(q(t)\). After the quotient/phase normalization is fixed, the one-zero contribution to \(q\) is exactly \(f_{\beta,\gamma}(t)\), with multiplicity inserted linearly.

Independently, the strip-edge kernel note proves the same kernel identity directly at the level
\[
\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)=f_{\beta,\gamma}(t),
\]
which is the stable atomic content needed for the theorem candidate.

The current RH draft already exposes the manuscript-facing target slot through
\[
q(t)=B_\zeta(t)+S(t)
\]
and later the scalar formula
\[
S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m),
\]
but that slot is not yet canonically justified by a source theorem.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:14-25`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-22`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:32-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:29-56`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:27-46`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26364`

## Dependencies

- Corrected quotient object \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\).
- Corrected boundary phase/sign convention and exact bridge between \((\phi'/\phi)(\tfrac12+it)\) and \(q(t)\).
- Compact-interval summation or regularization for the zero contributions.
- Unified background bookkeeping for gamma/trivial/pole terms.
- Explicit multiplicity convention.

## Strongest objection

The one-zero formula is not the real bottleneck. The strongest objection is that the manuscript still lacks the theorem that identifies its own \(q\) with the corrected completed quotient on a singularity-free compact interval together with the summation/regularization step. Without that package, the statement remains a candidate atomic theorem, not a promoted source theorem.

## Needed for promotion

- Insert the corrected source-normalization package fixing quotient, phase sign, and the \((\phi'/\phi)\)-to-\(q\) bridge.
- State and prove the one-zero contribution theorem with multiplicity.
- State and prove the compact-interval summation or regularized source theorem.
- Identify \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\) as the same background term.
- Then promote the bundled theorem in paper-facing form
  \[
  q(t)=B_\zeta(t)+\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(t)
  \]
  and recover the manuscript scalar slot
  \[
  S(m)=\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(m).
  \]
