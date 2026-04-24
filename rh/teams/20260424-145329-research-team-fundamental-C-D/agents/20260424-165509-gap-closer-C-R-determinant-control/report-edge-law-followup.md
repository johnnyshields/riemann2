# Follow-up report: septic edge law for \(R\)

## Claim

I do not prove actual-package descent for \([R](m,\kappa,0)\). I reduce the
edge-law target to the smallest concrete missing substatement and give a scoped
obstruction model.

If an actual order-7 corrected two-atom source package exists and satisfies the
minimal source criterion, then the septic quotient defect has a quadratic
interaction edge coefficient
\[
\mathfrak O_7(m,\kappa)
:=
\left[\mathcal J_2^{(7)}(a_1,a_2;m,m)\right]
\in
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m),
\]
where
\[
\mathcal I_2=a_1a_2(h_1-h_2)^2\mathcal J_2
\]
is the source-level interaction remainder. On \(A_5^{\mathfrak f}\neq0\), the
previous determinant report identifies this class with the scalar
\[
\det(\mathfrak O_7(m,\kappa),A_5^{\mathfrak f}(m)).
\]

The minimal positive theorem is therefore: compute the actual
\(\mathfrak O_7\), prove it factors through the descended collision state, and
prove its determinant is merger-normalized with no independent exceptional
slope/provenance dependence. The first obstruction term is precisely the
non-descended part of \(\mathfrak O_7(m,\kappa)\). The current draft does not
compute this term.

## Status

proved

This is a proved reduction and a scoped negative against deriving the septic
edge law from the current source axioms plus cubic/quintic edge laws alone. It
is not a proof or disproof of the actual corrected package.

## Evidence

The paper's WIP collision chart states a conditional edge-law target for the
actual corrected cubic/quintic defects:
\[
E_{12}^{(3)}=\delta^2\mathcal H_3(m,\kappa,\delta^2),
\qquad
E_{12}^{(5)}=\delta^2\mathcal H_5(m,\kappa,\delta^2),
\]
with edge values
\[
\mathcal H_3(m,\kappa,0)=c'(m)-\frac{\kappa}{2}c(m),
\qquad
\mathcal H_5(m,\kappa,0)=(A_5^{\mathfrak f})'(m)
-\frac{\kappa}{2}A_5^{\mathfrak f}(m).
\]
Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12511`.

For order 7, the source criterion gives only an abstract factorization. It
assumes an analytic finite-order package
\[
\mathfrak P_2(a_1,h_1;a_2,h_2)
\in
\mathbf C\oplus\mathfrak f\oplus
(\mathfrak f/\mathbf C A_5^{\mathfrak f})
\]
with swap symmetry, one-amplitude collapse, and diagonal merger, and proves
\[
\mathcal I_2=a_1a_2(h_1-h_2)^2\mathcal J_2.
\]
Refs: `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189`.

Thus a formal order-7 edge law would have the shape
\[
-a_1^{-1}\overline E_{12}^{(7;1)}
=
\delta^2\mathcal H_7(m,\kappa,\delta^2),
\]
with exceptional value determined by the septic quotient component of
\(\mathcal J_2\). The source theorem does not identify this component; it only
proves the \(\delta^2\) factor after the actual package hypotheses are supplied.

I tested the freedom by writing a finite model:
\[
\mathfrak P_2
=
a_1F(h_1)+a_2F(h_2)
+a_1a_2(h_1-h_2)^2(0,0,P(m,\kappa)),
\]
where \(P\) is an arbitrary septic quotient function. This model satisfies swap
symmetry, one-amplitude collapse, and diagonal merger. It changes only the
septic quotient edge coefficient, leaving cubic/quintic components unchanged.
With \(P(m,\kappa)=13+17\kappa+19m\), it gives a nonzero
\(\partial_\kappa\) obstruction.

Script:
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/scripts/septic_edge_obstruction_model.js`
(git object `83713d170276f9c788423db0f8c390d83030bffd`).

Output excerpt:

```text
swap_c_difference = 0
swap_a_difference = 0
swap_q_difference = 0
one_amplitude_c = -11.06
one_amplitude_a = -18.98
one_amplitude_q = -39.22
diagonal_c = -2.75
diagonal_a = -4.75
diagonal_q = -9.75
septic_interaction_over_delta2 = -723.0000000000025
edge_obstruction = a1*a2*(13 + 17*kappa + 19*m)
d_edge_obstruction_dkappa = -204
```

This realizes the pinned \(R_\kappa\) pressure test at the package level:
the free \(P(m,\kappa)\) term is exactly a quotient-defect edge contribution.
By the earlier determinant reduction, on \(A_5^{\mathfrak f}\neq0\) a nonzero
determinant of this class is the same obstruction as a nonzero quotient class.

Three-bin separation:

- proved: the minimal source criterion gives only the quadratic factorization
  and leaves the septic quotient component of \(\mathcal J_2\) free unless the
  actual package computes it.
- proved/computational: a finite package model can satisfy the source axioms and
  preserve lower components while adding an arbitrary \(\kappa\)-dependent
  septic quotient edge term.
- missing: no source line constructs the actual order-7 interaction Hessian
  \(\mathfrak O_7\), proves it descends to the collision state, or proves its
  determinant has zero independent exceptional slope/provenance derivative.

## Baseline / delta

