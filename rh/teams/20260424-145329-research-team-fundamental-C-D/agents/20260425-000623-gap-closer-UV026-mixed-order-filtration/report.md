# Claim

The candidate mixed-order scalar filtration is formally compatible with both
the scaled mixed input and the same-point Frechet inputs at the level of
ordinary-\(z\) order bookkeeping.  If one defines
\[
\operatorname{Gr}_a r(t)
=
\frac{r^{(a+2)}(m)}{(a+2)!}(t-m)^{a+2},
\qquad a\in\{1,5\},
\]
then \(\operatorname{Gr}_1 r\) is the \(r^{(3)}(m)\) monomial and
\(\operatorname{Gr}_5 r\) is the \(r^{(7)}(m)\) monomial.  For every scalar
Taylor derivative order \(k\ge2\), the displayed same-point input
\(\delta G^{\lin}\) and scaled mixed input
\(M=\mathfrak D_Q\delta N^{\lin}\) both first see that derivative in finite
order \(k-2\).  Thus this candidate can supply
\(\delta G_{i,\pm}^{\lin,[1/5]}\) and \(M_i^{[1/5]}\) consistently as a
theorem candidate.

It is not proved by current source.  Its main obstruction is that grade \(1\)
becomes \(r^{(3)}(m)\), not the existing \(\eta_2/X_1\) witness slice from the
quadratic source term \(r^{(2)}(m)\).  Therefore promotion requires a new
theorem declaring that UV-026 finite grade means pre-whitening matrix order,
not witness-slice labels, and explaining the grade-\(0\) \(r^{(2)}\) sector.

# Status

computational

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The current source defines the affine-removed
one-pair source remainder \(r_\rho\), then
\[
d_\pm=r_\rho(t_\pm),\qquad e_\pm=r_\rho'(t_\pm),\qquad
g_\pm=r_\rho''(t_\pm),\qquad
\eta=\int_{t_+}^{t_-}r_\rho(u)\,du
\]
with \(t_\pm=m\pm z/(2Q^2)\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2627`.

**Proved from source.**  The same-point linear input has entries linear in
\(d,e,g\):
\[
\delta G_{11}\sim d,\qquad
\delta G_{12}\sim e,\qquad
\delta G_{22}\sim g+\text{baseline}\cdot d.
\]
This follows from the displayed same-point formula and the subtraction
\(q=q_0+d\), \(q'=q_0'+e\), \(q''=q_0''+g\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722`.

**Proved from source.**  The mixed input has \(s^{-1},s^{-2},s^{-3}\)
denominators, and its linearized \((2,2)\) numerator contains
\(\partial_{q_-}F_0d_-+\partial_{q_+}F_0d_++\partial_\Delta F_0\eta\) before
division by \(s^3\).  Thus \(d/s^2\) and \(\eta/s^3\) are the lowest-order
linear channels.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787`.

**Proved from source boundary.**  UV-026 needs the pre-\(\Phi_K\) coefficient
lists \([z^r]\Lambda_{i,\pm}\) and \([z^s]M_i^{[5]}\) for the finite grade
\(1/5/1\) gate.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`.

**Computational/order audit.**  I wrote and ran
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/scripts/mixed_same_order_compatibility.py`
before citing its output.  Script SHA1:
`A231F8B468773642902DECB6D40BDB5EECA0E22E`.  Output manifest:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/notes/mixed_same_order_compatibility.json`,
SHA1 `F6591B5DD0383575F3F6DE1165A654CF30A2829B`.

Relevant output:

```text
"candidate_projection": "Gr_1 r keeps r^(3)(m)*(t-m)^3/3!"
"lowest_deltaG_order": 1
"lowest_M_order": 1
"candidate_projection": "Gr_5 r keeps r^(7)(m)*(t-m)^7/7!"
"lowest_deltaG_order": 5
"lowest_M_order": 5
"all_rows_order_compatible": true
```

**Conditional theorem candidate.**  If UV-026 finite grade means lowest
ordinary-\(z\) order in the pre-whitening source-linear matrix inputs, then
\(\operatorname{Gr}_a r\) may be defined as the homogeneous Taylor projection
with derivative order \(k=a+2\).  Under that convention, the same scalar piece
feeds both
\[
\delta G_{i,\pm}^{\lin,[a]}
\]
and
\[
M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})
\]
with matching leading order \(a\).

**Missing from current source alone.**  Current source does not state this
filtration.  Harvey's grade-convention audit correctly warns that
\(\eta_2/X_1\), \(q^{(5)}/X_3\), and \(q^{(7)}/X_5\) are matrix witness labels,
not scalar source projections.  The mixed-order candidate avoids importing
those labels, but it still needs a theorem saying UV-026 uses this
pre-whitening order grading.

