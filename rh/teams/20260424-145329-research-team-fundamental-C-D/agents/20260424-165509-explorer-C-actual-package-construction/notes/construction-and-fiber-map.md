# Actual C package construction and fiber map

## Decision

The current draft supports a fixed C-codomain schema, not a constructed actual
corrected two-atom object.

Confirmed source-supported pieces:

- One-pair C data:
  \[
  (c(h), A_5^{\mathfrak f}(h), \Delta_7(h)),
  \qquad
  A_5^{\mathfrak f}=u_5I+v_5S,
  \qquad
  \Delta_7=u_7v_5-u_5v_7.
  \]
- Gauge facts: \(A_7^{\mathfrak f}\) is canonical only modulo
  \(\mathbf C A_5^{\mathfrak f}\), while \(\Delta_7\) is gauge-invariant.
- C reduction:
  \[
  V_C=\mathbf C\times\mathfrak f\times\mathbf C,
  \qquad
  \mathcal R_C(C,UI+VS,\Delta)=
  \left(U/C,V/C,\Delta/C^2\right).
  \]
- One-pair target:
  \[
  \widehat\Psi(m)=
  \left(u_5/c,v_5/c,\Delta_7/c^2\right).
  \]

Missing source-supported object:

\[
\mathfrak P_{2,C}^{\corr}(m,\kappa,t)
=
(C^{\corr},A^{\mathfrak f,\corr},\Delta^{\corr}),
\qquad t=\delta^2,\quad 2\omega=\kappa\delta,
\]
as an analytic germ valued in \(V_C\), constructed from the actual corrected
two-atom formulas.

## Conditional fiber definition

If the actual object above exists on a good collision chart with
\(C^{\corr}\neq 0\), define
\[
\widetilde\Psi_{\mathrm{red}}^{\corr}
:=\mathcal R_C\circ\mathfrak P_{2,C}^{\corr},
\qquad
B_C(m,\kappa):=\widetilde\Psi_{\mathrm{red}}^{\corr}(m,\kappa,0).
\]

For a reduced value \(b=(Y,X,Z)\), the codomain fiber of \(\mathcal R_C\) is
\[
\mathcal R_C^{-1}(b)=
\{(\rho,\rho(YI+XS),\rho^2Z):\rho\in\mathbf C^\times\}.
\]
This is only the homogeneous C-normalization fiber.

For fixed \(m\), the exceptional reduced-package fiber over the one-pair datum
is
\[
\mathrm{Fib}^{C,\corr}_m(\widehat\Psi(m))
:=
\{\kappa: B_C(m,\kappa)=\widehat\Psi(m)\}.
\]
Bottleneck C is the assertion that the relevant exceptional divisor lies in
this fiber for all allowed \(\kappa\), equivalently
\[
B_C(m,\kappa)\equiv \widehat\Psi(m).
\]

## C versus D separation

The C codomain is \(V_C=\mathbf C\times\mathfrak f\times\mathbf C\). Its third
coordinate is determinant-level quotient data.

The raw septic affine line
\[
A_7^{\mathfrak f}+\mathbf C A_5^{\mathfrak f}
\]
and local sections such as \(v_7=0\), \(u_7=0\), or a scalar like \(T=v_7/c\)
belong to the D / hidden-state affine-lift analysis. They are not C coordinates.

## Smallest missing C stack

1. Definition: construct \(\mathfrak P_{2,C}^{\corr}\) as an actual analytic
   fixed-codomain two-atom germ in \(V_C\).
2. Definition/lemma: prove \(\widetilde\Psi_{\mathrm{red}}^{\corr}\) extends to
   \(t=0\) and that the reduced-package fiber above is the intended
   exceptional-divisor fiber.
3. Proposition: control the septic quotient-defect representative \(R\), or at
   least prove \(\det(R,A_5^{\mathfrak f})\) descends to the collision state
   with no independent provenance/slope term.
4. Proposition: diagonal merger / slope independence,
   \(B_C(m,\kappa)=B_0(m)\).
5. Lemma: identify \(B_0(m)=\widehat\Psi(m)\) from merged one-pair
   compatibility and the scaling law.

The live obstruction is item 3 plus item 4. The paper's current formal
properties allow a deformation with third reduced coordinate
\[
Z(m)+\varepsilon\kappa.
\]
