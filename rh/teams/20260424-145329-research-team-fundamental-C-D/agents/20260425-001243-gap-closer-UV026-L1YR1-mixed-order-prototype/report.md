# Claim

The homogeneous mixed-order candidate cannot supply the intended
\(L_1YR_1\) grade-five mixed input.  With
\[
\operatorname{Gr}_1r=\frac{r^{(3)}(m)}{3!}(t-m)^3,
\qquad
\operatorname{Gr}_5r=\frac{r^{(7)}(m)}{7!}(t-m)^7,
\]
the same-point inputs have the expected orders \(1\) and \(5\), but the mixed
input does not: the odd source pieces \(r^{(3)}\) and \(r^{(7)}\) first
contribute to \(M=\mathfrak D_Q\delta N^{\lin}\) in orders \(2\) and \(6\),
respectively, because the leading \((2,2)\) mixed channel cancels under
\(t_+\leftrightarrow t_-\).  Hence \([z^5]M^{[5]}=0\) for the pure
\(r^{(7)}\) candidate, and the \(L_1YR_1\) \([z^7]\) convolution is zero for
this prototype for the wrong reason: the proposed \(M_i^{[5]}\) table is absent
at order \(5\).  The blocker is exact mixed-block parity, not full baseline
\(q_0\) specialization.

# Status

computational

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The pre-\(\Phi_K\) source variables are
\[
d_\pm=r(t_\pm),\qquad e_\pm=r'(t_\pm),\qquad g_\pm=r''(t_\pm),\qquad
\eta=\int_{t_+}^{t_-}r(u)\,du,
\]
with \(t_\pm=m\pm z/(2Q^2)\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2627`.

**Proved from source.**  The same-point source-linear block has a direct
\(g=r''\) channel in the \((2,2)\) entry:
\[
\delta G_{22}^{\lin}\sim g+\text{baseline}\cdot d.
\]
Thus a scalar Taylor derivative of order \(k\) first appears in
\(\delta G^{\lin}\) at order \(z^{k-2}\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722`.

**Proved from source.**  The mixed source-linear \((2,2)\) channel is obtained
from
\[
\partial_{q_-}F_0\,d_-+\partial_{q_+}F_0\,d_+
+\partial_\Delta F_0\,\eta
\]
divided by \(s^3\), while off-diagonal entries have \(d_\pm/s\)-type channels.
Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787`.

**Proved source parity.**  For a pure scalar Taylor monomial of odd order \(k\),
\(\eta=0\) and \(d_-+d_+=0\).  Therefore the apparent \(M_{22}\) order
\(k-2\) channel cancels in the mixed block.  The first mixed contribution is
then the off-diagonal \(d/s\) channel at order \(k-1\).  For even \(k\), the
\(M_{22}\) channel survives at order \(k-2\).

**Computational prototype.**  I wrote and ran
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/scripts/l1yr1_mixed_order_prototype.py`
before making the prototype claim.  Script SHA1:
`30D20BF8EAAEFE99DA377FD399C5FFA6F6B7934D`.  Output manifest:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/notes/l1yr1_mixed_order_prototype.json`,
SHA1 `AC9BFE7386AF58FCD09E0462F18497FAC682FE42`.

Relevant output:

```text
"grade1": {
  "source": "r^(3)(m) only",
  "same_point_deltaG_order": 1,
  "mixed_M_order": 2,
  "compatible": false
}
"grade5": {
  "source": "r^(7)(m) only",
  "same_point_deltaG_order": 5,
  "mixed_M_order": 6,
  "M_z5": "zero by odd plus/minus cancellation",
  "compatible": false
}
"hard_blocker": "exact mixed-block parity: odd k=a+2 pieces miss odd mixed grades"
```

**Consequence for \(L_1YR_1\).**  In the \(L_1YR_1\) product,
\(\Lambda^{[1]}\) from pure \(r^{(3)}\) begins in order \(z^1\).  To contribute
to \([z^7]\), the middle factor must have \([z^5]M^{[5]}\).  The pure
\(r^{(7)}\) grade-five candidate has \([z^5]M=0\), so this prototype gives
\[
[z^7]\Lambda^{[1]}M^{[5]}\Lambda^{[1]}=0
\]
before any determinant or quotient argument.  This is not a proof of the
UV-026 gauge identity; it shows the homogeneous convention fails to populate
the intended order-seven \(L_1YR_1\) gate.

**Conditional.**  If a future theorem declares that \(M_i^{[5]}\) may start in
order \(6\), then the \(L_1YR_1\) family contributes nothing at \(B_7\) under
this homogeneous convention.  That would be a new source-grade theorem and
must explain why the existing UV-026 wording still calls the middle input
grade \(5\).

**Missing.**  No baseline inverse-square-root Frechet tables were computed,
because they are not the first blocker for this prototype.  Once a nonzero
\([z^5]M_i^{[5]}\) convention exists, the leading \(\Lambda\)-coefficients
will still require the baseline constant block
\[
G_0(0)=\pi^{-1}
\begin{pmatrix}
2q_0(m)&q_0'(m)/2\\
q_0'(m)/2&(q_0''(m)+2q_0(m)^3)/12
\end{pmatrix}
\]
and its inverse-square-root Frechet operator.

# Baseline / delta

Baseline: the mixed-order filtration report proposed the homogeneous Taylor
projection \(k=a+2\), and found formal order compatibility before accounting
for the exact plus/minus cancellation in the mixed block.  The accepted Stage 1
generator remains infrastructure: it assumes the finite-grade source split and
actual scalar inputs.

Delta: this pass instantiates the homogeneous candidate for \(L_1YR_1\) and
finds a sharper obstruction.  Odd homogeneous scalar pieces do not provide odd
mixed orders.  Therefore the candidate grade \(1=r^{(3)}\) and
grade \(5=r^{(7)}\) cannot simultaneously supply the same-point and mixed
tables required by the \(1/5/1\) gate.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - current UV-026 frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 source-table and source-jet subtargets.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/report.md`
  - mixed-order filtration candidate.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/report.md`
  - accepted Stage 1 generator infrastructure.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/report.md`
  - \(42\)-scalar generator schema.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2899` - source variables,
  exact same-point/mixed formulas, tagged source block, and scope guard.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - \(L_1YR_1\)
  coefficient gate and missing lists.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/notes/L1YR1-mixed-order-prototype-verdict.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/scripts/l1yr1_mixed_order_prototype.py`.
- Current commit named in prompt: `7b3dfb7 capture UV-026 mixed-order filtration`.

# Dependencies

- UV-026 Stage 0 normalization: ordinary \(z\), source tags retained,
  pre-\(\Phi_K\), and \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta
  N_i^{\lin})\).
