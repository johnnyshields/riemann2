# Septic Hessian source mine

## Target

UV-010 asks for the actual order-\(7\) quotient-defect edge package
\[
\overline E_{12}^{(7;1)}
=
\delta^2\mathcal H_7^q(m,\kappa,\delta^2)
\]
as a section of a fixed midpoint quotient
\[
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m).
\]
For this role, the narrow target is the exceptional edge coefficient
\[
\mathfrak O_7(m,\kappa)
:=
\left[\mathcal J_2^{(7)}(a_1,a_2;m,m)\right],
\]
or a source-level identity determining it.

## What is actually in the source

The paper exposes three nearby but distinct order-\(7\) objects.

1. One-pair fixed-sector quotient data:
\[
[A_7^{\mathfrak f}]
\in \mathfrak f/\mathbf C A_5^{\mathfrak f},
\qquad
\Delta_7=\det(A_7^{\mathfrak f},A_5^{\mathfrak f}).
\]
Refs: `rh/proof_of_rh.tex:7004-7191`.

2. One-pair quotient-septic closure:
\[
[A_7^{\mathfrak f}]=[A_{7,K_1}^{\mathfrak f}],
\qquad
\Delta_7=\Delta_{7,K_1}.
\]
Refs: `rh/proof_of_rh.tex:7540-7974`.  This computes the canonical
one-pair quotient representative up to the \(A_5^{\mathfrak f}\)-line, not the
two-atom interaction Hessian.

3. The abstract two-atom source criterion:
\[
\mathcal I_2=a_1a_2(h_1-h_2)^2\mathcal J_2.
\]
Refs: `rh/proof_of_rh.tex:11888-12189`.  This proves a quadratic factor if an
actual finite-order package already satisfies swap, one-amplitude collapse, and
diagonal merger.  It does not compute the order-\(7\) quotient component
\(\mathcal J_2^{(7)}\).

The defect-thickened theorem then uses a finite-delta class
\[
\overline E_{12}^{(7;1)}
\in \mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}
\]
and a representative \(R\) of
\[
-a_1^{-1}\overline E_{12}^{(7;1)}.
\]
Refs: `rh/proof_of_rh.tex:11587-11775`.  This is an algebraic bridge once the
class exists; it is not a construction of \(\mathcal H_7^q\) on the exceptional
divisor.

## Controlled formula from the centered package

The centered symmetric-placement package gives
\[
\Delta_7(s)=D_2s^2+D_4s^4+D_6s^6+\cdots,
\qquad
D_2=\widehat U_1V_1-U_1\widehat V_1.
\]
Refs: `rh/proof_of_rh.tex:23294-23409`.

With
\[
\widehat U_1=2\kappa A,
\qquad
\widehat V_1=2\kappa B,
\]
where
\[
A=
\delta x_1\nu_{6,0}
+\beta_{5,0}\delta u_1
+v_0\delta\alpha_{5,1}
+b_0\delta p_1
+r_0\delta a_1
\]
and
\[
B=
\delta x_1\bar\mu_{6,0}
-\bar x_0\delta\mu_{6,1}
+\bar\alpha_{5,0}\delta u_1
+\delta\alpha_{5,1}\bar u_0
+\bar a_0\delta p_1
+\delta a_1\bar p_0,
\]
the displayed source formulas give the conditional identity
\[
D_2=2\kappa(A V_1-B U_1).
\]

I wrote `scripts/centered_d2_template_check.js` before running it.  The script
checks this algebraic compression on a deterministic numeric sample and confirms
that the \(\kappa\)-linear channel is formally nonzero unless an additional
identity forces \(A V_1-B U_1=0\).

This is useful but not UV-010 closure: \(D_2\) is a centered one-pair/local
determinant coefficient.  The paper does not identify it with the actual
two-atom quotient interaction Hessian \(\mathfrak O_7\).

## Missing formulas

The smallest finite missing stack is:

1. the actual corrected two-atom finite-order package through order \(7\), with
   a septic quotient output before diagonal merger is assumed;
2. the quotient-line trivialization from the moving
   \(\mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}\) or
   \(\mathfrak f/\mathbf C A_{5,2}^{\mathfrak f}\) to
   \(\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)\);
3. the formula identifying the quotient component of
   \(\mathcal J_2\), i.e. \(\mathfrak O_7(m,\kappa)\), for that actual package;
4. a comparison lemma saying whether the centered \(D_2\) coefficient is the
   same edge coefficient, a projection of it, or irrelevant to the actual
   two-atom quotient package;
5. if promotion beyond UV-010 is attempted later, a separate descent or merger
   identity controlling \(A V_1-B U_1\) or its actual-package analogue.

## Honest verdict

The current sources do not expose \(\mathcal J_2^{(7)}\) / \(\mathfrak O_7\).
They expose the one-pair quotient-septic closure and a centered \(D_2\) channel.
Those give a controlled conditional formula and a pressure test, but not the
actual UV-010 Hessian.
