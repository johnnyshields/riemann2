Claim

The safest honest candidate channel for primitive complex Dirichlet characters is a paired scalar package built from \((\chi,\bar\chi)\), not the raw single \(L(s,\chi)\) channel and not yet a matrix-valued package. A rotated completed single channel is a plausible conditional candidate, but the current draft does not support it strongly enough for the future local package because the draft uses more than critical-line reality: it uses a real sign-compatible calibration amplitude, a corrected odd holomorphic transverse scalar, denominator comparability, and the swap-symmetry package behind oddness. A matrix-valued package is safer than the rotated single channel if scalar pairing fails, but on current evidence it is not the first honest target because it introduces new bookkeeping before the repo has exhausted the simpler paired scalar route.

Status

heuristic

Evidence

Proved from the current draft.

- `paper/proof_of_rh.tex:145-269` supports only a real-phase local kernel and jet package. Those formulas require a real scalar phase \(\Phi\) and its derivatives, not yet any Dirichlet-specific completed-\(L\) realization.
- `paper/proof_of_rh.tex:426-850` shows that the realized local channel is not just an odd germ. The calibration uses a real background slope \(B\), a real value scale \(S(m)=q(m)-B(m)\), the identity \(\Phi_K(A_{\val})=0\), and the comparison \(u^2\asymp (x/B)S(m)\). This is where sign-compatibility matters.
- `paper/proof_of_rh.tex:2212-2322` shows that the odd transverse scalar \(H_m(s)=\Phi_K(\widehat\Omega^{\corr}(s;m))\) is produced from symmetric placement plus jet-basis swap in a corrected whitened package, and its boundary bound is stated in terms of the real quantity \(L(m)S(m)^2/Q^3\). The current draft therefore needs more than a boundary object that is merely real on the critical line.
- `paper/proof_of_rh.tex:2975-3169` supports the universal odd-moment projector once an odd holomorphic scalar with the right boundary control already exists. This layer does not decide the correct Dirichlet channel.
- The repo synthesis and verifier already isolate the open decision: rotated single channel, paired \((\chi,\bar\chi)\) channel, or matrix-valued package. They also state that the present draft does not prove that complex Dirichlet characters fit the same one-channel package and that non-self-dual cases are the least supported. See `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:35-67`, `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:29-52`, and `tasks/20260423-050630-verify-grh-dirichlet-tau/reports/verifier-adversarial-portability.md:20-38`.

Conditional on external standard facts, clearly not repo-sourced.

- [external] For primitive \(\chi\), the completed function satisfies \(\Lambda(s,\chi)=\varepsilon_\chi\Lambda(1-s,\bar\chi)\) with \(|\varepsilon_\chi|=1\). Hence on the critical line one may rotate by \(\varepsilon_\chi^{-1/2}\) and obtain a real-valued scalar \(F_\chi(t)=\varepsilon_\chi^{-1/2}\Lambda(\tfrac12+it,\chi)\). This supports the rotated single-channel candidate at the level of critical-line reality only.
- [external] The paired scalar object \(|\Lambda(\tfrac12+it,\chi)|^2=\Lambda(\tfrac12+it,\chi)\Lambda(\tfrac12-it,\bar\chi)\) is automatically real and nonnegative on the critical line and packages \(\chi\) with its contragredient. This makes sign-compatibility of a future amplitude more plausible than in the rotated single-channel formulation, though the repo does not prove the needed local derivative/whitening theorem for this object either.
- [external] A matrix-valued package using the two-dimensional channel spanned by \(\Lambda(s,\chi)\) and \(\Lambda(s,\bar\chi)\) would encode the natural non-self-dual symmetry without forcing a scalar reduction too early. But from the current draft alone there is no theorem showing that the scalar functional \(\Phi_K\), the calibration denominator, or the odd-jet machinery survive unchanged in matrix form.

Proved / conditional / missing split for the three candidates.

- Proved: none of the three candidates is realized by the current draft.
- Conditional on external completed-\(L\) input: the rotated single channel gives a real boundary scalar; the paired \((\chi,\bar\chi)\) channel gives a real and more sign-stable scalar object; a matrix package preserves the natural non-self-dual symmetry.
- Missing: for every candidate, the draft lacks a completed-\(L\) realization theorem producing the analogue of the corrected whitened block, the odd holomorphic transverse scalar, denominator comparability on the microscopic disk, and a real sign-compatible calibration amplitude replacing \(S(m)\).

