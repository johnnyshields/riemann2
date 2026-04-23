# Benchmark Map

Compact map of what each benchmark currently demonstrates.

## Oscillator

Family:
- `psi_ω(x) = (ω/π)^{1/4} exp(-ω x^2 / 2)`

Role:
- reparameterization sanity check for the first-horizontal-jet block.

Main takeaway:
- raw first-jet matrices change under `ω <-> r = (1/2) log ω`,
- the bilaterally whitened first-jet block stays unchanged,
- but its singular values collapse to a function of overlap alone.

## Qutrit Polynomial

Family:
- `|psi(t)> = (1,t,t^2)^T / sqrt(1+t^2+t^4)`

Role:
- first positive benchmark where the surviving two-point data is richer than
  overlap alone.

Main takeaways:
- ambient `A_1` benchmark has explicit `Omega(u,v)` and equal-overlap witness,
- value-channel-free `O_1` also has an explicit equal-overlap witness,
- first-order richer-than-overlap behavior is not tied to the ambient state line.

## Quartit Cubic

Family:
- `|psi(t)> = (1,t,t^2,t^3)^T / sqrt(1+t^2+t^4+t^6)`

Role:
- higher-order benchmark where raw matrices fail but subspace geometry survives.

Main takeaways:
- ambient `A_2` has exact singular values `(1,1,sigma_3)`,
- value-channel-free `O_2` has an explicit `2x2` complement matrix,
- `O_2` is strictly finer than `A_2` at principal-angle level on this benchmark.

## Veronese Family

Family:
- `v_n(t) = (1,t,...,t^n)`

Role:
- benchmark-family unification of qutrit and quartit results.

Main takeaways:
- ambient order-`n-1` theorem: codimension-`1` hyperplane with normal from
  `(x-t)^n`,
- value-channel-free order-`n-1` theorem: explicit codimension-`2` complement
  matrix,
- richer-than-overlap behavior is systematic for all `n >= 2`.

## Spherical Twist

Family:
- `psi(t) = (cos t cos 2t, cos t sin 2t, sin t)`

Role:
- non-Veronese witness that the richer-than-overlap phenomenon is not confined
  to polynomial families.

Main takeaways:
- explicit equal-overlap / different-angle witness,
- works on both ambient `A_1` and value-channel-free `O_1` sides.
