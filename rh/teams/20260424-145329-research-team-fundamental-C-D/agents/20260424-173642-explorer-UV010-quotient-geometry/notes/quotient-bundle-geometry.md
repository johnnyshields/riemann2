# UV-010 quotient-bundle geometry note

## Setup

Let
\[
\mathfrak f=\operatorname{span}\{I,S\},
\qquad
A(h)=A_5^{\mathfrak f}(h)=u(h)I+v(h)S.
\]
On any patch where \(A(h)\neq0\), set
\[
L_h=\mathbf C A(h),\qquad Q_h=\mathfrak f/L_h .
\]
The determinant convention used by the draft is
\[
\det(r_uI+r_vS,uI+vS)=r_uv-ur_v .
\]

## Local geometry lemma

On \(U=\{h:A_5^{\mathfrak f}(h)\neq0\}\), the family
\[
Q=\mathfrak f/\mathbf C A_5^{\mathfrak f}
\]
is an analytic line bundle, and the determinant pairing gives a canonical
analytic trivialization
\[
\tau_h:Q_h\to\mathbf C,\qquad
\tau_h([R])=\det(R,A_5^{\mathfrak f}(h)).
\]
The map is well-defined because adding \(\xi A_5^{\mathfrak f}(h)\) to \(R\)
does not change the determinant. Its kernel in \(\mathfrak f\) is exactly
\(\mathbf C A_5^{\mathfrak f}(h)\), so it is an isomorphism on the quotient.

Consequently, for two nearby points \(h_1\) and \(m\) in \(U\), there is a
canonical analytic moving-quotient-to-midpoint identification
\[
T_{h_1\to m}:Q_{h_1}\to Q_m,
\qquad
T_{h_1\to m}:=\tau_m^{-1}\circ\tau_{h_1}.
\]
Equivalently, \(T_{h_1\to m}([R])\) is the unique midpoint quotient class whose
determinant against \(A_5^{\mathfrak f}(m)\) equals
\(\det(R,A_5^{\mathfrak f}(h_1))\).

No complement is part of the canonical definition. Complements only give local
representatives:
\[
u(m)\neq0:\quad R_m=-\frac{s}{u(m)}S,
\qquad
v(m)\neq0:\quad R_m=\frac{s}{v(m)}I,
\]
where \(s=\det(R,A_5^{\mathfrak f}(h_1))\). On the overlap these two
representatives differ by
\[
\frac{s}{u(m)v(m)}A_5^{\mathfrak f}(m),
\]
so they define the same class in \(Q_m\).

## Exceptional locus

At \(A_5^{\mathfrak f}(m)=0\), the subspace \(L_m=\mathbf C A_5^{\mathfrak f}(m)\)
has rank \(0\), not rank \(1\). The quotient jumps from a line to
\(\mathfrak f\), and the determinant map \(\det(-,A_5^{\mathfrak f}(m))\) is
identically zero. Thus the midpoint quotient object used above is not a vector
bundle across this locus.

There are only two clean conventions:

1. Restrict UV-010 to constant-rank good patches \(A_5^{\mathfrak f}(m)\neq0\).
2. Add a projectivized or blow-up convention that replaces a zero value by a
   chosen limiting line \(\ell\in\mathbf P(\mathfrak f)\), then use
   \(\mathfrak f/\ell\).

The second convention is extra structure. It is not present in the cited paper
ranges. It must not be treated as automatic.

## Consequence for UV-010

The quotient geometry itself is not the remaining obstruction on
\(A_5^{\mathfrak f}\neq0\). The determinant pairing supplies the needed
midpoint trivialization. The real missing statement is the analytic order-7
defect:
\[
\overline E_{12}^{(7;1)}
=
\delta^2\mathcal H_7^q(m,\kappa,\delta^2)
\]
after applying the above \(T_{h_1\to m}\) convention and the chosen amplitude
normalization. Once that edge object exists, the exceptional-divisor class is
\[
[R]_{\mathrm{edge}}(m,\kappa)
=
-a_1(0)^{-1}\mathcal H_7^q(m,\kappa,0)
\in
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m).
\]
This definition still allows \(\kappa\)-dependence. State-locality/descent and
diagonal merger are separate downstream targets.
