# C R-determinant pressure test notes

## Baseline

- C-FS3 formal countermodel: fixed codomain, reduction \(\mathcal R\), blow-up
  analyticity, swap-evenness, scalar normalization, and central value
  \(B(m,0)=\widehat\Psi(m)\) do not force \(\partial_\kappa B=0\).
- C-FS2 actual-formula negative: the audited formula neighborhoods do not
  construct the actual corrected two-atom fixed triple and leave the scalar slot
  \(\det(R,A_5^{\mathfrak f})\) uncontrolled. The centered branch has
  \(D_2=2\kappa(AV_1-BU_1)\) with no audited identity forcing
  \(AV_1-BU_1=0\).

## Pressure harness

Assume a future C proof proposes an exceptional-divisor trace
\[
B(m,\kappa)=
\mathcal R(\mathfrak P_2^{\corr})(m,\kappa,0)
\]
whose third coordinate is independent of \(\kappa\). Test the proof by adding
a quotient-defect perturbation \(R_\kappa\) with
\[
\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa.
\]
The defect-thickened identity shows this determinant enters the third
\(\widehat\Psi\) coordinate. Therefore the reduced third coordinate shifts by
\[
\frac{\Delta+c^2\varepsilon\kappa}{c^2}-\frac{\Delta}{c^2}
=\varepsilon\kappa.
\]
Any proof that never excludes this perturbation has not proved C-FS3.

The perturbation is not killed by representative-gauge invariance. Gauge
invariance says replacing \(R\) by \(R+\xi A_5^{\mathfrak f}\) leaves
\(\det(R,A_5^{\mathfrak f})\) unchanged. It does not forbid changing the
quotient class by an \(R_\kappa\) whose determinant against \(A_5^{\mathfrak f}\)
is prescribed.

On a chart where \(A_5^{\mathfrak f}=(u_5,v_5)\) and \(v_5\neq0\), one local
witness is \(R_\kappa=(c^2\varepsilon\kappa/v_5,0)\). On \(u_5\neq0\), one is
\(R_\kappa=(0,-c^2\varepsilon\kappa/u_5)\). Thus the prescribed scalar
perturbation is chartwise available wherever \(A_5^{\mathfrak f}\neq0\). If an
actual C proof works on an \(A_5^{\mathfrak f}=0\) locus, it needs a separate
exceptional-locus argument.

## What a future C closure must prove

It must supply at least one of the following, with source-level definitions:

1. Actual construction of \(\mathfrak P_2^{\corr}\) and the corrected reduced
   package fiber, including the exceptional divisor.
2. Computation of the actual quotient-defect representative \(R\) on that
   divisor, or a theorem that \(\det(R,A_5^{\mathfrak f})\) descends to the
   collision state and has no independent \(\kappa\) or provenance dependence.
3. A diagonal-merger or collision-functoriality theorem that implies
   \(B(m,\kappa)=\widehat\Psi(m)\) for all exceptional slopes.
4. An actual formula identity killing the centered channel, for example
   \(AV_1-BU_1=0\), or a proof that the centered \(D_2\) branch is not the
   C-visible determinant channel for the corrected package.

## Scoped failures

- The claim that C-FS3 follows from fixed codomain, \(\mathcal R\),
  blow-up analyticity, swap-evenness, scalar normalization, and the central
  value \(B(m,0)=\widehat\Psi(m)\) fails from that formal-properties-only
  scope.
- The claim that the displayed order-\(3,5,7\) formulas already forbid
  \(c^2\varepsilon\kappa\) slope dependence fails from the audited
  formula-neighborhood scope alone.
- The claim that no-extra-C-codomain-state would automatically imply
  C-FS3 fails from C-FS2 alone: the formal countermodel has no extra codomain
  coordinate but still has nonconstant exceptional trace.
- The centered \(D_2\) calculation is not a real counterexample to the actual
  corrected package by itself. Its role is adversarial: any proof must identify
  the theorem or actual formula that makes this channel vanish or irrelevant.
