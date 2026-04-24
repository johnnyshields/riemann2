## Claim

A bounded fallback citation package is acceptable for a working-paper draft of
the compact edge-difference source-input layer: cite stable DLMF references for
Dirichlet \(L\)-function continuation, primitive functional equation, trivial
zeros, and \(L(1,\chi)\ne0\); cite a standard complex-analysis Hadamard
factorization theorem for finite-order entire functions; and mark
Davenport/Montgomery--Vaughan as desired textbook upgrades. Clean Davenport
verification is not a hard blocker for this working-draft layer. It is still a
blocker for a polished textbook-grade bibliography, and it does not close full
UV-016 from this source lane alone.

## Status

proved

## Evidence

Proved: DLMF \(\S 25.15\) is stable enough for the Dirichlet-specific facts in
a working draft. DLMF gives the defining series and nonprincipal entire
continuation in \((25.15.1)\) and the paragraph following it; primitive
functional equation and Gauss sum in \((25.15.5)\)-\((25.15.6)\); primitive
trivial-zero locations in \((25.15.7)\)-\((25.15.8)\); and
\(L(1,\chi)\ne0\) for nonprincipal \(\chi\) in \((25.15.9)\). DLMF also
records source metadata to Apostol for these formulas.

Proved: a standard complex-analysis Hadamard theorem covers the
entire-function step once \(\Xi_\chi\) is known to be entire of finite order at
most one. A permitted working citation is Conway, `Functions of One Complex
Variable I`, 2nd ed., Chapter XI, Section 3, Hadamard's Factorization Theorem
(Theorem XI.3.4 in standard course notes following Conway): an entire function
of finite order \(\lambda\) has finite genus \(\mu\le\lambda\), with zeros
repeated according to multiplicity. This yields a genus-one product and
\(\sum m_\rho|\rho|^{-2}<\infty\) for order-one functions.

Conditional: DLMF by itself does not display a named completed
\(\Lambda(s,\chi)\) order-one theorem in the same explicit way Davenport does.
For the working draft, this is acceptable only if the text includes a short
standard-order sentence: from DLMF \((25.15.3)\), \((25.15.5)\), and Stirling's
formula for \(\Gamma\) (DLMF \(\S 5.11(i)\)), the completed primitive
nonprincipal function has order at most one; then the functional equation and
known nontrivial zeros put the usual order-one/Hadamard setting in place. If
the paper wants citation-only support for "completed \(\Lambda(s,\chi)\) is
entire of order one" with no local derivation, then a clean textbook source is
still needed.

Proved as the exact fallback stack I would permit for a working draft:

| Input | Fallback citation | Covers? | Upgrade / issue |
|---|---|---:|---|
| Dirichlet \(L(s,\chi)\) definition and nonprincipal entire continuation | DLMF \(\S 25.15(i)\), \((25.15.1)\) and following paragraph | Yes | Textbook upgrade: Apostol or Davenport page. |
| Primitive functional equation and conjugate character | DLMF \(\S 25.15(i)\), \((25.15.5)\)-\((25.15.6)\) | Yes | Convert DLMF's raw \(L\)-equation into the paper's \(\Lambda\)-normalization in text. |
| Parity/completed normalization | Derived in text from DLMF \((25.15.5)\) using \(a_\chi=(1-\chi(-1))/2\) | Yes for draft | DLMF does not name exactly the paper's \(\Lambda\); write the normalization explicitly. |
| Entire completed function and gamma-pole/trivial-zero cancellation | DLMF \(\S 25.15(ii)\), \((25.15.7)\)-\((25.15.8)\), plus the chosen \(\Lambda\)-definition | Yes for draft | State primitive nonprincipal only; principal case needs \(s(s-1)\) removal. |
| \(L(1,\overline\chi)\ne0\), hence no completed zero at \(0\) | DLMF \(\S 25.15(ii)\), \((25.15.9)\), plus functional equation | Yes | Write the one-line derivation; do not cite Davenport's "zero near \(0\)" warning as if it ruled out \(0\). |
| Order at most one of completed \(\Lambda\) and \(\Xi_\chi\) | Short local derivation from DLMF \((25.15.3)\), \((25.15.5)\), and DLMF \(\S 5.11(i)\) Stirling asymptotics | Conditional yes | If no derivation is included, clean Davenport/Montgomery--Vaughan is a hard citation blocker for this row. |
| Hadamard product, multiplicity convention, and \(\sum m_\rho|\rho|^{-2}<\infty\) | Conway, `Functions of One Complex Variable I`, 2nd ed., Ch. XI, \(\S 3\), Hadamard Factorization Theorem; exact theorem numbering to be checked if inserted | Yes for draft | Replace with exact theorem/page from the available complex-analysis text before final polish. |
| Log-derivative regularization | Differentiate the genus-one product from the preceding row away from zeros | Yes | State locally uniform convergence away from zeros and separate a zero at \(0\) if ever included. |
| Principal/nonprimitive exclusions | DLMF \(\S 25.15(i)\), paragraph after \((25.15.1)\), and DLMF \((25.15.4)\) | Yes | Keep theorem restricted to primitive nonprincipal characters. |

