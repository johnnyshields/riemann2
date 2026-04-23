## Claim

From the current draft alone, the diagonal-collapse value of the actual corrected reduced two-atom package at `\delta=0` is **not proved** to be independent of `\kappa`, and the exact missing input is precisely a diagonal-collapse / merger theorem identifying that value with the one-pair reduced package. More sharply: swap-even analyticity in the collision/cancellation chart only yields a reduced germ of the form

\[
\mathcal R(m,\kappa,\delta^2),
\]

so the edge value `\mathcal R(m,\kappa,0)` is an a priori arbitrary analytic function of `\kappa`; nothing in the present paper forces it to be constant in `\kappa` or equal to the one-pair reduced value.

## Status

open

## Evidence

- The paper already isolates the weaker exact route as a continuity plus diagonal-collapse statement for the actual corrected two-atom quotient germ, with diagonal value equal to the one-pair quotient class and independent of amplitudes; this is conditional, not proved. See Proposition `conditional-exact-two-point-exclusion-qabs`.
- The stronger source-level route likewise identifies exact diagonal merger

\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h
\]

as the needed input. Again this is isolated, not proved.
- The naive source-summed corrected-block model cannot supply such a merger law: after whitening, the extracted finite-order coefficients are even analytic in the source weight, so one-atom linearity and coincident-atom additivity do not follow from that model.
- On the blow-up chart, swap-even analyticity only implies representation in `(m,\kappa,\delta^2)`. This does **not** force `\kappa`-independence of the `\delta=0` slice. The paper’s own expected edge laws for the actual corrected cubic/quintic defects already have explicit `\kappa`-dependence:

\[
\mathcal H_3(m,\kappa,0)=c'(m)-\frac{\kappa}{2}c(m),\qquad
\mathcal H_5(m,\kappa,0)=(A_5^{\mathfrak f})'(m)-\frac{\kappa}{2}A_5^{\mathfrak f}(m).
\]

So `\kappa`-independence cannot be formal from chart regularity and swap symmetry alone.
- Therefore the clean obstruction is exact: Bottleneck C reduces to proving that the actual corrected reduced package has diagonal collapse to the one-pair reduced package, not merely an analytic edge value depending on `\kappa`.

## Exact refs

- `paper/proof_of_rh.tex:11888-11992`
- `paper/proof_of_rh.tex:12042-12137`
- `paper/proof_of_rh.tex:12149-12227`
- `paper/proof_of_rh.tex:12447-12510`
- `paper/proof_of_rh.tex:12513-12610`
- `paper/proof_of_rh.tex:22472-22505`
- `paper/proof_of_rh.tex:24985-25030`
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:44-50`

## Dependencies

- A definition of the actual corrected reduced two-atom package on the collision/cancellation chart with enough regularity to descend to `(m,\kappa,\delta^2)`.
- An exact diagonal-collapse theorem for that reduced package.
- Or equivalently, a corrected package merger theorem at coincidence identifying the two-atom package with the one-pair reduced package.

## Strongest objection

This is a sharp obstruction, not a no-go theorem. The report shows only that the present draft does not force `\kappa`-independence. A future theorem could still prove it by adding an exact merger / functoriality statement for the actual corrected package.

## Needed for promotion

1. State the actual corrected reduced two-atom package germ explicitly on the collision/cancellation chart.
2. Prove its diagonal value at `\delta=0` is independent of `\kappa`.
3. Prove that common diagonal value equals the one-pair reduced package.
4. Then Bottleneck C becomes formal from the existing strengthened coincidence algebra.

Honest verdict: the single blocker is now exact. The current paper does not prove `\kappa`-independence of the `\delta=0` diagonal-collapse value. Symmetry and blow-up analyticity allow an arbitrary analytic `\kappa`-family there, and the missing theorem is precisely diagonal merger of the actual corrected reduced package to the one-pair reduced package.
