## Claim

The cleanest proof skeleton, after the quotient/phase normalization is fixed, is one ordered proof of a single bundled localized zeta source theorem on a compact singularity-free interval. The proof should run in this order.

1. **Normalization input.** Fix
   \[
   \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
   \qquad
   \phi\!\left(\tfrac12+it\right)=e^{2 i\Phi(t)},
   \qquad
   q(t):=\Phi'(t),
   \]
   so that on the interval under discussion
   \[
   \left(\frac{\phi'}{\phi}\right)\!\left(\tfrac12+it\right)=2q(t).
   \]
   This is the upstream normalization theorem, not part of the bundled source proof itself.

2. **Interval and singularity scope.** Fix a compact interval \(I\subset\mathbb R\) avoiding the real singularities coming from the gamma factor, trivial zeros, and polar terms. Record that on such an interval the archimedean/trivial/polar contribution is real-analytic.

3. **Log-derivative decomposition of the quotient.** Write
   \[
   \partial_s\log\phi(s)
   = \partial_s\log\Lambda(2s-1)-\partial_s\log\Lambda(2s).
   \]
   Split this into:
   - the nontrivial-zero contributions;
   - the gamma/trivial/pole contribution, bundled into a background term \(B_{\mathrm{src}}\).

4. **One-zero atomic calculation.** For one nontrivial zero \(\rho=\beta+i\gamma\) of \(\xi\), with multiplicity \(m_\rho\), compute the contribution to \((\phi'/\phi)(\tfrac12+it)\) from the pole at \(\rho/2\) and zero at \((1+\rho)/2\):
   \[
   m_\rho\left(\frac{1}{s-\rho/2}-\frac{1}{s-(1+\rho)/2}\right).
   \]
   Restrict to \(s=\tfrac12+it\), take the real part, and obtain
   \[
   2m_\rho f_{\beta,\gamma}(t),
   \]
   where
   \[
   f_{\beta,\gamma}(t)=
   \frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
   +
   \frac{\beta}{\beta^2+(2t-\gamma)^2}.
   \]
   Using the normalized bridge \((\phi'/\phi)(\tfrac12+it)=2q(t)\), conclude that one zero contributes exactly \(m_\rho f_{\beta,\gamma}(t)\) to \(q(t)\).

5. **Finite partial sums.** Sum the one-zero identity over a finite symmetric set of nontrivial zeros. This yields a finite identity
   \[
   q_N(t)=B_{\mathrm{src},N}(t)+\sum_{\rho\in \mathcal Z_N} m_\rho f_{\beta_\rho,\gamma_\rho}(t)
   \]
   on \(I\), where the background absorbs the non-nontrivial-zero terms and the truncation convention.

6. **Compact-interval passage to the limit / regularization.** Show that the finite identities admit a compact-interval limit in the intended regularized sense induced by the logarithmic derivative of \(\phi\). On intervals where the zero sum is absolutely convergent, note that this regularized sum agrees with the ordinary sum. This is the key summation step.

7. **Bundled theorem conclusion.** Deduce
   \[
   q(t)=B_{\mathrm{src}}(t)+\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(t),
   \qquad t\in I.
   \]

8. **Paper-facing identification.** Define
   \[
   S(t):=\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(t)
   \]
   and identify \(B_{\mathrm{src}}\) with the manuscript background notation in scope, so that the paper-facing split becomes
   \[
   q(t)=B_\zeta(t)+S(t).
   \]

9. **Immediate corollary used later in the draft.** At a midpoint \(m\in I\), recover
   \[
   S(m)=\sum_\rho m_\rho f_{\beta_\rho,\gamma_\rho}(m).
   \]

Separate three bins.

- **[confirmed] Proved or effectively settled already.**
  - The atomic kernel identity
    \[
    \Re\!\left(\frac{1}{1+2it-\rho}-\frac{1}{2it-\rho}\right)=f_{\beta,\gamma}(t)
    \]
    is effectively settled in the archive.
  - The paper already contains the phase-kernel framework \(q=\Phi'\), the manuscript-facing split \(q=B_\zeta+S\), the kernel shape \(f_{\beta,\gamma}\), and later uses the scalar slot \(S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)\).
  - The archive already contains the exact quotient-side derivation template for the one-zero calculation and the compact-interval bundled identity, modulo the sign normalization now corrected.

- **[conditional on the fixed normalization package] Stable proof route.**
  - Once the boundary convention is fixed to \(\phi(\tfrac12+it)=e^{2i\Phi(t)}\) with \((\phi'/\phi)(\tfrac12+it)=2q(t)\), steps 2--4 above are the clean atomic beginning of the proof.
  - The theorem-facing unit should be step 7 as one bundled compact-interval theorem, not separate paper-facing mini-theorems.

- **Missing fresh proof writing.**
  - A canonical paper proof of the compact-interval summation/regularization step in step 6.
  - A theorem-facing identification of \(B_{\mathrm{src}}\) with the manuscript notations \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\).
  - An explicit multiplicity convention in the theorem statement and proof.

## Status

open

## Evidence

Proved in the paper already.

- The paper defines the abstract phase kernel and sets \(q(t)=\Phi'(t)\).
- The paper already first introduces zeta-side source data through
  \[
  q(t)=B_\zeta(t)+S(t)
  \]
  and later uses
  \[
  S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m).
  \]
- The kernel profile \(f_{\beta,\gamma}\) already appears in the tail-curvature section, so the paper's downstream local estimates already use the right scalar source shape.
- The paper also contains the later background notation \(B_{\bg}\), so the remaining issue is theorem-level source identification rather than invention of new objects.

Effectively in the archive already.

- The chat archive gives the quotient-side proof template: decompose \(\partial_s\log\phi\), isolate one nontrivial zero, compute the pole-zero difference, take the real part, and then sum over zeros on a compact singularity-free interval.
- The recent bundle notes sharpen the safe granularity: first fix quotient/phase normalization, then prove one bundled localized source theorem, with background identification and multiplicity handled inside or immediately after that theorem.
- The recent normalization note fixes the sign issue: to keep the manuscript normalization \(q=\Phi'\) and a positive split \(q=B_\zeta+S\), the clean boundary convention is
  \[
  \phi\!\left(\tfrac12+it\right)=e^{2i\Phi(t)}.
  \]

Missing fresh proof writing.

- The paper does not yet contain the compact-interval passage from the one-zero atomic identity to the full bundled theorem in a canonical theorem-proof block.
- The paper does not yet explicitly identify the three background names \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\) as one scoped background object.
- The paper-level zero sums do not yet visibly carry a multiplicity convention at the source theorem insertion point.

Honest proof-state separation.

- **proved:** paper-level downstream use of \(f_{\beta,\gamma}\), the manuscript-facing slot \(q=B_\zeta+S\), and the later scalar slot \(S(m)\).
- **conditional on the normalization theorem:** the ordered bundled proof route above, especially the one-zero computation and bundled compact-interval theorem statement.
- **missing:** theorem-proof writing for the compact-interval summation/regularization and scoped background identification.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-32`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-39`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-37`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:149-160`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-299`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:345-372`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1471-1505`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26326`
- `/mnt/c/workspace/riemann2/paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:5528-5598`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeA.md:3-34,60-78,91-107`
- `/mnt/c/workspace/riemann2/tasks/20260423-192522-attack-gap-zeta-source-theorem/reports/gap-zeta-source-routeB.md:3-20,42-57,73-91`
- `/mnt/c/workspace/riemann2/tasks/20260424-005013-attack-gap-zeta-source-bundle/reports/gap-zeta-source-bundle-routeA.md:3-49,62-72,117-142`
- `/mnt/c/workspace/riemann2/tasks/20260424-015132-attack-gap-compact-source-bundle/reports/gap-compact-source-bundle-routeA.md:3-45,54-98,114-131`

## Dependencies

- The corrected quotient declaration
  \[
  \phi(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)}.
  \]
- The corrected boundary phase convention and bridge
  \[
  \phi\!\left(\tfrac12+it\right)=e^{2i\Phi(t)},
  \qquad
  \left(\frac{\phi'}{\phi}\right)\!\left(\tfrac12+it\right)=2q(t).
  \]
- A compact-interval summation or regularization argument for the zero contributions.
- A scoped theorem-level identification of the background term used in the paper.
- An explicit multiplicity convention for all source sums.

## Strongest objection

The proof skeleton is clean only after the normalization package is treated as already fixed. From the current paper alone, the real unresolved mathematical step is not the one-zero kernel identity; it is the compact-interval passage from that atomic identity to the full bundled theorem in exactly the manuscript-facing normalization. If that step is written vaguely, the proof will look shorter than it is. A second risk is notation laundering: without an explicit scoped identification of \(B_\zeta\), \(B_{\Aut}\), and \(B_{\bg}\), the theorem may appear to conclude the existing paper notation without actually proving the identification.

## Needed for promotion

- Write the bundled theorem proof in the step order above: interval scope, quotient log-derivative split, one-zero calculation, finite partial sums, compact-interval limit/regularization, theorem conclusion, background identification, scalar corollary.
- Keep the one-zero clause inside the bundled proof package rather than promoting it as the main theorem-facing endpoint.
- State multiplicities explicitly in the theorem and in the compact-interval summation step.
- Identify the background term in scope so the theorem really concludes
  \[
  q(t)=B_\zeta(t)+S(t).
  \]
- Keep the proof-state labels honest: downstream paper uses are already present, the route is stable conditional on normalization, and the missing fresh writing is the compact-interval summation/background package.

Honest verdict: the proof skeleton is now sharp and localized. After the normalization fix, the clean route is one bundled compact-interval theorem. The remaining real writing is the compact-interval summation/regularization and explicit background identification, not the atomic one-zero computation.
