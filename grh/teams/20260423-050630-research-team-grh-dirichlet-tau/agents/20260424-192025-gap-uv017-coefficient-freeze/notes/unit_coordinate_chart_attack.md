# UV-017 Unit-Coordinate Chart Attack

Date: 2026-04-24

## Formal finite-s calculation

Let \(\Theta\) be the boundary phase used in the local block and put
\[
q(t)=\Theta'(t),\qquad t_\pm=m\pm s/2,\qquad
\Delta_m(s)=\Theta(t_-)-\Theta(t_+).
\]
The RH finite-\(s\) same-point and mixed blocks use only \(q(t_\pm)\),
\(q'(t_\pm)\), \(q''(t_\pm)\), and \(\Delta_m(s)\).

For a pure value deformation define
\[
\Theta_\alpha(t)=\Theta_0(t)+\alpha(t-m),
\qquad q_\alpha(t)=q_0(t)+\alpha.
\]
Then
\[
\frac{\partial}{\partial\alpha}q_\alpha(t_\pm)=1,\qquad
\frac{\partial}{\partial\alpha}q_\alpha'(t_\pm)=0,\qquad
\frac{\partial}{\partial\alpha}q_\alpha''(t_\pm)=0,
\]
and
\[
\Delta_{\alpha,m}(s)
=\Delta_{0,m}(s)+\alpha(t_- -t_+)
=\Delta_{0,m}(s)-\alpha s.
\]
If the source scalar in the same convention is
\[
S=q(m)-B(m),
\]
and the pure path freezes \(B(m)\), then along this path
\[
a:=q_\alpha(m)-B(m)=\alpha,
\qquad S(\alpha)=\alpha,
\qquad \frac{da}{dS}\bigg|_{0}=1.
\]

Thus the RH finite-\(s\) formulas themselves do not introduce a hidden scalar.
They give unit coordinate once the paired local blocks are literally obtained
from the same phase \( \Theta_\chi^{\mathrm{pair}}\) and the value coordinate
is declared to be \(q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\).

## What this proves for UV-017

Proved at the formal local-algebra level:

- literal substitution \(\Theta=\Theta_\chi^{\mathrm{pair}}\) and
  \(q=\Theta'\) gives \(da/dS=1\);
- derivative and curvature coordinates are frozen on the pure value path;
- the phase-gap variation is exactly \(-S\,s\), matching the RH
  value-channel rule.

This is stronger than the previous coefficient reduction: it proves the unit
coordinate for the universal finite-\(s\) phase-kernel model.

## What is still missing for the actual paired theorem

The current paired notes do not yet define the actual corrected paired blocks
\[
G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}(s),
\qquad
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
\]
by literal substitution into the RH finite-\(s\) formulas, nor do they state the
paired pure source path
\[
\Theta_{\chi,\alpha}^{\mathrm{pair}}(t)
=\Theta_{\chi,0}^{\mathrm{pair}}(t)+\alpha(t-m)
\]
as part of the local normal form.

Smallest missing construction statement:

> Paired finite-\(s\) unit-coordinate construction. After choosing the
> sign-audited boundary phase
> \(\Phi_\chi^{\mathrm{pair}}(1/2+it)=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)}\),
> the corrected paired same-point and mixed blocks are obtained from the RH
> finite-\(s\) block formulas by replacing \(\Ph\) with
> \(\Theta_\chi^{\mathrm{pair}}\), \(q\) with
> \(q_\chi^{\mathrm{pair}}=\Theta_\chi^{\mathrm{pair}\prime}\), and by using
> the local value coordinate
> \(a=q_\chi^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)\). The pure value
> path is
> \(q_{\chi,\alpha}^{\mathrm{pair}}(t)=q_{\chi,0}^{\mathrm{pair}}(t)+\alpha\)
> on the microscopic window, equivalently
> \(\Theta_{\chi,\alpha}^{\mathrm{pair}}(t)=
> \Theta_{\chi,0}^{\mathrm{pair}}(t)+\alpha(t-m)\), with all derivative,
> curvature, background, correction, multiplicity, and gauge coordinates
> frozen. Then \(da/dS|_0=1\).

Honest verdict: the unit-coordinate obstruction is closed for the universal
finite-\(s\) phase-kernel model, but not for the actual paired theorem until
the paired finite-\(s\) construction statement above is installed and followed
by the holomorphy/whitening, freeze-rule remainder, and scalar-readout checks.
