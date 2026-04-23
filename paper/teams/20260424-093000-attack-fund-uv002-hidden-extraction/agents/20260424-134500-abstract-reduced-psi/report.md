## Claim

The strongest current clean theorem statement for Bottleneck C is the abstract reduced-`\widehat\Psi` coincidence theorem, in the exceptional-divisor normalization:

\[
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

Here `\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)` means the blow-up value of the actual corrected reduced two-atom package after writing `2\omega=\kappa\delta` and analytically extending to `\delta=0`. This is strictly sharper than the slogan “same reduced image germ at coincidence” and is the clean abstract theorem target; the enlarged proxy package `\widetilde\Psi_{\min}` is not the main statement.

## Status

open

## Evidence

- `\widehat\Psi(h)=(u_5/c,v_5/c,\Delta_7/c^2)` is already the paper's canonical amplitude-invariant strengthened datum for the downstream multi-pair/minimal-core problem, so any clean coincidence theorem should be stated in terms of `\widehat\Psi`, not an ad hoc enlargement.
- The exact two-pair algebra already proves that vanishing of the cubic/quintic/septic corrected defects forces equality of `\widehat\Psi`; the paper also has the defect-thickened identities measuring failure of equality coordinatewise.
- The current convergence files sharpen Bottleneck C from the vague form “same reduced image germ at coincidence” to the exact diagonal-specialization identity above.
- The same convergence also isolates the exact obstruction: under present analyticity/swap-evenness hypotheses one may still have a free exceptional-divisor trace

\[
B(m,\kappa):=\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0),
\]

so the theorem is well-posed but not yet proved.

## Exact refs

- `paper/proof_of_rh.tex:11368-11585` — definition of `\widehat\Psi` and exact strengthened two-pair coincidence through order `7`.
- `paper/proof_of_rh.tex:11587-11827` — defect-thickened strengthened coincidence identities and good-patch consequence.
- `paper/proof_of_rh.tex:12447-12610` — current theorem shaping: good-patch edge law, exact fixed-shear package theorem, and provenance-sensitive package theorem; `\widehat\Psi` named as the correct downstream datum.
- `paper/proof_of_rh.tex:24985-25030` — endgame compression: live package-side target is package-level coincidence/functoriality, not another mixed lane.
- `paper/proof_of_rh.tex:26369-26398` — current endgame status: quotient-level order-`7` package is canonically closed; remaining issue is beyond raw septic representative choice.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:45-62` — latest exact convergence for Bottleneck C.
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:107-115` — Bottleneck C in the current queue.

## Dependencies

- A canonical definition of the actual corrected reduced two-atom package `\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}` on the collision/cancellation blow-up chart.
- Analytic extension in `(m,\kappa,\delta^2)` to the exceptional divisor `\delta=0`.
- A genuine diagonal-merger / collision-functoriality theorem for the actual corrected two-atom package forcing the exceptional-divisor value to equal the one-pair datum `\widehat\Psi(m)`.

## Strongest objection

The paper does not yet prove that the corrected reduced package has canonical diagonal specialization at coincidence. With only the present blown-up analyticity and swap-evenness framework, the exceptional-divisor value can still be an arbitrary analytic function `B(m,\kappa)`, so neither `\kappa`-independence nor equality to `\widehat\Psi(m)` follows formally.

## Needed for promotion

1. Define `\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}` canonically on `\delta\neq 0` in the collision/cancellation chart.
2. Freeze the exceptional-divisor convention: substitute `2\omega=\kappa\delta` and analytically extend to `\delta=0`.
3. Prove diagonal merger / collision-functoriality for the actual corrected two-atom package, yielding

\[
\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m).
\]

4. Then cite the existing strengthened coincidence algebra to recover the slogan form “same reduced image germ at coincidence” and proceed to the hidden extraction theorem.

Honest verdict: the clean abstract theorem target is now exact. The strongest current statement is the exceptional-divisor identity `\widetilde{\Psi}^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)`, not any enlarged proxy theorem. It is still open; the sole exact blocker is the missing diagonal-merger / collision-functoriality theorem for the actual corrected two-atom package.
