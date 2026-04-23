## Claim

The cleanest source theorem one would want in the main paper is the following local completed-quotient statement for the zeta/scattering phase derivative.

**Would-be source theorem.** Let
\[
\phi(s):=\frac{\Lambda(2s-1)}{\Lambda(2s)}
\]
and let \(I\subset \mathbb R\) be a compact interval avoiding the real singularities coming from the archimedean, trivial-zero, and polar factors of \(\phi\). Choose a continuous phase \(\Phi\) on \(I\) by
\[
\phi\!\left(\tfrac12+it\right)=e^{-2 i\Phi(t)},
\qquad q(t):=\Phi'(t).
\]
Then on \(I\),
\[
q(t)=B_{\mathrm{aut}}(t)+\sum_{\rho} f_{\beta_\rho,\gamma_\rho}(t),
\]
where the sum runs over the nontrivial zeros \(\rho=\beta_\rho+i\gamma_\rho\) of \(\xi\),
\[
f_{\beta,\gamma}(t)=
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2},
\]
and \(B_{\mathrm{aut}}\) is the real-analytic background coming from the gamma factor, trivial zeros, and pole structure. Equivalently, each nontrivial zero contributes
\[
f_{\beta,\gamma}(t)=\Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right).
\]

This is the exact theorem that would justify the draft's zeta-side split \(q=B_\zeta+S\) and identify the local value scale \(S(m)\) as a positive strip-edge zero kernel.

## Status

open

## Evidence

Proved in the canonical draft:

- The paper defines the local phase kernel from a real phase \(\Phi\) and sets \(q(t):=\Phi'(t)\).
- The paper explicitly uses the zeta-side split
  \[
  q(t)=B_\zeta(t)+S(t)
  \]
  and the local bookkeeping refinement \(q=q_{\mathrm{loc}}+g_{\sm}+E_{\est}\).
- The paper defines the local value scale by
  \[
  S(m):=q_\zeta(m)-B_\zeta(m)
  \]
  and uses the curvature estimate \(|S''(m)|\ll L(m)S(m)^2\).
- The paper defines the omitted-zero tail using exactly the kernel
  \[
  f_{\beta,\gamma}(t)=
  \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
  +
  \frac{\beta}{\beta^2+(2t-\gamma)^2}
  \]
  and proves the tail curvature bound from this kernel model.
- The paper also proves a crude bound for
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m).
  \]

Archive provenance only:

- The archived chat gives the explicit completed quotient
  \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\), the phase normalization
  \(\phi(\tfrac12+it)=e^{-2i\Phi(t)}\), and the identity
  \(\partial_s\log\phi(\tfrac12+it)=2q(t)\).
- The archived derivation identifies the contribution of one nontrivial zero \(\rho\) to \(\partial_s\log\phi\) as a pole at \(\rho/2\) and a zero at \((1+\rho)/2\), yielding exactly
  \[
  2f_{\beta,\gamma}(t).
  \]
- From that source computation, the archive states the exact decomposition
  \[
  q(t)=B_{\rm aut}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)
  \]
  on compact intervals away from singularities.

Missing from the canonical draft:

- The paper does not yet state or prove the completed-quotient source theorem itself.
- The paper does not yet identify \(B_\zeta\) with a rigorously defined \(B_{\mathrm{aut}}\) arising from gamma, trivial-zero, and pole bookkeeping of \(\phi\).
- The paper does not yet prove inside the canonical draft that the same kernel used for tails is exactly the pointwise nontrivial-zero contribution to \(q\).

## Exact refs

- `paper/proof_of_rh.tex:149-160` for the phase kernel and `q(t):=\Phi'(t)`.
- `paper/proof_of_rh.tex:271-301` for the asserted zeta-side split `q(t)=B_\zeta(t)+S(t)`, the local split, `S(m):=q_\zeta(m)-B_\zeta(m)`, `L(m)`, and the curvature estimate.
- `paper/proof_of_rh.tex:345-369` for the omitted-zero tail `T_{\far}` built from `f_{\beta,\gamma}` and the tail curvature theorem.
- `paper/proof_of_rh.tex:26301-26364` for the crude polynomial bound on `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)`.
- `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598` for the candidate quotient, phase normalization, single-zero source computation, and exact decomposition.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/scattering_generalization.md:21-37` for the archive-provenance summary and the warning that this is not yet canonical.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/scattering_candidate_note.tex:69-92` for the same quotient candidate and the strict archive/canonical separation.

## Dependencies

- A local logarithmic-derivative formula for the explicit completed quotient \(\phi(s)=\Lambda(2s-1)/\Lambda(2s)\).
- A phase normalization lemma relating \(\phi(\tfrac12+it)\) and the paper's phase \(\Phi(t)\) with the correct sign and factor of \(2\).
- A local partial-fraction or Hadamard bookkeeping lemma separating nontrivial zeros from the archimedean, trivial-zero, and pole terms.
- Local convergence on compact intervals away from singularities, enough to justify the summed zero contribution and its differentiation at the level used by the theorem.

## Strongest objection

The current paper already uses the split \(q=B_\zeta+S\) and the kernel \(f_{\beta,\gamma}\), but that does not by itself prove the source theorem. The missing issue is not conceptual shape; it is exact normalization and bookkeeping. Until the canonical draft explicitly connects its \(\Phi\) and \(q\) to the completed quotient \(\phi\), identifies the background term from that quotient, and justifies the zero expansion on singularity-free compact intervals, the source theorem remains archive provenance rather than proved manuscript content.

## Needed for promotion

Smallest bookkeeping sub-statements:

- **(1) Quotient-phase normalization.** On any compact singularity-free interval \(I\), define a continuous branch of \(\Phi\) so that
  \[
  \phi\!\left(\tfrac12+it\right)=e^{-2i\Phi(t)}
  \]
  and prove
  \[
  \partial_s\log\phi\!\left(\tfrac12+it\right)=2q(t).
  \]

- **(2) Single-zero contribution identity.** For one nontrivial zero \(\rho=\beta+i\gamma\), prove that the corresponding denominator/numerator terms from \(\Lambda(2s)\) and \(\Lambda(2s-1)\) contribute
  \[
  2f_{\beta,\gamma}(t)
  \]
  to \(\partial_s\log\phi(\tfrac12+it)\), hence \(f_{\beta,\gamma}(t)\) to \(q(t)\).

- **(3) Background identification.** Bundle the remaining gamma, trivial-zero, and pole terms into a real-analytic function \(B_{\mathrm{aut}}(t)\) on \(I\), and identify this with the paper's background notation \(B_\zeta(t)\).

- **(4) Local summation justification.** State the compact-interval convergence / differentiation justification needed to pass from the single-zero identity to
  \[
  q(t)=B_{\mathrm{aut}}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t).
  \]

After these four items, the draft's existing uses of \(S(m)\), the tail kernel, and the curvature bookkeeping sit on a clean source theorem.

Honest verdict: the target theorem is clear and the archive already contains the right candidate formula, but the canonical paper still lacks the normalization-and-bookkeeping bridge that turns that candidate into a theorem. The gap is small in shape and specific in content, but it is still open.
