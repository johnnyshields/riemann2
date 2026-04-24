# D-min odd-block functional search

## Route A: source search

The paper already has a transform-level corrected odd scalar:
\[
H_m(s)=\Phi_K\!\bigl(\widehat\Omega_\zeta^{\corr}(s;m)\bigr).
\]
The corrected whitening theorem proves holomorphy of \(\widehat\Omega_\zeta^{\corr}\), and the odd expansion gives coefficients \(c_{2r+1}(m)\). The \(N\)-point layer then isolates the first surviving corrected odd coefficient.

For D-min, the two-package functional should therefore not be another cubic/quintic defect \(E_{12}^{(3)},E_{12}^{(5)}\). It should be the package-fiber difference of the same transform-level scalar:
\[
\mathscr H_{12}(t;s)
:=
\Phi_K\!\left(
\widehat\Omega^{\corr}_{\mathcal P_1(t)}(s)
-
\widehat\Omega^{\corr}_{\mathcal P_2(t)}(s)
\right),
\]
with odd coefficients
\[
\mathscr H_{12}(t;z/Q^2)
=
\sum_{r\ge0}\mathscr c_{2r+1}(t)\frac{z^{2r+1}}{Q^{2r+4}}.
\]
The first D-min-visible odd block is
\[
\mathscr O_D^{(N)}(t):=\mathscr c_{2N-1}(t)
=
\Phi_K\!\left([s^{2N-1}]
(\widehat\Omega^{\corr}_{\mathcal P_1(t)}-
 \widehat\Omega^{\corr}_{\mathcal P_2(t)})
\right)
\]
for the first surviving odd order. Equivalently, use the transformed version
\[
\mathscr X_D^{(N)}(t):=
\sum_{j=1}^N a_j^{(N)}\mathscr H_{12}(t;s_j),
\]
which has the same leading surviving coefficient by the exact odd-tail expansion.

## Route B: fixed-shear state-locality translation

The fixed-shear conditional proposition uses analytic functions
\[
E_{12}^{(3)}(t)=\mathfrak e_3(\mathcal T_N(t)),\qquad
E_{12}^{(5)}(t)=\mathfrak e_5(\mathcal T_N(t))
\]
with diagonal vanishing. Since \(\mathcal T_N(t)=\mathcal T_N(0)+O(t^2)\), the defects are \(O(t^2)\).

The analogous D-min hypothesis is:
\[
\mathscr O_D^{(N)}(t)=\mathfrak o_D(\mathcal T_M(t),L(t)),
\qquad
\mathfrak o_D(\mathcal T_M(0),L(0))=0,
\]
where \(L(t)\) is the normalized septic affine lift data, understood modulo \(\ker\Phi_K\). If \(L(t)\) descends/evenly transports with \(L(t)=L(0)+O(t^2)\), then \(\mathscr O_D^{(N)}(t)=O(t^2)\). If two corrected packages are in the same reduced-package fiber and the lift variation is killed modulo \(\ker\Phi_K\), this gives
\[
\Phi_K(\Delta\widehat\Omega^{\corr}(s))=O(s^{2N+1})
\]
through the first surviving odd order.

## Route C / minimal missing lemma

Corrected whitening analyticity is enough to show that \(\mathscr H_{12}\), \(\mathscr O_D^{(N)}\), and \(\mathscr X_D^{(N)}\) depend analytically on the corrected block perturbation triple \((\delta G_-,\delta N,\delta G_+)\). It is not enough to show state-locality in \(\mathcal T_M\), because the paper explicitly says the actual corrected two-pair defect/package is not yet proved to factor through the descended fixed-shear state.

Minimal missing lemma:

> Along corrected reduced-package fibers, the corrected block perturbation triple feeding \(\widehat\Omega^{\corr}\), after applying \(\Phi_K\) to the first surviving odd coefficient, factors through a finite descended transport state and the normalized septic affine lift; all remaining higher-order/lift variation is \(\ker\Phi_K\)-invisible through order \(2N-1\).

This is a transport/holonomy lemma for the affine lift bundle, not a septic algebra identity.
