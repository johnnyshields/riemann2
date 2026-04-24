# Claim

The parallel Stage 1 generator deposit is source-faithful infrastructure for
UV-026, but only under a conditional scope.  It implements the current paper's
exact same-point and mixed pre-whitening formulas in ordinary \(z\) with
\(s=z/Q^2\), keeps tags and grades separated enough for the UV-026 cubic gate
inputs, emits the mixed source-linear table as
\[
M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin}),
\]
and its built-in demo genuinely checks that the baseline \(N_0\) and
source-linear \(M\) mixed numerators have no negative powers after the
\(1/s\), \(1/s^2\), and \(1/s^3\) divisions.

What is accepted: the generator and manifest are reproducible Stage 1
source-table infrastructure and a correct schema reduction to \(42\) scalar
midpoint derivatives.

What remains conditional: actual UV-026 use still requires the finite-grade
source split \(r_i=r_i^{[1]}+r_i^{[5]}+\cdots\) and actual scalar midpoint
derivative formulas or values in the same normalization.

What remains missing: the downstream inverse-square-root Frechet tables, the
seven cubic family \(\pi_{\mathfrak f}[z^7]\) vectors, and determinant
identities against \(A_5^{\mathfrak f}(m)\).

# Status

computational

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The scaled transfer section introduces
\(s=z/Q^2=Rw/Q^2\), \(\mathfrak D_Q\), and the relation
\[
\delta G_\pm=\mathfrak D_Q^{-1}X_\pm,\qquad
\delta N=\mathfrak D_Q^{-1}Y.
\]
This supports the audit requirement that mixed source tables use the scaled
\(Y=\mathfrak D_Q\delta N\) convention.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587`.

**Proved from source.**  The source-formula section uses ordinary \(z\) with
\[
t_\pm=m\pm z/(2Q^2)
\]
and defines the weighted one-pair source triple
\[
X_{\rho,\pm}=\mathfrak D_Q(\delta G_{\rho,\pm}),\qquad
Y_\rho=\mathfrak D_Q(\delta N_\rho).
\]
The same section displays the exact corrected same-point formula and mixed
formula.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2787`.

**Proved from source.**  The tagged two-atom block retains \(\tau_1,\tau_2\)
before whitening and before \(\Phi_K\), while its scope remark says
\(B_7^{\mathfrak f}\), \(\Pi_{1,1}\), and the cubic gauge theorem remain
separate obligations.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2797-2899`.

**Proved from source.**  The live UV-026 target is pre-\(\Phi_K\), pre
determinant-scalarization, and pre diagonal merger, with
\[
B_7^{\mathfrak f}(T)=\pi_{\mathfrak f}[z^7]T.
\]
The paper explicitly says the coefficient lists and determinant identities are
still missing for the displayed \(L_1YR_1\) gate.  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`.

**Verified by source/code comparison.**  The generator implements ordinary
\(z\) with \(s=z/Q^2\): constants and axes are declared at
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/scripts/stage1_source_table_generator.py:30`,
and the \(s\)-factor and Taylor expansion are at
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/scripts/stage1_source_table_generator.py:230`.
The baseline \(\Delta_0\) integral reconstruction is at line 234.

**Verified by source/code comparison.**  The exact same-point table generator
uses \(G=(1/\pi)\begin{pmatrix}2q&q'/2\\q'/2&(q''+2q^3)/12\end{pmatrix}\) at
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/scripts/stage1_source_table_generator.py:238`.
The mixed baseline numerator and divisions by \(s,s^2,s^3\) are implemented at
lines 253-272.  The source-linear mixed numerator, divisions, and
\(\mathfrak D_Q\) scaling are implemented at lines 287-341.

**Verified by manifest.**  The manifest records the accepted normalization:
ordinary \(z\), pre-\(\Phi_K\), tags `1,2`, grades `1,5`, order \(7\), and
mixed input
`M_i^[a] = Gr_a(mathfrak D_Q delta N_i^lin)`.  Manifest refs:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1_source_table_manifest.json:2`,
`:5`, `:64`, `:75`, `:102`, and `:1021`.

**Computational.**  I wrote and ran the owned verifier script
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/scripts/verify_stage1_generator.py`
before making this verifier claim.  Verifier script SHA1:
`C25FF0D44F21FB23A7D89049194A7368B6D85704`.  It reran the cited generator with
the built-in admissible demo and compared the rerun manifest to the deposited
manifest.

Relevant verifier output:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/notes/stage1_generator_verifier_output.json`.

```text
generator_sha1 = EBCF868CDE90CFEA3A5068C7C769F3F06F346E99
manifest_sha1 = 66EF80F8260752880035C7075F279E2FE01EBFB1
rerun_manifest_sha1 = 66EF80F8260752880035C7075F279E2FE01EBFB1
all_checks_passed = true
failed_checks = []
```

**Computational.**  The verifier confirms that the deposited manifest is
reproducible exactly from the cited script.  It also checks table shapes for
\(G_0^\pm\), \(N_0\), every `deltaG_lin[tag][grade][sign]`, and every
`M_scaled[tag][grade]`; all shape checks passed.

**Conditional.**  The removable-singularity check is genuine for the built-in
demo: it checks the coefficients that would become negative powers before
division and reports
`N0_negative_powers=[]`, `M_negative_powers=[]`, `passed=true`.  This is not a
symbolic proof for all possible actual source jets.

