# Claim

[confirmed] The cleanest source-light theorem schema genuinely supported by the current RH draft is a **local odd-transverse package for a real completed-phase kernel**:

Given a real phase \(\Phi\) with holomorphic microscopic continuation, symmetric finite-\(s\) jet blocks \(G_{m,\pm}(s)\), mixed block \(N_m(s)\), and positive-definite same-point jet blocks so that whitening is holomorphic, define the whitened block
\[
\widehat\Omega(s;m)=G_{m,-}(s)^{-1/2}N_m(s)G_{m,+}(s)^{-1/2}
\]
and the transverse scalar
\[
H_m(s):=\Phi_K(\widehat\Omega(s;m)).
\]
If, in addition, one has a corrected decomposition into a baseline local model plus a perturbation whose transfer into \(\widehat\Omega\) is bounded by \(\ll S_2/Q^3\) on \(|s|<\rho_0/Q\), and a microscopic boundary estimate
\[
|H_m(s)|\ll \mathcal B(m)/Q^3 \qquad (|s|=\rho_0/Q),
\]
then:

1. \(H_m\) is odd and holomorphic on \(|s|<\rho_0/Q\);
2. its odd Taylor coefficients satisfy Cauchy bounds of size \(\ll \mathcal B(m)\);
3. for the universal coefficients \(a_j^{(N)}\), the discrete projector
\[
\Xi^{(N)}(m):=\sum_{j=1}^N a_j^{(N)} H_m(j/Q^2)
\]
cancels odd jets through order \(2N-3\).

[confirmed] This is the correct portability boundary. The theorem must stop here to remain honest. The current draft does **not** support, from this local package alone, any RH/GRH endgame, any global sign law, or any exclusion of remote nonadjacent incidences.

# Status

open

# Evidence

proved

- The phase-kernel, point-to-jet, jet-limit block, finite-\(s\) block, and removable-singularity package is written in phase language and does not use zeta-specific source structure. This gives the abstract local matrix object to be whitened.
- The value-channel derivative \(A_{\val}\), its exact annihilation by \(\Phi_K\), its small-\(x\) expansion, and its nonzero pairing with the toy anomaly matrix are explicit algebraic facts inside the local constant-background model.
- The discrete \(N\)-point coefficients and their odd-moment cancellation are universal finite-difference algebra; they do not use zeta.

conditional on a new family-specific realization

- The corrected local decomposition, corrected whitening, transfer bounds, and boundary estimate are the layer where the manuscript uses zeta-side decomposition, omitted-zero tails, zero-free-region input, and the curvature estimate \(|S''(m)|\ll L(m)S(m)^2\).
- For another completed \(L\)-function, the same local theorem schema would go through if one can realize the same analytic package with \(Q\) replaced by the right conductor scale and with a real sign-compatible amplitude in the actual transverse channel used.
- The clean family-agnostic hypotheses are therefore:
1. a real phase \(\Phi\) on the critical-line object being studied, holomorphic on the microscopic disk;
2. positive-definite same-point jet Gram matrices on that disk, so whitening is holomorphic;
3. a corrected decomposition into baseline plus perturbation for which the same-point and mixed-block perturbations are \(O(S_2)\);
4. a transfer theorem preserving the \(Q^{-3}\) scale after applying \(\Phi_K\);
5. a boundary bound \(|H_m(s)|\ll \mathcal B(m)/Q^3\);
6. if one also wants the matrix-level calibration package, a real amplitude \(S(m)\) and a nontrivial pairing \(\langle A_{\val}(x),M(d)\rangle\asymp x/B\).

missing

- A completed-\(L\) realization theorem proving those six hypotheses outside zeta.
- A decision, in non-self-dual settings, on the correct real critical-line object. Raw complex values \(L(1/2+it,\chi)\) do not automatically fit the manuscript's real-phase and odd-sign setup.
- A family-uniform microscopic denominator comparability theorem replacing the zeta omitted-zero denominators.
- A conductor-uniform curvature or shell estimate strong enough to force the boundary scale \(Q^{-3}\).
- A proof that the actual family carries a sign-compatible value-channel amplitude replacing \(S(m)\).

