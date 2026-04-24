# UV-015 verifier report: nonbenchmark finite-jet genericity

## Claim

The gap report is correct enough for promotion after scope-tightening. It proves
a first-order, value-channel-free `O_1` finite-jet genericity theorem: for
normalized real `C^2` curves with nonzero endpoint velocities in dimension at
least `3`, endpoint overlap and the first `O_1` line-angle scalar are locally
functionally independent on the open endpoint-2-jet locus where
`Delta = det d(I,C)/d(u,v)` is nonzero and `C=<T_u,T_v>` is on a nonzero branch.

This closes UV-015 if the promoted claim is exactly this finite-jet `O_1`
genericity theorem. It does not close a broader theorem for all higher
`O_r/A_r` observables, all finite-dimensional model families without a rank
hypothesis, or holomorphic complex-Zariski genericity.

## Status

proved

## Evidence

Proved:

1. The endpoint formulas in the gap report are correct in the real setting. For
   a normalized curve with endpoint data `(x,a,b)` and `(y,c,d)`, the constraints
   are `<a,x>=0`, `<b,x>=-||a||^2`, and the analogous equations at `y`. With
   `T_x=a/||a||`, differentiating the unit tangent gives
   `dT_x/du = (I - T_x T_x^*)b/||a||` in the real inner-product sense. Hence
   `d_u I=<a,y>`, `d_v I=<x,c>`, `d_u C=<U_x,T_y>`, `d_v C=<T_x,U_y>`, and
   `Delta=<a,y><T_x,U_y>-<x,c><U_x,T_y>` as claimed in the primary report
   `agents/20260424-193527-gap-nonbenchmark-genericity/report.md:23-50`.
2. The explicit seed jet is admissible. I reran the primary script
   `agents/20260424-193527-gap-nonbenchmark-genericity/scripts/verify_o1_jet_determinant.py`
   with SHA256 `9290A89C67780A4D35DC3B5E19892B1135E39B643170D2B55F55D2CA6680FD13`;
   it returns the normalized-jet constraints, `C = 1/2`, and
   `Delta = 1/4*sqrt(2)`. I also wrote and ran an independent exact-arithmetic
   check at
   `agents/20260424-194246-verifier-nonbenchmark-genericity/scripts/verify_uv015_seed.py`
   with SHA256 `85F3F3E3A40A74F2DD851727C78FCEC67417C02FE263D06AC0601BB4C9949D5D`.
   Its output includes `C = 1/2`, `d_u_C = -1/2 - 1/2*sqrt(2)`,
   `d_v_C = -1/2*sqrt(2)`, and `Delta = 1/4*sqrt(2)`.
3. Nonzero determinant gives the advertised genericity on a finite-dimensional
   endpoint-jet chart. After clearing the nonzero velocity denominators, the
   determinant is a real polynomial on the admissible jet chart. The seed above
   proves that this polynomial is not identically zero. Therefore its nonzero
   locus is Euclidean open dense on the relevant connected smooth chart, and
   real-Zariski open dense where the chart is treated algebraically. The word
   "hypersurface" is acceptable if read as "proper algebraic zero set"; the
   paper wording should not require smoothness of that zero set.
4. The Hermite/local-sphere realization step is sound. In the chart
   `z in x^\perp -> (x+z)/sqrt(1+||z||^2)`, a curve with
   `z(0)=0`, `z'(0)=a`, and `z''(0)=b+||a||^2 x` realizes the admissible
   endpoint 2-jet `(x,a,b)`. The vector `b+||a||^2 x` lies in `x^\perp`
   exactly because `<b,x>=-||a||^2`. The same construction applies at `y`, and
   disjoint supports near the two distinct parameter values allow independent
   small endpoint-jet perturbations. Thus the finite-jet open dense statement
   transfers to the `C^2` curve space on the nonzero-velocity locus.
5. The finite-dimensional family pullback statements are correct with standard
   rank hypotheses. If the endpoint-2-jet map of a smooth family is submersive
   onto an open chart, the preimage of the nonzero-`Delta` locus is open dense.
   If the family is real analytic and connected, a pulled-back determinant that
   is not identically zero has a zero set with empty interior. For algebraic
   parameter spaces, this should be stated componentwise or on an irreducible
   smooth component; mere connectedness of a reducible real algebraic set is not
   the right hypothesis.

Conditional:

- The complex-Hilbert statement is acceptable only as a realified finite-jet
  statement, or after separately choosing a smooth nonzero branch of
  `|<T_u,T_v>|` or `|<T_u,T_v>|^2`. Do not state a holomorphic-Zariski theorem.
- The first-order theorem supports the paper's current `O_r` role split and
  benchmark narrative in `quantum/paper/jet_gram_quantum_note.md:343-370` and
  `quantum/paper/jet_gram_quantum_note.md:691-796`. It does not supply the
  missing determinants for `A_1`, higher `O_r/A_r`, or simple-spectrum
  multi-angle branches.

Missing:

- No residual substatement is needed to close UV-015 for first-order `O_1`
  structural genericity.
- Separate future work would be needed for higher-order genericity or for a
  source-specific family that does not have a submersive or non-identically-zero
  endpoint-jet determinant pullback.

## Baseline / delta

