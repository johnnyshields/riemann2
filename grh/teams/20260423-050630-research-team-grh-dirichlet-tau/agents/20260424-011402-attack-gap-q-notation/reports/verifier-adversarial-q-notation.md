# verifier-adversarial-q-notation

## Proved

### Item 1
- **Claim**
  The literal `q` versus `q_\zeta` mismatch is sharply localized in the canonical RH draft, but it sits exactly at the theorem-facing source boundary, so it is not safe to treat it as a purely cosmetic one-line typo.
- **Status**
  proved
- **Evidence**
  The generic phase derivative is introduced once, globally, by `q(t):=\Ph'(t)` in the local-kernel setup. The zeta-side lane then begins at the start of `\section{Zeta-side decomposition}` with `q(t)=B_\zeta(t)+S(t)`. Immediately after that, the value scale is defined instead by `S(m):=q_\zeta(m)-B_\zeta(m)`. Route A correctly identifies this as the only surviving `q_\zeta` occurrence in the canonical paper, and Route B correctly identifies the same cut point as the first place where the draft stops being generic phase geometry and starts using zeta-specific source data. So the token mismatch is local in the text, but it occurs exactly where the manuscript needs one canonical source object.
- **Exact refs**
  `paper/proof_of_rh.tex:149-160, 271-288`; `tasks/20260424-011402-attack-gap-q-notation/reports/gap-q-notation-routeA.md:21-35, 57-71`; `tasks/20260424-011402-attack-gap-q-notation/reports/gap-q-notation-routeB.md:15-24`
- **Dependencies**
  None beyond the cited paper text and the two route reports.
- **Strongest objection**
  A reader can infer the intended identification informally, so the local mathematics may still be recoverable by context. But the question here is whether the theorem-facing conclusion is already clean enough for an RH draft. On that standard, an inference is not enough.
- **Needed for promotion**
  One scoped source-side declaration at the start of `\section{Zeta-side decomposition}` saying which zeta/scattering phase derivative the manuscript is using there, followed by a matching value-scale definition using the same symbol.

### Item 2
- **Claim**
  The mismatch is not localized enough for a bare micro-patch from `q_\zeta(m)` to `q(m)` alone. The smallest safe patch-plan is still a short source-normalization package at the section boundary.
- **Status**
  proved
- **Evidence**
  The quotient-normalization note says the sign, not the factor of `2`, is the live source issue, and it explicitly warns that `q=B_\zeta+S` and `S(m)=q_\zeta(m)-B_\zeta(m)` should currently be read as manuscript notation rather than as a fully normalized canonical source theorem. The RH patch-plan note independently places the exact cut point at the start of `\section{Zeta-side decomposition}` and says the minimum safe package there has two parts: a source-normalization subsection, then a localized zeta-source theorem. So the local token mismatch is real, but the strongest adversarial objection is that the manuscript still has not fixed, in one place, the completed quotient, the boundary phase convention, and the `\phi'/\phi` to `q` bridge. From that scope alone, a one-line replacement is too small.
- **Exact refs**
  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-18, 24-49`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`; `tasks/20260424-011402-attack-gap-q-notation/reports/gap-q-notation-routeB.md:21-35`
- **Dependencies**
  The normalization diagnosis in `quotient_normalization.md` and the cut-point diagnosis in `rh_patch_plan.md`.
- **Strongest objection**
  If the only goal were to remove one visible notation clash, a local token swap would do that. But it would still leave the generic-to-zeta specialization and the source normalization implicit at the exact point where the RH-facing source theorem should be explicit.
- **Needed for promotion**
  A compact source-normalization subsection that fixes the source quotient, the strip-edge phase convention, and the bridge to the manuscript symbol used in both `q=B_\zeta+S` and `S(m)=q(m)-B_\zeta(m)`.

## Conditional

### Item 3
- **Claim**
  Conditional on installing that source-normalization subsection, the RH agent can safely use one canonical zeta-side symbol and treat the notation repair as a small local patch-plan rather than a redesign of the argument.
- **Status**
  conditional
- **Evidence**
  Downstream uses are driven by the scalar `S(m)` and the background `B_\zeta(m)`, not by an independently active `q_\zeta` notation. The corrected local deformation, calibration, and later value-scale bookkeeping all use `S(m)` as the load-bearing scalar. Route A is right that once the source object is normalized, the downstream package reads through one scalar slot without substantive mathematical redesign. The RH patch-plan note also says the patch strengthens the draft without changing the endgame architecture.
