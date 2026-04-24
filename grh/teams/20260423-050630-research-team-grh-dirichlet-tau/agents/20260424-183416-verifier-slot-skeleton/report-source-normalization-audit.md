## Claim

Jason's completed-Hadamard proposal is correct as a normalization lemma, but it
is not yet a theorem-ready UV-016 source statement "modulo citations" unless
the paper statement is rewritten to make that normalization explicit.

Proved in the completed convention: for primitive nonprincipal \(\chi\), on a
regular compact boundary interval, with
\[
\Phi_\chi^{\mathrm{pair}}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s),
\qquad
\Xi_\chi=\Lambda(s,\chi)\Lambda(s,\overline\chi),
\]
and the sign-audited convention
\[
\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\,\prime},
\]
one has
\[
q_\chi^{\mathrm{pair}}(t)
=-\frac12(\Phi_\chi^{\mathrm{pair}\,\prime}/
\Phi_\chi^{\mathrm{pair}})(1/2+it)
=\Re D_\chi(t),
\]
where
\[
D_\chi(t)=\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
-\frac{\Xi_\chi'}{\Xi_\chi}(2it).
\]
The completed Hadamard edge difference gives
\[
\Re D_\chi(t)=
\Re\sum_{\rho\in Z(\Xi_\chi)}m_\rho
\left({1\over 1+2it-\rho}-{1\over 2it-\rho}\right),
\]
with compact-uniform convergence, and no residual completed background:
\[
B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0.
\]

Honest verdict: keep the route, but do not promote it as the unqualified
`B_chi^pair` theorem yet. The theorem must say "completed-Hadamard
normalization" and must not also add raw gamma/trivial-zero/pole background
terms. Those raw terms belong only to a separate raw \(L\)-factor remark.

## Status

open

## Evidence

**Proved.**

- The sign bridge is already adversarially checked: for the fixed quotient, the
  positive one-zero strip-edge kernel is the contribution to
  \(-\frac12\Phi'/\Phi\), not \(+\frac12\Phi'/\Phi\). See
  `report-sign-audit.md:3-37` and `:47-78`.
- Jason's derivation uses the same sign convention and defines
  \(D_\chi(t)=\Xi_\chi'/\Xi_\chi(1+2it)-\Xi_\chi'/\Xi_\chi(2it)\), with
  \(\Phi'/\Phi=-2D_\chi\). See
  `agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md:5-38`.
- Under the standard primitive nonprincipal completed-function package, the
  genus-one log derivative has the regularized form
  \(b_\chi+\sum_\rho m_\rho((w-\rho)^{-1}+\rho^{-1})\). Taking the same edge
  difference cancels both \(b_\chi\) and \(\rho^{-1}\), leaving the completed
  zero edge-difference sum. See
  `agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md:40-75`.
- The compact-convergence audit already accepted the \(O_I(|\rho|^{-2})\)
  argument, fixed-derivative convergence, multiplicity handling, and edge-hit
  exclusions in the completed-zero series. See
  `report-compact-convergence-audit.md:3-28` and `:38-86`.
- The standard completed-function input block is adequate for the
  nonprincipal primitive lane: \(\Lambda(s,\chi)\) entire of order one,
  \(\Xi_\chi\) entire of order at most one, product multiplicities added, and
  \(\sum_{\rho\ne0}m_\rho|\rho|^{-2}<\infty\). See
  `agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:7-44`.

**Conditional.**

- \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) is theorem-safe only after the
  source statement explicitly chooses the completed-Hadamard normalization:
  \(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\) sums all completed zeros of
  \(\Xi_\chi\), counted as the product zero multiset with analytic
  multiplicity. No separate gamma, trivial-zero, pole, conductor, or raw
  Hadamard terms may be added in that same statement.
- The scalar source should be written as \(\Re D_\chi(t)\), or the theorem must
  include the boundary-realness lemma that \(D_\chi(t)\) is real on regular
  intervals. Jason's note says "with the understood real-part projection"; that
  should become theorem text, not remain implicit. See
  `agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md:26-38`.
- The edge exclusions must be part of the theorem: \(2it\notin Z(\Xi_\chi)\)
  and \(1+2it\notin Z(\Xi_\chi)\) on the compact interval. If a broader variant
  permits \(\rho=0\), it needs a separate finite factor before using the
  \(1/\rho\) regularized product notation.
- Source citations still need exact textbook replacement. The source audit says
  the mathematical inputs are standard, but the current locator list is not yet
  paper-grade. See
  `agents/20260424-183416-gap-compact-regularization/report-source-audit.md:123-148`.

**Missing.**

- The current paper candidates still use unqualified `B_chi^pair` language. The
  source-package candidate asks for one unified background term, and the older
  source-and-slot candidate lists conductor/scaling, gamma derivatives, and
  trivial-zero or pole corrections as \(B_\chi^{\mathrm{pair}}\) contents. See
  `paper/dirichlet_paired_source_package_candidate.tex:34-57` and
  `paper/dirichlet_paired_source_candidate.tex:69-85`.
- There is not yet a clean theorem/remark split saying:
  completed theorem: \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\);
  raw remark: gamma/trivial-zero/pole/raw-Hadamard terms appear only if the
  source is rewritten in raw \(L\)-factor zeros.
