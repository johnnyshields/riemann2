# Claim

The canonical calibration package splits into a portable local algebraic core and a non-portable analytic wrapper. The portable core consists of the whitening linearization at background value-channel parameter zero, the small-\(x\) asymptotics of \(A_{\val}(x)\), the transverse cancellation \(\Phi_K(A_{\val})=0\), and the nonvanishing denominator after pairing with the toy anomaly matrix on compact \(d\)-ranges. This part should extend to any completed \(L\)-function model once one has: (i) a local background slope \(B(m)\), (ii) a local value scale \(S(m)=q(m)-B(m)\), and (iii) a fixed local core whose off-line toy comparison still produces the same anomaly matrix \(M(d)\) or an equivalent compact-family replacement.

The non-portable part is the analytic package that keeps the corrected remainder and the microscopic holomorphic window uniform when \(x=B(m)\sigma\) is allowed to shrink. In the current draft this package uses zeta/scattering-specific input: the decomposition \(q=B_\zeta+S\), the curvature bound \(|S''(m)|\ll L(m)S(m)^2\), the omitted-zero denominator comparability based on a zero-free-region lower bound \(a_\rho\gg Q^{-1}\), shell counting for the far tail, and later Stirling control of the archimedean gamma ratio. For primitive Dirichlet \(L\)-functions the same variable-\(x\) strategy looks conditionally portable; for the Ramanujan \(\tau\) \(L\)-function it also looks conditionally portable, but only after redoing the microscopic denominator and gamma-factor bookkeeping with several archimedean parameters. Higher degree does not obviously break the normalization, but it enlarges the analytic checklist and may change constants in the admissible \(|s|\ll Q^{-1}\) window.

The cleanest target is not a full GRH-level rewrite but the following portability theorem schema: for any completed \(L\)-function family with a local decomposition \(q=B+S\), a microscopic holomorphic window \(|s|\le c/Q\), a curvature bound \(|S''(m)|\le C_1L(m)S(m)^2\), and a compact-\(d\) toy expansion \(\Delta_{\toy}(u;d)=u^2M(d)+O_D(u^4)\), the canonical calibration yields
\[
u^2 \asymp \frac{x}{B(m)}S(m)
\]
uniformly for \(0<x\le x_0(D)\), provided the corrected remainder satisfies \(|\Psi_{x,d}(R)|\le C_2 S_2/Q^3\) uniformly in that range. The smallest unresolved sub-statements are therefore the uniform-in-\(x\) analytic ones, not the local matrix algebra.

# Status

open

# Evidence

Proved.

- The explicit formula for \(A_{\val}(x)\) is derived entirely inside the symmetric constant-background local model from the same-point Gram matrices, the cross block, and the relation \(x=B\sigma\). No zeta-specific global input enters that differentiation once \(B\) is treated as a frozen background slope. This is the strongest evidence that the linear algebra package is portable.
- The transverse cancellation \(\Phi_K(A_{\val})=0\) is an exact entrywise identity coming from antisymmetry of the off-diagonal terms. This is purely local.
- The small-\(x\) expansion \(A_{\val}(x)=B^{-1}\bigl(\begin{smallmatrix}O(x^2)&-\sqrt3 x/3+O(x^3)\\ \sqrt3 x/3+O(x^3)&O(x^2)\end{smallmatrix}\bigr)\) and hence \(\|A_{\val}(x)\|_F\asymp x/B\) are again local Taylor facts.
- The denominator nonvanishing in the calibration functional comes from pairing that local expansion with the toy anomaly matrix \(M(d)\), with nonzero linear coefficient on every compact \(D\subset(0,\infty)\). This depends on the toy model and the chosen channel, but not on zeta-specific analytic input.
- The decomposition \(\Delta_\zeta=S(m)A_{\val}+R_\zeta\) is formulated abstractly through the whitening map linearized at value-channel parameter \(S(m)=0\). Conceptually this only needs a background package plus a value perturbation parameter. This suggests portability to other completed \(L\)-functions with the same local block architecture.

Conditional on explicit replacements.

- The variable-\(x\) regime should extend to primitive Dirichlet \(L\)-functions if one can reproduce four zeta-side inputs with conductor-uniform constants: a background split \(q=B_\chi+S_\chi\), a curvature estimate \(|S_\chi''(m)|\ll L_\chi(m)S_\chi(m)^2\), omitted-zero denominator comparability for \(|s|\le c/Q\), and a tail shell bound. None of these steps appears to use self-duality in an essential way at the level visible here; they use completed-function local denominators, a zero-free region away from the selected core, and counting. Complex characters mainly threaten reality/symmetry conventions, not the local calibration scaling itself.
- The same variable-\(x\) strategy should also extend to the Ramanujan \(\tau\) \(L\)-function provided the local core still reduces to an effective one-pair odd-jet anomaly and the completed logarithmic derivative admits the same microscopic split. The extra gamma factors alter the explicit background term and the Stirling constants, but they do not by themselves invalidate the normalization \(x=B(m)\sigma\).
- Higher degree or multiple archimedean parameters do not appear to obstruct the canonical normalization at the algebraic level. They do, however, make the background slope \(B(m)\) a sum of several gamma contributions, so one must re-check that \(B(m)\asymp Q\) and that the microscopic holomorphic window \(|s|\le c/Q\) survives with a family-uniform constant. This is a real analytic requirement, not a local matrix one.

Missing.

