Claim

The weakest honest local theorem that survives Dirichlet and Ramanujan-\(\tau\) pressure is this conditional package:

Given a chosen critical-line channel for a completed \(L\)-function family, if one has
1. a real odd holomorphic transverse scalar \(H_m(s)\) on \(|s|<\rho_0/Q_L\),
2. a real calibration amplitude \(A_L(m)\) and background slope \(B_L(m)\) giving a decomposition of the local deformation into a leading value channel plus a remainder,
3. denominator comparability and corrected-whitening estimates strong enough to force the remainder and boundary size to be \(O(S_{2,L}/Q_L^3)\),

then the odd microscopic expansion and the discrete \(N\)-point odd-moment projector go through exactly as abstract local statements. What does not survive as a theorem from the current draft is the realization claim that primitive Dirichlet \(L\)-functions or \(L(s,\tau)\) already furnish that package. For complex primitive characters the single-channel realization is presently the least supported; for \(\tau\) the self-dual side is cleaner, but the degree-2 denominator and whitening hierarchy are still unproved.

Status

heuristic

Evidence

Proved from the cited local text.

- `paper/proof_of_rh.tex:271-301` is the first explicit zeta-side input layer. The split \(q=B_\zeta+S\), the definition of \(S(m)\), the logarithmic control \(L(m)\), and the curvature estimate are not family-agnostic local algebra.
- `paper/proof_of_rh.tex:426-850` proves only a calibration interface. The local theorem there is: once a real value-channel derivative \(A_{\val}(x)\) and a toy anomaly matrix \(M(d)\) are available with nonzero pairing, one gets the formal calibration relation \(u^2\asymp (x/B)S(m)\) after the remainder is small. This is an abstract local mechanism, not a Dirichlet or \(\tau\) realization theorem.
- `paper/proof_of_rh.tex:856-946` makes microscopic holomorphy depend on a denominator shape and a zero-free lower bound \(a_\rho\ge \sigma_0/Q\). That is already a realization hypothesis, not a consequence of the odd-germ formalism.
- `paper/proof_of_rh.tex:2050-2322` shows the odd transverse scalar theorem is only as strong as the remainder and boundary package behind it. The oddness itself is formal, but the actual boundary bound \(|H_m(s)|\ll L(m)S(m)^2/Q^3\) uses the zeta-side remainder scale and the real quantity \(S(m)\).
- `paper/proof_of_rh.tex:2975-3169` is the cleanest universal layer. Once an odd holomorphic germ exists with the needed coefficient bounds, the \(N\)-point coefficients and projector are purely algebraic and do not care whether the source is zeta, Dirichlet, or \(\tau\).

Conditional on explicit realization hypotheses.

- Primitive Dirichlet families fit this package only after one chooses the correct real channel. For real characters, a self-dual scalar channel is plausible. For complex primitive characters, the paper does not show that raw or simply rotated one-channel data preserve the needed odd corrected scalar, real calibration amplitude, and sign-compatible boundary package. A paired \((\chi,\bar\chi)\) or matrix-valued channel may be required.
- The Ramanujan \(\tau\) family avoids the non-self-dual obstruction, so the theorem is cleaner there at the symmetry level. But the paper still does not prove that the degree-2 archimedean data preserve the same microscopic radius, denominator comparability, and \(Q^{-3}\) whitening hierarchy.

Missing from the current draft.

- A completed-\(L\) realization theorem producing the corrected local block and its odd transverse scalar outside zeta.
- A proof that the calibration amplitude replacing \(S(m)\) is real and sign-compatible in the actual chosen family/channel.
- A conductor-uniform denominator lemma replacing the zeta-specific scalar denominator package.
- A conductor-uniform proof that the corrected remainder still lands at the \(Q_L^{-3}\) scale needed for the boundary and projector arguments.

Smallest hidden assumptions that must be named explicitly.

- Real channel assumption: the local theorem needs a real odd scalar, not merely complex critical-line values.
- Calibration-sign assumption: the amplitude replacing \(S(m)\) must be real and of the sign needed to interpret \(u^2\asymp (x/B)A_L(m)\).
- Microscopic denominator assumption: omitted-zero denominators stay uniformly comparable on \(|s|<\rho_0/Q_L\).
- Whitening-scale assumption: the corrected remainder and boundary term still gain exactly the \(Q_L^{-3}\) factor used in `2050-2322`.

Weakest honest theorem statement.

- From the local odd-germ and calibration scope alone, the paper proves a representation-free projector theorem for any family that already supplies a real odd holomorphic transverse scalar with the same microscopic denominator and whitening bounds.
- It does not prove that primitive Dirichlet \(L\)-functions or \(L(s,\tau)\) satisfy those realization hypotheses.

Exact refs

- Brief and schema: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`.
- Cycle synthesis: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:6-67`.
- Prior adversarial verifier: `/mnt/c/workspace/riemann2/tasks/20260423-050630-verify-grh-dirichlet-tau/reports/verifier-adversarial-portability.md:11-53`.
- First zeta-side layer: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-301`.
- Calibration interface and dependence on `B_\zeta`, `S(m)`, and `x=B_\zeta\sigma`: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:426-850`.
- Denominator comparability and zero-free lower bound: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946`.
- Sharpened remainder, odd scalar, and boundary estimate: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2050-2322`.
- Universal `N`-point odd-moment projector: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2975-3169`.

Dependencies

- A family-by-family completed-\(L\) realization theorem for the corrected local block.
- A choice of channel that is genuinely real in the sense needed by the odd scalar and calibration steps.
- Conductor-uniform zero-free and zero-counting input strong enough to support denominator comparability and tail control.
- A proof that the family preserves the microscopic whitening hierarchy used to get the \(Q^{-3}\) remainder and boundary gain.

Strongest objection

Even this weakened theorem still packages several analytic requirements into the phrase "supplies a real odd holomorphic transverse scalar." In the current paper those requirements are not cosmetic. They encode the actual zeta-side work: real sign-compatible calibration, denominator control, zero-free input, and the \(Q^{-3}\) corrected-whitening gain. Without naming those hypotheses separately, the theorem still sounds more family-agnostic than it is.

Needed for promotion

- State the local theorem in two layers: abstract odd-germ/projector theorem first, realization hypotheses second.
- Name the four hidden assumptions explicitly: real channel, calibration sign, microscopic denominator comparability, and preserved whitening scale.
- Separate real/self-dual Dirichlet realizations from genuinely complex non-self-dual ones.
- Treat \(L(s,\tau)\) only as a conditional self-dual test case until the degree-2 denominator and whitening package is rebuilt.
- Keep any portability summary in three bins: proved local theorem, conditional family realization, missing realization input.
