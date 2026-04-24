# Paired Finite-\(s\) Formula Package

Date: 2026-04-24

## Candidate local chart formulas

Fix \(m\in I\) and set
\[
t_\pm=m\pm \frac{s}{2}.
\]
Use the sign-audited paired boundary phase
\[
\Phi_\chi^{\mathrm{pair}}\!\left(\tfrac12+it\right)
=e^{-2i\Theta_\chi^{\mathrm{pair}}(t)},
\qquad
q_\chi^{\mathrm{pair}}(t)
=\Theta_\chi^{\mathrm{pair}\,\prime}(t).
\]
Put
\[
q_{\chi,\pm}^{\mathrm{pair}}(s)
:=q_\chi^{\mathrm{pair}}(t_\pm),
\qquad
\Delta_{\chi,m}^{\mathrm{pair}}(s)
:=
\Theta_\chi^{\mathrm{pair}}(t_-)
-\Theta_\chi^{\mathrm{pair}}(t_+).
\]

The literal paired finite-\(s\) same-point chart is
\[
G_{\chi,m,\pm}^{\mathrm{pair},\mathrm{corr}}(s)
:=
\frac1\pi
\begin{pmatrix}
2q_{\chi,\pm}^{\mathrm{pair}}(s)
&
\frac12 q_\chi^{\mathrm{pair}\,\prime}(t_\pm)
\\[1ex]
\frac12 q_\chi^{\mathrm{pair}\,\prime}(t_\pm)
&
\frac1{12}
\left(
q_\chi^{\mathrm{pair}\,\prime\prime}(t_\pm)
+2q_{\chi,\pm}^{\mathrm{pair}}(s)^3
\right)
\end{pmatrix}.
\]

The literal paired finite-\(s\) mixed chart is
\[
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
:=
\frac1\pi
\begin{pmatrix}
-\dfrac{2\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)}{s}
&
\dfrac{
\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
+q_{\chi,+}^{\mathrm{pair}}(s)s
\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)
}{s^2}
\\[2ex]
-\dfrac{
\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
+q_{\chi,-}^{\mathrm{pair}}(s)s
\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)
}{s^2}
&
\dfrac{
\left(q_{\chi,-}^{\mathrm{pair}}(s)+q_{\chi,+}^{\mathrm{pair}}(s)\right)
s\cos \Delta_{\chi,m}^{\mathrm{pair}}(s)
+\left(2
-q_{\chi,-}^{\mathrm{pair}}(s)q_{\chi,+}^{\mathrm{pair}}(s)s^2
\right)
\sin \Delta_{\chi,m}^{\mathrm{pair}}(s)
}{2s^3}
\end{pmatrix}.
\]

When the same-point blocks are positive definite, the paired finite-\(s\)
whitened block is
\[
\widehat\Omega_{\chi}^{\mathrm{pair},\mathrm{corr}}(s;m)
:=
G_{\chi,m,-}^{\mathrm{pair},\mathrm{corr}}(s)^{-1/2}
N_{\chi,m}^{\mathrm{pair},\mathrm{corr}}(s)
G_{\chi,m,+}^{\mathrm{pair},\mathrm{corr}}(s)^{-1/2}.
\]

## Unit-coordinate path

Define the pure value path on the microscopic window by
\[
\Theta_{\chi,\alpha}^{\mathrm{pair}}(t)
=\Theta_{\chi,0}^{\mathrm{pair}}(t)+\alpha(t-m),
\qquad
q_{\chi,\alpha}^{\mathrm{pair}}(t)
=q_{\chi,0}^{\mathrm{pair}}(t)+\alpha.
\]
With
\[
S_{\chi,\alpha}^{\mathrm{pair}}(m)
:=
q_{\chi,\alpha}^{\mathrm{pair}}(m)
-B_\chi^{\mathrm{pair}}(m),
\]
and \(B_\chi^{\mathrm{pair}}(m)\) frozen, one has
\[
\frac{dS_{\chi,\alpha}^{\mathrm{pair}}(m)}{d\alpha}=1.
\]
If the baseline is chosen so that
\[
q_{\chi,0}^{\mathrm{pair}}(m)=B_\chi^{\mathrm{pair}}(m),
\]
then \(S_{\chi,\alpha}^{\mathrm{pair}}(m)=\alpha\). In any case, the coordinate
\[
a(\alpha)
:=q_{\chi,\alpha}^{\mathrm{pair}}(m)-B_\chi^{\mathrm{pair}}(m)
\]
satisfies
\[
\left.\frac{da}{dS_\chi^{\mathrm{pair}}}\right|_{\alpha=0}=1.
\]
Also
\[
\frac{\partial}{\partial\alpha}
q_{\chi,\alpha}^{\mathrm{pair}\,\prime}(t_\pm)=0,
\qquad
\frac{\partial}{\partial\alpha}
q_{\chi,\alpha}^{\mathrm{pair}\,\prime\prime}(t_\pm)=0,
\]
and
\[
\Theta_{\chi,\alpha}^{\mathrm{pair}}(t_-)
-\Theta_{\chi,\alpha}^{\mathrm{pair}}(t_+)
=
\Delta_{\chi,0}^{\mathrm{pair}}(s)-\alpha s.
\]

## Hypotheses still required

These formulas are a local chart package, not a proof that the paired
Dirichlet construction supplies this chart. Promotion still needs:

1. a construction or definition declaring these matrices to be the actual
   corrected paired local blocks;
2. microscopic holomorphy and removable singularity control for the paired
   phase on the \(s\)-disk;
3. same-point positivity/nondegeneracy and holomorphic inverse square roots;
4. a derivative-form freeze-rule remainder criterion;
5. a scalar-readout normalization check if the theorem exits the matrix level.

Smallest remaining obstruction: if "corrected" means something beyond literal
substitution into the RH finite-\(s\) formulas, the correction maps must be
named. Otherwise the display above can be adopted only as a definition or
explicit hypothesis.
