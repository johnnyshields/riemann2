# UV-015 gap report: nonbenchmark genericity

## Claim

There is a clean finite-jet genericity theorem for richer-than-overlap behavior.

Let \(H_\mathbb R\) be a real Hilbert space with \(\dim H_\mathbb R\ge 3\), fix
two distinct parameter values \(u_0\ne v_0\), and consider \(C^2\) normalized
curves \(\psi:I\to S(H_\mathbb R)\) with nonzero endpoint velocities. Define
\[
I_\psi(u,v)=\langle \psi(u),\psi(v)\rangle,\qquad
T_\psi(t)=\frac{\psi'(t)}{\|\psi'(t)\|},\qquad
C_\psi(u,v)=\langle T_\psi(u),T_\psi(v)\rangle .
\]
On any branch where \(C_\psi(u_0,v_0)\ne0\), the principal-angle observable
\(|C_\psi|\) has the same local rank test as \(C_\psi\). Richer-than-overlap
holds locally at \((u_0,v_0)\) whenever
\[
\Delta_\psi(u_0,v_0):=
\det\frac{\partial(I_\psi,C_\psi)}{\partial(u,v)}(u_0,v_0)\ne0 .
\]

This is an open dense finite-jet condition. More precisely, on the admissible
endpoint \(2\)-jet space
\[
(x,a,b;y,c,d)
\]
with
\[
\|x\|=\|y\|=1,\quad a\perp x,\quad c\perp y,\quad a,c\ne0,\quad
\langle b,x\rangle=-\|a\|^2,\quad \langle d,y\rangle=-\|c\|^2,
\]
write
\[
T_x=\frac a{\|a\|},\quad T_y=\frac c{\|c\|},\quad
U_x=\frac{(I-T_xT_x^*)b}{\|a\|},\quad
U_y=\frac{(I-T_yT_y^*)d}{\|c\|}.
\]
Then
\[
\partial_u I=\langle a,y\rangle,\quad
\partial_v I=\langle x,c\rangle,\quad
\partial_u C=\langle U_x,T_y\rangle,\quad
\partial_v C=\langle T_x,U_y\rangle,
\]
so
\[
\Delta=
\langle a,y\rangle\langle T_x,U_y\rangle
-\langle x,c\rangle\langle U_x,T_y\rangle .
\]
After clearing the nonzero velocity denominators, \(\Delta\ne0\) is the
complement of a proper real-algebraic hypersurface in this endpoint \(2\)-jet
space. Hence every finite-dimensional curve family whose endpoint \(2\)-jet map
is submersive onto an open jet chart has an open dense set of parameters with
locally richer-than-overlap \(O_1\) line-angle data. The same open-dense
conclusion also holds for a connected real-analytic or algebraic family when
the pulled-back determinant is not identically zero. In particular, any
finite-jet family containing one nonzero-\(\Delta\) jet and allowing independent
small endpoint \(2\)-jet perturbations has structurally generic
richer-than-overlap behavior. The same statement applies to complex Hilbert
spaces on the underlying real jet space, using \(|\langle T_u,T_v\rangle|\) or
\(|\langle T_u,T_v\rangle|^2\) on a nonzero branch.

Thus UV-015 reduces to a theorem with exact hypotheses rather than another
example: first-order value-channel-free richer-than-overlap behavior is generic
in the finite-jet sense for normalized curves in dimension at least \(3\). The
current benchmark families supply seed jets and narrative evidence, but the
genericity mechanism is the nonvanishing of the endpoint \(2\)-jet Jacobian.

## Status

proved

## Evidence

Proved:

