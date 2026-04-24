# Quantum Findings

Active briefing log for the jet-Gram / quantum-mechanics side track.

Last-pruned: 20260424. Matured details absorbed into
`quantum/paper/jet_gram_quantum_note.md` are indexed in
`quantum/findings-in-paper.md`.

Question:
- Can the normalized local jet-Gramian from `paper/proof_of_rh.tex` be recast
  as a gauge-invariant structure on families of quantum states?

Source anchor:
- The paper's local object is the normalized local jet-Gramian attached to the
  corrected phase geometry (`paper/proof_of_rh.tex` line 114), with jet-limit
  form `\Omega_\infty(T_1,T_2)=M_1^{-1/2}N_{12}M_2^{-1/2}` (lines 171--215)
  and finite-separation form
  `\widehat\Omega_\zeta(s;m)=G_{m,-}(s)^{-1/2}N_m(s)G_{m,+}(s)^{-1/2}`
  (lines 226--259).

## Confirmed

- The most source-faithful current name is **whitened local jet cross-Gram
  block**. It tracks the kernel-side construction better than stronger language
  such as a full quantum-geometric tensor, scattering matrix, or fundamental
  quantum structure.
- For a smooth normalized pure-state family, the same-point horizontal
  derivative Gram matrix `Q_ab = <D_a psi | D_b psi>` is exactly the quantum
  geometric tensor. This is the narrow first-order bridge.
- For one-parameter curves, the bilaterally whitened first-horizontal-jet
  two-point block is reparameterization invariant up to the recorded
  orientation-reversal sign conjugation, once the transport rule is fixed.
- Raw higher projected coordinate-jet matrices fail under phase gauge and
  reparameterization. The osculating subspace
  `O_r = span{j_1,...,j_r}` survives exactly.
- The one-parameter Berry-covariant jet hierarchy and the multiparameter
  ordered/symmetrized covariant-jet hierarchies generate the same canonical
  `O_r` subspaces as the raw mixed partials.
- In a fixed ambient Hilbert space, endpoint `A_r` and `O_r` subspaces determine
  transport-free principal angles, projector compressions, cross-contractions,
  polar partial isometries, and the associated operator package.
- Fixed endpoint subspaces determine all orthonormal-frame comparison matrices
  only up to a biunitary orbit. The singular values/principal-angle cosines are
  complete orbit data; entrywise matrices require extra frame-selecting
  structure.
- In several parameters, raw, covariant, and symmetrized jet hierarchies
  determine the `O_r`/`A_r` filtrations and the corresponding
  operator/principal-angle package, but no ordered frame or matrix from
  ray-field data alone.
- The exact relation `A_r = span{psi} \oplus O_r` gives a role split:
  `O_r` is the horizontal value-channel-removed object, while `A_r` is the
  ambient endpoint-subspace extension. No unique global winner is forced by the
  current invariant package.
- With coherent reflection access to endpoint projectors, phase estimation on
  `(2Pi_- - I)(2Pi_+ - I)` estimates the already-canonical principal-angle
  spectrum. This is a protocol for existing invariant data, not a new invariant.
- First-order value-channel-free richer-than-overlap behavior is generic in a
  finite-jet sense for normalized real `C^2` curves in dimension at least `3`,
  under the endpoint `2`-jet rank condition verified in the UV-015 reports.
- Explicit qutrit, quartit, Veronese, and spherical-twist benchmarks show that
  the surviving `A_r`/`O_r` two-point data can be richer than endpoint overlap
  alone.

## Conditional / Scope Limits

- The transported first-jet matrix is a ray-curve-with-transport invariant, not
  a transport-independent endpoint invariant.
- The oscillator benchmark is a useful first-order stress test, but its
  singular values reduce to endpoint overlap and do not prove richer endpoint
  geometry.
- Simple nonzero projector spectrum gives canonical principal directions up to
  phases/signs; repeated spectrum gives only the block partial isometry.
- Kato transport is a pathwise model. Nonzero Kato curvature blocks an
  endpoint-independent transport construction in several parameters.
- The finite-jet genericity theorem is first-order `O_1`, real-open-dense in
  the stated chart, and does not claim genericity for all higher `O_r/A_r`
  observables.

## Negative / Retry Guards

- Do not retry a raw higher-jet matrix invariant under gauge/chart changes
  without adding explicit frame-selecting structure.
- Do not treat a biunitary-orbit representative as canonical entrywise data.
- Do not upgrade Kato transport, coherent-reflection phase estimation, or
  benchmark examples into a universal physical implementation.
- Do not claim a globally forced choice between `A_r` and `O_r`; the proven
  statement is the role split.

## Goodies / Reusable Examples

- The qutrit polynomial curve
  `psi(t)=(1,t,t^2)^T/sqrt(1+t^2+t^4)` has an explicit equal-overlap /
  different-`O_1` witness.
- The quartit cubic curve
  `psi(t)=(1,t,t^2,t^3)^T/sqrt(1+t^2+t^4+t^6)` has second-order `O_2` data
  finer than `A_2` on the recorded witness pair.
- The Veronese family gives the exact ambient complement
  `A_r(t)^\perp = Coeff((x-t)^{r+1} R_{<= n-r-1}[x])` and the corresponding
  value-channel-free complement
  `O_r(t)^\perp = span{psi_n(t)} \oplus Coeff((x-t)^{r+1} R_{<= n-r-1}[x])`.
- The spherical-twist curve
  `psi(t)=(cos t cos 2t, cos t sin 2t, sin t)` gives a non-Veronese
  equal-overlap witness for richer `A_1` and `O_1` data.

## Future Extensions

- General lower-order (`r < n-1`) Veronese-family principal-angle formulas,
  especially on the value-channel-free `O_r` side.
- Higher-order `O_r/A_r` genericity beyond first-order `O_1`.
- A source-specific physical implementation of the reflection protocol.
