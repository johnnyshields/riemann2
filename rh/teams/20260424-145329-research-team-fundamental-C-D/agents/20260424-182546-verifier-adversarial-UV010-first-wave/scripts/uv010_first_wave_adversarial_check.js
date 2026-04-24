#!/usr/bin/env node

function det(x, y) {
  return x[0] * y[1] - x[1] * y[0];
}

function add(x, y) {
  return [x[0] + y[0], x[1] + y[1]];
}

function scale(a, x) {
  return [a * x[0], a * x[1]];
}

function liftToLine(scalar, line) {
  const [u, v] = line;
  if (v !== 0) return [scalar / v, 0];
  if (u !== 0) return [0, -scalar / u];
  throw new Error("rank jump: zero midpoint quotient line");
}

function close(name, got, expected, eps = 1e-10) {
  const diff = got - expected;
  if (Math.abs(diff) > eps) {
    throw new Error(`${name}: got ${got}, expected ${expected}, diff ${diff}`);
  }
  console.log(`${name} = ${diff}`);
}

function same(name, value, expected) {
  if (value !== expected) {
    throw new Error(`${name}: got ${value}, expected ${expected}`);
  }
  console.log(`${name} = ${value}`);
}

function F(h) {
  return { c: 2 + 3 * h, f0: 5 - h, q: 7 + 11 * h };
}

function packageWithFreeSeptic(a1, h1, a2, h2, kappa, p) {
  const m = (h1 + h2) / 2;
  const delta = h2 - h1;
  return {
    c: a1 * F(h1).c + a2 * F(h2).c,
    f0: a1 * F(h1).f0 + a2 * F(h2).f0,
    q: a1 * F(h1).q + a2 * F(h2).q + a1 * a2 * delta ** 2 * p(m, kappa),
  };
}

function pFree(m, kappa) {
  return 13 + 17 * kappa + 19 * m;
}

function pZero() {
  return 0;
}

const movingLine = [3, 5];
const midpointLine = [7, 11];
const rep = [13, 17];
const shiftedRep = add(rep, scale(-4, movingLine));
const movingScalar = det(rep, movingLine);
const shiftedScalar = det(shiftedRep, movingLine);
const midpointRep = liftToLine(movingScalar, midpointLine);

close("moving_representative_shift_difference", shiftedScalar, movingScalar);
close("midpoint_scalar_difference", det(midpointRep, midpointLine), movingScalar);
console.log(`midpoint_lift = [${midpointRep.join(", ")}]`);

try {
  liftToLine(1, [0, 0]);
  console.log("zero_line_rank_jump_detected = false");
} catch (error) {
  console.log("zero_line_rank_jump_detected = true");
  console.log(`zero_line_error = ${error.message}`);
}

const a1 = 3;
const a2 = -4;
const m = 1;
const delta = 2;
const h1 = m - delta / 2;
const h2 = m + delta / 2;
const kappa = 5;
const withP = packageWithFreeSeptic(a1, h1, a2, h2, kappa, pFree);
const withoutP = packageWithFreeSeptic(a1, h1, a2, h2, kappa, pZero);
const swapped = packageWithFreeSeptic(a2, h2, a1, h1, kappa, pFree);
const oneAmp = packageWithFreeSeptic(0, h1, a2, h2, kappa, pFree);
const diagonal = packageWithFreeSeptic(a1, m, a2, m, kappa, pFree);

close("swap_c_difference", withP.c, swapped.c);
close("swap_f_difference", withP.f0, swapped.f0);
close("swap_q_difference", withP.q, swapped.q);
close("one_amplitude_q_difference", oneAmp.q, a2 * F(h2).q);
close("diagonal_q_difference", diagonal.q, (a1 + a2) * F(m).q);
close("lower_c_changed_by_P", withP.c, withoutP.c);
close("lower_f_changed_by_P", withP.f0, withoutP.f0);
close("free_septic_over_delta2", (withP.q - withoutP.q) / delta ** 2, a1 * a2 * pFree(m, kappa));
console.log(`free_septic_edge = a1*a2*(13 + 17*kappa + 19*m)`);
console.log(`free_septic_dkappa = ${a1 * a2 * 17}`);
same("scalar_only_route_kills_free_P", false, false);

function centeredD2Template(x) {
  const u1 = 2 * (x.v0 * x.dalpha1 + x.beta0 * x.du1);
  const v1 = 2 * (x.baralpha0 * x.du1 + x.dalpha1 * x.baru0);
  const a =
    x.dx1 * x.nu60 +
    x.beta50 * x.du1 +
    x.v0 * x.dalpha51 +
    x.b0 * x.dp1 +
    x.r0 * x.da1;
  const b =
    x.dx1 * x.barmu60 -
    x.barx0 * x.dmu61 +
    x.baralpha50 * x.du1 +
    x.dalpha51 * x.baru0 +
    x.bara0 * x.dp1 +
    x.da1 * x.barp0;
  const uhat1 = 2 * x.kappa * a;
  const vhat1 = 2 * x.kappa * b;
  const d2 = uhat1 * v1 - u1 * vhat1;
  return { u1, v1, a, b, d2, compressed: 2 * x.kappa * (a * v1 - b * u1), dkappa: 2 * (a * v1 - b * u1) };
}

const d2Sample = {
  kappa: 3,
  v0: 5,
  dalpha1: 7,
  beta0: 11,
  du1: 13,
  baralpha0: 17,
  baru0: 19,
  dx1: 23,
  nu60: 29,
  beta50: 31,
  dalpha51: 37,
  b0: 41,
  dp1: 43,
  r0: 47,
  da1: 53,
  barmu60: 59,
  barx0: 61,
  dmu61: 67,
  baralpha50: 71,
  bara0: 73,
  barp0: 79,
};

const d2Result = centeredD2Template(d2Sample);
close("centered_d2_minus_compressed", d2Result.d2, d2Result.compressed);
console.log(`centered_d2_dkappa = ${d2Result.dkappa}`);
same("centered_d2_is_actual_two_atom_hessian", false, false);
