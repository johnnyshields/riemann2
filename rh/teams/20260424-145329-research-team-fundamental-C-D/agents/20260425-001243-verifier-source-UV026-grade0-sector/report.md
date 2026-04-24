# Claim

Current source and current UV-026 reports do not justify ignoring the grade-0 \(r^{(2)}(m)\) sector under the mixed-order filtration. From the inspected scope alone, \(r^{(2)}(m)\) is neither removed by affine normalization, nor classified by the seven cubic-family inventory, nor proved invisible to \(B_7^{\mathfrak f}\). The missing substatement is a pre-\(\Phi_K\), ordinary-\(z\), fixed-sector grade-0 exclusion/gauge/source-class theorem.

# Status

open

# Evidence

Proved from inspected source: affine source normalization defines
\[
r_\rho(t)=f_\rho(t)-f_\rho(m)-f_\rho'(m)(t-m),
\]
so it removes the \(0\)- and \(1\)-jets only. The same-point source variables then satisfy, with \(t_\pm=m\pm z/(2Q^2)\), that \(g_\pm=r_\rho''(t_\pm)\) has constant term \(r_\rho^{(2)}(m)\), \(e_\pm=r_\rho'(t_\pm)\) starts at order \(z\) with \(r_\rho^{(2)}(m)\), and \(d_\pm=r_\rho(t_\pm)\) starts at order \(z^2\) with \(r_\rho^{(2)}(m)\). The mixed block uses the same source data plus \(\eta=\int_{t_+}^{t_-}r_\rho(t)\,dt\) behind removable-singularity divisions by powers of \(s=z/Q^2\). Thus \(r^{(2)}(m)\) is a real pre-\(\Phi_K\) source input in the normalization under audit.

Conditional from the mixed-order filtration candidate: if \(\operatorname{Gr}_a r\) is defined by the first ordinary-\(z\) finite order after the displayed \(\mathfrak D_Q\)-scaled source formulas, then \(r^{(k)}(m)\) has grade \(k-2\). This places \(r^{(2)}(m)\) in grade \(0\), \(r^{(3)}(m)\) in grade \(1\), and \(r^{(7)}(m)\) in grade \(5\).

Missing from current source: no inspected theorem says that cubic terms containing a grade-0 source factor are excluded from the UV-026 finite source tables, killed by \((1-\Pi_{1,1})\), already one-pair \(K_5/K_3\), source-trivial, pure, or \(A_5^{\mathfrak f}\)-gauge. The seven-family inventory lists the algebraic cubic families for the \((1,1,5)\) target, but it does not prove that grade-0 terms cannot leak into the relevant \(z^7\) fixed-sector coefficient through the inverse-square-root/Frechet recurrences or mixed-block removable-singularity expansions.

# Baseline / delta

Baseline: UV-026 had a complete seven-family cubic inventory for the stated non-\((1,1)\) \((1,1,5)\) gates, and the mixed-order filtration candidate reduced \(\operatorname{Gr}_1\) and \(\operatorname{Gr}_5\) to \(r^{(3)}(m)\) and \(r^{(7)}(m)\), respectively.

Delta: this audit isolates the leftover \(r^{(2)}(m)\) sector as a separate source-normalization blocker. It rejects the shortcut "affine normalization already killed grade 0" from the inspected formulas alone, and adds explicit acceptance criteria for any theorem that wants to omit grade 0 from the UV-026 gates.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2607--2899: source remainder \(r_\rho\), \(t_\pm\), \(d_\pm,e_\pm,g_\pm,\eta\), same-point and mixed pre-whitening formulas, tagged block setup.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 12617--12714: UV-026 pre-\(\Phi_K\) fixed-sector target and \(L_1YR_1\) finite-grade subtarget.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 6535--6654 and 7656--7842: one-pair witness slices involving \(\eta_2/X_1\), \(q^{(5)}/X_3\), and \(q^{(7)}/X_5\); useful as witnesses, not scalar grade definitions for UV-026.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`, UV-026: immediate source-jet subtarget requiring scalar grade split and separate grade-0 handling/exclusion.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`: current UV-026 summary and mixed-order filtration finding.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-200220-gap-closer-UV026-cubic-source-terms/report.md`: seven cubic homogeneous families and source-classification gap.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/report.md`: candidate \(k\mapsto k-2\) filtration and explicit grade-0 obstruction.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-verifier-source-UV026-grade0-sector/notes/grade0-sector-guardrails.md`: guardrails deposited by this audit.

# Dependencies

- A source-level definition of the scalar finite-grade split before \(\Phi_K\), in ordinary \(z\), compatible with \(B_7^{\mathfrak f}=\pi_{\mathfrak f}[z^7]\).
- The Stage 1 normalized source-table theorem with source tags retained and \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\), not raw \(\delta N\).
- A theorem controlling how lower-grade source factors propagate through the inverse-square-root/Frechet expansions \(S^2=G\), \(BS=I\), and through the mixed block's removable singularities.

# Strongest objection

The UV-026 statement is explicitly about cubic terms of type \((1,1,5)\), so one could argue that grade-0 terms are out of scope by definition. That objection is not settled by the inspected source because the scalar grade convention itself is still being defined, and no source theorem yet states that lower-grade \(r^{(2)}(m)\) terms cannot contribute to the same \(B_7^{\mathfrak f}\) fixed-sector coefficient through normalization/Frechet mixing or that they are handled by an earlier source class.

# Needed for promotion

Promote only after one of the following is proved at the pre-\(\Phi_K\), matrix/fixed-sector, ordinary-\(z\) level:

1. an exclusion theorem saying all cubic terms with at least one \(\operatorname{Gr}_0 r\) factor are outside the UV-026 \((1,1,5)\) gate and cannot leak into \(B_7^{\mathfrak f}\);
2. a gauge theorem saying every such non-\((1,1)\) grade-0-containing term has \(B_7^{\mathfrak f}\in\mathbf C A_5^{\mathfrak f}(m)\);
3. a source-class theorem identifying those terms as actual one-pair \(K_5\), one-pair \(K_3\), source-trivial, or pure classes already covered by paper source results; or
4. an expanded cubic inventory that includes the grade patterns involving \(\operatorname{Gr}_0 r\) and proves their determinant/gauge tests against \(A_5^{\mathfrak f}(m)\).

# Autoresearch next step

Attack the smallest missing substatement: define \(\operatorname{Gr}_0 r=r^{(2)}(m)(t-m)^2/2\) in the same ordinary-\(z\), \(\mathfrak D_Q\)-scaled Stage 1 generator normalization, enumerate all cubic terms with at least one grade-0 factor that can reach \([z^7]\), and test whether they are excluded by type, already one-pair/pure, or require new \(A_5^{\mathfrak f}\)-gauge determinant checks.

# Ledger destination

Route row in `attempts.md` as `keep`: source audit sharpens UV-026 by isolating grade-0 handling as an unresolved blocker. The live UV-026 entry should retain or sharpen the existing scalar-grade subtarget to require a grade-0 exclusion/handling theorem before any \((1,1,5)\) scalar-grade convention is promoted.
