## Claim

For the paired quotient
`\Phi_\chi^{\mathrm{pair}}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s)` with
`\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi)`, the clean theorem-facing normalization is:

- define the boundary phase by
  `\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{2 i \Theta_\chi^{\mathrm{pair}}(t)}`
  on any compact interval where the boundary value is regular and unimodular;
- define the paired phase derivative by
  `q_\chi^{\mathrm{pair}}(t):=(\Theta_\chi^{\mathrm{pair}})'(t)`.

Then the exact bridge is

`(\Phi_\chi^{\mathrm{pair}\,\prime}/\Phi_\chi^{\mathrm{pair}})(1/2+it)=2 q_\chi^{\mathrm{pair}}(t)`.

Equivalently,

`q_\chi^{\mathrm{pair}}(t)=\tfrac12 (\Phi_\chi^{\mathrm{pair}\,\prime}/\Phi_\chi^{\mathrm{pair}})(1/2+it)`.

If one instead keeps the archived negative-sign boundary law
`\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2 i \Theta_\chi^{\mathrm{pair}}(t)}` while still writing
`q_\chi^{\mathrm{pair}}=(\Theta_\chi^{\mathrm{pair}})'`, then the bridge becomes

`(\Phi_\chi^{\mathrm{pair}\,\prime}/\Phi_\chi^{\mathrm{pair}})(1/2+it)=-2 q_\chi^{\mathrm{pair}}(t)`.

So the factor of `2` is unchanged from zeta; the only real normalization choice is the sign. The paired route matches the zeta quotient-normalization fix exactly at this bridge level: keep `q=(phase derivative)` and the positive source law `q=B+S`, so choose the positive phase convention `e^{2 i \Theta}` rather than the archived `e^{-2 i \Theta}`. The paired route is cleaner only in that pairing removes the residual root-number phase that complicates the single-channel Dirichlet quotient; it does not change the `\pm 2` bridge itself.

Three-bin split:

- **Proved.** Once the boundary law is written as `e^{\pm 2 i \Theta(t)}`, differentiation along `s=1/2+it` gives the exact bridge `(\Phi'/\Phi)(1/2+it)=\pm 2 \Theta'(t)`. For the paired quotient, the unimodular boundary-phase package is already the safe front-end candidate, and pairing removes the residual root-number asymmetry.
- **Conditional on source normalization being adopted in the theorem statement.** Writing the compact source package as `q_\chi^{\mathrm{pair}}=B_\chi^{\mathrm{pair}}+S_\chi^{\mathrm{pair}}` without further sign repair is safe only after the paper explicitly fixes the positive boundary-phase convention and identifies this `q_\chi^{\mathrm{pair}}` as the active paired phase derivative.
- **Missing.** The paired notes still do not provide the family-specific compact-interval source theorem, unified background identification, multiplicity closure, or exact local-slot realization. So this attack fixes the front-end normalization convention only; it does not close the paired source theorem.

Honest verdict: the exact sign/factor relation is settled, and the theorem-facing convention should simply mirror the zeta fix with `e^{2 i \Theta}` and `q=\Theta'`. What remains open is everything source-level after that normalization.

## Status

proved

## Evidence

The supplied paired-source note already fixes the theorem-facing paired object as `\Phi_\chi^{\mathrm{pair}}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s)` and says this packaging is cleaner than the single-channel quotient because the residual root number disappears at the boundary-phase level. The source-package candidate note then uses `q_\chi^{\mathrm{pair}}` as the phase derivative attached to that quotient, but leaves the sign convention unstated. The separate quotient-normalization note resolves exactly the analogous zeta issue: the factor `2` is correct, the actual ambiguity is the sign, and if one wants `q=\Phi'` together with a positive source split `q=B+S`, then the clean convention is `\phi(1/2+it)=e^{2 i \Phi(t)}`, not the archived `e^{-2 i \Phi(t)}`. The paired case inherits the same calculus because the argument is only differentiation of the boundary law along `s=1/2+it`: if `\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{2 i \Theta(t)}`, then `i(\Phi'/\Phi)(1/2+it)=2 i \Theta'(t)`, hence `(\Phi'/\Phi)(1/2+it)=2 q_\chi^{\mathrm{pair}}(t)`; with the negative-sign exponent one gets `-2 q_\chi^{\mathrm{pair}}(t)` instead. The paired route therefore needs the same normalization repair as zeta, but no extra root-number correction at the quotient boundary because pairing has already removed that asymmetry.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:8-17`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:29-55`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_package_candidate.tex:24-53`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-39`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/q_notation.md:11-36`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_normalization_compatibility.md:7-27`

## Dependencies

This conclusion depends on three things only: the theorem-facing paired quotient `\Phi_\chi^{\mathrm{pair}}`, a regular unimodular boundary-phase law on the compact interval under discussion, and the manuscript convention that `q_\chi^{\mathrm{pair}}` means the derivative of the chosen boundary phase. Any source-level use also depends on the later explicit identification of this normalized `q_\chi^{\mathrm{pair}}` with the `q_\chi^{\mathrm{pair}}` appearing in `q_\chi^{\mathrm{pair}}=B_\chi^{\mathrm{pair}}+S_\chi^{\mathrm{pair}}`.

## Strongest objection

The strongest objection is that this report may look stronger than the paired notes actually justify if the sentence `q_\chi^{\mathrm{pair}}=\tfrac12(\Phi'/\Phi)(1/2+it)` is read as already embedded in a proved paired source theorem. It is not. What is proved here is only the exact front-end normalization bridge once a boundary-phase convention is chosen. The compact-interval source decomposition and exact slot identification remain open, so the bridge should be presented as normalization data for the future theorem statement, not as closure of the paired source package.

## Needed for promotion

1. Add a source-normalization subsection for the paired package that explicitly fixes `\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{2 i \Theta_\chi^{\mathrm{pair}}(t)}` and `q_\chi^{\mathrm{pair}}=(\Theta_\chi^{\mathrm{pair}})'`.
2. State the paired compact-interval source identity using that normalized `q_\chi^{\mathrm{pair}}`, with one unified `B_\chi^{\mathrm{pair}}` and explicit multiplicity convention.
3. Prove the family-specific compact-interval convergence/regularization theorem for the paired source term.
4. Prove exact identification of `S_\chi^{\mathrm{pair}}(m)=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)` with the manuscript's paired local value-channel coefficient.
