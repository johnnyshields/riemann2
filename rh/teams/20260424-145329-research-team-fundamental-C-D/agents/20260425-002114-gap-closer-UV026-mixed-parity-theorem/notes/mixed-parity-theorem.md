# UV-026 Mixed-Input Parity Theorem

## Statement Supported By The Source Formulas

For the source-linear scaled mixed input
\[
M(z)=\mathfrak D_Q\delta N^{\lin}(z)
\]
constructed from the displayed mixed block before \(\Phi_K\),
\[
M(-z)=M(z)^T.
\]
Equivalently, \(M_{11}\) and \(M_{22}\) are even power series, while
\[
M_{12}(z)+M_{21}(z)
\]
is even and
\[
M_{12}(z)-M_{21}(z)
\]
is odd.

Thus \(M\) is not an even-only matrix-valued series.  Odd powers can occur,
but only in the off-diagonal antisymmetric channel.

## Source-Derivative Consequence

For a pure scalar Taylor source piece \(r^{(k)}(m)(t-m)^k/k!\):

- if \(k\) is odd, then \(\eta=0\) and \(d_-+d_+=0\), so the source contributes
  only even powers to \(M\);
- if \(k\) is even, the source can contribute even powers to the diagonal
  entries and odd powers to the off-diagonal antisymmetric channel.

Therefore \([z^5]M\) can be nonzero, but not from \(r^{(7)}(m)\).  Through
order \(7\), the finite audit gives
\[
[z^5]M_{11}=0,\qquad [z^5]M_{22}=0,
\]
and, in the script's harmless \(Q=1\), \(\pi\)-suppressed normalization,
\[
[z^5]M_{12}
=
-\frac{1}{96}q_0q_2r_2
-\frac{1}{640}q_0^2r_4
+\frac{1}{96}q_0^4r_2
+\frac{1}{53760}r_6,
\]
\[
[z^5]M_{21}=-[z^5]M_{12}.
\]

## UV-026 Consequence

The pure homogeneous \(r^{(7)}\) convention cannot produce the intended
\([z^5]M_i^{[5]}\) needed for the \(L_1YR_1\) \(B_7\) convolution.  A nonzero
\([z^5]M_i^{[5]}\) must come from an even source-derivative projection involving
\(r^{(2)}\), \(r^{(4)}\), and/or \(r^{(6)}\), or from a theorem explaining a
different source-grade convention.

This is still pre-\(\Phi_K\).  No determinant or quotient argument is used.
