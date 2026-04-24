# Parity-Corrected Grade Verdict

Separate proved / conditional / missing.

## Proved From Source And Prior Audit

The common scalar mixed-order rule gives
\[
\operatorname{ord}_z(\delta G^{\lin}[r^{(k)}])=k-2
\]
because the same-point \((2,2)\) channel contains \(g=r''\).  Thus a single
scalar split \(r=\sum_a r^{[a]}\) with grade equal to first same-point
ordinary-\(z\) order has
\[
r^{[1]}\leftrightarrow r^{(3)}(m),
\qquad
r^{[5]}\leftrightarrow r^{(7)}(m).
\]

The exact mixed parity audit shows that the full source-linear mixed input has
\[
M(-z)=M(z)^T,
\]
and through order \(7\), \([z^5]M\) is off-diagonal antisymmetric and supported
only by
\[
r^{(2)}(m),\quad r^{(4)}(m),\quad r^{(6)}(m).
\]
These are scalar same-point grades \(0,2,4\), not \(5\).

## Tested Conventions

1. **Homogeneous common scalar grade.**  Define
\[
\operatorname{Gr}_a r =
\frac{r^{(a+2)}(m)}{(a+2)!}(t-m)^{a+2}.
\]
This is the cleanest convention compatible with a single scalar source split
and the same-point \(\Lambda^{[1]}\) input.  It gives
\([z^5]M^{[5]}=0\), so \(L_1YR_1\) is absent at \(B_7\).

2. **Actual mixed-order-5 projection.**  Define \(M^{[5]}\) to mean the
\([z^5]\) projection of the full mixed input.  This gives a nonzero middle
slot, but it uses \(r^{(2)},r^{(4)},r^{(6)}\), so it consumes source grades
\(0,2,4\).  It cannot be the same scalar grade convention as
\(\Lambda^{[1]}\).

3. **Parity-corrected non-homogeneous mixed projection.**  Define a separate
mixed-output projection \(\operatorname{Gr}_5^M\) that extracts the
\([z^5]\) off-diagonal combination.  This can coexist formally with
\(\Lambda^{[1]}\), but only as a block-dependent grading.  Current source does
not supply the theorem that prevents duplication or hidden use of grades
\(0,2,4\).

## Minimal Theorem If Homogeneous Grade Remains

Under the common homogeneous scalar grade
\[
\operatorname{Gr}_a r =
\frac{r^{(a+2)}(m)}{(a+2)!}(t-m)^{a+2},
\]
the \(L_1YR_1\) cubic family contributes no \(B_7^{\mathfrak f}\) term because
the middle factor \(M^{[5]}\) has no \([z^5]\) coefficient.  The next
Y-containing gate is \(L_2YR_0/L_0YR_2\), which uses the same mixed input
convention but with second-Frechet same-point factors.

## Missing For A Positive Parity-Corrected Definition

A positive nonzero \(M^{[5]}\) convention must be stated as a block-dependent
mixed-output projection, not as the current scalar source-grade split.  It must
prove that the \(r^{(2)},r^{(4)},r^{(6)}\) pieces are allowed in a label
\([5]\) without consuming or duplicating grade \(0,2,4\) sectors in the
same-point Frechet gates.
