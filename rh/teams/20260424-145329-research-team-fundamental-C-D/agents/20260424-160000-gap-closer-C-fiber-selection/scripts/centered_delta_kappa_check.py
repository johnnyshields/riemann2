#!/usr/bin/env python3
"""Check kappa-linear freedom in the paper's centered septic determinant template.

This script encodes the coefficient identities from proof_of_rh.tex:23337-23408:
  Delta_7(s)=D_2 s^2 + ...,
  D_2 = Uhat_1 V_1 - U_1 Vhat_1,
where Uhat_1 and Vhat_1 are kappa times independent centered transport-channel
linear forms. It checks that D_2 is generically kappa-linear, so the displayed
order-7 template does not itself forbid a c^2 * eps * kappa deformation of the
third C-coordinate.
"""

import sympy as sp

kappa = sp.symbols("kappa")
U1, V1 = sp.symbols("U1 V1")
# Two independent channel linear forms standing for the bracketed expressions
# in proof_of_rh.tex:23345-23365.
A, B = sp.symbols("A B")

Uhat1 = 2 * kappa * A
Vhat1 = 2 * kappa * B
D2 = sp.expand(Uhat1 * V1 - U1 * Vhat1)

print("D2 =", D2)
print("dD2/dkappa =", sp.diff(D2, kappa))
print("generic_nonzero_condition =", sp.factor(sp.diff(D2, kappa)))
print("example_value =", D2.subs({A: 1, B: 0, U1: 0, V1: 1, kappa: sp.Symbol('k')}))
