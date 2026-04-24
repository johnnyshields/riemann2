# Claim

At the pre-\(\Phi_K\) matrix/fixed-sector level, the cubic families
\[
L_2YR_0,\qquad L_0YR_2
\]
are not classified by the current source as source-trivial, one-pair \(K_5\),
one-pair \(K_3\), or pure same-point sectors.  They reduce to an exact missing
second-Frechet inverse-square-root coefficient theorem coupled to the
grade-one/grade-five source-linear mixed input.

Matrix convention: write
\[
\mathcal W(G_-,N,G_+)=G_-^{-1/2}NG_+^{-1/2},
\]
\[
L=G_-^{(0)-1/2}+L_1+L_2+\cdots,\qquad
R=G_+^{(0)-1/2}+R_1+R_2+\cdots,\qquad N=N_0+Y,
\]
all before \(\Phi_K\).  The fixed-sector projection is
\[
\pi_{\mathfrak f}(A)=\frac12(A+J_0AJ_0),\qquad
\mathfrak f=\operatorname{span}\{I,S\}.
\]
The right family is the endpoint-swapped analogue of the left family under
\(z\mapsto -z\), \(-\leftrightarrow+\), with the ordered product \(LNR\) kept
at matrix level.

For \(L_2YR_0\), define
\[
\mathcal L_{-,ab}^{\{p,q\}}
\]
to be the tag-\(ab\), finite-grade multiset \(\{p,q\}\) part of
\[
\frac12D^2(G_-^{(0)}(z)^{-1/2})[\delta G_-(z),\delta G_-(z)].
\]
The braces include both ordered grade placements when \(p\neq q\).  With
\(R_0=G_+^{(0)-1/2}\), the missing \(112\) coefficient theorem is
\[
C_{112}^{L_2YR_0}
:=\pi_{\mathfrak f}[z^7]\Bigl(
\bigl(
\mathcal L_{-,11}^{\{1,1\}}M_2^{[5]}
+\mathcal L_{-,11}^{\{1,5\}}M_2^{[1]}
+\mathcal L_{-,12}^{\{1,1\}}M_1^{[5]}
+\mathcal L_{-,12}^{\{1,5\}}M_1^{[1]}
\bigr)R_0
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m),
\]
with the tag-swapped \(122\) statement
\[
C_{122}^{L_2YR_0}
:=\pi_{\mathfrak f}[z^7]\Bigl(
\bigl(
\mathcal L_{-,22}^{\{1,1\}}M_1^{[5]}
+\mathcal L_{-,22}^{\{1,5\}}M_1^{[1]}
+\mathcal L_{-,12}^{\{1,1\}}M_2^{[5]}
+\mathcal L_{-,12}^{\{1,5\}}M_2^{[1]}
\bigr)R_0
\Bigr)
\in \mathbf C A_5^{\mathfrak f}(m).
\]
For \(L_0YR_2\), the same theorem is required with the analogous
\(\mathcal R_{+,ab}^{\{p,q\}}\) second-Frechet outputs on the right and
left multiplication by \(L_0=G_-^{(0)-1/2}\).

# Status

open

# Evidence

Separate three things: proved / conditional / missing.

- **Proved from source:** corrected whitening is the matrix object
  \(G_-^{-1/2}NG_+^{-1/2}\) before \(\Phi_K\); see
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-1415` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1569-1575`.
- **Proved from source:** the whitening map has a homogeneous analytic
  expansion in the perturbation triple, while the displayed transfer estimate
  passes to \(\Phi_K\) only later; see
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1693-1732`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:1784-1799`, and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587`.
- **Proved from source:** the tagged pre-whitening source block is now
  canonical, keeps tags through \(\operatorname{Lin}_{\mathcal K}\), and states
  that \(B_7^{\mathfrak f}\), \(\Pi_{1,1}\), and the cubic
  \(A_5^{\mathfrak f}\)-gauge theorem remain separate obligations; see
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2797-2899`.
- **Proved from source:** the mixed input \(Y\) is a real source-linear mixed
  block, not a scalar or post-\(\Phi_K\) object.  The corrected mixed formula
  and its linear Taylor part are displayed at
  `C:/workspace/riemann2/rh/proof_of_rh.tex:2724-2787`.
