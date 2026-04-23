- Claim

  The partial-bundle framing is safe only in a narrow sense. The current draft supports `corrected-whitening transport` as an intermediate analytic package whose proved core is: microscopic denominator comparability and omitted-smooth holomorphy, holomorphy of the corrected same-point and mixed blocks, uniform positivity of the corrected same-point blocks on `|s|<\rho_0/Q`, holomorphic inverse square roots, and the preserved post-`\Phi_K` transfer scale `\ll S_2/Q^3`. It is not safe to let that phrase absorb the corrected local-decomposition theorem, the boundary estimate, or the realized odd/transverse scalar theorem. From current scope alone, those remain distinct downstream burdens.

  The strongest safe roadmap sentence now is:

  `corrected-whitening transport is a real but scoped intermediate bundle: after denominator comparability supplies microscopic holomorphy and the same-point spectral gap plus perturbation bounds keep whitening holomorphic, the corrected whitened block and its post-\Phi_K transverse transfer are controlled on |s|<\rho_0/Q; boundary control and realized odd-channel transport remain separate family-specific theorem targets.`

  The claims that need scoped weakening are:

  1. any sentence saying or implying that the full corrected local deformation package `\Delta_\zeta = S A_{\val} + R_\zeta` is already an intrinsic transport theorem rather than a first-order expansion with `R_\zeta` defined after subtraction;
  2. any sentence saying or implying that once corrected whitening is in place, the boundary estimate follows automatically;
  3. any sentence saying or implying that the odd/transverse package transports automatically from corrected whitening or from source theorem plus positive `S`.

- Status

  open

- Evidence

  Proved:

  Proposition `prop:denominator-comparability` proves only denominator lower/upper comparison and the resulting holomorphic extension of `g_{\sm}(t_\pm)` and its required derivatives on `|s|<\rho_0/Q`; this matches the denominator note's narrower verdict that denominator comparability is a necessary subtheorem inside corrected-whitening transport, not the whole transport theorem by itself.

  Proposition `prop:corrected-whitening` proves the actual holomorphic-whitening bundle and stops there: holomorphy of corrected blocks, uniform positive definiteness of same-point blocks after shrinking `\rho_0`, holomorphic inverse square roots, and therefore holomorphy of `\widehat\Omega_\zeta^{\corr}(s;m)`.

  Proposition `prop:whitened-mixed-transfer` is separate and proves the preserved post-whitening transverse scale
  \[
  \Phi_K\bigl(\widehat\Omega_\zeta^{\corr}(s;m)-\widehat\Omega_\zeta^{(0)}(s;m)\bigr)\ll \frac{S_2}{Q^3}.
  \]
  So even inside the paper the bundle naturally splits into at least a holomorphic-whitening theorem and a preserved-transfer theorem.

  Missing / conditional:

  Proposition `prop:corrected-local-decomposition` packages
  \[
  \Delta_\zeta(m,\sigma)=S(m)A_{\val}(m,\sigma)+R_\zeta(m,\sigma),
  \]
  but the proof obtains this by analytically expanding around `S(m)=0` and then defining
  \[
  R_\zeta:=\Delta_\zeta-S(m)A_{\val}.
  \]
  That is enough for internal bookkeeping, but from this scope alone it does not prove that a non-zeta family comes equipped with an intrinsic corrected value-channel theorem whose remainder decomposition is canonical independently of this subtraction. This is the strongest reason not to overstate the bundle.

  Proposition `prop:boundary-estimate` is also downstream and imports more than corrected whitening alone: it uses corrected local decomposition, cutoff compatibility, `\Phi_K(A_{\val})=0`, the preserved `S_2/Q^3` transfer, and then the corrected-regime input `S_2\ll L(m)S(m)^2` on the microscopic boundary. So boundary control is not part of the proved whitening theorem itself.

  Proposition `prop:odd-expansion` depends on both holomorphy from `prop:corrected-whitening` and the separate boundary estimate. This matches the odd-package note: the odd/projector algebra transports once a family already supplies a realized corrected odd holomorphic transverse scalar and its boundary control; existence of that realized odd scalar and its boundary estimate are not automatic from local scope alone.

  Therefore the partial-bundle framing is safe only if it is explicitly partial. It is unsafe if read as saying that denominator comparability, corrected local decomposition, preserved transfer, boundary control, and odd-channel realization all collapse into one automatic transport theorem.

- Exact refs

  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`

  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/denominator_theorem.md:6-20`

  `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/odd_package_transport.md:8-49`

  `/mnt/c/workspace/riemann2/tasks/20260423-213644-attack-gap-corrected-whitening-transport/reports/gap-whitening-transport-routeA.md:3-15,23-40,71-81`

  `/mnt/c/workspace/riemann2/tasks/20260423-213644-attack-gap-corrected-whitening-transport/reports/gap-whitening-transport-routeB.md:3-16,23-40,64-75`

  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946` (`prop:denominator-comparability`)

  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1392-1458` (`prop:corrected-whitening`)

  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1622` (`prop:corrected-local-decomposition`)

  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1624-1683` (`prop:cutoff-compatibility`)

  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1693-1754` (`prop:whitened-mixed-transfer`)

  `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2214-2322` (`eq:Hm-def`, `prop:boundary-estimate`, `prop:odd-expansion`)

- Dependencies

  A family analogue of the microscopic denominator lower bound replacing `a_\rho\ge \sigma_0/Q`.

  Family-specific same-point spectral-gap and perturbation estimates strong enough to keep the corrected same-point blocks uniformly positive definite and to support holomorphic inverse square roots.

  A family-specific proof of the preserved post-whitening `\Phi_K`-transfer scale, not just holomorphy of whitening.

  A family-specific intrinsic identification of the corrected value channel, if one wants to promote `\Delta = SA_{\val}+R` from bookkeeping to a theorem-facing transport statement.

  A separate realized odd/transverse scalar theorem with microscopic boundary control.

- Strongest objection

  The dangerous slippage is between `internal to the same corrected object` and `already a transported theorem`. In the present draft, internalization of auxiliary/tail/error bookkeeping is proved as a structural bookkeeping fact, while the key decomposition still defines `R_\zeta` after subtracting the first-order value-channel term. From that scope alone, one may safely say that corrected whitening packages holomorphy and supports a later boundary argument; one may not safely say that the entire boundary-to-odd-channel transport theorem is already contained in corrected whitening. Any such claim needs the scope qualifier `from current local corrected-whitening scope alone, no`.

- Needed for promotion

  State and prove, in one concrete non-zeta family, the exact analogue of `prop:corrected-whitening` with hypotheses separated into denominator control, positivity, and perturbation-scale input.

  Prove the family analogue of `prop:whitened-mixed-transfer`, so the preserved post-`\Phi_K` transverse gain is a theorem rather than a roadmap expectation.

  If the roadmap wants to include `\Delta = SA_{\val}+R` inside the transport bundle, prove that the corrected value channel is intrinsically realized from the fixed core and that `R` is a canonical internal remainder, not only the residual term after formal subtraction.

  Keep the boundary estimate and realized odd-channel package separate until a family theorem shows they follow from the narrower whitening package.

  Honest verdict: the partial-bundle framing is safe only if it stays explicitly partial. The strongest safe sentence is the scoped intermediate-bundle sentence above. The claims that need weakening are exactly those that let corrected whitening absorb intrinsic value-channel realization, boundary control, or odd-channel transport. Those do not follow from current local corrected-whitening scope alone.
