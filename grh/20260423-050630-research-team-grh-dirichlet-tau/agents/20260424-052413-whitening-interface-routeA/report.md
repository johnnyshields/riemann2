## Claim

The shortest safe theorem-facing hypothesis block for the paired source-plus-slot theorem is:

> **Local positivity/whitening interface.** Assume that for the paired corrected local family on a microscopic disk \(|s|<\rho_\chi/Q\), the paired corrected same-point blocks \(G_{\chi,m,\pm}^{\pair,\corr}(s)\) and mixed block \(N_{\chi,m}^{\pair,\corr}(s)\) are holomorphic, and that the same-point blocks remain uniformly positive definite there. Hence the holomorphic inverse square roots \((G_{\chi,m,\pm}^{\pair,\corr}(s))^{-1/2}\) are defined, and the paired corrected whitened block
> \[
> \widehat\Omega_{\chi}^{\pair,\corr}(s;m)
> :=
> (G_{\chi,m,-}^{\pair,\corr}(s))^{-1/2}
> N_{\chi,m}^{\pair,\corr}(s)
> (G_{\chi,m,+}^{\pair,\corr}(s))^{-1/2}
> \]
> is well-defined and holomorphic on the same disk. Assume further that the first-order paired value-channel derivative \(A_{\val,\chi}^{\pair}(m,\sigma)\) is defined for this whitened family.

What this guarantees:

- the paired whitened block is a well-posed local holomorphic object;
- whitening is legitimate because the same-point blocks stay positive/nondegenerate;
- the paired slot identity \(\Delta_{\chi}^{\pair}=S_{\chi}^{\pair}A_{\val,\chi}^{\pair}+R_{\chi}^{\pair}\) is at least well-formed.

What this does not guarantee:

- remainder dominance;
- quantitative corrected-whitening transport bounds;
- odd/transverse realization or boundary control;
- that same-point positivity/nondegeneracy follows from the compact paired source theorem alone.

## Status

conditional

Proved:

- The manuscript already proves the unpaired local template: holomorphy of corrected same-point and mixed blocks, uniform positive definiteness of the same-point blocks, holomorphic inverse square roots, and holomorphic whitening.
- The manuscript also already uses the corresponding local decomposition pattern \(\Delta_\zeta=S(m)A_{\val}+R_\zeta\) once the whitened object is defined.

Conditional on [paired analogue of the same local package]:

- The paired theorem can safely import the displayed interface as a hypothesis block.
- Under that hypothesis, the paired slot theorem may state its source-plus-slot identity without overclaiming denominator comparability or source data as a complete endpoint.

Missing:

- A manuscript proof that the compact paired source theorem itself implies the same-point positivity/nondegeneracy needed for whitening.
- A clean standalone paired spectral-gap stability lemma yielding the positivity package across the paired local family.
- A paired proof that the first-order value-channel derivative \(A_{\val,\chi}^{\pair}\) is available directly from the corrected local whitened family with no extra hidden admissibility inputs.

## Evidence

The notes agree on the same boundary.

- `paired_slot_hypotheses.md` says the paired slot theorem is not well-posed from the upstairs source theorem alone, and the minimal extra package must explicitly include microscopic holomorphy, same-point positivity/nondegeneracy, holomorphic whitening, and the first-order paired value derivative.
- `same_point_positivity.md` says same-point positivity is real but currently only as a perturbative manuscript-internal package built from baseline spectral gap, small variation, small perturbation, and holomorphic functional calculus; it is theorem-level transportable only as a conditional interface.
- `corrected_whitening_transport.md` says corrected-whitening transport is only a partial intermediate bundle and leaves slot realization, boundary control, odd/transverse realization, and remainder dominance separate.

So the clean safe theorem-facing interface is the local holomorphy-plus-positivity clause above, with an explicit non-guarantee paragraph. Anything shorter that compresses positivity into generic admissibility risks hiding the actual missing spectral-gap step; anything stronger that says source data alone supplies whitening overstates the current record.

## Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-29`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:31-59`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:68-77`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:7-24`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:25-46`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:6-27`
- `paper/proof_of_rh.tex:1392-1457` for the unpaired holomorphic-whitening template
- `paper/proof_of_rh.tex:1540-1565` and `paper/proof_of_rh.tex:1590-1621` for the local decomposition template \(\Delta=S A_{\val}+R\)
- Target deposit: `grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-052413-whitening-interface-routeA/report.md`

## Dependencies

- The paired corrected same-point and mixed blocks must already be defined.
- A microscopic holomorphy statement for those paired corrected blocks.
- A separate same-point positivity/nondegeneracy input on the same microscopic disk.
- Holomorphic functional calculus for the inverse square roots.
- Availability of the first-order paired value derivative \(A_{\val,\chi}^{\pair}\).

## Strongest objection

The proposed interface is still conditional because the current record does not show that the paired compact source package alone delivers the same-point spectral gap needed for positivity/nondegeneracy. If the theorem silently folds that gap into a vague `admissibility` phrase or into the source theorem itself, it will overstate what is presently proved.

## Needed for promotion

- A paired manuscript lemma or proposition proving the same-point positivity/nondegeneracy package on the microscopic disk.
- A paired holomorphic-whitening proposition matching the unpaired template with explicit notation.
- A precise paired definition or proposition for \(A_{\val,\chi}^{\pair}\) inside the whitened family.
- After those are written, the hypothesis block can likely be shortened to one sentence because the guarantees will have named upstream theorem labels.
