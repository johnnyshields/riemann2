# Claim

The cleanest theorem-facing formulation is not an unconditional paired theorem yet, but an explicit local hypothesis line:

`Paired same-point positivity/nondegeneracy for holomorphic whitening.`

Safe statement:

`There exist rho>0 and c>0 such that, for the paired corrected same-point blocks G_{chi,\pm}^{pair}(s;m) on |s|<rho/Q, the maps s \mapsto G_{chi,\pm}^{pair}(s;m) are holomorphic and Hermitian, and`

`lambda_min(G_{chi,\pm}^{pair}(s;m)) >= c`

`throughout the microscopic disk. Consequently the holomorphic inverse square roots G_{chi,\pm}^{pair}(s;m)^{-1/2} are well-defined there, and the paired whitened block`

`widehat\Omega_{chi}^{pair}(s;m)=G_{chi,-}^{pair}(s;m)^{-1/2} N_{chi}^{pair}(s;m) G_{chi,+}^{pair}(s;m)^{-1/2}`

`is holomorphic on that disk.`

This is the right theorem-facing clause because it says exactly what the manuscript whitening step needs: not merely denominator-side holomorphy, but same-point positive-definite nondegeneracy strong enough to define holomorphic inverse-square-root whitening. The paired exact-slot theorem should then be stated conditionally on this clause, for example:

`Assume the compact-interval paired source package, the paired local normal form, and paired same-point positivity/nondegeneracy for holomorphic whitening. Then the corrected paired local deformation is well-defined and admits`

`Delta_{chi}^{pair}(m,s)=S_{chi}^{pair}(m) A_{val,chi}^{pair}(m,s)+R_{chi}^{pair}(m,s).`

Proof-state split:

- proved in the manuscript model: holomorphic whitening is obtained only after uniform positivity of the same-point blocks on the microscopic disk;
- conditional for the paired family: the same theorem-facing clause is the cleanest local hypothesis/interface;
- missing: a paired proof deriving that clause from the intended paired inputs, and a paired proof that the first-order coefficient in the whitened expansion is exactly the source scalar `S_{chi}^{pair}`.

# Status

conditional

# Evidence

The supplied paired-slot note already fixes the logical role of this clause. It says the exact paired slot theorem is not well-posed from the upstairs source theorem alone and that the minimal local package must include microscopic holomorphy, same-point positivity/nondegeneracy, well-defined inverse-square-root whitening, and the first-order paired value-channel derivative. That already points to a theorem-facing whitening-admissibility clause rather than a downstream transport theorem.

The corrected-whitening transport note sharpens the same interface. Its safe bundle is: denominator comparability plus omitted-smooth holomorphy, holomorphic corrected whitening with positive same-point blocks, and preserved post-`Phi_K` transfer scale. It then keeps value-channel slot realization, odd/transverse realization, boundary control, and remainder dominance separate. So same-point positivity belongs to the front-end definability package, not the later quantitative package.

The manuscript makes this role explicit. Proposition `Corrected finite-s holomorphic whitening` first proves holomorphy of the corrected same-point and mixed blocks, then separately proves that the same-point blocks remain uniformly positive definite on the microscopic disk, and only then concludes that the inverse square roots are holomorphic and that the whitened block is holomorphic. So the right theorem-facing paired clause is exactly positivity/nondegeneracy sufficient for inverse-square-root whitening on the disk, not a weaker statement such as pointwise positivity at `s=0`.

The manuscript also shows why this clause belongs directly in the paired exact-slot interface. The decomposition

`Delta_zeta(m,s)=S(m) A_val(m,s)+R_zeta(m,s)`

is proved by applying the analytic whitening map

`W(G_-,N,G_+)=G_-^{-1/2} N G_+^{-1/2}`

on the open set where the same-point blocks remain uniformly positive definite. Therefore the exact slot identity lives inside the holomorphically whitened object; without same-point positivity/nondegeneracy, the paired identity is not yet even well-posed in the same manuscript sense.

The manuscript's later paired local-rigidity section supports the wording `positivity/nondegeneracy` rather than `spectral gap` as the formal theorem title. In that section, `x_1 != x_2` is explicitly isolated as a `background same-point nondegeneracy condition`. This suggests the safest theorem-facing name is `same-point positivity/nondegeneracy for holomorphic whitening`, with `spectral-gap` used only as explanatory gloss for the proof mechanism when a uniform lower bound is actually established.

Separated by proof state:

- Proved: in the manuscript model, denominator-side holomorphy is not enough by itself; positivity on the disk is the extra input that licenses holomorphic inverse-square-root whitening.
- Conditional: the paired exact-slot theorem should assume or later prove the analogous disk-level positivity/nondegeneracy clause.
- Missing: a paired derivation of that clause from the paired local model, and a paired proof that whitening preserves the exact source scalar as the coefficient of `A_{val,chi}^{pair}`.

Honest verdict: the cleanest theorem-facing target is an explicit `same-point positivity/nondegeneracy for holomorphic whitening` hypothesis attached to the paired exact-slot theorem. I do not see support in the current record for advertising it as already proved for the paired family.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_hypotheses.md:7-27,31-45,54-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/corrected_whitening_transport.md:8-22,24-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:11-31,38-46`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1457`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1510-1613`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:5998-6086`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-025851-paired-positivity-routeA/report.md:3-18,26-50,68-76`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-025851-paired-positivity-routeB/report.md:3-12,22-40,59-68`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-024215-paired-admissibility-boundary-routeB/report.md:9-19,40-56`

# Dependencies

- The supplied paired-slot and corrected-whitening notes.
- The manuscript's corrected holomorphic-whitening proposition as the model for what local same-point positivity actually buys.
- The manuscript's exact-slot decomposition proof, which uses the analytic whitening map inside the positive-definite region.
- Prior paired positivity/admissibility reports in this cycle.

# Strongest objection

The inequality `lambda_min(G_{chi,\pm}^{pair}(s;m)) >= c` may be stronger or more quantitative than the paired theorem can currently justify. The truly invariant core requirement is that the same-point blocks stay holomorphic and uniformly positive definite on the microscopic disk so that a holomorphic branch of the inverse square root exists. If the paired route only supports base-point nondegeneracy plus a perturbative radius depending on extra transport inputs, then my displayed formulation will need weakening or more careful quantification.

# Needed for promotion

- Prove a paired analogue of `Corrected finite-s holomorphic whitening` that separates `(i)` microscopic holomorphy from `(ii)` same-point positivity/nondegeneracy sufficient for holomorphic inverse-square-root whitening.
- Decide the final formal label conservatively: likely `same-point positivity/nondegeneracy for holomorphic whitening`, with `spectral-gap` retained only as proof-language unless a uniform lower bound is genuinely established.
- Prove that, inside the paired whitened local object, the first-order value-channel coefficient is exactly the compact-interval source scalar `S_{chi}^{pair}(m)`.
- Adversarially verify whether the paired clause should assert full disk-level uniform positivity, or only a weaker base-point nondegeneracy plus a separately proved perturbative extension.
