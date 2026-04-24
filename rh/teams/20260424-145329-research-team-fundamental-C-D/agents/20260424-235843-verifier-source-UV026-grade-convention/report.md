# Claim

Current source does not justify identifying the UV-026 scalar
\(\operatorname{Gr}_5 r_i\) with either the \(q^{(5)}\)/\(X_3\) quintic slice or
the \(q^{(7)}\)/\(X_5\) direct septic slice.  Both labels are source-supported
matrix-slice facts inside one-pair witness computations, but neither is defined
as a scalar grade projection on the affine-removed source remainder \(r_i\)
before \(\Phi_K\) and in the \(B_7^{\mathfrak f}\) normalization.

Current source also does not justify identifying scalar \(\operatorname{Gr}_1
r_i\) with the \(\eta_2\)/\(X_1\) off-diagonal slice before whitening.  The
source supports \(\eta_2\) as an off-diagonal \(X_1\) witness input, but that is
not yet a scalar \(\operatorname{Gr}_1\) theorem for the source remainder.

Source verdict: reject shortcut imports of \(\eta_2\), \(q^{(5)}\), or
\(q^{(7)}\) matrix witness slices as definitions of scalar
\(\operatorname{Gr}_1/\operatorname{Gr}_5\).  The precise missing theorem is a
scalar grade-projection theorem defining \(\operatorname{Gr}_1\) and
\(\operatorname{Gr}_5\) on \(r_i\), compatible with affine removal,
\(\mathfrak D_Q\), the Stage 1 generator, and
\[
B_7^{\mathfrak f}=\pi_{\mathfrak f}[z^7].
\]

# Status

open

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The quintic witness section isolates the graded slice
\((K_1,\eta_2,q^{(5)})\).  It says \(q^{(5)}\) first appears in the cubic
same-point coefficient \(G_3\), and the linear \(q^{(5)}\) contribution to
\(X_3\) is diagonal.  It also says the \(\eta_2\) slice of \(X_1\) is
off-diagonal.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:6535-6654`.

**Proved from source.**  The direct septic section isolates
\((K_1,\eta_2,q^{(7)})\).  It says \(q^{(7)}\) first appears in the quintic
same-point coefficient \(G_5\), the linear \(q^{(7)}\) contribution to \(X_5\)
is diagonal, and the mixed \((\eta_2,q^{(7)})\) slice of \(X_6\) is
off-diagonal.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:7656-7842`.

**Proved from source.**  A later fixed-sector argument again uses the
\((K_1,\eta_2,q^{(5)})\) witness: the tagged monomial contributes to \(u_5\),
not \(c\) or \(v_5\), and the proof relies on the \(\eta_2\)-input in \(X_1\)
being off-diagonal while the \(q^{(5)}\)-input in \(X_3\) is diagonal.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:13334-13375`.

**Proved from source.**  The source also reuses the explicit two-direction
computation: \(U_{12}\) is the tagged \(\eta_2\)-contribution to the
off-diagonal channel, and \(V_{22}\) is the tagged \(q^{(5)}\)-contribution to
the diagonal-difference channel.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:23850-23895`.

**Proved from source boundary.**  UV-026 is explicitly pre-\(\Phi_K\),
pre-determinant, and pre-diagonal-merger.  It defines
\[
B_7^{\mathfrak f}(T):=\pi_{\mathfrak f}[z^7]T
\]
and says the coefficient lists for \(\Lambda_{i,\pm}\) and \(M_i^{[5]}\)
remain missing.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`.

**Proved from current UV/report state.**  The current UV-026 entry says the
immediate source-jet subtarget is still to define the finite-grade split
\(r_i=r_i^{[1]}+r_i^{[5]}+\cdots\), and it explicitly asks whether grade \(5\)
means the \(q^{(5)}\)/\(X_3\), \(q^{(7)}\)/\(X_5\), or another mixed-block
slice.  The source-jet split report likewise concludes that the ungraded
one-pair derivative formula is source-supported while the scalar
grade-projection theorem is missing.

**Conditional.**  If the intended grade convention is matrix input order, then
the inspected source points toward \(\eta_2/X_1\) for grade \(1\) and
\(q^{(7)}/X_5\) for grade \(5\).  If the intended grade convention is the
quintic output witness, then \(q^{(5)}/X_3\) is the plausible grade-five
candidate.  Current source does not state which convention UV-026 uses for the
scalar \(M_i^{[5]}\) input.

**Missing.**  No inspected source defines \(\operatorname{Gr}_1\) or
\(\operatorname{Gr}_5\) on the scalar affine-removed source remainder \(r_i\).
No inspected source proves that those scalar projections commute with affine
removal or are defined after affine removal.

**Missing.**  No inspected source proves that a scalar
\(\operatorname{Gr}_5 r_i\), whether \(q^{(5)}\)-driven or \(q^{(7)}\)-driven,
produces the mixed input \(M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta
N_i^{\lin})\) used by the Stage 1 generator and UV-026 gates.

**Missing.**  No inspected source proves that the witness matrix slices can be
imported backward as scalar source projections before whitening.  Matrix
witnesses may motivate a convention; they are not source definitions in the
\(B_7^{\mathfrak f}\) normalization.

No computational claim is made in this audit; no script was needed.

Guardrails are deposited at
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-verifier-source-UV026-grade-convention/notes/grade-convention-guardrails.md`.

