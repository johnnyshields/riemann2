# Working Note: Jet-Gram Structures and Quantum Geometry

Status: working draft in `quantum/`.

This note does not modify the RH draft. It asks a separate question: whether
the local jet-Gramian pattern from `paper/proof_of_rh.tex` has a meaningful
quantum-side reformulation.

## Source Object

The source paper defines a local kernel-based construction with:

- same-point jet Gram blocks,
- a mixed cross block,
- bilateral whitening.

In the jet-limit notation this is

\[
\Omega_\infty(T_1,T_2)=M_1^{-1/2}N_{12}M_2^{-1/2},
\]

and at finite separation it is

\[
\widehat\Omega_\zeta(s;m)=G_{m,-}(s)^{-1/2}N_m(s)G_{m,+}(s)^{-1/2}.
\]

Source anchors: `paper/proof_of_rh.tex:114,171-259`.

The safest current name for this pattern is:

**whitened local jet cross-Gram block**.

## Established First-Order Bridge

Let \(\lambda=(\lambda^a)\mapsto |\psi(\lambda)\rangle\) be a smooth
normalized pure-state family. Define

\[
P(\lambda):=I-|\psi(\lambda)\rangle\langle\psi(\lambda)|,
\qquad
|D_a\psi\rangle:=P(\lambda)\,\partial_a|\psi(\lambda)\rangle.
\]

Then the same-point horizontal-derivative Gram matrix is

\[
Q_{ab}(\lambda):=\langle D_a\psi\mid D_b\psi\rangle
=\langle \partial_a\psi\mid (I-|\psi\rangle\langle\psi|)\mid\partial_b\psi\rangle.
\]

This is exactly the pure-state quantum geometric tensor. Therefore:

\[
g_{ab}=\Re Q_{ab},
\qquad
F_{ab}=2\,\Im Q_{ab},
\qquad
I_{ab}=4\,\Re Q_{ab}.
\]

Interpretation:

- The source paper's "remove the value channel, then form a same-point jet Gram
  block" pattern has a clean first-order quantum counterpart.
- What is identified exactly is the same-point horizontal block.
- This does not identify the source paper's full two-point whitened matrix with
  standard quantum geometry.

## Conditional Two-Point Construction

If one wants a quantum-side analogue of the source paper's two-point mixed and
whitened block, one must insert extra structure.

For two nearby parameters \(\lambda_1,\lambda_2\), choose a transport rule
between rays, for example Berry parallel transport \(U_{1\leftarrow 2}\).
Then define a first-order transported mixed block

\[
C_{ab}(\lambda_1,\lambda_2):=
\langle D_a\psi(\lambda_1)\mid U_{1\leftarrow 2}D_b\psi(\lambda_2)\rangle.
\]

When the retained same-point horizontal Gram blocks are positive definite, one
may whiten:

\[
\Omega^{(1)}(\lambda_1,\lambda_2)
:=
Q(\lambda_1)^{-1/2}
C(\lambda_1,\lambda_2)
Q(\lambda_2)^{-1/2}.
\]

Current status:

- This is a legitimate transported-frame construction.
- It is not yet a canonical quantum-geometric matrix invariant.
- Without extra structure, the honest invariant content may be only the
  singular values or principal angles of transported horizontal-jet subspaces.

## Proved One-Parameter Theorem

There is one exact two-point theorem in the current draft scope.

Let \(\lambda \mapsto |\psi(\lambda)\rangle\) be a \(C^1\) normalized local
lift of a one-parameter pure-state family, and define the first horizontal jet

\[
|h_\lambda\rangle:=(I-|\psi(\lambda)\rangle\langle\psi(\lambda)|)
\partial_\lambda|\psi(\lambda)\rangle.
\]

Choose a fixed two-point transport rule \(U_{1\leftarrow 2}\). In the frame
\((|\psi\rangle,|h_\lambda\rangle)\), define

\[
M_\lambda(\lambda_i)=
\begin{pmatrix}
1 & 0 \\
0 & \langle h_{\lambda_i}\mid h_{\lambda_i}\rangle
\end{pmatrix},
\]

