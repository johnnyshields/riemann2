#!/usr/bin/env node

// Analytic-transfer cross-effect harness.
// If T has a homogeneous expansion T1 + T2 + T3 + ..., then
// I(a1 x1, a2 x2) = T(a1 x1 + a2 x2) - T(a1 x1) - T(a2 x2)
// automatically vanishes on one-amplitude inputs and begins with a1*a2.

function T(a, b) {
  const t1 = 2 * a + 3 * b;
  const t2 = 5 * a * a + 7 * a * b + 11 * b * b;
  const t3 = 13 * a * a * b + 17 * a * b * b;
  return t1 + t2 + t3;
}

function add(x, y) {
  return [x[0] + y[0], x[1] + y[1]];
}

function scale(c, x) {
  return [c * x[0], c * x[1]];
}

function evalT(x) {
  return T(x[0], x[1]);
}

const x1 = [2, 5];
const x2 = [7, 11];
const a1 = 3;
const a2 = -4;

function cross(a1Value, a2Value) {
  const y1 = scale(a1Value, x1);
  const y2 = scale(a2Value, x2);
  return evalT(add(y1, y2)) - evalT(y1) - evalT(y2);
}

const interaction = cross(a1, a2);
const oneAmpLeft = cross(a1, 0);
const oneAmpRight = cross(0, a2);
const swapped = (() => {
  const oldX1 = x1.slice();
  const oldX2 = x2.slice();
  const y1 = scale(a2, oldX2);
  const y2 = scale(a1, oldX1);
  return evalT(add(y1, y2)) - evalT(y1) - evalT(y2);
})();

console.log(`one_amplitude_left = ${oneAmpLeft}`);
console.log(`one_amplitude_right = ${oneAmpRight}`);
console.log(`swap_difference = ${interaction - swapped}`);
console.log(`interaction = ${interaction}`);
console.log(`interaction_over_a1a2 = ${interaction / (a1 * a2)}`);
console.log(`has_a1a2_factor = ${Number.isFinite(interaction / (a1 * a2))}`);

// Diagonal/collision vanishing is not automatic. If x1=x2, the cross-effect
// still has a quadratic self-pair term unless an additional merger/renormalizing
// theorem kills it.
const x = [2, 5];
const diagInteraction =
  evalT(add(scale(a1, x), scale(a2, x))) -
  evalT(scale(a1, x)) -
  evalT(scale(a2, x));
console.log(`diagonal_cross_effect = ${diagInteraction}`);
console.log(`diagonal_cross_effect_over_a1a2 = ${diagInteraction / (a1 * a2)}`);
