# Dependency map for the exceptional-divisor quotient class [R]

## Local finite-delta class already in the paper

At finite separated two-point data, the paper has an algebraic placeholder:
\[
a_1[A_{7,1}^{\mathfrak f}]+a_2[A_{7,2}^{\mathfrak f}]
+\overline E_{12}^{(7;1)}=0
\quad\text{in}\quad
\mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}.
\]
Then any representative \(R\in\mathfrak f\) of
\[
-a_1^{-1}\overline E_{12}^{(7;1)}
\]
is enough for the determinant identity. This is a finite-delta algebraic
definition conditional on the existence of the septic quotient defect.

## Edge class needed for C

C needs an exceptional-divisor class, not only the finite-delta algebraic
placeholder. The minimal non-merger definition would be:
\[
\overline E_{12}^{(7;1)}(m,\omega,\delta)
=\delta^2\,\mathcal H_7^q(m,\kappa,\delta^2),
\qquad \kappa=2\omega/\delta,
\]
with values in a consistently transported quotient line
\[
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)
\]
or an explicitly specified \(h_1\)-based quotient plus analytic
identification to the midpoint quotient. Then define
\[
[R]_{\mathrm{edge}}(m,\kappa):=
-a_1(0)^{-1}\,\mathcal H_7^q(m,\kappa,0).
\]
If the amplitude gauge is normalized by \(a_1\equiv1\), the factor disappears.

This definition does not assume diagonal merger. It assumes actual
source-level construction of the septic quotient defect and its edge-law
extension.

## What the three candidate sources provide

1. Conditional package, lines 11994--12040:
   - Provides a finite-order source package target in
     \(\mathbf C\oplus\mathfrak f\oplus
       (\mathfrak f/\mathbf C A_5^{\mathfrak f})\).
   - But it explicitly imports the three hypotheses of the minimal source
     criterion, including diagonal merger.
   - It yields an \(O(\delta^2)\) estimate for
     \(\overline E_{12}^{(7;1)}\), not a definition of the edge coefficient
     \(\mathcal H_7^q\).

2. Quotient-diagonal route, lines 12042--12166:
   - Assumes an actual corrected two-atom quotient map
     \(\mathcal F_2\in\Qabs[[z^2]]\).
   - Uses continuity plus diagonal collapse.
   - Too coarse for \([R]\): it does not extract cubic/quintic/septic finite
     coefficients or the quotient-septic defect class.

3. Collision edge-law WIP, lines 12385--12584:
   - Gives the right chart:
     \(m=(h_1+h_2)/2\), \(\delta=h_2-h_1\),
     \(\omega=(\lambda-1)/(\lambda+1)\),
     \(\kappa=2\omega/\delta\).
   - Gives a template: analytic, swap-even, collision-vanishing defect
     \(E(m,\omega,\delta)\) has \(E=\delta^2\mathcal H(m,\kappa,\delta^2)\).
   - Displays only cubic and quintic edge laws:
     \(E_{12}^{(3)}=\delta^2\mathcal H_3\),
     \(E_{12}^{(5)}=\delta^2\mathcal H_5\).
   - Names package-level coincidence/functoriality as remaining conditional
     programs. No septic quotient edge law appears.

## First missing definition

The first missing definition is an actual corrected order-7 quotient-defect
edge package:
\[
\mathcal H_7^q(m,\kappa,t)\in
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m),
\qquad t=\delta^2,
\]
obtained from the actual corrected two-atom package by
\[
\overline E_{12}^{(7;1)}
=\delta^2\mathcal H_7^q(m,\kappa,\delta^2)
\]
after specifying the quotient-bundle trivialization from \(A_{5,1}\) to the
midpoint line \(A_5(m)\).

State-locality/descent for \([R]\) and diagonal-merger normalization are later
propositions. They should not be included in the definition.
