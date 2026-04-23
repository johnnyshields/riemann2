# Claim

From current local scope, the Dirichlet channel conclusions are only partially supported.

1. The paired `\((\chi,\bar\chi)\)` route is not proved safer. On current evidence it is only the more conservative scalar candidate, because external completed-`L` facts make its critical-line object automatically real and nonnegative, while the rotated single-channel route gives only critical-line reality. The repo does not prove that either candidate reproduces the draft's corrected whitening, oddness mechanism, denominator comparability, or calibration interface.
2. The draft does not support the claim that the odd package is mostly portable once a real sign-compatible amplitude exists. A real sign-compatible amplitude is necessary for the calibration layer, but it is not enough for the odd package as used in the paper. One also needs a realized corrected local block, microscopic holomorphy, swap-compatible oddness after correction and whitening, and the boundary estimate in the new family.
3. The strongest honest Dirichlet statement from current local scope plus explicit external completed-`L` facts is this: primitive Dirichlet completed functions supply plausible real critical-line scalar candidates for a future local package, with the paired scalar `|\Lambda(\tfrac12+it,\chi)|^2` the more conservative first scalar target; but no Dirichlet analogue of the paper's calibration theorem, odd transverse scalar theorem, or final contradiction is established.

# Status

open

# Evidence

Proved from the current draft.

- The phase-kernel and jet-normalization opening is genuinely source-light: it assumes a real phase `\Phi`, its derivative `q`, symmetric placement, jet passage, and whitening. This supports only a family-agnostic local algebra layer, not any Dirichlet realization. See `paper/proof_of_rh.tex:145-269`.
- The first explicit zeta-side input is the split `q=B_\zeta+S`, the definition of the real scalar `S(m)`, and the curvature estimate `|S''(m)|\ll L(m)S(m)^2`. This is already more than abstract phase algebra. See `paper/proof_of_rh.tex:271-301`.
- The calibration theorem uses a specific real one-dimensional leading channel: `\Delta_\zeta=S(m)A_{\val}+R_\zeta`, with `\Psi_{x,d}(\Delta_\zeta)=c_{x,d}(x/B)S(m)+\Psi_{x,d}(R_\zeta)` and hence `u^2\asymp (x/B)S(m)` once the remainder is small. This needs a real sign-compatible scalar in the realized channel, not merely a real boundary object. See `paper/proof_of_rh.tex:739-813`, `1529-1621`, `2050-2209`.
- The odd transverse scalar theorem is also not amplitude-only. The scalar `H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))` is built from the corrected whitened block, uses annihilation of the leading value channel through `\Phi_K(A_{\val})=0`, and gets its coefficient bounds from the microscopic boundary estimate `|H_m(s)|\ll L(m)S(m)^2/Q^3`. See `paper/proof_of_rh.tex:567-599`, `2212-2322`.
- The manuscript itself narrows the endgame twice: first to the pair-like branch, and second to an asymptotic high-height contradiction that still needs an effective threshold and low-height bridge. So any claim of a Dirichlet endgame analogue is outside current support even before non-self-duality is addressed. See `paper/proof_of_rh.tex:26369-26608`.

Conditional on explicit external completed-`L` facts.

- [external] For primitive `\chi`, the completed functional equation `\Lambda(s,\chi)=\varepsilon_\chi\Lambda(1-s,\bar\chi)` with `|\varepsilon_\chi|=1` implies that after a root-number rotation one can form a real-valued critical-line scalar `F_\chi(t)=\varepsilon_\chi^{-1/2}\Lambda(\tfrac12+it,\chi)`. This supports the rotated single-channel route only at the level of critical-line reality.
- [external] The paired scalar `|\Lambda(\tfrac12+it,\chi)|^2=\Lambda(\tfrac12+it,\chi)\Lambda(\tfrac12-it,\bar\chi)` is automatically real and nonnegative on the critical line. This makes it a more conservative candidate for a sign-compatible scalar amplitude than the rotated single channel.

Missing.

- No theorem in the repo constructs a Dirichlet corrected local block in either the rotated single channel or the paired scalar channel.
- No theorem shows that either candidate admits a decomposition of the form `\Delta_\chi=A_\chi A_{\val,\chi}+R_\chi` in the one-dimensional calibration direction used in the paper.
- No theorem shows that `\Phi_K` is still the correct scalar functional for the Dirichlet channel, or that the swap-symmetry mechanism making `H_m` odd survives after correction and whitening.
- No theorem supplies a Dirichlet analogue of the microscopic boundary estimate, denominator comparability, or the remainder bound needed to deduce `u^2\asymp (x/B_\chi)A_\chi(m)`.
- No local argument from this scope alone shows that pairing `\chi` with `\bar\chi` is intrinsically safer rather than merely more conservative. The reason to prefer it is that it visibly preserves reality and nonnegativity at the scalar level; that is a safety heuristic, not a proved structural theorem.

