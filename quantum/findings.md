# Quantum Findings

Active findings log for the jet-Gram / quantum-mechanics side track.

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

- The paper's object is a whitened local overlap/correlation block built from
  same-point jet Gram matrices and a mixed cross block. That makes a quantum
  reinterpretation plausible in form, because Gram matrices and gauge-quotiented
  local state geometry are standard motifs in quantum theory.
- The most source-faithful current name is **whitened local jet cross-Gram
  block**. This tracks the explicit kernel-side construction in
  `paper/proof_of_rh.tex:149-259` better than stronger language such as QGT,
  RKHS, scattering matrix, or fundamental quantum structure.
- The first horizontal jet of a smooth pure-state family plausibly reduces to
  standard one-point quantum geometry: Fubini-Study metric / QGT / Berry data.
  That supports a narrow first-order bridge, not yet a full higher-jet theorem.
- The exact first-order bridge is now sharp enough to state cleanly: for a
  smooth normalized pure-state family, the same-point horizontal-derivative Gram
  matrix `Q_ab = <D_a psi | D_b psi>` is the quantum geometric tensor. This is
  the source-faithful quantum-side analogue of “remove the value channel, then
  form a same-point jet Gram block.”
- There is now a real narrow theorem on the two-point side: for a
  one-parameter normalized pure-state family, with first horizontal jet,
  fixed transport, and orientation-preserving reparameterization, the
  bilaterally whitened first-jet two-point block is unchanged.
- That theorem also descends from a fixed-lift statement to a ray-curve
  statement once a gauge-covariant transport rule is included as part of the
  data. What is obtained is a ray-curve-with-transport invariant, not yet a
  transport-independent endpoint invariant.
- Under orientation-reversing reparameterization, the exact first-order law is
  not equality but `E \Omega E` with `E = diag(1,-1)`, provided endpoint labels
  are kept fixed. So reversal flips only the derivative channel.
- No canonical matrix-valued two-point quantum invariant has been justified so
  far. The safest verified framing is subspace-level: transported horizontal-jet
  subspaces, with singular values or principal angles as the honest invariant
  content.
- For higher raw projected coordinate jets `j_k = P ∂_λ^k ψ`, the ordered jet
  list changes by invertible upper-triangular transformations under both phase
  gauge and one-parameter reparameterization. So raw higher-jet matrices fail,
  but the osculating subspace `O_r = span{j_1,...,j_r}` is exactly preserved.
- In a fixed ambient Hilbert space, this gives a transport-free subspace-level
  output: principal angles between endpoint osculating subspaces are canonical.
  This is safe only as an ambient-subspace theorem, not as a transport-free
  matrix theorem.
- The ambient-subspace theorem extends cleanly to several parameters if one
  takes all mixed partials of total order `<= r`: the resulting ambient
  osculating subspace is chart- and gauge-invariant, while no corresponding
  multiparameter matrix theorem is currently justified.
- As a basis-free corollary, the orthogonal projector products onto these
  canonical ambient subspaces give canonical operators whose spectra are the
  squared principal-angle cosines. This is a clean reformulation, not stronger
  invariant content.
- The exact relation is `A_r = span{psi} \oplus O_r`. `O_r` is the faithful
  value-channel-removed object; `A_r` is the ambient subspace that currently
  supports the strongest transport-free two-point theorem. The present record
  does not justify a unique global winner between them.
- On the current qutrit/quartit benchmarks, `O_r` already carries richer
  two-point geometry than overlap alone. On the quartit second-order benchmark,
  `O_2` is actually finer than `A_2` at the level of principal-angle data.

## Conditional

- A plausible reformulation is: take a smooth family of normalized states,
  project derivatives orthogonally to the instantaneous ray, form same-point and
  mixed jet Gram blocks, then whiten to get a finite-separation transport matrix.
  This would make the construction look like a higher-jet, finite-separation
  extension of quantum geometric tensor / Berry / Fubini-Study data.
- A safer repaired object may be the transported overlap of orthonormal jet
  subspaces, with invariant content given by singular values or principal
  angles, rather than the full whitened matrix entry-by-entry.
