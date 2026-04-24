# Source audit for compact edge-difference inputs

## Theorem-ready input block

For the compact convergence lemma, state the inputs as follows.

Let \(\chi\) be a primitive nonprincipal Dirichlet character modulo \(q>1\), and
put
\[
a_\chi=\frac{1-\chi(-1)}{2}\in\{0,1\},
\qquad
\Lambda(s,\chi)=
\left(\frac{q}{\pi}\right)^{(s+a_\chi)/2}
\Gamma\left(\frac{s+a_\chi}{2}\right)L(s,\chi).
\]
Then:

1. \(\Lambda(s,\chi)\) is entire of order one.
2. It satisfies
   \[
   \Lambda(s,\chi)=\varepsilon(\chi)\Lambda(1-s,\overline{\chi}),
   \qquad |\varepsilon(\chi)|=1.
   \]
3. The paired function
   \[
   \Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\overline{\chi})
   \]
   is entire of finite order at most one and satisfies
   \(\Xi_\chi(s)=\Xi_\chi(1-s)\).
4. The zero multiset of \(\Xi_\chi\) is the union of the zero multisets of
   \(\Lambda(s,\chi)\) and \(\Lambda(s,\overline{\chi})\), with analytic
   multiplicities added at coincident zeros.
5. Since \(\Xi_\chi\) is entire of finite order at most one, its nonzero zeros
   \(\rho\), counted with multiplicity, satisfy
   \[
   \sum_{\rho\ne0}m_\rho|\rho|^{-2}<\infty,
   \]
   and a genus-one Hadamard product may be used. If \(0\) were a zero, it would
   be factored separately. For primitive nonprincipal \(\chi\), the functional
   equation plus \(L(1,\overline{\chi})\ne0\) gives \(\Lambda(0,\chi)\ne0\), so
   \(0\) is not a paired zero.

This is enough for Beauvoir's compact edge-difference proof. It does not supply
the explicit raw \(L\)-factor background split \(B_\chi^{\rm pair}\).

## Source map

- DLMF \(\S 25.15\) gives Dirichlet \(L\)-functions, primitive-character
  functional equation \(25.15.5\), the root-number definition \(25.15.6\), and
  the primitive trivial-zero discussion in \(\S 25.15(ii)\):
  https://dlmf.nist.gov/25.15
- Fungrim's Dirichlet \(L\)-function page gives a convenient formula database
  for the completed function, including the parity factor, the statement that
  \(\Lambda(s,\chi)\) is entire with limiting values at gamma-pole cancellation
  points, the Gauss-sum modulus, the functional equation, conjugation
  identities, and repeated-zero convention:
  https://fungrim.org/topic/Dirichlet_L-functions/
- Mathlib's `DirichletContinuation` page is a formalized check of analytic
  continuation and primitive functional equation, using `completedLFunction`,
  `gammaFactor`, `rootNumber`, and `IsPrimitive.completedLFunction_one_sub`:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/DirichletContinuation.html
- Khale, "An explicit Vinogradov-Korobov zero-free region for Dirichlet
  L-functions", arXiv:2210.06457, \(\S 2.1\), states the completed
  Dirichlet \(L\)-function preliminaries used here: nonprincipal entire
  continuation, parity \(a(\chi)\), completed function, primitive functional
  equation, entire order one, Hadamard factorization, trivial zeros, and
  multiplicity convention. It says these preliminaries are found in Davenport,
  `Multiplicative Number Theory`, 2nd ed. Use Khale as a locator; for a paper
  citation, replace it with the direct Davenport/Montgomery-Vaughan page.
  https://arxiv.org/abs/2210.06457
- MathWorld's Hadamard factorization theorem page records the general complex
  analysis input: finite-order entire functions have canonical products with
  zeros listed by multiplicity, and the rank condition gives convergence of
  \(\sum |a_n|^{-(p+1)}\). For an order-one function, genus at most one gives
  the required \(\sum |\rho|^{-2}<\infty\). For final paper use, cite a standard
  complex analysis text such as Conway or Krantz directly.
  https://mathworld.wolfram.com/HadamardFactorizationTheorem.html

## Special cases and exclusions

- Principal characters are excluded in this lane. The primitive principal case
  is the zeta case \(q=1\), where one must include \(s(s-1)\) or equivalent pole
  removal before applying an entire-function product.
- Nonprimitive characters are excluded. Imprimitive Euler factors can add zeros
  on \(\Re s=0\), which is outside the current primitive paired theorem target.
- Gamma poles and raw \(L\)-function trivial zeros are already canceled in the
  completed \(\Lambda(s,\chi)\), interpreted by limiting values. They re-enter
  only if Jason's \(B_\chi^{\rm pair}\) lane rewrites the source identity in raw
  \(L\)-factor components.
- A zero at \(\rho=0\) is not present for primitive nonprincipal \(\chi\), but
  the theorem statement may still say "nonzero zeros, with a separate finite
  zero-at-origin factor if present" for robustness.

## Source gaps

No mathematical input remains missing for the compact edge-difference
convergence lemma, provided the project accepts standard completed Dirichlet
\(L\)-function theory.

The remaining source-citation gap is bibliographic: for paper promotion, replace
the web-level citations for "entire of order one" and "Hadamard product for the
completed Dirichlet \(L\)-function" with exact textbook references, most likely
Davenport, `Multiplicative Number Theory`, 2nd ed., in the Dirichlet
\(L\)-function chapter, and a standard complex analysis text for Hadamard
factorization.
