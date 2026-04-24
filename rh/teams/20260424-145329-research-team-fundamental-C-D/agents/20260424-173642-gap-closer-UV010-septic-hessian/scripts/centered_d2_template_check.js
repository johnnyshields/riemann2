// Check the centered septic determinant template from proof_of_rh.tex
// lines 23312--23403.  This is a formal coefficient check, not an
// actual two-atom corrected-package Hessian computation.

function paperTemplate(x) {
  const U1 = 2 * (x.v0 * x.dalpha1 + x.beta0 * x.du1);
  const V1 = 2 * (x.baralpha0 * x.du1 + x.dalpha1 * x.baru0);
  const A =
    x.dx1 * x.nu60 +
    x.beta50 * x.du1 +
    x.v0 * x.dalpha51 +
    x.b0 * x.dp1 +
    x.r0 * x.da1;
  const B =
    x.dx1 * x.barmu60 -
    x.barx0 * x.dmu61 +
    x.baralpha50 * x.du1 +
    x.dalpha51 * x.baru0 +
    x.bara0 * x.dp1 +
    x.da1 * x.barp0;
  const Uhat1 = 2 * x.kappa * A;
  const Vhat1 = 2 * x.kappa * B;
  const D2 = Uhat1 * V1 - U1 * Vhat1;
  const compressed = 2 * x.kappa * (A * V1 - B * U1);
  const dD2dkappa = 2 * (A * V1 - B * U1);
  return { U1, V1, A, B, Uhat1, Vhat1, D2, compressed, dD2dkappa };
}

const sample = {
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

const result = paperTemplate(sample);
console.log("U1 =", result.U1);
console.log("V1 =", result.V1);
console.log("A =", result.A);
console.log("B =", result.B);
console.log("D2 =", result.D2);
console.log("compressed_D2 =", result.compressed);
console.log("D2_minus_compressed =", result.D2 - result.compressed);
console.log("dD2_dkappa =", result.dD2dkappa);
console.log("nonzero_channel =", result.dD2dkappa !== 0);
