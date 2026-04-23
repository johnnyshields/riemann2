Claim

One theorem candidate unifies Bottlenecks B and C: if the actual corrected two-atom package admits a pre-blow-up analytic extension
\[
\mathfrak P_2(a_1,h_1;a_2,h_2)
\]
with swap symmetry, one-amplitude collapse, and exact diagonal merger
\[
\mathfrak P_2(a_1,h;a_2,h)=(a_1+a_2)F_h,
\]
then:
1. the corrected cubic/quintic defects vanish on the exact fixed-shear diagonal, giving the diagonal coincidence input needed for Bottleneck B;
2. the reduced corrected two-atom package has diagonal value
\[
\widetilde\Psi^{\mathrm{corr}}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
\]
independent of the blow-up slope \(\kappa\), which is exactly Bottleneck C.

Sharp obstruction: the present draft does not supply this theorem for the actual corrected package, and the naive source-summed whitened-block model cannot supply it, because its extracted finite-order coefficients are even analytic in the source weight and therefore cannot realize the required linear one-atom / diagonal-merger law.

Status

heuristic

Evidence

- Lemma `minimal-source-level-two-point-criterion` proves that swap symmetry, one-amplitude collapse, and diagonal merger force the interaction remainder to factor as \(a_1a_2(h_1-h_2)^2\mathcal J_2\). This is the exact pre-blow-up divisibility needed for both the diagonal defect vanishing and the blown-up \(\delta^2\)-law.
- On the residual exact fixed-shear involutive branch, the draft already proves that any state-local defect functional vanishing at the diagonal gives \(E_{12}^{(3)},E_{12}^{(5)}=O((h_1-h_2)^2)\); under the stronger merger law, the interaction remainder dies identically along the branch. So Bottleneck B reduces to exact diagonal merger for the actual corrected package, not to further quotient transport work.
- For Bottleneck C, diagonal merger identifies the coincident two-atom package with the one-pair package of total amplitude \((a_1+a_2)F_m\). Because \(\widehat\Psi\) is amplitude-invariant under scalar rescaling, the reduced diagonal value is forced to be \(\widehat\Psi(m)\), hence independent of the exceptional-divisor parameter \(\kappa\).
- The present sharp negative fact is that the naive source-summed corrected-block route produces whitened finite-order coefficients that are even analytic in the source weight \(a\); therefore it cannot produce analytic one-atom linearity or coincident-atom additivity unless the package vanishes identically. This blocks the most obvious proof of the unifying theorem.
- The collision-cancellation chart remark already isolates the blown-up variables \((m,\omega,\delta)\) and shows that swap-even analytic defects become \(\delta^2\mathcal H(m,\kappa,\delta^2)\). The current report sharpens that observation: the missing exact input is pre-blow-up diagonal merger, whose quotient consequence is the \(\kappa\)-independent exceptional value.

Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:11889-12040`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:12149-12227`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:12385-12510`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:21736-21763`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:22409-22529`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:24987-25030`
- `/mnt/c/workspace/riemann2/paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:22-55`
- `/mnt/c/workspace/riemann2/paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:90-115`

Dependencies

- The actual corrected two-atom package must be defined pre-blow-up, not only through the naive source-summed whitened coefficients.
- The package must satisfy exact one-amplitude collapse and exact diagonal merger at coincident atoms.
- The reduced package on the blow-up side must be the amplitude-invariant reduction compatible with `\widehat\Psi`.

Strongest objection

The implication chain is clear, but the theorem is not proved for the actual corrected package. The current draft only proves the consequence once state-locality / merger is assumed, and the most obvious candidate lift is ruled out by even-amplitude parity. So the live issue is not whether pre-blow-up diagonal merger would be sufficient; it is how to realize that merger for the honest corrected package rather than for a toy or source-summed surrogate.

Needed for promotion

1. Define the honest corrected two-atom package as a pre-blow-up analytic object on normalized data.
2. Prove exact one-amplitude collapse and exact diagonal merger for that package.
3. Check that the reduced package extracted from this object agrees with the existing `\widehat\Psi` reduction on one-pair data.
4. Then Bottlenecks B and C collapse formally from the existing fixed-shear and blow-up algebra.

Honest verdict: the unifying theorem candidate is structurally correct and sharp. I do not have a proof for the actual corrected package. The sharp blocker is now exact: without a pre-blow-up diagonal merger theorem, the exceptional reduced value can vary with \(\kappa\); with it, both the exact fixed-shear diagonal coincidence and the `\kappa`-independent reduced diagonal value follow at once.
