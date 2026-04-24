# Claim

Moving the even source derivatives \(r^{(2)},r^{(4)},r^{(6)}\) into \(M_i^{[5]}\) is not source-supported as a scalar grade-five convention from current UV-026 language. It is conditionally coherent only if \(M_i^{[5]}\) is redefined as an actual ordinary-\(z\) mixed-output order-5 projection, or as a new parity-corrected non-homogeneous projection with explicit safeguards. Without that clarification, the move conflicts with grade-0/2/4 bookkeeping, contaminates same-point \(\delta G\) orders used by the \(\Lambda\) factors, and sits outside the current seven-family \((1,1,5)\) source-grade inventory.

# Status

computational

# Evidence

Proved from source. The paper defines the scaled mixed normalization by \(\delta N=\mathfrak D_Q^{-1}Y\) and the actual one-pair mixed input as \(Y_\rho=\mathfrak D_Q(\delta N_\rho)\). It defines affine-removed source variables \(d_\pm,e_\pm,g_\pm,\eta\), then expands the same-point and mixed source-linear blocks before \(\Phi_K\). The tagged source block keeps \(\tau_1,\tau_2\) linearly and explicitly leaves \(B_7^{\mathfrak f}\), \(\Pi_{1,1}\), and the cubic \((1,1,5)\) gauge theorem as separate obligations. Sources: `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466, 2607--2787, and 2797--2899.

Proved from paper wording. The \(L_1YR_1\) WIP remark says the family has source tags distributed in finite grade \(1/5/1\), writes \(M_i^{[5]}(z)=\sum_{s\ge0}M_{i,s}^{[5]}z^s\), and lists the coefficients \([z^s]M_i^{[5]}\) as missing. It names a grade-five mixed input, but does not define whether \([5]\) is scalar source grade, actual ordinary-\(z\) mixed order, or a placeholder. Source: `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 12617--12714.

Proved/verified upstream. Hilbert's mixed parity report proves \(M(-z)=M(z)^T\) and computationally verifies that through order \(7\), \([z^5]M\) is off-diagonal antisymmetric and supported only by even source derivatives \(r^{(2)},r^{(4)},r^{(6)}\), not by the homogeneous \(r^{(7)}\) candidate. Source: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/report.md`; script there `scripts/mixed_parity_audit.py`, SHA1 `5922070D51A1E2B3A4841D90317BD7A0A0727015`.

Computational adversarial audit. I wrote and ran `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-verifier-adversarial-UV026-parity-grade-conflicts/scripts/parity_grade_conflict_audit.py` before making the bookkeeping claim. Script SHA1: `33F181B288C21217D5394F4D71AC694F6A3DB578`. Output: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-verifier-adversarial-UV026-parity-grade-conflicts/notes/parity_grade_conflict_audit.json`, SHA1 `687BDDB4A41B5F95C41BDA778F7572F4F8C20C7F`.

Relevant output:

```text
"conflicting_derivatives": [
  {"source_derivative": "r^2", "natural_grade": 0, "same_point_lowest_order": 0, "mixed_lowest_order": 0},
  {"source_derivative": "r^4", "natural_grade": 2, "same_point_lowest_order": 2, "mixed_lowest_order": 2},
  {"source_derivative": "r^6", "natural_grade": 4, "same_point_lowest_order": 4, "mixed_lowest_order": 4}
]
"source_grade_label": "conflict unless a new non-homogeneous grade theorem moves or duplicates lower natural grades"
"actual_ordinary_z_order_5_projection": "conditionally coherent as a matrix-output projection, not as a scalar source grade"
"parity_corrected_nonhomogeneous_source_projection": "possible only with explicit compatibility conditions"
```

Reading 1, \([5]\) as scalar source-grade label: rejected from current scalar-grade consistency. The even derivatives that support \([z^5]M\) are precisely natural grades \(0,2,4\) under the lowest-order bookkeeping. Assigning them to grade \(5\) either duplicates data across grades or moves data out of grade \(0/2/4\). In either case, the source split \(r_i=r_i^{[1]}+r_i^{[5]}+\cdots\) is no longer a clean finite-grade split unless a new non-homogeneous direct-sum theorem says so.

Reading 2, \([5]\) as actual ordinary-\(z\) order-5 projection of the mixed matrix: conditionally acceptable as a matrix-output projection. It keeps source tags because the mixed source-linear input is tag-linear, and it directly captures Hilbert's off-diagonal antisymmetric \([z^5]M\). But then it is not \(\operatorname{Gr}_5 r_i\), does not provide \(\delta G_{i,\pm}^{\lin,[5]}\), and should not be used as the scalar source grade in the Stage 1 42-scalar theorem without renaming or a bridge theorem.

Reading 3, \([5]\) as parity-corrected non-homogeneous source projection: possible only as a new theorem. Such a projection would have to use \(r^{(2)},r^{(4)},r^{(6)}\) with baseline-dependent coefficients to produce the mixed order-5 off-diagonal coefficient. But the same scalar pieces also produce same-point \(\delta G\) in ordinary orders \(0,2,4\), not order \(5\), so their lower-order same-point shadows must be excluded from \(\Lambda^{[1]}\), from \(\Lambda^{[5]}\), and from every unlisted cubic family by an explicit rule.

Seven-family inventory conflict. The current seven-family inventory classifies cubic shapes under a stated \((1,1,5)\) finite-grade pattern. If the middle "5" is actually built from lower natural grades \(0,2,4\), the inventory no longer proves that all relevant cubic source terms are included. Either the inventory must be restated in matrix-order language, or it must be expanded to include grade patterns involving \(0,2,4\) in the mixed slot.

# Baseline / delta

Baseline: Hilbert's parity report found the positive matrix fact that \([z^5]M\) can be nonzero and is sourced by \(r^{(2)},r^{(4)},r^{(6)}\), while the source-language audit left \(M_i^{[5]}\) as a conditional placeholder.

Delta: this adversarial pass separates the viable matrix fact from the invalid scalar-grade shortcut. The even-derivative move is rejected as a current scalar \(\operatorname{Gr}_5\) theorem, but retained as a possible parity-corrected matrix projection if the theorem is rewritten with explicit bookkeeping and inventory compatibility.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466: \(\mathfrak D_Q\) scaling and \(\delta N=\mathfrak D_Q^{-1}Y\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2607--2787: affine-removed source variables and same-point/mixed source-linear formulas.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2797--2899: tagged pre-whitening source block and scope guard.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 12617--12714: \(L_1YR_1\) \(1/5/1\) wording and missing \(M_i^{[5]}\) coefficients.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/report.md`: transpose parity and \([z^5]M\) support theorem.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-verifier-source-UV026-M5-language/report.md`: \(M_i^{[5]}\) source-language ambiguity.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-verifier-source-UV026-grade0-sector/report.md`: grade-0 \(r^{(2)}\) handling gap.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/report.md`: natural lowest-order grade \(k-2\) candidate and grade-0 obstruction.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-200220-gap-closer-UV026-cubic-source-terms/report.md`: seven cubic-family inventory and source-classification gap.
- Own script: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-verifier-adversarial-UV026-parity-grade-conflicts/scripts/parity_grade_conflict_audit.py`, SHA1 `33F181B288C21217D5394F4D71AC694F6A3DB578`.
- Own output: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-verifier-adversarial-UV026-parity-grade-conflicts/notes/parity_grade_conflict_audit.json`, SHA1 `687BDDB4A41B5F95C41BDA778F7572F4F8C20C7F`.

