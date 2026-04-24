# Collation

## Resume Recovery 20260424-183416

The supplied team dir predates the current `findings.md` / `uv.md` /
`attempts.md` layout. I read the top-level handoff, note stack, theorem-facing
paper notes, recent lore, current RH source/local lines, and the agent report
index. The old reports were already distilled into notes and handoff files, but
several live gaps were stranded outside a UV ledger, so this resume files
UV-016 through UV-020 here.

Three-bin recovery:

- **proved:** the source-light local layer exists in the RH draft; one-zero
  strip-edge kernel positivity is solid; the compact paired bookkeeping block
  is at the right sub-theoremic scope.
- **conditional on new paired-family input:** compact paired source package;
  exact paired slot realization; downstream odd/transverse package.
- **missing:** paired compact convergence/regularization, unified
  `B_chi^pair`, multiplicity closure, exact `S_chi^pair` slot coefficient,
  paired local positivity/whitening, zeta source theorem in the RH draft, tau
  localization.

Resume target: UV-016 first, with a one-ahead verification lane on UV-017.

Live roster:

- Beauvoir (`019dbeda-2b9e-7a53-89c1-2218ff892545`) attacks UV-016 compact
  regularization in
  `agents/20260424-183416-gap-compact-regularization/`.
- Jason (`019dbeda-2c40-7ed0-a5ba-a9076f939fc7`) explores UV-016 unified
  background and multiplicity bookkeeping in
  `agents/20260424-183416-explorer-background-multiplicity/`.
- Sartre (`019dbeda-2d23-7da1-adf1-a557dccad97b`) adversarially verifies the
  UV-017 slot skeleton in
  `agents/20260424-183416-verifier-slot-skeleton/`.

Report-processing note: no old agent deposit is being rewritten. The live
briefing state is now captured in `findings.md`, `uv.md`, and `attempts.md`;
old report paths remain the provenance.

## Sartre Deposit 20260424

Report:
`agents/20260424-183416-verifier-slot-skeleton/report.md`.

Verdict: keep. UV-017 remains open. The paired slot skeleton is usable as a
conditional roadmap, but not promotable as a theorem. Sartre sharpened the
missing statement from broad "paired admissibility" to a precise
coefficient-normalization problem: prove that the paired source scalar is the
pure local value parameter to first order, with value-parameter holomorphy,
stable same-point positivity, explicit freeze rules, and no hidden
renormalization.

Capture action: refined `findings.md`, UV-017 in `uv.md`, and `attempts.md`.

## Jason Deposit 20260424

Report:
`agents/20260424-183416-explorer-background-multiplicity/report.md`.
Script:
`agents/20260424-183416-explorer-background-multiplicity/scripts/check_one_zero_sign.py`.

Verdict: keep. UV-016 remains open and now has a precise sign-normalization
subgap, filed as UV-021. Jason's chain-rule and one-zero sanity check say that
for the fixed quotient `Xi_chi(2s-1)/Xi_chi(2s)`, the positive strip-edge
kernel contributes to `-1/2 Phi'/Phi`, not `+1/2 Phi'/Phi`. This conflicts
with earlier positive-exponent normalization unless the team changes the phase
sign, defines `q=-Theta'`, or inverts the quotient.

Capture action: refined `findings.md`, UV-016 in `uv.md`, filed UV-021, and
logged the attempt. Sartre was redelegated to adversarially audit the sign
claim before any promotion.

## Beauvoir Deposit 20260424

Report:
`agents/20260424-183416-gap-compact-regularization/report.md`.
Proof note:
`agents/20260424-183416-gap-compact-regularization/notes/compact_regularization_reduction.md`.

Verdict: keep candidate. Beauvoir reduces the compact zero-regularization part
of UV-016 to Hadamard edge-difference cancellation: subtracting the two edge
logarithmic-derivative sums cancels the genus-one constant and `1/rho`
regularizers, leaving an `O_I(|rho|^{-2})` summand and uniform convergence on
compact intervals away from edge zeros. This is not promoted yet because it
requires adversarial/source audit and standard completed-\(L\) source checks.

Capture action: recorded the candidate reduction in `findings.md`, UV-016, and
`attempts.md`. Sartre was queued to audit the convergence proof after the sign
audit.

## Sartre Follow-Up Audits 20260424

Reports:
`agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md` and
`agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md`.
Script:
`agents/20260424-183416-verifier-slot-skeleton/scripts/audit_one_zero_sign.py`.

