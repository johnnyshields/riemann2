# UV-026 Source-Jet Split Audit

## Source-Supported Pieces

The current paper supplies an actual one-pair scalar source contribution before
the UV-026 tagged block:
\[
f_{\beta,\gamma}(t)=
\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}
+
\frac{\beta}{\beta^2+(2t-\gamma)^2}.
\]
The one-pair source remainder later used in the corrected block removes the
midpoint affine jet:
\[
r_\rho(t)=f_\rho(t)-f_\rho(m)-f_\rho'(m)(t-m).
\]
Hence, for every \(k\ge 2\),
\[
r_\rho^{(k)}(m)=f_{\beta,\gamma}^{(k)}(m),
\qquad
r_\rho(m)=r_\rho'(m)=0.
\]

For the elementary term
\[
F_a(t)=\frac{a}{a^2+(2t-\gamma)^2},\qquad x=2m-\gamma,
\]
write \(P_k(a,x)\) by
\[
\frac{d^k}{dx^k}(a^2+x^2)^{-1}
=
\frac{P_k(a,x)}{(a^2+x^2)^{k+1}}.
\]
Then
\[
F_a^{(k)}(m)=
\frac{2^k a\,P_k(a,2m-\gamma)}
{(a^2+(2m-\gamma)^2)^{k+1}},
\]
and therefore
\[
f_{\beta,\gamma}^{(k)}(m)=
F_{1-\beta}^{(k)}(m)+F_{\beta}^{(k)}(m).
\]
The script manifest lists \(P_k\) for \(0\le k\le9\).

This is a source-supported formula for the ungraded source jets.  It does not
yet give \((r_i^{[1]})^{(k)}(m)\) or \((r_i^{[5]})^{(k)}(m)\), because the
paper does not define the scalar projections \(r_i\mapsto r_i^{[1]}\) and
\(r_i\mapsto r_i^{[5]}\).

## Forced Relations Independent Of The Split

For any scalar germ \(h\) after affine removal, the ordinary-\(z\) point
samples satisfy
\[
[z^n]h(m-z/(2Q^2))
=(-1)^n[z^n]h(m+z/(2Q^2)).
\]
The same sign relation holds for \(h'\) and \(h''\) point samples at fixed
\(z^n\).  The integral
\[
\int_{m+z/(2Q^2)}^{m-z/(2Q^2)}h(u)\,du
\]
uses only even midpoint derivatives \(h^{(2)}(m),h^{(4)}(m),h^{(6)}(m),h^{(8)}(m)\)
through the numerator order needed for \([z^7]\) after the mixed-block
divisions.

For the baseline phase, \(\Delta_0=\Phi_0(t_-)-\Phi_0(t_+)\) similarly uses
only \(q_0^{(0)},q_0^{(2)},q_0^{(4)},q_0^{(6)},q_0^{(8)}\).  This does not
remove the need for \(q_0^{(0)},\ldots,q_0^{(9)}\), since \(G_\pm^{(0)}\) uses
\(q_0,q_0',q_0''\) point samples through \(z^7\).

## What The Witness Regions Actually Identify

The tagged/quintic witness regions identify matrix slices, not scalar
finite-grade source functions:

- \(\eta_2\) is the slice carried by the \(X_1\) off-diagonal input.
- \(q^{(5)}\) is the diagonal \(X_3\) input used in the quintic witness.
- \(q^{(7)}\) is the diagonal \(X_5\) input used in the direct septic
  \(K_1\)-witness.

Thus a plausible scalar-grade convention would make grade \(1\) the
\(\eta_2\) / quadratic source-jet slice, and a higher same-point grade either
the \(q^{(5)}\) / \(X_3\) slice or the \(q^{(7)}\) / \(X_5\) slice.  The current
source does not say which of these, if either, is the UV-026 \(M_i^{[5]}\)
input, and does not define \(r_i^{[5]}\) as a scalar germ.

## Smallest Missing Source Substatements

1. Define the scalar projections \(\operatorname{Gr}_1 r_i=r_i^{[1]}\) and
   \(\operatorname{Gr}_5 r_i=r_i^{[5]}\) in the tagged pre-whitening source
   normalization, before \(\Phi_K\).
2. State whether the UV-026 grade-five scalar input corresponds to the
   \(q^{(5)}\)/\(X_3\) quintic slice, the \(q^{(7)}\)/\(X_5\) direct septic
   slice, or a separate mixed-block grading.
3. Prove that this grade projection commutes with midpoint affine removal, so
   \((r_i^{[a]})(m)=(r_i^{[a]})'(m)=0\) for \(a=1,5\).
4. Provide \(q_0^{(k)}(m)\), \(0\le k\le9\), in the same baseline
   normalization.
5. Provide either formulas for \((r_i^{[a]})^{(k)}(m)\), \(a\in\{1,5\}\),
   \(2\le k\le9\), or a projection rule applying \(\operatorname{Gr}_a\) to the
   displayed rational \(f_{\beta,\gamma}^{(k)}(m)\) formulas.

From the inspected source alone, the ungraded rational source jets are
available, but the finite-grade scalar split needed by the Stage 1 generator is
not.
