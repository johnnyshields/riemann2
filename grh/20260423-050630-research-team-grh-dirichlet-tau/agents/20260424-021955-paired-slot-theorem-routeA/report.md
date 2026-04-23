## Claim

The cleanest theorem-facing statement, from current scope alone, is a compact-interval paired source-plus-slot theorem for a primitive nonprincipal Dirichlet character \(\chi\). It should be stated as follows.

**Proposed theorem-facing statement.** Let
\[
\Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\overline\chi),
\qquad
\Phi_\chi^{\pair}(s):=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)}.
\]
Fix a compact interval \(I=[a,b]\subset \mathbb R\) such that the boundary phase attached to \(\Phi_\chi^{\pair}(\tfrac12+it)\) is regular on a complex neighborhood of \(I\), and such that the paired strip-edge source theorem is valid on \(I\) with one unified background term. Define the paired phase derivative \(q_\chi^{\pair}(t)\) from \(\Phi_\chi^{\pair}\), and suppose one has an exact compact-interval decomposition
\[
q_\chi^{\pair}(t)=B_\chi^{\pair}(t)+S_\chi^{\pair}(t)
\qquad (t\in I),
\]
where \(B_\chi^{\pair}\) contains all conductor/scaling, gamma-derivative, and trivial-zero/pole bookkeeping, and \(S_\chi^{\pair}\) is the background-subtracted paired strip-edge zero scalar with the correct compact-interval convergence and multiplicity convention. For each midpoint \(m\in I\) and each symmetric local scale \(\sigma\) with \([m-\sigma/2,m+\sigma/2]\subset I\), let \(\Delta_\chi^{\pair}(m,\sigma)\) denote the paired corrected local deformation built from the same local whitening/value-channel construction as in the manuscript, and let \(A_{\val,\chi}^{\pair}(m,\sigma)\) be the pure paired value-channel derivative at paired background value \(S_\chi^{\pair}(m)=0\). Then
\[
\Delta_\chi^{\pair}(m,\sigma)
=
S_\chi^{\pair}(m)A_{\val,\chi}^{\pair}(m,\sigma)
+
R_\chi^{\pair}(m,\sigma).
\]
Equivalently, \(S_\chi^{\pair}(m)\) is exactly the coefficient occupying the manuscript-style leading local value channel.

What becomes automatic after this theorem: the manuscript's local leading-channel algebra is already in place, so no further theorem is needed to identify the leading coefficient once the exact slot identity above is proved.

What this theorem does **not** give: remainder dominance, corrected odd/transverse realization, denominator comparability, corrected whitening transport, boundary estimates, calibration uniformity in \(x\), or any ERH/GRH/endgame consequence.

The smallest honest unresolved sub-statements are:

1. A theorem-ready compact-interval definition of \(q_\chi^{\pair}\) and its regularity domain from \(\Phi_\chi^{\pair}\).
2. One unified compact-interval decomposition \(q_\chi^{\pair}=B_\chi^{\pair}+S_\chi^{\pair}\) with explicit background, convergence/regularization, and multiplicity bookkeeping.
3. An exact proof that the same scalar \(S_\chi^{\pair}(m)\) is the coefficient of the paired local value-channel derivative in the corrected whitened deformation.
4. A proof that the paired local object is built in the same symmetric normal form needed for the first-order \(A_{\val}\) transport.

## Status

conditional

## Evidence

**Proved.**

- The theorem-facing object is the paired quotient \(\Phi_\chi^{\pair}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s)\) with \(\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\overline\chi)\).
- The honest theorem burden splits into two linked pieces: an upstairs compact-interval paired source package and a downstairs exact local-slot identification.
- If the exact slot identity is proved, then the manuscript's existing local algebra already provides the leading value-channel interface; no extra coefficient theorem is needed beyond that identification.

**Conditional on [paired source-plus-slot theorem].**

- The displayed decomposition
  \(\Delta_\chi^{\pair}=S_\chi^{\pair}A_{\val,\chi}^{\pair}+R_\chi^{\pair}\)
  is exactly the theorem one needs to realize the manuscript-style leading coefficient.
- Positivity of the upstairs one-zero strip-edge kernel is automatic once the exact paired source theorem exists upstairs, but positivity of the manuscript-style slot is automatic only after exact local-slot identification.

**Missing.**

- A theorem-ready compact-interval source theorem with unified paired background identification.
- Exact paired compact-interval convergence/regularization and multiplicity bookkeeping.
- Exact proof of the downstairs slot identity in the corrected local deformation.
- Family-level corrected whitening/decomposition hypotheses needed to transport the first-order \(A_{\val}\) algebra into the paired Dirichlet setting.
- Every downstream step after the leading slot: remainder dominance, odd/transverse package, boundary control, and any contradiction-level consequence.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27,29-55,66-87`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:8-22,26-46,48-57`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_compact_theorem.md:8-27`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/aval_transport.md:8-30`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:8-15,17-38`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/first_milestone.md:8-13,20-41`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:84-108,146-176,180-202`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_candidate.tex:24-37,52-105,112-120`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:285-287,465-486,1531-1560,1590-1621,2060-2087`

## Dependencies

- Exact compact-interval paired source theorem for \(\Phi_\chi^{\pair}\).
- Unified paired background term \(B_\chi^{\pair}\).
- Compact-interval convergence/regularization and multiplicity bookkeeping for \(S_\chi^{\pair}\).
- Paired corrected local deformation and symmetric normal form compatible with first-order \(A_{\val}\) transport.

## Strongest objection

The current record supports the theorem only as a theorem-facing blueprint, not as a closed proof target with all primitives already defined. The main defect is that the same statement still hides the hard parts inside the phrases `paired source theorem`, `unified background`, and `corrected local deformation`; until those are proved in compact-interval form, the displayed identity risks looking more canonical than the present evidence justifies.

## Needed for promotion

1. Write a theorem-ready compact-interval definition of the paired phase derivative and regularity hypotheses directly from \(\Phi_\chi^{\pair}\).
2. Prove the exact decomposition \(q_\chi^{\pair}=B_\chi^{\pair}+S_\chi^{\pair}\) with full paired bookkeeping: conductor, gamma, trivial zeros/poles, convergence, and multiplicity.
3. Prove that the scalar from step 2 is exactly the coefficient of the paired local value-channel derivative in the corrected whitened block, not merely an upstairs source scalar.
4. Verify the symmetric normal form and corrected whitening assumptions needed so that the first-order \(A_{\val}\) algebra applies in the paired family.
5. Keep all downstream claims quarantined: no promotion to remainder dominance, odd/transverse realization, or ERH/GRH consequences from this theorem alone.
