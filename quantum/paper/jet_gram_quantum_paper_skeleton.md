# Paper Skeleton: Jet-Gram Structures and Higher Quantum Geometry

Status: ambitious paper skeleton. This is not yet a polished draft. It records
the theorem spine, the paper message, and the explicit research gaps that should
drive the next attacks.

Primary source note: `quantum/paper/jet_gram_quantum_note.md`.

Primary team state:
`quantum/teams/20260423-043347-research-team-jet-gram-qm/`.

## One-Sentence Thesis

The quantum-side analogue of a whitened jet cross-Gram construction is
matrix-valued only at first order and under extra transport/frame choices; at
higher order the canonical object is the osculating subspace filtration, whose
endpoint comparison is the principal-angle/operator package.

## Draft Abstract

The quantum geometric tensor is the first-order Gram matrix of horizontal
derivatives of a pure-state family. Motivated by the local jet cross-Gram
construction in `paper/proof_of_rh.tex`, we ask whether this first-order
geometry has a higher-order, two-point matrix analogue for quantum state
families. The answer is sharply mixed. The same-point first-horizontal block is
exactly the usual quantum geometric tensor, and a first-order transported
two-point block has a precise reparameterization law. From second order onward,
however, ordered jet matrices transform by non-unitary triangular laws under
phase gauge and coordinate change, so their entries are not canonical. The
surviving object is the osculating subspace filtration \(O_r\), together with
the ambient extension \(A_r=\operatorname{span}\{\psi\}\oplus O_r\). Endpoint
comparison is therefore governed by cross-contractions, projector compressions,
polar partial isometries, and principal angles. We prove that all
orthonormal-frame comparison matrices for a fixed endpoint subspace pair form a
single biunitary orbit, classified by the same principal-angle singular values;
thus a canonical entrywise matrix requires extra frame-selecting structure. We
give benchmark families where this higher-order subspace data is richer than
ordinary overlap, and we record a coherent reflection protocol that reads the
principal angles under explicit access assumptions.

## What This Paper Is Not

- It is not a claim about new fundamental particles.
- It is not a claim that the source paper's zeta-side matrix is literally a
  standard quantum geometric tensor.
- It is not a claim that arbitrary higher quantum jets define canonical
  matrices.
- It is not a new physical Hamiltonian model for every jet-derived subspace
  family.

## The Paper Message

The useful physics-facing message is:

> Higher-order quantum geometry should be compared through canonical endpoint
> subspaces and their principal-angle/operator package, not through raw
> derivative matrices.

This is useful because it gives a higher-order geometric fingerprint of a
quantum state family. It can detect endpoint structure not visible to ordinary
overlap/fidelity in explicit benchmarks, while also explaining why many tempting
matrix constructions are gauge or frame artifacts.

## Proved Spine

### Theorem A: First-Order QGT Bridge

For a smooth normalized pure-state family \(\psi(\lambda)\), with
\[
P=I-|\psi\rangle\langle\psi|,\qquad D_a\psi=P\partial_a\psi,
\]
the same-point horizontal Gram matrix
\[
Q_{ab}=\langle D_a\psi,D_b\psi\rangle
\]
is exactly the pure-state quantum geometric tensor. Its real part is the
quantum metric and its imaginary part is Berry curvature.

Role in paper: this anchors the construction to established quantum geometry.

### Theorem B: First-Order Two-Point Law

For a one-parameter pure-state curve and a chosen gauge-covariant transport
rule, the bilaterally whitened first-horizontal-jet two-point block is invariant
under orientation-preserving reparameterization. Under orientation reversal it
transforms by
\[
\Omega\mapsto E\Omega E,\qquad E=\operatorname{diag}(1,-1).
\]

Role in paper: first order is the only place where the transported matrix story
works cleanly.

### Theorem C: Higher-Jet Matrix No-Go

For raw projected higher jets
\[
j_k=P\partial_t^k\psi,
\]
the ordered list \((j_1,\ldots,j_r)\) transforms by invertible
upper-triangular laws under phase gauge and reparameterization. Therefore raw
higher-jet Gram matrices and whitened matrices are not canonical.

