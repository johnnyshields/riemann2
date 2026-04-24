# Claim

The universal versus family-specific split is correct only in the narrower Layer-1 sense of `notes/local_package_theorem.md`: the draft gives a universal odd-germ/projector theorem once one is already given one real odd holomorphic transverse scalar on a microscopic disk together with microscopic boundary control. The split is drawn too broadly if it treats real-channel oddness, the concrete boundary scale `L(m)S(m)^2/Q^3`, or the manuscript's exponential estimate `|Xi^{(N)}| \ll (L(m)S(m)^2/Q)e^{-\delta Q}` as family-agnostic.

The strongest safe roadmap sentence after exact scalar identification and remainder-dominance work is:

`After exact scalar-slot identification, the next bottleneck for the calibrated value-channel subchain is remainder dominance; independently, the odd/transverse package still requires a family theorem producing a chosen real odd holomorphic transverse scalar with microscopic boundary control.`

The claims that need scoped weakening are:

- any statement that the universal chain already reaches the manuscript's `L(m)S(m)^2`-scaled exponential bound;
- any statement that exact scalar-slot identification leaves only remainder dominance overall;
- any statement that complex Dirichlet characters or higher-degree/non-self-dual families fit the same one-channel odd package from local scope alone.

# Status

open

# Evidence

Proved:

- `notes/local_package_theorem.md:10-43` draws the clean portability boundary correctly. Layer 1 consists of odd holomorphic expansion, Cauchy coefficient bounds, and the universal `N`-point projector once a real odd holomorphic scalar with microscopic boundary control is given. Layer 2 is conditional calibration and requires extra realization hypotheses.
- In the paper, the genuinely universal projector algebra is `lem:n-point-coefficients`, `lem:n-point-mellin-symbol`, `lem:n-point-odd-generating-function`, `rem:surviving-odd-tail-structure`, and `cor:n-point-exact-odd-action` at `paper/proof_of_rh.tex:2996-3450`. These act on an odd analytic germ and do not use zeta-specific source input.
- The transport from a boundary bound to coefficient bounds is also abstract: `prop:odd-expansion` at `paper/proof_of_rh.tex:2294-2322` derives the coefficients entirely from odd holomorphy plus the boundary estimate.
- The contour-kernel and exponential-depth estimate in `prop:corrected-n-point` and `cor:optimized-zeta-cancellation-depth` at `paper/proof_of_rh.tex:3853-4319` use only the odd holomorphic scalar and its boundary-sized coefficients once those are available.

Conditional on a family realization theorem:

- Route A is basically right that the abstract odd-germ/projector package is universal only after the family has supplied the scalar on which that package acts. The safe universal consequence is: given one real odd holomorphic scalar with microscopic boundary control, the odd expansion, exact `N`-point action, contour-kernel formula, and exponential linear-depth cancellation follow formally.
- `notes/remainder_dominance.md:8-38` is also correct that remainder dominance is the next bottleneck only for the calibrated value-channel subchain after exact scalar-slot identification; it does not close the separate odd/transverse package.

Missing:

- `prop:boundary-estimate` in `paper/proof_of_rh.tex:2223-2292` is not part of the universal package. Its proof uses the zeta corrected decomposition, cutoff compatibility, preserved `Q^{-3}` whitening transfer, and the corrected-regime estimate `S_2 \ll L(m)S(m)^2`. So the manuscript's concrete scale `|H_m(s)| \ll L(m)S(m)^2/Q^3` is family-specific input, not a universal consequence.
- Oddness itself is not automatic in a new family. In the paper, oddness comes from symmetric placement plus the involution `\widehat\Omega^{\corr}(-s;m)=J_0\widehat\Omega^{\corr}(s;m)J_0` and `\Phi_K(J_0XJ_0)=-\Phi_K(X)` at `paper/proof_of_rh.tex:2311-2318`. From local scope alone there is no reason this one-channel real oddness mechanism survives for complex Dirichlet characters or non-self-dual higher-degree families.
- Route B overstates the amount of extra family work needed after the boundary theorem. The deeper zeta-side coefficient-localization material at `paper/proof_of_rh.tex:2415-2973` is not used in the proof of `prop:corrected-n-point`; that proof uses only `prop:boundary-estimate`, `prop:odd-expansion`, and the universal projector lemmas. So one should not present those localization sections as additional prerequisites for transporting the abstract odd package.

Honest verdict: the safe split is narrower than the optimistic route language. Universal means odd-germ/projector algebra plus Cauchy consequences once a family has already produced a chosen real odd holomorphic transverse scalar with microscopic boundary control. Family-specific means the existence of that channel, its oddness/real structure, and the manuscript's concrete `L(m)S(m)^2/Q^3` boundary scale. From local scope alone the odd package does not yet transport to complex-character or higher-degree settings.

# Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-58`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/remainder_dominance.md:6-38`
- `/mnt/c/workspace/riemann2/tasks/20260423-135020-attack-gap-odd-package-transport/reports/gap-odd-package-routeA.md:23-40`
- `/mnt/c/workspace/riemann2/tasks/20260423-135020-attack-gap-odd-package-transport/reports/gap-odd-package-routeB.md:22-39`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2212-2322`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2996-3450`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:3853-4319`
- `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1754`

# Dependencies

- A family theorem selecting a real critical-line channel and proving the corrected transverse scalar is real on that channel, odd under the relevant involution, and holomorphic on `|s|<\rho_0/Q`.
- Family-specific microscopic boundary control for that scalar.
- Exact scalar-slot identification only for the calibrated value-channel subchain.
- Remainder dominance only for the calibrated value-channel subchain.
- No claim about complex characters or higher degree without a separate channel-symmetry theorem.

# Strongest objection

The main risk is conflating two different senses of “universal.” The algebraic projector and its exact odd-tail formulas are universal as operators on odd analytic germs. The manuscript's concrete zeta-shaped estimate is not universal, because it depends on the family realizing a one-channel real odd scalar and on a family-specific boundary theorem at the scale `L(m)S(m)^2/Q^3`. Route A blurs this by saying the universal chain reaches exponential cancellation outright, while Route B blurs in the other direction by suggesting that the later zeta coefficient-localization machinery is still needed after the family boundary theorem. The safe middle statement is narrower than both.

# Needed for promotion

- State the split exactly in Layer-1/Layer-2 language, with Layer 1 ending at the abstract odd-germ/projector theorem and its boundary-to-Cauchy consequences.
- Replace any roadmap sentence of the form “after exact scalar identification only remainder dominance remains” by the scoped sentence above, explicitly restricting it to the calibrated value-channel subchain.
- Weaken any claim that `cor:optimized-zeta-cancellation-depth` is already family-agnostic to: it applies once the family has produced a chosen real odd holomorphic transverse scalar with microscopic boundary control.
- Add scope labels whenever discussing complex Dirichlet characters, non-self-dual channels, or higher degree: from local scope alone these are not covered by the present odd-package transport statement.
