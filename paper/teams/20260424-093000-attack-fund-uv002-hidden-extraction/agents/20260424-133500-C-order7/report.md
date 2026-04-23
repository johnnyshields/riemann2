## Claim

Bottleneck C does **not** currently close even through order \(7\) from the draft's existing package laws alone. The current notation already isolates the correct order-\(7\) reduced datum,
\[
\widehat\Psi(h)=\left(\frac{u_5(h)}{c(h)},\frac{v_5(h)}{c(h)},\frac{\Delta_7(h)}{c(h)^2}\right),
\]
and Proposition `exact-strengthened-two-pair-coincidence` proves order-\(7\) coincidence **if** the actual corrected cubic/quintic/septic package satisfies exact merger at coincidence. What remains open is exactly that merger / diagonal-collapse theorem for the actual corrected two-atom package.

## Status

open

## Evidence

- The draft defines the amplitude-invariant reduced order-\(7\) package `\widehat\Psi` using only `c`, `A_5^{\mathfrak f}`, and the gauge-invariant septic determinant `\Delta_7`; this is the canonical current-package notation for order \(7\).
- Proposition `Exact strengthened two-pair coincidence through order 7` proves `\widehat\Psi(h_1)=\widehat\Psi(h_2)` from exact cubic, quintic, and septic quotient identities. So the order-\(7\) algebra itself is already formal once exact package merger is granted.
- The minimal source criterion then identifies the exact missing input: swap symmetry, one-amplitude collapse, and diagonal merger
  \[
  \mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h.
  \]
- The draft explicitly says this merger statement is still unproved for the actual corrected cubic/quintic/septic package, and also records that the naive source-summed corrected-block model cannot prove it because its extracted one-atom finite-order coefficients are even in the source weight, so the required linear diagonal law is unavailable.
- On the current queue wording, Bottleneck C has already been sharpened to the exceptional-divisor diagonal specialization
  \[
  \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
  \]
  and the collation says the obstruction is still a free analytic exceptional-divisor trace `B(m,\kappa)`. That is the same obstruction seen at order \(7\): the reduced datum is correct, but diagonal collapse is not forced.

## Exact refs

- `paper/proof_of_rh.tex:7048-7062`
- `paper/proof_of_rh.tex:11368-11585`
- `paper/proof_of_rh.tex:11888-11992`
- `paper/proof_of_rh.tex:11994-12189`
- `paper/proof_of_rh.tex:12513-12579`
- `paper/proof_of_rh.tex:24518-24540`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:43-63`

## Dependencies

- Exact merger / diagonal-collapse theorem for the actual corrected two-atom cubic/quintic/septic package.
- Analytic collision/cancellation blow-up convention that canonically defines the exceptional-divisor value of the corrected reduced package.

## Strongest objection

The proposition proving order-\(7\) coincidence is conditional on exact vanishing of the corrected cubic/quintic/septic interaction package at coincidence. The current draft does not derive that from existing corrected-block formulas, and the naive weighted one-atom route is explicitly blocked. So one cannot currently upgrade the order-\(7\) package notation into an actual theorem for Bottleneck C.

## Needed for promotion

1. State the actual corrected reduced two-atom package on the collision/cancellation blow-up chart with a fixed exceptional-divisor convention.
2. Prove diagonal merger / collision-functoriality at coincidence for its cubic/quintic/septic package, equivalently the order-\(7\) specialization to the one-pair datum `\widehat\Psi(m)`.
3. Then the existing order-\(7\) coincidence algebra already yields the order-\(7\) version of Bottleneck C.

Honest verdict: the current package notation is already sufficient to **state** the order-\(7\) version of Bottleneck C sharply, but not to **prove** it. The exact blocker is still diagonal merger of the actual corrected cubic/quintic/septic two-atom package, i.e. the free exceptional-divisor trace survives even at order \(7\).
