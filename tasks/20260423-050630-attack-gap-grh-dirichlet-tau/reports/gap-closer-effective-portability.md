Claim

UV-008 does not look intrinsically zeta-specific. The clean portable target is an effective high-conductor exclusion theorem for a self-dual completed L-function with real local transverse scalar, followed by a separate finite low-height bridge. For primitive Dirichlet L-functions and the Ramanujan tau L-function, the natural replacement for `Q` is the logarithm of the analytic conductor at height `t`; the smallest unresolved sub-statements are the effective versions of the draft's background-scale, zero-density/tail-curvature, and calibrated toy-versus-arithmetic comparison constants in that conductor language.

Status

open

Evidence

proved

- In the present draft, the effective-gap problem is exactly the one isolated in `rem:wip-high-height-only`: replace the asymptotic comparison by explicit constants, convert `Q` to an actual height threshold, then add a finite low-height bridge.
- The current comparison uses only a short chain of ingredients: the tail-curvature bound `S_2 \ll \|B_{\Aut}''\| + Q/R^3`, the odd transverse boundary estimate `|H_m(s)| \ll L(m)S(m)^2/Q^3`, the universal `N`-point odd-moment cancellation coefficients, and the optimized cancellation corollary `|\Xi_\zeta^{(N)}(m)| \ll (L(m)S(m)^2/Q)e^{-\delta_*(\alpha,\rho_0)Q}`.
- The cancellation coefficients themselves are combinatorial and therefore degree/conductor independent once one has an odd holomorphic transverse scalar on a disk of radius `\rho_0/Q` with a boundary bound of size `\ll A(m)/Q^3`.
- The shell argument behind tail curvature is likewise structural: it needs a per-zero second-derivative bound of order `\Delta^{-4}` and local zero counting of size `\#\mathcal S_k \ll (2^kR) \times (\text{local zero density})`. This is the place where `Q` should be read as local zero density scale.

conditional on standard completed-L inputs

- For a primitive Dirichlet `L(s,\chi)`, the right scale is not bare `\log|t|` but `\Lambda_\chi(t):=\log(q_\chi(|t|+3))`, equivalently the logarithm of analytic conductor `\mathcal C_\chi(t) \asymp q_\chi(|t|+3)`. The zeta draft's `Q` should be replaced by `Q_\chi(t) \asymp \log \mathcal C_\chi(t)`.
- For a broader GRH-style completed `L`-function of degree `d`, conductor `\mathfrak q`, and gamma parameters `\mu_j`, the same role is played by `Q_L(t) \asymp \log \mathcal C_L(t)`, where `\mathcal C_L(t)` is the analytic conductor. The shell count and background derivative bounds should scale with `Q_L(t)` rather than with `\log|t|`.
- For the Ramanujan tau `L`-function, degree `2`, level `1`, the analytic conductor is `\mathcal C_\tau(t) \asymp (|t|+3)^2`, so `Q_\tau(t)=\log \mathcal C_\tau(t)=2\log(|t|+3)+O(1)`. This makes the `Q`-to-height conversion cleaner than for varying-conductor Dirichlet families because there is no character conductor parameter.
- The low-height bridge ingredients are standard in form for both Dirichlet and tau: one needs a rigorous verification result up to some height `T_*`, or an equivalent certified zero computation, plus the functional equation/symmetry needed to convert that verification into GRH/RH below `T_*`. None of that is bespoke to the present framework.
- What remains bespoke to this framework is not the low-height computation itself but the requirement that the framework's effective high-height theorem produce a concrete `T_*` in terms of its own constants: toy lower constant, arithmetic upper constant, and the calibrated conversion from toy parameter `u` to the arithmetic scale `(x/B_L)S_L`.

missing

- A completed-L analogue of the draft's arithmetic decomposition `q=B+S`, with explicit formulas for the background term `B_L(t)` and zero term `S_L(t)`, and an effective statement that `B_L(t) \asymp Q_L(t)` uniformly in the intended family.
- An effective conductor-uniform substitute for the zeta zero-free-region input used in the crude `S(m)` bound, namely the lower bound on the real-part distances `\min(\beta,1-\beta)` that turns each zero contribution into `\ll Q_L/(1+(2m-\gamma)^2)`. For Dirichlet and general automorphic families this is standard only conditionally on whatever explicit zero-free region and exceptional-zero exclusions are actually invoked; for a pure GRH abstraction it must be listed as an external hypothesis or replaced by a different bound.
- A conductor-uniform local zero counting theorem in the exact shape needed by the shell sums, with explicit constants and dependence on degree/conductor. This is standard in principle but not yet built into the draft's package.
- An explicit replacement for `\|B_{\Aut}''\|` in the tail-curvature theorem. For general completed L-functions this comes from differentiating the gamma-factor contribution; for tau this should be straightforward, for Dirichlet it is also standard, but the draft has not isolated the needed constants.
- A portable odd transverse scalar with the same microscopic holomorphy and boundary scaling. This is the real framework-specific bottleneck: outside zeta one still needs the local block construction, corrected whitening, and symmetry that make the leading value channel disappear under `\Phi_K` and leave only the curvature/tail/remainder channels.
- An effective toy-side lower bound on the admissible compact `d`-range and microscopic `u`-range that is uniform in the family once the arithmetic model has been matched to the toy model.
- A fully explicit final scalar inequality of the form `C_L e^{-\delta_L Q_L} Q_L^A < 1` with a computable exponent `A` and rate `\delta_L`, plus an explicit conversion from `Q_L` to a height threshold `T_*`.

