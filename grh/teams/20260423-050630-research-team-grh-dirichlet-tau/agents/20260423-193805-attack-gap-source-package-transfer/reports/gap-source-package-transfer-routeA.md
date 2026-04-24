# Claim

The localized zeta source-theorem package has a coherent paired-Dirichlet analogue at the level of package structure, but only part of it is formal transfer. A safe paired target is a five-item package built around
`Phi_chi^pair(s) = Xi_chi(2s-1)/Xi_chi(2s)` with `Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)`.

For the three theorem-level parts and two convention/identification items, the paired analogue is:

1. Quotient / phase normalization theorem.
Paired analogue: fix `Phi_chi^pair(s)` as the source quotient and prove that the manuscript's paired phase derivative is the correctly normalized logarithmic derivative or boundary-phase derivative of that quotient, including branch, sign, and factor-of-2 conventions.

2. Single-zero contribution theorem.
Paired analogue: prove that one paired zero packet contributes the exact local scalar occupying the paired manuscript `S(m)` slot after subtraction of the unified paired background. Because `Xi_chi` packages `rho` and `bar rho` together, the local term should be a contragredient-symmetrized one-zero contribution upstairs, not a raw single-channel contribution.

3. Compact-interval summation / regularization theorem.
Paired analogue: on singularity-free compact intervals for the paired strip-edge variable, prove convergence / regularization for the paired zero-sum after removing the unified background, so the paired local-slot sum is well-defined and equals the paired source quantity.

4. Background identification / unification item.
Paired analogue: identify one `B_chi^pair` that absorbs conductor scaling, gamma-derivative terms, and any trivial-zero / pole corrections, and prove that it is the same object wherever the manuscript would otherwise use multiple names for the paired background.

5. Zero multiplicity convention item.
Paired analogue: state explicitly whether zeros are counted by zeros of `Lambda(s,chi)`, by packets in `Xi_chi`, or by paired strip-edge images, and how multiplicities behave when `rho=bar rho` or when a zero appears in both factors with the same multiplicity.

Transfer classification:

- Formal transfer or near-formal transfer: the choice of quotient object in item 1, most of the normalization architecture in item 1 once the paired phase is defined, and the compact-interval summation / regularization template in item 3.
- Needs genuinely new family input: the exact local-slot identity in item 2, the full content of `B_chi^pair` in item 4, and the precise multiplicity convention in item 5 whenever pairing changes how zeros are grouped.

# Status

open

# Evidence

Proved:

- The theorem-facing paired quotient object is already identified safely as `Phi_chi^pair(s) = Xi_chi(2s-1)/Xi_chi(2s)` with `Xi_chi(s)=Lambda(s,chi)Lambda(s,bar chi)`.
- Pairing removes the residual root-number asymmetry at the boundary-phase level, so the zeta-style quotient-facing front end has a genuine paired analogue.
- Conditional on an exact paired-source theorem, the one-zero strip-edge kernel and its positivity are automatic upstairs. This supports transfer of the package architecture but not the missing source theorem itself.
- On the zeta side, the source gap is already localized as a package with exactly three theorem-level parts plus two convention/identification items. That localization is what transfers.

Conditional on explicit paired source bookkeeping:

- Item 1 should transfer with modest new work: once the paired manuscript phase quantity is fixed, the branch / sign / factor-of-2 normalization theorem should mirror the zeta quotient-phase theorem because pairing was chosen precisely to cancel the front-end root-number defect.
- Item 3 should transfer in template form: the compact-interval regularization argument is plausibly the same kind of singularity-free local summation theorem, but with `B_chi^pair` and the paired local zero packets in place of the zeta objects.
- If item 2 and item 4 are proved, then the paired `S(m)` slot would admit the same package-level decomposition as on the zeta side: unified background plus regularized local zero contributions.

Missing:

- No note supplied here proves that the paired manuscript phase derivative has already been defined and matched exactly to `Phi_chi^pair`; the source note only says this is the clean theorem target.
- The key new family step is the exact local-slot identification: proving that the background-subtracted paired source quantity is exactly the coefficient in the manuscript's paired `S(m)` slot, not just a related positive kernel upstairs.
- The content of `B_chi^pair` is not yet theorem-level. The note states what it should contain, but not an exact identity on compact intervals.
- The multiplicity convention is not routine bookkeeping, because pairing changes the granularity from individual `Lambda(s,chi)` zeros to packets inside `Xi_chi`; this matters for the one-zero term and for local-slot exactness.

# Exact refs

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-23` for the five-part zeta package.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:16-20` for the zeta model statement that the missing theorem identifies the manuscript phase derivative with the quotient candidate.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:31-40` for the zeta checklist of still-conditional items that define the transferable package structure.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:20-27` for the paired theorem target as exact local-slot source realization.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:29-47` for `Phi_chi^pair`, the cancellation of root-number asymmetry, and the statement that positivity upstairs is automatic only conditional on an exact paired-source theorem with exact local-slot identification.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:49-55` for the unified `B_chi^pair` content and the warning that exact background identification on compact intervals is still needed.
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/dirichlet_paired_source.md:66-73` for what pairing does not fix.

# Dependencies

- A precise paired manuscript-side definition of the phase derivative or local source quantity that is supposed to equal the logarithmic derivative data from `Phi_chi^pair`.
- Exact decomposition of `Xi_chi` logarithmic-derivative contributions into local zero packet terms plus a unified `B_chi^pair` on compact intervals.
- A theorem-level rule for how zeros and multiplicities of `Lambda(s,chi)` and `Lambda(s,bar chi)` descend to the paired local term.
- The existing conditional implication that the one-zero strip-edge kernel upstairs yields the desired paired local-slot scalar once exact source-to-slot identification is available.

# Strongest objection

The transfer may look more formal than it is. The package shape transfers, but the decisive theorem-level content on the paired side is exactly the part the notes still isolate as missing: exact source-to-slot identification. Without that, item 2 is not a routine adaptation of the zeta single-zero theorem, and items 3-5 may hide family-specific corrections from conductor, gamma factors, and paired multiplicity bookkeeping.

# Needed for promotion

1. State the paired analogue of the zeta quotient-phase theorem explicitly: what manuscript quantity equals the derivative of `Phi_chi^pair`, on what domain, and with what normalization.
2. Prove an exact one-zero paired contribution formula giving the coefficient that occupies the paired `S(m)` slot, not just an upstairs positive kernel.
3. Prove a compact-interval regularization theorem for the paired sum with all singular terms isolated.
4. Define and identify one exact `B_chi^pair` and show it matches every background term appearing in the paired source formula.
5. Fix and prove the multiplicity convention for paired zero packets, including the self-conjugate / overlapping cases.
6. Re-run an adversarial check that no hidden denominator-comparability, whitening, odd/transverse, or boundary-control assumptions have been smuggled into the paired source package.

Honest verdict: the package transfers cleanly as a blueprint, but not yet as a theorem. Items 1 and 3 look structurally portable once the paired phase quantity is defined. Items 2, 4, and the nontrivial part of 5 still need genuine paired-family input, so the direct route-A transfer does not close the paired source theorem from current scope alone.
