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
