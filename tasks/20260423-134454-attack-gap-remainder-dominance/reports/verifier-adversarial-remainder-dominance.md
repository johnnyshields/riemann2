Claim

After exact identification of the scalar occupying the manuscript's `S(m)` slot, remainder dominance is the next bottleneck only in a scoped sense: it is the next unresolved step in the calibrated value-channel comparison, provided the existing local whitening, denominator, fixed-scale, and cutoff hypotheses remain available. It is not yet safe to state, without that scope, that remainder dominance is the next bottleneck for the whole argument.

Status

open

Evidence

proved:

- The paper already contains the exact decomposition `\Delta_\zeta=S(m)A_{\val}(x)+R_\zeta` once the correct scalar slot is known, so no second leading-coefficient theorem is missing inside the current zeta architecture.
- The canonical calibration theorem reduces the toy/zeta comparison to the condition `\Psi_{x,d}(R_\zeta)=o((x/B)S(m))` and then yields `u^2\asymp (x/B)S(m)`.
- The sharpened remainder corollary further reduces this to the explicit inequality `S_2=o(xQ^2S(m))` in the fixed-scaled regime `x=B_\zeta(m)\sigma`, `|\sigma|\asymp Q^{-1}`.

conditional on named hypotheses:

- Calling remainder dominance the next bottleneck is correct for the calibration subchain only if one keeps the fixed-scale hypotheses in Corollary `cor:sharpened-calibration-remainder`, the small-`x` denominator nonvanishing from Proposition `prop:pairing`, the whitening-transfer hypotheses behind Proposition `prop:whitened-mixed-transfer`, the comparability `B_\zeta(m)\asymp Q`, and the cutoff-compatibility package used in Proposition `prop:calibration-remainder-cutoff`.
- Even inside the zeta draft, Proposition `prop:calibration-remainder-cutoff` is not unconditional. It assumes one may choose `R` with `R^3\gg 1/(xQ\,S(m))` and that the background term is negligible.
- For any family-level roadmap sentence, route B is still too optimistic unless it says explicitly that the family preserves the same local whitening architecture and denominator behavior. From the current scope alone, that has not been verified.

missing:

- An unconditional theorem in the regime actually used later that proves `S_2=o(xQ^2S(m))`, or directly proves `\Psi_{x,d}(R_\zeta)=o((x/B)S(m))`.
- A variable-`x` rewrite of the calibration chain. The paper itself states that if `x` must shrink to keep `|u|<u_0(D)`, then one still has to re-check uniform pairing, transfer, remainder, and cutoff compatibility in that regime.
- Any justification for treating remainder dominance as the unique next bottleneck for the whole program. The positive-`S` note explicitly keeps the odd/transverse package and family-specific denominator/whitening/boundary control as separate remaining blocks.

Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:17-38,42-50`
- `/mnt/c/workspace/riemann2/tasks/20260423-134454-attack-gap-remainder-dominance/reports/gap-remainder-dominance-routeA.md:16-25,77-87`
- `/mnt/c/workspace/riemann2/tasks/20260423-134454-attack-gap-remainder-dominance/reports/gap-remainder-dominance-routeB.md:7-17,27-37,98-113`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:361-371` (`thm:tail-curvature`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:601-659` (`lem:Aval-small-x`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:661-794` (`prop:pairing`, `prop:canonical-calibration`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:796-850` (`prop:calibration-remainder-cutoff`, `rem:status-sharpened-calibration-remainder`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1683` (`prop:corrected-local-decomposition`, `prop:cutoff-compatibility`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1693-1754` (`prop:whitened-mixed-transfer`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2050-2209` (`cor:sharpened-calibration-remainder`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2214-2322` (`prop:boundary-estimate`, `prop:odd-expansion`)
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5499-5598` (`rem:wip-calibration-small-u`)

Dependencies

- Exact source-level identification of the background-subtracted scalar that truly occupies the draft's `S(m)` slot.
- Small-`x` pairing and denominator nondegeneracy on compact `d`-ranges.
- Baseline same-point and mixed-block scales, uniform positive definiteness, and perturbation estimates needed for the `Q^{-3}` whitening transfer.
- The comparison `B_\zeta(m)\asymp Q` used when converting `S_2/Q^3` into the normalized remainder ratio.
- A cutoff choice compatible with the fixed core and with `R^3\gg 1/(xQ\,S(m))` when that route is used.
- If `x` varies with `m`, uniformity of all previous items for `0<x\le x_0(D)`.
- For any family-level statement beyond zeta: family analogues of denominator comparability, whitening transfer, and source-level control of the curvature/tail quantity replacing `S_2`.

Strongest objection

The hidden assumption load is still too large for the slogan "after exact scalar identification, remainder dominance is the next bottleneck" to stand unqualified. In the current draft, remainder dominance is isolated only after importing a fixed-scale regime, denominator nondegeneracy, whitening-transfer bounds, `B_\zeta(m)\asymp Q`, and either an unproved direct estimate `S_2=o(xQ^2S(m))` or a cutoff choice satisfying `R^3\gg 1/(xQ\,S(m))`. Moreover, `rem:wip-calibration-small-u` shows that if the argument needs shrinking `x`, then the whole calibration package must be re-proved uniformly. So from the present scope alone, remainder dominance is the next bottleneck for one subchain, not yet the uniquely isolated next bottleneck for the overall program.

Needed for promotion

1. Name the scope explicitly: calibrated value-channel comparison, not the whole endgame.
2. Name the hidden assumptions explicitly whenever remainder dominance is called the next step: fixed-scale or variable-`x` regime, denominator nondegeneracy, whitening-transfer hypotheses, `B_\zeta(m)\asymp Q`, and cutoff admissibility.
3. Prove either the direct target `S_2=o(xQ^2S(m))` in the regime actually used, or a direct calibrated estimate implying `\Psi_{x,d}(R_\zeta)=o((x/B)S(m))`.
4. If `x` must shrink to keep `|u|<u_0(D)`, upgrade the calibration, transfer, and cutoff arguments uniformly in `x` before treating remainder dominance as closed.
5. Strongest safe roadmap sentence: if a source theorem supplies the exact scalar in the manuscript's `S(m)` slot, and if the same local calibration/whitening hypotheses remain valid in the admissible microscopic regime, then the next unresolved step in the calibrated comparison is to prove the calibrated remainder negligible, equivalently `S_2=o(xQ^2S(m))` in the zeta model.
6. Honest verdict: yes for the calibrated scalar-comparison subchain, no for the whole program from the current scope alone. The main hidden assumptions are fixed-scale versus variable-`x` uniformity, denominator/whitening comparability, `B_\zeta(m)\asymp Q`, and cutoff admissibility.
