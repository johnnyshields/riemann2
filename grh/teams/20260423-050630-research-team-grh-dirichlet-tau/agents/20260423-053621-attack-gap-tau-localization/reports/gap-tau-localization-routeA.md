# Claim

[confirmed] The current manuscript splits cleanly into an abstract odd-germ layer and a degree-sensitive analytic layer. For a conservative Ramanujan-\(\tau\) degree-2 port, the smallest list of manuscript steps that need a fresh rederivation is:

1. the zeta-side source decomposition and curvature/tail package at `paper/proof_of_rh.tex:271-396`;
2. microscopic denominator comparability and omitted-smooth holomorphy at `paper/proof_of_rh.tex:856-946`;
3. the baseline scaling input behind preserved whitening at `paper/proof_of_rh.tex:1693-1754`, together with the imported scale lemmas/propositions it cites;
4. the boundary estimate, and therefore the actual microscopic radius and coefficient size package, at `paper/proof_of_rh.tex:2212-2322`;
5. the crude local-value-scale bound and all endgame growth bookkeeping at `paper/proof_of_rh.tex:26301-26551` if one wants anything beyond the abstract local theorem.

By contrast, the abstract odd-germ layer itself does not need a degree-2 rederivation once one already has a real odd holomorphic scalar on a microscopic disk with boundary control.

# Status

proved

# Evidence

## Proved

- The local kernel / jet formulas and removable-singularity algebra are phase-level, not zeta-specific. The manuscript itself already supports this reading in `paper/proof_of_rh.tex:145-269`: the constructions use only a real phase \(\Phi\), its derivative \(q\), the symmetric placement \(t_\pm=m\pm s/2\), and oddness of \(\Delta_m(s)\). Nothing here uses the zeta zero set or degree-1 counting.
- The explicit value-channel derivative package `A_{\val}` and its transverse cancellation are local algebra once the baseline channel has been realized. See `paper/proof_of_rh.tex:548-684`. This is not where degree 2 first enters.
- The odd holomorphic expansion step itself is abstract once holomorphy and a boundary bound are available: `paper/proof_of_rh.tex:2294-2322` is just oddness plus Cauchy.

## Conditional on a fresh tau realization package

- `paper/proof_of_rh.tex:271-301` is the first explicitly zeta-side input layer. It names `B_\zeta`, `S(m)=q_\zeta(m)-B_\zeta(m)`, `L(m)`, and the curvature estimate \(|S''(m)|\ll L(m)S(m)^2\). For \(\tau\), one needs a new completed-\(L\) source decomposition with its own background term, local value scale, and curvature theorem. This is not a constant-change issue because these quantities set the later microscopic bookkeeping.
- `paper/proof_of_rh.tex:343-396` is also degree-sensitive. The tail curvature theorem uses the specific denominator profile
  \[
  f_{\beta,\gamma}(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}
  \]
  together with shell counting `#\mathcal S_k\ll 2^kRQ`. For \(\tau\), one needs a fresh shell count and a fresh tail second-derivative estimate in the completed degree-2 channel. This is one of the places where the denominator shape may change.
- `paper/proof_of_rh.tex:856-946` is a direct rederivation point. The microscopic disk radius \(|s|<\rho_0/Q\) comes from the lower bound \(a_\rho\ge \sigma_0/Q\) and from the concrete denominator
  \[
  D_{\rho,\pm}(s)=((2m-\gamma_\rho)\pm s)^2+a_\rho^2.
  \]
  For \(\tau\), the smallest conservative requirement is a new denominator-comparability theorem in the actual completed-\(L\) channel. This is exactly where degree 2 could change the microscopic radius or denominator shape.
- `paper/proof_of_rh.tex:1693-1754` depends on a scale hierarchy imported from the earlier corrected-whitening package: baseline same-point blocks of size
  \[
  G_\pm^{(0)}\sim \begin{pmatrix}Q&1\\1&Q^3\end{pmatrix},
  \]
  mixed blocks of size
  \[
  N^{(0)}\sim \begin{pmatrix}Q&Q^2\\Q^2&Q^3\end{pmatrix},
  \]
  inverse square roots with entries \(Q^{-1/2},Q^{-3/2}\), and perturbation matrices of sizes inherited from `paper/proof_of_rh.tex:1145-1458`. For \(\tau\), one needs a fresh degree-2 derivation that these same powers of \(Q\) survive in the completed local channel. This is the step where the whitening hierarchy could fail or shift.