Baseline: my prior report proved that on \(A_5^{\mathfrak f}\neq0\),
\(\det(R,A_5^{\mathfrak f})\) is exactly the one-dimensional quotient-defect
class. The sibling explorer/source/adversarial reports then confirmed that the
actual two-atom fixed C package is not constructed, and that representative
independence does not kill the \(R_\kappa\) determinant deformation.

Delta: this follow-up identifies the first order-7 edge obstruction as a named
source-level object:
\[
\mathfrak O_7=\left[\mathcal J_2^{(7)}\right]_{\delta=0}.
\]
The cubic/quintic edge-law package cannot determine this object. Even the
abstract source criterion cannot determine it; it permits an arbitrary septic
quotient quadratic interaction term. The next C target is therefore not a
generic "order-7 edge law", but the exact theorem
\[
\mathfrak O_7(m,\kappa)
\text{ descends and is merger-normalized.}
\]

## Attempt status

keep

## Exact refs

- Prior deposited report:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/report.md`.
- Prior note:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/notes/determinant-slot-reduction.md`.
- Current note:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/notes/septic-edge-law-obstruction.md`.
- Current script:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-gap-closer-C-R-determinant-control/scripts/septic_edge_obstruction_model.js`,
  git object `83713d170276f9c788423db0f8c390d83030bffd`.
- Fresh sibling report:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-explorer-C-actual-package-construction/report.md`.
- Fresh sibling report:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-source-C-R-channel/report.md`.
- Fresh sibling report:
  `C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-165509-verifier-adversarial-C-R-channel/report.md`.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:10780-10810` for the honest
  order-7 package target: same reduced image germ or collision-functoriality.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11587-11775` for \(R\) as a
  representative of \(-a_1^{-1}\overline E_{12}^{(7;1)}\) and for the
  determinant slot.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12189` for the minimal
  finite-order source criterion and the abstract quadratic interaction
  remainder.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12192-12255` for the naive
  source-summed obstruction and shear-blind quotient warning.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12511` for the
  collision-cancellation chart and cubic/quintic edge-law target.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:12513-12584` for the statement that
  the remaining order-7 burden is package-level/provenance-sensitive.
- `C:/workspace/riemann2/rh/proof_of_rh.tex:24520-24610` and
  `C:/workspace/riemann2/rh/proof_of_rh.tex:24990-25030` for the later summary
  separating finite-order source merger, quotient-diagonal closure, and package
  coincidence/functoriality.

## Dependencies

- The reduction uses the paper's conditional source criterion and its
  interaction remainder \(\mathcal J_2\).
- It uses the prior determinant-slot reduction on
  \(A_5^{\mathfrak f}\neq0\). The exceptional locus
  \(A_5^{\mathfrak f}=0\) remains outside this reduction.
- The obstruction model is formal. It shows independence from the current
  source axioms and lower edge laws, not realizability by the actual corrected
  block formulas.
- The conclusion depends on the current absence of an actual constructed
  order-7 two-atom package and of a formula for \(\mathcal J_2^{(7)}\).

## Strongest objection

The formal \(P(m,\kappa)\) model may not be realizable by the actual corrected
two-atom package. A real construction could force \(P\) to be a descended
collision-state function, could set its \(\kappa\)-slope to zero on the relevant
fiber, or could identify it with the merger-normalized one-pair value. That is
exactly the missing theorem. This report only proves that the current source
criterion and cubic/quintic edge laws do not force such a result.

## Needed for promotion

1. Construct the actual order-7 corrected two-atom source package in
   \[
   \mathbf C\oplus\mathfrak f\oplus
   (\mathfrak f/\mathbf C A_5^{\mathfrak f})
   \]
   on the collision-cancellation chart.
2. Identify the quotient-septic component of the quadratic interaction Hessian:
   \[
   \mathfrak O_7(m,\kappa)=
   \left[\mathcal J_2^{(7)}(a_1,a_2;m,m)\right].
   \]
3. Prove \(\mathfrak O_7(m,\kappa)\) factors through the descended collision
   state. If the descended state is represented by lower edge data, the theorem
   must say explicitly which lower data determine \(\mathfrak O_7\).
4. Prove determinant fiber constancy:
   \[
   \partial_\kappa
   \det(\mathfrak O_7(m,\kappa),A_5^{\mathfrak f}(m))=0
   \]
   along any fixed descended state / provenance fiber relevant to C.
5. Prove merger normalization to the one-pair quotient-septic value.
6. Verify against the formal septic interaction
   \(a_1a_2\delta^2P(m,\kappa)\) and against the prior \(R_\kappa\) determinant
   pressure test.

## Autoresearch next step

continue: source-mine the actual corrected block formulas for the order-7
quadratic interaction Hessian \(\mathcal J_2^{(7)}\). If the actual Hessian is
not available, formulate the paper-ready UV as: prove the septic quotient
Hessian \(\mathfrak O_7\) descends to the collision state and is
merger-normalized.

verify: adversarial verification should test any proposed edge law by adding
\(a_1a_2\delta^2P(m,\kappa)\) in the septic quotient coordinate. Source
verification should require the exact actual formula or theorem that forbids
this addition.

blocked: no process blocker. Mathematical blocker is missing actual computation
or descent theorem for \(\mathcal J_2^{(7)}\).

terminal: terminal for the subroute "cubic/quintic edge laws plus the abstract
source criterion determine the septic edge coefficient." They do not. Not
terminal for an actual-package proof of septic descent.
