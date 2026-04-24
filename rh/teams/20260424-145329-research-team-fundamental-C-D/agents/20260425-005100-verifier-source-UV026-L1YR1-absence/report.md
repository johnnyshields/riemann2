# Claim

Under the clean homogeneous scalar-grade convention
\[
\operatorname{Gr}_a r=\frac{r^{(a+2)}(m)}{(a+2)!}(t-m)^{a+2},
\]
the \(L_1YR_1\) middle input is absent at \(B_7^{\mathfrak f}\). In that convention \(\Lambda^{[1]}\) is sourced by \(r^{(3)}\) and starts at ordinary \(z\)-order \(1\), while \(M^{[5]}\) is sourced by \(r^{(7)}\) and has no \([z^5]\) coefficient; its first mixed order is \(6\). Hence every \(L_1YR_1\) factor \(\Lambda^{[1]}M^{[5]}\Lambda^{[1]}\) starts at order \(1+6+1=8\), so \([z^7]\Lambda^{[1]}M^{[5]}\Lambda^{[1]}=0\).

This is promotable only as a scoped absence theorem conditional on adopting the homogeneous scalar-grade convention. It is not an unconditional theorem for alternative readings where \(M^{[5]}\) means the full mixed matrix \([z^5]\) output or a parity-corrected non-homogeneous projection.

# Status

proved

# Evidence

Separate proved / conditional / missing.

