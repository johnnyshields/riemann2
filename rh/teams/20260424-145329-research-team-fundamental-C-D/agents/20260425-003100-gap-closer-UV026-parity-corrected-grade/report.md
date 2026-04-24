# Claim

The cleanest source-compatible convention is the common homogeneous scalar
grade
\[
\operatorname{Gr}_a r=
\frac{r^{(a+2)}(m)}{(a+2)!}(t-m)^{a+2}.
\]
It coexists with \(\Lambda^{[1]}\), but then \(M_i^{[5]}\) is induced by
\(r_i^{(7)}(m)\) and has no \([z^5]\) coefficient.  Hence the
\(L_1YR_1\) family is absent from \(B_7^{\mathfrak f}\) under this convention.

A nonzero parity-corrected \([z^5]M_i^{[5]}\) cannot be defined as the same
scalar grade: the exact mixed support is \(r_i^{(2)},r_i^{(4)},r_i^{(6)}\),
which are same-point scalar grades \(0,2,4\).  Such a convention is only
possible as a new block-dependent mixed-output projection theorem, not from
current source alone.  The next Y-containing gate affected by this convention
choice is \(L_2YR_0/L_0YR_2\).

# Status

computational

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The \(\mathfrak D_Q\)-scaled perturbation convention is
\(\delta N=\mathfrak D_Q^{-1}Y\) and \(Y_\rho=\mathfrak D_Q(\delta N_\rho)\).
Source: `C:/workspace/riemann2/rh/proof_of_rh.tex:2429-2466` and
`C:/workspace/riemann2/rh/proof_of_rh.tex:2653-2664`.

