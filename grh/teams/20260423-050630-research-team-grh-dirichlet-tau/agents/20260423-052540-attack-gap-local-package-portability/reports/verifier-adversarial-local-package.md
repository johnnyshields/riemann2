# Claim

The proposed source-light local theorem is too strong as a family-agnostic theorem. The strongest theorem actually supported by the cited draft regions is a two-layer statement:

1. an abstract odd-germ/projector theorem: once a real odd holomorphic transverse scalar with the stated microscopic holomorphy and boundary control exists, the odd expansion and the discrete \(N\)-point odd-moment projector follow;
2. a separate calibration interface: once a real value-channel derivative, a real sign-compatible calibration amplitude, and a nonzero toy pairing are realized, one gets the formal comparison \(u^2\asymp (x/B)S(m)\) after the remainder is small.

What is not supported by the cited draft regions is the stronger portability claim that the current manuscript already furnishes a source-light local theorem for completed \(L\)-function families from those hypotheses alone. The theorem should stop before the current calibration comparison unless calibration is explicitly presented as a conditional layer with its own realization hypotheses.

# Status

rejected

# Evidence

proved

- `paper/proof_of_rh.tex:145-269` gives a genuine phase-level local kernel / jet / whitening setup. This part is abstract local algebra.
- `paper/proof_of_rh.tex:426-794` gives an explicit value-channel derivative \(A_{\val}\), the exact vanishing \(\Phi_K(A_{\val})=0\), the small-\(x\) expansion, the nonzero pairing with the toy anomaly matrix, and the formal calibration functional. This is a calibration interface, not a completed-\(L\) realization theorem.
- `paper/proof_of_rh.tex:856-946` already imports zeta-side realization input: omitted-zero denominators and the zero-free lower bound \(a_\rho\ge \sigma_0/Q\). So microscopic holomorphy in the actual draft is not purely source-light.
- `paper/proof_of_rh.tex:1497-1754` proves the corrected local decomposition and the preserved \(Q^{-3}\) transfer scale only after fixing the zeta-side core / tail / cutoff package.
- `paper/proof_of_rh.tex:2050-2322` proves the odd scalar theorem only for the realized corrected scalar \(H_m(s)=\Phi_K(\widehat\Omega_\zeta^{\corr}(s;m))\), with the boundary estimate tied to \(L(m)S(m)^2/Q^3\).
- `paper/proof_of_rh.tex:2975-3169` is the cleanest universal layer. Once an odd holomorphic germ with coefficient control is supplied, the coefficients \(a_j^{(N)}\) and the odd-moment cancellation are purely algebraic.
- `paper/proof_of_rh.tex:25842-26022` explicitly says the remaining contradiction is RH-specific and cannot be closed from local or intrinsic geometry alone.

conditional on explicit hypotheses

- The abstract odd-germ/projector theorem is honest only if the realization hypotheses are named separately: real channel, same-point positivity for holomorphic whitening, microscopic denominator comparability, corrected-whitening transfer at scale \(Q^{-3}\), and a boundary bound for the transverse scalar.
- The calibration comparison can be retained only as a conditional addon. It needs a real value-channel derivative in the chosen family, a real sign-compatible amplitude replacing \(S(m)\), a nonzero toy pairing in the same channel, and a remainder estimate small enough to justify \(u^2\asymp (x/B)A_L(m)\).
- For non-self-dual settings, the draft does not determine the correct real object. Any claim that a raw single complex channel suffices is unsupported from the cited regions alone.

missing

- A completed-\(L\) realization theorem for the corrected local block outside zeta.
- A named real-channel hypothesis. "Real phase" is too vague unless one says which completed critical-line object is real and odd under the required symmetry.
- A named calibration-sign hypothesis. "Calibration amplitude" is too vague unless one says it is real and sign-compatible in the channel used.
- A family-uniform microscopic denominator theorem replacing the zeta omitted-zero denominator package.
- A family-uniform preserved-whitening-scale theorem giving the same \(Q^{-3}\) gain after correction and application of \(\Phi_K\).
- For any calibration comparison beyond zeta, a proof that the pairing denominator does not vanish in the chosen family / channel.

