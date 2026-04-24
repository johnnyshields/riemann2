function det(pair, a) {
  const [ru, rv] = pair;
  const [u, v] = a;
  return ru * v - u * rv;
}

function uPatchLift(scalar, a) {
  const [u] = a;
  if (u === 0) throw new Error("u-patch requires u != 0");
  return [0, -scalar / u];
}

function vPatchLift(scalar, a) {
  const [, v] = a;
  if (v === 0) throw new Error("v-patch requires v != 0");
  return [scalar / v, 0];
}

function subtract(x, y) {
  return [x[0] - y[0], x[1] - y[1]];
}

function isMultipleOfA(diff, a, eps = 1e-9) {
  const [du, dv] = diff;
  const [u, v] = a;
  return Math.abs(du * v - u * dv) < eps;
}

const samples = [
  { scalar: 17, a1: [2, 5], am: [3, -7], r1: [11, 1], xi: -4 },
  { scalar: -31, a1: [4, -3], am: [-5, 2], r1: [8, 1], xi: 6 },
];

for (const [idx, sample] of samples.entries()) {
  const s = det(sample.r1, sample.a1);
  const liftU = uPatchLift(s, sample.am);
  const liftV = vPatchLift(s, sample.am);
  const transition = subtract(liftV, liftU);
  const gauged = [
    sample.r1[0] + sample.xi * sample.a1[0],
    sample.r1[1] + sample.xi * sample.a1[1],
  ];

  console.log(`sample_${idx}_source_scalar = ${s}`);
  console.log(`sample_${idx}_midpoint_u_lift_scalar = ${det(liftU, sample.am)}`);
  console.log(`sample_${idx}_midpoint_v_lift_scalar = ${det(liftV, sample.am)}`);
  console.log(`sample_${idx}_patch_difference_is_gauge = ${isMultipleOfA(transition, sample.am)}`);
  console.log(`sample_${idx}_source_gauge_invariant = ${det(gauged, sample.a1) === s}`);
}

const exceptionalA = [0, 0];
console.log(`exceptional_determinant_map_rank = ${det([1, 0], exceptionalA) === 0 && det([0, 1], exceptionalA) === 0 ? 0 : 1}`);
console.log("exceptional_quotient_dimension_without_line_convention = 2");
