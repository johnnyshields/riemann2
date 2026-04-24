# Claim

Option 2: dependency graph. The current paper does not give a theorem-ready
actual exceptional-divisor quotient class \([R]\). It gives a finite-delta
algebraic placeholder for \(R\) once the septic quotient defect
\(\overline E_{12}^{(7;1)}\) is already available:
\[
[R]_{\mathrm{fin}}
:=
-a_1^{-1}\overline E_{12}^{(7;1)}
\in \mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}.
\]
This is the class represented by \(R\) in
`proof_of_rh.tex:11625-11638`.

The minimal source definition that could produce the C-needed
exceptional-divisor object, without assuming diagonal merger, is a septic
quotient edge law:
\[
\overline E_{12}^{(7;1)}(m,\omega,\delta)
=
\delta^2\,\mathcal H_7^q(m,\kappa,\delta^2),
\qquad
\kappa=2\omega/\delta,
\]
with \(\mathcal H_7^q\) valued in a specified midpoint quotient
\(\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)\) or in the \(h_1\)-quotient plus
an explicit analytic trivialization to the midpoint quotient. Then
\[
[R]_{\mathrm{edge}}(m,\kappa)
:=
-a_1(0)^{-1}\mathcal H_7^q(m,\kappa,0)
\]
is the actual exceptional-divisor quotient class. This definition requires an
actual corrected order-\(7\) quotient-defect package and edge-law extension. It
does not require diagonal merger. The paper currently has this edge-law template
only for cubic and quintic defects, not for the septic quotient defect.

# Status

open

# Evidence

[confirmed] The quantitative defect-thickened theorem defines \(R\) only
relative to an already-written septic quotient defect:
\[
a_1[A_{7,1}^{\mathfrak f}]+a_2[A_{7,2}^{\mathfrak f}]
+\overline E_{12}^{(7;1)}=0
\quad\text{in}\quad
\mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}.
\]
It then chooses \(R\) as a representative of
\(-a_1^{-1}\overline E_{12}^{(7;1)}\), and proves only that
\(\det(R,A_{5,1}^{\mathfrak f})\) is independent of adding
\(\xi A_{5,1}^{\mathfrak f}\). This gives a finite-delta quotient class if
\(\overline E_{12}^{(7;1)}\) exists. It does not construct that defect from the
actual corrected two-atom package, nor does it give an exceptional-divisor edge
coefficient. Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:11603`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:11611`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:11625`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:11768`.

[conditional] The finite-order source route at `11994-12040` supplies the right
ambient target:
\[
\mathbf C\oplus\mathfrak f\oplus
(\mathfrak f/\mathbf C A_5^{\mathfrak f}).
\]
If an actual corrected two-pair finite-order package through order \(7\) exists
in that target, then its interaction remainder defines
\(\overline E_{12}^{(7;1)}\), hence \([R]_{\mathrm{fin}}\). But the corollary
imports the three hypotheses of Lemma
`minimal-source-level-two-point-criterion`, including diagonal merger. It proves
only the estimate \(\overline E_{12}^{(7;1)}=O(\delta^2)\), not the edge
coefficient \(\mathcal H_7^q(m,\kappa,0)\). Refs:
`C:/workspace/riemann2/rh/proof_of_rh.tex:11996`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12000`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12004`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12016`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12035`.

[negative] The quotient-diagonal route at `12042-12166` cannot define \([R]\).
It assumes a full actual corrected two-atom quotient map
\(\mathcal F_2\in\Qabs[[z^2]]\), continuity, diagonal collapse, and
precompactness. It does not extract the finite-order cubic/quintic/septic source
package, does not define \(\overline E_{12}^{(7;1)}\), and the follow-up remark
says this route does not produce the quantitative defect estimates used in the
defect-thickened theorem. Refs:
`C:/workspace/riemann2/rh/proof_of_rh.tex:12048`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12059`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12139`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12163`.

[candidate] The collision-cancellation / edge-law WIP is the right place to
define the exceptional-divisor class. It introduces
\[
m=(h_1+h_2)/2,\quad \delta=h_2-h_1,\quad
\omega=(\lambda-1)/(\lambda+1),\quad \kappa=2\omega/\delta,
\]
and observes that an analytic, swap-even, collision-vanishing defect has the
form \(E=\delta^2\mathcal H(m,\kappa,\delta^2)\). It then displays edge laws for
\(E_{12}^{(3)}\) and \(E_{12}^{(5)}\). No corresponding edge law is stated for
\(\overline E_{12}^{(7;1)}\). Refs:
`C:/workspace/riemann2/rh/proof_of_rh.tex:12385`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12452`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12463`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12477`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12513`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12552`,
`C:/workspace/riemann2/rh/proof_of_rh.tex:12576`.

