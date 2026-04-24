## Claim

Davenport, `Multiplicative Number Theory`, 2nd ed., gives a substantially
tighter citation package for Beauvoir's compact edge-difference source inputs:
Chapter 9 covers primitive Dirichlet analytic continuation, parity notation,
completed-function normalization, and functional equation; Chapter 11 covers
order-one Hadamard products and the zero-summability input; Chapter 12 applies
that product/log-derivative machinery to primitive Dirichlet \(L\)-functions.
DLMF \(\S 25.15\) remains the clean web fallback for the primitive functional
equation, trivial zeros, and \(L(1,\chi)\ne0\) checks. This pass improves the
paper-promotion source package but does not fully close the bibliographic
burden because the Davenport source checked here is OCR with corrupted symbols;
exact book page/equation references should be verified against a clean
physical or PDF copy before paper insertion.

## Status

open

## Evidence

Proved from the checked OCR locators: Davenport Chapter 9 supports the
primitive completed \(L\)-function setup. The even-character continuation is at
the supplied OCR lines 3991-3993; the odd-character continuation is at lines
4088-4089; the unified parity/completed-function/function-equation notation is
at lines 4106-4127. The OCR formula is symbol-corrupted, but the structure is
recognizable as Davenport's completed primitive Dirichlet \(L\)-function
functional equation.

Proved from the checked OCR locators: Davenport Chapter 11 supplies the
finite-order/order-one entire-function machinery. Lines 4240-4253 define finite
order and order. Lines 4427-4436 give the genus-one product form for an
integral function of order one. Lines 4456-4458 summarize that an order-one
integral function has that product form and that the zero radii satisfy the
needed exponent-of-convergence bounds.

