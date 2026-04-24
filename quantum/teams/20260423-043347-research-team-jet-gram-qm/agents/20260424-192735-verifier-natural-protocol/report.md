# UV-014 verifier: reflection and phase-estimation protocol

## Claim

The `20260424-192133-gap-natural-protocol` report is acceptable for promotion
after wording fixes. The algebraic two-reflection claim is correct: for
finite-rank endpoint subspaces \(S_\pm\) with projectors \(\Pi_\pm\), the
product
\[
W=(2\Pi_- - I)(2\Pi_+ - I)
\]
has eigenphases \(\pm 2\theta_i\) on each nontrivial principal two-plane, with
the expected \(+1\) sectors for \(\theta=0\) and common orthogonal complement
and \(-1\) sectors for \(\theta=\pi/2\) one-sided residuals. Thus controlled
phase estimation or coherent alternating-reflection dynamics gives a concrete
protocol for estimating the principal-angle spectrum already present in the
operator package.

The closure is conditional on coherent reflection access to the endpoint
projectors and adequate state preparation/sampling. It is not a new invariant,
not a new physical Hamiltonian for arbitrary jet families, and not a canonical
matrix representative.

## Status

proved

## Evidence

Proved. In a principal two-plane with \(e\in S_-\) and
\(g=\cos\theta\,e+\sin\theta\,f\in S_+\), where \(e,f\) are orthonormal,
\[
R_-=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
R_+=\begin{pmatrix}\cos 2\theta&\sin 2\theta\\
\sin 2\theta&-\cos 2\theta\end{pmatrix}.
\]
Therefore
\[
R_-R_+=\begin{pmatrix}\cos 2\theta&\sin 2\theta\\
-\sin 2\theta&\cos 2\theta\end{pmatrix},
\]
whose eigenvalues are \(e^{\pm 2i\theta}\), up to the convention for orientation
of the real rotation. The sign convention does not affect the recovered
principal angle because phase estimation sees the pair \(\pm 2\theta\).

Exceptional sectors check out. On \(S_-\cap S_+\), both reflections are \(+1\),
so \(W=+1\), representing \(\theta=0\). On one-sided orthogonal sectors such as
\(S_-\cap S_+^\perp\) or \(S_-^\perp\cap S_+\), exactly one reflection is
negative, so \(W=-1\), representing \(\theta=\pi/2\). On
\((S_-+S_+)^\perp\), \(W=+1\), but this sector is not principal-angle data for
the endpoint pair and should be excluded or treated as ambient padding. In
unequal dimensions, phase estimation on \(W\) alone does not identify which
extra \(-1\) eigenspaces belong to which endpoint side; the endpoint dimensions
and the preparation support must remain part of the protocol statement.

Conditional. Coherent reflection access is a strong but standard quantum
algorithmic hypothesis. It is stronger than the old destructive yes/yes
projector test, but not merely the same measurement written twice: it gives a
reversible alternating-reflection unitary whose phases are the principal angles
themselves, while the old effect operator gives only \(\cos^2\theta_i\)
probabilities. The hypothesis is natural for code spaces, symmetry sectors,
eigenspaces with phase-kickback access, or any implemented coherent membership
test; it is not automatic for arbitrary jet subspaces.

Missing. The report does not produce a universal physical Hamiltonian, does not
remove Kato path dependence, does not improve the exact unitary/Krylov or
compressed-propagator specializations, and does not create endpoint matrix
canonicity. No scripts were needed; this verification is algebraic.

## Baseline / delta

Baseline: the current note already has the endpoint operator package, including
\(\Pi_-\Pi_+\Pi_-\), cross-contraction, polar partial isometry, principal-angle
spectrum, finite-dimensional completeness, and the yes/yes effect-operator
interpretation. The prior dynamical reports cover exact unitary/Krylov
subspace orbits, compressed propagators, leakage/short-time formulas, and
pathwise Kato transport with curvature obstruction.

Delta: the reflection protocol gives a coherent endpoint experiment under an
explicit access model. It goes beyond the old yes/yes effect operationally
because repeated coherent reflections and phase estimation estimate
\(\theta_i\) as phases, not just \(\cos^2\theta_i\) as one-shot probabilities.
It does not go beyond the operator package invariantly.

