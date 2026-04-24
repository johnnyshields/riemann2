Fifth follow-up on C: patch transitions for the local affine lift coordinate.

Computation from the two canonical local gauges:

- on \(v_5\neq 0\), the section value is
  \[
  S:=\frac{\lambda}{c}=\frac{\Delta_7}{c v_5};
  \]
- on \(u_5\neq 0\), the analogous section value is
  \[
  S_u:=-\frac{\Delta_7}{c u_5}.
  \]

On the overlap \(u_5v_5\neq 0\), the transition is
\[
S_u=-\frac{v_5}{u_5}S=-\frac{x}{Y}S,
\qquad
Y=\frac{u_5}{c},\ x=\frac{v_5}{c}.
\]
Equivalently, the affine translation parameter is
\[
\tau:=\frac{\Delta_7}{u_5v_5}=\frac{\Delta_7/c^2}{(u_5/c)(v_5/c)},
\]
which is already a function of the reduced package datum \(\widehat\Psi=(Y,x,\Delta_7/c^2)\).

Consequences:

1. The patch-transition data for the local lift coordinate do NOT introduce a new hidden state beyond \(\widehat\Psi\); they are already determined by reduced data.
2. What remains hidden is the affine section value itself, i.e. the choice of lift in the affine fiber, not the cocycle.
3. So the best current C formulation is:
   - base = descended quotient-visible collision state together with reduced package \(\widehat\Psi\);
   - fiber = one-dimensional affine septic-lift coordinate;
   - transitions of local section values are controlled by the base;
   - Bottleneck C must canonically select / collapse the fiber at coincidence.

This is better than the previous report because it separates two issues:
- cocycle/patching is not the hidden obstruction;
- actual affine-fiber selection is the hidden obstruction.

Strongest objection: this is computed from one-pair local gauge sections, not from an actual corrected two-atom exceptional-divisor object. It shows the local model is coherent, but not that the corrected two-atom package has exactly this affine-bundle structure on the full collision chart.