- The best initial toy models are a qubit great-circle family and a coherent
  state displacement family. They show the shape of the construction, but they
  do not yet test asymmetric endpoint whitening or genuinely inhomogeneous jet
  geometry.
- A stronger benchmark example is the harmonic-oscillator ground-state family
  with variable frequency. In the `\omega` parameter its same-point first-jet
  block is exact and nonconstant, so it is a good stress test for bilateral
  whitening. But this asymmetry is parameter-sensitive and therefore not yet an
  intrinsic invariant.
- In that oscillator benchmark, the raw same-point and mixed first-jet blocks
  change under `\omega \leftrightarrow r=\tfrac12\log\omega`, but the
  bilaterally whitened first-jet two-point block stays unchanged. This is a
  real positive signal, but currently only for that specific one-parameter
  first-order calculation.

## Negative

- In the oscillator benchmark, the singular values of the whitened first-jet
  block admit a closed form but reduce to a function of the endpoint overlap
  alone. So that example does not show singular values carrying richer endpoint
  information than overlap/fidelity.

## Goodies

- The real qutrit polynomial curve
  `|psi(t)> = (1,t,t^2)^T / sqrt(1+t^2+t^4)` is the first clean benchmark where
  the singular values of the whitened first-horizontal-jet block are not
  determined by endpoint overlap alone, at least in the reduced scalar-phase
  transport class. One singular value is `1`; the second is the cosine between
  endpoint first-jet plane normals.
- For that qutrit benchmark, the direct whitened block `Omega(u,v)` is now
  explicit, and there is an exact rational witness pair with equal overlap but
  different second singular value.
- The real quartit cubic curve
  `|psi(t)> = (1,t,t^2,t^3)^T / sqrt(1+t^2+t^4+t^6)` is the natural next
  higher-jet benchmark: second-jet matrices fail under triangular mixing, while
  the second osculating subspace is a genuine varying `3`-plane in `R^4`.
- For that quartit benchmark, the surviving second-order singular values are
  exactly `(1, 1, sigma_3(u,v))`, where `sigma_3` is the cosine between the
  endpoint osculating-plane normals. There is also an explicit equal-overlap /
  different-`sigma_3` witness pair.

## Missing

- Exact gauge-invariant definition of the quantum-side jet vectors.
- Higher-jet covariantization that survives phase gauge and reparameterization
  without hidden coordinate leakage.
- Precise reduction of the first nontrivial jet level to known quantum geometry.
- Proof that any matrix-valued two-point object, rather than only singular
  values / principal angles of transported jet subspaces, is canonical.
- Operational interpretation: fidelity, adiabatic response, scattering, or
  another measurable quantity.
- Worked examples beyond analogy.
- A nonconstant, asymmetric example that better matches the paper's left/right
  whitening pattern.
- Canonical transport, higher-jet covariantization, and frame-selection results
  strong enough to justify a matrix-valued two-point invariant.
- A general theorem explaining when one-parameter first-jet bilateral
  whitening is reparameterization invariant, and when that phenomenon fails.
- A phase-gauge/transport theorem strong enough to turn the narrow first-jet
  reparameterization result into a transport-independent canonical ray-space
  statement.
- A principled restriction of the admissible transport class. With only a bare
  gauge-covariant transport rule, remaining ambiguity can be larger than a
  global phase on the matrix.
- If one explicitly restricts to scalar-phase transports of the endpoint
  first-jet pair, the remaining ambiguity drops to a single global phase on the
  whitened first-horizontal-jet block. Berry and Pancharatnam fall into this
  same phase class when endpoint overlap is nonzero.
- The singular values of the bilaterally whitened first-horizontal-jet block are
  already invariant under lift change and all reparameterizations for a fixed
  gauge-covariant transport. In the reduced scalar-phase transport class they
  are also transport-class invariant.
- In the identity/scalar-phase setting, those first-order singular values are
  exactly the principal-angle cosines of the ambient planes
  `A_1(λ)=span{ψ(λ), h_λ}`.
