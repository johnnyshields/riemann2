# UV-026 Mixed-Order Filtration Candidate

## Candidate

For an affine-removed scalar source germ
\[
r(t)=\sum_{k\ge2}\frac{r^{(k)}(m)}{k!}(t-m)^k,
\]
define the exact mixed-order homogeneous projection by
\[
\operatorname{Gr}_a r(t)
:=
\frac{r^{(a+2)}(m)}{(a+2)!}(t-m)^{a+2}.
\]
Thus \(\operatorname{Gr}_1 r\) is the \(r^{(3)}(m)\) Taylor monomial and
\(\operatorname{Gr}_5 r\) is the \(r^{(7)}(m)\) Taylor monomial.

This is not proved in the paper.  It is a theorem candidate consistent with
the displayed pre-\(\Phi_K\) same-point and mixed block formulas if UV-026
finite grade means lowest ordinary-\(z\) order of the source-linear
pre-whitening matrix input.

## Compatibility Check

For a scalar Taylor monomial of order \(k\):

- \(d=r(t_\pm)\) starts at \(z^k\);
- \(e=r'(t_\pm)\) starts at \(z^{k-1}\);
- \(g=r''(t_\pm)\) starts at \(z^{k-2}\);
- \(\eta=\int_{t_+}^{t_-}r(u)\,du\) starts at \(z^{k+1}\) when \(k\) is even
  and vanishes when \(k\) is odd.

The same-point source-linear input has
\[
\delta G_{11}\sim d,\qquad
\delta G_{12}\sim e,\qquad
\delta G_{22}\sim g+\text{baseline}\cdot d,
\]
so its lowest possible order is \(k-2\), through the \(g\) term.

The scaled mixed input \(M=\mathfrak D_Q\delta N\) has a lowest possible
\((2,2)\)-entry contribution \(d/s^2\), hence also starts in order \(k-2\).
For even \(k\), the \(\eta/s^3\) contribution lands in the same order; for odd
\(k\), \(\eta\) vanishes but the \(d/s^2\) channel remains.

Therefore the candidate \(\operatorname{Gr}_a r\) supplies both:
\[
\delta G_{i,\pm}^{\lin,[a]},
\qquad
M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})
\]
with the same lowest finite order \(a\).

## Objection

This candidate is not the same as importing the witness matrix slices:

- \(\operatorname{Gr}_1 r\) would be controlled by \(r^{(3)}(m)\), while the
  existing \(\eta_2/X_1\) witness comes from the quadratic source slice
  \(r^{(2)}(m)\).
- \(\operatorname{Gr}_5 r\) is controlled by \(r^{(7)}(m)\), matching the
  \(q^{(7)}/X_5\) degree calibration, but the paper proves that only as a
  matrix witness after same-point/inverse-square-root expansion.

Thus this candidate can be used as a clean theorem target, but not as a source
fact already proved by the paper.

## Minimal Compatibility List

To promote this filtration, prove:

1. UV-026 finite grade means lowest ordinary-\(z\) pre-whitening matrix order,
   not witness-output labels.
2. \(\operatorname{Gr}_a\) is the exact homogeneous Taylor projection
   \(k=a+2\), or state a different quotient/cumulative convention explicitly.
3. The quadratic slice \(r^{(2)}(m)\), which is grade \(0\) under this
   filtration, is excluded from the \((1,1,5)\) UV-026 gates or handled in a
   separate family.
4. The same scalar projection feeds both same-point and mixed source-linear
   inputs by substitution into the displayed formulas before \(\Phi_K\).
5. The Stage 1 generator should accept the reduced source input:
   \(r_i^{[1](3)}(m)\) and \(r_i^{[5](7)}(m)\), with all other
   \((r_i^{[1/5]})^{(k)}(m)\) set to zero, unless a richer source theorem gives
   non-homogeneous grade pieces.
