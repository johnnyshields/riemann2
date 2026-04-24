# UV-026 Scalar Grade-Projection Audit

## Verdict

The current source does not define a scalar projection
\[
r_i\longmapsto r_i^{[1]},\qquad r_i\longmapsto r_i^{[5]}
\]
on the affine-removed pre-whitening source remainder.  The witness-region
matrix slices cannot be used as that definition without a new theorem.

There is still a useful source decision:

- the \(q^{(5)}/X_3\) convention is not compatible with a grade-five mixed
  input \(M_i^{[5]}\) if the grade refers to finite order in the displayed
  mixed block.  Source text says \(q^{(5)}\) first appears in the cubic
  same-point coefficient \(G_3\), and the order audit places a scalar
  derivative \(k=5\) at lowest mixed order \(z^3\).
- the \(q^{(7)}/X_5\) convention is the only witness-region candidate with
  source support at finite degree \(5\): source text says \(q^{(7)}\) first
  appears in the quintic same-point coefficient \(G_5\), and the order audit
  places scalar derivative \(k=7\) at lowest mixed order \(z^5\).

This does not promote \(q^{(7)}/X_5\) to a definition of \(r_i^{[5]}\).  It only
rejects the \(q^{(5)}/X_3\) reading and identifies the exact theorem still
needed.

## Why Matrix Slices Do Not Define Scalar Grades

The witness-region slices are not scalar source projections:

1. They are formulated after matrix coefficient extraction and inverse
   square-root parity.  The objects are \(X_1,X_3,X_5,X_6\), fixed-sector
   channels, and \(K_1\)-transport products.
2. The proofs use matrix parity at a diagonal base, e.g. diagonal/off-diagonal
   behavior of \(X_j\), not a projection on the scalar germ \(r\).
3. The \(q^{(5)}\) slice is used to make \(A_5^{\mathfrak f}\) nontrivial; it is
   not the middle grade-five input for a cubic order-seven family.
4. The \(q^{(7)}\) slice is a direct septic witness and matches finite degree
   \(5\), but it remains a same-point \(X_5\) matrix slice.  UV-026 needs a
   tagged pre-whitening scalar/mixed input \(M_i^{[5]}=\operatorname{Gr}_5
   (\mathfrak D_Q\delta N_i^{\lin})\).

## Smaller Missing Theorem

The minimal scalar grade-projection theorem should state:

1. A filtration/projection \(\operatorname{Gr}_a\) on affine-removed scalar
   source germs in ordinary \(z\), before \(\Phi_K\), with source tags retained.
2. Compatibility with affine removal:
   \[
   (\operatorname{Gr}_a r_i)(m)=(\operatorname{Gr}_a r_i)'(m)=0.
   \]
3. Compatibility with the displayed pre-whitening formulas:
   \[
   \operatorname{Gr}_a(\mathfrak D_Q\delta G_{i,\pm}^{\lin})
   =\mathfrak D_Q\delta G_{i,\pm}^{\lin}[\operatorname{Gr}_a r_i],
   \]
   and
   \[
   \operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})
   =\mathfrak D_Q\delta N_i^{\lin}[\operatorname{Gr}_a r_i].
   \]
4. Degree calibration:
   - \(q^{(5)}/X_3\) is degree \(3\), not grade \(5\);
   - \(q^{(7)}/X_5\) is the degree \(5\) candidate;
   - if the theorem chooses a different mixed-block grading, it must specify
     how it relates to the order shifts from the \(s^{-1},s^{-2},s^{-3}\)
     denominators.
5. The resulting derivative list through order \(9\) for \(r_i^{[1]}\) and
   \(r_i^{[5]}\), or explicit vanishing/projection relations reducing it.

From the inspected source alone, this theorem is missing.
