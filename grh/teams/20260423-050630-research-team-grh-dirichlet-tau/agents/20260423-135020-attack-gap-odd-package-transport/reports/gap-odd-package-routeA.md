# Claim

The clean odd/transverse theorem chain in the current draft is:

1. `cor:PhiK-Aval-zero` removes the pure value-channel linear term after applying `\Phi_K` to the corrected local deformation.
2. `prop:boundary-estimate` converts the corrected local decomposition plus preserved `Q^{-3}` whitening transfer into the microscopic boundary bound
   `|H_m(s)| \ll_{\rho_0} L(m)S(m)^2/Q^3` on `|s|=\rho_0/Q`.
3. `prop:odd-expansion` gives an odd holomorphic expansion for `H_m` with Cauchy bounds on the odd coefficients.
4. `lem:n-point-coefficients`, `lem:n-point-mellin-symbol`, `lem:n-point-odd-generating-function`, and `rem:surviving-odd-tail-structure` provide the universal discrete odd projector: the first `N-1` odd moments vanish, the first surviving odd term is exactly order `2N-1`, and the post-cancellation tail is explicit and sign-rigid.
5. `prop:corrected-n-point` applies that projector to the corrected transverse scalar, producing an exact contour-kernel formula and the bound
   `|\Xi_\zeta^{(N)}(m)| \ll_{\rho_0} \rho_0^2 ((2N-1)N!(N-1)!/Q) (\Gamma(\rho_0Q-N)/\Gamma(\rho_0Q+N+1)) L(m)S(m)^2`.
6. `cor:optimized-zeta-cancellation-depth` inserts `N=\lfloor \alpha Q\rfloor`, uses Stirling, and yields exponential `N`-point cancellation
   `|\Xi_\zeta^{(N)}(m)| \ll_{\rho_0,\alpha} (L(m)S(m)^2/Q)e^{-\delta_*(\alpha,\rho_0)Q}`.

Universal part: Steps 3 and 4 are the family-agnostic odd-germ/projector package once one is given a real odd holomorphic scalar with microscopic boundary control. Realization-dependent part: Step 2 is the boundary input, and in the current draft it is obtained from zeta-specific corrected whitening, cutoff bookkeeping, and the realized `L(m)S(m)^2/Q^3` estimate. The exponential decay in Step 6 is universal once the Step 5 prefactor bound is available.

# Status

open

# Evidence

Proved in the current draft:

- The universal odd-projector algebra is fully proved. `lem:n-point-coefficients` shows normalization and vanishing of odd moments through degree `2N-3`. `lem:n-point-mellin-symbol` identifies the projector symbol and shows the odd part starts at order `2N-1`. `lem:n-point-odd-generating-function` gives the exact closed form for the surviving odd moments. `rem:surviving-odd-tail-structure` identifies the surviving tail coefficients explicitly and with fixed sign. `cor:n-point-exact-odd-action` states the abstract action on any odd analytic germ.
- The odd holomorphic scalar package for the draft's corrected transverse scalar is proved conditional only on the earlier draft results it cites: `prop:corrected-whitening` gives holomorphy of `\widehat\Omega_\zeta^{\corr}`, `cor:PhiK-Aval-zero` kills the value channel, `prop:boundary-estimate` supplies the microscopic boundary bound, and `prop:odd-expansion` converts this to coefficient bounds.
- Given those ingredients, `prop:corrected-n-point` is a complete theorem: exact kernel form, exact surviving expansion, and explicit `\Gamma`-ratio bound. `cor:optimized-zeta-cancellation-depth` is then a direct Stirling corollary.

Conditional on a realized boundary estimate:

- The clean portability boundary matches `notes/local_package_theorem.md`: if a real critical-line channel provides a real odd holomorphic transverse scalar on a microscopic disk together with microscopic boundary control, then the odd expansion, Cauchy coefficient bounds, universal `N`-point projector, exact surviving odd tail, and exponential linear-depth cancellation all go through formally.
- More precisely, the universal projector layer needs only an odd analytic germ `F` with coefficient or boundary control. The manuscript's zeta-specific scalar `H_m` is one realization of this layer.