\[
N_\lambda(\lambda_-,\lambda_+)=
\begin{pmatrix}
\langle\psi_-\mid U_{-\leftarrow +}\psi_+\rangle &
\langle\psi_-\mid U_{-\leftarrow +}h_+\rangle \\
\langle h_-\mid U_{-\leftarrow +}\psi_+\rangle &
\langle h_-\mid U_{-\leftarrow +}h_+\rangle
\end{pmatrix},
\]

and

\[
\Omega_\lambda:=M_\lambda(\lambda_-)^{-1/2}
N_\lambda
M_\lambda(\lambda_+)^{-1/2}.
\]

If \(\mu=\phi(\lambda)\) is orientation-preserving, then

\[
\Omega_\mu=\Omega_\lambda.
\]

Reason: \(h_\mu=(d\lambda/d\mu)h_\lambda\), so the derivative channel rescales
by positive endpoint factors, and those factors cancel exactly under bilateral
whitening because the same-point first-horizontal-jet block is diagonal.

This theorem is exact but narrow.

- It is first-order only.
- It is one-parameter only.
- It becomes independent of the choice of local lift once the transport rule is
  itself chosen gauge-covariantly on the ray curve.
- It still does not produce a transport-independent endpoint invariant.

If the reparameterization reverses orientation, the exact replacement for
equality is

\[
\Omega_\mu = E\,\Omega_\lambda\,E,
\qquad
E=\operatorname{diag}(1,-1),
\]

provided one keeps the original ordered pair of endpoints fixed. So reversal
changes only the derivative channel sign.

## Gauge Upgrade

The first-horizontal-jet theorem can be upgraded one step further.

Under a local phase change \(|\psi(\lambda)\rangle \mapsto e^{i\chi(\lambda)}
|\psi(\lambda)\rangle\), the projector \(P=I-|\psi\rangle\langle\psi|\) is
unchanged and the first horizontal jet transforms covariantly:

\[
h_\lambda \mapsto e^{i\chi(\lambda)} h_\lambda.
\]

So the same-point block is unchanged by phase gauge. If the two-point transport
rule is itself gauge-covariant on the ray curve, then the transported mixed
block is also unchanged by change of local lift. Therefore the bilaterally
whitened first-horizontal-jet block is well defined on:

- a one-parameter ray curve,
- together with a chosen gauge-covariant transport rule,
- up to orientation-preserving reparameterization.

This is stronger than a fixed-lift statement, but weaker than a canonical
endpoint invariant. The remaining unresolved issue is transport dependence.

At the current level of generality, that dependence can be larger than a single
global phase on the whole matrix. With only a bare gauge-covariant transport
rule, different admissible transports can change derivative-channel entries
entrywise. So the present theorem should still be read as:

- a ray-curve-with-chosen-transport invariant,
- not a transport-independent endpoint invariant,
- and not yet a canonical matrix on ray space.

There is, however, a useful reduced class. If one explicitly restricts to
**scalar-phase transports** on the endpoint first-jet pair,

\[
U_{-\leftarrow +}=e^{i\alpha(\gamma)}I,
\]

then the whole whitened first-horizontal-jet block changes only by one global
phase. In that restricted class, Berry transport and Pancharatnam transport
(when \(\langle\psi_-\mid\psi_+\rangle\neq 0\)) lie in the same phase class, so
they produce blocks differing only by a unit scalar factor.

This is useful, but still conditional:

- it depends on restricting the admissible transport class;
- it does not show that the scalar-phase class is canonical;
- it does not remove the zero-overlap issue for Pancharatnam transport.

## Singular-Value Output

The first-order block also has a more stable derived quantity than the raw
matrix itself.

For a fixed gauge-covariant transport rule, the singular values of the
bilaterally whitened first-horizontal-jet block are:

- independent of local lift,
- invariant under orientation-preserving reparameterization,
- invariant under orientation reversal, because
  \(\Omega \mapsto E\Omega E\) with unitary \(E=\operatorname{diag}(1,-1)\).

If one further restricts to the reduced scalar-phase transport class, then the
singular values are also independent of the chosen transport inside that class,
because \(\Omega\mapsto e^{i\theta}\Omega\) does not change singular values.

