# verifier-adversarial

- **Claim**: The note should not include the Krylov reading as a substantive new pillar. At most it supports a short exact remark: for unitary one-parameter families, `A_r(t)` is the transported order-`r` Krylov space and `O_r(t)` is its value-channel-removed / compressed counterpart.
- **Status**: proved
- **Evidence**: Proved: the Krylov reading is exact for `A_r` and exact in compressed form for `O_r`. Conditional: this is a natural dynamical specialization of the current subspace framework. Missing: any payoff beyond repackaging the existing subspace theorem, any new invariant, and any reason to enlarge the main theorem spine because of it.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:298-350`; `quantum/findings.md:50-76`; `quantum/20260423-201939-attack-krylov/notes/coordinator-brief.md:5-13`.
- **Dependencies**: The exact unitary-orbit assumption \(\psi(t)=e^{-itH}\psi_0\); the note’s existing `A_r` / `O_r` definitions.
- **Strongest objection**: Without a concrete downstream use, this is mostly a dynamical relabeling of subspace data rather than a new theorem with independent leverage.
- **Needed for promotion**: If added, keep it to a short remark and explicitly distinguish standard Krylov (`A_r`) from compressed Krylov (`O_r`).
