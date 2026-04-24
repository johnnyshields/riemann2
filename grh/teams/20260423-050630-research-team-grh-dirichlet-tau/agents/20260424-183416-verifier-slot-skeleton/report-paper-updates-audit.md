## Claim

The staged `paper-updates.md` completed-Hadamard theorem is mathematically close
to promotion as a UV-016 source-package statement, modulo citation cleanup, but
it is not quite promotion-ready as written. The sign, quotient derivative
bridge, edge exclusions, compact convergence scope, raw/completed separation,
primitive nonprincipal restriction, and nonclaim of UV-017/GRH are all in the
right shape. The blocking wording issue is multiplicity: the draft says
\(Z(\Xi_\chi)\) is the completed zero multiset and also multiplies by
\(m_\rho\), which can be read as double-counting. Two smaller precision edits
are also needed: make the boundary phase real \(C^1\) (or smooth), and state
explicitly that \(D_\chi(t)\) is real in the chosen boundary convention, or that
the source identity is the real-part-projected scalar identity.

Honest verdict: keep the staged theorem; do not promote until the smallest
wording edits below are made. No new mathematical obstruction appears from this
audit.

## Status

open

## Evidence

**Proved.**

- The fixed quotient and sign convention match the adversarial sign audit:
  \[
  \Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta(t)},\qquad
  q=\Theta',
  \qquad
  q=-\frac12(\Phi'/\Phi)(1/2+it).
  \]
  See `paper-updates.md:16-40` and `report-sign-audit.md:3-37`.
- The derivative bridge is correct. With
  \(D_\chi(t)=\Xi_\chi'/\Xi_\chi(1+2it)-\Xi_\chi'/\Xi_\chi(2it)\), the fixed
  quotient gives \((\Phi_\chi^{\mathrm{pair}\,\prime}/
  \Phi_\chi^{\mathrm{pair}})(1/2+it)=-2D_\chi(t)\). The staged draft records
  the compatible scalar form \(q=\Re D_\chi\). See `paper-updates.md:42-58` and
  `report-source-normalization-audit.md:1-38`.
- The compact convergence claim matches the checked completed-Hadamard
  regularization: the edge-difference summand is \(O_I(|\rho|^{-2})\), giving
  absolute uniform convergence on \(I\), and fixed \(t\)-derivatives are also
  summable. See `paper-updates.md:62-63` and
  `report-compact-convergence-audit.md:3-28`, `:38-86`.
- The primitive nonprincipal scope and edge exclusions are present. See
  `paper-updates.md:16-27`.
- The raw/completed separation is correct: the theorem uses completed zeros,
  declares \(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\), and the separate remark
  forbids adding gamma, trivial-zero, pole, conductor, or Hadamard-exponential
  terms to the completed-zero theorem. See `paper-updates.md:65-98`.
- The staged text does not claim UV-017 slot realization, local whitening,
  GRH/ERH, tau, or any downstream contradiction theorem. It is a Stage 1
  source-package replacement only. See `paper-updates.md:7-11`.

**Conditional.**

- Promotion remains conditional on Beauvoir's citation lane replacing
  placeholders with clean-copy references for the primitive nonprincipal
  completed-\(L\) package and Hadamard product inputs. This audit does not
  re-check those citations. See `paper-updates.md:101-111`.
- The equality \(q=\Re D_\chi\) is safe as a scalar source identity, but the
  text should not leave a possible gap between the complex identity
  \(q=-\frac12\Phi'/\Phi\) and the real-part-projected zero sum. Add a phrase
  saying the chosen real boundary phase makes \(D_\chi(t)\) real, or that all
  displayed source identities after \(D_\chi\) are real-part projections.

**Missing.**

- Replace "where \(Z(\Xi_\chi)\) is the completed zero multiset and \(m_\rho\)
  is analytic multiplicity" with one nonambiguous convention:
  either "the sum runs over distinct zeros \(\rho\) of \(\Xi_\chi\), and
  \(m_\rho\) is their analytic multiplicity", or "the sum runs over the
  completed zero multiset, with no \(m_\rho\) coefficient." The current wording
  at `paper-updates.md:52-61` and `:75-82` can be read as multiplying
  multiplicity twice.
- State that \(\Theta_\chi^{\mathrm{pair}}\) is a real \(C^1\) (indeed smooth)
  boundary phase on \(I\), so \(q=\Theta'\) is defined. See
  `paper-updates.md:27-33`.
- Add one sentence after the definition of \(D_\chi\): "With this convention
  \(D_\chi(t)\) is real; we write \(\Re D_\chi\) only to match the scalar kernel
  formula." Equivalently, consistently write the source formula as a real-part
  identity and avoid implying an unchecked complex equality.

No computation was run for this audit.

## Baseline / delta

Baseline: prior audits accepted the fixed-quotient negative-exponent sign,
completed edge-difference convergence, and completed-Hadamard
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\) normalization, while requiring an
explicit theorem/remark split to avoid raw-background double-counting.

Delta: the coordinator's staged draft implements that theorem/remark split
well enough that only wording-level normalization fixes remain before the
mathematical statement is promotion-ready modulo citations.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:3-5`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:7-11`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:16-40`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:42-63`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:65-83`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:86-98`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper-updates.md:101-117`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md:3-37`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-sign-audit.md:47-89`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:3-28`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-compact-convergence-audit.md:38-104`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-source-normalization-audit.md:1-38`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/report-source-normalization-audit.md:40-104`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:5-31`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/uv.md:66-90`

## Dependencies

- Beauvoir citation lane for exact primitive nonprincipal completed
  Dirichlet \(L\)-function and Hadamard-product citations.
- Fixed quotient convention
  \(\Phi_\chi^{\mathrm{pair}}=\Xi_\chi(2s-1)/\Xi_\chi(2s)\).
- Sign-audited boundary convention
  \(\Phi=e^{-2i\Theta}\), \(q=\Theta'\), equivalently
  \(q=-\frac12\Phi'/\Phi\).
- Completed-Hadamard normalization: \(S_{\chi,\mathrm{comp}}^{\mathrm{pair}}\)
  sums completed zeros of \(\Xi_\chi\), while raw \(L\)-factor background terms
  stay outside the completed theorem.

## Strongest objection

The multiplicity wording can accidentally double-count zeros. A "zero multiset"
already carries multiplicity, while the displayed formula also multiplies by
\(m_\rho\). This is not a deep proof gap, but it is promotion-blocking because
UV-016 explicitly requires multiplicity bookkeeping compatible with the same
compact identity.

## Needed for promotion

1. Change the zero-sum wording to one convention:
   "sum over distinct zeros with coefficient \(m_\rho\)" or "sum over the
   zero multiset with no \(m_\rho\)" in both displayed sums.
2. Say \(\Theta_\chi^{\mathrm{pair}}\) is real \(C^1\) or smooth on \(I\).
3. Add one realness/projection sentence after \(D_\chi\): either
   \(D_\chi(t)\in\mathbb R\) under this boundary convention, or the source
   identity is explicitly the real-part projection of the edge difference.
4. Keep the raw-bookkeeping remark separate and do not add raw gamma,
   trivial-zero, pole, conductor, or Hadamard-exponential terms to the completed
   theorem.
5. After those wording edits and Beauvoir's clean-copy citations, the Stage 1
   completed-Hadamard source theorem is promotion-ready from this verifier
   lane.

## Autoresearch next step

verify: after the coordinator applies the three wording edits, do one final
line-by-line check of the revised staged theorem against UV-016 and UV-021
before promotion.
