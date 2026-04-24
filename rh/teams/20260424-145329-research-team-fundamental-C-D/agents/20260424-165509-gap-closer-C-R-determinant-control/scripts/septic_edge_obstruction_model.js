function F(h) {
  return {
    c: 2 + 3 * h,
    a: 5 - h,
    q: 7 + 11 * h,
  };
}

function add(x, y) {
  return { c: x.c + y.c, a: x.a + y.a, q: x.q + y.q };
}

function scale(s, x) {
  return { c: s * x.c, a: s * x.a, q: s * x.q };
}

function obstruction(m, kappa) {
  return 13 + 17 * kappa + 19 * m;
}

function packageP(a1, h1, a2, h2, kappa) {
  const m = (h1 + h2) / 2;
  const delta = h2 - h1;
  const linear = add(scale(a1, F(h1)), scale(a2, F(h2)));
  const septicInteraction = a1 * a2 * delta ** 2 * obstruction(m, kappa);
  return add(linear, { c: 0, a: 0, q: septicInteraction });
}

function assertClose(name, got, expected, tolerance = 1e-10) {
  if (Math.abs(got - expected) > tolerance) {
    throw new Error(`${name}: got ${got}, expected ${expected}`);
  }
  console.log(`${name} = ${got}`);
}

const a1 = 3;
const a2 = -4;
const m = 0.25;
const delta = 0.01;
const h1 = m - delta / 2;
const h2 = m + delta / 2;
const kappa = 2.5;

const P = packageP(a1, h1, a2, h2, kappa);
const Pswap = packageP(a2, h2, a1, h1, kappa);
assertClose("swap_c_difference", P.c - Pswap.c, 0);
assertClose("swap_a_difference", P.a - Pswap.a, 0);
assertClose("swap_q_difference", P.q - Pswap.q, 0);

const oneAmp1 = packageP(0, h1, a2, h2, kappa);
assertClose("one_amplitude_c", oneAmp1.c, a2 * F(h2).c);
assertClose("one_amplitude_a", oneAmp1.a, a2 * F(h2).a);
assertClose("one_amplitude_q", oneAmp1.q, a2 * F(h2).q);

const diag = packageP(a1, m, a2, m, kappa);
assertClose("diagonal_c", diag.c, (a1 + a2) * F(m).c);
assertClose("diagonal_a", diag.a, (a1 + a2) * F(m).a);
assertClose("diagonal_q", diag.q, (a1 + a2) * F(m).q);

const linear = add(scale(a1, F(h1)), scale(a2, F(h2)));
const interaction = P.q - linear.q;
assertClose(
  "septic_interaction_over_delta2",
  interaction / delta ** 2,
  a1 * a2 * obstruction(m, kappa),
);
console.log(`edge_obstruction = a1*a2*(13 + 17*kappa + 19*m)`);
console.log(`d_edge_obstruction_dkappa = ${a1 * a2 * 17}`);
