# Claim

Hilbert's order-count absence for \(L_2YR_0\) and \(L_0YR_2\) is correct under the homogeneous scalar-grade convention
\[
\operatorname{Gr}_a r=\frac{r^{(a+2)}(m)}{(a+2)!}(t-m)^{a+2}.
\]
The possible weak point does not fail: the second-Frechet inverse-square-root term cannot lower ordinary \(z\)-order, because the baseline inverse square roots and their Frechet coefficients are holomorphic ordinary-\(z\) series. With homogeneous grades, the only allowed \((1,1,5)\) placements start at order \(8\), so \(L_2YR_0\) and \(L_0YR_2\) are absent at \(B_7^{\mathfrak f}\). This closure is scoped to homogeneous scalar grade only; alternative matrix-output \(M^{[5]}\) conventions remain quarantined.

# Status

proved

# Evidence

Separate proved / conditional / missing.

Proved from source. Corrected whitening is a pre-\(\Phi_K\) matrix product
\[
G_{m,-}^{\corr}(s)^{-1/2}N_m^{\corr}(s)G_{m,+}^{\corr}(s)^{-1/2}.
\]
The same-point blocks remain uniformly positive definite and their inverse square roots are holomorphic on the small disk. The proof invokes holomorphic functional calculus after the spectral gap estimate. Therefore the baseline inverse-square-root coefficients have no negative ordinary-\(z\) powers. Source: `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 1392--1458.

Proved order lemma. Let \(B_2(z)\) denote the second Frechet bilinear map of \(A\mapsto A^{-1/2}\) at the holomorphic baseline block \(G_\pm^{(0)}(z)\). Since \(B_2(z)\) is holomorphic in \(z\), if same-point source inputs \(H(z)\) and \(K(z)\) start at ordinary orders \(a\) and \(b\), then
\[
B_2(z)[H(z),K(z)]
\]
starts at order at least \(a+b\). Baseline inverse-square-root factors may contribute order \(0\) and higher, but cannot lower order. Any \(Q\)-scale factors are not negative powers of ordinary \(z\).

Proved source-order inputs. The source variables are affine-removed and the same-point source-linear block contains the \(g=r''\) channel. Under homogeneous scalar grade, a grade-\(a\) same-point input starts at ordinary order \(a\). The mixed input is delayed for the odd homogeneous pieces by exact mixed parity: \(M^{[1]}\) starts at order \(2\) and \(M^{[5]}\) starts at order \(6\). Sources: `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466, 2607--2787, and 2797--2899; parity reports cited below.

Proved placement reduction. The earlier \(L_2YR_0/L_0YR_2\) inventory reduced the \((1,1,5)\) Y-slot families to the placements \(\{1,1\}\) with \(M^{[5]}\), and \(\{1,5\}\) with \(M^{[1]}\), with left/right mirrored versions. Under the order lemma, \(\{1,1\}\) second Frechet starts at order \(2\), \(\{1,5\}\) starts at order \(6\), \(M^{[5]}\) starts at order \(6\), \(M^{[1]}\) starts at order \(2\), and the baseline side factor starts at order \(0\). Thus all placements have total order \(8\).