So the singular values are a stronger candidate for a first-order canonical
quantity than the full matrix. But this is still only a partial resolution:

- for fixed transport, they are reparameterization- and lift-invariant;
- in the scalar-phase transport class, they are transport-class invariant;
- outside that reduced class, transport-independence is still open.

At first order there is also a useful split interpretation. Define the ambient
plane

\[
\mathcal A_1(\lambda)=\mathrm{span}\{\psi(\lambda),h_\lambda\}.
\]

Its principal angles with \(\mathcal A_1(\lambda_+)\) are canonical ambient
invariants. The singular values of the whitened first-horizontal-jet block
coincide with those principal-angle cosines exactly when the block is realized
in the common ambient space, for example in the identity/scalar-phase transport
setting. For a general transport convention, the same singular values instead
describe the principal angles between \(\mathcal A_1(\lambda_-)\) and the
transported plane \(U\mathcal A_1(\lambda_+)\).

## Higher-Jet Delimitation

The first-horizontal-jet matrix theorem is exceptional.

For higher raw projected coordinate jets

\[
j_k(\lambda):=(I-|\psi(\lambda)\rangle\langle\psi(\lambda)|)
\partial_\lambda^k|\psi(\lambda)\rangle,
\qquad 1\le k\le r,
\]

the ordered jet list no longer transforms by a scalar under gauge change or
reparameterization. Instead it transforms by an invertible upper-triangular law.

At second order the first nontrivial formulas already appear:

\[
j_2 \mapsto e^{i\chi}(j_2+2i\chi'j_1)
\]

under phase gauge, and

\[
j_2^{(\mu)}=\left(\frac{d\lambda}{d\mu}\right)^2 j_2^{(\lambda)}
+\frac{d^2\lambda}{d\mu^2}j_1^{(\lambda)}
\]

under one-parameter reparameterization.

So from second order onward, the raw higher-jet Gram and whitened matrices are
not canonical under the same exact mechanism that made the first-order theorem
work.

What does survive exactly is the osculating subspace

\[
O_r(\lambda)=\mathrm{span}\{j_1(\lambda),\dots,j_r(\lambda)\}.
\]

Because the higher-jet coordinate change is invertible and upper-triangular,
this subspace is unchanged by local phase gauge and by any one-parameter
reparameterization with nonzero derivative.

So the currently safe higher-order statement is:

- raw higher-jet matrices fail,
- the raw higher-jet osculating subspace survives,
- two-point higher-order data should therefore be sought at the subspace level,
  via transported principal angles or singular values, not via raw matrix
  entries.

There is also a transport-free ambient-subspace theorem.

For a one-parameter ray curve in a fixed ambient Hilbert space, define

\[
\mathcal A_r(\lambda)=\mathrm{span}\{\psi(\lambda),j_1(\lambda),\dots,j_r(\lambda)\},
\qquad
j_k=(I-|\psi\rangle\langle\psi|)\partial_\lambda^k\psi.
\]

Equivalently,

\[
\mathcal A_r(\lambda)=\mathrm{span}\{\psi,\partial_\lambda\psi,
\dots,\partial_\lambda^r\psi\}.
\]

This ambient osculating subspace is invariant under local phase gauge and under
one-parameter reparameterization with nonzero derivative. Therefore the
principal angles between \(\mathcal A_r(\lambda_-)\) and
\(\mathcal A_r(\lambda_+)\) are canonical transport-free two-point invariants.

This is a distinct statement from the earlier transport-based matrix language.
It wins by changing the object from a bilaterally whitened matrix to an ambient
subspace pair. It should be read as a new invariant, not as a proof that the
matrix story was transport-free all along.

There are therefore two related but distinct canonical subspace objects in the
current note:

\[
O_r(\lambda)=\mathrm{span}\{j_1(\lambda),\dots,j_r(\lambda)\},
\qquad
A_r(\lambda)=\mathrm{span}\{\psi(\lambda)\}\oplus O_r(\lambda).
\]

`O_r` is the value-channel-removed object and stays closest to the original
horizontal/jet-normalized motivation. `A_r` is the ambient object on which the
strongest transport-free two-point principal-angle theorem is currently stated.
The present record does not justify declaring one of them uniquely canonical in
all roles.

Current benchmarks sharpen this split. On the qutrit first-order and quartit
second-order families, `O_r` already carries richer two-point geometry than
overlap alone. On the quartit benchmark, `O_2` is actually finer than `A_2` at
the level of principal-angle data. So the present note keeps both objects on
purpose: `O_r` for the value-channel-free geometry, `A_r` for the cleanest
transport-free ambient theorem.

This ambient-subspace theorem also extends cleanly to several parameters. If the
parameter space is a manifold and one includes **all mixed partials of total
order at most \(r\)**, then the resulting ambient osculating subspace is still
independent of local phase gauge and of chart choice. So the multiparameter
extension survives exactly at the subspace/principal-angle level, while the
matrix story remains unresolved.

As a basis-free corollary, if \(\Pi_\pm\) are the orthogonal projectors onto the
canonical endpoint subspaces, then the compression

\[
K_-:=\Pi_-\Pi_+\Pi_-\big|_{\mathcal A_r(x_-)}
\]

has spectrum equal to the squared principal-angle cosines. This is a clean
operator reformulation of the same subspace data, not a stronger invariant.

The cleanest current second-order benchmark is the real quartit cubic curve

\[
|\psi(t)\rangle=\frac{(1,t,t^2,t^3)^T}{\sqrt{1+t^2+t^4+t^6}}.
\]

Its second osculating space is a genuine varying \(3\)-plane in \(\mathbb R^4\),
with normal

\[
n(t)=(-t^3,3t^2,-3t,1)^T.
\]

So in the identity/scalar-phase transport setting, the surviving second-order
singular values are

\[
1,
\qquad 1,
\qquad
\frac{|1+9uv+9u^2v^2+u^3v^3|}
{\sqrt{(1+9u^2+9u^4+u^6)(1+9v^2+9v^4+v^6)}}.
\]

This gives a first concrete second-order example where the surviving datum is a
principal-angle quantity of osculating subspaces rather than a raw jet matrix.

It also admits an explicit overlap-separation witness: there are endpoint pairs
with the same overlap but different nontrivial second-order singular value.
One such pair is

\[
(u,v)=(0,1),
\qquad
(u',v')=\left(\frac12,\alpha\right),
\]

where \(\alpha\) is the positive real root of

\[
81x^6-16x^5+37x^4-128x^3-107x^2-256x-171=0.
\]

For these two pairs the endpoint overlap is the same, but the nontrivial
second-order singular value is different.

## Benchmark Example

The best current small stress test is the harmonic-oscillator ground-state
family with variable frequency:

\[
\psi_\omega(x)=\left(\frac{\omega}{\pi}\right)^{1/4}e^{-\omega x^2/2},
\qquad \omega>0.
\]

Using the first jet pair \((|\psi_\omega\rangle,\partial_\omega|\psi_\omega\rangle)\),
the same-point block is exact and nonconstant:

\[
M(\omega)=
\begin{pmatrix}
1 & 0 \\
0 & \frac{1}{8\omega^2}
\end{pmatrix}.
\]

The endpoint overlap is

\[
I(\omega_-,\omega_+)=
\frac{\sqrt{2}\,(\omega_-\omega_+)^{1/4}}{\sqrt{\omega_-+\omega_+}}.
\]

This gives an exact mixed block and an exact bilaterally whitened block. It is
therefore a better stress test than the earlier qubit and coherent-state
examples.

But the example has a built-in warning:

- in the parameter \(\omega\), the same-point block is nonconstant;
- in the squeeze parameter \(r=\tfrac12\log\omega\), that same behavior can be
  normalized away.

There is also one positive lesson. In this specific one-parameter first-jet
benchmark, the raw same-point and mixed blocks do change under
\(\omega \leftrightarrow r=\tfrac12\log\omega\), but the bilaterally whitened
two-point block stays unchanged. So the oscillator family is not only a warning
about coordinate sensitivity; it is also evidence that whitening can remove at
least some parameterization artifacts.

At present this should be read narrowly:

- it is an exact fact for this benchmark;
- it is not yet a general theorem for arbitrary one-parameter families;
- it says nothing yet about higher jets or multiparameter families.

There is also now a better finite-dimensional benchmark for the singular-value
side. Consider the real qutrit curve

\[
|\psi(t)\rangle=\frac{(1,t,t^2)^T}{\sqrt{1+t^2+t^4}}.
\]

For this family, in the reduced scalar-phase transport setting, the singular
values of the whitened first-horizontal-jet block are **not** determined by the
endpoint overlap alone. One singular value is \(1\); the second is the cosine
between the endpoint first-jet plane normals. So this family is a clean first
example where the singular-value output carries more endpoint information than
overlap/fidelity alone.

More concretely, writing

\[
D(t)=1+t^2+t^4,
\qquad
J(t)=1+4t^2+t^4,
\]

the identity-transport representative of the whitened block is

\[
\Omega(u,v)=
\begin{pmatrix}
\frac{1+uv+u^2v^2}{\sqrt{D(u)D(v)}} &
\frac{(u-v)(1+2v^2+2uv+uv^3)}{\sqrt{D(u)D(v)J(v)}}\\[1.2ex]
\frac{(v-u)(1+2u^2+2uv+u^3v)}{\sqrt{D(u)D(v)J(u)}} &
\frac{1-u^4-v^4+5uv+4u^3v+4uv^3+5u^3v^3+u^4v^4}{\sqrt{D(u)D(v)J(u)J(v)}}
\end{pmatrix}.
\]

Its singular values are \(1\) and

\[
\frac{|1+4uv+u^2v^2|}{\sqrt{(1+4u^2+u^4)(1+4v^2+v^4)}}.
\]

An explicit witness that overlap does not determine the second singular value is

\[
(u,v)=\left(-5,\frac65\right),
\qquad
(u',v')=\left(-\frac52,-\frac35\right),
\]

for which

\[
I(u,v)=I(u',v')=\frac{25\sqrt{39}}{273},
\]

but the second singular values are different.

This is still a benchmark-level observation, not a transport-independent
general theorem.

## What Can Be Claimed Now

Safe claims:

1. The source paper's local object is well described, for this track, as a
   whitened local jet cross-Gram block.
2. The exact first-order quantum bridge is the same-point horizontal-derivative
   Gram matrix, i.e. the pure-state QGT.
3. For one-parameter pure-state curves, the bilaterally whitened
   first-horizontal-jet two-point block is invariant under
   orientation-preserving reparameterization, and it descends to ray space once
   a gauge-covariant transport rule is included as part of the data.
4. The oscillator family is a concrete stress test for nonconstant same-point
   blocks and bilateral whitening.

Unsafe claims, for now:

1. The full two-point whitened matrix is a canonical quantum-geometric tensor.
2. Higher jets already define a gauge- and reparameterization-safe matrix
   invariant.
3. The oscillator example proves intrinsic left/right asymmetry.
4. The construction is fundamental for quantum mechanics.

## Open Problems

1. Define a higher-jet covariantization that survives phase gauge and
   reparameterization cleanly.
2. Decide whether the meaningful two-point object is matrix-valued or only
   subspace-valued.
3. If matrix-valued, prove the extra structure needed:
   transport-independence, canonical parameter, canonical frames.
4. Extend or sharply delimit the new one-parameter first-horizontal-jet theorem:
   orientation reversal, higher jets, and multiparameter families.

## Provenance

- `quantum/findings.md`
- `quantum/20260423-043347-research-team-jet-gram-qm/notes/synthesis-1.md`
- `quantum/20260423-051725-attack-jet-qgt-core/notes/synthesis-2.md`
- `quantum/20260423-051725-attack-jet-qgt-core/reports/`
- `quantum/20260423-053100-attack-oscillator-reparam/reports/`
- `quantum/20260423-053443-attack-first-jet-reparam/reports/`
- `quantum/20260423-053832-attack-first-jet-gauge/reports/`