**Conditional.**  The \(42\)-scalar count follows from \(10\) baseline
derivatives \(q_0^{(0)},\ldots,q_0^{(9)}\) and \(2\cdot2\cdot8=32\) source
derivatives \((r_i^{[a]})^{(2)},\ldots,(r_i^{[a]})^{(9)}\).  The derivative
order \(9\) is justified by the mixed \(s^{-3}\) entry: output through
\([z^7]\) requires numerator data through \(z^{10}\).

**Missing.**  The generator does not supply the actual finite-grade split
\(r_i^{[1]},r_i^{[5]}\) from the paper source.  It assumes that split as input.

**Missing.**  The generator does not supply actual \(q_0^{(k)}(m)\) or
\((r_i^{[a]})^{(k)}(m)\) values/formulas; the manifest is built from an
admissible demo.

**Missing.**  The generator does not compute the finite equations \(S^2=G\),
\(BS=I\), the first/second/third Frechet inverse-square-root tables, or any
UV-026 determinant identity.

# Baseline / delta

Baseline: the Stage 1 source-normalization audit accepted the paper formulas
as starting definitions but required ordinary-\(z\), tag-retaining,
\(\mathfrak D_Q\)-normalized, removable-singularity-expanded, pre-\(\Phi_K\)
tables.  The parallel generator claimed to reduce those Stage 1 tables to a
\(42\)-scalar source-jet schema.

Delta: this adversarial pass confirms the generator and manifest as faithful
infrastructure for that schema, and narrows the conditional scope.  It does not
promote UV-026: the actual finite-grade split and actual scalar source jets are
still missing, and all determinant gates remain downstream.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/skills/research-resume/SKILL.md` - read
  because this is a resumed UV-026 research lane.
- `C:/workspace/riemann2/.agents/agents/_autoresearch.md` - read before
  acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - read completely before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 source-table and source-jet subtargets.
- Observed repository head while auditing:
  `563c0d4 dispatch UV-026 source-jet split`.  The prompt named
  `b5d2230 capture UV-026 source-table generator`; I did not move or revert
  the repository.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587` - scaled transfer,
  \(s=z/Q^2\), and \(\mathfrak D_Q\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2899` - source remainders,
  exact same-point/mixed formulas, tags, and scope guard.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - UV-026
  pre-\(\Phi_K\) \(B_7^{\mathfrak f}\) target.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1-source-table-reduction.md`.
- Generator:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/scripts/stage1_source_table_generator.py`,
  SHA1 `EBCF868CDE90CFEA3A5068C7C769F3F06F346E99`.
- Manifest:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1_source_table_manifest.json`,
  SHA1 `66EF80F8260752880035C7075F279E2FE01EBFB1`.
- Prior checklist:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-verifier-source-UV026-stage1-normalization/notes/source-normalization-map.md`.
- Owned verifier script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/scripts/verify_stage1_generator.py`,
  SHA1 `C25FF0D44F21FB23A7D89049194A7368B6D85704`.
- Owned verifier output:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/notes/stage1_generator_verifier_output.json`.
- Owned notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/notes/adversarial-stage1-generator-verdict.md`.

# Dependencies

- The displayed same-point and mixed source formulas in the paper.
- The Stage 0 normalization convention: ordinary \(z\), pre-\(\Phi_K\), tags
  retained, and \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\).
- The affine-jet removal convention \(r^{(0)}=r^{(1)}=0\).
- Actual finite-grade source split \(r_i^{[1]},r_i^{[5]}\).
- Actual scalar midpoint derivatives through the \(42\)-scalar schema.
- Downstream square-root/Frechet table generation and seven UV-026 gate tests.

# Strongest objection

The verifier confirms infrastructure, not the UV-026 theorem.  The script's
built-in demo uses rational admissible data and proves reproducibility and
negative-power cancellation for that demo.  It does not prove the actual zeta
source jets satisfy the required finite-grade split, does not reject invalid
nonzero \(r^{(0)}\) or \(r^{(1)}\) inputs at parse time, and does not handle
arbitrary symbolic parameter formulas without extension beyond
`fractions.Fraction`.

# Needed for promotion

To promote Stage 1 from infrastructure to source theorem, add or cite:

1. the actual finite-grade split \(r_i=r_i^{[1]}+r_i^{[5]}+\cdots\) in the same
   ordinary-\(z\), pre-\(\Phi_K\), tagged normalization;
2. actual formulas or values for \(q_0^{(k)}(m)\), \(0\le k\le9\);
3. actual formulas or values for \((r_i^{[a]})^{(k)}(m)\), \(i=1,2\),
   \(a\in\{1,5\}\), \(2\le k\le9\);
4. a run of the generator, or a symbolic extension of it, on those actual
   inputs with removable-singularity checks passing;
5. downstream \(S^2=G\), \(BS=I\) Frechet tables and determinant identities
   for all seven UV-026 cubic families.

# Autoresearch next step

continue: attack the immediate source-jet subtarget now in UV-026.  Define or
source the actual finite-grade split \(r_i^{[1]},r_i^{[5]}\) and the \(42\)
midpoint derivatives, then run the accepted generator on actual inputs.  If the
actual inputs are symbolic rather than rational, first extend the generator to
a symbolic backend while preserving the same manifest checks.

# Ledger destination

`findings.md`, `attempts.md`, and `uv.md`: record this verifier as `keep`.
The generator is verified as source-faithful infrastructure, while UV-026 must
remain open on the actual source-jet split, actual \(42\)-scalar data, and
downstream determinant gates.
