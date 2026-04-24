# Claim

Current paper/team language treats \(M_i^{[5]}\) inconsistently enough that no theorem should use it without a clarifying definition. The paper WIP remark uses \(M_i^{[5]}\) as a "grade-five mixed input" for a \(1/5/1\) source-grade family, not as an explicitly defined ordinary-\(z\) mixed-order-5 projection. The UV/generator language upgrades that placeholder to the intended object \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\), but the actual scalar grade projection \(\operatorname{Gr}_5\) remains undefined. The mixed-order prototype then shows that the natural homogeneous \(r^{(7)}\) candidate gives \([z^5]M^{[5]}=0\), so the notation cannot silently mean both "finite source grade five" and "nonzero ordinary-\(z\) middle coefficient at order five."

# Status

open

# Evidence

Proved from wording. The WIP paper remark states that \(L_1YR_1\) has source tags distributed in finite grade \(1/5/1\), then says to "write the grade-five mixed input" as \(M_i^{[5]}(z)=\sum_{s\ge0}M_{i,s}^{[5]}z^s\). It later lists \([z^s]M_i^{[5]}\) as missing coefficient data. This names a grade-five mixed input but does not define the grade projection or state that the superscript \([5]\) means actual ordinary-\(z\) order \(5\). Source: `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 12617--12714, especially 12649--12660 and 12706--12712.

Proved from UV wording. UV-026 now defines the Stage 1 table target as ordinary \(z\), pre-\(\Phi_K\), with source tags retained and \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\). The same UV says the scalar grade split \(r_i=r_i^{[1]}+r_i^{[5]}+\cdots\) is still missing and explicitly asks whether grade \(5\) means \(q^{(5)}/X_3\), \(q^{(7)}/X_5\), or another mixed-block slice. Source: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md` lines 62--83.

Proved from source normalization. The paper defines the scaled mixed normalization by \(\delta N=\mathfrak D_Q^{-1}Y\) and the one-pair weighted mixed input \(Y_\rho=\mathfrak D_Q(\delta N_\rho)\). The tagged source block is pre-whitening only and explicitly does not assert \(B_7^{\mathfrak f}\), \(\Pi_{1,1}\), or the cubic \((1,1,5)\) gauge theorem. Source: `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466, 2653--2664, 2797--2899.

Conditional infrastructure. The Stage 1 generator and manifest are source-faithful infrastructure for a schema whose mixed input is \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\), but they assume the finite-grade split as input. The generator report says current source does not define \(r_i^{[1]},r_i^{[5]}\) or the actual 42 scalar midpoint derivatives. Its reduction note also says the built-in demo is only an admissible algebra check, not a zeta-source claim. Sources: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/report.md` lines 54--60 and 94--97; `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1-source-table-reduction.md` lines 63--69 and 99--115; `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1_source_table_manifest.json` lines 2--14 and 1356--1358.

Conditional and then obstructed. The mixed-order filtration report proposes a theorem candidate: if finite grade means lowest ordinary-\(z\) order of the pre-whitening source-linear matrix inputs, then \(\operatorname{Gr}_5 r\) is the \(r^{(7)}(m)(t-m)^7/7!\) piece and \(M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})\). But the later \(L_1YR_1\) prototype shows exact mixed parity: for odd scalar derivative order \(k\), the leading mixed \(M_{22}\) channel cancels, so \(r^{(7)}\) contributes to \(M\) first in order \(6\), not \(5\). It records \([z^5]M^{[5]}=0\) for the pure \(r^{(7)}\) grade-five candidate. Sources: `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/report.md` lines 87--99 and 101--112; `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/report.md` lines 3--17, 55--60, 87--102, and 166--182.

Missing. No inspected source defines whether the superscript \([5]\) on \(M_i^{[5]}\) is an actual ordinary-\(z\) mixed-order projection, a finite source-grade label whose induced mixed table may start at another ordinary-\(z\) order, or a temporary placeholder for grade-five data still to be supplied. The current language leaves those three readings in play.

# Baseline / delta

Baseline: UV-026 had already been reduced to a Stage 1 normalized source-table theorem plus scalar grade-projection and baseline-jet subtargets. Prior reports rejected importing \(q^{(5)}/X_3\), \(q^{(7)}/X_5\), or \(\eta_2/X_1\) matrix witnesses as scalar source grades without a source theorem.