- **Exact refs**
  `paper/proof_of_rh.tex:1540-1621, 2058-2205, 5497-5541, 26301-26326`; `tasks/20260424-011402-attack-gap-q-notation/reports/gap-q-notation-routeA.md:39-53`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:23-38`
- **Dependencies**
  The source-normalization package described in `quotient_normalization.md`.
- **Strongest objection**
  This remains conditional because the live sign/quotient bridge is source data, not notation polish. Until that is stated cleanly, the repair is only a manuscript-level intention, not yet a canonical theorem package.
- **Needed for promotion**
  Install the source-normalization subsection first, then make the zeta-side value-scale definition and downstream references use that same canonical symbol.

### Item 4
- **Claim**
  The strongest safe wording for an RH agent is a scoped specialization statement, not a global identity claim.
- **Status**
  conditional
- **Evidence**
  The background-unification note says one canonical source symbol with scoped parenthetical aliases is safe, while exact global aliasing is not safe until source theorem and `q` / `q_\zeta` usage are normalized. Combined with the quotient-normalization warning, the safe line is therefore section-scoped: define the zeta-side source quantity once, specialize the manuscript's generic `q` to that source quantity for the zeta-side decomposition, and then use only that symbol below. Any stronger wording claiming the draft already proves exact identity of all source conventions overstates the current record.
- **Exact refs**
  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:8-30`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:41-49`; `tasks/20260424-011402-attack-gap-q-notation/reports/gap-q-notation-routeB.md:31-35`
- **Dependencies**
  The source-normalization subsection exists and states the convention it is using.
- **Strongest objection**
  Even this wording should not pretend to settle family portability or endgame consequences from notation alone.
- **Needed for promotion**
  Use wording of the form: in the zeta-side decomposition below, let the manuscript symbol `q` denote the zeta/scattering phase derivative fixed by the source-normalization convention; then `q(t)=B_\zeta(t)+S(t)` and in particular `S(m)=q(m)-B_\zeta(m)`.

## Missing

### Item 5
- **Claim**
  Several current RH-facing claims need scoped weakening until the source-normalization package is installed.
- **Status**
  open
- **Evidence**
  The current paper text states `q(t)=B_\zeta(t)+S(t)` and then defines `S(m):=q_\zeta(m)-B_\zeta(m)` without an explicit theorem-level identification between the symbols. The quotient-normalization and background-unification notes both say not to claim exact aliasing yet. So the following stronger readings are not currently safe: that the existing draft has already canonically identified generic `q` with the zeta-source derivative; that `q=B_\zeta+S` is already a normalized source theorem rather than manuscript notation; and that the background symbols `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` are already proved to be exact global aliases rather than lane-dependent roles.
- **Exact refs**
  `paper/proof_of_rh.tex:273-288, 1471-1505`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:24-49`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:13-30`
- **Dependencies**
  None. This is exactly what remains missing.
- **Strongest objection**
  Some of these stronger readings may turn out to be correct after the normalization package is written. But from the present manuscript record alone, that has not yet been established.
- **Needed for promotion**
  Scoped weakening now, then explicit source normalization and background-role normalization before restoring any stronger theorem-facing wording.

## Scoped weakening list

- Read `q(t)=B_\zeta(t)+S(t)` as manuscript notation for the zeta-side lane, not yet as a fully normalized source theorem.
- Read `S(m):=q_\zeta(m)-B_\zeta(m)` as an intended specialization of the same zeta-side source quantity, not yet as a proved theorem-level identification with the generic global `q`.
- Do not say the current draft already proves exact identity of `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`; at present they are role-level symbols in different lanes.
- Do not claim any family portability or endgame consequence from this notation repair alone.

## Honest verdict

The mismatch is local in the narrow textual sense but not local enough for a bare one-line patch-plan. The token clash itself is concentrated at `paper/proof_of_rh.tex:285-288`, yet that line is exactly where the RH draft first needs a canonical zeta-source theorem. So the honest verdict is:

- the literal `q` versus `q_\zeta` mismatch is real and sharply localized;
- the safest RH-facing repair is still a small section-boundary normalization package, not just a token swap;
- the strongest safe wording is a scoped specialization for the zeta-side lane only;
- claims of already-normalized source identity, or exact global background aliasing, need weakening.

From this scope alone, the issue looks patchable without redesigning the RH architecture. It is not closed by notation-only surgery.
