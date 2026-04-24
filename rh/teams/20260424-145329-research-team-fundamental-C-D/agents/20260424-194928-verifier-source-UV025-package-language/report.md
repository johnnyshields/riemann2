# Claim

The existing "actual corrected two-pair finite-order package" language does not
already supply the UV-025 pre-whitening source block
`\mathcal B_2`.  It assumes quotient-output data
`\mathfrak P_2(a_1,h_1;a_2,h_2)` valued in
`\mathbf C\oplus\mathfrak f\oplus(\mathfrak f/\mathbf C A_5^{\mathfrak f})`
and states output-level source identities.  It does not define the actual
two-atom corrected block triple with source tags, nor prove the
pair-kernel-linear identity
`\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=a_1L_{h_1}+a_2L_{h_2}`.

# Status

open

# Evidence

Three-bin separation:

- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415`
  defines corrected same-point and mixed blocks and the corrected whitened
  matrix object
  `G_{m,-}^{\corr}(s)^{-1/2}N_m^{\corr}(s)G_{m,+}^{\corr}(s)^{-1/2}`.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:1569-1575`
  names the analytic whitening map
  `\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2}`.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732`
  writes one corrected finite-`s` triple as baseline plus perturbations
  `(R_-,\widetilde R,R_+)` and expands the matrix whitening up to a quadratic
  error.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799`
  gives the matrix Frechet derivative of whitening at the baseline.
- **Proved from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787`
  gives one-pair scaled perturbations
  `\mathfrak D_Q(\delta G_{\rho,\pm})`,
  `\mathfrak D_Q(\delta N_\rho)` and proves one-pair pair-kernel linearity
  modulo terms containing at least two pair kernels.
- **Conditional/output-level from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11474`
  defines only a schematic quotient odd-germ decomposition
  `F_{(a_1,h_1;a_2,h_2)}=a_1F_{h_1}+a_2F_{h_2}+\mathcal I_{12}`.  It says
  finite-order projections of the interaction are quadratic/divisible, but it
  does not define a pre-whitening two-atom block.
- **Conditional/output-level from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11616`
  assumes cubic, quintic, and septic quotient defects.  It starts from extracted
  output identities, not from source-tagged block data.
- **Conditional/output-level from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:11994-12009`
  assumes that the actual corrected two-pair finite-order package through order
  7 admits a source-level realization
  `\mathfrak P_2\in\mathbf C\oplus\mathfrak f\oplus
  (\mathfrak f/\mathbf C A_5^{\mathfrak f})`, with
  `F_h=(c(h),A_5^{\mathfrak f}(h),[A_7^{\mathfrak f}](h))`.  This is precisely
  quotient-output package language.