# Dependencies

- UV-026 Stage 0 normalization in ordinary \(z\), before \(\Phi_K\), with source tags retained.
- A decision whether \([5]\) denotes source grade, mixed matrix order, or a parity-corrected non-homogeneous projection.
- If non-homogeneous, a direct-sum or no-double-counting theorem for \(r^{(2)},r^{(4)},r^{(6)}\) relative to grades \(0,2,4\).
- A same-point compatibility theorem proving lower-order \(\delta G\) shadows from those even derivatives do not enter \(\Lambda^{[1]}\), \(\Lambda^{[5]}\), or unlisted cubic families.
- A revised seven-family inventory if "type \((1,1,5)\)" is no longer a scalar source-grade pattern.

# Strongest objection

The strongest positive objection is that \(L_1YR_1\) only needs the middle mixed factor at ordinary order \(5\), so perhaps \(M_i^{[5]}\) can simply mean \([z^5]\mathfrak D_Q\delta N_i^{\lin}\). That objection is valid as a possible new convention, but it concedes the main point: \(M_i^{[5]}\) is then a matrix-output coefficient, not scalar \(\operatorname{Gr}_5\) source data, and it cannot justify the UV wording requiring \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\), the Stage 1 scalar source split, or the seven-family scalar-grade inventory without further definitions.

# Needed for promotion

Before any theorem uses the even derivatives inside \(M_i^{[5]}\), supply all of the following:

1. A definition choosing one reading of \([5]\): scalar source grade, actual ordinary-\(z\) mixed order, or parity-corrected non-homogeneous projection.
2. If scalar source grade: a proof that assigning \(r^{(2)},r^{(4)},r^{(6)}\) to grade \(5\) is a direct-sum source split and does not leave unresolved grade-0/2/4 terms.
3. If actual mixed order: rename or define \(M_i^{[5]}\) as a matrix coefficient/projection and stop using it as \(\operatorname{Gr}_5 r_i\) or as a source for \(\delta G_{i,\pm}^{\lin,[5]}\).
4. If non-homogeneous: state the exact linear combination of \(r^{(2)},r^{(4)},r^{(6)}\), its baseline dependence, source-tag behavior, and removable-singularity expansion.
5. In every case: prove compatibility with the same-point \(\Lambda^{[1]}\) factors and update the seven-family inventory or prove no extra lower-grade mixed-slot families reach \(B_7^{\mathfrak f}\).

# Autoresearch next step

verify: cross-check Hilbert's proposed parity-corrected grade convention against this checklist. The first fail-fast test is whether it treats \(M_i^{[5]}\) as a matrix-output order projection or as a scalar source grade; if it is scalar, require an explicit no-double-counting theorem for grades \(0,2,4\).

# Ledger destination

`attempts.md` and `uv.md`: keep. This is a scoped adversarial rejection of the scalar-grade shortcut and a promotion checklist for the still-possible matrix-order or parity-corrected conventions.
