## Claim

The exact theorem obligation for Bottleneck C is the following canonical diagonal-specialization / collision-functoriality statement for the actual corrected two-atom package:

\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)
=
\mathcal R\bigl(\mathfrak P^{\corr}_2(a_1,m;a_2,m)\bigr)
=
\mathcal R\bigl((a_1+a_2)F_m\bigr)
=
\widehat\Psi(m),
\]

after writing \(2\omega=\kappa\delta\) in the collision/cancellation blow-up chart and analytically extending to \(\delta=0\). Equivalently: the reduced corrected two-atom package must commute with diagonal collision specialization, so its exceptional-divisor trace is \(\kappa\)-independent and equal to the one-pair datum. This is exactly what kills the free term

\[
B(m,\kappa):=\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0).
\]

## Status

heuristic

## Evidence

- The draft already isolates the honest remaining order-7/two-atom burden as a provenance-sensitive package theorem, specifically same reduced image germ at coincidence or collision-functoriality, not raw septic equality.
- The collision/cancellation blow-up analysis only yields parity/projective factorization for corrected defects of the form \(E=\delta^2\mathcal H(m,\kappa,\delta^2)\); this does not constrain the reduced package value at \(\delta=0\).
- The weaker exact two-point route identifies continuity plus diagonal collapse of the actual corrected two-atom quotient germ as the missing input. On the stronger source-level route, the decisive identity is diagonal merger \(\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h\).
- After reduction to the strengthened datum \(\widehat\Psi\), the same structural issue survives: unless the corrected two-atom package has canonical diagonal specialization, the exceptional-divisor value remains an arbitrary analytic function of \(\kappa\).
- Therefore the minimal theorem that removes the residual freedom is exactly: reduction commutes with collision merger on the actual corrected package. Any weaker hypothesis listed in the draft leaves room for a free \(B(m,\kappa)\).

## Exact refs

- `paper/proof_of_rh.tex:10780-10809` — honest order-7 target is same reduced image germ / collision-functoriality.
- `paper/proof_of_rh.tex:12139-12165` — weaker exact route requires continuity + diagonal collapse of the corrected two-atom quotient germ.
- `paper/proof_of_rh.tex:12168-12189` — stronger source-level route isolates diagonal merger `\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h`.
- `paper/proof_of_rh.tex:12431-12489` — blow-up chart and parity/projective factorization only give `\delta^2\mathcal H(m,\kappa,\delta^2)` for defects.
- `paper/proof_of_rh.tex:12513-12559` — remaining burden split; Bottleneck C is package-level coincidence/functoriality.
- `paper/proof_of_rh.tex:12586-12609` — reduced target datum is `\widehat\Psi`.
- `paper/proof_of_rh.tex:21277-21329` — remaining order-7 burden is package-level / provenance-sensitive, not another pointwise field.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:50-78` — current exact formulation of Bottleneck C and the free exceptional-divisor trace `B(m,\kappa)`.

## Dependencies

- A well-defined actual corrected two-atom package object `\mathfrak P_2^{\corr}` on the collision/cancellation blow-up chart.
- A reduction map `\mathcal R` from that package to the strengthened datum represented by `\widehat\Psi`.
- Analytic extension of `\widetilde\Psi^{\corr}_{\mathrm{red}}=\mathcal R\circ\mathfrak P_2^{\corr}` to `\delta=0` after `2\omega=\kappa\delta`.
- A genuine collision-merger theorem on coincident atoms, not just swap-evenness or quotient-visible continuity.

## Strongest objection

The report identifies the exact missing obligation, but it does not prove that the actual corrected package admits such a collision-functorial reduction. In particular, the draft’s current blow-up regularity and symmetry do not themselves produce the equality above, so the theorem shape could still be correct while the chosen package object is too weak or incorrectly normalized.

## Needed for promotion

1. Define `\widetilde\Psi^{\corr}_{\mathrm{red}}=\mathcal R\circ\mathfrak P_2^{\corr}` canonically on the collision/cancellation chart.
2. Prove analytic extension to the exceptional divisor `\delta=0` after `2\omega=\kappa\delta`.
3. Prove diagonal collision-functoriality:
   `\mathfrak P^{\corr}_2(a_1,m;a_2,m)` reduces to the merged one-pair package `(a_1+a_2)F_m`.
4. Conclude `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)` and hence eliminate the free trace `B(m,\kappa)`.

Honest verdict: Bottleneck C is now reduced to one exact package theorem only. The killer for `B(m,\kappa)` is not more blow-up analyticity, swap symmetry, or quotient continuity; it is the canonical statement that reduced corrected two-atom package formation commutes with diagonal collision merger, forcing the exceptional-divisor value to be the one-pair datum `\widehat\Psi(m)` and nothing else.
