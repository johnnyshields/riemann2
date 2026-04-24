# UV-026 L1YR1 Mixed-Order Prototype Verdict

## Result

The homogeneous mixed-order candidate does not populate the intended
\(L_1YR_1\) order-seven convolution.

Candidate:
\[
\operatorname{Gr}_1 r=\frac{r^{(3)}(m)}{3!}(t-m)^3,\qquad
\operatorname{Gr}_5 r=\frac{r^{(7)}(m)}{7!}(t-m)^7.
\]

Same-point behavior:

- \(r^{(3)}\) contributes to \(\delta G^{\lin}\) first in order \(z^1\) through
  the \(g=r''\) entry.
- \(r^{(7)}\) contributes to \(\delta G^{\lin}\) first in order \(z^5\) through
  the same \(g=r''\) entry.

Mixed behavior:

- For even scalar derivative order \(k\), the mixed input first appears in
  order \(k-2\), through \(M_{22}\).
- For odd scalar derivative order \(k\), the leading \(M_{22}\) channel
  cancels because \(d_-+d_+=0\) and \(\eta=0\).  The first mixed contribution
  is off-diagonal, from \(d/s\), in order \(k-1\).

Therefore:

- \(r^{(3)}\) gives \(\delta G\) order \(1\), but \(M\) order \(2\).
- \(r^{(7)}\) gives \(\delta G\) order \(5\), but \(M\) order \(6\).
- In particular, \([z^5]M^{[5]}=0\) for the pure \(r^{(7)}\) grade-five
  candidate.

Since the \(L_1YR_1\) \(z^7\) convolution needs
\[
[z]\Lambda^{[1]}\cdot [z^5]M^{[5]}\cdot [z]\Lambda^{[1]},
\]
the homogeneous candidate gives zero for the prototype before any determinant
test.  This is not a positive gauge proof; it is a compatibility failure for
the proposed source-grade convention.

## Exact Obstruction

Full baseline \(q_0\) specialization is not the hard blocker for this
prototype.  The hard blocker is exact mixed-block parity under
\(t_+\leftrightarrow t_-\): odd scalar Taylor pieces miss odd mixed orders.

To get a nonzero \(M_i^{[5]}\) feeding \(L_1YR_1\), UV-026 needs a different
grade-five source convention, a non-homogeneous projection whose mixed table
has nonzero \([z^5]\), or a proof that the \(L_1YR_1\) grade-five mixed input is
allowed to start later and therefore contributes no \(B_7^{\mathfrak f}\)
term.
