# Claim

The exact missing convention for Bottleneck C is this.

Let the actual corrected reduced two-atom package be written on the collision/cancellation chart

\[
h_1=m-\frac{\delta}{2},\qquad h_2=m+\frac{\delta}{2},\qquad 2\omega=\kappa\delta,
\]

and assume its reduced representative is analytic and swap-even after blow-up, so for `\delta\neq 0` it factors through an analytic germ

\[
\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\omega,\delta)
=
\mathcal P^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,\delta^2).
\]

Then the notation

\[
\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)
\]

must mean the exceptional-divisor value

\[
\mathcal P^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0),
\]

not an arbitrary diagonal placeholder. The precise theorem statement is that this exceptional-divisor value is canonically normalized by diagonal collapse to the one-pair datum:

\[
\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\qquad\text{for all }(m,\kappa).
\]

Equivalently: the blow-up extension exists, is independent of the approach parameter `\kappa`, and its value on the exceptional divisor is the coincident-atoms one-pair package `\widehat\Psi(m)`.

# Status

heuristic

# Evidence

The draft already fixes the ingredients of this normalization but does not state them as one theorem-ready convention.

1. `\widehat\Psi(h)` is the amplitude-invariant one-pair datum, so it is the only diagonal target compatible with scalar normalization:

\[
\widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right).
\]

2. The collision/cancellation chart uses `(m,\omega,\delta)` with swap
`(m,\omega,\delta)\mapsto(m,-\omega,-\delta)`, and the blow-up parameter is
`\kappa=2\omega/\delta`.

3. For swap-even analytic corrected defects, the draft already records the exact blow-up pattern

\[
E(m,\omega,\delta)=\delta^2\,\mathcal H(m,\kappa,\delta^2),
\]

so the natural exceptional-divisor variable is `(m,\kappa)` and the value at `\delta=0` must be read by analytic continuation in `(m,\kappa,\delta^2)`.

4. The weaker exact two-point route already isolates the quotient-level requirement as continuity plus diagonal collapse of the corrected two-atom quotient germ to the one-pair germ. Bottleneck C is the reduced-package analogue of that same diagonal-collapse requirement.

5. Without this convention, the exceptional divisor still allows a free analytic term
`B(m,\kappa)`, so “same reduced image germ at coincidence” is underspecified. The missing statement is exactly that the exceptional-divisor section is the canonical diagonal one-pair section, not a `\kappa`-dependent family.

# Exact refs

- `paper/proof_of_rh.tex:11368-11512` (`\widehat\Psi` and its amplitude-invariant normalization)
- `paper/proof_of_rh.tex:12042-12137` (quotient-level continuity + diagonal collapse route)
- `paper/proof_of_rh.tex:12385-12445` (collision/cancellation chart)
- `paper/proof_of_rh.tex:12447-12511` (swap-even blow-up factorization through `\kappa=2\omega/\delta`)
- `paper/proof_of_rh.tex:12552-12610` (package-level coincidence target and minimal-core reformulation)
- `paper/proof_of_rh.tex:23072-23109` (package-level vanishing on coincident atoms on the residual fixed-shear corner)
- `paper/proof_of_rh.tex:24987-25030` (current finite-core queue phrased as edge-law + transport + package-level coincidence)

# Dependencies

- A theorem-level definition of the actual corrected reduced two-atom package on the punctured collision/cancellation chart.
- Analytic swap-even extension after substituting `2\omega=\kappa\delta`.
- A diagonal-collapse / collision-functoriality statement identifying the coincident-atoms package with the one-pair datum `\widehat\Psi(m)`.

# Strongest objection

The draft does not yet define the corrected reduced two-atom package as a canonical object on the blown-up chart, so the statement above still depends on choosing the right reduced package representative before speaking about its exceptional-divisor value. Until that object is fixed, one could hide gauge choices inside the symbol `\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}`.

# Needed for promotion

1. Define `\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}` canonically on `\delta\neq 0` in the collision/cancellation chart.
2. State explicitly that `\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)` means analytic continuation of the blown-up germ in `(m,\kappa,\delta^2)` to `\delta=0`.
3. Prove diagonal collapse / collision-functoriality:

\[
\mathcal P^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

4. Then Bottleneck C becomes a precise theorem statement rather than a slogan.

Honest verdict: the gap is now sharply localized. The missing issue is not another reduced coordinate search; it is the convention that the exceptional-divisor value is the analytically continued blow-up value and must be canonically anchored to the diagonal one-pair package `\widehat\Psi(m)`, hence independent of `\kappa`.