1. The displayed formulas for \(\partial_u I,\partial_v I,\partial_u C,\partial_v C\)
   follow by differentiating the endpoint overlap and the unit tangent
   \(T=\psi'/\|\psi'\|\). The second derivative only enters through the normal
   part \(U=(I-TT^*)\psi''/\|\psi'\|\).
2. The normalized-curve constraints on an endpoint \(2\)-jet are exactly
   \(\langle a,x\rangle=0\) and \(\langle b,x\rangle=-\|a\|^2\), with the same
   equations at \(y\).
3. The determinant is not identically zero. In \(\mathbb R^3\), take
   \[
   x=e_1,\quad y=e_2,\quad
   a=\frac{e_2+e_3}{\sqrt2},\quad
   c=\frac{e_1+e_3}{\sqrt2},
   \]
   \[
   b=-e_1+\frac{e_2-e_3}{\sqrt2},\quad d=-e_2 .
   \]
   These satisfy the admissible normalized \(2\)-jet constraints. Here
   \(C=\langle T_x,T_y\rangle=1/2\), so the principal-angle branch is smooth, and
   direct substitution gives
   \[
   \Delta=\frac{1}{2\sqrt2}\ne0 .
   \]
   The exact arithmetic check is
   `scripts/verify_o1_jet_determinant.py` with SHA256
   `9290A89C67780A4D35DC3B5E19892B1135E39B643170D2B55F55D2CA6680FD13`;
   its relevant output is `C = 1/2` and `Delta = 1/4*sqrt(2)`, the same value.
4. Since the cleared determinant is a nonzero polynomial on a finite-dimensional
   jet chart, its nonvanishing locus is real-Zariski open and Euclidean open
   dense. Hermite interpolation in local sphere charts, with disjoint supports
   near \(u_0\) and \(v_0\), realizes arbitrary nearby admissible endpoint
   \(2\)-jets by normalized \(C^2\) curves. Therefore the same open-dense result
   holds in the \(C^2\) curve space. It also holds after pullback to any
   finite-dimensional family whose endpoint jet map is submersive onto an open
   jet chart, and to any connected real-analytic/algebraic family where the
   pulled-back determinant is not identically zero.
5. The proof is independent of the Veronese and spherical-twist formulas. Those
   reports remain useful seed/provenance checks: the qutrit \(O_1\) report has
   an explicit nonzero Jacobian, and the spherical-twist report has a
   non-polynomial witness and local Jacobian evidence.

Conditional:

- For complex Hilbert spaces, the theorem is stated on the underlying real
  endpoint jet space and on a branch where the chosen scalar angle observable is
  smooth. A holomorphic-Zariski statement for complex jets is not claimed,
  because physical principal-angle observables use conjugation and absolute
  values.
- The theorem is first-order \(O_1\). The same finite-jet rank template should
  apply to \(A_1\) plane-angle branches and higher \(O_r/A_r\) simple-spectrum
  branches, but those require writing the corresponding determinant and showing
  a seed jet with nonzero determinant.

Missing:

- A promoted paper paragraph should decide how broad a statement it wants:
  either the first-order \(O_1\) theorem above, or a shorter "finite-jet rank
  criterion" proposition that explicitly leaves \(A_1\) and higher-order
  analogues as applications.
- An adversarial verifier should check the Hermite-realization step and the
  complex-scope wording before UV removal.

One script was run after being written under this agent directory:
`scripts/verify_o1_jet_determinant.py`. It checks the seed normalized-curve
constraints and returns `C = 1/2`, `Delta = 1/4*sqrt(2)`.

## Baseline / delta

Baseline: the note and findings already had benchmark families. The Veronese
reports prove all-\(n\) richer-than-overlap behavior inside a polynomial family,
and the spherical-twist reports prove non-polynomial benchmark behavior. The
live UV still asked whether this behavior is structurally generic outside those
families rather than another isolated or benchmark-family example.

Delta: this report replaces the example search with a finite-jet theorem. The
rank condition \(\Delta\ne0\) depends only on endpoint \(2\)-jets, is open, and
is dense away from the determinant-zero failure locus in any sufficiently rich
jet class. This proves structural genericity for first-order \(O_1\) line-angle
data in a precise Baire/open-dense sense, and in a real-Zariski sense for
algebraic jet families.

## Attempt status

keep

## Exact refs

- Target and frontier: `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md:7-9`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/dispatch.md:155-171`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/attempts.md:14,40-42`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/collation.md:186`.
- Current note package and open problem: `quantum/paper/jet_gram_quantum_note.md:35-49`; `quantum/paper/jet_gram_quantum_note.md:321-369`; `quantum/paper/jet_gram_quantum_note.md:798-852`.
- Current findings: `quantum/teams/20260423-043347-research-team-jet-gram-qm/findings.md:243-257`.
- Veronese benchmark theorem and richness: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-190226-attack-veronese/reports/gap-veronese-theorem.md:3-43`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-194242-attack-veronese-richness/reports/gap-veronese-richness.md:3-66`.
- Value-channel-free Veronese theorem and richness: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-192859-attack-Or-veronese/reports/gap-Or-veronese-theorem.md:3-58`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-194725-attack-Or-richness/reports/gap-Or-richness.md:3-27`.
- Qutrit/quartit \(O_r\) witnesses: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/gap-Or-vs-Ar.md:3-65`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-133641-attack-qutrit-omega/reports/gap-qutrit-omega.md:3-60`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-133641-attack-qutrit-omega/reports/gap-qutrit-witness.md:3-38`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-144313-attack-quartit-O2/reports/gap-quartit-O2.md:3-43`.
- Non-Veronese witnesses: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-204337-attack-nonveronese/reports/gap-spherical-twist.md:3-43`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-215017-attack-spherical-witness/reports/gap-spherical-witness.md:3-52`; `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-033611-attack-twist-family/reports/gap-twist-family.md:3-56`.
- Verification script: `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-193527-gap-nonbenchmark-genericity/scripts/verify_o1_jet_determinant.py`, SHA256 `9290A89C67780A4D35DC3B5E19892B1135E39B643170D2B55F55D2CA6680FD13`; run output `C = 1/2`, `Delta = 1/4*sqrt(2)`.

## Dependencies

- Elementary differential geometry of normalized curves on a finite-dimensional
  sphere.
- Endpoint \(2\)-jet realization by local Hermite interpolation in sphere
  charts.
- Principal-angle smoothness on a branch where the relevant singular value or
  line-angle scalar is simple/nonzero.
- The existing quantum-note decision that `O_r` is the value-channel-free
  object and that principal-angle data is the canonical subspace-level output.

## Strongest objection

This closes a precise first-order finite-jet genericity theorem, not every
possible reading of "generic" for every higher-order observable. A referee can
still ask for a separate \(A_1\) determinant, a higher \(O_r/A_r\) determinant,
or a source-specific finite-dimensional family whose endpoint jet map is proved
submersive. Those are extensions, not defects in the \(O_1\) theorem. The
complex statement is real-open-dense on the underlying real jet space, not a
holomorphic-Zariski theorem.

## Needed for promotion

Promote only a scoped proposition:

"For \(C^2\) normalized curves in a fixed finite-dimensional Hilbert space of
dimension at least \(3\), the local independence of endpoint overlap and the
first \(O_1\) principal-angle scalar is an open dense endpoint \(2\)-jet
condition. Equivalently, in any finite-dimensional curve class whose endpoint
\(2\)-jet map is submersive onto an open jet chart, or whose analytic/algebraic
determinant pullback is not identically zero, richer-than-overlap behavior is
generic on the corresponding open-dense locus."

The verifier should check the determinant formula, the explicit nonzero jet,
the interpolation-to-curves step, and the branch caveat for absolute
principal-angle observables. Do not promote a blanket theorem for all
higher-order \(O_r/A_r\) observables or a holomorphic complex-Zariski statement.

## Autoresearch next step

verify: send this report to an adversarial verifier focused on the endpoint
\(2\)-jet determinant, the density/interpolation argument, and the exact scope of
the complex and higher-order caveats.