Computational order audit. I wrote and ran `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-010000-verifier-adversarial-UV026-L2YR0-order/scripts/l2yr0_order_verifier.py`. Script SHA1: `3E96FEB9304BD6AAF3F1FE3547D10E058BBB766E`. Output: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-010000-verifier-adversarial-UV026-L2YR0-order/notes/l2yr0_order_verifier.json`, SHA1 `9447540DC0DE5BF6D7DE3C0E9A4FC6F00AF7D641`.

Relevant output:

```text
"minimum_total_order": 8
"all_terms_start_after_z7": true
"families_absent_at_B7": true
```

Conditional on convention. This verifies absence only if \(M^{[5]}\) is the mixed series induced by homogeneous \(\operatorname{Gr}_5 r\), i.e. by the \(r^{(7)}\) scalar piece. If a future theorem defines \(M^{[5]}\) as an actual mixed matrix \([z^5]\) output projection, then \(M^{[5]}\) may be nonzero from \(r^{(2)},r^{(4)},r^{(6)}\), and all Y-slot gates must be reopened.

Missing for alternative conventions. No inspected source proves a parity-corrected non-homogeneous \(M^{[5]}\) projection with no-double-counting against grades \(0,2,4\). The present closure does not cover that path.

# Baseline / delta

Baseline: Hilbert's homogeneous gate report claimed \(L_2YR_0/L_0YR_2\) are absent at \(B_7\), but marked source/adversarial verification as the next step, especially for the second-Frechet order-lowering concern. The older L2YR0 report had reduced the families to a missing coefficient theorem before the homogeneous parity convention was adopted.

Delta: this verifier closes the weak point. The second Frechet inverse-square-root term is order-preserving in the needed lower-bound sense. Under homogeneous scalar grade, \(L_1YR_1\), \(L_2YR_0\), and \(L_0YR_2\) are absent at \(B_7^{\mathfrak f}\), so the active homogeneous UV-026 inventory can move to the non-Y cubic families unless the \(M^{[5]}\) convention is reopened.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 1392--1458: holomorphic corrected whitening and inverse square roots.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466: \(\mathfrak D_Q\) and \(Y\)-normalization.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2607--2787: affine-removed source variables, same-point \(g=r''\), and exact mixed formulas.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2797--2899: tagged pre-whitening source block and scope guard.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 12617--12714: UV-026 \(B_7^{\mathfrak f}\) matrix/fixed-sector target and \(L_1YR_1\) model.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md` lines 56--114: UV-026 homogeneous Y-slot absence language.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`: current UV-026 parity and homogeneous Y-slot frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-005100-gap-closer-UV026-L2YR0-homogeneous-gate/report.md`: Hilbert's L2YR0/L0YR2 homogeneous order claim.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-005100-verifier-source-UV026-L1YR1-absence/report.md`: verified \(L_1YR_1\) homogeneous absence.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-003100-gap-closer-UV026-parity-corrected-grade/report.md`: homogeneous scalar-grade convention and quarantine of nonzero alternatives.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-231056-explorer-UV026-next-cubic-L2YR0/report.md`: original second-Frechet/Y-slot placement reduction.
- Own script: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-010000-verifier-adversarial-UV026-L2YR0-order/scripts/l2yr0_order_verifier.py`, SHA1 `3E96FEB9304BD6AAF3F1FE3547D10E058BBB766E`.
- Own output: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-010000-verifier-adversarial-UV026-L2YR0-order/notes/l2yr0_order_verifier.json`, SHA1 `9447540DC0DE5BF6D7DE3C0E9A4FC6F00AF7D641`.

# Dependencies

- Explicit homogeneous scalar-grade convention for this branch.
- The mixed parity theorem giving \(M^{[1]}\) lowest order \(2\) and \(M^{[5]}\) lowest order \(6\) for homogeneous odd source pieces.
- Holomorphic baseline inverse square roots and their Frechet coefficients.
- The earlier placement reduction for \(L_2YR_0/L_0YR_2\).

# Strongest objection

The conclusion is not invariant under a different interpretation of \(M^{[5]}\). If \(M^{[5]}\) is redefined as the full ordinary-\(z\) mixed matrix order-5 output, then the middle factor can start at \(5\), and the old \(L_2YR_0/L_0YR_2\) coefficient theorem must be reopened. This report only proves absence under the homogeneous scalar source-grade convention.

# Needed for promotion

Promote only as a scoped absence theorem with these clauses:

1. \(M^{[1]}\) and \(M^{[5]}\) are induced by homogeneous scalar grades \(r^{(3)}\) and \(r^{(7)}\).
2. The second-Frechet inverse-square-root bilinear terms have holomorphic ordinary-\(z\) coefficients and cannot lower input order.
3. \(L_2YR_0\) and \(L_0YR_2\) are absent at \(B_7^{\mathfrak f}\), not proved by determinant identities.
4. Alternative matrix-output or non-homogeneous parity-corrected \(M^{[5]}\) conventions remain quarantined and would reopen all Y-slot gates.

# Autoresearch next step

continue: verify the non-Y homogeneous gates \(L_2N_0R_1/L_1N_0R_2\), where the mixed factor is baseline \(N_0\) instead of delayed \(Y\). The same second-Frechet no-lowering lemma applies, but \(N_0\) starts at order \(0\), so the order count is no longer automatically absent.

# Ledger destination

`attempts.md`, `findings.md`, and `uv.md`: keep. This verifies the homogeneous order absence for \(L_2YR_0/L_0YR_2\) and supports capturing all Y-slot homogeneous families as absent at \(B_7\), while preserving the quarantine for matrix-output \(M^{[5]}\).
