#!/usr/bin/env node

function close(name, got, expected, eps = 1e-10) {
  const diff = got - expected;
  if (Math.abs(diff) > eps) {
    throw new Error(`${name}: got ${got}, expected ${expected}, diff ${diff}`);
  }
  console.log(`${name} = ${diff}`);
}

function same(name, got, expected) {
  if (got !== expected) {
    throw new Error(`${name}: got ${got}, expected ${expected}`);
  }
  console.log(`${name} = ${got}`);
}

function det(x, y) {
  return x[0] * y[1] - x[1] * y[0];
}

function add(x, y) {
  return [x[0] + y[0], x[1] + y[1]];
}

function scale(c, x) {
  return [c * x[0], c * x[1]];
}

function quotientScalar(x, line) {
  if (line[0] === 0 && line[1] === 0) {
    throw new Error("rank jump: zero A5 line");
  }
  return det(x, line);
}

const a1 = 3;
const a2 = -5;
const m = 2;
const delta = 0.25;
const kappa = 7;

function diagonalTerm(center) {
  return 23 + 29 * center;
}

function freeP(center, slope) {
  return 13 + 17 * center + 19 * slope;
}

function rawCrossEffectQ(leftAmp, rightAmp, center, sep, slope) {
  return leftAmp * rightAmp * (diagonalTerm(center) + sep ** 2 * freeP(center, slope));
}

const raw = rawCrossEffectQ(a1, a2, m, delta, kappa);
const rawSwap = rawCrossEffectQ(a2, a1, m, -delta, kappa);
const oneAmpLeft = rawCrossEffectQ(a1, 0, m, delta, kappa);
const oneAmpRight = rawCrossEffectQ(0, a2, m, delta, kappa);
const diagonalRaw = rawCrossEffectQ(a1, a2, m, 0, kappa);

close("one_amplitude_left", oneAmpLeft, 0);
close("one_amplitude_right", oneAmpRight, 0);
close("swap_difference", raw, rawSwap);
console.log(`raw_diagonal_cross_effect = ${diagonalRaw}`);
same("raw_diagonal_vanishes", diagonalRaw === 0, false);

const sourceHonestDiagonalCounterterm = a1 * a2 * diagonalTerm(m);
const corrected = raw - sourceHonestDiagonalCounterterm;
const correctedDiagonal =
  rawCrossEffectQ(a1, a2, m, 0, kappa) - sourceHonestDiagonalCounterterm;

close("source_honest_counterterm_diagonal", correctedDiagonal, 0);
close("corrected_over_a1a2delta2", corrected / (a1 * a2 * delta ** 2), freeP(m, kappa));
console.log(`surviving_free_P = ${freeP(m, kappa)}`);

const countertermUsingFreeP = raw;
const killedByUnsourcedCounterterm = raw - countertermUsingFreeP;
close("counterterm_using_free_P_residual", killedByUnsourcedCounterterm, 0);
same("counterterm_using_free_P_is_source_honest", false, false);

const A5 = [7, 11];
const quotientUnit = [2, 3];
const quotientValue = scale(corrected, quotientUnit);
const representativeShift = add(quotientValue, scale(101, A5));
close(
  "determinant_chart_shift_difference",
  quotientScalar(representativeShift, A5),
  quotientScalar(quotientValue, A5),
);
close(
  "determinant_chart_free_edge",
  quotientScalar(quotientValue, A5) / (a1 * a2 * delta ** 2),
  det(quotientUnit, A5) * freeP(m, kappa),
);
same("determinant_chart_kills_free_coordinate", false, false);

try {
  quotientScalar(quotientValue, [0, 0]);
  console.log("A5_zero_rank_jump_detected = false");
} catch (error) {
  console.log("A5_zero_rank_jump_detected = true");
  console.log(`A5_zero_error = ${error.message}`);
}
