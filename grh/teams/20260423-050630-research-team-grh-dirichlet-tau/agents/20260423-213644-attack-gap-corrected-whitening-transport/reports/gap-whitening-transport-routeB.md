# Claim

`corrected-whitening transport` is a legitimate roadmap bundle, but only as a mid-level analytic package. In the current draft, the genuinely bundled statement is narrow: once the corrected same-point and mixed blocks are holomorphic on `|s|<\rho_0/Q`, the same-point blocks stay uniformly positive definite there, and the inverse square roots exist holomorphically, the corrected whitened block is holomorphic on the microscopic disk.

What should remain separately named subtargets is not cosmetic. The paper keeps the following pieces logically distinct:

- denominator comparability and omitted-smooth holomorphy;
- corrected same-point and mixed-block perturbation bounds;
- preserved `Q^{-3}` transverse transfer after whitening and application of `\Phi_K`;
- the boundary estimate for the corrected transverse scalar;
- the realized odd/transverse scalar theorem package.

The strongest safe roadmap sentence is:

`corrected-whitening transport is a real intermediate theorem bundle: it packages microscopic holomorphy of the corrected blocks together with same-point positivity and holomorphic whitening, but denominator comparability, preserved transverse gain, boundary control, and realized odd-channel transport should still be tracked as separate subtargets unless a family-specific realization theorem proves they collapse.`

# Status

open

# Evidence

Proved:

- Proposition `prop:denominator-comparability` proves only the denominator comparison and the resulting holomorphic extension of the omitted-smooth part and its derivatives on `|s|<\rho_0/Q` (`paper/proof_of_rh.tex:856-946`).
- Proposition `prop:corrected-whitening` is the actual bundled whitening theorem: it uses the denominator proposition for holomorphy, then separately uses perturbation and baseline spectral-gap input to obtain uniform positive definiteness and holomorphic inverse square roots, and only then concludes holomorphy of `\widehat\Omega_\zeta^{\corr}(s;m)` (`paper/proof_of_rh.tex:1392-1458`).
- The manuscript treats the preserved transverse scale as a separate theorem. Proposition `prop:whitened-mixed-transfer` proves that after whitening and applying `\Phi_K`, the corrected-vs-baseline difference is `\ll S_2/Q^3`; this is not part of Proposition `prop:corrected-whitening` itself (`paper/proof_of_rh.tex:1693-1809` and continuation through `1754`).
- The odd/transverse package starts later. Proposition `prop:odd-expansion` cites Proposition `prop:corrected-whitening` only for holomorphy, while Proposition `prop:boundary-estimate` is a separate boundary theorem using corrected local decomposition, cutoff compatibility, `\Phi_K(A_{\val})=0`, and the corrected transfer scale (`paper/proof_of_rh.tex:2214-2322`).
- The supplied roadmap notes already separate these burdens. `denominator_theorem.md` says denominator comparability is a necessary subtheorem inside corrected-whitening transport, not the complete theorem by itself; `remainder_dominance.md` and `odd_package_transport.md` both warn that other localization burdens remain independent (`grh/.../notes/denominator_theorem.md:6-25`, `grh/.../notes/remainder_dominance.md:6-38`, `grh/.../notes/odd_package_transport.md:6-49`).

Conditional on explicit family-specific realization input:

- A family may admit a larger single theorem that bundles denominator comparability, positivity, and preserved whitening scale together, but the current draft does not prove that this collapse is automatic from local algebra alone.
- For roadmap use, it is safe to speak of `corrected-whitening transport` only if the family has already supplied the microscopic denominator model, the analogue of the same-point spectral gap, and perturbation bounds strong enough to recover the same holomorphic whitening regime and transverse gain.

Missing:

- No cited result shows that denominator comparability, positivity of same-point blocks, preserved `Q^{-3}` transfer, and the boundary estimate automatically come as one theorem in primitive Dirichlet families or for `L(s,\tau)`.
- No cited result shows that the odd/transverse scalar package follows from corrected whitening alone. The current manuscript still treats realized odd-channel existence and its boundary bound as additional theorem burdens.
- No cited result decides, for a concrete non-zeta family, which of these analytic layers genuinely collapse and which remain separate named targets.

# Exact refs

- Common brief and required three-bin split: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- Denominator-note verdict: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:6-25`
- Remainder-dominance note: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:6-38`
- Odd-package note: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:6-49`
- Denominator comparability theorem: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946`
- Corrected-whitening theorem: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1458`
- Corrected local decomposition and cutoff compatibility: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1683`
- Preserved corrected-whitening transfer scale: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1693-1754`
- Boundary estimate and odd expansion: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2214-2322`
- Prior adversarial portability split naming denominator comparability, preserved whitening scale, and boundary theorem separately: `/mnt/c/workspace/riemann2/tasks/20260423-052540-attack-gap-local-package-portability/reports/verifier-adversarial-local-package.md:28-39,64-85`

# Dependencies

- A realized family-specific microscopic denominator model and the lower bound replacing `a_\rho\ge \sigma_0/Q`.
- Holomorphy of the corrected same-point and mixed blocks on the microscopic disk.
- Uniform positivity of the same-point blocks on that disk, so holomorphic inverse square roots are defined.
- Corrected same-point and mixed perturbation bounds strong enough to preserve the transverse `Q^{-3}` gain after whitening and `\Phi_K`.
- A separate boundary theorem for the realized corrected transverse scalar.
- A family-specific decision about the correct real odd channel if the family is not self-dual.

# Strongest objection

The phrase `corrected-whitening transport` can easily hide several independent analytic burdens and make the roadmap sound cleaner than the paper actually supports. In the draft, Proposition `prop:corrected-whitening` does not by itself prove the denominator theorem, the preserved `Q^{-3}` transfer, the boundary estimate, or the realized odd-channel theorem. It sits strictly between them. From current scope alone, any wording that treats the whole denominator-to-boundary chain as one transported theorem bundle is too strong.

# Needed for promotion

- For one concrete non-zeta family, state the analogue of Proposition `prop:corrected-whitening` with hypotheses separated explicitly into denominator control, positivity, and perturbation-scale input.
- Prove whether the family's denominator theorem and same-point positivity theorem are naturally one result or only adjacent inputs.
- Prove the preserved `Q^{-3}` corrected-whitening transfer in that same family rather than assuming it from the holomorphic whitening theorem.
- Keep the boundary estimate and realized odd-channel package separate until an actual family theorem shows they are consequences of the whitening package.

Honest verdict: corrected-whitening transport survives as a real but scoped intermediate bundle. It should be used on the roadmap, but only with a hard boundary: it packages holomorphic whitening itself, not the entire denominator-to-odd-channel transport chain.