- The draft does not prove that Corollary \(\ref{cor:sharpened-calibration-remainder}\), currently written in the fixed-scaled regime \(|\sigma|\asymp Q^{-1}\), remains valid uniformly for all \(0<x\le x_0(D)\), equivalently \(|\sigma|\le c/Q\) with no lower bound. This is the central missing portability statement.
- The denominator-comparability argument uses a zero-free-region lower bound \(a_\rho\ge \sigma_0/Q\) for every omitted zero. For general completed \(L\)-functions this has to be re-established in the relevant admissible midpoint class, with constants uniform in conductor/degree. Without it, the microscopic holomorphic extension can shrink or fail.
- The far-tail curvature theorem uses shell counting \(\#\mathcal S_k\ll 2^kRQ\). For a broader family one needs the corresponding local zero-density/counting statement in the conductor-height aspect that matches the chosen \(Q\).
- The corrected remainder bound is normalized using whitening scales of size \(Q^{-1/2}\) and \(Q^{-3/2}\). For higher-degree gamma factors one must verify that these same powers remain correct after redefining the local blocks; otherwise the bound \(S_2/Q^3\) may change.
- UV-009 is still open, so even a perfectly portable zeta-side rewrite would only show \(\Psi_{x,d}(\Delta_{\toy})=u^2+O_D(u^4)\) once the explicit toy remainder is written uniformly on compact \(D\).

Minimal unresolved sub-statements.

- A uniform variable-\(x\) version of the sharpened remainder estimate: prove \(|\Psi_{x,d}(R(m,\sigma))|\le C_D S_2/Q^3\) for all \(0<x\le x_0(D)\).
- A family-uniform microscopic denominator lemma: for omitted zeros and \(|s|\le c/Q\), denominators at \(t_\pm=m\pm s/2\) stay comparable to their real-line sizes.
- A family-uniform tail curvature estimate of the form \(S_2\ll |B''(m)|+Q/R^3\) or an equivalent substitute strong enough to imply \(S_2=o(xQ^2S(m))\) after the adaptive choice of \(x(m)\).
- A background-growth lemma showing \(B(m)\asymp Q\) and controlling \(B''(m)\) for the target completed \(L\)-family.
- For \(\tau\) or higher degree, a check that the corrected same-point and mixed blocks still whiten with the same local power counting.

# Exact refs

- Common brief and schema: `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`.
- Background split and curvature estimate: `paper/proof_of_rh.tex:273-300`.
- Tail curvature theorem: `paper/proof_of_rh.tex:343-396`.
- Leading value matrix and local calibration algebra: `paper/proof_of_rh.tex:426-794`.
- Corrected local deformation decomposition around `S(m)=0`: `paper/proof_of_rh.tex:1497-1622`.
- Sharpened calibration remainder estimate in the fixed-scaled regime: `paper/proof_of_rh.tex:2050-2088`.
- Boundary estimate feeding the corrected scalar: `paper/proof_of_rh.tex:2231-2307`.
- Microscopic denominator comparability and omitted-smooth holomorphy: `paper/proof_of_rh.tex:856-941`.
- Archimedean Stirling/gamma-ratio dependence in the zeta-side `N`-point bound: `paper/proof_of_rh.tex:4347-4387`.
- Work-in-progress remark defining UV-001: `paper/proof_of_rh.tex:5500-5598`.
- UV-001 ledger entry: `paper/unverified.tex:43-64`.
- UV-009 ledger entry: `paper/unverified.tex:221-238`.

# Dependencies

- UV-009 for the quantitative toy remainder.
- A completed-\(L\)-function analogue of the split \(q=B+S\).
- A family-uniform zero-free-region input strong enough to give microscopic denominator comparability for omitted zeros.
- A family-uniform local zero counting / tail shell estimate.
- Background Stirling estimates for the relevant gamma factors, including conductor and degree dependence.
- Preservation of the fixed-core local toy anomaly package under the target family’s local normalization.

# Strongest objection

The local algebra may be portable while the analytic normalization is not. In particular, the proof of microscopic denominator comparability is written for omitted zeros with denominators of the simple form \(((2m-\gamma_\rho)\pm s)^2+a_\rho^2\), and the later corrected-whitening estimates use zeta-specific \(Q\)-power scales and a single-background-slope normalization. For primitive Dirichlet \(L\)-functions this likely survives only after a careful completed-function rewrite; for the Ramanujan \(\tau\) \(L\)-function or higher degree, extra gamma parameters could change the admissible microscopic radius or the whitening exponents. From the present text alone, portability beyond degree one is therefore not proved.

# Needed for promotion

- State and prove a family-agnostic local calibration theorem whose hypotheses mention only \(B(m)\), \(S(m)\), a microscopic holomorphic window, denominator comparability, and a tail curvature bound.
- Reprove the sharpened calibration remainder estimate uniformly in the variable-\(x\) regime \(0<x\le x_0(D)\), not just \(|\sigma|\asymp Q^{-1}\).
- For at least one non-zeta test family, preferably primitive Dirichlet \(L\)-functions, verify the four analytic hypotheses explicitly with conductor-uniform constants.
- Check for the \(\tau\) \(L\)-function that higher-degree gamma factors do not alter the whitening power counting or, if they do, rewrite the normalization accordingly.
- Close UV-009 with an explicit compact-\(D\) toy remainder so that the adaptive calibration actually forces \(|u|<u_0(D)\).
- Honest verdict: the canonical calibration is plausibly portable at the local algebra level and plausibly extends to Dirichlet and \(\tau\) settings after substantial analytic repackaging, but the current draft does not justify that portability. The smallest real gap is a uniform variable-\(x\) analytic remainder theorem, not a new local matrix computation.
