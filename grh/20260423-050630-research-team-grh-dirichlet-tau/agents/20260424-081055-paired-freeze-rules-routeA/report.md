## Claim

Proved from the manuscript text:

- The manuscript's pure value-channel derivative freezes all derivative and curvature data at background level and varies only the common value slot. Concretely, in the symmetric constant-background model one sets `q_1=q_2=B+alpha`, keeps the derivative/curvature jet data fixed, and therefore varies the phase gap only through the value shift `Delta=Delta_0-alpha sigma` with `Delta_0=-B sigma`.
- In the corrected theorem-facing formulation, the same derivative is taken by expanding the corrected whitened block around background value-channel parameter `S(m)=0`; the coefficient of the linear term in `S(m)` is declared to be `A_val(m,sigma)` for the fixed core `mathcal C`.

Conditional paired analogue:

- The cleanest paired theorem-facing analogue is to fix the paired source slot and the paired local whitening interface, then vary only the common paired value slot:
  `q_{1,chi}^{pair}=q_{2,chi}^{pair}=B_chi^{pair}(m)+alpha`, equivalently `S_chi^{pair}(m)=alpha`, with all paired derivative, mixed-jet, curvature, and whitening data frozen at their paired background values.
- Define
  `A_{val,chi}^{pair}(m,sigma) := (partial/partial alpha) widehatOmega_{chi,bg+alpha}^{pair}(sigma;m)|_{alpha=0}`
  where the derivative is taken through the paired corrected whitened block after the paired admissibility package is fixed, and at paired background `S_chi^{pair}(m)=0`.

Missing for a fully promoted theorem statement:

- The manuscript does not itself prove the paired admissibility package, nor does it spell out the exact paired slot-identification formula needed to show that only one scalar parameter is moving in the paired corrected block.

## Status

conditional

## Evidence

The freeze rule is explicit in the manuscript's toy `A_val` definition: it says "Let the local value-channel parameter be perturbed by `q_1=q_2=B+alpha`, while all derivative and curvature data are frozen at background level," then defines `A_val(m,sigma)` as the `alpha`-derivative of the jet-limit local block at `alpha=0`. The proof confirms this operationally: the same-point Gram blocks and the cross block are rewritten as functions of `(B+alpha)` and `Delta=Delta_0-alpha sigma`, then differentiated at `alpha=0`.

The theorem-facing corrected version uses the same one-parameter logic but expressed around background value scale `S(m)=0`: the corrected whitened block is expanded analytically at background, and the coefficient of the linear term `S(m) Dmathcal W_{(bg)}[...]` is identified with `A_val(m,sigma)`. The text also says this coefficient is attached only to the fixed core `mathcal C`, so all auxiliary/tail/cutoff effects are excluded from the frozen toy derivative and remain inside the corrected scalar remainder.

The paired notes sharpen the analogue: the paired value-channel is still safe only as a one-scalar perturbation after fixing the paired source slot and local whitening interface, and the strongest safe phrasing is "conditional, source-normalized interface," not canonical or source-free. That supports the paired rule above but also blocks any stronger claim at present.

## Exact refs

- Manuscript value-channel freeze rule: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:446-469`
- Manuscript operational differentiation showing what varies: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:489-545`
- Background-subtracted value scale `S(m)`: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:285-288`
- Corrected theorem-facing expansion at `S(m)=0`: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1531-1612`
- Core-only stability of `A_val`: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1640-1671`
- Paired value-channel scope note: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_value_channel.md:7-30`
- Paired `A_val` note: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_aval.md:7-29`

## Dependencies

- The manuscript's exact toy freeze rule for `A_val`.
- The corrected local deformation proposition identifying `A_val` as the linear coefficient at `S(m)=0`.
- In the paired setting, the unproved admissibility inputs listed in the notes: paired corrected same-point and mixed blocks, microscopic holomorphy, same-point positivity/nondegeneracy, and holomorphic inverse-square-root whitening.
- Exact identification of the paired common value slot inside the source-normalized interface.

## Strongest objection

The paired analogue is not yet canonical from the current manuscript alone: unlike the scalar manuscript model, the paired setting has not yet proved that the corrected whitened block depends on the intended value direction through a uniquely identified one-scalar slot with all other paired local data truly frozen. So the proposed paired freeze rule is theorem-facing and clean, but still conditional on the paired admissibility and slot-identification package.

## Needed for promotion

- A precise paired definition of the background value parameter `S_chi^{pair}(m)` and of the common paired source/value slot it controls.
- A proof that, after fixing the paired source-normalized whitening interface, varying `S_chi^{pair}(m)` changes only that common paired value slot to first order, with derivative/mixed/curvature data frozen.
- A paired holomorphic-whitening theorem giving the first derivative of the paired corrected whitened block at `S_chi^{pair}(m)=0`.
- An adversarial verification pass confirming that no hidden source-normalization or mixed-block dependence leaks into the purported pure paired value direction.
