function det(R, A) {
  return R[0] * A[1] - A[0] * R[1];
}

function assertClose(name, got, expected, tolerance = 1e-10) {
  if (Math.abs(got - expected) > tolerance) {
    throw new Error(`${name}: got ${got}, expected ${expected}`);
  }
  console.log(`${name} = ${got}`);
}

const samples = [
  { u: 3, v: 5, ru: 7, rv: 11, xi: 13, c: 2, eps: 17, kappa: 19 },
  { u: -4, v: 9, ru: 6, rv: -8, xi: 5, c: -3, eps: 2, kappa: 7 },
  { u: 10, v: -6, ru: -1, rv: 4, xi: -2, c: 5, eps: -3, kappa: 11 },
];

for (const [index, s] of samples.entries()) {
  const A5 = [s.u, s.v];
  const R = [s.ru, s.rv];
  const base = det(R, A5);
  const shifted = det([s.ru + s.xi * s.u, s.rv + s.xi * s.v], A5);
  assertClose(`sample_${index}_gauge_shift_difference`, shifted - base, 0);

  const target = s.c ** 2 * s.eps * s.kappa;
  const RkUPatch = [0, -target / s.u];
  const RkVPatch = [target / s.v, 0];
  assertClose(`sample_${index}_Rk_u_patch_det`, det(RkUPatch, A5), target);
  assertClose(`sample_${index}_Rk_v_patch_det`, det(RkVPatch, A5), target);

  const kernelVector = [s.u, s.v];
  assertClose(`sample_${index}_kernel_span_det`, det(kernelVector, A5), 0);
}

const centered = { A: 23, B: -29, U1: 31, V1: -37, kappa: 41 };
const D2 = 2 * centered.kappa * (centered.A * centered.V1 - centered.B * centered.U1);
const dD2 = 2 * (centered.A * centered.V1 - centered.B * centered.U1);
console.log(`centered_D2 = ${D2}`);
console.log(`centered_dD2_dkappa = ${dD2}`);
console.log("symbolic_D2 = 2*kappa*(A*V1 - B*U1)");
console.log("symbolic_deformation_target = c^2*eps*kappa");
