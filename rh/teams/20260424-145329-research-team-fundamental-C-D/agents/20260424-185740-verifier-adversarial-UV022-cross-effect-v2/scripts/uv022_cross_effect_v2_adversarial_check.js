#!/usr/bin/env node

function key(exp) {
  return exp.join(",");
}

function parseKey(k) {
  return k.split(",").map(Number);
}

function constant(c) {
  return c === 0 ? new Map() : new Map([[key([0, 0, 0, 0, 0]), c]]);
}

function variable(i) {
  const exp = [0, 0, 0, 0, 0];
  exp[i] = 1;
  return new Map([[key(exp), 1]]);
}

function add(p, q) {
  const out = new Map(p);
  for (const [k, c] of q.entries()) {
    const next = (out.get(k) || 0) + c;
    if (next === 0) out.delete(k);
    else out.set(k, next);
  }
  return out;
}

function neg(p) {
  const out = new Map();
  for (const [k, c] of p.entries()) out.set(k, -c);
  return out;
}

function sub(p, q) {
  return add(p, neg(q));
}

function scale(c, p) {
  if (c === 0) return new Map();
  const out = new Map();
  for (const [k, coeff] of p.entries()) out.set(k, c * coeff);
  return out;
}

function mul(p, q) {
  const out = new Map();
  for (const [k1, c1] of p.entries()) {
    const e1 = parseKey(k1);
    for (const [k2, c2] of q.entries()) {
      const e2 = parseKey(k2);
      const exp = e1.map((e, i) => e + e2[i]);
      const k = key(exp);
      const next = (out.get(k) || 0) + c1 * c2;
      if (next === 0) out.delete(k);
      else out.set(k, next);
    }
  }
  return out;
}

function power(p, n) {
  let out = constant(1);
  for (let i = 0; i < n; i += 1) out = mul(out, p);
  return out;
}

function T(x) {
  return add(add(scale(3, x), scale(5, power(x, 2))), add(scale(7, power(x, 3)), scale(11, power(x, 4))));
}

function X(h) {
  return add(add(constant(2), h), scale(3, power(h, 2)));
}

function substituteZero(p, i) {
  const out = new Map();
  for (const [k, c] of p.entries()) {
    const exp = parseKey(k);
    if (exp[i] === 0) out.set(k, c);
  }
  return out;
}

function swapAtoms(p) {
  const out = new Map();
  for (const [k, c] of p.entries()) {
    const [e1, e2, em, ed, ek] = parseKey(k);
    const nextKey = key([e2, e1, em, ed, ek]);
    const nextCoeff = ed % 2 === 0 ? c : -c;
    out.set(nextKey, (out.get(nextKey) || 0) + nextCoeff);
    if (out.get(nextKey) === 0) out.delete(nextKey);
  }
  return out;
}

function termsBelowDelta2(p) {
  let count = 0;
  for (const k of p.keys()) {
    const exp = parseKey(k);
    if (exp[3] < 2) count += 1;
  }
  return count;
}

function sample(p, vals) {
  let total = 0;
  for (const [k, c] of p.entries()) {
    const exp = parseKey(k);
    let term = c;
    for (let i = 0; i < vals.length; i += 1) term *= vals[i] ** exp[i];
    total += term;
  }
  return total;
}

function scalarClose(name, got, expected, eps = 1e-10) {
  const diff = got - expected;
  if (Math.abs(diff) > eps) {
    throw new Error(`${name}: got ${got}, expected ${expected}, diff ${diff}`);
  }
  console.log(`${name} = ${diff}`);
}

function bool(name, value) {
  console.log(`${name} = ${value}`);
}

function det(x, y) {
  return x[0] * y[1] - x[1] * y[0];
}

function vectorScale(c, x) {
  return [c * x[0], c * x[1]];
}

function vectorAdd(x, y) {
  return [x[0] + y[0], x[1] + y[1]];
}

function quotientScalar(x, line) {
  if (line[0] === 0 && line[1] === 0) throw new Error("rank jump: zero A5 line");
  return det(x, line);
}

