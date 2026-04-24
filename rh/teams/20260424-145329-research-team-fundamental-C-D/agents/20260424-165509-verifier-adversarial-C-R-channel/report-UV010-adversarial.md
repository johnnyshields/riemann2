# Adversarial verifier report: UV-010

## Claim

UV-010 is the cleanest immediate C-FS2/C-FS3 definition target if it is kept
narrow: construct the actual corrected order-\(7\) quotient-defect edge package
\[
\overline E_{12}^{(7;1)}
=
\delta^2\mathcal H_7^q(m,\kappa,\delta^2)
\]
with an analytic quotient-line trivialization to the midpoint quotient, without
asserting descent, \(\kappa\)-independence, or merger normalization. In that
narrow form it does not smuggle in diagonal merger or state-locality. It does
unavoidably include actual-package construction, because \(\mathcal H_7^q\) is
not a formal consequence of the current source axioms, the cubic/quintic edge
laws, or the finite-delta \(R\) notation.

The formal model
\[
\mathfrak P_2
=
a_1F(h_1)+a_2F(h_2)+a_1a_2\delta^2(0,0,P(m,\kappa))
\]
shows what a future positive proof must explicitly forbid or compute: an
arbitrary septic quotient Hessian term \(P(m,\kappa)\). Such a term can preserve
swap symmetry, one-amplitude collapse, diagonal merger, and all lower
cubic/quintic edge data while producing independent \(\kappa\)-dependence in the
order-\(7\) quotient edge.

## Status

proved

## Evidence

Three-bin separation:

- **proved:** The finite-delta theorem defines \(R\) only after a septic
  quotient defect has already been written:
  \[
  a_1[A_{7,1}^{\mathfrak f}]+a_2[A_{7,2}^{\mathfrak f}]
  +\overline E_{12}^{(7;1)}=0
  \quad \text{in} \quad
  \mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}.
  \]
  It then chooses \(R\) as a representative of
  \(-a_1^{-1}\overline E_{12}^{(7;1)}\). This is not an exceptional-divisor
  construction of \(\mathcal H_7^q\).
- **proved:** The current collision-cancellation WIP gives the right chart and
  cubic/quintic edge-law template, but it stops at \(E_{12}^{(3)}\) and
  \(E_{12}^{(5)}\). It does not state
  \(\overline E_{12}^{(7;1)}=\delta^2\mathcal H_7^q\).
- **proved:** The formal perturbation
  \(a_1a_2\delta^2(0,0,P(m,\kappa))\) is invisible to the lower components and
  vanishes on one-amplitude and diagonal loci. Therefore those conditions alone
  cannot determine or forbid the septic quotient edge term.