**Obstruction.**  The candidate puts the quadratic source slice
\(r^{(2)}(m)\) in grade \(0\), because it first contributes to both
\(\delta G\) and \(M\) in order \(0\).  The existing \(\eta_2/X_1\) witness is
quadratic-source driven, so the candidate grade \(1\) is not the witness
\(\eta_2\) slice.  A valid theorem must either exclude grade \(0\) from the
\((1,1,5)\) UV-026 gates or explain where those terms were already handled.

# Baseline / delta

Baseline: the scalar-grade report rejected \(q^{(5)}/X_3\) as a grade-five
mixed input if grade means finite mixed order, and identified \(q^{(7)}/X_5\)
as the only source-compatible grade-five witness candidate.  Harvey's
grade-convention audit rejected importing any witness slice as a scalar
\(\operatorname{Gr}_1/\operatorname{Gr}_5\) definition from current source.

Delta: this pass tests a different convention: exact mixed-order Taylor
projection \(k=a+2\).  It gives a usable theorem candidate and proves
order-level compatibility with same-point \(\delta G\), not only with mixed
\(M\).  The remaining blocker is narrowed to convention/promotion statements:
declare this grading, handle grade \(0\), and then run the Stage 1 and Frechet
tables.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - read completely before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 source-table and source-jet subtargets.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-gap-closer-UV026-scalar-grade-projection/report.md`
  - scalar-grade reduction and \(q^{(5)}\)/\(X_3\) rejection.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-verifier-source-UV026-grade-convention/report.md`
  - Harvey's grade-convention guardrail.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-verifier-source-UV026-grade-convention/notes/grade-convention-guardrails.md`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2899` - source remainders,
  same-point/mixed formulas, tagged source block, and scope guard.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - UV-026
  \(L_1YR_1\) gate and missing coefficient lists.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/notes/mixed-order-filtration-theorem-candidate.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/scripts/mixed_same_order_compatibility.py`.
- Current commit named in prompt: `2e29dc0 capture UV-026 scalar grade reduction`.

# Dependencies

- UV-026 Stage 0 normalization: ordinary \(z\), tags retained,
  pre-\(\Phi_K\), and \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta
  N_i^{\lin})\).
- A convention that finite source grade means lowest pre-whitening
  ordinary-\(z\) matrix order.
- The Stage 1 generator and downstream \(S^2=G\), \(BS=I\) Frechet algebra.
- A separate handling or exclusion of grade-\(0\) \(r^{(2)}(m)\) contributions.

# Strongest objection

The candidate is only an order-compatible filtration, not a source theorem.
It deliberately diverges from the existing \(\eta_2/X_1\) witness by assigning
the quadratic source term to grade \(0\), while UV-026's prose does not yet
state that grade \(0\) is outside the \((1,1,5)\) families.  If the intended
grade \(1\) was the witness \(\eta_2\) slice, this candidate is the wrong
filtration.

# Needed for promotion

Promote this route only after proving the following finite source-grade
theorem:

1. For UV-026, finite grade \(a\) is lowest ordinary-\(z\) order of the
   pre-whitening source-linear matrix inputs \(\delta G^{\lin}\) and
   \(\mathfrak D_Q\delta N^{\lin}\).
2. For \(a\in\{1,5\}\),
   \[
   \operatorname{Gr}_a r(t)=r^{(a+2)}(m)(t-m)^{a+2}/(a+2)!.
   \]
3. This projection is defined after midpoint affine removal, so
   \((\operatorname{Gr}_a r)(m)=(\operatorname{Gr}_a r)'(m)=0\).
4. The grade-\(0\) \(r^{(2)}(m)\) terms are not part of the UV-026
   \((1,1,5)\) gates, or their contribution is already killed/handled by a
   separate source theorem.
5. With all other \((r_i^{[1/5]})^{(k)}(m)\) set to zero except
   \(k=3\) for grade \(1\) and \(k=7\) for grade \(5\), run the Stage 1
   generator, derive the Frechet tables, and check all seven determinant
   identities.

# Autoresearch next step

continue: instantiate the Stage 1 generator with this homogeneous
mixed-order candidate, using symbolic placeholders for \(r_i^{(3)}(m)\) and
\(r_i^{(7)}(m)\).  The first concrete check is whether the resulting
\(L_1YR_1\) and \(L_2YR_0/L_0YR_2\) tables are small enough to compute
fixed-sector \(B_7^{\mathfrak f}\) vectors before full baseline \(q_0\)
specialization.

# Ledger destination

`uv.md`, `attempts.md`, and `collation.md`: record as `keep`.  This gives a
precise theorem candidate and a compatibility list for the mixed-order scalar
filtration, while keeping UV-026 open on grade-\(0\) handling and actual
determinant tests.
