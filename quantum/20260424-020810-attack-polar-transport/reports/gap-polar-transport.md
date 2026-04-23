# gap-polar-transport

- **Claim**: Let \(S_-,S_+\subset \mathcal H\) be a canonical pair of endpoint subspaces in a common ambient Hilbert space, with orthogonal projectors \(\Pi_\pm\), and define the canonical cross-contraction
  \[
  C:=\Pi_-\big|_{S_+}:S_+\to S_-.
  \]
  Then \(C\) is a canonical bounded contraction with
  \[
  C^*=\Pi_+\big|_{S_-},\qquad C^*C=\Pi_+\Pi_-\Pi_+\big|_{S_+}=:K_+,
  \qquad CC^*=\Pi_-\Pi_+\Pi_-\big|_{S_-}=:K_-.
  \]
  Hence \(C\) has a canonical polar decomposition
  \[
  C=V\,|C|,
  \qquad |C|=(K_+)^{1/2},
  \]
  where \(V:S_+\to S_-\) is the unique partial isometry with initial space
  \(\overline{\mathrm{ran}\,|C|}\) and final space \(\overline{\mathrm{ran}\,C}\). Equivalently, \(V\) canonically identifies the nonorthogonal-overlap sector of \(S_+\) with the corresponding sector of \(S_-\), intertwines the nonzero spectral subspaces of \(K_+\) and \(K_-\), and on each principal-angle block with \(\cos\theta>0\) acts as the canonical operator-level transport. This is stronger than the simple-spectrum frame corollary, but it still carries no more invariant content than the principal-angle / projector-product data. It does not canonically choose bases inside repeated-singular-value sectors.
- **Status**: proved
- **Evidence**: Proved: the note already establishes that for canonical endpoint subspaces the projector compressions \(K_\pm\) are canonical and their nonzero spectra are the squared principal-angle cosines. Therefore \(C=\Pi_-|_{S_+}\) is itself canonical, and \(C^*C=K_+\), \(CC^*=K_-\) follow by direct projector algebra. Standard polar decomposition then gives a unique partial isometry \(V\) from \((\ker C)^\perp=\overline{\mathrm{ran}\,|C|}\) onto \(\overline{\mathrm{ran}\,C}\). Since \(K_\pm\) are canonical, so are \(|C|=(K_+)^{1/2}\) and \(V\). This yields an exact operator-level transport on the sector where \(\cos\theta_i>0\), including the common-intersection sector \(\theta_i=0\). Conditional: if the nonzero spectrum is simple, \(V\) upgrades to canonical paired principal vectors, recovering the diagonal frame theorem. Missing: no exact theorem turns \(V\) into a canonical full matrix-valued comparison object without extra frame choices; repeated singular values leave internal unitary freedom.
- **Exact refs**: `quantum/paper/jet_gram_quantum_note.md:356-372`; `quantum/findings.md:73-79`; `quantum/20260423-141619-attack-projector-operator/reports/gap-projector-operator.md:3-19`; `quantum/20260424-003729-attack-canonical-frames/reports/gap-canonical-frames.md:3-26`; `quantum/20260424-020810-attack-polar-transport/notes/coordinator-brief.md:3-12`.
- **Dependencies**: Fixed common ambient Hilbert space; the already-proved canonicity of the endpoint subspaces \(S_\pm\); orthogonal projector identities; standard principal-angle theorem identifying \(\operatorname{spec}(K_\pm)\setminus\{0\}\) with \(\{\cos^2\theta_i\}\); standard polar decomposition for bounded operators between Hilbert spaces.
- **Strongest objection**: The polar factor \(V\) is canonical only as a basis-free partial isometry on the nonzero singular sector. It does not produce a canonical entrywise matrix or canonical frames inside degenerate principal-angle sectors, and it does not add invariant content beyond the projector-product / principal-angle package already known.
- **Needed for promotion**: State the theorem at operator level, not frame level: \(C=\Pi_-|_{S_+}\) is the canonical contraction, \(K_\pm=C^*C,CC^*\) are the canonical positive factors, and the polar partial isometry \(V\) is the strongest exact canonical transport presently justified. Then explicitly separate this from the stronger but only conditional matrix-frame claim: canonical principal frames require simple nonzero spectrum.
