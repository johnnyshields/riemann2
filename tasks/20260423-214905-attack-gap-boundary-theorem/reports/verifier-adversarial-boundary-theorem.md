## Claim

The right standalone target after corrected whitening is not the boundary estimate by itself, but a family-specific corrected transverse realization-and-boundary package. That package is the correct next bottleneck only in the scoped sense that corrected whitening already supplies holomorphic whitening and the post-`\Phi_K` transfer scale, while three further clauses still have to be supplied for the chosen family/slot: realization of the odd transverse scalar, annihilation of the leading value channel in that realized slot, and the microscopic boundary domination that turns the `S_2/Q^3` transfer bound into the final boundary majorant. From corrected whitening alone, the boundary theorem conclusion does not yet transport.

## Status

open

## Evidence

### Proved

In the zeta draft, Proposition `boundary-estimate` is the first actual boundary theorem for the corrected transverse scalar `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))`. Its proof uses more than the narrow corrected-whitening bundle. It explicitly calls on:

- corrected local decomposition, to isolate `S(m)A_{\val}+R_\zeta` inside the full corrected cutoff-dependent scalar;
- cutoff compatibility, to keep auxiliary/tail/jet/error terms internal rather than external remainders;
- transverse value-channel vanishing `\Phi_K(A_{\val})=0`;
- whitened mixed-block transfer at scale `S_2/Q^3`;
- the final domination step `S_2\ll L(m)S(m)^2` on `|s|=\rho_0/Q`.

The transport notes already separate these layers. `corrected_whitening_transport.md` identifies the safe corrected-whitening bundle as denominator comparability plus omitted-smooth holomorphy, holomorphic corrected whitening with positive same-point blocks, and preserved post-`\Phi_K` transfer scale, while listing value-channel slot realization, odd-scalar boundary control, odd/transverse realization, and remainder dominance as still separate. `odd_package_transport.md` then identifies the next independent bottleneck as a family-specific corrected transverse realization-and-boundary theorem.

### Conditional on extra family-specific input

The package is the right next standalone target provided it is stated with the missing clauses exposed. The strongest safe wording I see now is:

`After corrected whitening, the next independent bottleneck is a family-specific corrected transverse realization-and-boundary package: realize the corrected odd holomorphic transverse scalar in the chosen slot, prove the corresponding transverse value-channel cancellation and cutoff-internalization for the full corrected object, and establish the microscopic boundary bound needed for the odd Cauchy/projector machinery.`

This is stronger than saying only `boundary theorem`, but weaker than saying the whole odd package transports. Under that scoped package, the downstream odd expansion and projector/cancellation algebra remain plausible universal consequences, because the paper's Proposition `odd-expansion` uses only oddness, holomorphy, and the boundary estimate once the scalar is already realized.

### Missing

What is still missing from corrected whitening alone is exactly what blocks the boundary-theorem conclusion as a transport claim.

First, corrected whitening does not by itself realize the relevant odd transverse scalar in the family-specific slot. In the paper the scalar is defined as `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))`, but the transport notes explicitly warn that value-channel slot realization remains separate.

Second, corrected whitening does not by itself prove the analogue of `\Phi_K(A_{\val})=0` in the realized slot. Without that cancellation, one cannot safely replace the full corrected scalar by the non-leading remainder at the boundary stage.

Third, corrected whitening does not by itself prove the boundary domination step. It gives only the transfer-scale bound
`\Phi_K(\widehat\Omega^{\corr}-\widehat\Omega^{(0)})\ll S_2/Q^3`; converting this into the final boundary majorant requires the additional comparison `S_2\ll L(m)S(m)^2` in the corrected regime.

For that reason the claims that need scoped weakening are:

- `the boundary theorem is the right next standalone target after corrected whitening`; safe weakening: `the right next standalone target is the corrected transverse realization-and-boundary package, of which the boundary estimate is one clause`;
- `corrected whitening transports the odd package`; safe weakening: `corrected whitening transports only the holomorphic-whitening and post-\Phi_K transfer-scale layer`;
- `the odd package transports automatically after source theorem plus positive S`; safe weakening: `the odd germ/projector algebra transports once the family supplies the realized odd scalar and its microscopic boundary control`;
- any claim that the final boundary majorant follows from local whitening data alone; safe weakening: `from local whitening data alone one only gets the `S_2/Q^3` transfer scale, not the final boundary bound`.

## Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-45`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-27`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:8-49`
- `tasks/20260423-214905-attack-gap-boundary-theorem/reports/gap-boundary-theorem-routeA.md:15-49`
- `tasks/20260423-214905-attack-gap-boundary-theorem/reports/gap-boundary-theorem-routeB.md:11-34`
- `paper/proof_of_rh.tex:567-598` (`cor:PhiK-Aval-zero`)
- `paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`)
- `paper/proof_of_rh.tex:1497-1622` (`prop:corrected-local-decomposition`)
- `paper/proof_of_rh.tex:1624-1683` (`prop:cutoff-compatibility`)
- `paper/proof_of_rh.tex:1693-1754` (`prop:whitened-mixed-transfer`)
- `paper/proof_of_rh.tex:2050-2210` (`cor:sharpened-calibration-remainder`)
- `paper/proof_of_rh.tex:2214-2322` (definition of `H_m`, `prop:boundary-estimate`, `prop:odd-expansion`)

## Dependencies

- corrected-whitening package: denominator comparability, omitted-smooth holomorphy, holomorphic corrected whitening, positive same-point blocks, preserved post-`\Phi_K` transfer scale
- family-specific realization of the corrected odd/transverse scalar in the chosen slot
- family-specific analogue of transverse value-channel cancellation
- cutoff-internalization of auxiliary/tail/jet/error terms into the full corrected scalar used at the boundary stage
- family-specific boundary domination converting `S_2/Q^3` into the final majorant

## Strongest objection

The main objection is packaging ambiguity. Because the paper presents the boundary proposition immediately after the corrected-whitening transfer results, one could say that calling the combined realization-and-boundary package the `next target` merely repackages the same mathematics. But from the transport scope alone that objection fails: the proof of the boundary proposition uses hypotheses not contained in the narrow corrected-whitening bundle, and the transport notes themselves isolate those missing pieces. So the stronger statement `corrected whitening already gets us to the boundary theorem` is unsupported from that scope alone.

## Needed for promotion

- State the next theorem target with all three extra clauses visible: realized odd scalar, transverse value-channel cancellation/cutoff-internalization, and microscopic boundary domination.
- Keep the phrase `boundary theorem` scoped to the zeta draft unless those clauses are already built into the theorem statement for the target family.
- Avoid any wording that suggests automatic transport of the final boundary majorant from local corrected whitening alone.
- Once a family-specific package is proved, then and only then promote the downstream statements that odd Cauchy coefficient bounds and the `N`-point projector/cancellation mechanism transport.

Honest verdict: yes, the corrected transverse realization-and-boundary package is the right standalone target after corrected whitening, but only as a family-specific package broader than the boundary estimate alone. The strongest safe wording is that corrected whitening is only a partial intermediate bundle, and the next independent bottleneck is realization plus slot cancellation plus microscopic boundary control. Any wording that treats the boundary theorem, or the odd package, as automatic from corrected whitening alone needs scoped weakening.
