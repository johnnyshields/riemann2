## Claim

The draft suggests that
\[
\bigl(\widehat\Psi,[\delta c:\delta v_5:\delta u_5:\delta\lambda]\bigr)
\]
is not the sharpest plausible enlargement. A smaller reduced candidate is
\[
\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)
\quad\text{with}\quad
x=\frac{v_5}{c},\ Y=\frac{u_5}{c},\ S=\frac{\Delta_7}{c\,v_5}=\frac{\lambda}{c},
\]
or equivalently the projective secant/tangent shadow of the reduced package curve
\(Q_v=(Y,x,S)\).

## Status

heuristic

## Evidence

- `\widehat\Psi` is already declared the correct projective datum for downstream multi-pair and minimal-core extraction, so any enlargement should be measured relative to reduced variables, not raw amplitudes.
- In the collision-cancellation chart, the first blown-up cancellation datum is the projective source direction built from `(c,u_5,v_5)`, but the later mixed exact branch is reformulated more sharply as an exact projective secant shadow in `(x,Y,S)` that is independent of the moving shears and of `\Lambda_n`.
- The residual mixed lane is explicitly described as the projective `\lambda`-shear / secant-shadow route, which points to a reduced tangent/secant class of `Q_v`, not to the full raw four-vector `[\delta c:\delta v_5:\delta u_5:\delta\lambda]`.
- Since `S=\lambda/c` is already a function of `\widehat\Psi`, the extra datum naturally suggested by the draft is the tangent/secant direction of the reduced package curve, i.e. `[\delta x:\delta Y:\delta S]` or the equivalent tangent shadow `\mathbf\Pi`, rather than the unreduced hidden increment class.

## Exact refs

- `paper/proof_of_rh.tex:11368-11450`
- `paper/proof_of_rh.tex:12391-12445`
- `paper/proof_of_rh.tex:12586-12610`
- `paper/proof_of_rh.tex:20853-20924`
- `paper/proof_of_rh.tex:24380-24403`
- `paper/proof_of_rh.tex:24538-24543`

## Dependencies

- The reduced package coordinates `x=v_5/c`, `Y=u_5/c`, `S=\Delta_7/(c\,v_5)` remain valid on an overlap patch with `c,u_5,v_5\neq 0`.
- Bottleneck D still needs a hidden-state/package-to-jet theorem; this note addresses only which enlarged state looks sharpest from the present draft.

## Strongest objection

The paper does not prove that `\bigl(\widehat\Psi,[\delta x:\delta Y:\delta S]\bigr)` is sufficient for the hidden extraction step. The blow-up source direction `\Theta_{m,\theta}` in `(c,u_5,v_5)` shows that raw source-level increments remain natural earlier in the argument, so the smaller reduced datum is only a plausible sharpening, not a theorem already latent in the draft.

## Needed for promotion

1. Prove that the first surviving odd jet of `H_m` is constant on fibers of the reduced secant/tangent package of `Q_v=(Y,x,S)`.
2. Or show that the raw-to-reduced quotient from `[\delta c:\delta v_5:\delta u_5:\delta\lambda]` to `[\delta x:\delta Y:\delta S]` loses only `\Phi_K`-invisible directions through the first surviving odd order.

Honest verdict: the enlarged raw package with `[\delta c:\delta v_5:\delta u_5:\delta\lambda]` is a plausible safe overpackage, but the draft itself points to a sharper reduced candidate: `\widehat\Psi` plus the projective tangent/secant shadow of the reduced curve `Q_v=(Y,x,S)`.