Role in paper: this is the main negative theorem. It explains why the paper
pivots away from matrices.

### Theorem D: Osculating Subspace Survival

The subspace
\[
O_r=\operatorname{span}\{j_1,\ldots,j_r\}
\]
is invariant under the same gauge and coordinate changes that destroy the
ordered matrix. In a fixed ambient Hilbert space,
\[
A_r=\operatorname{span}\{\psi,\partial\psi,\ldots,\partial^r\psi\}
    =\operatorname{span}\{\psi\}\oplus O_r
\]
gives the ambient version.

Role in paper: this is the central positive theorem.

### Theorem E: Covariant And Multiparameter Jet Filtrations

Berry-covariant iterated derivatives generate the same \(O_r\) filtration as
raw projected jets. In several parameters, ordered and symmetrized covariant
jets generate the same canonical subspace filtration. These constructions
repair the generators, not the ordered matrix.

Role in paper: this makes the subspace theorem robust rather than merely a
one-parameter accident.

### Theorem F: Endpoint Operator Package

For endpoint subspaces \(S_-\) and \(S_+\), with projectors \(\Pi_\pm\), the
canonical endpoint data is
\[
C=\Pi_-|_{S_+},\qquad K_+=C^*C,\qquad K_-=CC^*,\qquad C=V|C|.
\]
The spectra of \(K_\pm\) are the squared principal-angle cosines, and the polar
partial isometry \(V\) gives the canonical basis-free transport on the
nonzero-overlap sector.

Role in paper: this is the replacement for the failed matrix object.

### Theorem G: Matrix Finality

If \(U_-:\mathbb C^p\to S_-\) and \(U_+:\mathbb C^q\to S_+\) are orthonormal
frames, the comparison matrix \(A=U_-^*U_+\) changes under frame replacement by
\[
A\mapsto L^*AR,\qquad L\in U(p),\quad R\in U(q).
\]
Every orthonormal-frame comparison matrix for the same subspace pair is in this
biunitary orbit. The rectangular SVD classifies the orbit by singular values,
which are exactly the principal-angle cosines.

Role in paper: no entrywise matrix is canonical without extra frame-selecting
structure.

### Theorem H: Frame Boundary

On the nonzero-overlap sector, canonical principal frames exist from the
subspace pair alone exactly when the nonzero principal spectrum is simple.
Repeated nonzero principal values carry an unavoidable internal unitary freedom.

Role in paper: this gives a sharp positive/negative boundary.

### Theorem I: Dynamics And Operational Readout

Exact unitary orbits identify \(A_r\) and \(O_r\) with transported Krylov and
compressed-Krylov spaces. Kato transport realizes arbitrary smooth projector
paths but is path-dependent; in several parameters its curvature is the
endpoint-independence obstruction.

Under coherent reflection access to endpoint projectors, the product
\[
W=(2\Pi_- - I)(2\Pi_+ - I)
\]
has eigenphases \(\pm 2\theta_i\) on the principal two-planes. Phase estimation
on \(W\) therefore reads the principal angles under reflection-access and
state-preparation hypotheses.

Role in paper: this connects the invariant to dynamics and measurement without
overclaiming new invariant content.

## Benchmark Spine

### Oscillator Benchmark

Use: sanity check for first-order reparameterization and whitening.

Result: the raw first-jet matrices depend on parameterization, but the whitened
first-order block is stable in the tested reparameterization. Its singular
values collapse to endpoint overlap, so this is not a richer-than-overlap
example.

### Qutrit Polynomial Benchmark

Use: first finite-dimensional richer-than-overlap example.

Family:
\[
\psi(t)=\frac{(1,t,t^2)^T}{\sqrt{1+t^2+t^4}}.
\]

Result: both \(A_1\) and \(O_1\) have endpoint principal-angle data not
determined by ordinary overlap.

### Quartit Cubic Benchmark

Use: second-order example where matrices fail but subspaces survive.

Family:
\[
\psi(t)=\frac{(1,t,t^2,t^3)^T}{\sqrt{1+t^2+t^4+t^6}}.
\]

