# gap-oscillator-singular-values

- **Claim**: For the variable-frequency oscillator benchmark, the singular values of the whitened first-horizontal-jet block admit an exact closed form, but in this family they reduce to a function of the endpoint overlap alone. So they do not provide richer endpoint information than overlap/fidelity here.
- **Status**: proved
- **Evidence**: The benchmark block depends only on the squeeze separation \(\Delta r\), and the singular values collapse to explicit functions of \(\operatorname{sech}^{1/2}(\Delta r)\), i.e. of the overlap itself. This makes the oscillator a useful sanity check, not a richer-than-overlap example.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:484-533`; `quantum/findings.md:99-115`; `quantum/teams/20260423-131859-attack-oscillator-singular-values/notes/coordinator-brief.md:3-13`.
- **Dependencies**: The exact oscillator first-jet benchmark formulas already used in the note.
- **Strongest objection**: This is benchmark-specific and negative rather than structural.
- **Needed for promotion**: None beyond keeping it as a cautionary benchmark.
