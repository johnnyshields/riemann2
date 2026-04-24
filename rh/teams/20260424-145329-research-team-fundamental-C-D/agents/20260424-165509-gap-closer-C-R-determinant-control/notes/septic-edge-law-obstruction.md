# Septic edge-law obstruction

## Target

The requested order-7 analogue of the WIP cubic/quintic edge laws would be a
statement in the quotient bundle
\[
\mathfrak f/\mathbf C A_5^{\mathfrak f}.
\]
Using the convention of
`rh/proof_of_rh.tex:11587-11775`, write
\[
R=-a_1^{-1}\overline E_{12}^{(7;1)}
\quad
\text{in}\quad
\mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}.
\]
The desired edge-law target is:
\[
R(m,\kappa,\delta)=\delta^2\mathcal H_7(m,\kappa,\delta^2),
\]
and on the exceptional divisor
\[
\mathcal H_7(m,\kappa,0)
\]
must factor through the descended collision state. By the previous determinant
report, this is equivalent on \(A_5^{\mathfrak f}\neq0\) to descent of
\[
\det(\mathcal H_7(m,\kappa,0),A_5^{\mathfrak f}(m)).
\]

## What the current source proves

The paper proves a formal quadratic factorization if an actual finite-order
package
\[
\mathfrak P_2(a_1,h_1;a_2,h_2)
\in
\mathbf C\oplus\mathfrak f\oplus
(\mathfrak f/\mathbf C A_5^{\mathfrak f})
\]
satisfies swap symmetry, one-amplitude collapse, and diagonal merger. The proof
is abstract: it writes the interaction remainder as
\[
\mathcal I_2=a_1a_2(h_1-h_2)^2\mathcal J_2.
\]
Thus the order-7 edge coefficient is the septic quotient component of
\(\mathcal J_2\) on the collision locus.

This is already the smallest missing object:
\[
\mathfrak O_7(m,\kappa)
:=
\left[\mathcal J_2^{(7)}(a_1,a_2;m,m)\right]
\in
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m),
\]
after translating the amplitude ratio into the collision slope
\(\kappa=2\omega/\delta\). The source criterion proves the factor
\(\delta^2\), but it does not compute \(\mathfrak O_7\), does not make it
descended, and does not force its determinant to be independent of provenance.

## Obstruction model

Let \(F(h)=(c(h),A(h),Q(h))\) be any one-pair finite-order package in a vector
space with a one-dimensional septic quotient coordinate. Define
\[
\mathfrak P_2(a_1,h_1;a_2,h_2)
=
a_1F(h_1)+a_2F(h_2)
+a_1a_2(h_1-h_2)^2(0,0,P(m,\kappa)),
\]
where \(m=(h_1+h_2)/2\), \(\delta=h_2-h_1\), and \(P\) is any analytic
swap-compatible septic quotient function of \((m,\kappa)\).

Then:

- swap symmetry holds, because \(a_1a_2\), \(\delta^2\), \(m\), and \(\kappa\)
  are swap-invariant in the blown-up chart;
- one-amplitude collapse holds, because the interaction term has factor
  \(a_1a_2\);
- diagonal merger holds, because the interaction term has factor \(\delta^2\);
- cubic and quintic edge data are unchanged, because the added term is purely
  septic quotient;
- the order-7 edge coefficient is shifted by \(P(m,\kappa)\).

The script `scripts/septic_edge_obstruction_model.js` checks this finite model.
With \(P(m,\kappa)=13+17\kappa+19m\), the script reports a nonzero
\(\kappa\)-derivative of the septic edge coefficient.

## Consequence

The first obstruction to order-7 descent is not a raw representative or a lower
edge-law failure. It is the septic quotient Hessian
\[
\mathfrak O_7(m,\kappa)
\]
in the quadratic interaction remainder of the actual package.

The minimal theorem needed for C is:

1. construct the actual order-7 source package and its quotient interaction
   remainder \(\mathcal J_2^{(7)}\);
2. prove \(\mathfrak O_7(m,\kappa)\) factors through the descended collision
   state;
3. prove the determinant scalar is constant on any exceptional provenance fiber
   and is merger-normalized to the one-pair value.

Absent item 2, the formal model above realizes the same lower source axioms and
lower edge laws while changing \([R](m,\kappa,0)\).

## Honest verdict

The order-7 edge-law route is reduced to one concrete missing substatement:
control the septic quotient component of the quadratic interaction Hessian
\(\mathcal J_2\). The current draft supplies the abstract divisibility
mechanism but not the actual order-7 Hessian or its descent.
