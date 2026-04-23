## Claim

With the theorem statement fixed as
\[
\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m),
\]
the minimal proof-obligation split for Bottleneck C is:

1. construct the actual corrected reduced two-atom package germ on the collision/cancellation blow-up chart and show it extends analytically to the exceptional divisor after writing \(2\omega=\kappa\delta\);
2. prove the formal symmetry input already expected by the draft, namely swap-evenness in \((m,\omega,\delta)\), so the diagonal trace is a well-defined exceptional-divisor function \(B(m,\kappa):=\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)\);
3. prove the only substantive new theorem: canonical diagonal specialization / collision-functoriality, equivalently
\[
B(m,\kappa)=\widehat\Psi(m)
\quad\text{for all small }\kappa.
\]

After (1) and (2), the rest of C is exactly the elimination of the free exceptional-divisor term \(B(m,\kappa)\). No further independent local obstruction remains on the present draft.

## Status

heuristic

## Evidence

- The draft already identifies the honest package target as a provenance-sensitive statement such as same reduced image germ at coincidence or collision-functoriality, not raw septic equality.
- The draft's abstract two-point lemmas show the general pattern: once a two-atom package is well-defined on the diagonal and the correct collapse identity is known, exclusion/coincidence consequences become formal.
- Current team collation sharpens Bottleneck C to the exact statement \(\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)\) and says explicitly that analyticity/swap-evenness alone still leave a free analytic trace \(B(m,\kappa)\).
- Therefore the fixed theorem C does not split into multiple deep subtheorems. It splits into setup/definition obligations plus one genuine package theorem: diagonal specialization to the one-pair datum.

## Exact refs

- `paper/proof_of_rh.tex:10780-10810` — honest order-7 target is same reduced image germ / collision-functoriality.
- `paper/proof_of_rh.tex:11368-11450` — definition and role of `\widehat\Psi`.
- `paper/proof_of_rh.tex:11888-11932` — abstract three-identity lemma showing collapse becomes formal once diagonal data are fixed.
- `paper/proof_of_rh.tex:12042-12137` — weaker quotient-diagonal route from continuity plus diagonal collapse.
- `paper/proof_of_rh.tex:12139-12166` — continuity and diagonal-collapse problem isolated as the weaker exact route.
- `paper/proof_of_rh.tex:12168-12184` — source-level version isolates swap symmetry, one-amplitude collapse, diagonal merger.
- `paper/proof_of_rh.tex:12586-12610` — finite-core endgame first needs coincidence information for `\widehat\Psi`.
- `paper/proof_of_rh.tex:24985-25030` — endgame summary: live target is package-level coincidence/functoriality.
- `paper/teams/20260424-093000-attack-fund-uv002-hidden-extraction/collation.md:50-72` — current exact form of Bottleneck C and explicit free term `B(m,\kappa)`.

## Dependencies

- A precise definition of the actual corrected reduced package `\widetilde\Psi^{\corr}_{\mathrm{red}}` on the collision/cancellation blow-up chart.
- Analytic extension/continuity to `\delta=0` under the convention `2\omega=\kappa\delta`.
- Swap symmetry of the corrected package germ under atom exchange.
- One-pair datum `\widehat\Psi(m)` already fixed.

## Strongest objection

Step (1) may itself conceal nontrivial package choices: if the corrected reduced package is not canonically defined before passing to the exceptional divisor, then the line between "setup" and "theorem" is less sharp than stated here. In that case the real blocker is earlier: well-definedness of `\widetilde\Psi^{\corr}_{\mathrm{red}}`, not only the identity `B(m,\kappa)=\widehat\Psi(m)`.

## Needed for promotion

1. State the exact definition of `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,\delta)` in the blow-up chart.
2. Verify analytic extension to `\delta=0` and swap-evenness.
3. Prove canonical diagonal specialization / collision-functoriality:
   `\widetilde\Psi^{\corr}_{\mathrm{red}}(m,\kappa,0)=\widehat\Psi(m)`.
4. Then record that Bottleneck C is closed and Bottleneck D is the remaining substantive theorem front.

Honest verdict: Bottleneck C is now reduced to one real theorem after the convention/regularity setup is fixed. The only genuinely non-formal obligation is to kill the free exceptional-divisor trace by proving diagonal specialization of the corrected reduced package to the one-pair datum `\widehat\Psi(m)`.
