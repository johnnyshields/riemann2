function det(x, y) {
  return x[0] * y[1] - x[1] * y[0];
}

function add(x, y) {
  return [x[0] + y[0], x[1] + y[1]];
}

function scale(a, x) {
  return [a * x[0], a * x[1]];
}

function midpointClassScalar(rep, movingLine) {
  return det(rep, movingLine);
}

function inverseMidpointRepresentative(scalar, midpointLine) {
  const [u, v] = midpointLine;
  if (v !== 0) {
    return [scalar / v, 0];
  }
  if (u !== 0) {
    return [0, -scalar / u];
  }
  throw new Error("midpoint line is zero: quotient rank jumps");
}

const movingLine = [3, 5];
const midpointLine = [7, 11];
const representative = [13, 17];
const gaugeShift = -4;
const shiftedRepresentative = add(representative, scale(gaugeShift, movingLine));

const scalar = midpointClassScalar(representative, movingLine);
const shiftedScalar = midpointClassScalar(shiftedRepresentative, movingLine);
const targetRepresentative = inverseMidpointRepresentative(scalar, midpointLine);

console.log(`det_rep_moving = ${scalar}`);
console.log(`det_shifted_rep_moving = ${shiftedScalar}`);
console.log(`representative_independent = ${scalar === shiftedScalar}`);
console.log(`target_rep = [${targetRepresentative.join(", ")}]`);
console.log(`det_target_midpoint = ${det(targetRepresentative, midpointLine)}`);

try {
  inverseMidpointRepresentative(1, [0, 0]);
  console.log("zero_midpoint_line_error = false");
} catch (error) {
  console.log("zero_midpoint_line_error = true");
  console.log(`zero_midpoint_line_message = ${error.message}`);
}
