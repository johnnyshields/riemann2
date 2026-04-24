## Claim

For primitive nonprincipal Dirichlet characters, the standard completed
Dirichlet \(L\)-function inputs needed by Beauvoir's compact edge-difference
regularization proof are mathematically standard and sufficient. The compact
zero-regularization lemma may assume the completed function
\[
\Lambda(s,\chi)=
\left(\frac{q}{\pi}\right)^{(s+a_\chi)/2}
\Gamma\left(\frac{s+a_\chi}{2}\right)L(s,\chi),
\qquad
a_\chi=(1-\chi(-1))/2,
\]
with \(\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\overline{\chi})\), the paired
functional equation, analytic multiplicity of zeros, and genus-one
Hadamard/log-derivative regularization. This source audit does not close
UV-016 because it does not derive the explicit \(B_\chi^{\rm pair}\) split or
the sign-normalized source identity.

## Status

proved

## Evidence

Proved: the theorem-ready input block is recorded in
`notes/source_audit_standard_inputs.md:3-43`. It states the primitive
nonprincipal hypothesis, parity factor, completed normalization, entire/order
input, paired self-dual functional equation, product multiplicity rule,
\(\sum_{\rho\ne0}m_\rho|\rho|^{-2}<\infty\), and the zero-at-origin handling.

Proved: the local source map in `notes/source_audit_standard_inputs.md:46-77`
identifies standard references or locators for each input: DLMF for primitive
Dirichlet functional equations and trivial-zero discussion, Fungrim for
completed-function formulae and repeated-zero conventions, Mathlib as a
formalized analytic-continuation and primitive-functional-equation check, Khale
as a Davenport locator for entire/order-one and Hadamard preliminaries, and
MathWorld as a locator for the general Hadamard finite-order product theorem.

Proved: the special cases are controlled in
`notes/source_audit_standard_inputs.md:79-92`. Principal characters are outside
this lane; nonprimitive characters are outside this primitive paired theorem;
gamma poles and raw \(L\)-function trivial zeros are canceled in the completed
\(\Lambda(s,\chi)\) and re-enter only if the source identity is rewritten in
raw factors; \(\rho=0\) is absent for primitive nonprincipal \(\chi\) by the
functional equation and \(L(1,\overline{\chi})\ne0\), but can also be handled
by a separate finite factor if a broader statement is later desired.

Conditional: paper promotion should replace the web-level locators for
"entire of order one" and "Hadamard product for the completed Dirichlet
\(L\)-function" with exact textbook citations, most likely Davenport's
`Multiplicative Number Theory`, 2nd ed., for Dirichlet \(L\)-function
preliminaries and a standard complex analysis text for Hadamard factorization.
This bibliographic replacement is stated in
`notes/source_audit_standard_inputs.md:94-104`.

Missing: no mathematical source input remains missing for the compact
edge-difference convergence lemma from this source-audit scope alone. What
remains missing for UV-016 is not this completed-function input layer, but the
explicit \(B_\chi^{\rm pair}\) background split and the sign-normalized
source-package statement.

Honest verdict: the compact convergence source inputs are enough and standard;
the remaining promotion blocker is citation quality, not a new analytic
theorem at this layer.

## Baseline / delta

Baseline: Beauvoir's prior compact regularization proof used standard
completed Dirichlet inputs as assumptions; Sartre's compact-convergence audit
accepted the proof in that scoped form but required source citations and
special-case handling before promotion. See
`report.md:23-27`,
`notes/compact_regularization_reduction.md:11-14`,
`notes/compact_regularization_reduction.md:36-76`, and
`../20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:71-84`.

Delta: this audit converts that conditional input list into a theorem-ready
primitive nonprincipal assumption block, identifies exact exclusions
(principal and nonprimitive characters), explains the \(\rho=0\) issue, and
separates the remaining bibliographic source-citation task from the
mathematical compact-convergence proof.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:3-43`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:46-77`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:79-92`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:94-104`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report.md:23-27`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:11-14`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md:36-76`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:71-84`
- DLMF, `Dirichlet L-Functions`, especially the primitive functional equation
  and trivial-zero discussion: https://dlmf.nist.gov/25.15
- Fungrim, `Dirichlet L-functions`: https://fungrim.org/topic/Dirichlet_L-functions/
- Mathlib documentation, `DirichletContinuation`, including
  `completedLFunction` and `IsPrimitive.completedLFunction_one_sub`:
  https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/DirichletContinuation.html
- Khale, `An explicit Vinogradov-Korobov zero-free region for Dirichlet
  L-functions`, arXiv:2210.06457, Section 2.1 as a Davenport locator:
  https://arxiv.org/abs/2210.06457
- MathWorld, `Hadamard Factorization Theorem`, as a general complex-analysis
  locator for finite-order canonical products:
  https://mathworld.wolfram.com/HadamardFactorizationTheorem.html

## Dependencies

- Primitive nonprincipal \(\chi\) modulo \(q>1\).
- Compact interval \(I\) avoiding the edge-zero sets
  \(2it\in Z(\Xi_\chi)\) and \(1+2it\in Z(\Xi_\chi)\).
- Standard completed Dirichlet \(L\)-function theory: analytic continuation,
  functional equation, entire order-one completed function, and zero
  multiplicities.
- Standard Hadamard factorization for finite-order entire functions.
- A separate sign-normalized source identity and explicit
  \(B_\chi^{\rm pair}\) split for full UV-016 promotion.

## Strongest objection

The present audit still relies on web-level or secondary locators for some
promotion-critical citations. Fungrim, Mathlib, Khale, and MathWorld are useful
checks and pointers, but a theorem-facing paper should cite exact book theorem
numbers, sections, or pages for the completed Dirichlet \(L\)-function being
entire of order one and for the Hadamard product/log-derivative theorem. This
does not reopen the compact convergence proof from this scope alone, but it
does block polished paper promotion until replaced by direct textbook
references.

## Needed for promotion

1. Replace the locator citations with exact textbook references for the
   completed primitive nonprincipal Dirichlet \(L\)-function package:
   normalization, parity, functional equation, entire order one, and
   zero-multiplicity convention.
2. Cite a standard complex analysis theorem for finite-order Hadamard products
   and the resulting \(\sum m_\rho|\rho|^{-2}<\infty\) summability.
3. State the theorem only for primitive nonprincipal characters, or add a
   separate clause for principal/nonprimitive cases before broadening it.
4. State edge-zero avoidance for the compact interval and, for robustness, how
   a zero at \(\rho=0\) would be factored if a later variant permits one.
5. Keep this as the completed-zero regularization input layer; combine it with
   Jason's \(B_\chi^{\rm pair}\) lane and the UV-021 sign convention only after
   those pieces are theorem-ready.

## Autoresearch next step

verify: have a source verifier replace the locator references with exact
Davenport or Montgomery-Vaughan references for completed Dirichlet
\(L\)-functions and an exact complex-analysis theorem citation for Hadamard
factorization, then hand the cleaned assumption block to the paired
source-package writer without claiming UV-016 closed.
