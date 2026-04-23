# gap-Ar-Or-krylov

- **Claim**: In the exact unitary/Krylov specialization, the cleanest role split is: `A_r` is the transported ordinary Krylov space including the state line, while `O_r` is the exact value-channel-removed / compressed Krylov space. This sharpens intuition but still does not force a unique global choice between them.
- **Status**: proved
- **Evidence**: The exact identities `A_r(t)=e^{-itH} span{psi_0,H psi_0,...,H^r psi_0}` and `O_r(t)=A_r(t) ∩ psi(t)^⊥` hold. So `A_r` is the natural ambient dynamical object, `O_r` the natural quotient/horizontal one.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:343-348`; `quantum/findings.md:70-79`; `quantum/teams/20260423-234222-attack-Ar-Or-krylov/notes/coordinator-brief.md:3-10`.
- **Dependencies**: The exact unitary/Krylov identities.
- **Strongest objection**: This is an exact role split, not a uniqueness theorem.
- **Needed for promotion**: Already reflected in the note’s `A_r` / `O_r` discussion.