Comparison of the three candidates.

- Rotated completed single channel: enough only for a tentative phase-level start. It gives critical-line reality, but the draft needs more than reality, and the verifier already flags that critical-line reality is not a proxy for the self-dual package used in the paper.
- Paired \((\chi,\bar\chi)\) channel: safest honest target. It stays scalar, preserves the contragredient pairing explicitly, and is the best bet for a real sign-compatible amplitude without importing full matrix machinery.
- Matrix-valued package: safest in principle against hidden non-self-dual defects, but not safest as the next theorem target because it adds a new formal layer before the scalar paired route has been tested.

Honest verdict: the rotated single channel is not enough on current evidence. The safest honest candidate for primitive complex Dirichlet characters is a paired \((\chi,\bar\chi)\) scalar package, with the rotated single channel kept as a conditional subcase to be recovered only if one proves that its calibration amplitude and corrected odd scalar behave exactly as required. If the paired scalar route fails to supply those properties, then the correct fallback is a matrix-valued package.

Exact refs

- Common brief and schema: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`.
- Cycle synthesis, including the unresolved channel decision: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:35-67`.
- Local package theorem boundary: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-52`.
- Adversarial verifier on portability and non-self-dual weakness: `/mnt/c/workspace/riemann2/tasks/20260423-050630-verify-grh-dirichlet-tau/reports/verifier-adversarial-portability.md:20-39`, `72-90`.
- Generic phase and jet layer: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:145-301`.
- Calibration package and real value-scale dependence: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:426-850`.
- Odd transverse scalar and boundary estimate: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2212-2322`.
- Universal odd-moment projector: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2975-3169`.
- Related exploratory report favoring rotated critical-line reality but flagging sign risk: `/mnt/c/workspace/riemann2/tasks/20260423-050630-attack-fund-grh-dirichlet-tau/reports/explorer-dirichlet-phase.md:31-46`, `58-78`.
- Related finite-core report flagging paired or matrix reformulation for non-self-dual cases: `/mnt/c/workspace/riemann2/tasks/20260423-050630-attack-gap-grh-dirichlet-tau/reports/gap-closer-finite-core-portability.md:13-21`, `33-48`.

Dependencies

- [external] Standard primitive Dirichlet completed functional equation and root-number normalization.
- A completed-\(L\) realization theorem for the chosen channel producing a corrected local block with microscopic holomorphy.
- A proof that the chosen channel has a real sign-compatible calibration amplitude replacing `S(m)`.
- A conductor-uniform denominator comparability theorem for the chosen channel on the microscopic disk.
- A proof that the oddness mechanism used in `paper/proof_of_rh.tex:2214-2322` survives in the chosen channel after correction and whitening.
- If the paired scalar route is used, a precise definition of its local phase derivative and background/value split.
- If the matrix route is used, a replacement for the scalar functional `\Phi_K` and for the scalar calibration denominator.

Strongest objection

The recommendation for the paired \((\chi,\bar\chi)\) channel is still not proved from the repo. It is a safety judgment, not a theorem. The present draft never constructs a Dirichlet corrected local block in any of the three channels, so even the paired channel may fail to reproduce the exact oddness, denominator shape, or calibration linearization that the zeta argument uses.

Needed for promotion

- Prove, for one primitive complex character family, a completed-\(L\) local realization theorem in the paired \((\chi,\bar\chi)\) channel: corrected whitening, odd holomorphic scalar, and microscopic boundary bound.
- Check whether the paired channel yields a real sign-compatible local amplitude that can replace `S(m)` in the calibration theorem.
- Attempt the rotated single-channel realization only after the paired route identifies exactly which sign and symmetry properties are genuinely needed.
- If either scalar route breaks, define the minimal matrix-valued replacement and reprove the analogue of `\Phi_K`, oddness, and the projector interface there.
- Keep all future claims split into proved / conditional on external completed-\(L\) input / missing until one channel is actually realized.