## Attempt status

keep

## Exact refs

- Target UV: `quantum/teams/20260423-043347-research-team-jet-gram-qm/uv.md:7`
  to `uv.md:10`.
- Primary report:
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-192133-gap-natural-protocol/report.md:5`
  to `report.md:22`, `report.md:30` to `report.md:82`, and `report.md:160`
  to `report.md:168`.
- Current operator package and yes/yes baseline:
  `quantum/paper/jet_gram_quantum_note.md:422` to
  `quantum/paper/jet_gram_quantum_note.md:510`.
- Exact unitary/Krylov, compressed-propagator, leakage, Kato, and curvature
  boundaries: `quantum/paper/jet_gram_quantum_note.md:372` to
  `quantum/paper/jet_gram_quantum_note.md:411` and
  `quantum/paper/jet_gram_quantum_note.md:512` to
  `quantum/paper/jet_gram_quantum_note.md:551`.
- Open problem wording:
  `quantum/paper/jet_gram_quantum_note.md:830` to
  `quantum/paper/jet_gram_quantum_note.md:833`.
- Prior operational baseline:
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-191742-attack-operational-meaning/reports/gap-operational-meaning.md`.
- Prior exact unitary/Krylov report:
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260423-201939-attack-krylov/reports/gap-krylov-theorem.md`.
- Prior compressed-propagator report:
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-002612-attack-propagator-subspaces/reports/gap-propagator-subspaces.md`.
- Prior leakage and short-time reports:
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-001425-attack-commutator-metric/reports/gap-commutator-metric.md`;
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-024026-attack-short-time-expansion/reports/gap-short-time-expansion.md`.
- Prior Kato reports:
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-055506-attack-kato-transport/reports/gap-kato-transport.md`;
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-060404-attack-kato-curvature/reports/gap-kato-curvature.md`.
- Current collation:
  `quantum/teams/20260423-043347-research-team-jet-gram-qm/collation.md`
  section `Gap return - UV-014`.

## Dependencies

Finite-rank endpoint subspaces in a fixed Hilbert space, orthogonal projectors
\(\Pi_\pm\), coherent implementation of \(R_\pm=2\Pi_\pm-I\), controlled
application of \(W=R_-R_+\) for phase estimation, and state preparation or
sampling that has support in the principal sectors one wants to observe. To
recover rectangular/unequal-dimension bookkeeping, the endpoint dimensions and
preparation support must be stated separately from the raw spectrum of \(W\).

## Strongest objection

The access model is doing the work. For arbitrary jet-derived endpoint
subspaces, coherent reflection access may be as hard as constructing the
projectors themselves, so the result should not be sold as a natural Hamiltonian
or laboratory model without naming an implementation class. The honest closure
is: if endpoint-subspace reflections are available, the package has a standard
phase-estimation/amplitude-amplification protocol. Without that access, UV-014
falls back to the old yes/yes test and remains open for a more physical model.

## Needed for promotion

Promote a short paragraph after the yes/yes operational paragraph. Safe wording:

"If the endpoint projectors can be implemented coherently as reflections
\(R_\pm=2\Pi_\pm-I\), then the product \(R_-R_+\) gives a reversible
alternating-reflection protocol for the same endpoint data. On each nontrivial
principal two-plane its eigenphases are \(\pm2\theta_i\), while the intersection
and orthogonal residual sectors give the expected \(+1\) and \(-1\) exceptional
phases. Controlled phase estimation therefore estimates the principal angles
under the reflection-access and state-preparation hypotheses."

Also state:

"This is a protocol for reading the existing principal-angle/operator package,
not a new invariant, not a canonical matrix representative, and not a substitute
for the exact unitary/Krylov or pathwise Kato transport specializations."

Avoid wording that says the protocol is available for arbitrary jet families,
that the phase spectrum alone classifies unequal-dimensional endpoint data
without dimension/preparation bookkeeping, that coherent reflections are the
same resource as destructive projective measurements, or that this supplies a
new Hamiltonian dynamics.

## Autoresearch next step

terminal: after the wording fixes above, UV-014 can be promoted as a conditional
positive protocol under coherent reflection access. No residual substatement is
needed unless the coordinator wants a stronger model without reflection oracles.