Proved from the checked OCR locators: Davenport Chapter 12 applies the Chapter
11 product to primitive Dirichlet \(L\)-functions. Lines 4653-4663 define the
primitive completed function \(\xi(s,\chi)\), state there is no \(s(s-1)\)
factor in the nonprincipal primitive case, and give the functional equation
with unimodular factor. Lines 4673-4680 give the growth/order conclusion and
the product
\[
\xi(s,\chi)=e^{A+B s}\prod_\rho(1-s/\rho)e^{s/\rho}
\]
for zeros in the critical strip, with the same summability properties as in
the zeta case. Lines 4693-4698 give the logarithmic-derivative/partial-fraction
formula for \(L'/L\), obtained from the completed product and the gamma factor.

Proved as a citation table:

| Input | Best citation | Covers? | Remaining issue |
|---|---|---:|---|
| Definition and parity factor for \(\Lambda(s,\chi)\) | Davenport Ch. 9, functional-equation section, OCR lines 4106-4127; Davenport Ch. 12, OCR lines 4653-4656 | Yes, as locator | OCR corrupts \(\xi\), \(\Gamma\), \(\pi/q\), and \(a\); verify exact equation/page in clean copy. |
| Analytic continuation / entire status for primitive nonprincipal \(L\) and completed \(\Lambda\) | Davenport Ch. 9, OCR lines 3991-3993 and 4088-4089; Ch. 12, lines 4653-4663 | Yes, as locator | Need clean-copy confirmation that the statement is for primitive nonprincipal characters; principal \(q=1\) must remain excluded or separately completed with \(s(s-1)\). |
| Paired/self-dual functional equation for \(\Xi_\chi=\Lambda_\chi\Lambda_{\overline\chi}\) | Davenport Ch. 9, OCR lines 4106-4127; Ch. 12, lines 4659-4663; DLMF 25.15.5-25.15.6 | Yes after multiplying conjugate equations | Davenport gives the single-character equation; the paired self-dual equation is a one-line derived statement, not a named theorem citation. |
| Zero multiset and product multiplicity | General analytic fact plus Davenport Ch. 11 product theorem, OCR lines 4427-4436; Ch. 12 product, lines 4677-4680 | Mostly | OCR does not explicitly state "listed with analytic multiplicity" in the visible lines. Paper text should state this as standard entire-function convention or cite a clean complex-analysis theorem. |
| Genus-one Hadamard product for completed Dirichlet function | Davenport Ch. 11, OCR lines 4427-4436 and 4456-4458; Ch. 12, lines 4677-4680 | Yes, as locator | Clean-copy citation required because the OCR mangles symbols and "properties (4) and (5)" point back to zeta lines 4518-4538. |
| Log-derivative regularization \(\xi'/\xi=B+\sum_\rho((s-\rho)^{-1}+\rho^{-1})\) | Davenport Ch. 12, zeta model lines 4546-4558; Dirichlet application lines 4693-4698; Ch. 17 reuse lines 6496-6500 | Yes in structure | Ch. 12 displays the final Dirichlet formula as \(L'/L\) after subtracting gamma/conductor terms. For a paper lemma about \(\Xi'/\Xi\), cite the completed product directly and derive the log derivative in text. |
| \(\sum m_\rho|\rho|^{-2}<\infty\) | Davenport Ch. 11, OCR lines 4456-4458, plus Ch. 12 "same properties" at lines 4677-4680 | Yes | Clean-copy equation references needed; multiplicities should be made explicit in the theorem statement. |
| Trivial-zero/gamma-pole cancellation | Davenport Ch. 12, lines 4653-4658 for no \(s(s-1)\) factor in the Dirichlet completed function; DLMF \(\S 25.15(ii)\), lines 182-217 | Yes | Davenport's visible text is enough as a locator but not clean enough for a final quote. DLMF remains clearer for trivial-zero locations. |
| Possible zero at \(\rho=0\) | DLMF 25.15.5 plus \(L(1,\overline\chi)\ne0\) from DLMF 25.15.9; Davenport Ch. 12, lines 4691-4692 and 4722-4725 discuss \(\xi(0,\chi)\) and possible nearby zeros | Partial | Need clean citation for \(L(1,\chi)\ne0\) and a one-line derivation that \(\Lambda(0,\chi)\ne0\) for primitive nonprincipal \(\chi\). Davenport's "zero near \(s=0\)" warning is not a zero-at-origin result. |
| Principal/nonprimitive exclusions | Davenport Ch. 12, lines 4656-4658 distinguishes the zeta \(s(s-1)\) factor; DLMF 25.15, lines 66-67 and 125-127 distinguish principal/primitive cases | Yes | State exclusions in the theorem; do not silently broaden beyond primitive nonprincipal characters. |
| Chapter 17 explicit-formula reuse | Davenport Ch. 17, OCR lines 6496-6500 and 6576-6586 | Locator only | Useful confirmation that Davenport later uses Ch. 12 equation (17), but it is not the primary citation for the compact regularization lemma. |

Conditional: the table above should be treated as a promotion draft, not as a
final bibliography. The mathematical coverage is present, but exact page
numbers, equation labels, and uncorrupted formulas still need a clean copy of
Davenport or an equivalent textbook such as Montgomery--Vaughan.

Missing: I did not obtain a clean non-OCR book page/PDF in this pass. From this
source lane alone, the exact final citation package still cannot honestly be
called paper-ready.

Honest verdict: Davenport plus DLMF is enough to replace most web-level
locators with textbook-grade targets. The remaining blocker is a clean-copy
verification step, not a missing theorem.

## Baseline / delta

Baseline: `report-source-audit.md` reduced the compact convergence source
inputs to standard completed Dirichlet \(L\)-function theory but left
Fungrim/Mathlib/Khale/MathWorld as web-level or secondary locators. It named
the remaining source-citation gap as bibliographic rather than mathematical.

Delta: this pass identifies Davenport chapters and equation neighborhoods for
the exact inputs needed by the compact edge-difference proof, and it demotes
Fungrim/Mathlib/Khale/MathWorld from promotion sources to optional checks. The
strongest remaining source gap is now narrow: verify exact Davenport page and
equation references against a clean copy, especially for corrupted OCR symbols,
multiplicity convention, and the zero-at-origin derivation.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:24-64`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:123-132`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:134-147`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:3-43`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:94-104`
- Davenport, `Multiplicative Number Theory`, 2nd ed., online OCR:
  https://djvu.online/file/Rh8B8jEVpxFgk
  - Ch. 9, OCR lines 3991-3993, 4088-4089, 4106-4127.
  - Ch. 11, OCR lines 4240-4253, 4427-4436, 4456-4458.
  - Ch. 12, OCR lines 4546-4558, 4653-4680, 4693-4698.
  - Ch. 17, OCR lines 6496-6500, 6576-6586.
- DLMF \(\S 25.15\), especially lines 66-67, 125-148, 169-217, and
  219-244 in the browsed page: https://dlmf.nist.gov/25.15

## Dependencies

- A clean physical or PDF copy of Davenport, `Multiplicative Number Theory`,
  2nd ed., or a replacement textbook with stable page/equation citations.
- Acceptance that the theorem is restricted to primitive nonprincipal
  characters unless principal/nonprimitive background factors are added
  separately.
- A standard entire-function convention that zeros in canonical products are
  counted with analytic multiplicity, or an exact complex-analysis citation
  making that convention explicit.
- DLMF or an equivalent textbook citation for \(L(1,\chi)\ne0\) for
  nonprincipal characters, used to rule out a completed zero at \(\rho=0\).

## Strongest objection

The Davenport OCR is not a reliable final citation surface. It verifies that
the relevant material is in Davenport and sharply locates it, but corrupted
symbols in the displayed formulas make it unsafe to cite the OCR line numbers
as final paper evidence. This is especially serious for the completed-function
normalization, the exact root-number factor, the Dirichlet \(L'/L\)
partial-fraction formula, and any claim about zero multiplicity. From this
source lane alone, the clean theorem can be drafted but not promoted with final
bibliographic precision.

## Needed for promotion

1. Check Davenport Chapter 9 in a clean copy and record exact page/equation
   references for the primitive completed-function definition, parity \(a\),
   analytic continuation, and functional equation.
2. Check Davenport Chapter 11 and Chapter 12 in a clean copy and record exact
   page/equation references for the order-one product, zero summability, and
   primitive Dirichlet product/log-derivative formula.
3. Add or cite a clean entire-function statement that product zeros are counted
   with analytic multiplicity.
4. Cite \(L(1,\chi)\ne0\) for nonprincipal \(\chi\) and write the short
   functional-equation argument excluding a completed zero at \(0\).
5. Keep DLMF \(\S 25.15\) as a precise web cross-check for functional equation
   and trivial-zero conventions, but do not rely on it alone if the paper needs
   textbook-only citations.

## Autoresearch next step

verify: perform a clean-copy Davenport check, replacing the OCR line locators
with exact pages/equation labels. If a clean copy is unavailable, switch to
Montgomery--Vaughan or Apostol and build the same table with stable references;
then pass the citation package to the paired source-package writer without
claiming UV-016 closed.
