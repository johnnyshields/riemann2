# Formal countermodel for C-FS3 under current axioms

## Purpose

Test route (A): construct an explicit formal model with fixed C codomain
\[
V_C=\mathbf C\times\mathfrak f\times\mathbf C,
\qquad \mathfrak f=\operatorname{span}\{I,S\},
\]
reduction
\[
\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2),
\]
current blow-up/symmetry/scalar-normalization properties, and nonconstant exceptional trace \(B(m,\kappa)\).

This is a formal adversarial model, not a claim about the actual corrected formulas.

## Model

Fix one-pair base functions \(c(m)\neq0\), \(Y(m)=u_5(m)/c(m)\), \(X(m)=v_5(m)/c(m)\), and \(Z(m)=\Delta_7(m)/c(m)^2\). Work in the collision blow-up chart
\[
2\omega=\kappa\delta,
\qquad t=\delta^2.
\]
Under the swap action \((\omega,\delta)\mapsto(-\omega,-\delta)\), both \(\kappa\) and \(t\) are invariant.

Define a fixed-codomain package germ
\[
\mathfrak P_{\mathrm{toy}}(m,\kappa,t)
=
\bigl(C,UI+VS,\Delta\bigr)
\]
by
\[
C=c(m),
\qquad U=c(m)Y(m),
\qquad V=c(m)X(m),
\]
and
\[
\Delta=c(m)^2\bigl(Z(m)+\varepsilon \kappa+tR(m,\kappa,t)\bigr),
\]
where \(\varepsilon\neq0\) is a scalar and \(R\) is any analytic germ.

Then
\[
\mathcal R(\mathfrak P_{\mathrm{toy}})
=
\bigl(Y(m),X(m),Z(m)+\varepsilon\kappa+tR(m,\kappa,t)\bigr).
\]
So the exceptional-divisor trace is
\[
B(m,\kappa)=\bigl(Y(m),X(m),Z(m)+\varepsilon\kappa\bigr),
\]
which is nonconstant in \(\kappa\).

## Properties checked

1. Fixed codomain: yes, \(\mathfrak P_{\mathrm{toy}}\in\mathbf C\times\mathfrak f\times\mathbf C\).
2. Reduction map: exactly \(\mathcal R(C,UI+VS,\Delta)=(U/C,V/C,\Delta/C^2)\).
3. Scalar normalization: the third coordinate scales quadratically with \(C\), matching the \(\widehat\Psi\) scaling convention.
4. Blow-up analyticity: analytic in \((m,\kappa,t)\), where \(t=\delta^2\).
5. Swap-evenness in the blown-up chart: since \(\kappa=2\omega/\delta\) and \(t=\delta^2\) are invariant under \((\omega,
\delta)\mapsto(-\omega,-\delta)\), the model is swap-invariant.
6. Diagonal identification at the central slope: \(B(m,0)=\widehat\Psi(m)\) if \(Z(m)=\Delta_7(m)/c(m)^2\).
7. C-FS3 failure: \(\partial_\kappa B_3=\varepsilon\neq0\), so no \(\kappa\)-independence.

Script check: `scripts/formal_countermodel.py` outputs

```text
R = (Y, X, Z + eps*kappa + r*t)
B = (Y, X, Z + eps*kappa)
swap_invariant = True
dB3/dkappa = eps
B_at_kappa_0 = (Y, X, Z)
```

## Consequence

C-FS3 cannot be derived from the currently audited formal properties:

- fixed C codomain;
- reduction \(\mathcal R\);
- scalar normalization / homogeneous degrees \((1,1,2)\);
- analytic extension after \(2\omega=\kappa\delta\);
- swap-evenness in the blow-up chart;
- identification with \(\widehat\Psi\) at one chosen slope.

A genuine diagonal-merger / collision-functoriality theorem is required to exclude the \(\varepsilon\kappa\) term. This formal model also shows why C-FS2 and C-FS3 should be separated: the model has no extra codomain coordinate beyond \((C,A^{\mathfrak f},\Delta)\), but C-FS3 still fails.

## Scope of the countermodel

This countermodel does not inspect the actual corrected two-atom formulas and does not prove such a \(\kappa\)-term occurs. It proves only a scoped negative:

> From the listed formal C-codomain, blow-up, swap, and scalar-normalization properties alone, slope independence of \(B(m,\kappa)\) is not forced.

Thus any promotion of C must cite an actual package-level merger/functoriality identity, not these formal properties.