- A corrected scalar grade theorem that accounts for mixed-block parity.
- Baseline \(q_0(m),q_0'(m),q_0''(m)\) and the inverse-square-root Frechet
  operator once a nonzero \([z^5]M^{[5]}\) convention exists.

# Strongest objection

The vanishing of the \(L_1YR_1\) prototype is not a determinant-gauge proof.
It follows because the proposed homogeneous \(M^{[5]}\) has no \([z^5]\)
coefficient.  Treating that as UV-026 progress without changing the source
grade theorem would launder an absent input into a proved gauge identity.

# Needed for promotion

One of the following must be supplied:

1. A revised scalar grade convention that gives a nonzero
   \([z^5]M_i^{[5]}\) while remaining compatible with the same-point
   \(\delta G_{i,\pm}^{\lin,[1]}\) inputs.
2. A theorem that \(M_i^{[5]}\) is allowed to start at \(z^6\) under the
   homogeneous convention, so \(L_1YR_1\) is absent from \(B_7\), plus a
   correction of the seven-family inventory accordingly.
3. A proof that non-homogeneous combinations of source derivatives define
   \(\operatorname{Gr}_5 r_i\) and produce the intended \([z^5]\) mixed table.

After that, compute the leading \(\Lambda\) coefficients from the baseline
constant block and resume the fixed-sector \(B_7^{\mathfrak f}\) tests.

# Autoresearch next step

continue: attack the parity-corrected scalar grade theorem.  Determine whether
source-linear mixed inputs have only even ordinary-\(z\) orders in general, and
whether UV-026's \(M_i^{[5]}\) must therefore be reinterpreted as a source
label rather than an actual mixed order.

# Ledger destination

`findings.md`, `uv.md`, and `attempts.md`: record as `keep`.  This is a
source/formula obstruction to the homogeneous mixed-order prototype and a
smaller blocker for \(L_1YR_1\): exact mixed parity kills
\([z^5]M^{[5]}\) for the \(r^{(7)}\) candidate before baseline specialization.
