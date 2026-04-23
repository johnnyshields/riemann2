# Claim

The strongest safe wording is:

`The paired value-channel derivative is locally definable only after one fixes a paired background scalar S_\chi^{\pair}(m), a pure paired value-direction through the corrected local block, and the local whitening admissibility package. So the derivative notion is local after the direction is fixed, but the present record does not support calling that direction itself purely local or source-free.`

More explicitly:

- purely local, once fixed: first-order differentiation of the paired corrected whitened block inside a microscopic holomorphic/whitenable local family;
- not yet purely local: the choice of what counts as the `pure paired value channel`, what is frozen under that perturbation, and how the paired background subtraction `S_\chi^{\pair}(m)=q_\chi^{\pair}(m)-B_\chi^{\pair}(m)` is normalized.

So the safe theorem-facing formulation is not `the paired value channel is canonically local`. It is `after fixing the paired source-normalized value parameter and the local whitening interface, one may define the first derivative in that direction.`

# Status

conditional

# Evidence

Proved from the cited manuscript and notes:

- In the manuscript, `A_{\val}` is introduced only after a specific perturbation has already been chosen: `q_1=q_2=B+\alpha`, with derivative and curvature data frozen at background level. So even there, the derivative is local only relative to a named parameterization of the value direction, not from locality alone.
- The corrected local decomposition then expands the corrected whitened block around background value `S(m)=0` and identifies the first-order coefficient with `A_{\val}`. This proves the local algebra point: once an admissible local family and a value-direction are fixed, the derivative is a local first-order object.
- The paired notes repeatedly say the exact paired slot theorem is not well-posed from the paired source theorem alone, and that one must add explicit local hypotheses: microscopic holomorphy, same-point positivity/nondegeneracy, holomorphic whitening, and the first paired value derivative.
- The same notes also say same-point positivity/nondegeneracy is not supplied by denominator holomorphy alone and should remain an explicit local whitening clause. Hence even the local derivative language already sits on top of a nontrivial admissibility package.
- The positivity note sharpens the obstruction further: the reusable local blueprint still imports source-normalized background/core data and the manuscript's `A_val` interface. That is direct evidence against calling the paired value-channel parameterization source-free.

Conditional on a paired analogue of the manuscript's setup:

- One may safely define
  `A_{\val,\chi}^{\pair}(m,\sigma)=\left.\partial_\alpha \widehat\Omega_{\chi,\alpha}^{\pair,\corr}(m,\sigma)\right|_{\alpha=0}`
  provided `\alpha` has already been specified as the pure paired value-channel deformation and the corrected same-point/mixed blocks admit holomorphic whitening on the microscopic disk.
- Under that conditional setup, the derivative itself is local and first-order; no calibration, boundary estimate, or odd-channel claim is built into the definition.

Missing:

- A theorem-ready paired definition of the pure value perturbation matching the manuscript's specificity: what parameter varies, which local blocks depend on it, and exactly which data are frozen.
- A proof that this perturbation can be chosen canonically from local paired data alone, without importing source-level normalization choices from `B_\chi^{\pair}` and `S_\chi^{\pair}`.
- A paired theorem deriving the whitening admissibility package from actual Dirichlet-family source data.
- A paired statement showing that any further symmetry property, such as a `\Phi_K(A_{\val,\chi}^{\pair})=0` analogue, survives under the chosen paired parameterization.

Honest verdict: the derivative can be described locally only after a source-normalized value direction has already been fixed. On the present record, the parameterization itself is not yet purely local; it already bakes in family-specific choices.

# Exact refs

- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:446-469`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:471-565`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1458`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1531-1606`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1636-1644`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_aval.md:7-29`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-29`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:31-59`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:68-77`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/whitening_interface.md:7-28`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/same_point_positivity.md:7-46`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_proof_plan.md:8-36`

# Dependencies

- The manuscript distinction between `choosing a perturbation direction` and `differentiating the local whitened block along it`.
- The paired source-side bookkeeping for `B_\chi^{\pair}` and `S_\chi^{\pair}`.
- The local admissibility package: microscopic holomorphy, same-point positivity/nondegeneracy, and holomorphic inverse-square-root whitening.
- A precise statement of what is frozen under the paired value perturbation.

# Strongest objection

One could argue that `purely local` should mean only `defined inside the local corrected-whitened family once some scalar direction is named`, and under that weaker meaning the paired value channel is already local. I do not think that is the safest reading for theorem-facing wording here, because the unresolved issue is exactly which scalar direction deserves the name `pure paired value channel`. Until the paired analogue of `q_1=q_2=B+\alpha` is written with the same precision as in the manuscript, the definition still depends on source-level normalization choices and freeze rules that are not merely formal local bookkeeping.

# Needed for promotion

- Write the paired pure value perturbation explicitly, at manuscript level of specificity.
- Separate cleanly which ingredients are local hypotheses and which are imported source normalizations.
- Prove, or explicitly retain as hypotheses, the whitening admissibility inputs for the paired corrected local family.
- Decide whether the paper should say `local after fixing a paired source-normalized value direction` or whether a genuinely canonical local parameterization can be proved.