- **Proved from source:** the fixed-sector line is
  \(A_5^{\mathfrak f}=u_5I+v_5S\), and the target membership test is
  \(u v_5-u_5 v=0\) for each fixed-sector vector \(uI+vS\); see
  `C:/workspace/riemann2/rh/proof_of_rh.tex:7057-7127` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714`.
- **Proved from source:** the one-pair \(K_5\) and \(K_3\) laws apply only
  after the actual term is identified with the displayed source classes
  \(c_2A_5+[B_2,A_5]\) or
  \(c_4A_3+[B_4,A_3]+c_2[B_2,A_3]+A_3B_2^2-B_2A_3B_2\); see
  `C:/workspace/riemann2/rh/proof_of_rh.tex:7297-7409`.
- **Proved from source boundary:** pure same-point parity kills terms with no
  ordered-pair transport factor.  \(L_2YR_0\) and \(L_0YR_2\) contain the
  actual mixed perturbation \(Y\), so they are not pure same-point by source
  class; see `C:/workspace/riemann2/rh/proof_of_rh.tex:7855-7906`.
- **Proved from prior reports:** the seven-family UV-026 inventory lists
  \(L_2YR_0\) and \(L_0YR_2\) as live cubic families, and the all-left report
  fixed the convention for matrix-level mirror use without scalarization.
- **Conditional:** if the missing second-Frechet output lists and
  \(M_i^{[1]},M_i^{[5]}\) mixed-input lists are supplied in the same
  \(B_7^{\mathfrak f}\) normalization, the formulas in the Claim give finite
  \(z^7\) checks for the \(112\) and \(122\) tag coefficients.
- **Missing:** no inspected source line identifies \(L_2YR_0\) or \(L_0YR_2\)
  with \(K_5\), \(K_3\), or pure same-point source classes.
- **Missing:** no inspected source line computes the four fixed-sector vectors
  \(C_{112}^{L_2YR_0}\), \(C_{122}^{L_2YR_0}\), \(C_{112}^{L_0YR_2}\), and
  \(C_{122}^{L_0YR_2}\), nor proves their determinant identities against
  \(A_5^{\mathfrak f}(m)\).

Computational/formal check:

- Script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-231056-explorer-UV026-next-cubic-L2YR0/scripts/l2yr0_formal_witness.py`.
- Script SHA1: `4F5A14BBD1517DA12F7978005E4311494FA7335E`.
- Relevant output:

```text
"second_inverse_sqrt_coefficient": "3/8 times AB+BA"
"mixed_input_Y_fixed_sector": ["3", "7"]
"L2YR0_fixed_sector": ["9/4", "21/4"]
"L0YR2_fixed_sector": ["9/4", "21/4"]
"A5_fixed_sector": ["2", "5"]
"det_L2YR0_against_A5": "3/4"
"det_L0YR2_against_A5": "3/4"
"algebra_forces_A5_gauge": false
```

Interpretation: at an identity baseline, the mixed second-order coefficient of
\((I+E)^{-1/2}\) is \(3(AB+BA)/8\).  Multiplication by a source-linear mixed
input can produce a fixed-sector vector not proportional to
\(A_5^{\mathfrak f}\).  This is not actual-package evidence; it only rejects
formal matrix algebra or source support as a shortcut proof.

# Baseline / delta

Baseline: the cubic-source inventory left all seven cubic families live unless
source-classified or directly proved \(A_5^{\mathfrak f}\)-gauge.  The
all-left/all-right report reduced \(L_3N_0R_0\) and \(L_0N_0R_3\) to
third-Frechet coefficient identities.  The parallel \(L_1YR_1\) lane reduced
that family to first-Frechet \(\Lambda\)-tables, \(M_i^{[5]}\), and finite
convolutions.

Delta: this pass classifies the second-Frechet-with-mixed-input families.  The
new exact theorem is smaller than a full seven-family theorem: it needs
second-Frechet source-tag coefficient lists
\(\mathcal L_{-,ab}^{\{1,1\}}\), \(\mathcal L_{-,ab}^{\{1,5\}}\) and their
right analogues, plus \(M_i^{[1]}\), \(M_i^{[5]}\), followed by four fixed-sector
determinant tests.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/.agents/skills/research-resume/SKILL.md` - read
  because the brief invoked `research-resume`.
- `C:/workspace/riemann2/.agents/agents/_autoresearch.md` - read before
  acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/findings.md`
  - read completely before acting.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md:55-68`
  - UV-026 entry.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/dispatch.md:858-910`
  - resume dispatch and ground-truth checks.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:1392-2048` - corrected whitening,
  matrix Frechet expansion, and Loewner boundary.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2324-2587` - scaled matrix gain,
  \(\mathfrak D_Q\), and homogeneous transfer.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:2607-2899` - source kernels,
  corrected same-point/mixed formulas, and tagged pre-whitening block.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:6976-7409` - fixed-sector target
  and \(K_5/K_3\) source classes.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:7742-8048` - pure same-point
  boundary and one-pair quotient-septic closure after source-class
  identification.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12617-12714` - UV-026
  matrix/fixed-sector target and \(L_1YR_1\) coefficient-gate model.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-225250-explorer-UV026-next-cubic-L3N0R0-v2/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-200220-gap-closer-UV026-cubic-source-terms/report.md`.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-225250-gap-closer-UV026-L1YR1-Lambda-M5-coefficients-v2/report.md`.
