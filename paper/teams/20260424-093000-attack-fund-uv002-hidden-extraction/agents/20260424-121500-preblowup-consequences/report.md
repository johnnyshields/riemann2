# Report

## Claim

Assume the exact pre-blow-up diagonal theorem for the actual corrected two-atom package lands: on coincident atoms the corrected package has the one-pair diagonal value, equivalently the corrected cubic/quintic defects have the exact diagonal-collapse/merger value at coincidence. Then its immediate consequences split as follows.

1. Bottleneck B closes: on the residual exact fixed-shear involutive branch, the only live missing input is exactly this diagonal value-zero / merger statement, so the actual corrected cubic/quintic defects become swap-even with
   \[
   E_{12}^{(3)}(0)=E_{12}^{(5)}(0)=0,
   \]
   which is the missing package hypothesis for the existing exact fixed-shear closure route.
2. Bottleneck C becomes formal: the corrected reduced two-atom package has diagonal value at `\delta=0` independent of `\kappa` and equal to the one-pair reduced package,
   \[
   \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
   \]
   so the reduced-`\widehat\Psi` coincidence theorem follows from the existing strengthened coincidence algebra.
3. Bottleneck A is only partially closed: the pre-blow-up diagonal theorem gives the quadratic/projective factorization
   \[
   E_{12}^{(3)}=\delta^2\mathcal H_3(m,\kappa,\delta^2),\qquad
   E_{12}^{(5)}=\delta^2\mathcal H_5(m,\kappa,\delta^2),
   \]
   but by itself does not identify the edge traces
   \[
   \mathcal H_3(m,\kappa,0)=c'(m)-\frac{\kappa}{2}c(m),\qquad
   \mathcal H_5(m,\kappa,0)=(A_5^{\mathfrak f})'(m)-\frac{\kappa}{2}A_5^{\mathfrak f}(m).
   \]
   So it supplies the vanishing/factorization half of the good-patch edge-law theorem, not yet the full sharp edge-trace theorem.

## Status

heuristic

## Evidence

- The draft isolates diagonal merger as the exact sufficient source/package input for quadratic two-point factorization.
- The fixed-shear corner has already been compressed to a quotient-diagonal involutive branch with rank-one quotient-visible transport state and no further finite hidden reset; the live missing input there is diagonal coincidence/merger of the actual corrected package.
- The current team collation sharpens Bottleneck C to one exact statement: diagonal-collapse at `\delta=0`, independent of `\kappa`, matching the one-pair reduced package. Once that holds, reduced-`\widehat\Psi` coincidence is formal.
- The blow-up chart remark proves that any analytic swap-even corrected defect vanishing on the collision locus factors as `\delta^2` times an analytic function of `(m,\kappa,\delta^2)`. The sharper edge traces are additional data beyond mere diagonal vanishing.

## Exact refs

- `paper/proof_of_rh.tex:11888-12029` — diagonal merger implies quadratic factorization.
- `paper/proof_of_rh.tex:12447-12511` — blown-up edge-law factorization and the sharper edge-trace target.
- `paper/proof_of_rh.tex:12543-12555` — three live downstream two-point targets B/A/C split explicitly.
- `paper/proof_of_rh.tex:22302-22505` — quotient descent, rank-one transport, and the conditional fixed-shear closure/package-collapse route.
- `paper/proof_of_rh.tex:22579-22618` — what the quotient-transport package proves and what remains missing.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:24-55` — exact sharpening of B and C.
- `paper/tasks/20260424-090000-other-uv002-fundamental/notes/current-attack.md:70-115` — current Bottlenecks A, B, C.

## Dependencies

- The pre-blow-up diagonal theorem must apply to the actual corrected two-atom package, not only to the naive source-summed model.
- For Bottleneck C, one still uses the existing strengthened coincidence algebra after the diagonal value is identified.
- For Bottleneck A, additional work is still needed to compute the edge traces explicitly.

## Strongest objection

The phrase "pre-blow-up diagonal theorem" can hide two different strengths. If it proves only diagonal value-zero / merger at coincidence, then B closes and C becomes formal, but A gets only quadratic/projective factorization, not the specific edge traces needed to recover the detector `M/c` on the cubic-killing slope. So A is not fully closed by diagonal coincidence alone.

## Needed for promotion

1. State the pre-blow-up theorem in the exact package language: diagonal merger / diagonal-collapse for the actual corrected two-atom package.
2. For B, plug that theorem into the existing fixed-shear closure proposition/corollary and record the exact consequence.
3. For C, write the one-line deduction
   \[
   \widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)
   \]
   and cite the existing strengthened coincidence algebra.
4. For A, separate the already-forced quadratic/projective factorization from the still-missing edge-trace identities.

Honest verdict: assuming exact pre-blow-up diagonal merger for the actual corrected package, the immediate payoff is asymmetric: Bottleneck B closes, Bottleneck C becomes formal, and Bottleneck A is reduced to the sharper trace-identification step rather than fully solved.
