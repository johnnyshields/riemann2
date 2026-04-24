# UV-010 Source-Language Map

## Best native terms

- Use the paper's existing phrase **septic quotient defect** for the finite-delta
  object. The exact notation is
  \[
  \overline E_{12}^{(7;1)}
  \in \mathfrak f/\mathbf C A_{5,1}^{\mathfrak f},
  \]
  from `rh/proof_of_rh.tex:11603-11615`.
- Use **representative \(R\)** only for the finite-delta lift of the quotient
  class
  \[
  -a_1^{-1}\overline E_{12}^{(7;1)}.
  \]
  The paper proves only representative independence of
  \(\det(R,A_{5,1}^{\mathfrak f})\), not an exceptional-divisor definition.
  Refs: `rh/proof_of_rh.tex:11625-11638`, `11768-11775`.
- Use the finite-order source package notation
  \[
  \mathfrak P_2(a_1,h_1;a_2,h_2)\in
  \mathbf C\oplus\mathfrak f\oplus
  (\mathfrak f/\mathbf C A_5^{\mathfrak f})
  \]
  and
  \[
  F_h=(c(h),A_5^{\mathfrak f}(h),[A_7^{\mathfrak f}](h)).
  \]
  This is the native ambient target for any order-\(7\) quotient package, but
  it is conditional and currently imports diagonal merger.
  Refs: `rh/proof_of_rh.tex:11888-11932`, `11994-12008`.
- Use **collision-cancellation chart** for the blow-up variables:
  \[
  m=(h_1+h_2)/2,\quad \delta=h_2-h_1,\quad
  \lambda=-a_2/a_1,\quad
  \omega=(\lambda-1)/(\lambda+1),\quad
  \kappa=2\omega/\delta.
  \]
  The paper calls \(\omega\) the **swap-compatible amplitude coordinate**.
  Refs: `rh/proof_of_rh.tex:12385-12413`, `12452-12469`.
- Use **edge law** or **quadratic/projective edge-law package** for the
  analytic factorization
  \[
  E(m,\omega,\delta)=\delta^2\mathcal H(m,\kappa,\delta^2).
  \]
  The displayed native edge functions are \(\mathcal H_3\) and
  \(\mathcal H_5\), not an order-\(7\) edge function.
  Refs: `rh/proof_of_rh.tex:12452-12469`, `12477-12489`.

## Proposed clean UV-010 block language

The least invasive paper wording should define an **actual corrected order-\(7\)
quotient-defect edge package** as follows:

\[
\mathcal H_7^q(m,\kappa,t)\in
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m),
\qquad t=\delta^2,
\]
after an analytic trivialization from the moving quotient
\[
\mathfrak f/\mathbf C A_5^{\mathfrak f}(h_1)
\]
to the midpoint quotient
\[
\mathfrak f/\mathbf C A_5^{\mathfrak f}(m).
\]
The edge law should be stated as
\[
\overline E_{12}^{(7;1)}(m,\omega,\delta)
=\delta^2\mathcal H_7^q(m,\kappa,\delta^2).
\]

Patch hypotheses should include at least \(c\neq0\), the good-patch hypothesis
used by the collision chart, and a quotient-rank convention such as
\[
A_5^{\mathfrak f}(m)\neq0.
\]
If the paper wants to include \(A_5^{\mathfrak f}(m)=0\), it needs a separate
projectivized or blown-up quotient convention.

The exceptional-divisor quotient class for \(R\) should then be downstream from
the edge package:
\[
[R]_{\mathrm{edge}}(m,\kappa)
=-a_1(0)^{-1}\mathcal H_7^q(m,\kappa,0),
\]
with the amplitude convention stated explicitly. The finite-delta theorem
provides the factor \(-a_1^{-1}\), but the edge-limit convention is not yet in
the paper.

## Existing notation that is close but not equivalent

- \(\mathcal J_2\) is a generic finite-order interaction Hessian in an arbitrary
  finite-dimensional target \(V\). It is not order-specific and does not fix a
  quotient bundle. Refs: `rh/proof_of_rh.tex:11920-11930`.
- \(\overline E_{12}^{(7;1)}=O(\delta^2)\) is only an estimate after conditional
  source hypotheses. It is not an analytic edge package or a midpoint quotient
  definition. Refs: `rh/proof_of_rh.tex:12016-12027`.
- The generic edge function \(\mathcal H\) at
  `rh/proof_of_rh.tex:12467` is a template for an already-defined actual
  defect. It does not define the septic quotient defect.
- Theorem `thm:quotient-septic-closure` closes the **one-pair canonical
  quotient-level order-\(7\) package**:
  \[
  [A_7^{\mathfrak f}]=[A_{7,K_1}^{\mathfrak f}],
  \qquad \Delta_7=\Delta_{7,K_1}.
  \]
  It is not the two-atom interaction edge package for
  \(\overline E_{12}^{(7;1)}\). Refs:
  `rh/proof_of_rh.tex:7892-7924`, `7976-8002`.
- The later paper explicitly warns that canonical quotient-septic closure is
  still locally free and provenance-sensitive. Refs:
  `rh/proof_of_rh.tex:10780-10810`, `10812-10843`.

Searches in `rh/proof_of_rh.tex` for `\mathcal H_7`, `H_7`,
`\mathcal H^q`, `\mathfrak O_7`, and `\mathcal J_2^{(7)}` found no canonical
definition. The team directory contains these names only in UV-010 reports and
ledgers, not in the paper.

## What UV-010 must not claim

- It must not claim state-locality, descent, or \(\kappa\)-independence of
  \(\mathcal H_7^q\). The arbitrary
  \(a_1a_2\delta^2P(m,\kappa)\) pressure term remains admissible before a later
  descent theorem.
- It must not claim diagonal-merger normalization to \(\widehat\Psi(m)\).
  Diagonal merger is a hypothesis in the finite-order source criterion and a
  downstream package theorem target, not a proved input.
- It must not rely on the quotient-diagonal route alone. That route is coarser
  and explicitly does not produce the finite-order defect factorization.
  Refs: `rh/proof_of_rh.tex:12042-12166`.

## Suggested theorem heading

Best heading candidate:

`Conditional order-7 quotient-defect edge package in the collision-cancellation chart`

Sharper if promoted as a WIP theorem:

`Work in progress: order-7 quotient-defect edge package`

Avoid calling it a quotient-septic closure theorem; that phrase is already used
for the one-pair canonical closure at `thm:quotient-septic-closure`.