Result: \(A_2\) has exact singular values \((1,1,\sigma_3)\), while \(O_2\)
has an explicit \(2\times2\) complement matrix and is strictly finer than
\(A_2\) on this benchmark.

### Veronese Family

Use: systematic polynomial benchmark theorem.

Family:
\[
v_n(t)=(1,t,\ldots,t^n).
\]

Result: at top order \(r=n-1\), the ambient osculating subspace is a
codimension-one hyperplane with normal from \((x-t)^n\). The corresponding
principal-angle cosine is generically not determined by overlap. The
value-channel-free \(O_{n-1}\) side has a parallel codimension-two complement
description.

### Spherical Twist Family

Use: non-polynomial richer-than-overlap witness.

Family:
\[
\psi_k(t)=(\cos t\cos kt,\cos t\sin kt,\sin t),\qquad k\ge2.
\]

Result: exact equal-overlap pairs have different \(A_1\) and \(O_1\)
principal-angle data.

## Proposed Paper Outline

### 1. Introduction

Tasks:
- Explain the local jet cross-Gram motivation.
- State the problem: can one build a higher-order quantum-geometric matrix?
- State the answer: first order gives QGT; higher order gives subspaces and
  operators, not canonical matrices.
- Give the physics-facing value: higher-order fingerprints of quantum state
  families, with no-go clarity for frame-dependent matrices.

### 2. Background And Notation

Tasks:
- Pure-state families, rays, gauges, projectors.
- QGT and Fubini-Study geometry.
- Principal angles, cross-contractions, and projector compressions.
- The source-side jet cross-Gram pattern, stated only as motivation.

### 3. First-Order Quantum Jet-Gram Geometry

Main content:
- Prove Theorem A.
- Define the first-order two-point transported block.
- Prove Theorem B.
- Explain transport dependence and scalar-phase transport as a restricted
  invariant class.

GAP-3A: decide whether this section should include a complete classification of
all first-order transport choices, or keep only the current gauge-covariant and
scalar-phase statements.

Minimum closure: a short remark saying no transport-independent endpoint matrix
is claimed.

### 4. Higher Jets: Matrix Failure And Subspace Survival

Main content:
- Prove triangular transformation laws.
- Prove Theorem C.
- Prove Theorem D.
- Prove the one-parameter covariant jet hierarchy.
- Prove multiparameter covariant and symmetrized filtration results.

GAP-4A: write the associated-graded/tensor-symbol option cleanly, or explicitly
defer it.

Why it matters: the multiparameter no-go leaves room for basis-free tensor data
that is not an ordered matrix. The paper should either include that object or
say why it is outside scope.

### 5. The Endpoint Operator Package

Main content:
- Define endpoint pairs \(S_-,S_+\).
- Prove the canonical cross-contraction and compression package.
- Prove polar partial isometry.
- Prove simple-spectrum frame corollary.
- Prove repeated-spectrum no-go.
- Prove finite-dimensional completeness by CS normal form.
- Prove biunitary matrix finality.

GAP-5A: compress the operator package into one clean theorem with corollaries.

Why it matters: this is the heart of the paper. It needs to read as one
coherent result, not as a list of deposits.

### 6. \(A_r\) Versus \(O_r\)

Main content:
- State \(A_r=\operatorname{span}\{\psi\}\oplus O_r\).
- Prove the quotient relation \(O_r\simeq A_r/\operatorname{span}\{\psi\}\).
- State the role split: \(O_r\) is value-channel-free; \(A_r\) is the ambient
  endpoint package.
- Explain why no global winner is forced.

GAP-6A: decide whether any physical selection principle chooses \(A_r\) or
\(O_r\) in specific applications.

Minimum closure: keep both and make the role split explicit.

### 7. Dynamics And Readout

Main content:
- Exact unitary/Krylov specialization.
- Propagator compression.
- Finite-cyclic saturation and Jacobi/Lanczos normal form.
- Projector leakage and short-time expansion.
- Kato pathwise transport and curvature obstruction.
- Conditional reflection/phase-estimation readout.

GAP-7A: find a natural physical model beyond reflection access.