Verdicts: keep. The sign audit confirms Jason's objection: for the fixed
paired quotient, the positive strip-edge source is `-1/2 Phi'/Phi`; the old
positive-exponent recommendation is inconsistent as written. The safest
convention is fixed quotient, `Phi(1/2+it)=e^{-2iTheta(t)}`, and `q=Theta'`.
The compact-convergence audit accepts Beauvoir's Hadamard edge-difference proof
under standard primitive nonprincipal completed-function inputs. It proves only
the completed zero-regularization layer, not the full `B_chi^pair` source
identity.

Capture action: corrected stale paired sign wording in
`notes/dirichlet_paired_source.md` and
`paper/dirichlet_paired_source_candidate.tex`, refined `findings.md`, UV-016,
UV-021, `attempts.md`, and this collation. Next target is the explicit
`B_chi^pair` background split in the verified convention.

## Follow-Up Wave 20260424

Queued:

- Jason continues in
  `agents/20260424-183416-explorer-background-multiplicity/` with
  `report-background-split.md`: derive the explicit `B_chi^pair` background
  split in the fixed-quotient, negative-exponent convention, or reduce it to
  precise missing substatements.
- Beauvoir continues in
  `agents/20260424-183416-gap-compact-regularization/` with
  `report-source-audit.md`: source-audit the standard primitive nonprincipal
  completed-\(L\) inputs used by the compact edge-difference proof.

Reason: these two lanes are independent. Jason attacks the remaining
normalization/source identity content of UV-016, while Beauvoir hardens the
source citations behind the convergence lemma Sartre accepted.

## Jason Background-Split Deposit 20260424

Report:
`agents/20260424-183416-explorer-background-multiplicity/report-background-split.md`.
Note:
`agents/20260424-183416-explorer-background-multiplicity/notes/background_split_derivation.md`.

Verdict: keep, not promoted. In the sign-audited fixed-quotient convention,
Jason reduces the clean source-package formulation to completed-Hadamard
normalization: after summing all completed zeros of
`Xi_chi=Lambda_chi Lambda_bar_chi` with multiplicity, the residual background
is `B_chi,comp^pair=0`. The older gamma/trivial-zero/pole/Hadamard component
list is still meaningful only as a separate raw `L`-factor bookkeeping
convention. Mixing the two would double-count background structure.

Capture action: refined `findings.md`, UV-016 in `uv.md`, and `attempts.md`.
Next verifier question: cite the standard primitive completed-\(L\) package and
adversarially check that the completed-zero theorem wording does not also add
raw gamma/trivial-zero terms.

## Beauvoir Source-Audit Deposit 20260424

Report:
`agents/20260424-183416-gap-compact-regularization/report-source-audit.md`.
Note:
`agents/20260424-183416-gap-compact-regularization/notes/source_audit_standard_inputs.md`.

Verdict: keep. The completed-\(L\) input layer for the compact
edge-difference proof is mathematically standard for primitive nonprincipal
characters: parity-normalized completed functions, entire order one, paired
self-dual product, analytic multiplicity, genus-one Hadamard/log-derivative
regularization, and square-summability of nonzero zeros. The remaining source
problem is bibliographic precision rather than a new analytic theorem.

Capture action: refined `findings.md`, UV-016 in `uv.md`, and `attempts.md`.
Next source task: replace web-level locators with exact textbook citations
before any paper promotion.

## Verifier Wave 20260424

Queued:

- Sartre continues in
  `agents/20260424-183416-verifier-slot-skeleton/` with
  `report-source-normalization-audit.md`: adversarially check Jason's
  completed-Hadamard `B_chi,comp^pair=0` proposal against sign, real-part,
  edge-exclusion, and double-counting risks.
- Beauvoir continues in
  `agents/20260424-183416-gap-compact-regularization/` with
  `report-textbook-citation-pass.md`: replace the completed-\(L\) input
  locators with exact textbook citations where possible, or mark the remaining
  bibliographic checks precisely.

Reason: UV-016 now has a plausible compact source-package core, but promotion
still needs adversarial normalization review and citation-grade source support.

## Sartre Source-Normalization Audit 20260424

Report:
`agents/20260424-183416-verifier-slot-skeleton/report-source-normalization-audit.md`.

