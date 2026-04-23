Claim

A new-family theorem of pure quotient type would not, from quotient data alone, automatically produce a positive background-subtracted scalar analogue of `S(m)`. What follows immediately is only a phase-channel identity for a phase derivative `q_F` attached to the quotient. A positive scalar analogue appears only if the source theorem is strengthened to identify `q_F-B_F` with a sum of positive single-zero strip-edge kernels and to match the paper's background conventions.

Status

open

Evidence

Proved:

- In the paper, `S(m)` is not introduced as the quotient itself; it is defined only after an explicit split `q(t)=B_\zeta(t)+S(t)` and then `S(m):=q_\zeta(m)-B_\zeta(m)` (`paper/proof_of_rh.tex:273-288`).
- The local value-channel decomposition uses that scalar exactly as the coefficient of the leading value direction: `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)` (`paper/proof_of_rh.tex:1540-1565`). So the scalar needed by the later machinery is a background-subtracted value coefficient, not merely a unimodular quotient or a phase.
- The quotient-phase note already separates this point: a completed-strip-edge quotient can be a serious phase candidate, but this upgrade is `phase-channel only` and does not by itself supply a realized positive `S(m)` analogue (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:8-36`).
- The source-theorem gap note says the current missing theorem is the identification of the manuscript phase derivative with the scattering quotient candidate, and it also lists a separate missing task: `identify and unify the full background term behind B_zeta, B_Aut, and B_bg` (`grh/.../notes/source_theorem_gap.md:16-18,33-40`). So quotient identification and scalar/background identification are distinct steps.

Conditional on a strengthened source theorem:

- The candidate source theorem note records the exact stronger form that would produce positivity: on a compact interval one proves `q(t)=B_{\mathrm{aut}}(t)+\sum_\rho f_{\beta_\rho,\gamma_\rho}(t)`, with each displayed kernel
  `f_{\beta,\gamma}(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}`
  nonnegative and in fact positive termwise away from singular coincidence (`grh/.../paper/source_theorem_candidate_note.tex:32-63`). Under that theorem, the background-subtracted scalar analogue would be
  `S_F(m):=q_F(m)-B_F(m)=\sum_\rho f^F_{\rho}(m)`
  and positivity would then be automatic from the displayed kernel formula.
- This is exactly why the candidate note says such a theorem would `identify S(m) as a positive strip-edge zero density` (`grh/.../paper/source_theorem_candidate_note.tex:56-63`).

Missing:

- A quotient-source theorem stated only at the level `phi_F(1/2+it)=e^{-2i\Phi_F(t)}` or `q_F=\Phi_F'` does not yet specify the decomposition into `B_F +` positive zero kernels. From that scope alone, positivity of the background-subtracted scalar is not automatic.
- Even if the quotient theorem gives a logarithmic derivative formula, the implication to the manuscript scalar still needs the background-identification step matching the family's explicit terms to the role played by `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` in the draft (`paper/proof_of_rh.tex:277-283,1500-1505`; `grh/.../paper/source_theorem_candidate_note.tex:121-122`).
- The paper's crude bound lemma for `S(m)` is an upper bound only; it does not prove positivity from within the current canonical draft (`paper/proof_of_rh.tex:26301-26364`). Its formula is consistent with positivity if the kernel representation is granted, but that positivity enters through the source representation, not through the bound lemma itself.

Honest verdict: a quotient theorem in a new family buys the phase channel immediately. It buys a positive background-subtracted scalar analogue only if the theorem already includes, or is paired with, the explicit source decomposition `q_F=B_F+\sum f^F_\rho` and the background matching. Positivity of the scalar itself is not automatic at the quotient-only stage.

Exact refs

- `paper/proof_of_rh.tex:273-288`
- `paper/proof_of_rh.tex:1540-1565`
- `paper/proof_of_rh.tex:26301-26364`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:8-36`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:16-18`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:33-40`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:32-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:112-123`

Dependencies

- The paper's source split `q=B_\zeta+S` and value-channel use of `S`.
- The quotient-phase note's `phase-channel only` conclusion.
- The candidate source theorem's stronger formula expressing `q` as explicit background plus positive kernel sum.
- Matching the family-specific background term to the manuscript roles of `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`.

Strongest objection

The phrase `source theorem of the quotient type` is ambiguous. If it means the full strengthened theorem in the candidate note, including the explicit kernel expansion and background term, then positivity of the background-subtracted scalar is automatic. If it means only a quotient-phase identification theorem, then it is not. So the implication turns on the theorem's exact conclusion, not merely on the existence of a quotient object.

Needed for promotion

- State the exact new-family source theorem in one of two scopes: `quotient-phase only` versus `quotient plus explicit kernel decomposition`.
- Prove the family-specific single-zero source contribution identity giving the analogue of the displayed positive kernel.
- Fix the multiplicity convention and compact-interval regularization/convergence for the family.
- Identify the explicit background term and prove it matches the manuscript subtraction used by the local value channel.
- Only after those points are closed may one state that the family has a positive background-subtracted scalar analogue of `S(m)`.