[confirmed] The fresh sibling reports support this dependency graph. The
gap-closer proves that \([R]\mapsto\det(R,A_5^{\mathfrak f})\) is an isomorphism
on \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\) when
\(A_5^{\mathfrak f}\neq0\), so defining \([R]\) is exactly the determinant-slot
problem. Source and adversarial verifiers agree that representative
independence is not state-locality, and that no current source computes or
constrains \(R\) on the exceptional divisor. Refs:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report.md:5`,
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report.md:148`,
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-source-C-R-channel/report.md:75`,
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/report.md:8`.

Dependency graph for \([R]_{\mathrm{edge}}\):

1. **Actual finite-order source package through order \(7\).** Needed to define
   the cubic/quintic/septic interaction defects before any diagonal statement.
   Current status: conditional/schema only.
2. **Septic quotient output.** The package must include a quotient-septic
   component in \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\), with an explicit
   convention for whether the quotient line is based at \(h_1\), \(h_2\), or the
   midpoint \(m\). Current status: finite-delta notation exists only once
   \(\overline E_{12}^{(7;1)}\) is assumed.
3. **Collision-chart analytic trivialization.** To pass to the exceptional
   divisor, the moving quotient
   \(\mathfrak f/\mathbf C A_5^{\mathfrak f}(h_1)\) must be analytically
   identified with a fixed midpoint quotient
   \(\mathfrak f/\mathbf C A_5^{\mathfrak f}(m)\), at least on
   \(A_5^{\mathfrak f}\neq0\). Current status: not defined.
4. **Septic quotient edge law.** Prove
   \[
   \overline E_{12}^{(7;1)}
   =\delta^2\mathcal H_7^q(m,\kappa,\delta^2).
   \]
   Current status: missing. The draft gives only the cubic/quintic edge-law
   template.
5. **Definition of \([R]_{\mathrm{edge}}\).** Once 1-4 exist, set
   \[
   [R]_{\mathrm{edge}}(m,\kappa)
   =-a_1(0)^{-1}\mathcal H_7^q(m,\kappa,0).
   \]
   Current status: available as a proposed conditional definition, not as a
   paper-defined object.
6. **State-locality/descent.** Prove \([R]_{\mathrm{edge}}\) factors through the
   descended collision state and excludes the \(R_\kappa\) deformation. Current
   status: missing and downstream of the definition.
7. **Diagonal-merger normalization.** Prove the descended value gives
   \(\widehat\Psi(m)\). Current status: missing and downstream of
   state-locality.

# Baseline / delta

Baseline: my previous report said the actual fixed C package is still a schema
and identified determinant descent/control for \(R\) as the next target. The
fresh gap-closer and verifier reports sharpened that: on
\(A_5^{\mathfrak f}\neq0\), controlling \(\det(R,A_5^{\mathfrak f})\) is exactly
controlling the quotient class \([R]\).

Delta: this follow-up separates finite-delta \([R]_{\mathrm{fin}}\) from the
exceptional-divisor class \([R]_{\mathrm{edge}}\). The conditional package
route can define the finite-delta class only after promoting an actual
finite-order source package; the quotient-diagonal route is too coarse; and the
edge-law/WIP material gives the correct chart but lacks the septic quotient edge
law. The first missing definition is therefore
\(\mathcal H_7^q\), the actual corrected order-\(7\) quotient-defect edge
package, plus the quotient-line trivialization.

# Attempt status

keep

# Exact refs