- **Conditional/output-level from source:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12189`
  says the remaining two-point issue is verification of swap symmetry,
  one-amplitude collapse, and diagonal merger for the corrected two-atom
  package.  It does not provide the package's pre-whitening construction.
- **Proved source negative:** `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227`
  rejects the naive source-summed whitened model: finite-order whitened
  coefficients are even analytic functions of the source weight, so a different
  lift/transport object is required.
- **Missing:** no inspected source line defines
  `\mathcal B_2(a_1,h_1;a_2,h_2)=
  (G_{2,-}^{\corr},N_2^{\corr},G_{2,+}^{\corr})`
  before whitening with source tags.
- **Missing:** no inspected source line defines the pair-kernel filtration
  `\mathcal K` for that two-atom block.
- **Missing:** no inspected source line proves
  `\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
  =a_1L_{h_1}+a_2L_{h_2}`.

No computational script was needed for this source-language audit.

# Baseline / delta

Baseline: the UV-024 actual-source-block pass reduced the matrix coefficient
problem to an upstream source object: define the actual two-atom pre-whitening
block `\mathcal B_2`, define its pair-kernel filtration, and prove its
linearized scaled derivative is `a_1L_{h_1}+a_2L_{h_2}`.

Delta: this verifier confirms the reduction.  The existing paper wording can
be reused for the quotient-output package `\mathfrak P_2` and for its desired
formal identities, but it cannot be treated as a definition of
`\mathcal B_2`.  The missing piece is not only a wording patch: defining
`\mathcal B_2` is a paper definition addition, while proving the
`\operatorname{Lin}_{\mathcal K}` identity requires new source computation for
the actual two-atom corrected block.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/references/agents/_autoresearch.md` - read
  before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - current UV-023/UV-024/UV-025 frontier.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md`
  - UV-025 entry.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415` - corrected blocks and
  holomorphic matrix whitening.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1569-1575` - analytic whitening
  map.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732` - baseline plus
  perturbation notation for one corrected triple.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799` - matrix Frechet
  derivative.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787` - one-pair
  pair-kernel-linear scaled block perturbation.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11459-11474` - schematic two-pair
  quotient odd-germ decomposition.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11616` - defect theorem
  assumes output-level quotient defects.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11994-12009` - assumed
  source-level realization of the quotient-output package.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12168-12189` - exact remaining
  output-level source identities.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12227` - even-amplitude
  obstruction for naive source-summed whitened coefficients.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-194309-gap-closer-UV024-actual-source-block/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-verifier-source-UV024-prePhi-coefficient/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-193725-gap-closer-UV024-matrix-cross-effect/report.md`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-194928-verifier-source-UV025-package-language/notes/source-language-map.md`.

# Dependencies

- A new definition of the actual source-tagged two-atom corrected
  pre-whitening block triple `\mathcal B_2`.
- A pair-kernel filtration `\mathcal K` on that block, compatible with the
  one-pair kernels appearing in `proof_of_rh.tex:2659-2787`.
- A source computation proving the pair-kernel-linear derivative identity.
- A theorem that the quotient-output package `\mathfrak P_2` is induced by
  `\mathcal B_2` after whitening and coefficient extraction, rather than
  assumed independently.

# Strongest objection

The phrase "actual corrected two-pair finite-order package through order 7
admits a source-level realization" at `proof_of_rh.tex:11996-11999` sounds
close to UV-025.  But the codomain displayed immediately after it is
`\mathbf C\oplus\mathfrak f\oplus
(\mathfrak f/\mathbf C A_5^{\mathfrak f})`, so the object is already an
extracted cubic/quintic/septic quotient-output package.  It has no block
components `G_-`, `N`, `G_+`, no pre-whitening source tags, and no
pair-kernel filtration.

# Needed for promotion

1. Add a definition block for
   `\mathcal B_2(a_1,h_1;a_2,h_2)` as a corrected pre-whitening block triple
   with source tags.
2. Define `\mathcal K` and
   `\operatorname{Lin}_{\mathcal K}` on that block.
3. Define `L_h` using the one-pair pair-kernel-linear derivative supported by
   `proof_of_rh.tex:2659-2787`.
4. Prove, by actual source/block expansion, that
   `\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
   =a_1L_{h_1}+a_2L_{h_2}`.
5. Only after that, define or verify the quotient-output package
   `\mathfrak P_2` as induced by `\mathcal B_2`, and then feed UV-024.

# Autoresearch next step

continue: draft the minimal source-definition skeleton for `\mathcal B_2` using
the existing block names `G_\pm^{\corr}`, `N^{\corr}`, perturbation notation
`R_\pm,\widetilde R`, and the one-pair scaled perturbations
`\mathfrak D_Q(\delta G_{\rho,\pm})`, `\mathfrak D_Q(\delta N_\rho)`.
Keep the skeleton separate from the linearization theorem.

verify: after the skeleton exists, source-check the actual two-atom block
formulas against the equality
`\operatorname{Lin}_{\mathcal K}\mathfrak D_Q(\mathcal B_2-\mathcal B_0)
=a_1L_{h_1}+a_2L_{h_2}`.  Do not accept quotient-output assumptions as a
pre-whitening proof.

blocked: no process blocker.  Mathematical blocker is the missing actual
two-atom block expansion and its pair-kernel-linear computation.

terminal: terminal for treating the current `\mathfrak P_2` quotient-output
language as already defining `\mathcal B_2`.  Not terminal for adding
`\mathcal B_2` as an upstream definition and proving the derivative theorem.

Honest verdict: UV-025 is not closed by existing package language.  The draft
has reusable output-package phrasing, but the pre-whitening source block is
still missing.

# Ledger destination

attempts.md - record this as a kept source verification of UV-025's boundary;
uv.md remains appropriate as-is unless the coordinator splits the definition
addition from the derivative theorem into separate UVs.
