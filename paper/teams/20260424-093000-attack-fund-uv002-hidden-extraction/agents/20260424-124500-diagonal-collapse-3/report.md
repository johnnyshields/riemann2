## Claim

The exact Bottleneck C statement

\[
\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
\]

is one theorem-step away from the present package data. The single narrowest missing convention/theorem is a **canonical diagonal specialization (diagonal merger / collision-functoriality) for the actual corrected reduced two-atom package**: when the two atoms collide, the corrected reduced package must specialize to the one-pair strengthened datum at the merged atom, independent of the blow-up slope \(\kappa\).

## Status

open

## Evidence

- The paper already fixes the one-pair reduced target uniquely as
  \[
  \widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right).
  \]
- The strengthened coincidence algebra is already formal: if the corrected cubic/quintic/septic package agrees through the three levels used in Proposition `exact-strengthened-two-pair-coincidence`, then equality of reduced data follows automatically.
- The draft itself says the honest remaining order-`7` theorem is not raw septic equality but a provenance-sensitive package theorem such as “same reduced image germ at coincidence” or “collision-functoriality.”
- The blow-up chart already identifies the correct exceptional-divisor variables `(m,\kappa,\delta^2)` and shows that swap-even analytic corrected defects naturally descend to `\delta^2` with `\kappa=2\omega/\delta`.
- What is still missing is exactly the value at `\delta=0`: current hypotheses allow an arbitrary analytic exceptional-divisor term
  \[
  B(m,\kappa):=\widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0).
  \]
  Nothing in the present package data forces `B` to equal `\widehat\Psi(m)` unless one adds the diagonal specialization law.
- The naive source-summed whitened-coefficient model cannot supply that law, because its extracted coefficients are even analytic in the source weight and therefore cannot produce the required one-atom linear diagonal merger.

Concrete route once that law is supplied:

1. Define the actual corrected reduced package germ in the collision/cancellation chart by the corrected cubic/quintic/septic outputs reduced to the amplitude-invariant triple.
2. Use swap-even analyticity in `(m,\omega,\delta)` to descend it to an analytic germ `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,\delta^2)`.
3. Impose/prove the diagonal specialization
   \[
   \mathfrak P_2(a_1,m;a_2,m)\rightsquigarrow (a_1+a_2)F_m
   \]
   at the level of the actual corrected package, hence after reduction
   \[
   \widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
   \]
4. Then Bottleneck C follows formally, and the slogan “same reduced image germ at coincidence” becomes a theorem rather than a placeholder.

## Exact refs

- `paper/proof_of_rh.tex:10780-10809`
- `paper/proof_of_rh.tex:11368-11450`
- `paper/proof_of_rh.tex:11476-11585`
- `paper/proof_of_rh.tex:11888-12166`
- `paper/proof_of_rh.tex:12208-12227`
- `paper/proof_of_rh.tex:12447-12510`
- `paper/proof_of_rh.tex:12513-12610`
- `paper/proof_of_rh.tex:24985-25030`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-58`

## Dependencies

- A precise definition of the actual corrected reduced two-atom package germ in the blow-up chart.
- A diagonal specialization / collision-functoriality theorem for that package.
- No additional extractor-side theorem is needed for Bottleneck C itself.

## Strongest objection

Calling the blocker a “definition/convention” risks understating the real burden. For the actual corrected package, diagonal specialization is not presently a harmless notation choice; it is a substantive theorem because the naive source-summed model fails exactly at one-atom linearity / coincident-atom additivity.

## Needed for promotion

1. State the actual corrected reduced package germ explicitly in the blow-up variables `(m,\kappa,\delta^2)`.
2. Prove its diagonal specialization to the merged one-pair package at `\delta=0`.
3. Deduce `\kappa`-independence on the exceptional divisor, hence
   \(
   \widetilde{\Psi}^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
   \).

Honest verdict: the route is now exact. Bottleneck C is blocked by one package-side theorem only: canonical diagonal specialization of the actual corrected reduced two-atom package. Without it, the exceptional-divisor value remains a free analytic function of `\kappa`; with it, the target identity is formal.
