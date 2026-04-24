# Background split derivation

## Fixed convention

For the current paired quotient
\[
\Phi_\chi^{\mathrm{pair}}(s)
=\frac{\Xi_\chi(2s-1)}{\Xi_\chi(2s)},
\qquad
\Xi_\chi(w)=\Lambda(w,\chi)\Lambda(w,\bar\chi),
\]
set
\[
D_\chi(t):=
\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
-\frac{\Xi_\chi'}{\Xi_\chi}(2it).
\]
Then
\[
\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}{\Phi_\chi^{\mathrm{pair}}}
\left(\frac12+it\right)
=2\frac{\Xi_\chi'}{\Xi_\chi}(2it)
-2\frac{\Xi_\chi'}{\Xi_\chi}(1+2it)
=-2D_\chi(t).
\]
With
\(\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)}\)
and \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\,\prime}\),
the positive source scalar is the real boundary value of \(D_\chi\), equivalently
\[
q_\chi^{\mathrm{pair}}(t)
=-\frac12
\frac{\Phi_\chi^{\mathrm{pair}\,\prime}}{\Phi_\chi^{\mathrm{pair}}}
\left(\frac12+it\right)
=D_\chi(t)
\]
on regular boundary intervals, with the understood real-part projection when
the identity is written as a scalar kernel sum.

## Completed-Hadamard normalization

Assume the standard primitive nonprincipal completed-function package:
\(\Xi_\chi\) is entire of order one and has a genus-one Hadamard logarithmic
derivative
\[
\frac{\Xi_\chi'}{\Xi_\chi}(w)
=b_\chi+\sum_\rho m_\rho
\left(\frac1{w-\rho}+\frac1{\rho}\right),
\]
with zeros counted in the completed zero multiset of
\(\Xi_\chi=\Lambda_\chi\Lambda_{\bar\chi}\). If \(\rho=0\) occurs, the finite
factor must be removed and treated separately before using the displayed
\(1/\rho\) notation.

The edge difference cancels the Hadamard constant and the genus-one
regularizers:
\[
D_\chi(t)=
\sum_\rho m_\rho
\left(\frac1{1+2it-\rho}-\frac1{2it-\rho}\right),
\]
with compact-uniform convergence on regular intervals by the checked
\(O_I(|\rho|^{-2})\) edge-difference estimate. Therefore the theorem-facing
completed normalization can take
\[
S_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)
=\Re \sum_\rho m_\rho
\left(\frac1{1+2it-\rho}-\frac1{2it-\rho}\right),
\qquad
B_{\chi,\mathrm{comp}}^{\mathrm{pair}}(t)=0.
\]
In this normalization the conductor, gamma factors, trivial zeros, and
Hadamard exponential have already been absorbed into the completed entire
function and do not leave a residual after the completed zero edge-difference
is subtracted.

## Raw \(L\)-factor normalization

Let \(\mathfrak q_\chi\) be the conductor and
\(a_\chi\in\{0,1\}\) the parity, so
\[
\Lambda(w,\chi)
=\left(\frac{\mathfrak q_\chi}{\pi}\right)^{(w+a_\chi)/2}
\Gamma\left(\frac{w+a_\chi}{2}\right)L(w,\chi),
\]
and the same \(\mathfrak q_\chi,a_\chi\) apply to \(\bar\chi\). Then
\[
\frac{\Xi_\chi'}{\Xi_\chi}(w)
=\log\left(\frac{\mathfrak q_\chi}{\pi}\right)
+\psi\left(\frac{w+a_\chi}{2}\right)
+\frac{L'}{L}(w,\chi)+\frac{L'}{L}(w,\bar\chi).
\]
The conductor/scaling constant cancels exactly in \(D_\chi(t)\):
\[
B_{\mathrm{cond},\chi}^{\mathrm{pair}}(t)=0.
\]
The gamma piece is
\[
B_{\gamma,\chi}^{\mathrm{pair}}(t)
=\Re\left[
\psi\left(\frac{1+a_\chi+2it}{2}\right)
-\psi\left(\frac{a_\chi+2it}{2}\right)\right].
\]
If the raw source \(S_{\chi,\mathrm{raw}}^{\mathrm{pair}}\) is defined using
only nontrivial zeros of \(L(w,\chi)\) and \(L(w,\bar\chi)\), then a compatible
raw background has the schematic exact form
\[
B_{\chi,\mathrm{raw}}^{\mathrm{pair}}(t)
=B_{\gamma,\chi}^{\mathrm{pair}}(t)
+B_{\mathrm{triv},\chi}^{\mathrm{pair}}(t)
-B_{\mathrm{pole},\chi}^{\mathrm{pair}}(t)
+B_{\mathrm{Had},\chi}^{\mathrm{pair}}(t),
\]
where all terms are real parts of the same edge-difference kernel:
\[
B_{\mathrm{triv},\chi}^{\mathrm{pair}}(t)
=\Re\sum_{\eta\in\{\chi,\bar\chi\}}\sum_{\tau\in T_\eta}
m_{\eta,\tau}
\left(\frac1{1+2it-\tau}-\frac1{2it-\tau}\right),
\]
\[
B_{\mathrm{pole},\chi}^{\mathrm{pair}}(t)
=\Re\sum_{\eta\in\{\chi,\bar\chi\}}\sum_{p\in P_\eta}
n_{\eta,p}
\left(\frac1{1+2it-p}-\frac1{2it-p}\right),
\]
and \(B_{\mathrm{Had}}\) records any residual edge difference
\(E_\eta'(1+2it)-E_\eta'(2it)\) from the chosen raw Hadamard exponential
for \(L(w,\eta)\). For primitive nonprincipal characters \(P_\eta\) is empty.
For a genus-one completed edge-difference normalization there is no residual
\(B_{\mathrm{Had}}\); a nonzero residual here signals a raw normalization
choice, not a completed-source theorem term.

The raw formula is useful bookkeeping, but it is not the clean theorem-facing
UV-016 normalization unless its singular cancellations at gamma poles and
trivial zeros are stated explicitly. The clean package is the completed
normalization above: subtract completed zeros with multiplicity, then
\(B_{\chi,\mathrm{comp}}^{\mathrm{pair}}=0\).

