- Claim

  [candidate] The cleanest exact paired `S(m)`-slot realization theorem candidate is a primitive-Dirichlet paired source theorem formulated for
  `Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\bar\chi)` and
  `\Phi_\chi^{\pair}(s):=Xi_\chi(2s-1)/Xi_\chi(2s)`.

  A theorem at the manuscript slot level should assert the following.

  Let `q_\chi^{\pair}(t)` be the strip-edge phase derivative attached to `\Phi_\chi^{\pair}(1/2+it)`, with the same branch/sign normalization as the manuscript's zeta phase. Then there is one explicit unified paired background `B_\chi^{\pair}(t)` such that, on every compact interval avoiding strip-edge singularities and with multiplicities stated, the background-subtracted scalar
  `S_\chi^{\pair}(m):=q_\chi^{\pair}(m)-B_\chi^{\pair}(m)`
  is exactly the coefficient of the local value-channel derivative in the paired corrected local deformation:

  `\Delta_{\chi}^{\pair}(m,\sigma)=S_\chi^{\pair}(m)A_{\val,\chi}^{\pair}(m,\sigma)+R_{\chi}^{\pair}(m,\sigma)`.

  Equivalently, the theorem should identify the scalar produced by the paired strip-edge source package with the manuscript's local value-channel slot, not merely with an analogous positive quantity upstairs.

  [proved] In the manuscript, the zeta slot has the exact form
  `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)` with `S(m)=q_\zeta(m)-B_\zeta(m)`.

  [conditional on the candidate theorem above] The paired scalar is the exact manuscript-style leading coefficient, so the leading-channel coefficient theorem is already available in that paired channel. Conditional on the same theorem, the paired one-zero strip-edge kernel and its positivity are automatic upstairs, and positivity of the paired local-slot scalar is automatic because the slot is identified with that source scalar.

  [missing] The theorem itself: exact phase/quotient identification for `\Phi_\chi^{\pair}`, exact single-zero contribution, exact compact-interval convergence/regularization, unified paired background bookkeeping, multiplicity convention, and proof that the resulting scalar is the exact coefficient in the paired corrected local block rather than only a parallel positive scalar.

- Status

  open

- Evidence

  The manuscript fixes the relevant slot unambiguously. It defines `S(m)=q_\zeta(m)-B_\zeta(m)` and later writes the corrected local deformation as `\Delta_\zeta=S(m)A_{\val}+R_\zeta`. So the transport target is not merely a real scalar or a positive kernel sum; it is the coefficient of the value-channel derivative inside the corrected local deformation.

  The paired Dirichlet notes already isolate the clean theorem-facing paired object as `\Phi_\chi^{\pair}(s)=Xi_\chi(2s-1)/Xi_\chi(2s)` with `Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi)`, and they sharpen the safe target to `exact paired-scalar source theorem with full bookkeeping and exact local-slot identification`.

  The positive-implication note gives the exact downstream consequence: if a family theorem yields the exact scalar occupying the manuscript's `S(m)` slot, then no new coefficient theorem `\Delta=SA_{\val}+R` is needed. What remains after that is remainder dominance, the odd/transverse package, and family-specific denominator/whitening/boundary control.

  The source-package-transfer and source-theorem-gap notes show why the candidate theorem must be stated with all bookkeeping in the theorem body. The open burden is not just positivity or quotient selection. It is the exact source-to-slot identification on compact intervals, together with the paired background, convergence, and multiplicity package.

- Exact refs

  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:273-299`
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:465-486`
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:748-778`
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1540-1560`
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1590-1621`
  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2060-2087`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:18-27`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:29-55`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:8-18`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/positive_s_implication.md:19-38`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:11-15`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:33-38`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:16-21`
  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:31-40`

- Dependencies

  1. A precise definition of `q_\chi^{\pair}` from `\Phi_\chi^{\pair}(1/2+it)` with manuscript-compatible branch/sign/factor-of-2 normalization.
  2. One explicit unified paired background `B_\chi^{\pair}` absorbing conductor/scaling, gamma-derivative, and trivial-zero or pole corrections.
  3. Exact single-zero strip-edge contribution identity for the paired quotient.
  4. Compact-interval convergence or regularization theorem for the paired source sum, with multiplicities.
  5. A realized paired corrected local block and its paired value-channel derivative `A_{\val,\chi}^{\pair}`.
  6. Exact proof that the scalar from items 1-4 is the coefficient in item 5.

- Strongest objection

  The candidate theorem still bundles two distinct realization steps: an upstairs paired source theorem for `q_\chi^{\pair}-B_\chi^{\pair}` and a downstairs identification theorem placing that scalar into the corrected local deformation as the coefficient of `A_{\val,\chi}^{\pair}`. Current scope gives good reasons to choose this as the clean target, but it does not yet show that those two steps collapse into one natural theorem or that the paired corrected local block has been realized cleanly enough for the slot statement to be non-circular.

- Needed for promotion

  1. State the theorem with exact hypotheses, normalization, compact-interval domain, and multiplicity convention.
  2. Prove `q_\chi^{\pair}=B_\chi^{\pair}+\text{paired zero source}` on singularity-free compact intervals.
  3. Construct the paired corrected local block and identify its first value-channel derivative `A_{\val,\chi}^{\pair}`.
  4. Prove the decomposition `\Delta_{\chi}^{\pair}=S_\chi^{\pair}A_{\val,\chi}^{\pair}+R_{\chi}^{\pair}` with the same exact-slot meaning as the manuscript.
  5. Verify that the downstream implication is only the leading-channel interface, not remainder dominance, odd/transverse closure, or any GRH endgame.
