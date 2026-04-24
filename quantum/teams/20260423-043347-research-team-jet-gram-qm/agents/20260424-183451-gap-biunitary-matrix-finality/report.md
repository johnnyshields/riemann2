# Biunitary Matrix Finality for UV-012

**Claim**

For fixed finite-dimensional endpoint subspaces \(S_-,S_+\subset\mathcal H\), with
\(\dim S_-=p\) and \(\dim S_+=q\), choose orthonormal frame isometries
\(U_-:\mathbb C^p\to S_-\) and \(U_+:\mathbb C^q\to S_+\). The comparison matrix
\[
A:=U_-^*U_+\in M_{p\times q}(\mathbb C)
\]
is the matrix of the canonical cross-contraction
\[
C:=\Pi_-|_{S_+}:S_+\to S_-
\]
in these frames, since \(A=U_-^*CU_+\). If the frames are changed to
\(\widetilde U_-=U_-L\) and \(\widetilde U_+=U_+R\), with
\(L\in U(p)\), \(R\in U(q)\), then
\[
\widetilde A=L^*AR.
\]
Conversely, every orthonormal-frame comparison matrix for the same subspace pair
arises this way. Therefore the full set of entrywise matrices attached to the
fixed subspace pair is exactly the biunitary orbit
\[
\{L^*AR:L\in U(p),\ R\in U(q)\}.
\]
For fixed \(p,q\), two rectangular comparison matrices lie in the same orbit if
and only if they have the same singular values, counted with multiplicity and
including zeros up to \(\min(p,q)\). These singular values are the principal-angle
cosines of \((S_-,S_+)\). Hence, from the subspace pair alone, no entrywise
comparison matrix is canonical beyond its biunitary orbit. The surviving
canonical content is exactly the already-recorded principal-angle /
projector-spectrum / polar-operator package, with the simple-spectrum frame
corollary and repeated-spectrum no-go as the sharp qualified exceptions.

**Status**

proved

**Evidence**

Proved. Any two orthonormal frames of \(S_-\) differ by a unique unitary
\(L\in U(p)\), and any two orthonormal frames of \(S_+\) differ by a unique
unitary \(R\in U(q)\). Thus the frame-change law is exactly
\((U_-L)^*(U_+R)=L^*(U_-^*U_+)R\), and the converse is immediate by choosing
\(\widetilde U_-=U_-L\), \(\widetilde U_+=U_+R\).

The orbit classification is the rectangular singular-value theorem. If
\(B=L^*AR\), then \(B^*B=R^*A^*AR\), so \(A\) and \(B\) have the same singular
values. Conversely, if \(A\) and \(B\) have the same singular values, their SVDs
can be written with the same rectangular diagonal block
\(\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_{\min(p,q)})\), including
zero entries in rank-deficient cases:
\[
A=P_A\Sigma Q_A^*,\qquad B=P_B\Sigma Q_B^*.
\]
Then \(B=L^*AR\) with \(L=P_AP_B^*\) and \(R=Q_AQ_B^*\), after the harmless
standard completion of singular-vector bases in null spaces. This covers
rectangular and rank-deficient matrices.

The singular values of \(A=U_-^*U_+\) are the singular values of
\(C=\Pi_-|_{S_+}\), hence the principal-angle cosines for the subspace pair.
Equivalently, their squares are the eigenvalues of the canonical positive
compressions \(C^*C=\Pi_+\Pi_-\Pi_+|_{S_+}\) and
\(CC^*=\Pi_-\Pi_+\Pi_-|_{S_-}\), with zero padding according to the endpoint
dimensions.

No scripts were needed; this is a finite-dimensional linear-algebra proof.

Conditional. If extra frame-selecting structure is supplied, or if the nonzero
principal spectrum is simple, one may choose matched principal frames up to
phase/sign and obtain a diagonal representative. That is an additional
hypothesis, not a matrix determined entrywise by the subspace pair alone.

