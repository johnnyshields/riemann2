**Claim**

The gap report's linear-algebra core is correct and is strong enough to close
UV-012 under the UV's stated frame-comparison closure criterion. For a fixed
finite-dimensional subspace pair \(S_-,S_+\) with dimensions \(p,q\), every
orthonormal-frame comparison matrix for the canonical cross-contraction
\(C=\Pi_-|_{S_+}:S_+\to S_-\) is in the orbit
\[
A\mapsto L^*AR,\qquad L\in U(p),\ R\in U(q),
\]
and the \(U(p)\times U(q)\) orbit is classified by the singular values of
\(A\), with dimensions \(p,q\) fixed. The theorem should be promoted as a
negative closure for entrywise frame-comparison matrices from the subspace pair
alone, not as a claim that no matrix can ever be produced after adding
transport, dynamics, ordering, or frame-selecting structure.

**Status**

proved

**Evidence**

Proved. If \(U_-:\mathbb C^p\to S_-\) and
\(U_+:\mathbb C^q\to S_+\) are orthonormal frame isometries, then
\[
U_-^*CU_+=U_-^*\Pi_-U_+=U_-^*U_+.
\]
Thus \(A=U_-^*U_+\) is exactly the coordinate matrix of \(C\) in those two
frames. If \(\widetilde U_-=U_-L\) and \(\widetilde U_+=U_+R\), then
\[
\widetilde A=(U_-L)^*(U_+R)=L^*AR.
\]
Conversely, any two orthonormal frame isometries onto the same endpoint subspace
differ by a unique unitary, so these are exactly all frame changes.

Proved. Rectangular SVD gives complete orbit classification. For a \(p\times q\)
matrix, write \(m=\min(p,q)\) and use the rectangular diagonal normal form
\(\Sigma\) with entries \(\sigma_1\ge\cdots\ge\sigma_m\ge0\) on the first
\(m\) diagonal positions and all remaining rectangular entries zero. If
\(A=P_A\Sigma Q_A^*\) and \(B=P_B\Sigma Q_B^*\), then
\[
B=(P_BP_A^*)A(Q_AQ_B^*),
\]
so \(B=L^*AR\) after setting \(L=P_AP_B^*\), \(R=Q_AQ_B^*\). Rank deficiency
only means some of the \(m\) displayed singular values are zero. Unequal
dimensions add the forced rectangular zero rows or columns; if one records the
full spectra of \(C^*C\) on \(S_+\) or \(CC^*\) on \(S_-\), additional zeros
are padded to lengths \(q\) and \(p\), respectively. With the standard
principal-angle convention, the \(m\) values \(\sigma_i=\cos\theta_i\) give the
principal angles; extended conventions append the dimension-forced right-angle
directions.

Proved. A sorted diagonal SVD representative is a canonical normal form for the
orbit once \(p,q\) and the order convention are fixed. It is not a canonical
entrywise comparison matrix attached to the original subspaces, because producing
it requires choosing singular-vector frames. Its entries carry only
\((p,q)\) and the singular values, hence no content beyond the
principal-angle/projector-spectrum package.

Conditional. Extra frame-selecting data can produce matrices. Simple nonzero
spectrum gives matched principal directions up to phase/sign on the nonzero
sector, and hence a diagonal representative there. This is a conditional
frame-selection corollary, not a new invariant beyond the singular values and
polar partial isometry.

Missing. No residual mathematical substatement remains for UV-012 as phrased:
the supplied closure alternative asks for the biunitary orbit theorem, and that
theorem is correct. What remains is promotion wording that keeps the scope on
orthonormal-frame comparison matrices and on data determined by the fixed
subspace pair alone.

No scripts were needed; this verification is finite-dimensional linear algebra.

**Baseline / delta**

Baseline: the paper already states the canonical operator package
\(C,K_\pm,V\), simple-spectrum frame corollary, repeated-spectrum no-go, and
finite-dimensional completeness at
`quantum/paper/jet_gram_quantum_note.md:405-454`, while the open problem at
`quantum/paper/jet_gram_quantum_note.md:783-790` asks whether any
matrix-valued two-point object beyond projector/principal-angle data can be
canonical without extra frame selection.

