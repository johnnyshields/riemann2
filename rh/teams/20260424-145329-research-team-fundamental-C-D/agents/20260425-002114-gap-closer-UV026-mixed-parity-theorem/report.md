# Claim

The source-linear scaled mixed input
\[
M(z)=\mathfrak D_Q\delta N^{\lin}(z)
\]
does not have an even-only parity theorem as a matrix-valued ordinary-\(z\)
series.  The exact pre-\(\Phi_K\) mixed formulas instead give the transpose
parity
\[
M(-z)=M(z)^T.
\]
Thus \(M_{11}\) and \(M_{22}\) are even, while the off-diagonal antisymmetric
channel can carry odd powers.  In particular \([z^5]M\) can be nonzero, but
not from the pure \(r^{(7)}(m)\) source derivative: through order \(7\),
\([z^5]M\) is off-diagonal and depends only on even source derivatives
\(r^{(2)},r^{(4)},r^{(6)}\).  This rules out the homogeneous
\(r^{(7)}\)-only convention for \(M_i^{[5]}\) in \(L_1YR_1\), while showing
that a parity-corrected grade-five mixed input could exist only as an even
source-derivative/non-homogeneous projection.

# Status

computational

# Evidence

Separate proved / conditional / missing.

**Proved from source.**  The exact mixed block before \(\Phi_K\) is
\[
N_m^{\corr}(s)=\frac1\pi
\begin{pmatrix}
-2\sin\Delta/s&
(\sin\Delta+q(t_+)s\cos\Delta)/s^2\\
-(\sin\Delta+q(t_-)s\cos\Delta)/s^2&
F(q_-,q_+,\Delta;s)/(2s^3)
\end{pmatrix},
\]
with \(F=(q_-+q_+)s\cos\Delta+(2-q_-q_+s^2)\sin\Delta\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2767`.

**Proved from source.**  The source-linear expansion sets
\[
q_\pm=q_{0,\pm}+d_\pm,\qquad \Delta=\Delta_0+\eta,
\]
and linearizes the mixed block in \(d_-,d_+,\eta\).  Source:
`C:/workspace/riemann2/rh/proof_of_rh.tex:2740-2787`.

**Parity proof from the exact formulas.**  Under \(z\mapsto -z\),
\[
s\mapsto -s,\quad t_+\leftrightarrow t_-,\quad
q_{0,+}\leftrightarrow q_{0,-},\quad
d_+\leftrightarrow d_-,\quad
\Delta_0\mapsto-\Delta_0,\quad \eta\mapsto-\eta.
\]
Therefore \(\sin\Delta_0\) is odd and \(\cos\Delta_0\) is even.  Substituting
these transformations into the four linearized mixed entries gives
\[
M_{11}(-z)=M_{11}(z),\qquad
M_{22}(-z)=M_{22}(z),\qquad
M_{12}(-z)=M_{21}(z).
\]
So \(M(-z)=M(z)^T\).  This theorem is before \(\Phi_K\), determinant
scalarization, or quotient extraction.

**Computational finite audit.**  I wrote and ran
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/scripts/mixed_parity_audit.py`
before making the finite coefficient claim.  Script SHA1:
`5922070D51A1E2B3A4841D90317BD7A0A0727015`.  Output manifest:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/notes/mixed_parity_audit.json`,
SHA1 `1C227B17F1EDFBED6D8A9E74A9D7C11AB9D4BAD1`.

Relevant output:

```text
"parity_by_entry": {
  "11": {"even_powers": [2,4,6], "odd_powers": [], "only_even": true},
  "12": {"even_powers": [2,4,6], "odd_powers": [1,3,5,7], "only_even": false},
  "21": {"even_powers": [2,4,6], "odd_powers": [1,3,5,7], "only_even": false},
  "22": {"even_powers": [0,2,4,6], "odd_powers": [], "only_even": true}
}
"z5_source_derivatives": ["r2", "r4", "r6"]
"z5_not_from_odd_derivative_r7": true
```

The same output records the finite \([z^5]\) support:

```text
"z5_support": {
  "11": {},
  "12": {"r2": ["q0*q2","q0^4"], "r4": ["q0^2"], "r6": ["1"]},
  "21": {"r2": ["q0*q2","q0^4"], "r4": ["q0^2"], "r6": ["1"]},
  "22": {}
}
```

In the script normalization \(Q=1\) with harmless \(\pi\)-scaling suppressed,
the coefficient is
\[
[z^5]M_{12}
=-\frac1{96}q_0q_2r_2-\frac1{640}q_0^2r_4
+\frac1{96}q_0^4r_2+\frac1{53760}r_6,
\]
and \([z^5]M_{21}=-[z^5]M_{12}\).

**Source-derivative characterization.**  For a pure scalar Taylor source
piece of derivative order \(k\), if \(k\) is odd then \(\eta=0\) and
\(d_-+d_+=0\), so all \(M\)-powers contributed by that source derivative are
even.  If \(k\) is even, diagonal contributions remain even, while
off-diagonal antisymmetric contributions can be odd.  This matches the finite
audit through \(z^7\).

**Consequence for \(L_1YR_1\).**  The pure homogeneous candidate
\(\operatorname{Gr}_5r=r^{(7)}(m)(t-m)^7/7!\) cannot produce
\([z^5]M_i^{[5]}\).  If \([z^5]M_i^{[5]}\) is to be nonzero, the grade-five
mixed source projection must involve even derivative data \(r^{(2)},r^{(4)}\),
and/or \(r^{(6)}\), or a different non-homogeneous projection.  The obstruction
is source parity, not baseline \(q_0\) specialization.

# Baseline / delta

Baseline: the \(L_1YR_1\) prototype found that the homogeneous
\(r^{(7)}\)-only candidate gives \([z^5]M^{[5]}=0\), but it left open whether
the mixed input might generally have only even powers or whether other source
derivatives could populate \([z^5]M\).

Delta: this pass proves the exact parity structure.  \(M\) is not even-only;
odd powers exist in the off-diagonal antisymmetric channel.  However, odd
source derivatives cannot produce those odd powers.  The specific \(z^5\) slot
is source-supported only by \(r^{(2)},r^{(4)},r^{(6)}\) through the finite range
needed for UV-026.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - current UV-026 frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-026 source-table and parity-corrected grade subtargets.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-001243-gap-closer-UV026-L1YR1-mixed-order-prototype/report.md`
  - prior homogeneous candidate obstruction.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2627` - source variables
  \(d,e,g,\eta\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787` - exact mixed formula
  and source-linear expansion.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - \(L_1YR_1\)
  coefficient gate.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/notes/mixed-parity-theorem.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260425-002114-gap-closer-UV026-mixed-parity-theorem/scripts/mixed_parity_audit.py`.
- Current commit named in prompt: `cf168f0 capture UV-026 L1YR1 prototype`.

# Dependencies

- Stage 0 normalization: ordinary \(z\), tags retained, pre-\(\Phi_K\),
  \(M_i^{[a]}=\operatorname{Gr}_a(\mathfrak D_Q\delta N_i^{\lin})\).
- A revised scalar grade theorem specifying whether \(M_i^{[5]}\) is allowed
  to draw from even derivative data \(r^{(2)},r^{(4)},r^{(6)}\).
- Baseline \(q_0(m)\) and \(q_0''(m)\) if the explicit \([z^5]M\) coefficient
  is used downstream.
- Downstream inverse-square-root Frechet tables for the \(\Lambda\) factors.

# Strongest objection

The finite audit proves the parity and support of the full source-linear
mixed input, not the UV-026 grade projection.  It shows where \([z^5]M\) can
come from, but a source theorem must still say whether those even-derivative
terms belong to \(M_i^{[5]}\) rather than grade \(0,2,4\), a baseline shadow,
or a different family.

# Needed for promotion

To advance \(L_1YR_1\), supply one of:

1. A parity-corrected scalar grade theorem defining \(M_i^{[5]}\) so that its
   \([z^5]\) coefficient is the off-diagonal antisymmetric combination of
   \(r_i^{(2)},r_i^{(4)},r_i^{(6)}\) displayed above.
2. A theorem that \(M_i^{[5]}\) is zero at \([z^5]\), so the \(L_1YR_1\)
   family is absent from \(B_7\) and the seven-family inventory must be
   adjusted.
3. A different source-grade convention that gives a nonzero \([z^5]M_i^{[5]}\)
   and remains compatible with the same-point \(\Lambda^{[1]}\) inputs.

After such a convention is fixed, compute the leading \(\Lambda\)-tables from
the baseline constant same-point block and test the fixed-sector products.

# Autoresearch next step

continue: test option 1 by defining a parity-corrected \(M_i^{[5]}\) from the
explicit \([z^5]\) off-diagonal source combination, then check whether the
same source-grade convention can also define \(\delta G_{i,\pm}^{\lin,[5]}\)
without reintroducing the rejected \(q^{(5)}/X_3\) or \(q^{(7)}/X_5\) shortcut.

# Ledger destination

`findings.md`, `uv.md`, and `attempts.md`: record as `keep`.  This is a
source/formula parity theorem for the mixed input and a sharp UV-026 blocker:
\([z^5]M\) is possible, but only from even source derivatives, not from the
homogeneous \(r^{(7)}\) grade-five candidate.