Answers to the attack questions.

- Is the paired `\((\chi,\bar\chi)\)` route actually safer on current evidence, or merely more conservative?
  Merely more conservative on current evidence. It is safer only in the narrow pre-theorem sense that its obvious scalar candidate is real and nonnegative by construction. The repo does not show that this scalar is the right local amplitude, nor that it preserves the draft's oddness and calibration machinery.
- Does the draft support the claim that the odd package is mostly portable once a real sign-compatible amplitude exists?
  No. That needs scoped weakening. A real sign-compatible amplitude is necessary for the calibration comparison, but the odd package also depends on a corrected holomorphic whitening package, annihilation of the leading channel by `\Phi_K`, swap-compatible oddness, and a boundary estimate of the right size in the new family.
- Which parts of the conclusion need scoped weakening?
  Claims of the form "the paired route is safer," "the odd package is mostly portable once amplitude reality is fixed," and any suggestion that a Dirichlet final contradiction is close. Each should be weakened to "conditional on a completed-`L` realization theorem supplying the corrected local block, the one-dimensional calibration channel, the odd scalar, and the boundary/remainder estimates." For the pair choice, say "more conservative first scalar target" rather than "safer" unless a local realization theorem is proved.
- What is the strongest Dirichlet statement that is still honest from current local scope plus explicit external completed-`L` facts?
  The strongest honest statement is a candidate-selection statement: primitive Dirichlet completed functions provide plausible real critical-line scalar objects, with the paired scalar route the more conservative first scalar candidate and the rotated single channel a weaker reality-only candidate. From local scope alone, no more than the Layer 1 abstract odd-germ/projector theorem is portable, and Dirichlet calibration, odd-package realization, and any contradiction theorem remain open.

# Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:11-18,35-67,79-85`.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-52`.
- `tasks/20260423-053136-attack-gap-dirichlet-channel/reports/gap-dirichlet-channel-routeA.md:26-52,72-86`.
- `tasks/20260423-053136-attack-gap-dirichlet-channel/reports/gap-dirichlet-channel-routeB.md:11-37,62-72`.
- `paper/proof_of_rh.tex:145-301`.
- `paper/proof_of_rh.tex:426-850`.
- `paper/proof_of_rh.tex:1529-1621`.
- `paper/proof_of_rh.tex:2050-2322`.
- `paper/proof_of_rh.tex:26369-26608`.
- [external] Standard primitive-Dirichlet completed functional equation `\Lambda(s,\chi)=\varepsilon_\chi\Lambda(1-s,\bar\chi)` and its critical-line root-number rotation.

# Dependencies

- The abstract local odd-germ/projector boundary isolated in `notes/local_package_theorem.md`.
- The zeta-side calibration interface built from the real scalar `S(m)` and the one-dimensional derivative `A_{\val}`.
- Explicit external completed-`L` facts for primitive Dirichlet characters.
- A missing completed-`L` realization theorem for whichever Dirichlet channel is chosen.

# Strongest objection

The route reports still slide too quickly from "real scalar candidate exists" to "the odd package should port." The paper's usable package is not just a real scalar plus Cauchy bounds. It is a corrected whitened local block with a very specific one-dimensional calibration channel, a scalar annihilator `\Phi_K`, swap-based oddness, and a `Q^{-3}` microscopic boundary hierarchy. From this scope alone, none of those Dirichlet realization steps is proved in either the rotated single-channel or paired scalar channel.

# Needed for promotion

1. Prove a completed-`L` local realization theorem for one primitive Dirichlet family in a chosen channel.
2. Show that the chosen channel has a real sign-compatible scalar amplitude that actually enters the leading local deformation as a one-dimensional coefficient.
3. Reprove the corrected whitening package, denominator comparability, and boundary estimate in that channel.
4. Show that the scalar functional and symmetry mechanism producing oddness survive unchanged, or replace them with a proved channel-specific analogue.
5. Only after those steps, compare paired, rotated-single, and matrix routes as theorems rather than safety heuristics.

Honest verdict: the paired `\((\chi,\bar\chi)\)` route is the more conservative first scalar target, not a proved safer route. The draft does not justify saying that the odd package is mostly portable once amplitude reality is fixed. The honest boundary is much narrower: abstract odd-germ/projector structure is portable; Dirichlet realization of calibration, oddness, and contradiction remains open.