const a1 = variable(0);
const a2 = variable(1);
const m = variable(2);
const d = variable(3);
const kappa = variable(4);

const h1 = sub(m, d);
const h2 = add(m, d);
const x1 = X(h1);
const x2 = X(h2);
const xm = X(m);

const rawCross = sub(sub(T(add(mul(a1, x1), mul(a2, x2))), T(mul(a1, x1))), T(mul(a2, x2)));
const diagonalSelf = sub(sub(T(mul(add(a1, a2), xm)), T(mul(a1, xm))), T(mul(a2, xm)));
const renormalized = sub(rawCross, diagonalSelf);

bool("renorm_one_amplitude_left_zero", substituteZero(renormalized, 0).size === 0);
bool("renorm_one_amplitude_right_zero", substituteZero(renormalized, 1).size === 0);
bool("renorm_swap_difference_zero", sub(renormalized, swapAtoms(renormalized)).size === 0);
bool("raw_diagonal_zero", substituteZero(rawCross, 3).size === 0);
bool("renorm_diagonal_zero", substituteZero(renormalized, 3).size === 0);
bool("renorm_delta2_divisible", termsBelowDelta2(renormalized) === 0);
console.log(`renorm_terms_below_delta2 = ${termsBelowDelta2(renormalized)}`);
console.log(`renorm_sample_a1_2_a2_-3_m_5_d_7 = ${sample(renormalized, [2, -3, 5, 7, 0])}`);

function diagonalTerm(center) {
  return 23 + 29 * center;
}

function freeP(center, slope) {
  return 13 + 17 * center + 19 * slope;
}

function rawQ(leftAmp, rightAmp, center, sep, slope) {
  return leftAmp * rightAmp * (diagonalTerm(center) + sep ** 2 * freeP(center, slope));
}

const nA1 = 3;
const nA2 = -5;
const nM = 2;
const nDelta = 0.25;
const nKappa = 7;
const rawQValue = rawQ(nA1, nA2, nM, nDelta, nKappa);
const sourceHonestDiagonal = nA1 * nA2 * diagonalTerm(nM);
const correctedQ = rawQValue - sourceHonestDiagonal;
const correctedDiagonal = rawQ(nA1, nA2, nM, 0, nKappa) - sourceHonestDiagonal;

scalarClose("source_honest_counterterm_diagonal", correctedDiagonal, 0);
scalarClose("corrected_over_a1a2delta2", correctedQ / (nA1 * nA2 * nDelta ** 2), freeP(nM, nKappa));
console.log(`corrected_edge_value = ${correctedQ / (nA1 * nA2 * nDelta ** 2)}`);
bool("free_P_survives_source_honest_counterterm", correctedQ !== 0);

const unsourcedFullCountertermResidual = rawQValue - rawQValue;
scalarClose("unsourced_full_counterterm_residual", unsourcedFullCountertermResidual, 0);
bool("unsourced_full_counterterm_is_source_honest", false);

const A5 = [7, 11];
const qUnit = [2, 3];
const quotientValue = vectorScale(correctedQ, qUnit);
const shiftedRepresentative = vectorAdd(quotientValue, vectorScale(101, A5));

scalarClose(
  "determinant_chart_shift_difference",
  quotientScalar(shiftedRepresentative, A5),
  quotientScalar(quotientValue, A5),
);
scalarClose(
  "determinant_chart_free_edge",
  quotientScalar(quotientValue, A5) / (nA1 * nA2 * nDelta ** 2),
  det(qUnit, A5) * freeP(nM, nKappa),
);
console.log(`determinant_chart_free_edge_value = ${quotientScalar(quotientValue, A5) / (nA1 * nA2 * nDelta ** 2)}`);
bool("determinant_chart_kills_free_P", false);

try {
  quotientScalar(quotientValue, [0, 0]);
  bool("A5_zero_rank_jump_detected", false);
} catch (error) {
  bool("A5_zero_rank_jump_detected", true);
  console.log(`A5_zero_error = ${error.message}`);
}