**Proved from source.**  The affine-removed scalar source remainder only
removes \(0\)- and \(1\)-jets:
\[
r_\rho(t)=f_\rho(t)-f_\rho(m)-f_\rho'(m)(t-m),
\]
and the same-point source-linear block contains \(g_\pm=r_\rho''(t_\pm)\) in
the \((2,2)\) entry.  Therefore \(r^{(k)}(m)\) first appears in
\(\delta G^{\lin}\) at ordinary \(z\)-order \(k-2\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2627` and
`C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2722`.

**Proved from source/prior audit.**  The exact mixed formulas give
\[
M(-z)=M(z)^T.
\]
The prior finite audit through \(z^7\) found that \([z^5]M\) is off-diagonal
antisymmetric and source-supported only by \(r^{(2)},r^{(4)},r^{(6)}\), not
\(r^{(7)}\).  Source formula:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787`; prior audit:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/report.md`.

**Computational compatibility test.**  I wrote and ran
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-gap-closer-UV026-parity-corrected-grade/scripts/parity_corrected_grade_test.py`
before making the convention claim.  Script SHA1:
`6C6560D7F02ACF0BC1A2FDCC7B2ECCFF4646270B`.  Output:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-gap-closer-UV026-parity-corrected-grade/notes/parity_corrected_grade_test.json`,
SHA1 `1E9F99AB5B5BB1E02C8E8C374860C293075002E7`.

Relevant output:

```text
"mixed_z5_sources_from_exact_parity_audit": ["r2", "r4", "r6"]
"lambda_grade_1_sources_under_common_scalar_grade": ["r3"]
"same_point_grade_5_sources_under_common_scalar_grade": ["r7"]
```

The same output records the conflict for a nonzero parity-corrected mixed
order-five definition:

```text
"r2": {"same_point_scalar_grade": 0, "requested_mixed_label": 5}
"r4": {"same_point_scalar_grade": 2, "requested_mixed_label": 5}
"r6": {"same_point_scalar_grade": 4, "requested_mixed_label": 5}
```

**Convention test.**

- If \([5]\) is a source-grade label for a single scalar split
  \(r=\sum_a r^{[a]}\), the coherent choice is homogeneous:
  \(r^{[1]}\leftrightarrow r^{(3)}(m)\) and
  \(r^{[5]}\leftrightarrow r^{(7)}(m)\).  Then
  \([z^5]M^{[5]}=0\).
- If \([5]\) is actual ordinary-\(z\) mixed order \(5\), then \(M^{[5]}\) is
  nonzero but uses \(r^{(2)},r^{(4)},r^{(6)}\).  This is not the same scalar
  source-grade convention as \(\Lambda^{[1]}\).
- If \([5]\) is a parity-corrected non-homogeneous mixed projection, current
  source must add a new theorem proving that the \(r^{(2)},r^{(4)},r^{(6)}\)
  terms are allowed in the middle label \([5]\) without consuming or duplicating
  grade \(0,2,4\) sectors.

**Conditional theorem under homogeneous grade.**  If UV-026 keeps the common
homogeneous scalar grade, then
\[
[z^7]\bigl(\Lambda^{[1]}M^{[5]}\Lambda^{[1]}\bigr)=0
\]
for the \(L_1YR_1\) family, because the required middle coefficient
\([z^5]M^{[5]}\) is zero.  This is an absence theorem for the family at
\(B_7^{\mathfrak f}\), not a determinant-gauge identity.

**Missing.**  Current source does not prove the alternative block-dependent
projection theorem.  In particular, it does not explain why even derivatives
\(r^{(2)},r^{(4)},r^{(6)}\) may be relabeled as \(M^{[5]}\) while their
same-point appearances remain grades \(0,2,4\).

# Baseline / delta

Baseline: the mixed-parity report showed that \([z^5]M\) is possible, but only
from even source derivatives; the M5-language verifier warned that \(M_i^{[5]}\)
was still a conditional placeholder.

Delta: this pass tests the cleanest parity-corrected convention against the
same-point \(\Lambda^{[1]}\) requirement.  It rejects a nonzero
\([z^5]M^{[5]}\) as a common scalar grade from current source alone, and gives
the exact fallback theorem: homogeneous grade makes \(L_1YR_1\) absent at
\(B_7\).  The next affected gate is \(L_2YR_0/L_0YR_2\), since those are the
next Y-containing families needing the same mixed-input convention.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex:2429-2466` -
  \(\mathfrak D_Q\) scaling and \(Y\)-normalization.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2787` - scalar source
  variables, same-point \(g=r''\) channel, and exact mixed formulas.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2797-2899` - tagged pre-whitening
  source block and scope guard.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - \(L_1YR_1\)
  coefficient gate and missing \(\Lambda\)/\(M^{[5]}\) lists.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/report.md`
  and its script
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/scripts/mixed_parity_audit.py`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-verifier-source-UV026-M5-language/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-verifier-source-UV026-grade0-sector/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-gap-closer-UV026-parity-corrected-grade/notes/parity-corrected-grade-verdict.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-gap-closer-UV026-parity-corrected-grade/scripts/parity_corrected_grade_test.py`.

# Dependencies

- The prior mixed-parity finite audit, including the exact support
  \([z^5]M\leftarrow\{r^{(2)},r^{(4)},r^{(6)}\}\).
- The common scalar grade rule \(r^{(k)}\mapsto k-2\), derived from the
  same-point \(g=r''\) channel.
- A future theorem if the project wants a nonzero \(M^{[5]}\): it must define a
  block-dependent mixed-output grade and separately handle lower scalar grades
  \(0,2,4\).
- The \(L_2YR_0/L_0YR_2\) second-Frechet gate if \(L_1YR_1\) is removed under
  homogeneous grade.

# Strongest objection

The result depends on accepting a single scalar grade split as the intended
meaning of \(r_i=r_i^{[1]}+r_i^{[5]}+\cdots\).  A different theorem could
define \([5]\) separately for the mixed block as an output-order label.  But
that theorem is not in the current source, and it would have to explain why
the same \(r^{(2)},r^{(4)},r^{(6)}\) source data do not also belong to the
grade \(0,2,4\) same-point/Frechet sectors.

# Needed for promotion

Promote one of two mutually exclusive statements:

1. **Homogeneous absence theorem.**  Define the scalar grade by
   \(\operatorname{Gr}_a r=r^{(a+2)}(m)(t-m)^{a+2}/(a+2)!\).  Then
   \([z^5]M^{[5]}=0\) and \(L_1YR_1\) contributes nothing to
   \(B_7^{\mathfrak f}\).  The next live Y-containing coefficient gate is
   \(L_2YR_0/L_0YR_2\).
2. **Parity-corrected mixed-output theorem.**  Define a separate
   \(M^{[5]}\) projection extracting the off-diagonal \([z^5]\) combination
   from \(r^{(2)},r^{(4)},r^{(6)}\), and prove it does not consume or duplicate
   grade \(0,2,4\) source sectors in the same-point Frechet gates.

Without one of these, \(M_i^{[5]}\) remains a placeholder and the
\(L_1YR_1\) determinant identities should not be attempted.

# Autoresearch next step

continue: under the homogeneous absence theorem, move the coefficient-table
attack to \(L_2YR_0/L_0YR_2\) and test whether their \(Y\)-slot also disappears
at \(B_7\) when \(M^{[5]}\) starts at \(z^6\), or whether second-Frechet
lower-order factors can still reach order \(7\).

# Ledger destination

`uv.md`, `findings.md`, and `attempts.md`: record as `keep`.  This is a sharp
UV-026 convention reduction: nonzero parity-corrected \(M^{[5]}\) is blocked
from current source alone, while the coherent homogeneous convention removes
\(L_1YR_1\) at \(B_7\) and redirects the mixed-input question to
\(L_2YR_0/L_0YR_2\).
