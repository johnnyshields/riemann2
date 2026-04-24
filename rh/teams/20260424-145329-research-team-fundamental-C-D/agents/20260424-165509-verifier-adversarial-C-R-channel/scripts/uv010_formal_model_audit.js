#!/usr/bin/env node
/*
 * Formal UV-010 pressure test.
 *
 * Model:
 *   P2 = a1 F(h1) + a2 F(h2) + a1*a2*delta^2*(0,0,P(m,kappa)).
 *
 * This tests whether swap symmetry, one-amplitude collapse, diagonal merger,
 * and fixed lower cubic/quintic edge data force the order-7 quotient edge term.
 */

function F(h) {
  return { c: 2 + 3 * h, f: 5 - h, q: 7 + 11 * h };
}

function add(x, y) {
  return { c: x.c + y.c, f: x.f + y.f, q: x.q + y.q };
}

function scale(s, x) {
  return { c: s * x.c, f: s * x.f, q: s * x.q };
}

function Pfree(m, kappa) {
  return 13 + 17 * kappa + 19 * m;
}

function P2(a1, h1, a2, h2, kappa) {
  const m = (h1 + h2) / 2;
  const delta = h2 - h1;
  const linear = add(scale(a1, F(h1)), scale(a2, F(h2)));
  const septic = a1 * a2 * delta ** 2 * Pfree(m, kappa);
  return add(linear, { c: 0, f: 0, q: septic });
}

function close(name, got, expected, tolerance = 1e-10) {
  const diff = got - expected;
  if (Math.abs(diff) > tolerance) {
    throw new Error(`${name}: got ${got}, expected ${expected}`);
  }
  console.log(`${name} = ${diff}`);
}

const a1 = 3;
const a2 = -4;
const m = 1;
const delta = 2;
const h1 = m - delta / 2;
const h2 = m + delta / 2;
const kappa = 5;

const base = P2(a1, h1, a2, h2, kappa);
const swap = P2(a2, h2, a1, h1, kappa);
close("swap_c_difference", base.c, swap.c);
close("swap_f_difference", base.f, swap.f);
close("swap_q_difference", base.q, swap.q);

const amp1Zero = P2(0, h1, a2, h2, kappa);
close("one_amplitude_c_difference", amp1Zero.c, a2 * F(h2).c);
close("one_amplitude_f_difference", amp1Zero.f, a2 * F(h2).f);
close("one_amplitude_q_difference", amp1Zero.q, a2 * F(h2).q);

const diag = P2(a1, m, a2, m, kappa);
close("diagonal_c_difference", diag.c, (a1 + a2) * F(m).c);
close("diagonal_f_difference", diag.f, (a1 + a2) * F(m).f);
close("diagonal_q_difference", diag.q, (a1 + a2) * F(m).q);

const linear = add(scale(a1, F(h1)), scale(a2, F(h2)));
const interactionEdge = (base.q - linear.q) / delta ** 2;
close("edge_over_delta2_difference", interactionEdge, a1 * a2 * Pfree(m, kappa), 1e-8);

console.log("lower_components_changed_by_P = false");
console.log("edge_term = a1*a2*(13 + 17*kappa + 19*m)");
console.log(`d_edge_term_dkappa = ${a1 * a2 * 17}`);
