## Claim

The safest theorem-facing stance is:

- Proved: the paired Dirichlet note is currently safest when it states only the sign-free strip-edge quotient object
  `\Phi_\chi^{\mathrm{pair}}(s)=\Xi_\chi(2s-1)/\Xi_\chi(2s)`
  with `\Xi_\chi(s)=\Lambda(s,\chi)\Lambda(s,\bar\chi)`.
- Conditional on introducing a boundary phase variable and keeping the manuscript normalization `q_\chi^{\mathrm{pair}}=(\Theta_\chi^{\mathrm{pair}})'` together with a positive source split, the safest mirrored convention is
  `\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{2 i \Theta_\chi^{\mathrm{pair}}(t)}`,
  so that
  `((\Phi_\chi^{\mathrm{pair}})'/\Phi_\chi^{\mathrm{pair}})(1/2+it)=2 q_\chi^{\mathrm{pair}}(t)`.
- Missing: a theorem-sized paired-source statement that fixes exact local-slot identification and explicitly ties the quotient's logarithmic derivative to the manuscript's paired `S(m)` slot. Until that exists, the paired theorem-facing note should not assert a sign-sensitive derivative identity as if it were already canonical.

So the RH-side sign repair should be mirrored in the paired notes only as a normalization guardrail, not as a new standalone theorem claim. If the note remains object-level, the safest text is to stay sign-free. If it introduces phase notation, it should adopt the same positive-exponent convention package as the repaired zeta-side notes.

## Status

heuristic

## Evidence

- `notes/quotient_normalization.md:18-39` isolates the zeta-side issue: with the archived negative boundary phase one gets `((\phi')/\phi)(1/2+it)=-2q(t)`, while a positive `q=B_\zeta+S` normalization is cleanly preserved by switching to `\phi(1/2+it)=e^{2 i \Phi(t)}`.
- `notes/quotient_phase.md:15-17,36-43` upgrades the completed quotient only at the phase-channel level and explicitly says the paired `((\chi,\bar\chi))` route is still the conservative scalar-amplitude target. That means the paired theorem-facing note should avoid taking on extra sign-sensitive commitments unless it needs them.
- `notes/dirichlet_paired_source.md:29-55,82-87` already presents the clean theorem-facing paired object as the quotient `\Phi_\chi^{\mathrm{pair}}`, but it does not yet fix a boundary exponent convention or a derivative-to-source sign. So there is no direct paired statement to "correct" yet; the gap is ambiguity, not an established wrong sign.
- Because the paired note is intentionally theorem-facing and conservative, the least risky update is a wording guard that either defers phase normalization to the common source-normalization subsection or, if phase is named, matches the repaired zeta-side positive-exponent convention.

## Exact refs

- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:18-39`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:15-17`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_phase.md:36-43`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:29-55`
- `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:82-87`
- Target deposit: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/agents/20260424-155603-paired-quotient-normalization-routeB/report.md`

## Dependencies

- The zeta-side normalization conclusion that the sign issue lives in the boundary-phase convention, not in the factor of `2`.
- The phase-channel result that the completed quotient is naturally unimodular on `\Re(s)=1/2` under the standard completed-`L` functional equation and conjugation symmetry.
- The paired-source note's existing decision to make the quotient itself, rather than the raw product, the theorem-facing paired object.

## Strongest objection

The recommendation to use the positive exponent in the paired note is only a consistency choice, not something independently proved necessary by the paired-source note itself. Since the paired theorem is still missing exact local-slot identification, one could argue that any explicit phase convention is premature and that the note should simply remain quotient-only until a full source theorem exists.

## Needed for promotion

- Decide whether the paired theorem-facing note will remain strictly quotient-level or will explicitly introduce a boundary phase / `q_\chi^{\mathrm{pair}}` notation.
- If it remains quotient-level, update the warning text to say that phase/sign normalization is deferred to the common source-normalization package.
- If it introduces phase notation, add one sentence of the form:
  `When a boundary phase is used, fix \Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{2 i \Theta_\chi^{\mathrm{pair}}(t)} and q_\chi^{\mathrm{pair}}=(\Theta_\chi^{\mathrm{pair}})'; then ((\Phi_\chi^{\mathrm{pair}})'/\Phi_\chi^{\mathrm{pair}})(1/2+it)=2 q_\chi^{\mathrm{pair}}(t).`
- Avoid any theorem-facing sentence that combines the quotient with a negative boundary exponent and a positive `q`-split unless the minus sign in the logarithmic-derivative bridge is written explicitly.