Missing:

- What is not universal is the realized boundary estimate itself. In the draft, `prop:boundary-estimate` depends on the zeta-side chain `prop:corrected-local-decomposition` + `prop:cutoff-compatibility` + `prop:whitened-mixed-transfer` + the tail-curvature/corrected-transfer input giving `S_2 \ll L(m)S(m)^2`. Without an analogue of this realized bound in a new family, the abstract projector theorem does not produce an `L(m)S(m)^2`-scaled exponential estimate.
- The report `notes/remainder_dominance.md` is consistent with this split: remainder dominance is only the next bottleneck after exact scalar-slot identification in the calibrated value-channel subchain; it does not solve the separate odd/transverse package. So for portability the missing item is not merely a generic remainder estimate but a family-realized odd scalar with the right boundary norm.
- The current draft also does not prove that every relevant family supplies a single real sign-compatible odd channel. Complex characters and higher-degree/non-self-dual settings are outside this theorem chain from local scope alone.

Honest verdict: the odd/transverse package already splits cleanly into a universal odd-germ/projector theorem and a separate realized boundary-input theorem. The universal chain to exponential `N`-point cancellation is closed. The unresolved part is realization of the boundary estimate in the intended channel.

# Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-43`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:6-38`
- `paper/proof_of_rh.tex:567-572` `cor:PhiK-Aval-zero`
- `paper/proof_of_rh.tex:1392-1458` `prop:corrected-whitening`
- `paper/proof_of_rh.tex:1497-1622` `prop:corrected-local-decomposition`
- `paper/proof_of_rh.tex:1624-1683` `prop:cutoff-compatibility`
- `paper/proof_of_rh.tex:1693-1727` and cited continuation `prop:whitened-mixed-transfer`
- `paper/proof_of_rh.tex:2212-2322` odd holomorphic transverse channel, especially `prop:boundary-estimate` and `prop:odd-expansion`
- `paper/proof_of_rh.tex:2996-3169` `lem:n-point-coefficients` and `lem:n-point-mellin-symbol`
- `paper/proof_of_rh.tex:3252-3280` `lem:n-point-odd-generating-function`
- `paper/proof_of_rh.tex:3396-3450` `rem:surviving-odd-tail-structure` and `cor:n-point-exact-odd-action`
- `paper/proof_of_rh.tex:3853-4016` `prop:corrected-n-point`
- `paper/proof_of_rh.tex:4215-4319` `cor:optimized-zeta-cancellation-depth`
- `paper/proof_of_rh.tex:4505-4517` `rem:no-contour-loss-kernel-factor`

# Dependencies

- For the universal layer: only an odd holomorphic germ on a microscopic disk plus a boundary bound on that germ.
- For the current draft's realization of that layer: `\Phi_K(A_{\val})=0`, corrected finite-`s` holomorphic whitening, corrected local decomposition with fixed core, cutoff compatibility, preserved `Q^{-3}` whitening transfer, and the corrected-regime estimate `S_2 \ll L(m)S(m)^2` used inside `prop:boundary-estimate`.
- For the exponential form: Stirling applied to the `\Gamma`-ratio in `prop:corrected-n-point`.

# Strongest objection

The theorem chain is clean only after one treats `prop:boundary-estimate` as a realized input theorem rather than as part of the universal projector package. If one blurs that distinction, the draft can look stronger than it is: the projector algebra is universal, but the norm bound feeding it is still tied to the zeta-specific corrected-whitening and tail-curvature machinery. In particular, nothing in the universal odd-germ argument alone produces the manuscript's scale `L(m)S(m)^2/Q^3`.

# Needed for promotion

- State the package in two layers exactly as in `notes/local_package_theorem.md`: an abstract odd-germ/projector theorem, and a separate realization theorem supplying the boundary estimate.
- For any new family, prove existence of a real odd holomorphic transverse scalar in the relevant channel and establish its microscopic boundary bound with the correct scale.
- Keep claims about value-channel calibration, remainder dominance, and endgame consequences outside this odd/transverse package unless the extra realization hypotheses are explicitly named.