- `paper/proof_of_rh.tex:2050-2210` is not abstract by itself. The sharpened calibration remainder estimate uses the preserved \(Q^{-3}\) whitening gain, the realized amplitude \(S(m)\), and the scale \(B_\zeta(m)\asymp Q\). A tau version therefore requires a fresh realized value-channel amplitude and a fresh verification that the same \(Q^{-3}\) gain survives after degree-2 whitening.
- `paper/proof_of_rh.tex:2223-2322` splits in two. The boundary estimate at `2223-2292` is degree-sensitive because it uses the tau analogue of `S_2\ll L(m)S(m)^2` and the preserved whitening estimate \(\Phi_K(\widehat\Omega^{\corr}-\widehat\Omega^{(0)})\ll S_2/Q^3\). The odd expansion at `2294-2322` is then formal. So only the boundary-control half needs fresh analytic work.

## Missing

- The manuscript does not currently prove that the \(\tau\) completed local channel has the same microscopic radius \(\rho_0/Q\), the same denominator comparability constants, or the same preserved whitening power counting. From the present manuscript alone, these are missing theorems, not consequences.
- The manuscript does not currently provide a degree-2 replacement for the crude bound `S(m)\ll Q^2` and the endgame growth package in `paper/proof_of_rh.tex:26301-26551`. If one wants only the abstract local odd-germ theorem, this is outside scope. If one wants any contradiction or quantitative boundary comparison for \(\tau\), it must be rederived.
- The manuscript does not currently show that degree 2 changes only constants. From current scope alone, that claim is unsupported.

# Exact refs

- Abstraction boundary: `paper/proof_of_rh.tex:145-269`, `2212-2322`, especially `2294-2322`.
- First explicitly zeta-side layer: `paper/proof_of_rh.tex:271-301`.
- Tail curvature package: `paper/proof_of_rh.tex:343-396`.
- Local value-channel algebra used later but not itself degree-sensitive: `paper/proof_of_rh.tex:548-684`.
- Direct microscopic-disk / denominator step: `paper/proof_of_rh.tex:856-946`.
- Imported whitening-scale inputs: `paper/proof_of_rh.tex:1145-1458`.
- Fixed-core corrected deformation interface: `paper/proof_of_rh.tex:1497-1683`.
- Preserved whitening theorem: `paper/proof_of_rh.tex:1693-1754`.
- Calibration remainder using that hierarchy: `paper/proof_of_rh.tex:2050-2210`.
- Boundary estimate and odd expansion: `paper/proof_of_rh.tex:2223-2322`.
- Crude local-value bound and current endgame status: `paper/proof_of_rh.tex:26301-26551`.
- Portability boundary note: `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/local_package_theorem.md:10-42`.
- Cycle synthesis: `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:11-18`, `43-49`, `51-66`, `70-77`.

# Dependencies

- A completed-\(L\) realization of the local phase derivative for the Ramanujan \(\tau\) \(L\)-function in a real critical-line channel.
- A tau analogue of the background/value decomposition replacing `B_\zeta` and `S(m)`.
- A degree-2 denominator-comparability theorem on the microscopic disk.
- Degree-2 shell counting / zero-density input strong enough for the omitted-tail curvature estimates used in the local package.
- A fresh derivation of the baseline same-point and mixed-block \(Q\)-scales in the completed degree-2 channel.
- A proof that the whitening gain remains at the \(Q^{-3}\) level, or an explicit replacement if it does not.

# Strongest objection

The report infers the degree-sensitive fault lines from the manuscript's internal dependency structure rather than from an explicit tau computation. So the localization is conservative, but it does not prove that the \(\tau\) channel actually changes the microscopic radius or the whitening powers; it only identifies the exact places where that question must be rechecked.

# Needed for promotion

- Prove a tau-specific replacement for `paper/proof_of_rh.tex:271-396` in completed-\(L\) language.
- Prove a tau-specific replacement for `paper/proof_of_rh.tex:856-946`, with an explicit microscopic radius.
- Recompute the baseline same-point / mixed-block scaling hierarchy and verify whether `paper/proof_of_rh.tex:1693-1754` and `2050-2210` still deliver a \(Q^{-3}\) gain.
- Reprove the boundary estimate in `paper/proof_of_rh.tex:2223-2292` for the tau channel.
- Decide scope: if the goal is only the local package theorem, stop there; if the goal includes any contradiction/endgame statement, also rederive `paper/proof_of_rh.tex:26301-26551` in degree-2 conductor language.

Honest verdict: the abstract odd-germ layer looks portable, but the actual tau localization package is not in the manuscript yet. The fresh degree-2 work is concentrated in five analytic checkpoints, and the most delicate ones are the microscopic denominator theorem and the whitening-scale hierarchy.