Cleanest target by setting

- Primitive Dirichlet, fixed character: cleanest among the non-zeta extensions. Degree `1` keeps the gamma/background side close to zeta, and standard low-height verification technology already exists in principle. The extra complication relative to zeta is family uniformity in the conductor `q_\chi` and, for non-real characters, handling a complex-valued local transverse object or passing to a real two-channel package.
- General completed-L abstraction: best as a conditional theorem template, not as the first effective closure. Too many constants move at once: degree, conductor, gamma shifts, self-duality, and possibly non-real coefficients. The right theorem would be conditional on explicit conductor-uniform background, zero counting, and symmetry inputs.
- Ramanujan tau: conceptually cleaner than zeta for the high-height effective step if one only compares analytic-conductor bookkeeping, because the conductor is fixed and the object is self-dual with standard completed-L data. It is harder than zeta only to the extent that this framework's microscopic local block and toy matching were built around zeta/scattering formulas and would need a fresh arithmetic realization. So tau is cleaner on the analytic-conductor side and harder on the framework-integration side.

Exact refs

- Common brief and reporting discipline: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-37`.
- UV target: `/mnt/c/workspace/riemann2/paper/unverified.tex:199-219` (UV-008).
- Zeta-side decomposition and tail curvature: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-396`.
- Calibration remainder and `S_2/Q^3` scale: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:796-839`, `2050-2210`.
- Odd transverse channel boundary estimate: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2212-2322`.
- Local zero counting shell scale: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2868-2890`.
- `N`-point odd cancellation coefficients: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2975-3169`.
- Optimized cancellation depth and exponential rate: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:4215-4248`.
- Crude `S(m)` bound and explicit effective-gap remark: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:26301-26551`.

Dependencies

- External completed-L input: explicit functional equation and gamma-factor formulas for the target family.
- External analytic input if one wants unconditional effective constants: explicit zero-free region or an alternative effective bound on individual zero contributions; explicit local zero counting with constants; explicit verified zero range up to `T_*` for the low-height bridge.
- Framework input from the current draft: a portable construction of the corrected local block, corrected whitening, odd transverse scalar, and toy-side calibration in the target family.

Strongest objection

The analytic-conductor replacement itself is not the hard part. The strongest objection is that the current effective comparison sits on a zeta-specific local package: the draft already has a completed-L-looking tail shell argument and a universal combinatorial `N`-point cancellation, but the actual odd transverse scalar `H_m`, the annihilation of the leading value channel by `\Phi_K`, and the calibrated comparison `u^2 \asymp (x/B)S` are not yet available for Dirichlet or tau in the paper. Without that arithmetic-to-toy identification, an effective `T_*` theorem for those families is not merely missing constants; it is missing the framework object to which the constants attach.

Needed for promotion

- Reduce portability to one explicit theorem schema: for a self-dual completed `L`-function with analytic conductor scale `Q_L(t)=\log \mathcal C_L(t)`, prove `|\Xi_L^{(N)}(t)| \le C_L Q_L(t)^A e^{-\delta_L Q_L(t)}` once `N=\lfloor \alpha Q_L(t)\rfloor`.
- Isolate which parts are family-uniform: shell-count/tail-curvature, gamma-background bounds, and the combinatorial `N`-point projector.
- Write the smallest missing sub-statements explicitly:
  1. completed-L decomposition `q_L=B_L+S_L` with `B_L(t) \asymp Q_L(t)` and explicit `B_L''` bounds;
  2. conductor-uniform crude bound `S_L(t) \ll Q_L(t)^2` or a replacement sufficient for the final comparison;
  3. portable construction of the odd microscopic scalar `H_{L,t}(s)` with boundary bound `\ll A_L(t)/Q_L(t)^3`;
  4. effective toy lower constant and calibrated relation `u^2 \asymp (x/B_L)S_L` in the target family;
  5. explicit `Q_L \leftrightarrow T` conversion and a certified low-height verification result up to the resulting `T_*`.
- For first closure, target either one fixed primitive real Dirichlet character or the Ramanujan tau `L`-function rather than a full GRH abstraction. My honest ranking is: fixed primitive Dirichlet is the best first portability target, tau is analytically cleaner but requires more framework re-anchoring, and the general completed-L theorem should be written only as a conditional template after one concrete family works.