- `C:/workspace/riemann2/rh/proof_of_rh.tex:11603` - assumes cubic/quintic/septic
  quotient defects are already written.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11611` - finite-delta septic quotient
  defect equation.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11625` - representative \(R\) of
  \(-a_1^{-1}\overline E_{12}^{(7;1)}\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11768` - determinant
  representative-independence only.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888` - source criterion assumes an
  analytic package \(\mathfrak P_2\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11912` - diagonal merger is one of
  the source criterion hypotheses.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11996` - conditional actual
  corrected package through order \(7\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12000` - target
  \(\mathbf C\oplus\mathfrak f\oplus(\mathfrak f/\mathbf C A_5^{\mathfrak f})\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12016` - only an
  \(O(\delta^2)\) statement for the septic quotient defect.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12048` - quotient-diagonal route
  assumes actual \(\mathcal F_2\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12059` - quotient-diagonal route
  assumes diagonal collapse.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12139` - weaker route does not
  produce quantitative defect factorization.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12163` - neither route is proved.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385` - collision-cancellation
  chart.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12452` - edge-law template for an
  actual corrected defect.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12463` - blow-up slope \(\kappa\).
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12477` - cubic/quintic edge-law
  target only.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12513` - remaining two-pair fronts.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12552` - package theorem remains a
  conditional downstream program.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12576` - honest higher-order target
  is package-level coincidence/functoriality.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report.md:5` - determinant controls quotient class.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report.md:148` - next target is actual exceptional-divisor quotient class.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-source-C-R-channel/report.md:75` - source audit: \(R\) not computed on exceptional divisor.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/report.md:8` - pressure test for \(R_\kappa\).
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-explorer-C-actual-package-construction/report.md` - previous construction report.
- `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-explorer-C-actual-package-construction/notes/R-definition-dependency-map.md` - scratch dependency map for this follow-up.

# Dependencies

- Good collision chart with \(c\neq0\), \(a_1\neq0\), and for determinant
  reconstruction \(A_5^{\mathfrak f}\neq0\). The good-patch statements around
  `12385-12511` also use \(M\neq0\).
- A normalized amplitude gauge or explicit nonzero analytic \(a_1\) limit for
  the factor \(-a_1^{-1}\).
- A constructed actual corrected finite-order source package through order
  \(7\).
- A quotient-bundle convention/trivialization for
  \(\mathfrak f/\mathbf C A_5^{\mathfrak f}\) in the collision chart.
- A missing septic quotient edge law
  \(\overline E_{12}^{(7;1)}=\delta^2\mathcal H_7^q\).
- Later, but not part of definition: state-locality/descent for
  \([R]_{\mathrm{edge}}\) and diagonal-merger normalization.

# Strongest objection

The proposed \([R]_{\mathrm{edge}}\) definition assumes
\(\overline E_{12}^{(7;1)}\) vanishes to second order and has an analytic
edge coefficient. That is not currently proved for the septic quotient defect.
Requiring it may look close to diagonal merger, but it is weaker: it is an
edge-law/regularity definition for the quotient-defect class, not the assertion
that the edge class descends, is \(\kappa\)-independent, or equals the one-pair
value. The paper still has to promote this edge law before \([R]\) exists as an
actual exceptional-divisor object.

# Needed for promotion

1. Promote an actual corrected finite-order source package through order \(7\)
   with septic quotient output, without importing diagonal merger as a
   hypothesis.
2. Define the moving quotient line convention and its analytic trivialization in
   the collision chart.
3. Prove or state as the next theorem the septic quotient edge law
   \[
   \overline E_{12}^{(7;1)}
   =
   \delta^2\mathcal H_7^q(m,\kappa,\delta^2).
   \]
4. Define
   \([R]_{\mathrm{edge}}(m,\kappa)
   =-a_1(0)^{-1}\mathcal H_7^q(m,\kappa,0)\).
5. Only after that, attack state-locality/descent:
   \([R]_{\mathrm{edge}}\) factors through the descended collision state and
   excludes \(R_\kappa\).
6. Then prove diagonal-merger normalization to \(\widehat\Psi(m)\).

# Autoresearch next step

continue: formulate the missing septic quotient edge-law theorem precisely,
including the quotient-line trivialization from
\(\mathfrak f/\mathbf C A_{5,1}^{\mathfrak f}\) to the midpoint quotient. Then
test whether the actual corrected order-\(7\) formulas or the existing
quotient-septic closure give the required
\(\overline E_{12}^{(7;1)}=\delta^2\mathcal H_7^q\).

verify: source verifier should reject any proposed \([R]\) definition that uses
the quotient-diagonal route alone, since it does not define finite-order septic
defects; adversarial verifier should check that the definition does not already
assume state-locality or diagonal merger.

blocked: no process blocker. Mathematical blocker is the missing actual septic
quotient edge-law package \(\mathcal H_7^q\).

terminal: terminal for the subroute "current conditional package or
quotient-diagonal route already defines actual exceptional-divisor \([R]\)".
Not terminal for defining \([R]\) after promoting the septic quotient edge law.