Missing. Nothing is missing for the frame-comparison orbit theorem. A different
object outside this class would need additional natural structure not present in
UV-012's fixed subspace-pair data.

**Baseline / delta**

Baseline: the current findings already contain the canonical operator package
\((C,K_\pm,V)\), the simple-spectrum frame corollary, the repeated-spectrum
no-go, and finite-dimensional CS completeness, but the resume note identifies a
missing paper-ready theorem that all orthonormal-frame comparison matrices for a
fixed subspace pair are one biunitary orbit.

Delta: this report supplies that missing theorem and proof, including unequal
dimensions and rank-deficient cases. It turns UV-012 into a negative closure
from the fixed subspace-pair data alone: the entrywise matrix representative is
not canonical without extra frame-selection structure, and the complete orbit
invariant is the principal-angle singular-value list.

**Attempt status**

terminal

**Exact refs**

- `quantum/paper/jet_gram_quantum_note.md:405-454` for the canonical
  cross-contraction, positive compressions, polar partial isometry,
  simple-spectrum corollary, repeated-spectrum no-go, and finite-dimensional
  completeness.
- `quantum/paper/jet_gram_quantum_note.md:783-790` for the open matrix-valued
  two-point problem targeted by UV-012.
- `quantum/paper/benchmark_map.md` for consistent terminology: surviving
  two-point data, ambient `A_r`, value-channel-free `O_r`, and richer-than-overlap
  benchmarks.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md`:
  confirmed operator package and missing matrix/frame theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md`: UV-012,
  `quantum-open-endpoint-matrix-beyond-operator-package`.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/notes/resume-readthrough-20260424.md`
  for the explicit best next move and the stale no-deposit biunitary target.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-192358-attack-matrix-data/reports/gap-matrix-data.md`
  for the earlier orbit-level matrix-data claim.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-020810-attack-polar-transport/reports/gap-polar-transport.md`
  for the polar partial isometry.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-030000-attack-operator-package/reports/gap-operator-package.md`
  for the complete operator package.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-023315-attack-degenerate-nogo/reports/gap-degenerate-nogo.md`
  for the repeated-spectrum no-go.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-024917-attack-frame-criterion/reports/gap-frame-criterion.md`
  for the simple-spectrum iff frame criterion.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-044343-attack-completeness/reports/gap-completeness.md`
  and
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-054845-attack-cs-normal-form/reports/gap-cs-normal-form.md`
  for finite-dimensional CS completeness.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-040334-attack-biunitary-classification/notes/coordinator-brief.md`
  for the prior targeted but undeposited biunitary-classification brief.

**Dependencies**

Finite-dimensional endpoint subspaces in a common Hilbert space; orthonormal
frame isometries; the canonical cross-contraction \(C=\Pi_-|_{S_+}\); standard
finite-dimensional SVD for rectangular matrices; standard principal-angle theory
identifying singular values of \(U_-^*U_+\) with principal-angle cosines;
unitary-equivariant meaning of "canonical from the pair alone."

**Strongest objection**

The no-canonical-entrywise conclusion depends on the naturality requirement that
"canonical from the subspace pair alone" be invariant under unitary changes of
orthonormal frames, equivalently under automorphisms of the presented frame
coordinates. Without that requirement one can choose arbitrary bases by external
convention, but that is exactly extra frame-selecting structure. This objection
does not affect the orbit theorem itself.

**Needed for promotion**

An adversarial verifier should check the wording does not overclaim beyond the
frame-comparison class. If accepted, promote as a short theorem after the
operator-package paragraph: state the biunitary orbit theorem, mention
rectangular/rank-deficient coverage through SVD, and close UV-012 negatively from
the fixed subspace-pair data alone. Keep the exceptions as already qualified:
simple nonzero spectrum gives diagonal frames up to phase/sign, while repeated
nonzero spectrum leaves only the block partial isometry without extra structure.

**Autoresearch next step**

terminal: UV-012 is closed at the level requested by the ground-truth check,
subject to adversarial verification of the negative closure wording before paper
promotion.
