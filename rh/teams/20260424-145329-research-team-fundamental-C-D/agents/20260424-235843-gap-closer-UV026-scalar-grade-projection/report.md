# Claim

From the inspected current source alone, the witness-region matrix slices do
not define scalar projections \(r_i\mapsto r_i^{[1]},r_i^{[5]}\) on the
affine-removed pre-whitening source remainder.  A tempting convention is
nevertheless rejectable: UV-026 grade \(5\) for the middle mixed input
\[
M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})
\]
should not be read as the \(q^{(5)}/X_3\) quintic witness slice.  Source text
places \(q^{(5)}\) in finite degree \(3\), while \(q^{(7)}\) is the source
candidate matching finite degree \(5\).  Thus the only witness-compatible
candidate for a grade-five scalar source slice is the \(q^{(7)}/X_5\) direct
septic slice, but promoting that candidate to a scalar pre-\(\Phi_K\)
projection is still a missing theorem.

# Status

open

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The UV-026 target itself is pre-\(\Phi_K\) and
pre-determinant, and defines the middle input as a grade-five mixed object:
\[
M_i^{[5]}(z)=\sum_s M_{i,s}^{[5]}z^s.
\]
It says the coefficient lists remain missing.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`.

**Proved from source.**  The quintic witness slice is explicitly
\((K_1,\eta_2,q^{(5)})\), but the proof says the factor \(q^{(5)}(h)\) first
appears in the cubic same-point coefficient \(G_3\), and the corresponding
linear contribution is to \(X_3\), diagonal.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:6535-6654`.  The later reuse of the
same tagged slice says the monomial \(\kappa\eta_2q^{(5)}\) occurs in \(u_5\),
not \(v_5\) or \(c\); source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:13334-13375`.

**Proved from source.**  The direct septic witness slice is
\((K_1,\eta_2,q^{(7)})\).  The proof says \(q^{(7)}(h)\) first appears only in
the quintic same-point coefficient \(G_5\), and its linear contribution to
\(X_5\) is diagonal.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:7656-7842`.

