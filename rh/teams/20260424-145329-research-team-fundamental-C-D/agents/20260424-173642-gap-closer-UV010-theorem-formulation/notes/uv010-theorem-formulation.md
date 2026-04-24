# UV-010 theorem formulation

## Paper-ready target

The clean UV-010 theorem is a definition/edge-regularity theorem, not a
descent theorem and not a diagonal-merger theorem.

**Theorem target.** Work on a compact good collision patch
\[
J\Subset \{c\neq0,\ M\neq0,\ A_5^{\mathfrak f}\neq0\}.
\]
For close normalized two-atom data set
\[
m=\frac{h_1+h_2}{2},\qquad
\delta=h_2-h_1,\qquad
\lambda=-\frac{a_2}{a_1},\qquad
\omega=\frac{\lambda-1}{\lambda+1},\qquad
\kappa=\frac{2\omega}{\delta},
\]
with \(a_1\neq0\), \(\lambda\) near \(1\), and \(\kappa\) bounded after
blow-up. Let
\[
Q_t:=\mathfrak f/\mathbf C A_5^{\mathfrak f}(t).
\]

Assume the actual corrected two-atom finite-order package through order \(7\)
defines a septic quotient defect
\[
\overline{\mathcal E}_{12}^{(7;1)}(a_1,h_1;a_2,h_2)\in Q_{h_1}
\]
as an analytic moving-quotient section before any diagonal-merger input. Assume
there is an analytic collision-chart trivialization
\[
\tau_{m,\omega,\delta}:Q_{h_1}\longrightarrow Q_m
\]
on the same patch, normalized by \(\tau_{m,0,0}=\mathrm{id}_{Q_m}\) and
compatible with the chosen \(h_1\)-quotient convention. If the paper instead
uses the \(h_2\)-quotient convention, the theorem must specify the corresponding
trivialization to \(Q_m\).

Amplitude convention: the displayed UV-010 defect is the \(a_1\)-normalized,
fixed-target class
\[
\overline E_{12}^{(7;1)}
:=
\tau_{m,\omega,\delta}
\left(a_1^{-1}\overline{\mathcal E}_{12}^{(7;1)}\right)\in Q_m.
\]
With this convention \(R\) represents
\(-\overline E_{12}^{(7;1)}\). If the canonical draft keeps the raw defect
notation from the quantitative theorem, the statement must replace the displayed
edge law by the equivalent normalized version after applying \(a_1^{-1}\) and
\(\tau_{m,\omega,\delta}\).

Assume the fixed-target normalized quotient defect is analytic in
\((m,\omega,\delta)\), swap-even in the collision chart, and vanishes on the
collision locus:
\[
\overline E_{12}^{(7;1)}(m,-\omega,-\delta)
=
\overline E_{12}^{(7;1)}(m,\omega,\delta),
\qquad
\overline E_{12}^{(7;1)}(m,0,0)=0.
\]
Then there is an analytic section
\[
\mathcal H_7^q(m,\kappa,\delta^2)\in Q_m
\]
such that
\[
\overline E_{12}^{(7;1)}
=
\delta^2\mathcal H_7^q(m,\kappa,\delta^2).
\]
Consequently the exceptional-divisor quotient class is definable as
\[
[R]_{\mathrm{edge}}(m,\kappa)=-\mathcal H_7^q(m,\kappa,0)\in Q_m.
\]

No conclusion about descent, \(\kappa\)-independence, determinant constancy, or
identification with \(\widehat\Psi(m)\) belongs to UV-010. Those are downstream
C-FS3/package-merger targets.

## Current mechanisms

### `rh/proof_of_rh.tex:11888-12189`

Proved: Lemma `minimal-source-level-two-point-criterion` proves the formal
quadratic factorization
\[
\mathcal I_2=a_1a_2(h_1-h_2)^2\mathcal J_2
\]
for a fixed finite-dimensional target \(V\), but only from analytic package,
swap symmetry, one-amplitude collapse, and diagonal merger.

Conditional: the corollary applies that lemma to the conditional actual
order-7 target
\[
\mathbf C\oplus\mathfrak f\oplus
\bigl(\mathfrak f/\mathbf C A_5^{\mathfrak f}\bigr)
\]
and gives only \(O(\delta^2)\) for the normalized septic quotient defect on
good patches.

Missing without diagonal merger: the actual order-7 quotient defect, the
moving-line-to-midpoint trivialization, a named \(\mathcal H_7^q\), and a
diagonal-free proof of the \(\delta^2\) edge law. Lines 12168-12189 explicitly
name diagonal merger as one of the remaining finite-order source identities.

### `rh/proof_of_rh.tex:12385-12584`

Proved/usable: the source defines the cancellation variables
\((m,\delta,\lambda,\omega,\kappa)\) and records the generic analytic parity
template: an actual corrected defect that is analytic, swap-even, and
collision-vanishing has the form \(\delta^2\mathcal H(m,\kappa,\delta^2)\).

Conditional: displayed edge laws exist only for the cubic and quintic defects,
with edge values \(\mathcal H_3\) and \(\mathcal H_5\).

Missing: no order-7 quotient defect, no fixed quotient target, no midpoint
trivialization, no \(\mathcal H_7^q\), and no descent/merger result. The
subsequent remarks keep quotient transport/state-local closure and
package-level coincidence/functoriality as downstream programs.

### `rh/proof_of_rh.tex:24520-24610`

Proved/source-supported: the later summary separates the stronger
finite-order source route from the weaker quotient-diagonal route, and records
that naive source-summed corrected-block coefficients do not supply the needed
linear merger law.

Conditional: the stronger local route still requires the actual corrected
two-pair cubic/quintic/septic package to satisfy swap, one-amplitude collapse,
and diagonal merger.

Missing for UV-010: this summary does not construct the order-7 quotient edge
package. It instead lists finite-order source merger, quotient-diagonal
continuity/diagonal collapse, and a transport/package theorem as live targets.

### `rh/proof_of_rh.tex:24990-25030`

Proved/source-supported: the summary says \(\widehat\Psi\) remains the correct
bridge and that the minimal finite-order criterion isolates the exact swap /
one-amplitude / diagonal-merger package needed for quadratic interaction
factorization.

Conditional: the live downstream targets are edge-law regularity for actual
corrected cubic/quintic defects, quotient-visible transport/state-local closure,
and a provenance-sensitive package theorem.

Missing for UV-010: no septic quotient edge law is stated. The line window
supports the ordering "edge package first, quotient transport second, package
coincidence/merger third"; it does not prove any of the three for the order-7
quotient class without additional input.
