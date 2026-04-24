# UV-023 Adversarial Projection Map

Assigned lane: `verifier-adversarial-UV023-projection`.

## Source bins

- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2415-2587` defines the
  analytic corrected-whitening transfer, `\mathfrak D_Q`, the homogeneous
  expansion `\mathcal T_{Q,R}(X)=\sum_{p\ge1}\mathcal T_p(X)`, and coefficient
  bounds. This is not a source-bidegree theorem.
- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:2659-2787` gives adjacent
  actual one-pair weighted inputs and formula-level `\mathfrak D_Q`
  bookkeeping. Some weighted entries have no forced positive `w`-order.
- Proved: `C:/workspace/riemann2/rh/proof_of_rh.tex:7742-8033` closes the
  one-pair quotient-septic class and determinant after fixed-sector projection.
  It does not define the two-atom corrected-whitening cross-effect or a
  source-bidegree projector.
- Conditional: `C:/workspace/riemann2/rh/proof_of_rh.tex:11888-12255` gives
  quadratic factorization only after swap symmetry, exact one-amplitude
  collapse, and diagonal merger are supplied for an actual package; it also
  rules out the naive source-summed whitened coefficients and warns that
  quotient/determinant-only routes are shear-blind.
- Conditional: `C:/workspace/riemann2/rh/proof_of_rh.tex:12385-12584` gives the
  collision chart and edge law only for an actual analytic, swap-even,
  collision-vanishing defect.
- Target-only: `C:/workspace/riemann2/rh/proof_of_rh.tex:10790-10810`,
  `21293-21330`, and `23072-23109` present same-reduced-image,
  collision-functoriality, or package-level collapse as remaining theorem
  targets.

## Adversarial checks

The formal bidegree idea works only under all four hidden inputs:

1. `X^{[1]}` is an actual source-weight-linear corrected-block perturbation.
2. `\Pi_{1,1}` is defined on the source-tagged object before quotient
   extraction.
3. `Q_7^q` is a fixed-target order-7 quotient extraction before determinant
   scalarization.
4. `Q_7^q(C)=Q_7^q(\Pi_{1,1}C)` is proved.

The harness
`C:/workspace/riemann2/rh/teams/20260424-145329-research-team-fundamental-C-D/agents/20260424-191517-verifier-adversarial-UV023-projection/scripts/uv023_projection_adversarial_check.py`
separates the failure modes:

- pre-quotient `(1,1)` projection keeps the quadratic transfer and kills
  formal `p>=3` cross-effect terms;
- determinant scalarization loses source tags, so a post-hoc projection is not
  well-defined;
- a nonlinear quotient/scalar extraction need not commute with projection;
- finite-order grading alone permits a cubic `(1,1,5)` septic witness;
- diagonal value zero does not imply `\delta^2` divisibility because the first
  collision derivative can survive.

## Smallest missing object

The smallest missing object is not just `\Pi_{1,1}`. It is the complete
source-bidegree quotient-compatibility package:

\[
X^{[1]},\quad \Pi_{1,1},\quad Q_7^q,\quad
Q_7^q(C)=Q_7^q(\Pi_{1,1}C).
\]

If forced to choose one theorem statement, make it:

**Source-bidegree quotient-compatibility lemma.** For the actual
source-weight-linear corrected-block input `X^{[1]}` and corrected-whitening
cross-effect `C`, the fixed-target septic quotient extraction satisfies
`Q_7^q((1-\Pi_{1,1})C)=0`. Equivalently, every non-`(1,1)` source bidegree is
quotient-invisible through order 7.