Verdict: keep, still open. Sartre accepts the completed-Hadamard
`B_chi,comp^pair=0` subclaim inside explicit completed normalization, but not
as an unqualified `B_chi^pair` theorem statement. The theorem text must state
the real-part projection, the negative-exponent boundary convention, regular
compact edge exclusions, and the rule that raw gamma/trivial-zero/pole
bookkeeping belongs only in a separate raw `L`-factor remark.

Capture action: refined `findings.md`, UV-016, UV-021, and `attempts.md`.
Next writing task: draft the completed-source theorem wording without claiming
UV-017 slot realization.

## Beauvoir Textbook-Citation Pass 20260424

Report:
`agents/20260424-183416-gap-compact-regularization/report-textbook-citation-pass.md`.

Verdict: keep, citation burden narrowed. Davenport's `Multiplicative Number
Theory`, chapters 9, 11, 12, and 17, gives strong OCR locators for primitive
Dirichlet completed functions, order-one Hadamard products, zero summability,
and Dirichlet log-derivative formulae. The OCR is too symbol-corrupted for
final paper citations; exact page/equation references must be checked against
a clean copy or replaced by Montgomery-Vaughan/Apostol-level references.

Capture action: refined `findings.md`, UV-016, and `attempts.md`. The
remaining source task is clean-copy citation verification, not a new analytic
lemma.

## Coordinator Paper-Updates Draft 20260424

File: `paper-updates.md`.

Verdict: keep as staged text only. The draft states the completed-Hadamard
paired source package with `B_chi,comp^pair=0`, makes the real-part projection
and edge exclusions explicit, and separates raw `L`-factor gamma/trivial-zero
bookkeeping into a remark. It carries citation placeholders rather than final
book citations.

Capture action: recorded the staged draft in `findings.md`, UV-016, and
`attempts.md`. Do not promote until clean-copy citations and final wording
review are complete.

## Sartre Paper-Updates Audit 20260424

Report:
`agents/20260424-183416-verifier-slot-skeleton/report-paper-updates-audit.md`.

Verdict: keep, still open. Sartre found the staged theorem mathematically close
to promotion modulo citations. Signs, derivative bridge, compact convergence,
edge exclusions, primitive nonprincipal scope, raw/completed separation, and
nonclaim of UV-017/GRH are all in the right shape. The blocking wording issue
was multiplicity: the first draft said `Z(Xi_chi)` was a zero multiset while
also multiplying by `m_rho`, which could double-count. Two smaller fixes were
also requested: state the boundary phase is real `C^1`, and add a
realness/projection sentence for `D_chi`.

Capture action: patched `paper-updates.md` with the three requested wording
fixes, then refined `findings.md`, UV-016, and `attempts.md`. A final wording
pass is still needed before promotion.

## Beauvoir Citation-Fallback Plan 20260424

Report:
`agents/20260424-183416-gap-compact-regularization/report-citation-fallback-plan.md`.

Verdict: keep. Clean Davenport verification is not a hard blocker for a
working-paper draft if the source-input lemma uses stable DLMF references for
Dirichlet facts, includes a short order-one derivation from DLMF plus
Stirling, and cites a standard complex-analysis Hadamard factorization theorem.
Clean Davenport/Montgomery-Vaughan references remain a final bibliography
upgrade.

Capture action: updated `paper-updates.md` citation placeholders, refined
`findings.md`, UV-016, and `attempts.md`. Full UV-016 still waits on final
wording review and a promotion decision.

## Sartre Final Paper-Updates Check 20260424

Report:
`agents/20260424-183416-verifier-slot-skeleton/report-paper-updates-final-check.md`.

Verdict: terminal for the wording lane. After the coordinator's fixes, Sartre
clears the staged completed-Hadamard source theorem as mathematically
promotion-ready modulo citation quality. The distinct-zero multiplicity
convention, real `C^1` phase, real/projection wording for `D_chi`, sign bridge,
compact convergence, primitive nonprincipal scope, edge exclusions, and
raw/completed separation all pass. The staged text does not claim UV-017 slot
realization or any GRH consequence.

Capture action: refined `paper-updates.md`, `findings.md`, UV-016, and
`attempts.md`. Remaining decision: promote as a working source theorem with the
DLMF/Hadamard fallback citation stack, or wait for clean-copy textbook
citations.

Coordinator decision: keep UV-016 live for now. The GRH directory currently has
no canonical `grh/<main>.tex` promotion target, so the verified theorem remains
staged in `paper-updates.md` rather than promoted/removed from `uv.md`.