Missing: no clean Davenport or Montgomery--Vaughan page/equation numbers are
provided by this fallback. The fallback is a working-draft citation stack, not
the final preferred bibliography.

Honest verdict: clean textbook verification is not a hard blocker for drafting
or locally promoting the compact-convergence source-input lemma, provided the
order-one row is handled by a short in-text derivation. It is a hard blocker
only if the project demands citation-only support for order one or a final
publication-grade bibliography.

## Baseline / delta

Baseline: `report-textbook-citation-pass.md` found that Davenport OCR locators
cover the desired theory but are too symbol-corrupted for final paper citation.
It left clean Davenport or Montgomery--Vaughan verification as the next best
step.

Delta: this report supplies a bounded fallback if that clean-copy check stalls.
The source-input layer can move in a working draft with DLMF plus a standard
Hadamard theorem, while the final citation upgrade remains explicitly marked.
The delta is not a proof-state closure for UV-016; it is a citation-risk
reduction for one component of UV-016.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:24-64`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:123-147`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-textbook-citation-pass.md:1-13`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-textbook-citation-pass.md:52-76`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:3-43`
- DLMF \(\S 25.15(i)\), `Definitions and Basic Properties`, especially
  \((25.15.1)\), \((25.15.3)\), \((25.15.5)\), and \((25.15.6)\):
  https://dlmf.nist.gov/25.15.i
- DLMF \(\S 25.15(ii)\), `Zeros`, especially \((25.15.7)\),
  \((25.15.8)\), \((25.15.9)\), and \((25.15.10)\):
  https://dlmf.nist.gov/25.15.ii
- DLMF \(\S 5.11(i)\), Stirling/gamma asymptotics, especially
  \((5.11.1)\), \((5.11.3)\), and \((5.11.7)\)-\((5.11.9)\):
  https://dlmf.nist.gov/5.11.i
- Conway, `Functions of One Complex Variable I`, 2nd ed., Ch. XI, \(\S 3\),
  Hadamard's Factorization Theorem. Locator check: ETSU notes
  `XI.3. Hadamard's Factorization Theorem`, Theorem XI.3.4, records the
  finite-order-to-finite-genus statement and multiplicity convention:
  https://faculty.etsu.edu/gardnerr/5510/notes/XI-3.pdf

## Dependencies

- The working draft must allow DLMF as a stable reference for Dirichlet
  \(L\)-function facts.
- The theorem must remain restricted to primitive nonprincipal characters.
- The order-one input must either be derived briefly in text from DLMF formulas
  plus Stirling estimates or backed by a clean textbook citation.
- A standard complex-analysis Hadamard theorem with zeros counted by analytic
  multiplicity must be cited exactly before final polish.
- Full UV-016 still depends on the sign-normalized source package and
  \(B_\chi^{\rm pair}\) normalization lanes.

## Strongest objection

The fallback citation package is weaker than the desired textbook package
because DLMF does not package the paper's exact completed
\(\Lambda(s,\chi)\) order-one theorem as a single named result. If the draft
simply cites DLMF and asserts order one without a proof sentence or a textbook
reference, the citation is underpowered. From this source lane alone, the
fallback is acceptable only because the order-one claim is standard and can be
derived locally from DLMF's formulas and Stirling asymptotics; it is not an
excuse to leave the growth input uncited and unproved.

## Needed for promotion

1. In the compact source-input lemma, cite DLMF \(\S 25.15(i)\)-\((ii)\) for
   Dirichlet \(L\)-function continuation, functional equation, trivial zeros,
   and \(L(1,\chi)\ne0\).
2. Define the paper's \(\Lambda(s,\chi)\) explicitly and say it is the
   completed primitive nonprincipal function obtained from DLMF
   \((25.15.5)\) with parity \(a_\chi=(1-\chi(-1))/2\).
3. Add a short order-one sentence using DLMF \((25.15.3)\), DLMF
   \((25.15.5)\), and DLMF \(\S 5.11(i)\), unless a clean
   Davenport/Montgomery--Vaughan citation is available.
4. Cite a standard Hadamard factorization theorem, preferably Conway Ch. XI,
   \(\S 3\), with exact page/theorem checked before final polish.
5. Mark Davenport or Montgomery--Vaughan as desired upgrades, not blockers for
   the working draft.
6. Do not claim full UV-016 is closed until the sign-normalized source identity
   and \(B_\chi^{\rm pair}\) split are also promoted.

## Autoresearch next step

continue: hand this fallback stack to the wording owner for a working-draft
source-input lemma. In parallel, keep the clean-copy Davenport or
Montgomery--Vaughan check open as a bibliography upgrade rather than blocking
the compact-convergence source layer.