Proved from source. The \(\mathfrak D_Q\)-scaled convention is fixed by \(\delta N=\mathfrak D_Q^{-1}Y\), and the actual one-pair mixed input is \(Y_\rho=\mathfrak D_Q(\delta N_\rho)\). The source variables are affine-removed before expansion:
\[
r_\rho(t)=f_\rho(t)-f_\rho(m)-f_\rho'(m)(t-m),
\]
with \(d_\pm=r_\rho(t_\pm)\), \(e_\pm=r_\rho'(t_\pm)\), \(g_\pm=r_\rho''(t_\pm)\), and \(\eta=\int_{t_+}^{t_-}r_\rho(u)\,du\). The tagged block is pre-whitening and explicitly leaves \(B_7^{\mathfrak f}\), \(\Pi_{1,1}\), and the cubic gauge theorem as separate obligations. Sources: `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466, 2607--2787, and 2797--2899.

Proved from same-point order. Under the homogeneous scalar grade, \(\operatorname{Gr}_1 r\) is the \(r^{(3)}(m)(t-m)^3/3!\) monomial. Since the same-point block has the \(g=r''\) channel in the \((2,2)\) entry, the same-point source-linear input first appears at order \(3-2=1\). The inverse-square-root Frechet operator has ordinary nonnegative baseline series, so it cannot lower this order; thus \(\Lambda^{[1]}\) starts at order \(1\).

Proved from mixed parity. Under the same convention, \(\operatorname{Gr}_5 r\) is the \(r^{(7)}(m)(t-m)^7/7!\) monomial. For an odd source monomial, \(\eta=0\) and the leading mixed diagonal channel cancels by \(d_-+d_+=0\). The first surviving mixed channel is off-diagonal \(d/s\), which for \(k=7\) starts at ordinary order \(6\). Therefore \([z^5]M^{[5]}=0\). This agrees with Hilbert's mixed-parity theorem: the full \([z^5]M\) slot exists only in the off-diagonal antisymmetric channel and is supported by even derivatives \(r^{(2)},r^{(4)},r^{(6)}\), not by \(r^{(7)}\).

Computational order audit. I wrote and ran `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-005100-verifier-source-UV026-L1YR1-absence/scripts/homogeneous_l1yr1_absence_audit.py`. Script SHA1: `4EB3C1ECBBE13F4E6563EA343CFC4A2B7000C5E2`. Output: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-005100-verifier-source-UV026-L1YR1-absence/notes/homogeneous_l1yr1_absence_audit.json`, SHA1 `213464FED96AFD7B888CF9EC124815CF819710CE`.

Relevant output:

```text
"M5_has_z5_coefficient": false
"L1YR1_min_order": 8
"L1YR1_has_z7_contribution": false
"verdict": "absent at z^7 under homogeneous scalar grade"
```

Conditional on convention. The absence theorem is valid if \(M_i^{[5]}\) is the mixed table induced by the homogeneous scalar \(\operatorname{Gr}_5 r_i\). It is not valid for a convention where \(M_i^{[5]}\) is separately defined as the full ordinary-\(z\) matrix coefficient \([z^5]\mathfrak D_Q\delta N_i^{\lin}\), because that coefficient is generally nonzero and supported by \(r^{(2)},r^{(4)},r^{(6)}\).

Missing for alternative conventions. Current source does not prove a parity-corrected non-homogeneous source projection that moves \(r^{(2)},r^{(4)},r^{(6)}\) into \(M^{[5]}\) while preserving grade-0/2/4 bookkeeping and same-point \(\Lambda\)-factor compatibility.

# Baseline / delta

Baseline: the parity-corrected grade report proposed the homogeneous scalar grade as the clean convention and said \(L_1YR_1\) is absent at \(B_7\), while the adversarial parity-grade report rejected moving even derivatives into scalar grade \(5\) from current bookkeeping.

Delta: this source/adversarial pass confirms the absence theorem under the homogeneous convention. It sharpens the promotion boundary: the result is promotable as a scoped absence statement only after the convention choice is explicit; otherwise \(M_i^{[5]}\) remains a placeholder and the alternative matrix-output reading is still a separate theorem path.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466: \(\mathfrak D_Q\) scaling and \(Y\)-normalization.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2607--2787: affine-removed source variables, same-point \(g=r''\) channel, and exact mixed formulas.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2797--2899: tagged pre-whitening source block and scope guard.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 12617--12714: \(L_1YR_1\) coefficient gate and missing \(\Lambda\)/\(M^{[5]}\) coefficient lists.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md` lines 56--110: UV-026 homogeneous absence and alternative \(M^{[5]}\) convention language.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`: current UV-026 mixed-input parity and homogeneous absence finding.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-gap-closer-UV026-parity-corrected-grade/report.md`: homogeneous convention and absence proposal.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-verifier-adversarial-UV026-parity-grade-conflicts/report.md`: rejection of the scalar-grade shortcut moving \(r^{(2)},r^{(4)},r^{(6)}\) into grade \(5\).
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/report.md`: transpose parity and \([z^5]M\) support.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/report.md`: initial \(L_1YR_1\) homogeneous prototype.
- Own script: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-005100-verifier-source-UV026-L1YR1-absence/scripts/homogeneous_l1yr1_absence_audit.py`, SHA1 `4EB3C1ECBBE13F4E6563EA343CFC4A2B7000C5E2`.
- Own output: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-005100-verifier-source-UV026-L1YR1-absence/notes/homogeneous_l1yr1_absence_audit.json`, SHA1 `213464FED96AFD7B888CF9EC124815CF819710CE`.

# Dependencies

- Explicit adoption of the homogeneous scalar-grade convention for UV-026:
  \[
  \operatorname{Gr}_a r=r^{(a+2)}(m)(t-m)^{a+2}/(a+2)!.
  \]
- The prior mixed-parity theorem that odd source monomials miss odd mixed orders and that \([z^5]M\) is supported only by even derivatives in the full mixed matrix.
- A ledger/paper wording update distinguishing this absence theorem from any alternative matrix-output \(M^{[5]}\) convention.
- The next \(Y\)-slot gates \(L_2YR_0/L_0YR_2\), because \(L_1YR_1\) no longer carries a \(B_7\) middle input under homogeneous grade.

# Strongest objection

The strongest objection is source-language, not algebraic: the current paper remark writes a "grade-five mixed input" \(M_i^{[5]}\) but does not itself define \([5]\). If a future theorem defines \(M_i^{[5]}\) as the full ordinary-\(z\) matrix order-5 projection, then \(L_1YR_1\) is not absent, because \([z^5]M\) can be nonzero from \(r^{(2)},r^{(4)},r^{(6)}\). Thus the absence theorem must not be promoted as an unconditional statement about every possible \(M_i^{[5]}\) reading.

# Needed for promotion

Promote as a scoped absence theorem only if the following are made explicit:

1. UV-026 uses the homogeneous scalar-grade convention for this branch.
2. \(M_i^{[5]}\) in the \(L_1YR_1\) branch means the mixed series induced by \(\operatorname{Gr}_5 r_i=r_i^{(7)}(m)(t-m)^7/7!\), not the full \([z^5]\mathfrak D_Q\delta N_i^{\lin}\) matrix coefficient.
3. The seven-family inventory marks \(L_1YR_1\) absent at \(B_7^{\mathfrak f}\) under this convention, rather than treating the zero as a determinant-gauge identity.
4. Any nonzero matrix-output or parity-corrected \(M^{[5]}\) alternative remains quarantined behind a separate no-double-counting/source-inventory theorem.

# Autoresearch next step

continue: redirect the \(Y\)-slot coefficient attack to \(L_2YR_0/L_0YR_2\) under the homogeneous scalar-grade convention and test whether the second-Frechet side factors can combine with the delayed \(M^{[5]}\) order \(6\) to reach \(B_7\), or whether those families are also absent.

# Ledger destination

`attempts.md`, `findings.md`, and `uv.md`: keep. This confirms the homogeneous \(L_1YR_1\) absence theorem for capture, while preserving the source-language guardrail that alternative matrix-output \(M^{[5]}\) conventions are not covered.
