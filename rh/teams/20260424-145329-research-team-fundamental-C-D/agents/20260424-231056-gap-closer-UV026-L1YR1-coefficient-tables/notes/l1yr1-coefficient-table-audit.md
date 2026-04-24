# \(L_1YR_1\) Coefficient-Table Audit

## Target

The task was to find coefficient tables, not to restate the already-derived
Sylvester recurrence or the \(r+s+t=7\) convolution.  The needed positive input
is finite order-\(\le 7\) data in the same pre-\(\Phi_K\) normalization as
\[
B_7^{\mathfrak f}(T)=\pi_{\mathfrak f}[z^7]T.
\]

## Proved From Source

- The scaled perturbation variable for the mixed block is \(Y\), with
  \(\delta N=\mathfrak D_Q^{-1}Y\), from
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2429-2466`.
- The one-pair variables are explicitly
  \(X_{\rho,\pm}=\mathfrak D_Q(\delta G_{\rho,\pm})\) and
  \(Y_\rho=\mathfrak D_Q(\delta N_\rho)\), from
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2653-2664`.
- The paper gives exact same-point and mixed block formulas, then reduces the
  one-pair contribution only to linear-in-kernel expressions with bounded
  baseline coefficients; see
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2688-2784`.
- The live WIP target names
  \(\Lambda_{i,\pm}\) and \(M_i^{[5]}\), but explicitly states that the
  coefficient lists \([z^r]\Lambda_{i,\pm}\) and \([z^s]M_i^{[5]}\) are missing;
  see `C:/workspace/riemann2/rh/proof_of_rh.tex:12651-12713`.

## Conditional

The only normalization compatible with the transfer variables is
\[
M_i^{[5]}(z)=\operatorname{Gr}_5\bigl(\mathfrak D_Q\delta N_i^{\lin}\bigr)(z),
\]
not \(\operatorname{Gr}_5(\delta N_i^{\lin})\), unless a later theorem explicitly
overrides the symbol.  This matches the source-auditor formulation at
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-201525-source-auditor-UV026-L1YR1-matrix-provenance/report.md:163-169`.

## Missing

The coefficient-table source still needs:

- \(S_{\pm,r}=[z^r]G_\pm^{(0)}(z)^{1/2}\), \(0\le r\le 7\).
- \(B_{\pm,r}=[z^r]G_\pm^{(0)}(z)^{-1/2}\), \(0\le r\le 7\).
- \(H_{i,\pm,r}=[z^r]\delta G_{i,\pm}^{\lin}(z)\), \(i=1,2\), \(0\le r\le 7\),
  after the tagged one-atom kernels are fixed.
- \(M_{i,r}^{[5]}=[z^r]\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})(z)\),
  \(i=1,2\), \(0\le r\le 7\).
- \(A_5^{\mathfrak f}(m)=u_5I+v_5S\) in the same fixed-sector basis for the two
  determinant tests.

## Script Artifact

`scripts/l1yr1_table_contract.py` records a table schema and validates a future
coefficient-table JSON.  It also performs a source-window audit and rejects the
currently inspected ranges as containing no explicit finite order-\(\le 7\)
table block.

Run output:

- Script SHA1:
  `206663C05A1B307A06619137B3069CEB3D7D58BC`.
- Output file:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-231056-gap-closer-UV026-L1YR1-coefficient-tables/notes/l1yr1_table_contract_output.json`.
- Output SHA1:
  `F4579B9FF12A8B3EFAC558CC535739D904128871`.
- Key output: `table_block_found=false`, and all four finite-table checks for
  \(G_\pm^{(0)\pm1/2}\), \(\delta G_{i,\pm}^{\lin}\),
  \(M_i^{[5]}\), and \(\Lambda_{i,\pm}\) are false.

## Exact Missing Theorem

Finite-order normalized \(L_1YR_1\) coefficient-table theorem:

For the UV-025 tagged pre-whitening block \(\mathcal B_2\), in ordinary \(z\)
and before \(\Phi_K\), display matrices
\[
S_{\pm,r},\quad B_{\pm,r},\quad H_{i,\pm,r},\quad M_{i,r}^{[5]}
\qquad (i=1,2,\ 0\le r\le 7)
\]
such that
\[
G_\pm^{(0)}(z)^{1/2}=\sum_{r=0}^7S_{\pm,r}z^r+O(z^8),
\qquad
G_\pm^{(0)}(z)^{-1/2}=\sum_{r=0}^7B_{\pm,r}z^r+O(z^8),
\]
\[
\delta G_{i,\pm}^{\lin}(z)=\sum_{r=0}^7H_{i,\pm,r}z^r+O(z^8),
\qquad
M_i^{[5]}(z)=
\operatorname{Gr}_5(\mathfrak D_Q\delta N_i^{\lin})(z)
=\sum_{r=0}^7M_{i,r}^{[5]}z^r+O(z^8).
\]
With these data, the already-fixed Sylvester gate must produce
\(\Lambda_{i,\pm}^{[0]},\ldots,\Lambda_{i,\pm}^{[7]}\), and the two
pre-\(\Phi_K\) tag products must satisfy
\[
\pi_{\mathfrak f}[z^7]C_{112}^{L_1YR_1},\,
\pi_{\mathfrak f}[z^7]C_{122}^{L_1YR_1}
\in \mathbf C A_5^{\mathfrak f}(m).
\]
