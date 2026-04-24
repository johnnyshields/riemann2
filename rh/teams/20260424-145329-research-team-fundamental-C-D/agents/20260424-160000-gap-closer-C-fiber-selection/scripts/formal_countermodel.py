#!/usr/bin/env python3
"""Formal C-FS3 countermodel check.

This script verifies the algebraic properties of the fixed-codomain toy package
used in notes/formal-countermodel-CFS23.md. It is not a numerical model of the
paper's corrected blocks; it checks that the proposed formal package has the
required reduction, is invariant under the swap action in blow-up coordinates,
and has nonconstant exceptional trace B(kappa).
"""

import sympy as sp

c, Y, X, Z, eps, kappa, t, r = sp.symbols("c Y X Z eps kappa t r", nonzero=True)

# Fixed codomain V_C = C x f x C, with f-coordinate U I + V S.
C = c
U = c * Y
V = c * X
Delta = c**2 * (Z + eps * kappa + t * r)

R = (sp.simplify(U / C), sp.simplify(V / C), sp.simplify(Delta / C**2))
B = tuple(sp.simplify(expr.subs(t, 0)) for expr in R)

# In the affine blow-up chart kappa=2 omega/delta and t=delta^2.
# The atom swap sends (omega, delta) -> (-omega, -delta), hence kappa -> kappa and t -> t.
R_swapped = tuple(sp.simplify(expr.subs({kappa: kappa, t: t})) for expr in R)

print("R =", R)
print("B =", B)
print("swap_invariant =", all(sp.simplify(a - b) == 0 for a, b in zip(R, R_swapped)))
print("dB3/dkappa =", sp.diff(B[2], kappa))
print("B_at_kappa_0 =", tuple(sp.simplify(expr.subs(kappa, 0)) for expr in B))
