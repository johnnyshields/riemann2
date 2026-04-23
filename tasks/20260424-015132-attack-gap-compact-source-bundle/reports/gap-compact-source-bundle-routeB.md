# gap-compact-source-bundle-routeB

**Claim**

The strongest safe patch-plan is: keep one bundled compact-interval localized source theorem, but state only the normalized compact-interval source identity inside the theorem; move background identification and multiplicity immediately after the theorem as a scoped convention plus a short corollary/remark. Putting either item inside the theorem overstates what the present draft and source notes safely justify.

**Status**

conditional

**Evidence**

proved:
- The archive consistently supports a two-step package: first a source-normalization subsection, then one bundled localized source theorem rather than several mini-theorems. See `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-26` and `.../notes/rh_patch_plan.md:23-32`.
- The exact cut point is the start of `\section{Zeta-side decomposition}`, where the draft first introduces zeta-specific source notation. See `paper/proof_of_rh.tex:271-291` and `.../notes/rh_patch_plan.md:16-21`.
- Later arguments already depend on a clean leading source scalar `S(m)` through decompositions such as `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)` and the calibration step `u^2\asymp (x/B)S(m)`. See `paper/proof_of_rh.tex:739-779` and `paper/proof_of_rh.tex:1527-1565`.

conditional on prior normalization:
- The draft currently writes `q(t)=B_\zeta(t)+S(t)` and `S(m):=q_\zeta(m)-B_\zeta(m)` before proving the quotient/phase bridge or the source normalization that identifies manuscript `q` with the quotient-normalized source object. See `paper/proof_of_rh.tex:273-291` and `grh/.../notes/q_notation.md:8-16,24-36`.
- The notes explicitly say the current draft does not yet prove exact identity of `B_\zeta`, `B_\Aut`, and `B_\bg`; the safe move is one canonical background symbol with role-level parenthetical aliases. See `grh/.../notes/background_unification.md:8-30`.
- The archive treats multiplicity as part of the five-piece source package, but only after the quotient/source theorem is in place. See `grh/.../notes/source_theorem_gap.md:31-40` and `grh/.../notes/source_package_transfer.md:19-25`.

missing:
- A proved source-normalization subsection fixing the quotient object, branch/sign/factor-of-2 normalization, and the bridge from `\phi'/\phi` to the manuscript phase derivative `q`. See `grh/.../notes/source_theorem_gap.md:16-20,31-38` and `grh/.../notes/q_notation.md:11-16`.
- A theorem-facing compact-interval convergence/regularization statement for the localized source sum, rather than manuscript-level usage only. See `grh/.../notes/source_theorem_gap.md:36-40`.
- A proved exact background identification strong enough to place `B_\zeta = B_\Aut = B_\bg` inside the theorem statement, rather than after it as scoped correspondence language. See `grh/.../notes/background_unification.md:13-17,24-30`.
- A proved theorem-facing multiplicity treatment. Right now the safest wording is bookkeeping language immediately after the theorem, not theorem-body content.

**Exact refs**

- `paper/proof_of_rh.tex:271-291`.
- `paper/proof_of_rh.tex:739-779`.
- `paper/proof_of_rh.tex:1527-1565`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-35`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-32`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:8-30`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/q_notation.md:8-36`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:11-18,31-40,44-53`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:19-25,33-39`.
- `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:195-214` for the general minimal-hypothesis caution against overstating what a formal package already forces.

**Dependencies**

- The theorem bundle depends first on the quotient/phase normalization step.
- The safe theorem body then depends on a localized compact-interval source identity with explicit regularization/convergence.
- Any stronger background-identification sentence depends on resolving the `q` versus `q_\zeta` clash and proving exact background aliasing.
- Any theorem-body multiplicity clause depends on a theorem-facing multiplicity derivation, not just manuscript convention.

**Strongest objection**

Moving background identification and multiplicity outside the theorem risks making the bundle look weaker or less self-contained than intended. If later uses silently rely on exact aliasing or on multiplicity-weighted sums, then relegating those points to post-theorem conventions could hide a real dependency rather than close it. The cure is not to force them into the theorem now; it is to make the post-theorem statements explicitly scoped: `background correspondence in the present manuscript lanes` and `zeros counted with multiplicity by convention`, unless and until exact theorem-level proofs are supplied.

**Needed for promotion**

- Add the source-normalization subsection at `paper/proof_of_rh.tex:271-291`.
- State the bundled theorem in normalized notation only: single-zero contribution plus compact-interval summation/regularization for the localized source scalar.
- Immediately after, add a scoped background-identification corollary/remark using one canonical symbol with parenthetical lane aliases, not an exact equality claim.
- Immediately after that, add a multiplicity convention/remark specifying how zeros are counted in the localized source sum.
- Audit all later uses of `S(m)`, `B_\zeta`, `B_\Aut`, `B_\bg`, and `q_\zeta` so no later statement implicitly upgrades these post-theorem conventions into theorem content.

Honest verdict: one bundled compact-interval source theorem is still the right paper-facing unit, but the strongest safe patch is narrower than the full five-part bundle advertised in rough notes. Inside the theorem: normalized local source identity on singularity-free compact intervals. Immediately after the theorem: scoped background identification and multiplicity bookkeeping. Exact theorem-body background aliasing and theorem-body multiplicity are still missing.