- **proved/computational:** I wrote and ran
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/scripts/uv010_formal_model_audit.js`.
  Output:

```text
swap_c_difference = 0
swap_f_difference = 0
swap_q_difference = 0
one_amplitude_c_difference = 0
one_amplitude_f_difference = 0
one_amplitude_q_difference = 0
diagonal_c_difference = 0
diagonal_f_difference = 0
diagonal_q_difference = 0
edge_over_delta2_difference = 0
lower_components_changed_by_P = false
edge_term = a1*a2*(13 + 17*kappa + 19*m)
d_edge_term_dkappa = -204
```

- **conditional:** If a future source construction gives the actual corrected
  order-\(7\) two-atom package and computes its quotient interaction Hessian,
  then \(\mathcal H_7^q\) becomes a legitimate object. If a later theorem proves
  that this object descends to the collision state and has merger-normalized
  determinant, then the \(R_\kappa\) obstruction is killed. These are separate
  downstream claims.
- **missing:** No current source supplies the actual order-\(7\) quotient edge
  package, the quotient-line trivialization, the actual formula for the septic
  quotient Hessian, or an identity forbidding the free \(P(m,\kappa)\) term.

Adversarial audit of possible smuggling:

- UV-010 does **not** smuggle diagonal merger if it asks only for construction of
  \(\mathcal H_7^q\). A statement that additionally asserts
  \(B(m,\kappa)=\widehat\Psi(m)\), \(\partial_\kappa B=0\), or determinant
  constancy is no longer UV-010; it has imported C-FS3.
- UV-010 does **not** smuggle state-locality if \(\mathcal H_7^q\) is allowed to
  depend on \(\kappa\) and provenance. A statement that says
  \(\mathcal H_7^q\) is determined by the descended collision state has imported
  the next theorem.
- UV-010 **does** contain actual-package construction. This is not avoidable:
  without the actual corrected order-\(7\) quotient defect and quotient-bundle
  convention, \(\mathcal H_7^q\) is only notation.

## Baseline / delta

Baseline: my previous report established the \(R_\kappa\) determinant pressure
test: changing the quotient-defect class by a term with
\(\det(R_\kappa,A_5^{\mathfrak f})=c^2\varepsilon\kappa\) shifts the reduced
third C coordinate by \(\varepsilon\kappa\). The explorer follow-up separated
finite-delta \([R]\) from the missing exceptional-divisor edge class and proposed
\(\mathcal H_7^q\) plus quotient-line trivialization as the first missing
definition. The gap-closer follow-up showed that lower edge laws and the
abstract source criterion leave a free order-\(7\) quotient Hessian.

Delta: this audit confirms UV-010 as the right next target only after stripping
off downstream conclusions. UV-010 should define the edge object; it should not
claim descent, determinant constancy, or one-pair identification. The formal
\(a_1a_2\delta^2P(m,\kappa)\) model is the adversarial acceptance test: any
positive proof must identify the actual formula or theorem that prevents this
term from being arbitrary.

## Attempt status

keep

## Exact refs

- UV entry:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/uv.md:19`.
- UV-010 collation frontier:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:327`,
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/collation.md:335`.
- Explorer follow-up:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-explorer-C-actual-package-construction/report-R-definition-followup.md:1`.
- Gap-closer follow-up:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report-edge-law-followup.md:1`.
- Gap-closer formal model script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/scripts/septic_edge_obstruction_model.js`.
- This audit script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/scripts/uv010_formal_model_audit.js`.
- Prior adversarial \(R_\kappa\) report:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/report.md`.
- Finite-delta \(R\) theorem:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11587`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11603`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11625`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11768`.
- Source criterion and diagonal merger as an assumption:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11888`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11912`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:11996`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12016`.
- Quotient-diagonal route too coarse for finite-order defects:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12042`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12139`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12163`.
- Collision chart and cubic/quintic edge-law template:
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12385`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12452`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12463`,
  `C:/workspace/riemann2/rh/proof_of_rh.tex:12477`.

## Dependencies

- Good collision chart and nondegenerate quotient line. The edge class needs an
  analytic convention for moving
  \(\mathfrak f/\mathbf C A_5^{\mathfrak f}(h_1)\) or
  \(\mathfrak f/\mathbf C A_5^{\mathfrak f}(h_2)\) to the midpoint quotient.
- A constructed actual corrected order-\(7\) two-atom source package. UV-010
  cannot be proved from the abstract source criterion alone, because that
  criterion either assumes merger or leaves the quotient Hessian arbitrary.
- A normalized nonzero amplitude convention for the factor
  \(-a_1^{-1}\) in \([R]_{\mathrm{edge}}\).
- No use of downstream state-locality or diagonal merger in the definition
  step. Those may be later dependencies for C closure, but they must not be
  hidden inside UV-010.

## Strongest objection

The formal \(P(m,\kappa)\) model is not an actual corrected-package
counterexample. The actual order-\(7\) corrected block formulas may force a
specific \(P\), may make it descended, or may cancel its determinant. But a
positive proof must show that from actual formulas or a named theorem. The
current formal axioms, lower edge laws, one-amplitude collapse, and diagonal
merger do not do it.

## Needed for promotion

No C promotion follows from UV-010 alone. To promote UV-010 as a definition
target, a future proof must provide:

1. The actual corrected finite-order source package through order \(7\), with
   a septic quotient output.
2. The moving quotient-line convention and analytic trivialization to
   \(\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)\).
3. The edge law
   \[
   \overline E_{12}^{(7;1)}
   =
   \delta^2\mathcal H_7^q(m,\kappa,\delta^2)
   \]
   in that fixed quotient.
4. The actual formula for, or theorem determining, the quotient Hessian
   represented by \(\mathcal H_7^q(m,\kappa,0)\).
5. An explicit explanation of why the arbitrary formal addition
   \(a_1a_2\delta^2P(m,\kappa)\) is not admissible for the actual package, or a
   clear admission that UV-010 only defines the object and leaves \(P\)'s
   \(\kappa\)-dependence for the next UV.
6. Only after UV-010: a separate state-locality/descent theorem and a separate
   diagonal-merger normalization theorem to close C-FS3.

## Autoresearch next step

continue: source-mine the actual corrected order-\(7\) formulas for the quotient
Hessian \(\mathcal H_7^q(m,\kappa,0)\), keeping the target purely definitional:
edge package plus quotient-line trivialization.

verify: reject any proposed UV-010 proof that proves \(\kappa\)-independence by
assuming diagonal merger, or proves descent by naming state-locality without an
actual formula. Test it against the formal
\(a_1a_2\delta^2P(m,\kappa)\) addition.

blocked: no process blocker. Mathematical blocker is the missing actual
order-\(7\) quotient edge package and quotient-bundle trivialization.

terminal: terminal for deriving UV-010 from lower cubic/quintic edge laws,
formal source axioms, or diagonal conditions alone. Not terminal for an
actual-package construction of \(\mathcal H_7^q\).
