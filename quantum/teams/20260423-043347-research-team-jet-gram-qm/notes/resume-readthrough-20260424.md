# Resume Readthrough - 20260424

Scope: full local reconstruction of
`quantum/teams/20260423-043347-research-team-jet-gram-qm`, including top-level
reports, `HANDOFF-20260424.md`, `INDEX.md`, `findings.md`, all
`agents/*/reports/*.md`, and the agent notes/briefs. The only prior no-deposit
subdir is `agents/20260424-040334-attack-biunitary-classification/`.

## Chronology

1. **Source-faithful naming.** The first research team rejected broad
   "quantum tensor" language and settled on **whitened local jet cross-Gram
   block** as the source-faithful object. The verifier/source reports keep the
   zeta-side object narrow: same-point jet Gram blocks, a mixed cross block, and
   bilateral whitening.

2. **First-order bridge.** The first real positive theorem is the same-point
   horizontal derivative Gram matrix
   \(Q_{ab}=\langle D_a\psi,D_b\psi\rangle\), exactly the pure-state QGT.
   The two-point first-horizontal-jet block is narrower: invariant under
   orientation-preserving reparameterization, transforms by
   \(E\Omega E\) under reversal, and descends to ray curves only after a
   gauge-covariant transport rule is fixed.

3. **Transport caveat.** Fixed transport is part of the data. Arbitrary
   gauge-covariant transports can change entries by more than a global phase.
   In the reduced scalar-phase class, Berry/Pancharatnam-type choices differ
   only by a global phase, so singular values are transport-class invariant
   there. Outside that class, endpoint-canonicity is not proved.

4. **Higher-jet failure and repair.** Raw projected higher jets mix by
   invertible upper-triangular laws under gauge and reparameterization, so raw
   higher-jet Gram/whitened matrices fail. The spans \(O_r\) survive. One- and
   multi-parameter Berry-covariant jet hierarchies have since been proved to
   generate the same \(O_r\) spaces, and symmetrized multiparameter jets generate
   the same filtration. This closes "find a covariant hierarchy"; it does not
   close "find a canonical ordered matrix."

5. **Ambient subspace pivot.** Because endpoints live in a common Hilbert
   space, \(A_r=\mathrm{span}\{\psi\}\oplus O_r\) gives transport-free
   principal-angle/projector data. \(O_r\) is the quotient of \(A_r\) by the
   state line and is value-channel-free. The archive does not justify a unique
   global winner; the role split is intentional.

6. **Benchmarks.** Oscillator is a reparameterization sanity check but its
   singular values collapse to overlap. Qutrit/quartit/Veronese and spherical
   twist benchmarks prove that the surviving \(A_r\) and \(O_r\) data can be
   richer than overlap. Lower-order Veronese results are complement-basis
   theorems, not closed spectral formulas.

7. **Operator package.** The endpoint subspace pair has a canonical
   cross-contraction \(C=\Pi_-|_{S_+}\), positive compressions
   \(K_\pm=C^*C,CC^*\), and polar partial isometry \(V\). Simple nonzero
   spectrum gives canonical principal frames up to phase/sign; repeated nonzero
   spectrum gives an exact no-go for canonical frames from the pair alone.
   Finite-dimensional CS normal form proves the principal-angle/operator package
   is complete up to ambient unitary equivalence.

8. **Dynamics.** Exact unitary orbits give transported Krylov/compressed-Krylov
   spaces, compressed-propagator formulas, finite-cyclic saturation, and a
   Jacobi/Lanczos normal form in that specialization. Kato transport gives an
   exact pathwise model, and Kato curvature explains why endpoint-independent
   transport fails generically. These are useful corollaries, not a new general
   matrix theorem.

## Proved / Conditional / Missing

**Proved.**
- First-order QGT bridge.
- First-horizontal-jet reparameterization laws with transport caveats.
- Higher-jet subspace survival and covariant-jet subspace hierarchies.
- \(A_r\), \(O_r\), quotient, benchmark richer-than-overlap examples.
- Operator package, simple-spectrum frame corollary, repeated-spectrum no-go,
  finite-dimensional CS completeness.
- Exact unitary/Krylov, Kato transport, and Kato curvature corollaries.

**Conditional on extra structure.**
- Any entrywise two-point matrix after choosing transport and endpoint frames.
- Scalar-phase transport-class statements beyond the explicitly restricted
  first-order class.
- Smooth pathwise polar/frame regularity until perturbation details are written.
- Jacobi/Lanczos matrix packages outside the exact finite-cyclic unitary
  specialization.

**Missing.**
- A paper-ready theorem stating that all orthonormal-frame comparison matrices
  for a fixed subspace pair are exactly the biunitary orbit of one representative,
  with singular values/principal angles as the complete invariant. The stale
  `20260424-040334-attack-biunitary-classification` brief targeted this but has
  no report.
- A final honest decision on whether the note's open matrix problem is now closed
  negatively by the operator/CS package, or whether some extra natural
  frame-selecting structure should be named and isolated.
- A genuinely natural dynamical/experimental protocol stronger than the current
  projector yes/yes test and exact unitary/Kato repackagings.

## Best Next Move

Do a focused UV-012 attack, not a 3+3+2 cycle. The old agents have already
exhausted the broad example and covariant-jet lanes. The highest-leverage missing
piece is the finite-dimensional matrix-finality theorem:

> For a fixed canonical subspace pair \(S_-,S_+\), every orthonormal-frame
> comparison matrix is \(LAR\) for one representative \(A\) and unitaries
> \(L,R\), and two such matrices have the same canonical content exactly when
> they have the same singular values. Therefore no entrywise matrix is canonical
> without a frame-selection rule.

One gap-closer should write the theorem and proof. One adversarial verifier
should test whether it actually closes UV-012 or only restates existing
principal-angle facts.
