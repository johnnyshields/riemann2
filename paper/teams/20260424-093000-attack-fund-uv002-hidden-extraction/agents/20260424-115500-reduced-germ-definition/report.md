## Claim

The slogan "same reduced image germ at coincidence" can be made precise in current notation as follows.

Let the actual corrected two-atom package on the collision/cancellation chart be a germ

\[
\mathfrak P^{\mathrm{corr}}_2(m,\omega,\delta)
=
\bigl(C(m,\omega,\delta),\ A^{\mathfrak f}(m,\omega,\delta),\ [B](m,\omega,\delta)\bigr),
\]

with

\[
A^{\mathfrak f}=U\,I+V\,S\in \mathfrak f,
\qquad
[B]\in \mathfrak f/\mathbf C A^{\mathfrak f},
\]

and define its canonical residual determinant by

\[
\Delta^{\mathrm{corr}}(m,\omega,\delta):=\det(B,A^{\mathfrak f}),
\]

which is independent of the choice of representative \(B\) modulo
\(\mathbf C A^{\mathfrak f}\). Then on \(\{C\neq 0\}\) the correct reduced package map is

\[
\widehat\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\omega,\delta)
:=
\left(
\frac{U}{C},\frac{V}{C},\frac{\Delta^{\mathrm{corr}}}{C^2}
\right).
\]

This is the exact two-atom analogue of the one-pair datum
\(\widehat\Psi(h)=(u_5/c,v_5/c,\Delta_7/c^2)\). Because swap acts by
\((m,\omega,\delta)\mapsto(m,-\omega,-\delta)\), the theorem should be stated on the blow-up variables

\[
\kappa:=\frac{2\omega}{\delta},
\qquad
\varepsilon:=\delta^2,
\]

as the existence of an analytic germ

\[
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,\varepsilon)
\]

such that

\[
\widehat\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\omega,\delta)
=
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}\!\left(m,\frac{2\omega}{\delta},\delta^2\right).
\]

In this language, "same reduced image germ at coincidence" is exactly the single exceptional-divisor condition

\[
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\quad\text{for all nearby }\kappa,
\]

equivalently: the diagonal value is \(\kappa\)-independent and agrees with the one-pair reduced package.

If one wants a chartwise image-germ statement on \(V\neq 0\), its image is the lifted curve germ

\[
Q_v^{\mathrm{corr}}=(Y^{\mathrm{corr}},x^{\mathrm{corr}},S^{\mathrm{corr}})
=
\left(\frac{U}{C},\frac{V}{C},\frac{\Delta^{\mathrm{corr}}}{CV}\right),
\]

but the theorem should be formulated in the full \(\widehat\Psi\)-coordinates, not only in the \(v_5\neq 0\) chart.

## Status

heuristic

## Evidence

- The one-pair canonical reduced datum already exists and is exactly \(\widehat\Psi(h)=(u_5/c,v_5/c,\Delta_7/c^2)\).
- The order-7 canonical object is the quotient class \([A_7^{\mathfrak f}]\in \mathfrak f/\mathbf C A_5^{\mathfrak f}\), and its determinant against the quintic vector is gauge-invariant.
- The collision/cancellation chart \((m,\omega,\delta)\) and its blow-up variable \(\kappa=2\omega/\delta\) are already the draft's canonical coordinates for close cancelling two-atom analysis.
- The draft already isolates swap-evenness plus vanishing at coincidence as the exact mechanism producing a descended analytic germ in \((m,\kappa,\delta^2)\).
- Therefore the non-slogan definition is: take the actual corrected package, apply the same \(\widehat\Psi\)-reduction as in the one-pair case, then descend it to the blow-up chart and require its exceptional-divisor value to match \(\widehat\Psi(m)\).

## Exact refs

- `paper/proof_of_rh.tex:7004-7062`
- `paper/proof_of_rh.tex:8004-8033`
- `paper/proof_of_rh.tex:11368-11584`
- `paper/proof_of_rh.tex:11639-11775`
- `paper/proof_of_rh.tex:12391-12469`
- `paper/proof_of_rh.tex:12513-12610`
- `paper/proof_of_rh.tex:13910-13926`
- `paper/proof_of_rh.tex:21142-21195`
- `paper/proof_of_rh.tex:25290-25325`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:45-52`

## Dependencies

- A canonically defined actual corrected two-atom package \(\mathfrak P^{\mathrm{corr}}_2\) through the cubic/quintic/quotient-septic levels.
- Analyticity of that package in the collision/cancellation chart.
- Swap-equivariance of the corrected package under atom interchange.
- Agreement of the corrected order-7 quotient component with a determinant-type scalar \(\Delta^{\mathrm{corr}}\) defined modulo the quintic line.

## Strongest objection

The draft does not yet contain a canonical actual corrected two-atom order-7 package with established quotient representative. So the formula above is sharp as a theorem target, but still schematic until the corrected package itself is constructed in exactly this form. If the actual corrected package naturally carries an extra hidden scalar not killed by the quotient-septic gauge, then \(\widehat\Psi^{\mathrm{corr}}_{\mathrm{red}}\) will need enlargement before Bottleneck D, though Bottleneck C itself should still be stated this way.

## Needed for promotion

1. Introduce notation for the actual corrected two-atom package \(\mathfrak P^{\mathrm{corr}}_2\) and its quotient-septic determinant \(\Delta^{\mathrm{corr}}\).
2. Prove that \(\widehat\Psi^{\mathrm{corr}}_{\mathrm{red}}\) is analytic after descent to \((m,\kappa,\delta^2)\).
3. Prove the exceptional-divisor identity
   \(\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)\).
4. Then invoke the existing strengthened-coincidence algebra to get the reduced-\(\widehat\Psi\) coincidence theorem.

Honest verdict: the slogan can be replaced by a concrete object. The reduced package germ should be the blow-up-descended \(\widehat\Psi\) of the actual corrected two-atom package, and the whole theorem reduces to one exact statement: its value on the exceptional divisor \(\delta=0\) is independent of \(\kappa\) and equals the one-pair datum \(\widehat\Psi(m)\).
