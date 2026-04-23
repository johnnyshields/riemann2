# gap-aval-transport-routeB

- Claim

  Exact `A_val` transport is a narrow theorem burden. After exact slot identification and the current local algebra, what comes for free is only the statement that the family's corrected local deformation has the same first-order value-channel coefficient as the manuscript's `A_val`, with the exact transported scalar in that slot. What does not come for free is the later calibration/remainder chain: denominator comparability, finite-`s` holomorphic whitening, quantitative control of the transported remainder after whitening, remainder dominance in the calibrated functional, the odd/transverse package, and the variable-`x` uniformity needed by the later endgame. In the manuscript's own logic, `A_val` is used in two different roles that must be kept separate: exact leading-coefficient identification in `\Delta_\zeta=S(m)A_{\val}+R_\zeta`, and later quantitative calibration through `\Psi_{x,d}` plus the bound `\Psi_{x,d}(R_\zeta)=o((x/B)S)`.

- Status

  open

- Evidence

  Proved in the current draft:
  `A_val` itself is explicit and purely local. Proposition `prop:explicit-Aval` gives the exact matrix formula, Lemma `lem:Aval-small-x` gives the small-`x` size, and Corollary `cor:PhiK-Aval-zero` proves `\Phi_K(A_{\val})=0` (`paper/proof_of_rh.tex:471-659`). Proposition `prop:corrected-local-decomposition` then identifies the first-order transported slot inside the corrected whitened object: `\Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma)`, with `R_\zeta` defined to be everything left after subtracting the explicit value-channel term (`paper/proof_of_rh.tex:1497-1622`). This is the exact manuscript model for what an `A_val` transport theorem would look like.

  Proved in the current draft:
  The later calibration chain is separate. Proposition `prop:canonical-calibration` only turns the decomposition into `u^2\asymp (x/B)S(m)` after applying the functional `\Psi_{x,d}` and after controlling the remainder term (`paper/proof_of_rh.tex:739-794`). Corollary `cor:sharpened-calibration-remainder` shows the sufficient quantitative remainder statement is `|\Psi_{x,d}(R_\zeta)|\ll_D S_2/Q^3`, hence one needs `S_2=o(xQ^2S(m))` to conclude `\Psi_{x,d}(R_\zeta)=o((x/B)S(m))` (`paper/proof_of_rh.tex:2050-2209`). This matches the separate remainder note: after exact scalar-slot identification, the next bottleneck for the calibrated value-channel subchain is remainder dominance, not a further `A_val`-identification step.

  Proved in the current draft:
  The odd/transverse chain is also separate. Since `\Phi_K(A_{\val})=0`, the value-channel main term disappears after applying `\Phi_K`, and the transverse scalar becomes `H_m(s)=\Phi_K(R_\zeta(m,\sigma))` (`paper/proof_of_rh.tex:2214-2265`). The boundary estimate is then obtained from whitened-transfer control and tail-curvature bounds, not from the exact `A_val` formula (`paper/proof_of_rh.tex:2267-2291`). So transporting `A_val` does not by itself transport the odd/transverse theorem package; it only identifies the piece that is annihilated there.

  Conditional on the family analogue of the manuscript's local package:
  The paired-slot note is right that exact source-plus-slot realization is the cleanest theorem-facing target: one theorem upstairs for the paired source realization, one theorem downstairs for exact local-slot identification. If both are proved, then the family has an exact scalar multiplying the same local value-channel derivative slot. From current scope alone, that is enough to transport the exact `A_val` formula into the family-level decomposition, but only conditionally on family analogues of the corrected finite-`s` holomorphic whitening and corrected local decomposition machinery (`paired_slot_realization.md:8-37`; `paper/proof_of_rh.tex:1392-1458,1497-1622`). Exact slot identification alone does not prove those analytic prerequisites.

  Missing theorem burdens after `A_val` transport:
  `1.` A family-level analogue of denominator comparability and holomorphic whitening, so the corrected same-point and mixed blocks exist holomorphically on the microscopic disk and inverse square roots stay controlled (`paper/proof_of_rh.tex:856-946,1392-1458`).
  `2.` A family-level corrected local decomposition theorem putting the transported scalar in the precise first-order slot of the corrected whitened block, with all auxiliary/tail/error bookkeeping internal to the corrected scalar (`paper/proof_of_rh.tex:1497-1683`).
  `3.` Quantitative whitened-transfer and remainder estimates for the transported family remainder, strong enough to imply the calibrated dominance condition `\Psi(R)=o((x/B)S)` or the manuscript's sufficient form `S_2=o(xQ^2S)` (`paper/proof_of_rh.tex:1693-1754,2050-2209`; `remainder_dominance.md:8-38`).
  `4.` The odd/transverse package: after `\Phi_K(A_{\val})=0`, one still needs boundary control, odd microscopic expansion, and the later odd-moment machinery for the corrected scalar built from the transported family (`paper/proof_of_rh.tex:2214-2321`).
  `5.` The variable-`x` calibration rewrite remains independent. Even in the zeta draft, the fixed-`x` calibration does not yet force the toy parameter into the microscopic regime, and the draft marks this as conditional on a uniform variable-`x` rewrite (`paper/proof_of_rh.tex:5500-5598`). Exact `A_val` transport does not remove that burden.

  Missing, in the strict sense of "not free from current scope alone":
  The transported exact formula does not identify the size of the denominator `\langle A_{\val}(x),M(d)\rangle_\F` in the family, does not control how whitening reshapes non-leading terms, does not prove the remainder is lower order after calibration, and does not prove any endgame contradiction. Those are separate theorems.

- Exact refs

  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/paired_slot_realization.md:8-37`
  `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:8-38`
  `paper/proof_of_rh.tex:431-850`
  `paper/proof_of_rh.tex:856-946`
  `paper/proof_of_rh.tex:1392-1458`
  `paper/proof_of_rh.tex:1497-1683`
  `paper/proof_of_rh.tex:1693-1754`
  `paper/proof_of_rh.tex:2050-2209`
  `paper/proof_of_rh.tex:2214-2321`
  `paper/proof_of_rh.tex:5500-5598`

- Dependencies

  The argument depends on reading `A_val` transport as the family analogue of Proposition `prop:corrected-local-decomposition`, not as a synonym for the whole calibration package. It also depends on the manuscript's current split between value-channel calibration (`\Psi_{x,d}`) and transverse annihilation by `\Phi_K`, and on the notes' scoped claims that exact slot identification and remainder dominance are separate burdens.

- Strongest objection

  One could object that once the exact scalar slot is identified, most of the rest is routine bookkeeping because the manuscript already has the local algebra. I do not think the current draft supports that stronger claim. The later results use quantitative denominator comparability, holomorphic inverse-square-root control, entrywise whitened transfer bounds, and a separate smallness hypothesis on the calibrated remainder. Those are not formal consequences of exact slot identification from current scope alone.

- Needed for promotion

  A promotable statement should isolate the burden as follows: prove a family-level corrected local decomposition with the transported exact scalar in the `A_val` slot; then prove, separately, the quantitative remainder dominance theorem needed for calibration; then prove, separately, the odd/transverse boundary and expansion package for the corrected scalar. If one wants an endgame-facing statement, it must also include the variable-`x` uniformity rewrite now flagged in `rem:wip-calibration-small-u`.
