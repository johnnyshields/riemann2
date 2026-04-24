# Adversarial Verdict: UV-026 Stage 1 Generator

## Verdict

Accept the generator as source-faithful Stage 1 infrastructure under a
conditional scope.  It implements the displayed same-point and mixed formulas
in ordinary \(z\) after \(s=z/Q^2\), preserves tag and grade axes as separate
tables, emits the mixed source-linear block as
\[
M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin}),
\]
and checks the demo baseline/source-linear mixed numerators have no negative
powers after division by \(s,s^2,s^3\).

Do not accept it as an actual UV-026 table theorem or determinant proof.  The
actual finite-grade split and actual scalar source jets are still external.

## Checklist Result

- Ordinary \(z\): pass.  The script uses \(s=z/Q^2\) via
  `s_factor = Fraction(1, q_value**2)` and expands
  \(q_0(m\pm z/(2Q^2))\).
- Source tags and grades: pass.  `TAGS=("1","2")` and `GRADES=("1","5")`;
  output has separate `deltaG_lin[tag][grade][sign]` and
  `M_scaled[tag][grade]` tables.
- Mixed normalization: pass.  The manifest states
  `M_i^[a] = Gr_a(mathfrak D_Q delta N_i^lin)`, and the script applies
  \(\mathfrak D_Q\) after division with factors
  \(\begin{pmatrix}Q^2&Q\\Q&1\end{pmatrix}\).
- Removable singularities: pass for the built-in demo.  The rerun reports
  `N0_negative_powers=[]`, `M_negative_powers=[]`, `passed=true`.
  Scope: this is a demo/test, not a symbolic proof for all source jets.
- 42-scalar count: pass.  The count is
  \(10+2\cdot2\cdot8=42\): \(q_0^{(0)},\ldots,q_0^{(9)}\), and
  \((r_i^{[a]})^{(2)},\ldots,(r_i^{[a]})^{(9)}\) for two tags and two grades.
  The derivative cap \(9\) is justified because the mixed \(s^{-3}\) entry
  requires numerator coefficients through \(z^{10}\) to output through
  \([z^7]\).

## Conditional Scope

- The script is standard-library rational arithmetic.  Actual symbolic source
  formulas in parameters may need a symbolic extension or rational
  specialization.
- The source-removal conditions \(r^{(0)}=r^{(1)}=0\) are assumed by the source
  definition.  The parser does not reject invalid nonzero lower derivatives,
  though such inputs may fail the mixed removable-singularity check.
- The output is Stage 1 source-table data only.  It does not compute
  inverse-square-root Frechet tables, seven cubic gate vectors, or determinant
  identities against \(A_5^{\mathfrak f}(m)\).

## Verifier Run

Owned verifier:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/scripts/verify_stage1_generator.py`.

Owned verifier SHA1:
`C25FF0D44F21FB23A7D89049194A7368B6D85704`.

Output:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-234737-verifier-adversarial-UV026-stage1-generator/notes/stage1_generator_verifier_output.json`.

Relevant result:

```text
generator_sha1 = EBCF868CDE90CFEA3A5068C7C769F3F06F346E99
manifest_sha1 = 66EF80F8260752880035C7075F279E2FE01EBFB1
rerun_manifest_sha1 = 66EF80F8260752880035C7075F279E2FE01EBFB1
all_checks_passed = true
failed_checks = []
```