# Baseline / delta

Baseline: the Stage 1 generator is verified only as infrastructure.  The
current UV-026 ledger has sharpened the immediate blocker to the scalar
source-jet split: define \(r_i^{[1]}\), \(r_i^{[5]}\), and supply the \(42\)
source derivatives.  The latest source-jet split report sources the ungraded
one-pair derivative formula but leaves the scalar grade projection open.

Delta: this audit rejects both candidate grade-five identifications from
current source alone.  It separates three facts that were easy to blur:
\(\eta_2/X_1\), \(q^{(5)}/X_3\), and \(q^{(7)}/X_5\) are matrix-slice facts in
witness computations; none is yet a scalar \(\operatorname{Gr}_1\) or
\(\operatorname{Gr}_5\) theorem for UV-026.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/skills/research-resume/SKILL.md` - read
  because this is a resumed UV-026 research lane.
- `C:/workspace/riemann2/.agents/agents/_autoresearch.md` - read before
  acting.
- Current repository head while auditing:
  `2fa6569 capture UV-026 source-jet split`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - read completely before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 immediate source-jet and grade-projection subtarget.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-gap-closer-UV026-source-jet-split/report.md`
  - current source-jet split report.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6535-6654` - quintic witness
  \((K_1,\eta_2,q^{(5)})\), \(q^{(5)}\)/\(X_3\), and \(\eta_2\)/\(X_1\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7656-7842` - direct septic
  \(q^{(7)}\)/\(X_5\) and \((\eta_2,q^{(7)})\)/\(X_6\) witness.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - UV-026
  pre-\(\Phi_K\) target and missing coefficient lists.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:13334-13375` - fixed-sector
  use of the \(q^{(5)}\) quintic witness.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:23850-23895` - repeated
  \(\eta_2\)/off-diagonal and \(q^{(5)}\)/diagonal witness computation.
- Own note:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-verifier-source-UV026-grade-convention/notes/grade-convention-guardrails.md`.

# Dependencies

- UV-026 Stage 0 normalization: ordinary \(z\), source tags retained,
  pre-\(\Phi_K\), and \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta
  N_i^{\lin})\).
- The Stage 1 generator and its \(42\)-scalar input schema.
- The ungraded rational one-pair source-jet formula from the source-jet split
  report.
- A new scalar grade-projection theorem for \(\operatorname{Gr}_1\) and
  \(\operatorname{Gr}_5\) on affine-removed \(r_i\).

# Strongest objection

The word "grade" is used in witness sections for matrix coefficient slices and
in UV-026 for source-table inputs, but the inspected source does not prove that
these are the same grading.  The \(q^{(5)}\)/\(X_3\) convention is natural for
the quintic \(A_5\) witness, while the \(q^{(7)}\)/\(X_5\) convention is natural
for same-point matrix input order \(5\).  Choosing either one without a scalar
projection theorem would silently import a post-source matrix witness into the
pre-whitening scalar source table.

# Needed for promotion

Add or cite a theorem with these exact contents:

1. Define \(\operatorname{Gr}_1\) and \(\operatorname{Gr}_5\) on the scalar
   affine-removed source remainder \(r_i\), before \(\Phi_K\), with source tags
   retained, and in the \(B_7^{\mathfrak f}\) normalization.
2. State whether \(\operatorname{Gr}_5 r_i\) is the \(q^{(5)}\)/\(X_3\)
   quintic slice, the \(q^{(7)}\)/\(X_5\) direct septic slice, or another
   mixed-block scalar slice.
3. Prove compatibility with
   \[
   M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})
   \]
   and with the same-point Frechet inputs
   \(\delta G_{i,\pm}^{\lin,[5]}\).
4. Prove the projection commutes with midpoint affine removal, or define it
   after affine removal.
5. Supply or derive \((r_i^{[a]})^{(k)}(m)\), \(a\in\{1,5\}\),
   \(2\le k\le9\), for the Stage 1 generator.

# Autoresearch next step

continue: attack the scalar grade-projection theorem directly.  The first
decision is a convention choice: matrix input order would point to
\(q^{(7)}\)/\(X_5\), while quintic-output grading would point to
\(q^{(5)}\)/\(X_3\).  Either choice needs a source theorem pulling the witness
slice back to scalar affine-removed \(r_i\)-jets and proving compatibility with
\(M_i^{[5]}\).

# Ledger destination

`findings.md`, `uv.md`, and `attempts.md`: record this route as `keep`.  It
adds a reusable negative guardrail against shortcut grade identifications and
sharpens UV-026's open source-jet blocker to the missing scalar
grade-projection theorem.
