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

## Current Package

The strongest exact results currently established in this note are:

1. The same-point first horizontal block is exactly the pure-state QGT.
2. For one-parameter curves, the bilaterally whitened first-horizontal-jet
   block has an exact reparameterization theorem, with orientation reversal
   acting by derivative-channel sign conjugation.
3. Raw higher-jet matrices fail, but higher osculating subspaces survive.
4. In a fixed ambient Hilbert space, the endpoint ambient osculating subspaces
   define canonical transport-free principal-angle and projector-spectrum data.
5. The qutrit / quartit benchmark families, and more generally the Veronese
   benchmark family, show that the surviving two-point data is generically
   richer than overlap alone on both the ambient `A_r` side and the
   value-channel-free `O_r` side.
6. For fixed endpoint subspaces, orthonormal-frame comparison matrices have a
   complete biunitary-orbit classification by the same principal-angle
   singular values, so entrywise matrices require extra frame-selecting
   structure.
7. In several parameters, raw, covariant, and symmetrized jet hierarchies
   determine the `O_r`/`A_r` filtrations and the corresponding
   operator/principal-angle package, but not an ordered matrix or frame from
   ray-field data alone.
8. With coherent reflection access, the principal-angle spectrum has a natural
   phase-estimation protocol for the product of endpoint reflections.

The boundary is now explicit: the canonical output is the subspace/operator
package and its principal-angle spectrum. Entrywise matrix representatives,
global `A_r` versus `O_r` selection rules, and stronger physical implementations
need extra structure beyond the scoped note.

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

## First-Order Two-Point Package

If one wants a quantum-side analogue of the source paper's two-point mixed and
whitened block, one must insert extra structure.

Let \(\lambda \mapsto |\psi(\lambda)\rangle\) be a \(C^1\) normalized local
lift of a one-parameter pure-state family, and define the first horizontal jet

\[
|h_\lambda\rangle:=(I-|\psi(\lambda)\rangle\langle\psi(\lambda)|)
\partial_\lambda|\psi(\lambda)\rangle.
\]

Choose a two-point transport rule \(U_{-\leftarrow +}\). In the frame
\((|\psi\rangle,|h_\lambda\rangle)\), define