- Full UV-016 still needs source-normalized theorem wording and exact textbook
  citations. UV-017 slot realization is untouched.

No computation was run for this audit.

## Baseline / delta

Baseline: the previous state had sign normalization checked, compact
completed-zero convergence checked, and standard completed-\(L\) inputs checked
up to citation quality. Jason's background-split pass proposed
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) when all completed zeros of
\(\Xi_\chi\) are summed.

Delta: this audit accepts the \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\)
subclaim inside the completed-Hadamard normalization, but rejects the stronger
reading that UV-016 is theorem-ready modulo citations alone. The remaining
work is a normalization rewrite: define the completed \(q=B+S\) interface with
\(B=0\), real-part projection, edge exclusions, and a no-double-counting raw
remark.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:5-27`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:66-80`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/findings.md`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report-background-split.md:3-43`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report-background-split.md:51-87`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report-background-split.md:89-148`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report-background-split.md:188-231`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md:5-38`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md:40-75`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md:77-138`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:1-18`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:24-65`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/report-source-audit.md:123-148`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:7-44`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md:79-105`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md:3-37`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md:47-89`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:3-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:38-104`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_package_candidate.tex:24-57`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_candidate.tex:25-49`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_candidate.tex:69-85`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:29-55`

## Dependencies

- Primitive nonprincipal Dirichlet character; principal and nonprimitive cases
  remain outside this completed-source candidate unless separately treated.
- Standard completed-\(L\) package with exact citations: parity-normalized
  \(\Lambda(s,\chi)\), entire order-one completed functions, paired functional
  equation, product zero multiset with analytic multiplicities, and genus-one
  Hadamard log-derivative.
- Sign-audited fixed quotient convention:
  \(\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)}\),
  \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\,\prime}\), equivalently
  \(q_\chi^{\mathrm{pair}}=-\frac12\Phi'/\Phi\).
- Regular compact intervals avoiding numerator and denominator edge zeros.
- A theorem wording choice that distinguishes completed normalization from raw
  \(L\)-factor bookkeeping.

## Strongest objection

The phrase \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) can hide a convention
switch. It is true only because \(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\) is
defined to sum all completed zeros of \(\Xi_\chi\) after the completed
Hadamard edge difference. The existing paper candidates still speak as if
\(B_\chi^{\mathrm{pair}}\) is a unified background term containing gamma,
conductor, trivial-zero, and pole corrections. If those raw-background pieces
are added after summing completed zeros, the source statement double-counts or
mixes two normalizations.

## Needed for promotion

1. Rewrite the UV-016 theorem statement in completed notation:
   \(q_{\chi,\mathrm{comp}}^{\mathrm{pair}}
   =B_{\chi,\mathrm{comp}}^{\mathrm{pair}}
   +S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\), with
   \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\).
2. Define
   \(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)=
   \Re\sum_{\rho\in Z(\Xi_\chi)}m_\rho((1+2it-\rho)^{-1}-(2it-\rho)^{-1})\)
   and state compact-uniform convergence plus fixed derivative convergence.
3. State the boundary sign and scalar convention:
   \(\Phi=e^{-2i\Theta}\), \(q=\Theta'\), and
   \(q=-\frac12\Phi'/\Phi=\Re D_\chi\).
4. State edge exclusions and primitive nonprincipal hypotheses, including the
   \(\rho=0\) finite-factor clause only as a robustness note.
5. Add a separate raw \(L\)-factor bookkeeping remark, not part of the completed
   theorem, explaining where gamma/trivial-zero/pole/raw-Hadamard terms appear
   if one uses raw zeros instead of completed zeros.
6. Replace source locators with exact textbook citations before any paper
   promotion.
7. Suggest ledger update: UV-016 should say "completed-Hadamard normalization
   accepted modulo theorem wording and citations; raw-background bookkeeping
   quarantined as a separate convention." UV-021 should remain open until the
   source-package rewrite actually installs the sign convention.

## Autoresearch next step

continue: draft the exact theorem-facing statement for the completed UV-016
source package as a proposed `paper-updates.md` block, with a separate raw
bookkeeping remark and no UV-017 slot-realization claim.
