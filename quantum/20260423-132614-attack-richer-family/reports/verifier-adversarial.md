# verifier-adversarial

- **Claim**: The real qutrit curve \(\ket{\psi(t)}=(1,t,t^2)^T/\sqrt{1+t^2+t^4}\) is a sound next first-order one-parameter benchmark for the quantum note, because in the reduced scalar-phase transport setting its bilaterally whitened first-horizontal-jet singular values are not determined by endpoint overlap alone. The note must keep the claim narrow: this is a first-order, one-parameter, scalar-phase-transport result, not a transport-independent or endpoint-canonical matrix theorem.
- **Status**: proved
- **Evidence**: Proved: for this real normalized family, \(\langle \psi(t),\partial_t\psi(t)\rangle=0\), so the first horizontal jet is just \(h_t=\partial_t\psi(t)\). With identity/scalar-phase transport, the whitened \(2\times2\) block is the overlap matrix between orthonormal bases of the two endpoint first-jet planes \(\mathrm{span}\{\psi(t_\pm),h_{t_\pm}\}\). In \(\mathbb R^3\), two \(2\)-planes always share a line, so one singular value is exactly \(1\). Proved: the second singular value is the cosine of the angle between the plane normals. Using the unnormalized lift \(u(t)=(1,t,t^2)\), a normal is \(n(t)=u(t)\times u'(t)=(t^2,-2t,1)\), so
  \[
  \sigma_2(t_-,t_+)=\frac{|1+4t_-t_+ + t_-^2 t_+^2|}{\sqrt{1+4t_-^2+t_-^4}\sqrt{1+4t_+^2+t_+^4}}.
  \]
  The endpoint overlap is
  \[
  I(t_-,t_+)=\frac{|1+t_-t_+ + t_-^2 t_+^2|}{\sqrt{1+t_-^2+t_-^4}\sqrt{1+t_+^2+t_+^4}}.
  \]
  These are different invariants. Proved: if \(\sigma_2\) were determined by overlap alone, then the Jacobian \(\det \partial(I,\sigma_2)/\partial(t_-,t_+)\) would vanish identically. Direct differentiation gives a nonzero value already at \((0,1)\): \(\sqrt2/2\neq 0\). So the richer-than-overlap claim is true for this family. Conditional: this proof uses the reduced scalar-phase transport class; for this real curve that is the natural class, but from present scope alone it does not upgrade to unrestricted gauge-covariant transports. Missing: an in-note deposited derivation or script, and any theorem extending this richer-than-overlap behavior beyond first order / one parameter / scalar-phase transport.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:225-247,300-332`; `quantum/findings.md:78-82,99-113`; `quantum/20260423-132614-attack-richer-family/notes/coordinator-brief.md:3-14`.
- **Dependencies**: One-parameter \(C^1\) pure-state curve; nonzero first horizontal jets at the chosen endpoints; reduced scalar-phase transport class; first-order bilaterally whitened block interpreted as principal-angle data of endpoint first-jet planes.
- **Strongest objection**: The positive verdict is narrower than the benchmark might first suggest. From present scope alone, it does not show a transport-independent endpoint invariant, does not justify the full matrix entrywise, and does not imply that generic one-parameter families will also separate singular values from overlap.
- **Needed for promotion**: The note should state this benchmark with the exact caveats: first-order only; one-parameter only; scalar-phase transport class only; singular values/principal angles are the honest invariant content; no claim that the full matrix is canonical. A short deposited derivation of the formulas for \(I\) and \(\sigma_2\), or the Jacobian test above, would make the benchmark promotion-ready.
