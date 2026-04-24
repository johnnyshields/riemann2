# gap-q-notation-routeA

## Proved

### Item 1
- **Claim**
  The current draft uses `q` in two distinct roles that are textually visible and compatible: first as a generic phase derivative, then as the manuscript's zeta/scattering phase derivative.
- **Status**
  proved
- **Evidence**
  The generic role is introduced in the local kernel setup: `\Ph` is an arbitrary real phase and `q(t):=\Ph'(t)` at `paper/proof_of_rh.tex:149-160`. That generic `q` drives the jet matrices and finite-`s` whitening formulas at `180-258`. The zeta-specialized role begins only at `271-299`, where the paper says "Write the zeta/scattering phase derivative as" and then states `q(t)=B_\zeta(t)+S(t)` and `q(t)=q_{\loc}(t)+g_{\sm}(t)+E_{\est}(t)` at `273-283`. Downstream zeta-side decompositions keep using bare `q` for the full phase derivative, for example in the fixed-core bookkeeping `q=q_{\core}+q_{\aux,R}+g_{\sm,R}+E_{\est,R}` at `1483-1505`, `1576-1583`, and `1631-1667`.
- **Exact refs**
  `paper/proof_of_rh.tex:149-160, 180-258, 271-283, 1483-1505, 1576-1583, 1631-1667`
- **Dependencies**
  None beyond the current draft text.
- **Strongest objection**
  Bare `q` is overloaded: the early generic local-kernel notation and the later zeta/scattering specialization use the same symbol, so the reader must infer the scope change from section boundaries rather than from a renamed theorem-level object.
- **Needed for promotion**
  Nothing further is needed for the narrow claim that the draft already uses bare `q` as the active manuscript symbol in both the generic setup and the zeta-specialized lane.

### Item 2
- **Claim**
  `q_\zeta` is specialized notation in the current draft, but it appears only once and is not defined as an active symbol parallel to `q`.
- **Status**
  proved
- **Evidence**
  The only appearance in the canonical draft is the definition `S(m):=q_\zeta(m)-B_\zeta(m)` at `paper/proof_of_rh.tex:285-288`. No earlier displayed statement defines `q_\zeta`; the surrounding section uses `q(t)` instead. The older notation pattern survives in archived material, but not in the current canonical draft.
- **Exact refs**
  `paper/proof_of_rh.tex:273-288`; repo-wide search for `q_\zeta` shows no second use in the canonical draft.
- **Dependencies**
  None beyond the current draft text.
- **Strongest objection**
  One could infer informally that `q_\zeta` means "the same `q` after the zeta specialization," but that identification is not stated in the draft.
- **Needed for promotion**
  Either define `q_\zeta:=q` once in the source-normalization package or replace the isolated symbol by `q(m)`.

## Conditional

### Item 3
- **Claim**
  Conditional on a source-normalization theorem that identifies the completed quotient/phase convention and fixes one canonical symbol, the downstream zeta value-scale package can be stated cleanly with no substantive mathematical change.
- **Status**
  conditional
- **Evidence**
  The downstream package depends on the scalar `S(m)` and the background `B_\zeta(m)`, not on any further independent use of `q_\zeta`. After `S(m)` is introduced, the paper uses that scalar in the corrected local deformation `\Delta_\zeta=S(m)A_{\val}+R_\zeta` at `1540-1621`, in the calibrated comparison with `x=B_\zeta(m)\sigma` and remainder estimates at `2050-2209`, in the toy calibration at `5495-5541`, and in the crude source sum formula `S(m)=\sum_\rho f_{\beta_\rho,\gamma_\rho}(m)` at `26301-26318`. If a source theorem fixes the quotient normalization and says which object is meant by the manuscript's phase derivative, then these downstream uses can all be read through one scalar slot.
- **Exact refs**
  `paper/proof_of_rh.tex:1540-1621, 2050-2209, 5495-5541, 26301-26318`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:24-49`; `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/background_unification.md:24-30`
- **Dependencies**
  A source-normalization package fixing the quotient `\phi`, boundary phase convention, and the bridge between `\phi'/\phi` and the manuscript phase derivative `q`.
- **Strongest objection**
  The normalization issue is not merely notation: the archived note says the sign convention in the `\phi'/\phi` bridge is still unsettled, so identifying `q_\zeta` with `q` without that package would overstate what is proved.
- **Needed for promotion**
  State one canonical source theorem at the start of the zeta-source subsection, then make the `S(m)` definition use that same canonical symbol.

## Missing

### Item 4
- **Claim**
  The `q` versus `q_\zeta` mismatch blocks a clean source theorem exactly at the point where the manuscript tries to turn the generic phase derivative into the theorem-level zeta source scalar.
- **Status**
  open
- **Evidence**
  The section `Zeta-side decomposition` first introduces the active theorem-facing object as the zeta/scattering phase derivative `q(t)` at `273-283`. Immediately after that, the paper defines the load-bearing value scale by `S(m):=q_\zeta(m)-B_\zeta(m)` at `285-288`. That switch matters because the source package needs one theorem saying which completed quotient and phase convention produce the manuscript derivative, and hence which exact object is being background-subtracted. As written, the theorem would have to choose between proving a split for `q` or for `q_\zeta`; the draft does not state that these are the same object. This is not cosmetic, because `S(m)` is later the exact coefficient of the leading value channel in `\Delta_\zeta=S(m)A_{\val}+R_\zeta` and the exact scalar entering the curvature, calibration, and contradiction package. Without a single canonical symbol, the source theorem cannot cleanly conclude the manuscript-facing statement that the same source object both satisfies `q=B_\zeta+S` and gives `S(m)=q(m)-B_\zeta(m)`.
- **Exact refs**
  `paper/proof_of_rh.tex:273-288, 296-299, 1540-1621, 2050-2209, 5495-5541, 26301-26318`
- **Dependencies**
  The missing source-normalization theorem package described in `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:24-49`.
- **Strongest objection**
  A reader can probably guess the intended meaning, so the mathematics downstream may still be recoverable informally. But the mission here is a clean theorem-level source package, and that requires an explicit identification rather than an inference.
- **Needed for promotion**
  One theorem-level normalization package that fixes: the completed quotient, the boundary phase convention, the exact `\phi'/\phi` to `q` bridge, and the canonical symbol used in both `q=B_\zeta+S` and the definition of `S(m)`.

## Honest verdict

The mismatch is real and localized. In the current draft, bare `q` is the active generic-then-zeta-specialized manuscript symbol, while `q_\zeta` is a one-off specialized symbol used only in the definition of `S(m)`. That one line is exactly where the clean source theorem breaks: the draft has not yet stated that the source object whose quotient normalization is being proved is the same object used in both formulas.