phrases that need weakening with scoped negation

- Replace "the local package rules out global obstructions" by "the local package does not, from this scope alone, rule out the remaining global propagation problem."
- Replace "the calibration comparison is family-agnostic" by "the calibration comparison is not family-agnostic from the cited draft regions alone; it is conditional on a realized real calibration channel."
- Replace "complex Dirichlet channels fit the same theorem" by "complex Dirichlet channels are not shown from the cited draft regions alone to fit the same real odd-scalar theorem."
- Replace "the current local theory excludes remote incidences" by "the current local theory does not, from local scope alone, exclude remote endpoint-gap incidences."
- Replace "only constants change in other families" by "it is not shown from the cited draft regions alone that other families differ only by constants."

# Exact refs

- Common brief and reporting discipline: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/notes/common-brief.md:15-44`.
- Cycle synthesis portability boundary: `/mnt/c/workspace/riemann2/grh/20260423-050630-research-team-grh-dirichlet-tau/synthesis.md:11-18`, `20-67`, `79-85`.
- Route A portability proposal: `/mnt/c/workspace/riemann2/tasks/20260423-052540-attack-gap-local-package-portability/reports/gap-local-package-routeA.md:3-27`, `41-65`, `88-103`.
- Route B portability proposal: `/mnt/c/workspace/riemann2/tasks/20260423-052540-attack-gap-local-package-portability/reports/gap-local-package-routeB.md:5-10`, `20-48`, `68-78`.
- Abstract local kernel / finite-\(s\) block package: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:145-269`.
- First explicit zeta-side layer: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:271-301`.
- Calibration interface: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:426-850`.
- Denominator comparability and holomorphic omitted-smooth package: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:856-946`.
- Corrected decomposition / cutoff compatibility / preserved transfer scale: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:1497-1754`.
- Sharpened calibration remainder and odd holomorphic transverse scalar: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2050-2322`.
- Universal \(N\)-point odd-moment projector: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:2975-3169`.
- Scoped-negation endgame boundary: `/mnt/c/workspace/riemann2/paper/proof_of_rh.tex:25842-26022`.

# Dependencies

- A chosen real completed critical-line channel.
- Positive-definite same-point blocks on the microscopic disk so that holomorphic whitening is defined.
- Microscopic denominator comparability on that disk.
- Corrected same-point and mixed-block perturbation estimates with preserved \(Q^{-3}\) transverse scale after whitening and application of \(\Phi_K\).
- A microscopic boundary estimate for the realized transverse scalar.
- For the calibration layer: a real sign-compatible amplitude, a nonzero toy pairing, and a small calibration remainder in the same channel.

# Strongest objection

The proposed theorem still hides the hard family-specific analytic work inside phrases like "real phase," "corrected decomposition," "boundary estimate," and "calibration interface." In the cited draft regions those are not cosmetic wrappers around abstract local algebra. They encode the actual zeta-side realization: omitted-zero denominator control, zero-free input, holomorphic whitening on the microscopic disk, the preserved \(Q^{-3}\) gain, and a real sign-compatible value-channel amplitude. If those hypotheses are not split out explicitly, the statement overstates what the draft has really proved.

# Needed for promotion

1. State the theorem in two explicit layers: abstract odd-germ/projector theorem first, calibration comparison second.
2. Name the hidden realization hypotheses separately: real channel, denominator comparability, preserved whitening scale, boundary theorem, calibration sign, and nonvanishing toy pairing.
3. Stop the unconditional theorem before calibration.
4. If calibration is kept, label it conditional on those added hypotheses rather than as part of the source-light theorem itself.
5. Use scoped negation whenever excluding what the theorem does not do: remote incidences, global propagation, GRH-style consequences, and complex-channel realizations should all be qualified by "from the cited draft regions alone" or "from local scope alone."

Honest verdict: the cited draft regions support a real abstract odd-germ / odd-projector mechanism and a separate conditional calibration interface. They do not support the stronger family-agnostic local portability theorem as currently proposed. The clean honest boundary is: unconditional theorem up to the odd-germ/projector layer; calibration only as a conditional layer; no claim, from local scope alone, about remote incidences or any GRH-style endgame.
