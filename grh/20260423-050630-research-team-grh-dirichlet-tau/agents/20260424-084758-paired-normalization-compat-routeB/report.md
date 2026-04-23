# Claim

The strongest safe compatibility statement is:

`after fixing the paired source package, the paired source scalar can be identified with the common paired local value-slot scalar only conditionally, through a source-normalized whitening interface; no additional scalar renormalization is seen at the matrix-whitening step itself, but a nontrivial factor could still enter through the source-to-slot identification and through the downstream scalar normalization used to read out a theorem-facing scalar.`

Equivalently, the safe wording is not `canonical`, `purely local`, or `source-free`; it is `conditional, source-normalized interface`.

# Status

open

# Evidence

Proved:

- The manuscript's local whitening map is a matrix identity. In the unpaired model, the explicit value-channel derivative is defined by differentiating the whitened block with respect to a source scalar perturbation `alpha` while freezing derivative and curvature data; see `A_{\val}` at `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:446-469` and the resulting formula `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:471-565`.
- The corrected local deformation is decomposed as `Delta_zeta(m,sigma)=S(m)A_val(m,sigma)+R_zeta(m,sigma)` with `S(m)=q_zeta(m)-B_zeta(m)`, so the theorem-facing slot scalar in the current paper is the background-subtracted local value slot, not an abstract source scalar; see `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:285-288` and `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1540-1621`.
- The paper explicitly warns that any extra power in a corrected transverse scalar can come from the scalar normalization used to define that scalar, not from the matrix whitening identity itself; see `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2381-2385`.
- The paired value-channel note already sharpens the safe conclusion to `conditional, source-normalized interface` and says exact freeze rules and slot identification must be fixed before `A_{val,chi}^{pair}` is meaningful; see `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:16-19,25-37`.

Conditional on explicit paired interface choices:

- If the paired theorem fixes the same perturbation convention as the unpaired draft, namely `common paired value slot = B_chi^pair(m)+alpha` with all non-value local data frozen, then the first-order paired whitening derivative can be read as the local slot coefficient for that chosen source normalization; see `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:13-15,32-37`.
- If the later slot-realization theorem proves that `S_chi^pair(m)=q_chi^pair(m)-B_chi^pair(m)` is exactly the coefficient of the paired local value-channel derivative in `Delta_chi^pair=S_chi^pair A_{val,chi}^{pair}+R_chi^pair`, then the source scalar and slot scalar are compatible with no extra factor beyond the chosen source normalization; see `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:24-31`.

Missing:

- The current canonical draft does not yet contain the paired definitions `Phi_chi^pair`, `A_{val,chi}^{pair}`, `B_chi^pair`, `S_chi^pair`, or `Delta_chi^pair`, so there is no paper-level proof that the paired source scalar lands in the paired slot with unit coefficient.
- The paired source-package note explicitly stops before exact slot realization and before any local whitening-interface claim, so source packaging alone cannot rule out a hidden factor; see `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:7-20`.
- There is not yet a paired proof that the common source scalar perturbs the same-point blocks, mixed block, and background subtraction in exactly the coordinated way needed for a unit coefficient after whitening. In particular, the freeze rules, slot-identification map, and theorem-facing scalar readout are not yet locked in one formal statement.

Where renormalization could still creep in:

- between the upstream source scalar and the chosen local perturbation parameter `alpha`;
- in the definition of the paired background scalar `B_chi^pair(m)` and hence of `S_chi^pair(m)=q_chi^pair(m)-B_chi^pair(m)`;
- in whether the paired same-point and mixed blocks are differentiated with exactly the same frozen derivative/curvature data on both sides;
- in any rescaling introduced when passing from the matrix-level whitening derivative to a scalar functional, exactly as the unpaired paper warns at `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2381-2385`;
- in any later normalization-gauge quotient if the statement is pushed beyond the raw matrix-level slot coefficient; compare the manuscript's generic normalization-gauge discussion at `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:6123-6223`.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:11-19`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:25-37`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:24-31`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:7-20`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:285-288`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:446-469`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:471-565`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:739-779`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1540-1621`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2381-2385`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:6123-6223`

# Dependencies

- The unpaired local whitening/value-channel derivative framework in the canonical paper.
- The paired source-package note for what has and has not yet been proved upstream.
- The paired slot-realization note for the theorem-facing exact target.
- The paired value-channel note for the current freeze-rule-based interface wording.

# Strongest objection

The key objection is that the current evidence only shows that no extra scalar is forced by the matrix-whitening step once a perturbation parameter is chosen. It does not yet prove that the paired source scalar is itself the correct perturbation parameter for the local slot, nor that the theorem-facing scalar readout avoids an additional normalization factor. So `source scalar = slot scalar` is still too strong unless explicitly qualified by the chosen source-normalized interface.

# Needed for promotion

- Add paired definitions to the canonical draft for `B_chi^pair(m)`, `S_chi^pair(m)`, `A_{val,chi}^{pair}`, and `Delta_chi^pair`.
- Prove a paired analogue of the unpaired decomposition `Delta = S A_val + R` with the exact freeze rules stated in theorem form.
- Show that the source scalar used in the compact-interval paired source package maps to that local perturbation with unit coefficient.
- Check that the downstream paired scalar functional introduces no extra normalization beyond that already fixed at the matrix level.
- Only then upgrade the wording from `conditional, source-normalized interface` to a genuinely local exact-slot statement.
