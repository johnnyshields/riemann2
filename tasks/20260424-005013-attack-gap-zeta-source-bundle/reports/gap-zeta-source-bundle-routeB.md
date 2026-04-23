# gap-zeta-source-bundle-routeB

**Claim**

After the quotient / phase normalization bridge is fixed, the safest paper-facing patch is **not** four separate micro-theorems. The single-zero contribution, compact-interval summation / regularization, background identification, and multiplicity convention should be packaged as **one localized zeta source theorem with internal clauses**, adjacent to but separate from the front-loaded quotient / phase normalization theorem. So the theorem-level split should be:

1. quotient / phase normalization theorem;
2. localized source theorem containing: single-zero source formula, compact-interval sum / regularization, identification of the background term, and the multiplicity convention.

This is the strongest safe patch-plan verdict. A further split into independent theorem statements is not yet justified by the current dependency structure.

**Status**

conditional

**Evidence**

Proved:

- The package boundary is already localized in the notes: only quotient / phase normalization is cleanly first, while the remaining items are safer together after that bridge is fixed (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:20-30`).
- The patch-plan note says the minimal paper-facing insertion at the start of `\section{Zeta-side decomposition}` is exactly a five-part source package (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-12,23-31`).
- The current draft first uses zeta-specific source notation at `paper/proof_of_rh.tex:271-301`, namely `q=B_\zeta+S`, the local split, and `S(m)=q_\zeta(m)-B_\zeta(m)`. This is the natural cut point for a front-loaded theorem package (`paper/proof_of_rh.tex:271-301`).

Conditional on the quotient fix:

- The missing front-end is the quotient object and sign convention, not the factor of `2`; the exact bridge currently needed is `(\phi'/\phi)(1/2+it)=-2q(t)` under the archived negative-sign boundary law, or equivalently one must flip the phase convention if the draft keeps positive `q=B_\zeta+S` (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-39`).
- Once that bridge is repaired, the remaining burden is described as explicit source bookkeeping on singularity-free compact intervals, but still with theorem content, not mere notation cleanup (`grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:16-18,31-40,46-48`).
- Those remaining items are coupled in the draft’s notation itself: `S(m)` is defined through `B_\zeta`, later estimates also use `B_{\Aut}` and `B_{\bg}`, and the package must explain why all these denote the same background contribution in the theorem-facing source normalization (`paper/proof_of_rh.tex:275-287,281-283,1471-1490`; `grh/.../notes/zeta_source_package.md:27-30`).

Missing:

- There is still no canonical theorem in the draft proving the single-zero source contribution in the manuscript’s exact `S` slot.
- There is still no compact-interval theorem converting the formal zero sum into a regularized/convergent source formula with the needed removable-singularity bookkeeping.
- There is still no theorem-facing identification unifying `B_\zeta`, `B_{\Aut}`, and `B_{\bg}`.
- There is still no explicit multiplicity convention stating whether zeros are counted with multiplicity in the source sum and how that enters the local formula.

Why one bundled theorem is safer than several adjacent independent theorems:

- The single-zero formula by itself does not yet produce the manuscript’s `S(m)` object. It only becomes paper-usable after the compact-interval summation and background identification are stated together.
- Background identification is not cosmetically downstream. It determines what quantity is being subtracted in the very definition of `S(m)`.
- Multiplicity is not an optional remark. It changes the exact coefficient in the local source sum, so if it is deferred to prose the theorem statement remains underspecified.
- Splitting these into separate theorems would invite false independence: the second theorem would still have to assume the background and multiplicity conventions from later statements, or else restate them. That is weaker and less clear than one localized source theorem with explicit clauses.

**Exact refs**

- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-30`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/quotient_normalization.md:8-49`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_theorem_gap.md:16-18,31-40,46-48`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/rh_patch_plan.md:8-31`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/source_package_transfer.md:19-38`
- `paper/proof_of_rh.tex:271-301`
- `paper/proof_of_rh.tex:1471-1490`
- `paper/chats/20260410-043629-69d87e03-a5c8-83a5-9f21-1062e8b6d064-riemann-hypothesis-insight.md:617-657`

**Dependencies**

- A corrected quotient declaration `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`.
- A fixed boundary phase convention consistent with the sign of `q`.
- An explicit theorem-level statement that the zero-source sum on compact singularity-free intervals equals the manuscript’s `S` after subtraction of the identified background term and with multiplicity specified.

**Strongest objection**

The bundled-theorem recommendation could be too conservative if the single-zero formula can be proved in a genuinely normalization-free way and the compact-interval/background/multiplicity package can then be reduced to a short corollary. I do not see that independence in the current notes or in the draft’s notation. Right now the paper uses `S(m)` only after background subtraction, so a stand-alone single-zero theorem would still not justify the object actually used later.

**Needed for promotion**

- Repair the quotient / phase normalization bridge in theorem-facing form.
- State one localized source theorem immediately after that bridge, with explicit clauses for:
  - single-zero source contribution;
  - compact-interval summation / regularization;
  - background identification `B_\zeta=B_{\Aut}=B_{\bg}` in the scope actually used;
  - zero multiplicity convention.
- Make the theorem conclude the manuscript-facing identity `q=B_\zeta+S` with precise scope, so that `S(m)=q_\zeta(m)-B_\zeta(m)` is justified where first used.

Honest verdict: keep quotient normalization separate, but bundle the rest. One theorem after the bridge is the strongest safe patch. More fragmentation would overstate independence that the current source package does not yet have.