where the theorem must stop

- It may assert odd holomorphy, coefficient control, and discrete odd-jet cancellation for \(H_m\).
- It may include the matrix-level calibration template only as a conditional addon requiring a realized amplitude and toy pairing.
- It must **not** assert any global contradiction, any GRH consequence, any sign theorem for remote endpoint-gap functions, or any portability of the late RH-specific endgame.

# Exact refs

- Abstract local kernel and jet package: `paper/proof_of_rh.tex:145-269`.
- First explicitly zeta-side layer and curvature estimate: `paper/proof_of_rh.tex:271-301`.
- Matrix-level value-channel derivative, \(\Phi_K(A_{\val})=0\), small-\(x\) expansion, toy pairing, calibration functional: `paper/proof_of_rh.tex:426-850`.
- Corrected local decomposition with all auxiliary/tail/error terms internal to the corrected scalar: `paper/proof_of_rh.tex:1497-1622`.
- Cutoff stability and preserved \(Q^{-3}\) transfer scale after whitening: `paper/proof_of_rh.tex:1624-1754`.
- Odd holomorphic transverse scalar and microscopic coefficient bounds: `paper/proof_of_rh.tex:2212-2322`.
- Universal discrete odd-moment projector coefficients and Mellin symbol: `paper/proof_of_rh.tex:2975-3169`.
- Honest boundary of local methods and RH-specific nature of the remaining global step: `paper/proof_of_rh.tex:25842-26022`.
- Cycle synthesis aligning with this boundary: `grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:8-67`.

# Dependencies

- Real phase formalism and jet normalization.
- Holomorphic functional calculus for \(G^{-1/2}\) on positive-definite same-point blocks.
- Existence of a corrected decomposition into baseline plus perturbation.
- A family-specific transfer estimate giving \(\Phi_K\)-error \(\ll S_2/Q^3\).
- A family-specific microscopic boundary estimate for the transverse scalar.
- For the calibration addon: a real amplitude \(S(m)\), background slope \(B\), and a toy anomaly matrix with nonzero pairing against \(A_{\val}\).

# Strongest objection

The current manuscript does not prove this theorem schema in a family-agnostic form. Even though the algebraic core is abstract, the actual odd holomorphic scalar \(H_m\) in the draft is produced only after a zeta-specific corrected decomposition, denominator comparability, and curvature estimate. So the proposed schema is a clean extraction of what the RH draft supports, but it is not yet an autonomous theorem for completed \(L\)-functions. In particular, for complex Dirichlet characters the required real phase and sign-compatible amplitude are not supplied by the present paper.

# Needed for promotion

The smallest concrete unresolved sub-statements are:

1. **Completed-\(L\) local realization.** Construct the analogue of the corrected finite-\(s\) whitened block and prove holomorphy on \(|s|<\rho_0/Q\).
2. **Microscopic denominator comparability.** Prove the omitted-zero denominators in the new family stay comparable on the complex microscopic disk.
3. **Transferred perturbation bound.** Prove same-point and mixed-block perturbations are \(O(S_2)\), and after whitening and \(\Phi_K\) give \(\ll S_2/Q^3\).
4. **Boundary theorem.** Prove \(|H_m(s)|\ll \mathcal B(m)/Q^3\) on \(|s|=\rho_0/Q\) with the correct conductor scale.
5. **Real amplitude channel.** Identify a real, sign-compatible amplitude replacing \(S(m)\) in the family under study.
6. **Non-self-dual object choice.** For complex characters, decide whether the correct package is built from a rotated single channel, a \((\chi,\bar\chi)\)-paired scalar, or a matrix-valued object.

Honest verdict: the RH draft contains a real portable **local package template**, but only up to the odd holomorphic scalar plus universal odd-moment projector. Everything beyond that boundary is still family-specific analytic realization, not a proved GRH-style extension.
