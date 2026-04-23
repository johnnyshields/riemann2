## Claim

With the exceptional-divisor convention frozen so that `\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)` means the blow-up value obtained after substituting `2\omega=\kappa\delta` and analytically extending to `\delta=0`, the theorem

\[
\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]

is mathematically well-posed but is **not proved by the current Bottleneck C draft material**. The sharp exact blocker is that the present hypotheses still allow a free analytic exceptional-divisor trace

\[
B(m,\kappa):=\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0),
\]

so neither `\kappa`-independence nor equality to `\widehat\Psi(m)` follows without a genuine diagonal-merger / collision-functoriality theorem for the actual corrected two-atom package.

## Status

open

## Evidence

- The one-pair reduced datum `\widehat\Psi` is canonical and amplitude-invariant, so it is the correct target on the diagonal once a corrected two-atom reduced package is known to specialize to the merged one-pair package.
- The collision/cancellation blow-up chart already identifies the right variables: swap-even analytic corrected data descend to analytic germs in `(m,\kappa,\delta^2)` with `\kappa=2\omega/\delta`.
- But the paper only reaches theorem-level statements of the form “same reduced image germ at coincidence” / “collision-functoriality” as future targets; it does not prove a corrected reduced two-atom package theorem forcing the value at `\delta=0`.
- Therefore, after blow-up one may still write abstractly

\[
\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,\delta)=B(m,\kappa)+\delta^2R(m,\kappa,\delta^2),
\]

with `B` analytic. This is compatible with the currently cited symmetry/analyticity structure and leaves the exceptional-divisor value unconstrained.
- The paper's own exact local criterion isolates what would remove this freedom: swap symmetry, one-amplitude collapse, and diagonal merger for the actual corrected two-atom package. Under that stronger input, diagonal specialization to `\widehat\Psi(m)` would be formal because `\widehat\Psi` is invariant under scalar rescaling of the merged one-pair package.
- The naive source-summed corrected-block model cannot supply that missing merger theorem: its extracted finite-order coefficients are even in the source weight, so it cannot produce the required linear one-atom / coincident-atom merger law.

## Exact refs

- `paper/proof_of_rh.tex:11368-11585` — definition and exact coincidence algebra for `\widehat\Psi`.
- `paper/proof_of_rh.tex:11888-12209` — minimal finite-order two-point criterion; swap symmetry + one-amplitude collapse + diagonal merger are exactly the sufficient package identities.
- `paper/proof_of_rh.tex:12431-12510` — blow-up chart and analytic form `E=\delta^2\mathcal H(m,\kappa,\delta^2)`.
- `paper/proof_of_rh.tex:12513-12610` — Bottleneck C is explicitly framed as same reduced image germ / collision-functoriality for `\widehat\Psi`.
- `paper/proof_of_rh.tex:24522-24543` and `24985-25030` — current queue summary: the live burden is package-level coincidence/functoriality, and the naive source-summed route is ruled out.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-60` — current exact Bottleneck C formulation and the frozen exceptional-divisor convention.

## Dependencies

- A canonically defined actual corrected reduced two-atom package germ on the blow-up chart.
- Analytic extension/continuity of that package to the exceptional divisor in `(m,\kappa,\delta)` or equivalently `(m,\kappa,\delta^2)`.
- A real diagonal-merger / collision-functoriality theorem for coincident atoms in the actual corrected package, before or at reduction.

## Strongest objection

This is an obstruction from the presently read material, not a proof that the true corrected package fails diagonal specialization. A stronger theorem in the underlying corrected package, not yet present in the draft, could still force `B(m,\kappa)=\widehat\Psi(m)`. So the result is sharp only as a **current-draft obstruction**.

## Needed for promotion

1. State the actual corrected reduced package `\widetilde{\Psi}^{\corr}_{\mathrm{red}}` explicitly on `\delta\neq 0` in the collision/cancellation blow-up chart.
2. Prove that its exceptional-divisor value is canonically the merged one-pair reduced datum.
3. Equivalently, prove diagonal merger / collision-functoriality for the actual corrected two-atom package strongly enough to imply

\[
\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

Honest verdict: with the convention frozen, the theorem statement is precise. I do not see a proof from the current Bottleneck C paper material. The exact remaining freedom is one analytic exceptional-divisor trace `B(m,\kappa)`, and the exact missing input is a genuine diagonal-merger / collision-functoriality theorem for the actual corrected package.