Baseline: the note already had benchmark-family evidence: qutrit/quartit and
Veronese richer-than-overlap results, plus spherical-twist non-Veronese
witnesses. The live UV asked for a theorem-level genericity mechanism beyond
those examples (`uv.md:7-10`; `attempts.md:14-15`).

Delta: this verification accepts the gap report's finite-jet determinant route.
The benchmark reports remain supporting context, but the proof now rests on the
nonzero endpoint-2-jet polynomial determinant and local endpoint-jet
realization. This is a genuine structural theorem for first-order `O_1`, not
another isolated example.

## Attempt status

terminal

## Exact refs

- Target: `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md:7-10`.
- Current run ledger: `quantum/teams/20260423-043347-research-team-jet-gram-qm/attempts.md:14-15`.
- Primary report: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-193527-gap-nonbenchmark-genericity/report.md:5-69`, `:77-142`, `:185-210`.
- Primary script: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-193527-gap-nonbenchmark-genericity/scripts/verify_o1_jet_determinant.py:80-115`, SHA256 `9290A89C67780A4D35DC3B5E19892B1135E39B643170D2B55F55D2CA6680FD13`, rerun output `C = 1/2`, `Delta = 1/4*sqrt(2)`.
- Independent verifier script: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-194246-verifier-nonbenchmark-genericity/scripts/verify_uv015_seed.py:83-125`, SHA256 `85F3F3E3A40A74F2DD851727C78FCEC67417C02FE263D06AC0601BB4C9949D5D`, output `C = 1/2`, `Delta = 1/4*sqrt(2)`.
- Note context: `quantum/paper/jet_gram_quantum_note.md:35-49`, `:343-370`, `:423-488`, `:691-796`, `:798-852`.
- Findings context: `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md`, read in full; especially the current Missing and Candidate expansions near the end.
- Benchmark provenance read: `agents/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md`, `agents/20260423-194242-attack-veronese-richness/reports/gap-veronese-richness.md`, `agents/20260423-192859-attack-Or-veronese/reports/gap-Or-veronese-theorem.md`, `agents/20260423-194725-attack-Or-richness/reports/gap-Or-richness.md`, `agents/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md`, `agents/20260423-133641-attack-qutrit-omega/reports/gap-qutrit-omega.md`, `agents/20260423-133641-attack-qutrit-omega/reports/gap-qutrit-witness.md`, `agents/20260423-144313-attack-quartit-O2/reports/gap-quartit-O2.md`, `agents/20260423-204337-attack-nonveronese/reports/gap-spherical-twist.md`, `agents/20260423-215017-attack-spherical-witness/reports/gap-spherical-witness.md`, and `agents/20260424-033611-attack-twist-family/reports/gap-twist-family.md`.

## Dependencies

- Elementary differential geometry of normalized real sphere curves.
- Endpoint 2-jet evaluation and Hermite interpolation in local sphere charts.
- The existing note decision that `O_r` is the horizontal/value-channel-removed
  object and that principal-angle data is the canonical subspace-level output.
- Real analytic zero-set facts for the analytic-family pullback statement.
- Componentwise or irreducible-component interpretation for algebraic-family
  pullbacks.

## Strongest objection

The only real objection is overstatement. The determinant proof is first-order,
real finite-jet, and branch-local. It does not prove that every natural
higher-order `O_r/A_r` observable is generically richer than overlap, and it
does not prove holomorphic complex-algebraic genericity. The algebraic-family
line in the primary report also needs componentwise wording. These are wording
constraints, not defects in the `O_1` theorem.

## Needed for promotion

Promote a scoped proposition along these lines:

"For normalized real `C^2` curves in a fixed finite-dimensional Hilbert space
of dimension at least `3`, with nonzero endpoint velocities, local independence
of endpoint overlap and the first value-channel-free `O_1` line-angle scalar is
detected by an endpoint-2-jet determinant. The nonvanishing of this determinant
is an open dense condition on the admissible endpoint-2-jet chart. Consequently,
any smooth finite-dimensional curve family whose endpoint-2-jet map is
submersive onto such a chart, and any connected real-analytic family on which
the pulled-back determinant is not identically zero, has an open dense locus
where the `O_1` line-angle data is not locally determined by overlap alone."

Add, if needed:

"The same finite-jet argument may be read on the underlying real jet space of a
complex Hilbert space, on a branch where the chosen absolute principal-angle
observable is smooth. No holomorphic-Zariski statement is claimed."

Avoid:

- "generic for all `O_r/A_r` observables";
- "generic in every finite-dimensional family" without submersive or
  non-identically-zero determinant hypotheses;
- "holomorphic genericity" or "complex Zariski open" for absolute-value
  observables;
- "canonical matrix genericity" rather than principal-angle/line-angle
  genericity;
- an unqualified algebraic-family claim on reducible parameter spaces.

Ledger destination: `attempts.md` should record this verifier route as
`terminal`; `paper-updates.md` or the paper should receive the scoped proposition
above; `uv.md` can remove UV-015 in the same promotion commit if the coordinator
uses this exact scope.

## Autoresearch next step

terminal: accept the primary gap report for promotion with the wording
constraints above. If redelegated, the next bounded check is not UV-015 closure
but a separate higher-order determinant problem for `A_1` or higher `O_r/A_r`.