\[
M_\lambda(\lambda_i)=
\begin{pmatrix}
1 & 0 \\
0 & \langle h_{\lambda_i}\mid h_{\lambda_i}\rangle
\end{pmatrix},
\qquad
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

This is a legitimate transported-frame construction, but not yet a canonical
matrix invariant.

The exact theorem at first order is:

- if \(\mu=\phi(\lambda)\) is orientation-preserving, then
  \(\Omega_\mu=\Omega_\lambda\);
- if the reparameterization reverses orientation, then
  \[
  \Omega_\mu=E\,\Omega_\lambda\,E,
  \qquad
  E=\operatorname{diag}(1,-1),
  \]
  provided one keeps the original ordered pair of endpoints fixed.

So the derivative channel is the only part that changes sign under orientation
reversal.

Under a local phase change \(|\psi(\lambda)\rangle\mapsto e^{i\chi(\lambda)}
|\psi(\lambda)\rangle\), the projector is unchanged and
\(h_\lambda\mapsto e^{i\chi(\lambda)}h_\lambda\). Therefore, if the transport
rule is itself gauge-covariant on the ray curve, the first-horizontal-jet block
is well defined on:

- a one-parameter ray curve,
- together with a chosen gauge-covariant transport rule,
- up to orientation-preserving reparameterization.

This is stronger than a fixed-lift statement, but weaker than a
transport-independent endpoint invariant.

There is one useful reduced class. If one explicitly restricts to
**scalar-phase transports** on the endpoint first-jet pair,

\[
U_{-\leftarrow +}=e^{i\alpha(\gamma)}I,
\]

then the whole first-horizontal-jet block changes only by one global phase.
Berry transport and Pancharatnam transport (when
\(\langle\psi_-\mid\psi_+\rangle\neq 0\)) lie in this same phase class.

The strongest exact derived output at first order is therefore the singular-value
package:

- for fixed gauge-covariant transport, the singular values are lift-invariant
  and invariant under all one-parameter reparameterizations, including
  orientation reversal;
- in the scalar-phase transport class, they are also transport-class invariant.

At first order there is also a useful split interpretation. Define the ambient
plane

\[
\mathcal A_1(\lambda)=\mathrm{span}\{\psi(\lambda),h_\lambda\}.
\]

Its principal angles with \(\mathcal A_1(\lambda_+)\) are canonical ambient
invariants. The singular values of the whitened first-horizontal-jet block
coincide with those principal-angle cosines exactly when the block is realized
in the common ambient space, for example in the identity/scalar-phase transport
setting. For a general transport convention, the same singular values describe
the principal angles between \(\mathcal A_1(\lambda_-)\) and the transported
plane \(U\mathcal A_1(\lambda_+)\).

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

For one-parameter curves there is also an exact higher-order gauge-covariant jet
hierarchy. Let

\[
a(t):=\langle\psi(t),\partial_t\psi(t)\rangle,
\qquad
\nabla_t\xi:=P_t\bigl(\partial_t\xi-a(t)\xi\bigr),
\qquad
P_t:=I-|\psi(t)\rangle\langle\psi(t)|.
\]

If \(\xi\mapsto e^{i\chi(t)}\xi\) under phase gauge, then
\(\nabla_t\xi\mapsto e^{i\chi(t)}\nabla_t\xi\). Defining

\[
h_{[1]}:=\nabla_t\psi=j_1,
\qquad
h_{[k+1]}:=\nabla_t h_{[k]},
\]

one obtains gauge-covariant higher jets with the same osculating subspaces as
the raw projected jets:

\[
\mathrm{span}\{h_{[1]},\dots,h_{[r]}\}=O_r(t).
\]

So in one parameter the failure is not the absence of a covariant hierarchy; it
is the continued lack of a canonical higher-jet matrix representative beyond the
subspace data.

The same point now extends to several parameters at the subspace level. Writing

\[
a_a:=\langle\psi,\partial_a\psi\rangle,
\qquad
\nabla_a\xi:=P\bigl(\partial_a\xi-a_a\xi\bigr),
\]

one obtains an exact gauge-covariant hierarchy from ordered iterated operators
\(\nabla_{a_k}\cdots\nabla_{a_1}\psi\). These covariant jets still span the same
canonical `O_r` spaces as the raw mixed partial jets. This repairs the
generators at the subspace level, but not at the level of an ordered frame or
entrywise matrix. Raw coordinate arrays transform by non-unitary
block-upper-triangular gauge/chart laws; covariant generators still depend on
chosen tangent directions and do not select an orthonormal basis of the
resulting subspace.

Moreover, ordering matters only up to lower-order terms. The commutator
\([\nabla_a,\nabla_b]\) is zero-th order on the horizontal bundle, so the same
subspace filtration is generated by **symmetrized** covariant jets as by ordered
ones. Thus the multiparameter ray-field data determines the filtered subspaces
`O_r` and, after adjoining the state line, `A_r`; it does not determine a
canonical ordered matrix/frame package beyond that common symmetrized subspace
data.

At two endpoints this leaves exactly the same basis-free operator package as
above: endpoint projectors, cross-contractions, polar partial isometries on the
nonzero-overlap sectors, and principal-angle spectra. By the biunitary-orbit
classification below, any orthonormal-frame comparison matrix for these
endpoint subspaces is only a representative of an orbit classified by those
principal-angle singular values. Matrices can still arise after adding explicit
frame-selecting structure, such as preferred coordinates, a source metric or
connection, a dynamics, a transport rule, a protocol, or symmetry breaking. A
tensor-valued associated-graded jet symbol may also be useful as a separate
basis-free object. Neither is an ordered matrix/frame package determined by the
multiparameter ray-field hierarchy alone.

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

`O_r` is the horizontal, value-channel-removed object and stays closest to the
original jet-normalized motivation. `A_r` is the ambient extension used when the
state line is intended to remain part of the endpoint subspace package. The
current invariant package gives this role split, not a global rule selecting one
object for every purpose.

There is also a precise quotient relation: the orthogonal projector
\(P=I-|\psi\rangle\langle\psi|\) restricts to a surjection \(A_r\to O_r\) with
kernel \(\mathrm{span}\{\psi\}\), so `O_r` is canonically the Hilbert-space
quotient of `A_r` by the state line.

Current benchmarks sharpen this split. On the qutrit first-order and quartit
second-order families, `O_r` already carries richer two-point geometry than
overlap alone. On the quartit benchmark, `O_2` is actually finer than `A_2` at
the level of principal-angle data. This does not make `O_r` universally
dominant, and the unlabeled principal-angle data of an `A_r` endpoint pair does
not by itself identify the state line inside `A_r`. The note keeps both objects
on purpose: `O_r` for value-channel-free horizontal geometry, and `A_r` for
ambient subspace, Krylov, and full-subspace projector packages.

There is also one useful dynamical specialization. For a unitary orbit
\(\psi(t)=e^{-itH}\psi_0\), the ambient space \(A_r(t)\) is exactly the
transported order-\(r\) Krylov space generated by \((H,\psi_0)\), while
`O_r(t)` is its value-channel-removed / compressed counterpart. This is an
exact reformulation, not a new invariant.

If the cyclic space of \((H,\psi_0)\) has finite dimension \(m\), this picture
stabilizes exactly at order \(m-1\): for every \(r\ge m-1\), the spaces
\(A_r(t)\) and \(O_r(t)\) stop changing, and so do all the exact two-point
principal-angle / projector-spectrum invariants built from them.

In that finite-cyclic case there is also a canonical matrix normal form. The
spectral measure of \((H,\psi_0)\) determines orthonormal polynomials and hence
a canonical Lanczos/Jacobi basis of the full cyclic space. In that basis,
\(H\) is represented by a finite Jacobi matrix \(J\), and the full ambient
two-point package is exactly the matrix function \(e^{-i\Delta J}\). This is an
exact specialization of the already-known unitary/Krylov package, not a new
general matrix theorem.

In particular, exact unitary orbits avoid rank-jump issues entirely: both `A_r`
 and `O_r` move by unitary conjugation, so their ranks are constant and the
 local projector/subspace metrics are globally well defined along the orbit.

At finite separation, the same unitary specialization says that the two-point
principal-angle data is exactly the singular-value/spectral data of the
propagator compressed to the initial subspace. On the ambient side this is the
compression of \(e^{-i\Delta H}\) to the initial Krylov space; on the
value-channel-free side it is the analogous compression to the initial
compressed Krylov space. This is a dynamical corollary of the subspace theorem,
not a stronger matrix result.

At small \(\Delta\), this finite-separation data has an exact leakage expansion:
if \(\Pi_t\) is the orthogonal projector onto the moving subspace and
\(L_t=(I-\Pi_t)H\Pi_t\), then the endpoint compression satisfies

\[
\Pi_t\Pi_{t+\Delta}\Pi_t\big|_{S(t)}=I-\Delta^2 L_t^*L_t+O(\Delta^3).
\]

So the leading defect from identity is exactly the positive leakage operator.
Its trace is the local projector-metric density, and in rank one it reduces to
the usual Hamiltonian variance.

This ambient-subspace theorem also extends cleanly to several parameters. If the
parameter space is a manifold and one includes **all mixed partials of total
order at most \(r\)**, then the resulting ambient osculating subspace is still
independent of local phase gauge and of chart choice. So the multiparameter
extension survives exactly at the subspace/principal-angle level, while the
entrywise matrix story resolves only to the same biunitary-orbit statement:
without extra frame-selecting structure, the canonical output is the
operator/principal-angle package.

As a basis-free corollary, if \(\Pi_\pm\) are the orthogonal projectors onto the
canonical endpoint subspaces, then the compression

\[
K_-:=\Pi_-\Pi_+\Pi_-\big|_{\mathcal A_r(x_-)}
\]

has spectrum equal to the squared principal-angle cosines. This is a clean
operator reformulation of the same subspace data, not a stronger invariant.

Equivalently, the canonical cross-contraction
\(C=\Pi_-|_{S_+}:S_+\to S_-\) has a canonical polar decomposition
\(C=V|C|\). The partial isometry \(V\) gives a basis-free transport on the
nonzero-overlap sector, while \(|C|\) carries the principal-angle spectrum. This
is the strongest exact operator-level transport presently justified, but it is
still not a canonical full matrix package.

More precisely, let \(\dim S_-=p\) and \(\dim S_+=q\), and let
\(U_-:\mathbb C^p\to S_-\), \(U_+:\mathbb C^q\to S_+\) be orthonormal frame
isometries. The comparison matrix
\[
A=U_-^*U_+
\]
is the matrix of \(C\) in these two frames. Replacing the endpoint frames by
\(U_-L\) and \(U_+R\), with \(L\in U(p)\) and \(R\in U(q)\), changes the matrix
exactly by \(A\mapsto L^*AR\), and every orthonormal-frame comparison matrix for
the same pair arises in this way. For fixed \(p,q\), rectangular SVD classifies
this biunitary orbit by the singular values of \(A\), including rank-deficient
zeros and the forced rectangular zero rows or columns in a normal form. These
singular values are exactly the principal-angle cosines. Thus a sorted diagonal
SVD representative is only an orbit normal form carrying dimensions and
principal angles; it is not an endpoint-selected comparison matrix, and zero
singular sectors or rectangular padding do not select frames.

On that nonzero-overlap sector, canonical principal frames exist from the
subspace pair alone exactly when the nonzero spectrum is simple. In the simple
case one gets canonical matched principal vectors up to phase/sign; in repeated
nonzero blocks the strongest exact canonical object remains the block partial
isometry coming from the polar factor, not a frame.

If the nonzero spectrum of this compression is simple, then the corresponding
principal directions are canonical up to independent phase/sign choices. In that
nondegenerate sector one may therefore choose canonical principal frames and a
diagonal comparison matrix with entries \(\cos\theta_i\). This is a conditional
normal form for the already-known principal-angle data, not a stronger general
matrix theorem.

The converse boundary is also sharp. If a nonzero principal value has
multiplicity \(m\ge2\), then the corresponding principal block carries an
unavoidable internal \(U(m)\) freedom, so no canonical orthonormal principal
frame can be recovered from the subspace pair alone. In that degenerate sector,
the strongest exact canonical object is the block partial isometry coming from
the polar decomposition of the canonical cross-contraction, not a frame or an
entrywise matrix representative.

Taken together, the complete exact operator package of a canonical subspace pair
is therefore: the cross-contraction \(C\), the positive compressions
\(K_\pm=C^*C,CC^*\), the polar partial isometry \(V\) on the nonzero-overlap
sector, the simple-spectrum diagonal-frame corollary, and the repeated-spectrum
no-go. This is the strongest exact operator-level refinement now available, and
it still does not amount to a canonical full matrix package.

In finite dimension, this package is also complete up to ambient unitary
equivalence: the dimensions of the two endpoint subspaces together with the
principal-angle multiset determine the subspace pair up to unitary conjugacy.
So the current operator package is not only canonical; it is complete at the
subspace-pair level.

On the current benchmark families this conditional normal form is genuinely
usable on a nonempty open set. For the qutrit first-order benchmark there is
only one nontrivial principal angle, so simplicity is automatic. For the
quartit `O_2` and, more generally, the Veronese `O_{n-1}` benchmarks, the
nontrivial singular block is generically simple, so the diagonal principal-frame
normal form is available on an open dense set of endpoint pairs.

If the nonzero spectrum of this compression is simple, then the corresponding
principal directions are canonical up to independent phase/sign choices. In that
simple spectral sector one may therefore choose canonical principal frames and a
diagonal comparison matrix with entries \(\cos\theta_i\). This is a conditional
normal form for the already-known principal-angle data, not a stronger general
matrix theorem.

It also has a short exact operational reading. For a state prepared in the
`-` endpoint subspace, the operator \(\Pi_-\Pi_+\Pi_-\) is the effect operator
for the ideal sequential yes/yes test “is the state in the `-` subspace?” then
“is the post-measurement state in the `+` subspace?”. Its eigenvalues are
therefore the corresponding optimal success probabilities \(\cos^2\theta_i\).
This is an operator interpretation of the same subspace-overlap data, not a new
physical theorem.

There is also a coherent protocol under an explicit access hypothesis. If the
endpoint projectors can be implemented as reflections
\[
R_\pm=2\Pi_\pm-I,
\]
then the alternating-reflection unitary \(R_-R_+\) acts on each nontrivial
principal two-plane with eigenphases \(\pm 2\theta_i\). The intersection and
orthogonal residual sectors give the expected exceptional phases \(+1\) and
\(-1\), and unequal-dimensional padding must be tracked with the endpoint
dimensions and preparation support. Thus controlled phase estimation estimates
the principal angles when coherent reflection access and adequate
state-preparation or sampling are available. This is a protocol for reading the
existing principal-angle/operator package, not a new invariant, not a canonical
matrix representative, and not a substitute for the exact unitary/Krylov or
pathwise Kato specializations below.

For exact unitary subspace orbits \(S(t)=e^{-itH}S(0)\), there is also a short
local dynamical corollary. If \(\Pi_t\) is the orthogonal projector onto
\(S(t)\), then

\[
\dot\Pi_t=-i[H,\Pi_t],
\qquad
\frac12\|\dot\Pi_t\|_{HS}^2
=\frac12\|[H,\Pi_t]\|_{HS}^2
=\|(I-\Pi_t)H\Pi_t\|_{HS}^2.
\]

So the local Grassmannian speed is exactly the Hilbert-Schmidt size of the
Hamiltonian block leaking the subspace into its orthogonal complement. This is
an infinitesimal corollary of the projector formalism, not a new invariant.

More generally, every smooth projector path has an exact Kato transport
realization:

\[
H_K(t)=i[\dot\Pi(t),\Pi(t)],
\qquad
\Pi(t)=U_K(t)\Pi(0)U_K(t)^*.
\]

This is the unique realizing Hamiltonian with vanishing instantaneous
block-diagonal part relative to the moving projector. It gives a canonical
pathwise dynamical model of the subspace path, but it is path-dependent and does
not by itself solve the endpoint matrix-canonicity problem.

In several parameters, that path dependence has an exact curvature obstruction.
The Kato connection on the projector bundle has curvature

\[
R^K=\Pi(d\Pi\wedge d\Pi)\Pi.
\]

Nonzero curvature forces local holonomy, hence rules out endpoint-independent
Kato transport. In rank one this reduces exactly to Berry curvature. So the
Kato picture gives an exact pathwise transport, but generically not an
endpoint-only matrix package.

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

The value-channel-free side is also explicit on this same benchmark. For

\[
O_2(t)=\mathrm{span}\{j_1(t),j_2(t)\},
\]

the principal-angle cosines of \(O_2(u),O_2(v)\) are the singular values of the
compact \(2\times 2\) matrix

\[
M_{O_2}(u,v)=
\begin{pmatrix}
\frac{1+uv+u^2v^2+u^3v^3}{\sqrt{D_4(u)D_4(v)}} & \frac{(u-v)^3}{\sqrt{D_4(u)N_4(v)}}\\[1.2ex]
-\frac{(u-v)^3}{\sqrt{N_4(u)D_4(v)}} & \frac{1+9uv+9u^2v^2+u^3v^3}{\sqrt{N_4(u)N_4(v)}}
\end{pmatrix},
\]

where \(D_4(t)=1+t^2+t^4+t^6\) and \(N_4(t)=1+9t^2+9t^4+t^6\). In
particular, `O_2` is strictly finer than `A_2` on this benchmark: `A_2`
retains only the product of the two `O_2` singular values, while `O_2` keeps
both.

## Benchmarks

### Oscillator

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

### Qutrit

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

The value-channel-free line \(O_1(t)=\mathrm{span}\{h_t\}\) is already rich on
this benchmark as well: there are endpoint pairs with the same overlap but
different `O_1` principal-angle cosine. For example, \((0,1)\) and
\((-2,\beta)\), where \(\beta\) is any real root of
\(9x^4-16x^3+5x^2-4x-6=0\), have the same overlap but different `O_1` data.

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

### Quartit And Veronese

These low-dimensional polynomial benchmarks are not isolated accidents. They are
the first two cases of a clean order-\(n-1\) Veronese-family statement for
\(v_n(t)=(1,t,\dots,t^n)\): the ambient osculating subspace is a codimension-1
hyperplane whose normal is the coefficient vector of \((x-t)^n\), and the
single nontrivial principal-angle cosine is the normalized binomial-square
polynomial in \(uv\). This is best read as a benchmark-family theorem, not as a
new generic result about arbitrary quantum families.

Moreover, for every \(n\ge 2\) in that family, this nontrivial principal-angle
cosine is generically not determined by endpoint overlap alone; the richer-than-
overlap behavior seen in the qutrit and quartit cases is therefore systematic,
not accidental.

The same is true on the value-channel-free side: the order-\(n-1\) complement
matrix for \(O_{n-1}\) has determinant equal to this same nontrivial cosine, so
the `O_{n-1}` data is generically not determined by overlap alone for every
\(n\ge2\) as well.

A simple non-Veronese benchmark also exists: the spherical-twist curve
\(\psi(t)=(\cos t\cos 2t,\cos t\sin 2t,\sin t)\) already has exact endpoint
pairs with the same overlap but different `A_1` and `O_1` angle data. For
example, \((0,\pi/4)\) and \((0,\pi/2)\) both have overlap `0`, but
\[
c_{A_1}\!\left(0,\frac{\pi}{4}\right)=\frac{\sqrt{15}}{5},
\qquad
c_{A_1}\!\left(0,\frac{\pi}{2}\right)=-\frac{\sqrt5}{5},
\]
and
\[
c_{O_1}\!\left(0,\frac{\pi}{4}\right)=-\frac{\sqrt{30}}{30},
\qquad
c_{O_1}\!\left(0,\frac{\pi}{2}\right)=0.
\]
So the richer-than-overlap phenomenon is not confined to polynomial families.
In fact this persists for the whole twist family
\(\psi_k(t)=(\cos t\cos kt,\cos t\sin kt,\sin t)\), \(k\ge2\), with exact
equal-overlap witnesses for every integer \(k\).

There is also a local genericity theorem behind these examples. For normalized
real \(C^2\) curves in a finite-dimensional Hilbert space of dimension at least
\(3\), fix two distinct parameter values and assume the endpoint velocities are
nonzero. Let
\[
I(u,v)=\langle\psi(u),\psi(v)\rangle,\qquad
T(t)=\frac{\psi'(t)}{\|\psi'(t)\|},\qquad
C(u,v)=\langle T(u),T(v)\rangle .
\]
On a branch where \(C\ne0\), the first value-channel-free `O_1` line-angle
observable is locally independent of endpoint overlap whenever
\[
\det\frac{\partial(I,C)}{\partial(u,v)}\ne0 .
\]
This determinant depends only on the endpoint \(2\)-jets. On the admissible
endpoint \(2\)-jet chart it is a nonzero polynomial after clearing the nonzero
velocity denominators, so its nonvanishing is an open dense finite-jet
condition. Consequently any smooth finite-dimensional curve family whose
endpoint \(2\)-jet map is submersive onto such a chart, and any connected
real-analytic family for which the pulled-back determinant is not identically
zero, has an open dense locus where the `O_1` line-angle data is not locally
determined by overlap alone. The same finite-jet statement applies to complex
Hilbert spaces after realification and on a smooth branch of the absolute
principal-angle observable. This is a first-order `O_1` genericity theorem, not
a blanket claim for all higher `O_r` or `A_r` observables.

## What Can Be Claimed Now

Safe claims:

1. The source paper's local object is well described, for this track, as a
   whitened local jet cross-Gram block.
2. The exact first-order quantum bridge is the same-point horizontal-derivative
   Gram matrix, i.e. the pure-state QGT.
3. For one-parameter pure-state curves, the bilaterally whitened
   first-horizontal-jet two-point block is invariant under
   orientation-preserving reparameterization, and under orientation reversal it
   transforms by derivative-channel sign conjugation.
4. At first order, after a gauge-covariant transport choice, the two-point block
   descends to ray space; in the scalar-phase class its singular values are also
   transport-class invariant.
5. Higher raw jet matrices fail, but the higher osculating subspaces survive.
   In one parameter there is also an exact gauge-covariant higher-jet hierarchy
   with the same `O_r` subspaces.
6. In a fixed ambient Hilbert space, the endpoint osculating subspaces define
   canonical transport-free principal-angle and projector-spectrum data.
7. In finite dimension, the resulting principal-angle/operator package is
   complete up to ambient unitary equivalence.
8. For fixed endpoint subspaces, all orthonormal-frame comparison matrices form
   one biunitary orbit, classified by the singular values/principal-angle
   cosines; an entrywise representative requires extra frame-selecting
   structure.
9. In several parameters, raw, covariant, and symmetrized jet hierarchies
   determine the canonical `O_r` and `A_r` filtrations and the corresponding
   operator/principal-angle package, but no ordered matrix/frame from the
   ray-field data alone.
10. The relation \(A_r=\mathrm{span}\{\psi\}\oplus O_r\) gives a role split:
    `O_r` is the horizontal/value-channel-removed quotient object, while `A_r`
    is the ambient extension when the state line belongs in the endpoint
    subspace package. No unique global winner is forced by the current
    invariants.
11. With coherent reflection access to endpoint projectors, phase estimation on
    \((2\Pi_- - I)(2\Pi_+ - I)\) gives a natural protocol for estimating the
    already-canonical principal-angle spectrum.
12. First-order value-channel-free richer-than-overlap behavior is generic in
    the finite-jet sense for normalized curves in dimension at least \(3\),
    under the stated endpoint \(2\)-jet rank condition.
13. There are now explicit benchmark families on both the ambient `A_r` side and
    the value-channel-free `O_r` side where the surviving two-point data is not
    determined by overlap alone.

Unsafe claims, for now:

1. The full two-point whitened matrix is a canonical quantum-geometric tensor.
2. Higher jets already define a gauge- and reparameterization-safe matrix
   invariant.
3. A unique global choice between `A_r` and `O_r` is already mathematically
   forced in all roles.
4. The construction is fundamental for quantum mechanics.

## Open Problems

No open problem remains in the scoped quantum note. Stronger variants would
require new targets, such as higher-order `O_r/A_r` genericity or a
source-specific physical implementation of the reflection protocol.

## Provenance

- `quantum/findings.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/notes/synthesis-1.md`
- `quantum/teams/20260423-051725-attack-jet-qgt-core/notes/synthesis-2.md`
- `quantum/teams/20260423-051725-attack-jet-qgt-core/reports/`
- `quantum/teams/20260423-053100-attack-oscillator-reparam/reports/`
- `quantum/teams/20260423-053443-attack-first-jet-reparam/reports/`
- `quantum/teams/20260423-053832-attack-first-jet-gauge/reports/`
- `quantum/teams/20260423-130653-attack-first-jet-remaining/reports/`
- `quantum/teams/20260423-131101-attack-transport-class/reports/`
- `quantum/teams/20260423-131550-attack-first-jet-singular-values/reports/`
- `quantum/teams/20260423-132614-attack-richer-family/reports/`
- `quantum/teams/20260423-133641-attack-qutrit-omega/reports/`
- `quantum/teams/20260423-134344-attack-higher-jets/reports/`
- `quantum/teams/20260423-135052-attack-quartit-osculating/reports/`
- `quantum/teams/20260423-140111-attack-transport-free-subspaces/reports/`
- `quantum/teams/20260423-140931-attack-multiparameter-osculating/reports/`
- `quantum/teams/20260423-142558-attack-Or-vs-Ar-benchmarks/reports/`
- `quantum/teams/20260423-190226-attack-veronese/reports/`
- `quantum/teams/20260423-192859-attack-Or-veronese/reports/`
- `quantum/teams/20260423-194242-attack-veronese-richness/reports/`
- `quantum/teams/20260423-194725-attack-Or-richness/reports/`
- `quantum/teams/20260423-195245-attack-lower-order-veronese/reports/`
- `quantum/teams/20260423-201939-attack-krylov/reports/`
- `quantum/teams/20260423-204337-attack-nonveronese/reports/`
- `quantum/teams/20260423-215017-attack-spherical-witness/reports/`
- `quantum/teams/20260423-234645-attack-covariant-jets/reports/`
- `quantum/teams/20260423-235606-attack-multiparameter-covariant-jets/reports/`
- `quantum/teams/20260424-001425-attack-commutator-metric/reports/`
- `quantum/teams/20260424-002612-attack-propagator-subspaces/reports/`
- `quantum/teams/20260424-003729-attack-canonical-frames/reports/`
- `quantum/teams/20260424-004443-attack-simple-spectrum-benchmarks/reports/`
- `quantum/teams/20260424-004954-attack-constant-rank/reports/`
- `quantum/teams/20260424-021540-attack-rank-growth/reports/`
- `quantum/teams/20260424-014948-attack-lower-order-Or/reports/`
- `quantum/teams/20260424-020810-attack-polar-transport/reports/`
- `quantum/teams/20260424-023315-attack-degenerate-nogo/reports/`
- `quantum/teams/20260424-024917-attack-frame-criterion/reports/`
- `quantum/teams/20260424-025436-attack-smooth-frames/reports/`
- `quantum/teams/20260424-024026-attack-short-time-expansion/reports/`
- `quantum/teams/20260424-030000-attack-operator-package/reports/`
- `quantum/teams/20260424-030928-attack-smooth-polar/reports/`
- `quantum/teams/20260424-032829-attack-saturation/reports/`
- `quantum/teams/20260424-033611-attack-twist-family/reports/`
- `quantum/teams/20260424-034240-attack-quotient/reports/`
- `quantum/teams/20260424-054845-attack-cs-normal-form/reports/`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183451-gap-biunitary-matrix-finality/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-183451-verifier-biunitary-finality/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-190708-gap-multiparameter-frame-finality/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-191018-verifier-multiparameter-frame-finality/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-191454-gap-Ar-Or-role-split/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-191817-verifier-Ar-Or-role-split/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-192133-gap-natural-protocol/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-192735-verifier-natural-protocol/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-193527-gap-nonbenchmark-genericity/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-193527-gap-nonbenchmark-genericity/scripts/verify_o1_jet_determinant.py`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-194246-verifier-nonbenchmark-genericity/report.md`
- `quantum/teams/20260423-043347-research-team-jet-gram-qm/agents/20260424-194246-verifier-nonbenchmark-genericity/scripts/verify_uv015_seed.py`
- `quantum/teams/20260424-032829-attack-saturation/reports/`
- `quantum/teams/20260424-033611-attack-twist-family/reports/`
- `quantum/teams/20260424-034240-attack-quotient/reports/`
