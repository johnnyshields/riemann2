## Claim

The cleanest theorem-facing normalization convention for the paired quotient is:

\[
\Phi_\chi^{\mathrm{pair}}(s):=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)},
\qquad
\Xi_\chi(s):=\Lambda(s,\chi)\Lambda(s,\bar\chi),
\]

and on the critical line one should write

\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)=e^{2 i \Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}(t):=\bigl(\Theta_\chi^{\mathrm{pair}}\bigr)'(t).
\]

This is the safest theorem-facing convention because the factor `2` keeps the paired boundary phase on the same footing as the repaired zeta-side normalization, while `q_\chi^{\mathrm{pair}}` is defined as the derivative of the actual phase variable rather than of a renormalized half-phase.

Proved:
- pairing removes the residual root-number/front-end asymmetry, so the quotient admits a clean scalar boundary-phase packaging in the form `e^{2 i \Theta_\chi^{\mathrm{pair}}}`;
- with that packaging, the natural front-end notation is `q_\chi^{\mathrm{pair}}=(\Theta_\chi^{\mathrm{pair}})'`.

Conditional on later theorem input:
- any theorem using this convention must match the exact source-normalized scalar `S_\chi^{\mathrm{pair}}(m)` from the compact paired source package, not an upstairs-only or renormalized surrogate;
- the convention is compatible with the theorem target only as a source-normalized interface.

Missing:
- a proof that this normalization alone yields exact local `S_\chi^{\mathrm{pair}}(m)` slot realization;
- compact-interval convergence/regularization for the paired source package;
- theorem-body canonicality of unified `B_\chi^{\mathrm{pair}}`, multiplicity bookkeeping, and any whitening-interface claim.

## Status

open

## Evidence

`dirichlet_paired_source.md` gives the explicit front-end recommendation: the safest theorem-facing phase convention is to mirror the repaired zeta-side normalization and write `\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{2 i \Theta_\chi^{\mathrm{pair}}(t)}` with `q_\chi^{\mathrm{pair}}=(\Theta_\chi^{\mathrm{pair}})'`; it also states what pairing fixes and what it does not fix, namely cleaner boundary-phase packaging and removal of residual root-number asymmetry, but not the theorem-sized source gap, local-slot identification, denominator comparability, corrected whitening, odd/transverse realization, or boundary control.

`paired_source_package.md` sharpens the theorem-facing scope: the paired source theorem is still only a compact-interval source-package blueprint, with compact-interval convergence/regularization the first real missing burden, and with unified `B_\chi^{\mathrm{pair}}` plus multiplicity bookkeeping kept in immediate post-theorem bookkeeping rather than promoted into canonical theorem-body content.

`paired_normalization_compatibility.md` fixes the interface condition: the coefficient in `\Delta_\chi^{\mathrm{pair}}=S_\chi^{\mathrm{pair}}A_{\mathrm{val},\chi}^{\mathrm{pair}}+R_\chi^{\mathrm{pair}}` must be the same `S_\chi^{\mathrm{pair}}(m)` from the compact paired source package, not a renormalized substitute or upstairs-only scalar. So the front-end `q_\chi^{\mathrm{pair}}` convention is safe only when kept subordinate to that source-normalized target.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:29-63`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:65-81`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:7-29`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_source_package.md:37-74`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_normalization_compatibility.md:7-27`

## Dependencies

- the paired quotient object `\Phi_\chi^{\mathrm{pair}}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s)` with `\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi)`;
- the compact paired source-package blueprint that defines the source scalar `S_\chi^{\mathrm{pair}}(m)`;
- later compact-interval regularization and bookkeeping results for unified `B_\chi^{\mathrm{pair}}` and multiplicity.

## Strongest objection

The present notes justify the `e^{2 i \Theta}` / `q=(\Theta)'` convention as the cleanest front-end packaging, but they do not yet prove that this normalization is canonical independently of the compact paired source package; without the missing source theorem and exact slot identification, `q_\chi^{\mathrm{pair}}` could still be only an upstairs phase variable rather than the theorem-ready scalar attached to the manuscript's local coefficient.

## Needed for promotion

- prove the compact paired source-package theorem at least at blueprint level with compact-interval convergence/regularization;
- prove that the coefficient in the paired value decomposition is exactly `S_\chi^{\mathrm{pair}}(m)` from that source package, with no renormalized surrogate;
- separate theorem-body content from post-theorem bookkeeping for `B_\chi^{\mathrm{pair}}` and multiplicity;
- prove exact local-slot realization before claiming that the `q_\chi^{\mathrm{pair}}` normalization fixes more than the front-end phase convention.
