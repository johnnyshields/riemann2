#!/usr/bin/env node

// Toy harness for the source-weight obstruction at proof_of_rh.tex:12192-12227.
// Raw corrected blocks have the form a * G(a^2). Whitening cancels the overall
// a and leaves an even function of a. A signed lift a*W(a) restores oddness but
// not exact one-amplitude linearity unless all higher even coefficients vanish.

function polyEven(a, coeffs) {
  return coeffs[0] + coeffs[1] * a ** 2 + coeffs[2] * a ** 4;
}

function rawBlock(a, coeffs) {
  return a * polyEven(a, coeffs);
}

function whitened(a, coeffs) {
  if (a === 0) return coeffs[0];
  return rawBlock(a, coeffs) / a;
}

function signedLift(a, coeffs) {
  return a * whitened(a, coeffs);
}

function linearProjection(a, coeffs) {
  return a * coeffs[0];
}

const coeffs = [7, 11, 13];
const a = 3;
const minusA = -a;

const wA = whitened(a, coeffs);
const wMinusA = whitened(minusA, coeffs);
const liftA = signedLift(a, coeffs);
const liftMinusA = signedLift(minusA, coeffs);
const linearA = linearProjection(a, coeffs);

console.log(`whitened_even_difference = ${wA - wMinusA}`);
console.log(`whitened_one_amplitude_error = ${wA - linearA}`);
console.log(`signed_lift_odd_sum = ${liftA + liftMinusA}`);
console.log(`signed_lift_one_amplitude_error = ${liftA - linearA}`);
console.log(`linear_projection_one_amplitude_error = ${linearA - a * coeffs[0]}`);
console.log(`higher_source_weight_terms = ${coeffs[1] * a ** 3 + coeffs[2] * a ** 5}`);
