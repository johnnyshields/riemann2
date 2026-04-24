# Stage 1 Source-Table Reduction

## Result

The displayed source formulas are enough to generate the Stage 1 source tables
from a smaller scalar midpoint-jet input.  In ordinary \(z\), with
\[
s=z/Q^2,\qquad t_\pm=m\pm z/(2Q^2),
\]
the needed source tables through \(z^7\) are determined by:

- baseline derivatives \(q_0^{(k)}(m)\) for \(0\le k\le 9\);
- for each tag \(i=1,2\) and finite grade \(a\in\{1,5\}\), source-remainder
  derivatives \((r_i^{[a]})^{(k)}(m)\) for \(2\le k\le 9\).

That is \(10+2\cdot2\cdot8=42\) scalar derivative inputs.

## Reconstruction Formulas

Baseline:
\[
q_{0,\pm}(z)=q_0(m\pm z/(2Q^2)),
\]
\[
\Delta_0(z)=\Phi_0(t_-)-\Phi_0(t_+)
=\sum_{k=0}^9
\frac{q_0^{(k)}(m)}{(k+1)!}
\left[
\left(-\frac{z}{2Q^2}\right)^{k+1}
-
\left(\frac{z}{2Q^2}\right)^{k+1}
\right]
+O(z^{11}).
\]
This is the exact finite form of the relation \(q_0=\Phi_0'\).

For source grade \(a\in\{1,5\}\):
\[
d_{i,\pm}^{[a]}(z)=r_i^{[a]}(m\pm z/(2Q^2)),
\qquad
e_{i,\pm}^{[a]}(z)=(r_i^{[a]})'(m\pm z/(2Q^2)),
\]
\[
g_{i,\pm}^{[a]}(z)=(r_i^{[a]})''(m\pm z/(2Q^2)),
\]
and
\[
\eta_i^{[a]}(z)=\int_{t_+}^{t_-}r_i^{[a]}(u)\,du
=\sum_{k=2}^9
\frac{(r_i^{[a]})^{(k)}(m)}{(k+1)!}
\left[
\left(-\frac{z}{2Q^2}\right)^{k+1}
-
\left(\frac{z}{2Q^2}\right)^{k+1}
\right]
+O(z^{11}).
\]
The lower derivatives \(r_i^{[a]}(m)\) and \((r_i^{[a]})'(m)\) vanish because
the midpoint affine jet is removed in the source definition.

## Generated Tables

With the above scalar jets, the script generates:

- \(G_\pm^{(0)}(z)\) from the exact same-point formula;
- \(N_0(z)\) from the exact mixed formula;
- \(\delta G_{i,\pm}^{\lin,[a]}(z)\) from the source-linear same-point formula;
- \(M_i^{[a]}(z)=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})(z)\) from
  the source-linear mixed formula and the Stage 0 scaled-\(Y\) normalization.

The mixed block divisions by \(s,s^2,s^3\) require numerator expansions up to
\(z^8,z^9,z^{10}\), respectively, to produce \(z^0,\ldots,z^7\) output.  This
is why the scalar baseline/source derivative input goes up to order \(9\), not
only order \(7\).

## Script Evidence

Script:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/scripts/stage1_source_table_generator.py`.

Output:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-233157-gap-closer-UV026-stage1-source-tables/notes/stage1_source_table_manifest.json`.

Relevant run summary:

```text
"minimal_scalar_input_count": {
  "baseline_q_derivatives": 10,
  "source_r_derivatives": 32,
  "total": 42
}
"removable_singularity_check": {
  "N0_negative_powers": [],
  "M_negative_powers": [],
  "passed": true
}
```

The built-in demo is only an admissible algebra check, not a zeta-source claim.
Its purpose is to verify that the Taylor/integral reconstruction removes the
negative powers created by the \(1/s,1/s^2,1/s^3\) formulas and that the code
emits all Stage 1 table shapes.

## Smallest Missing Source Sub-Statements

From the inspected source alone, the remaining missing statements are:

1. A finite-grade split \(r_i=r_i^{[1]}+r_i^{[5]}+\cdots\) for the tagged
   source remainders in the same normalization as \(B_7^{\mathfrak f}\).
2. The scalar midpoint derivative values, or formulas, for
   \(q_0^{(k)}(m)\), \(0\le k\le9\).
3. The scalar midpoint derivative values, or formulas, for
   \((r_i^{[a]})^{(k)}(m)\), \(i=1,2\), \(a\in\{1,5\}\), \(2\le k\le9\).
4. A statement that these scalar jets are the actual tagged source-linear input
   used by the UV-026 matrix product before \(\Phi_K\).

Once these are supplied, Stage 1 tables are generated directly, and the finite
equations \(S^2=G\), \(BS=I\) can consume them through \(z^7\).
