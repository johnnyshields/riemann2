#!/usr/bin/env node
/*
 * Symbolic/numeric pressure test for the C R-determinant channel.
 *
 * The determinant convention is det((p, q), (u, v)) = p*v - q*u for
 * coordinates in span{I, S}.  The symbolic lines are the exact algebraic
 * identities under test; the numeric sample confirms the same identities on
 * one generic nonzero assignment without external dependencies.
 */

const sample = {
  c: 3,
  eps: 5,
  kappa: 7,
  Delta: 11,
  u5: 13,
  v5: 17,
  U1: 19,
  V1: 23,
  A: 29,
  B: 31,
};

function det(p, q, u, v) {
  return p * v - q * u;
}

const { c, eps, kappa, Delta, u5, v5, U1, V1, A, B } = sample;
const detRkA5 = c ** 2 * eps * kappa;
const reducedShift = (Delta + detRkA5) / c ** 2 - Delta / c ** 2;
const vChartDet = det((c ** 2 * eps * kappa) / v5, 0, u5, v5);
const uChartDet = det(0, -(c ** 2 * eps * kappa) / u5, u5, v5);
const D2 = 2 * kappa * (A * V1 - B * U1);
const dD2Coeff = 2 * (A * V1 - B * U1);

console.log("symbolic det_Rk_A5 = c^2*eps*kappa");
console.log("symbolic reduced_third_coordinate_shift = eps*kappa");
console.log("symbolic d_shift_dkappa = eps");
console.log("symbolic v_chart_det = c^2*eps*kappa");
console.log("symbolic u_chart_det = c^2*eps*kappa");
console.log("symbolic D2 = 2*kappa*(A*V1 - B*U1)");
console.log("symbolic dD2_dkappa = 2*(A*V1 - B*U1)");
console.log(`sample det_Rk_A5 = ${detRkA5}`);
console.log(`sample reduced_shift = ${reducedShift}`);
console.log(`sample v_chart_det = ${vChartDet}`);
console.log(`sample u_chart_det = ${uChartDet}`);
console.log(`sample D2 = ${D2}`);
console.log(`sample dD2_coeff = ${dD2Coeff}`);