**Proved from source.**  The tagged-slice computation around the centered
quintic witness again identifies the \(\eta_2\) input as an off-diagonal
contribution and the \(q^{(5)}\) input as a diagonal-difference contribution,
but it remains a matrix-channel statement about \(v_0\) and
\(\gamma-\alpha\), not a scalar projection on \(r\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:23850-23895`.

**Computational/order audit.**  I wrote and ran
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-gap-closer-UV026-scalar-grade-projection/scripts/mixed_grade_order_audit.py`
before citing its output.  Script SHA1:
`A8A2F96C09AD3FABFDF48FCF09895E699AB3B6B8`.  Output manifest:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-gap-closer-UV026-scalar-grade-projection/notes/mixed_grade_order_audit.json`,
SHA1 `C904556906B31D66E3654BC6E110F5AF41765883`.

The script records the order shift forced by the displayed mixed-block
denominators: a scalar source derivative of order \(k\) can first enter the
scaled mixed input \(M=\mathfrak D_Q\delta N\) in order \(z^{k-2}\) through the
\((2,2)\)-entry.  Relevant output:

```text
"k_to_lowest_M_order": {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7}
"q^(5)_lowest_M_order": 3
"q^(7)_lowest_M_order": 5
"grade_5_if_grade_means_lowest_M_z_order": "q^(7), not q^(5)"
```

**Scoped rejection.**  Therefore, if UV-026's \(M_i^{[5]}\) grade is the
finite mixed order that the Stage 1 generator needs, \(q^{(5)}/X_3\) is the
wrong scalar candidate: it is degree \(3\), not \(5\).  This also fits the
paper's use of \(q^{(5)}\) as the quintic \(A_5^{\mathfrak f}\) witness rather
than the middle grade-five input for an order-seven cubic family.

**Conditional.**  The \(q^{(7)}/X_5\) slice is the only source-supported
witness candidate matching finite degree \(5\).  But current source proves
this only as a same-point/inverse-square-root matrix slice in the direct septic
\(K_1\) witness.  It does not define \(r_i^{[5]}\), does not state
\(\operatorname{Gr}_5 r_i\), and does not prove compatibility with
\(M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})\).

**Missing from current source alone.**  There is no scalar filtration
\(\operatorname{Gr}_a\) on affine-removed source germs \(r_i\).  The tagged
pre-whitening block has \(\mathcal K\)-degree one for every pair kernel at
`C:/workspace/riemann2/rh/proof_of_rh.tex:2797-2899`; it does not refine the
source into grades \(1\) and \(5\).  The generator verifier accepts the Stage 1
script only as infrastructure and keeps the finite-grade split as an input
assumption, not as a proved source theorem; see
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/report.md`.

# Baseline / delta

Baseline: the source-jet split report reduced the Stage 1 generator's missing
input to a scalar grade-projection theorem plus baseline \(q_0\) jets.  It left
open whether grade \(5\) meant the \(q^{(5)}/X_3\) quintic slice, the
\(q^{(7)}/X_5\) direct septic slice, or a separate mixed-block grading.

Delta: this pass rejects the \(q^{(5)}/X_3\) convention for \(M_i^{[5]}\) and
identifies \(q^{(7)}/X_5\) as the only witness-compatible grade-five candidate.
It also proves that this still does not define scalar \(r_i^{[5]}\): the
witness slices are matrix-channel facts after whitening/parity, while UV-026
needs a pre-\(\Phi_K\) scalar/mixed projection.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - read completely before acting; UV-026 frontier says the scalar
  `Gr_1/Gr_5` projection remains missing.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 source-jet subtarget and current grade-projection ambiguity.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-gap-closer-UV026-source-jet-split/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-verifier-source-UV026-stage1-normalization/report.md`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6535-6654` -
  \(q^{(5)}\) first appears in \(G_3\), producing diagonal \(X_3\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7656-7842` -
  \(q^{(7)}\) first appears in \(G_5\), producing diagonal \(X_5\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` -
  UV-026 \(L_1YR_1\), \(M_i^{[5]}\), and missing coefficient lists.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:13334-13375` -
  \(q^{(5)}\) as a quintic \(A_5^{\mathfrak f}\) witness.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:23850-23895` -
  tagged \(\eta_2/q^{(5)}\) matrix-channel witness.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-gap-closer-UV026-scalar-grade-projection/notes/scalar-grade-projection-audit.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-gap-closer-UV026-scalar-grade-projection/scripts/mixed_grade_order_audit.py`.

# Dependencies

- UV-026 Stage 0 normalization: ordinary \(z\), tags retained, pre-\(\Phi_K\),
  and \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\).
- The source formulas for the mixed block and same-point block.
- The Stage 1 generator and verifier, which accept the source formula
  infrastructure but require the grade split as input.
- A new scalar grade-projection theorem defining \(\operatorname{Gr}_1\) and
  \(\operatorname{Gr}_5\) before table generation.

# Strongest objection

The \(q^{(7)}/X_5\) identification is still not a proof of \(r_i^{[5]}\).  It is
a degree calibration from source and the mixed-block order audit.  The witness
proofs live after matrix coefficient extraction and inverse-square-root parity;
they do not define a source-level projection, do not prove compatibility with
affine removal, and do not specify what \(r_i^{[1]}\) should be.

# Needed for promotion

The scalar grade-projection theorem must supply all of the following:

1. A source-level filtration/projection \(\operatorname{Gr}_a\) on
   affine-removed scalar germs \(r_i\), before \(\Phi_K\), with source tags
   retained.
2. A calibration statement rejecting \(q^{(5)}/X_3\) as grade \(5\) and either
   identifying grade \(5\) with the \(q^{(7)}/X_5\)-compatible source slice or
   defining a distinct mixed-block grade with its exact relation to the
   \(s^{-1},s^{-2},s^{-3}\) order shifts.
3. Compatibility with affine removal:
   \((\operatorname{Gr}_a r_i)(m)=(\operatorname{Gr}_a r_i)'(m)=0\).
4. Compatibility with the pre-whitening formulas:
   \[
   \operatorname{Gr}_a(\mathfrak D_Q\delta G_{i,\pm}^{\lin})
   =\mathfrak D_Q\delta G_{i,\pm}^{\lin}[\operatorname{Gr}_a r_i],
   \]
   and
   \[
   \operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})
   =\mathfrak D_Q\delta N_i^{\lin}[\operatorname{Gr}_a r_i].
   \]
5. The derivative data or vanishing relations for
   \((r_i^{[1]})^{(k)}(m)\) and \((r_i^{[5]})^{(k)}(m)\), \(2\le k\le9\), so
   the accepted Stage 1 generator can be run on actual inputs.

# Autoresearch next step

continue: formulate and test a candidate scalar filtration.  The most
source-compatible candidate is a mixed-order filtration in which a scalar
derivative \(r^{(k)}(m)\) first contributes to \(M\) in order \(k-2\), so
grade \(5\) starts at \(r^{(7)}(m)\).  The next task is to decide whether this
same filtration can also define \(r_i^{[1]}\) consistently with the
same-point/inverse-square-root \(L_1,R_1\) inputs.

# Ledger destination

`findings.md`, `uv.md`, and `attempts.md`: record as `keep`.  This is a
source-based scoped rejection of the \(q^{(5)}/X_3\) grade-five convention and
a sharper UV-026 subtarget: prove the scalar/mixed grade-projection theorem,
with \(q^{(7)}/X_5\) as the only currently source-compatible grade-five
candidate.