Delta: this audit sharpens the language blocker. The term \(M_i^{[5]}\) should currently be read only as a conditional placeholder for "the mixed table produced by whatever source theorem defines \(\operatorname{Gr}_5\)." It is not source-supported as a nonzero ordinary-\(z\) order-5 mixed input, and it is not yet a defined finite source grade.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 12617--12714: WIP \(L_1YR_1\) remark, \(1/5/1\) source-grade wording, \(M_i^{[5]}\), and missing coefficient lists.
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2429--2466: \(\mathfrak D_Q\) scaling and \(\delta N=\mathfrak D_Q^{-1}Y\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex` lines 2607--2899: source remainders, \(Y_\rho=\mathfrak D_Q(\delta N_\rho)\), tagged pre-whitening source block, and scope guard.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md` lines 56--95: UV-026 source-table, source-jet, grade-convention, parity, and gate subtargets.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`: current UV-026 source-bidegree summary and \(M^{[5]}\) parity warning.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/report.md` lines 54--60, 87--97, and 136--149.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1-source-table-reduction.md` lines 63--69 and 99--115.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/report.md` lines 87--90 and 129--130.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-235843-verifier-source-UV026-grade-convention/report.md` lines 83--96 and 161--181.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-000623-gap-closer-UV026-mixed-order-filtration/report.md` lines 87--112 and 174--190.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/report.md` lines 3--17, 87--102, and 175--182.

# Dependencies

- A scalar source-grade theorem defining \(\operatorname{Gr}_5\) on the affine-removed tagged source remainder before \(\Phi_K\).
- A compatibility theorem stating how that scalar grade induces \(M_i^{[5]}=\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})\) through the exact mixed block with removable singularities expanded.
- A convention deciding whether \([5]\) is a source-grade label independent of ordinary-\(z\) order, or an actual mixed-order projection.
- If the theorem needs \(L_1YR_1\) at \(B_7^{\mathfrak f}\), a nonzero \([z^5]M_i^{[5]}\) source convention or an explicit proof that the middle input is absent and the family contributes nothing at order \(7\).

# Strongest objection

One could say the paper already distinguishes the superscript \([5]\) from the coefficient index \(s\) in \(M_i^{[5]}(z)=\sum_sM_{i,s}^{[5]}z^s\), so \([5]\) is plainly a grade label and not ordinary-\(z\) order. That helps notation, but it does not define the grade label. The WIP product still requires the actual coefficient \([z^5]M_i^{[5]}\) to feed \([z^7]\Lambda^{[1]}M^{[5]}\Lambda^{[1]}\), and the homogeneous source-grade prototype makes that coefficient vanish.

# Needed for promotion

Add or cite a definition/theorem with these exact contents before using \(M_i^{[5]}\) in any UV-026 theorem:

1. Define \(\operatorname{Gr}_5 r_i\) on the affine-removed source remainder, with source tags retained, in ordinary \(z\), before \(\Phi_K\), and in the \(B_7^{\mathfrak f}\) normalization.
2. State whether \(M_i^{[5]}\) is the full mixed series induced by the source-grade piece \(\operatorname{Gr}_5 r_i\), or the actual ordinary-\(z\) order-5 part of \(\mathfrak D_Q\delta N_i^{\lin}\).
3. If \(M_i^{[5]}\) is induced by the homogeneous \(r^{(7)}\) piece, state that its \(z^5\) coefficient is zero and revise the \(L_1YR_1\) gate accordingly.
4. If \(L_1YR_1\) is meant to have a nonzero order-5 middle factor, define the non-homogeneous or parity-corrected \(\operatorname{Gr}_5\) source projection that produces it.

# Autoresearch next step

continue: formulate the parity-corrected \(M_i^{[5]}\) definition theorem. First decide between two clean conventions: \([5]\) as a source-grade label whose induced mixed table may start at \(z^6\), or \([5]\) as an actual \([z^5]\) mixed-order projection requiring a non-homogeneous source projection. Then rerun the \(L_1YR_1\) prototype under the chosen convention.

# Ledger destination

`uv.md` and `attempts.md`: keep as a source-language blocker. UV-026 should state explicitly that \(M_i^{[5]}\) is presently a conditional placeholder until the scalar/mixed grade definition is supplied; the route row should record that the WIP theorem cannot use \(M_i^{[5]}\) as a nonzero ordinary-\(z\) order-5 input from current source alone.
