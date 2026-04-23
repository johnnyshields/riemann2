# A_val Transport Note

Date: 2026-04-23
Focused attack: `tasks/20260423-202340-attack-gap-aval-transport/`

## Main conclusion

The `A_val` transport statement is safe only as a first-order local statement.

Safe version:

- conditional on the same local symmetric normal form plus a family-level
  corrected whitening/decomposition theorem, the explicit `A_val` matrix and
  the formal annihilation `Phi_K(A_val)=0` transport.

## What this does not include

It does not automatically include:

- the full `Delta = S A_val + R` theorem in a new family;
- calibration via `Psi_{x,d}`;
- remainder dominance;
- odd/transverse consequences.

Those remain separate theorem burdens.

## Safe wording

`A_val transport is a first-order local algebra statement, not the whole
calibration chain.`

## Report refs

- `tasks/20260423-202340-attack-gap-aval-transport/reports/gap-aval-transport-routeA.md`
- `tasks/20260423-202340-attack-gap-aval-transport/reports/gap-aval-transport-routeB.md`
- `tasks/20260423-202340-attack-gap-aval-transport/reports/verifier-adversarial-aval-transport.md`
