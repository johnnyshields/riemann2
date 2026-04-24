## Claim

The single convention that still must be frozen is the **exceptional-divisor convention for the corrected reduced two-atom package**: define `\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,\delta)` in the collision-cancellation blow-up chart by substituting `2\omega=\kappa\delta` and then analytically extending in `(m,\kappa,\delta)` to `\delta=0`. With that convention, the statement
\[
\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]
means equality of the **exceptional-divisor trace** of the corrected reduced package with the one-pair amplitude-invariant datum `\widehat\Psi`, rather than a literal restriction of the raw `(m,\omega,\delta)` package to the diagonal.

## Status

heuristic

## Evidence

- `\widehat\Psi(h)` is already frozen precisely as the amplitude-invariant one-pair datum `(u_5/c,\,v_5/c,\,\Delta_7/c^2)`.
- The collision chart introduces `(m,\omega,\delta)` and then the blown-up slope parameter `\kappa=2\omega/\delta`; at `\delta=0`, `\kappa` has meaning only on the blow-up exceptional divisor, not in the raw chart.
- The current draft repeatedly names “same reduced image germ at coincidence” and “collision-functoriality” as theorem targets, but does not yet define a canonical reduced corrected package map whose value at `\delta=0` is taken on that exceptional divisor.
- So the equation is presently ambiguous between at least two readings: literal diagonal restriction in raw variables, or exceptional-divisor value after blow-up. Only the second makes `\kappa` visible and makes the theorem mathematically well-posed.

## Exact refs

- `paper/proof_of_rh.tex:11368-11383` — definition of `\widehat\Psi`.
- `paper/proof_of_rh.tex:11436-11449` — `\widehat\Psi` is the scalar-invariant multi-pair datum.
- `paper/proof_of_rh.tex:12385-12440` — collision-cancellation chart `(m,\omega,\delta)` and blow-up direction.
- `paper/proof_of_rh.tex:12452-12469` — `\kappa=2\omega/\delta` and analytic blown-up form `E=\delta^2\mathcal H(m,\kappa,\delta^2)`.
- `paper/proof_of_rh.tex:12552-12555` — target phrased as same reduced image germ / collision-functoriality.
- `paper/proof_of_rh.tex:12586-12608` — `\widehat\Psi` identified as the correct downstream datum.
- `paper/proof_of_rh.tex:12048-12165` — existing exact route already uses continuity plus diagonal collapse language for the actual corrected two-atom quotient map.

## Dependencies

- A definition of the actual corrected two-atom reduced package in the collision chart, with the same normalization convention as the one-pair datum it is meant to limit to.
- Analytic extension/continuity of that reduced package in blow-up coordinates `(m,\kappa,\delta)` up to the exceptional divisor `\delta=0`.
- A fixed choice of whether “reduced” means the affine amplitude-invariant datum matching `\widehat\Psi` directly, not a projectivized shadow such as `(x,Y,S)`.

## Strongest objection

Freezing only the exceptional-divisor convention does not yet prove that the corrected package actually extends analytically to `\delta=0`, nor that the chosen reduced state is canonical. If the draft later decides that the package must retain an extra hidden visible scalar, then equality with bare `\widehat\Psi(m)` may still be too small.

## Needed for promotion

1. State a definition of `\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,\delta)` on `\delta\neq 0` using the corrected two-atom package and the same affine normalization class as `\widehat\Psi`.
2. Explicitly declare that `\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)` means the exceptional-divisor value after rewriting with `2\omega=\kappa\delta`.
3. Then the theorem statement `\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)` becomes precise; the remaining burden is proving extension and coincidence, not clarifying notation.

Honest verdict: the main missing freeze is not another coordinate on the one-pair side. It is the convention that `\delta=0` is read on the collision blow-up exceptional divisor, with `\kappa` held fixed there, for the corrected reduced package that is normalized to match `\widehat\Psi`.
