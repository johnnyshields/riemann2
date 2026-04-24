## Claim

For the fixed quotient
\[
\Phi_\chi^{\mathrm{pair}}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s),
\]
Jason's sign claim is correct in the narrow one-zero sense: the positive
strip-edge kernel
\[
K_\rho(t)=\Re\left({1\over 1+2it-\rho}-{1\over 2it-\rho}\right)
\]
is the contribution to \(-\frac12(\Phi_\chi^{\mathrm{pair}\,\prime}/
\Phi_\chi^{\mathrm{pair}})(1/2+it)\), not to \(+\frac12\) of that
logarithmic derivative.

This is a genuine conflict with
`agents/20260424-155603-paired-quotient-normalization-routeA/report.md` as
written. That report uses the same quotient, the positive exponent
\(e^{2i\Theta}\), and \(q=\Theta'\); it does not invert the quotient, define
\(q=-\Theta'\), or define the source term as the negative of the positive
strip-edge kernel. Its bridge calculation is correct for the named phase, but
it did not check the zero-kernel sign.

Safest convention decision: keep the fixed quotient and use
\[
\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad q_\chi^{\mathrm{pair}}=(\Theta_\chi^{\mathrm{pair}})'
\]
for the positive-source package. Equivalently,
\[
q_\chi^{\mathrm{pair}}=-\frac12
(\Phi_\chi^{\mathrm{pair}\,\prime}/\Phi_\chi^{\mathrm{pair}})(1/2+it)
\]
at the zero-source level. Keeping \(e^{2i\Theta}\) would require defining
\(q=-\Theta'\) or inverting the quotient; both are viable algebraically but are
larger convention changes. Until the source theorem is rewritten in one
consistent convention, quarantine the older positive-exponent recommendation.

## Status

proved

## Evidence

**Proved.**

- Chain rule for the fixed quotient gives
  \[
  {\Phi'\over\Phi}(s)=2{\Xi'\over\Xi}(2s-1)-2{\Xi'\over\Xi}(2s).
  \]
  A zero \(\rho\) of \(\Xi_\chi\) therefore contributes
  \(2((2it-\rho)^{-1}-(1+2it-\rho)^{-1})\) on \(s=1/2+it\). Taking real parts,
  this is \(-2K_\rho(t)\). See
  `agents/20260424-183416-explorer-background-multiplicity/report.md:9-25`
  and `:47-55`.
- The positive kernel definition is already fixed independently by the
  strip-edge note:
  \[
  K_\rho(t)=
  {1-\beta\over(1-\beta)^2+(2t-\gamma)^2}
  +{\beta\over \beta^2+(2t-\gamma)^2}>0.
  \]
  See `paper/strip_edge_kernel_note.tex:29-55`.
- My independent script confirms the sign on three sample zeros. Output:
  `K=4 fixed_plus_half=-4 fixed_minus_half=4 inverse_plus_half=4`;
  `K=1.40472410641 fixed_plus_half=-1.40472410641 fixed_minus_half=1.40472410641 inverse_plus_half=1.40472410641`;
  `K=3.68383766825 fixed_plus_half=-3.68383766825 fixed_minus_half=3.68383766825 inverse_plus_half=3.68383766825`.
  Script:
  `agents/20260424-183416-verifier-slot-skeleton/scripts/audit_one_zero_sign.py:1-27`,
  SHA256 `AB1F79B936547C7B73275E51A328E641F9ACCFE6EADF900564B3ECF11B4EC681`.
- The phase bridge itself is not disputed: if
  \(\Phi(1/2+it)=e^{2i\Theta(t)}\), then
  \((\Phi'/\Phi)(1/2+it)=2\Theta'(t)\); if
  \(\Phi(1/2+it)=e^{-2i\Theta(t)}\), then
  \((\Phi'/\Phi)(1/2+it)=-2\Theta'(t)\). The older route correctly records this
  bridge but chooses the sign opposite to the positive zero-kernel convention.
  See `agents/20260424-155603-paired-quotient-normalization-routeA/report.md:7-27`
  and `:43-56`.

**Conditional.**

- The conclusion assumes the source scalar \(S_\chi^{\mathrm{pair}}\) is meant
  to be the positive strip-edge zero sum \(+\sum_\rho m_\rho K_\rho\). If a
  future theorem deliberately defines the source scalar with the opposite sign,
  the convention decision changes, but that would no longer be the positive
  strip-edge source described in the current notes.
- Inverting the quotient would make the positive kernel appear in
  \(+\frac12(\Phi^{-1})'/\Phi^{-1}\), but it changes the front-end object that
  the paired source notes currently fix.

**Missing.**

- A theorem-ready paired source-normalization subsection tying quotient,
  boundary phase, \(q\), \(B_\chi^{\mathrm{pair}}\), and
  \(S_\chi^{\mathrm{pair}}\) together in the same sign convention.
- A compact regularized source identity; this sign audit only checks the
  one-zero convention.

## Baseline / delta

Baseline: routeA recommended keeping the fixed quotient,
\(e^{2i\Theta}\), and \(q=\Theta'\), giving \(q=+\frac12\Phi'/\Phi\). Jason
claimed that this makes the positive zero contribution sign-reversed.

Delta: the one-zero calculation verifies Jason's objection. The earlier route
was not using a different quotient or a hidden \(q=-\Theta'\) convention; it
made a front-end phase choice that is incompatible with the positive
strip-edge kernel for the fixed quotient.

## Attempt status

keep

## Exact refs

- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report.md:3-25`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report.md:47-55`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-explorer-background-multiplicity/report.md:69-73`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeA/report.md:3-35`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeA/report.md:43-56`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeB/report.md:3-14`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeB/report.md:42-52`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-39`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:29-55`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/dirichlet_paired_source_package_candidate.tex:24-53`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:38-62`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/paper/strip_edge_kernel_note.tex:29-55`
- `grh/teams/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-183416-verifier-slot-skeleton/scripts/audit_one_zero_sign.py:1-27`

## Dependencies

- Fixed quotient orientation
  \(\Xi_\chi(2s-1)/\Xi_\chi(2s)\).
- Positive strip-edge kernel convention \(K_\rho(t)>0\) as in
  `strip_edge_kernel_note.tex`.
- Boundary intervals avoiding zeros and singularities so a continuous phase is
  available.
- Standard log-derivative convention that zeros contribute
  \((z-\rho)^{-1}\) with analytic multiplicity.

## Strongest objection

This resolves only the zero-source sign. It does not prove the full
\(q_\chi^{\mathrm{pair}}=B_\chi^{\mathrm{pair}}+S_\chi^{\mathrm{pair}}\)
identity, and a future source theorem could choose the inverse quotient or
define \(q=-\Theta'\) instead. The objection to routeA is therefore a convention
conflict, not a proof that the paired source theorem itself is false.

## Needed for promotion

1. Rewrite the paired source-normalization interface in one place with the
   fixed quotient, boundary phase, log-derivative bridge, and \(q=B+S\) sign.
2. If keeping the fixed quotient and positive kernel, adopt
   \(e^{-2i\Theta}\), \(q=\Theta'\), and
   \(q=-\frac12\Phi'/\Phi\).
3. If the coordinator prefers \(e^{2i\Theta}\), explicitly choose between
   \(q=-\Theta'\) and the inverse quotient; do not leave the positive source
   sign implicit.
4. Recompute the \(B_\chi^{\mathrm{pair}}\) bookkeeping in the chosen sign
   convention before promoting any source-package statement.

## Autoresearch next step

continue: after the sign convention is quarantined, audit whether the compact
zero-regularization proof actually gives uniform convergence of the paired
edge-difference zero series, separate from all \(B_\chi^{\mathrm{pair}}\)
background bookkeeping.