Target theorem: for a physically motivated class of Hamiltonians or
measurements, the endpoint \(A_r/O_r\) principal angles appear directly in an
observable response, transition spectrum, or controlled protocol without
assuming arbitrary projector reflections.

Minimum closure: state the reflection protocol as conditional and leave the
stronger physical model open.

### 8. Benchmarks

Main content:
- Oscillator as a warning and sanity check.
- Qutrit and quartit explicit richer-than-overlap witnesses.
- Veronese top-order family theorem.
- Spherical twist non-polynomial family.

GAP-8A: nonbenchmark genericity.

Target theorem: prove that richer-than-overlap endpoint principal-angle data is
generic in an open class of smooth pure-state curves, not only in the Veronese
and spherical twist families.

Minimum closure: keep the benchmark theorem honest and state genericity as an
open problem.

GAP-8B: lower-order Veronese spectra.

Target theorem: for \(v_n(t)=(1,t,\ldots,t^n)\) and \(r<n-1\), derive closed or
structural formulas for the principal-angle spectra of \(A_r\) and \(O_r\).

Minimum closure: present only the complement-basis theorem and avoid claiming a
full spectral formula.

### 9. Limits Of The Theory

Main content:
- No canonical full matrix from higher jets.
- No endpoint-independent Kato transport in nonzero curvature.
- No canonical repeated-spectrum principal frame.
- No genericity theorem yet.
- No claim of fundamental new physics.

This section should be direct. It is part of the paper's credibility.

### 10. Research Program

Convert the following gaps into future UV entries or targeted attacks:

| Gap | Target | Current status | Promotion condition |
|---|---|---|---|
| GAP-4A | Associated-graded/tensor-symbol formulation | open | Basis-free definition plus transformation law, or explicit deferral |
| GAP-5A | Unified operator-package theorem | editorial/proof packaging | Single theorem with proof and named corollaries |
| GAP-6A | Physical criterion for \(A_r\) versus \(O_r\) | open | Application-specific selection principle or scoped no-go |
| GAP-7A | Natural physical protocol beyond reflection access | open | Observable model not equivalent to arbitrary projector reflection access |
| GAP-8A | Nonbenchmark genericity | open | Clean generic theorem for richer-than-overlap behavior |
| GAP-8B | Lower-order Veronese spectra | open | Formula or structural spectral theorem for \(r<n-1\) |
| GAP-10A | Experimental/numerical case study | open | Concrete system where these invariants reveal information QGT/fidelity misses |

### 11. Conclusion

The conclusion should say that the attempted matrix-valued higher quantum
geometry fails for principled reasons, and that this failure identifies the
correct invariant object: endpoint osculating subspaces and their
principal-angle/operator package.

## Ambitious Extensions

These are not needed for a first paper, but could make a stronger second paper
or a more physics-facing version.

### Mixed States And Degenerate Bands

Question: can the osculating-subspace package be extended from pure-state rays
to density matrices, purification bundles, or degenerate Bloch bands?

Risk: this may collide with existing non-Abelian QGT/Wilczek-Zee geometry. It
needs a careful literature pass.

### Quantum Materials Case Study

Question: can higher osculating-subspace angles detect band-geometry structure
that ordinary QGT or fidelity susceptibility misses?

Candidate setting: Bloch-state families, flat bands, topological phase
boundaries, or variational ground-state manifolds.

### Quantum Algorithms Case Study

Question: can \(O_r/A_r\) principal angles diagnose ansatz expressivity or
Krylov-subspace saturation in variational algorithms?

Candidate setting: compare ansatz tangent/second-order subspaces along
training, or compare Krylov subspaces under different Hamiltonian parameters.

## Current Honest Verdict

We have enough for a real mathematical note now. The clean version is:

- first-order bridge to QGT;
- higher-order matrix no-go;
- canonical osculating-subspace survival;
- endpoint operator/principal-angle package;
- biunitary matrix finality;
- benchmark families richer than overlap;
- conditional reflection protocol.

The main missing item for a more ambitious physics paper is not another isolated
example. It is either a genericity theorem or a compelling physical case study.