Delta: I accept the primary gap report's algebra, including unequal-dimension
and rank-deficient cases, but narrow the promotion language. The result closes
UV-012 by proving finality for frame comparison matrices. It does not license an
unqualified statement about every possible future matrix object if additional
structure is added.

**Attempt status**

terminal

**Exact refs**

- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183451-gap-biunitary-matrix-finality/report.md` for the primary orbit theorem under verification.
- `quantum/paper/jet_gram_quantum_note.md:405-454` for the current
  cross-contraction, positive compression, polar partial isometry,
  simple-spectrum, repeated-spectrum, and finite-dimensional completeness
  package.
- `quantum/paper/jet_gram_quantum_note.md:783-790` for the open matrix-valued
  endpoint problem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md` for the
  current in-cycle operator-package frontier and missing matrix/frame theorem.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/notes/resume-readthrough-20260424.md` for the stated missing biunitary classification target.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/collation.md` for the
  provisional keep verdict on the gap report.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-030000-attack-operator-package/reports/gap-operator-package.md` for the operator-package synthesis.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-023315-attack-degenerate-nogo/reports/gap-degenerate-nogo.md` for the repeated nonzero block no-go.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-024917-attack-frame-criterion/reports/gap-frame-criterion.md` for the simple-spectrum iff frame criterion.
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-054845-attack-cs-normal-form/reports/gap-cs-normal-form.md` for finite-dimensional CS completeness.

**Dependencies**

Finite-dimensional Hilbert-space subspaces; orthogonal projectors
\(\Pi_\pm\); orthonormal frame isometries for \(S_\pm\); standard rectangular
SVD over \(\mathbb C\); standard principal-angle conventions; the naturality
requirement that "canonical from the subspace pair alone" be invariant under
unitary changes of endpoint frames and under automorphisms preserving the pair.

**Strongest objection**

The phrase "no canonical matrix-valued two-point object" is too broad unless it
is tied to the fixed subspace pair and to orthonormal-frame representations of
the canonical cross-contraction. A future construction with extra dynamical,
transport, ordering, or symmetry-breaking data is outside this theorem's scope.
This objection affects wording only; it does not affect the biunitary orbit
classification or the UV-012 closure criterion as supplied in the brief.

**Needed for promotion**

Promote a theorem in this form:

> Let \(S_-,S_+\subset\mathcal H\) be finite-dimensional endpoint subspaces
> with dimensions \(p,q\), and let \(C=\Pi_-|_{S_+}:S_+\to S_-\). If
> \(U_-:\mathbb C^p\to S_-\) and \(U_+:\mathbb C^q\to S_+\) are orthonormal
> frame isometries, then \(A=U_-^*U_+\) is the matrix of \(C\) in these frames.
> Under all changes of endpoint orthonormal frames it transforms exactly as
> \(A\mapsto L^*AR\), with \(L\in U(p)\), \(R\in U(q)\). For fixed \(p,q\), this
> biunitary orbit is completely classified by the singular values of \(A\),
> equivalently by the principal-angle cosines, with the usual rectangular zero
> padding in the associated normal form. Therefore an entrywise comparison
> matrix is not canonical from the subspace pair alone; only its orbit, or an
> SVD normal form encoding the same singular values, is canonical without extra
> frame-selecting structure.

Add immediately after it:

> If the nonzero principal spectrum is simple, the polar package gives matched
> principal directions up to phase/sign and hence a conditional diagonal
> representative on that nonzero sector. Repeated nonzero principal values leave
> an internal \(U(m)\) freedom on each multiplicity-\(m\) block, so the canonical
> object there is the block partial isometry, not a frame. Zero singular sectors
> and dimension-forced rectangular padding do not select frames.

Avoid these wordings:

- "No matrix-valued two-point object can be canonical" without adding "as an
  orthonormal-frame comparison matrix determined by the subspace pair alone."
- "The diagonal SVD matrix is the canonical comparison matrix" without saying it
  is only an orbit normal form carrying the singular values.
- "Simple spectrum gives a canonical matrix" without the phase/sign and
  nonzero-sector qualifications.
- "Repeated spectrum is the only obstruction" unless zero singular sectors and
  unequal-dimension forced kernels are also excluded from frame canonicity.

**Autoresearch next step**

terminal: accept the gap report for promotion after the wording fixes above.
UV-012 need not remain open unless the coordinator wants to broaden it beyond
the supplied frame-comparison closure criterion.