- Own notes:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-231056-explorer-UV026-next-cubic-L2YR0/notes/L2YR0-classification.md`.
- Own script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-231056-explorer-UV026-next-cubic-L2YR0/scripts/l2yr0_formal_witness.py`
  - SHA1 `4F5A14BBD1517DA12F7978005E4311494FA7335E`.

# Dependencies

- The tagged pre-whitening source block in the canonical draft.
- A normalization decision for \(M_i^{[1]}\) and \(M_i^{[5]}\) matching
  \(B_7^{\mathfrak f}\): raw \(\delta N\) versus scaled
  \(Y=\mathfrak D_Q(\delta N)\).
- Coefficient lists through order \(7\) for the baseline inverse square roots
  \(G_\pm^{(0)-1/2}\).
- Second-Frechet coefficient lists for the same-point inputs, separated by
  source tag and finite-grade multisets \(\{1,1\}\) and \(\{1,5\}\).
- Coefficient lists for the mixed inputs \(M_i^{[1]}\) and \(M_i^{[5]}\).
- Matching coordinates for \(A_5^{\mathfrak f}(m)=u_5I+v_5S\).

# Strongest objection

The formal witness uses identity baselines and freely chosen source directions,
so it does not prove an actual obstruction.  The real corrected two-atom
coefficients may cancel, or the exact term may turn out to be a one-pair
\(K_5\), one-pair \(K_3\), or another fixed-sector gauge source class after a
coefficient-level calculation.  Current source simply does not provide that
identification.

# Needed for promotion

Promotion of the \(L_2YR_0\) and \(L_0YR_2\) subfamilies needs one of:

1. A source-class theorem identifying the actual coefficients with the
   displayed \(K_5\), \(K_3\), or pure same-point classes, before applying
   \(\Phi_K\).
2. Direct coefficient data for
   \(C_{112}^{L_2YR_0}\), \(C_{122}^{L_2YR_0}\),
   \(C_{112}^{L_0YR_2}\), and \(C_{122}^{L_0YR_2}\), each written as \(uI+vS\)
   and satisfying
   \[
   uv_5-u_5v=0
   \]
   against \(A_5^{\mathfrak f}(m)=u_5I+v_5S\).

# Autoresearch next step

continue: derive a Sylvester/second-variation recurrence for the
second-Frechet outputs \(\mathcal L_{-,ab}^{\{1,1\}}\),
\(\mathcal L_{-,ab}^{\{1,5\}}\), \(\mathcal R_{+,ab}^{\{1,1\}}\), and
\(\mathcal R_{+,ab}^{\{1,5\}}\), then combine them with \(M_i^{[1]}\) and
\(M_i^{[5]}\) in the four displayed \(z^7\) fixed-sector tests.

verify: a source auditor should reject any proof that uses \(K_5/K_3\) or
pure-sector laws before identifying these actual matrix products with those
source classes.

blocked: no process blocker.  Mathematical blocker is the missing actual
second-Frechet coefficient theorem and mixed-input coefficient normalization.

terminal: terminal for proving these two families from source-support, scalar,
determinant, diagonal-merger, or unclassified one-pair laws alone.  Not
terminal for a direct coefficient computation.

Honest verdict: \(L_2YR_0\) and \(L_0YR_2\) remain open UV-026 subfamilies,
now reduced to a precise finite coefficient theorem.

# Ledger destination

uv.md and attempts.md - refine UV-026 with the second-Frechet-plus-mixed-input
coefficient subtarget, and record this route as `keep` because it classifies
the two families as a sharp missing theorem rather than a closed gauge or
source-trivial case.
