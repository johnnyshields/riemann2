## Claim
The clean minimal patch is to insert one new zeta-source subsection at the start of `\section{Zeta-side decomposition}` in `paper/proof_of_rh.tex`, immediately before the current split `q(t)=B_\zeta(t)+S(t)` at lines 271-288. The subsection should canonically identify the manuscript's abstract phase derivative `q(t):=\Phi'(t)` from lines 149-160 with the zeta quotient source `\phi(s)=\Lambda(2s-1)/\Lambda(2s)` on `s=\tfrac12+it`, then package the zero kernel formula and the compact-interval summation statement needed to justify `S`.

## Status
open

## Evidence
Proved:
- The draft already separates an abstract local phase package from the later zeta-specific package. The abstract object is introduced at `paper/proof_of_rh.tex:149-160`, where `q(t):=\Phi'(t)` is defined with no canonical zeta source attached yet.
- The first zeta-specific insertion point is `paper/proof_of_rh.tex:271-288`. There the draft begins using `q(t)=B_\zeta(t)+S(t)` and `S(m):=q_\zeta(m)-B_\zeta(m)` before any theorem identifies `q` or `q_\zeta` with a specific completed-zeta quotient.
- The positive strip-edge kernel already appears in canonical form in the tail section at `paper/proof_of_rh.tex:345-355`. So the single-zero term needed by the source theorem already matches an existing manuscript kernel.
- The smallest source package is already isolated in the GRH notes as three theorem-level parts plus two explicit convention/identification items: quotient/phase normalization, single-zero contribution, compact-interval summation/regularization, plus background identification and multiplicity convention. See `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-23`.
- The candidate theorem note states the exact desired theorem with the quotient `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`, a boundary phase `\phi(\tfrac12+it)=e^{-2i\Phi(t)}`, the derivative `q(t):=\Phi'(t)`, and the zero-kernel sum; see `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:32-63`.

Conditional on archive-backed source promotion:
- The candidate note records archive provenance for the quotient and the factor-of-2 normalization `\partial_s\log\phi(\tfrac12+it)=2q(t)`, but explicitly says this remains archive provenance until promoted into the canonical draft; see `.../source_theorem_candidate_note.tex:81-125`.

Missing:
- The main draft still lacks the theorem that ties its abstract `\Phi` and `q` to the specific zeta quotient object before using `B_\zeta` and `S`; compare `paper/proof_of_rh.tex:149-160` with `paper/proof_of_rh.tex:271-288`.
- The draft still uses three background names without one source-level identification theorem: `B_\zeta` at lines 275-287, `B_{\Aut}` at line 281, and `B_{\bg}` at lines 1479-1490.
- The draft still has a notation hitch at `paper/proof_of_rh.tex:287`, where `S(m)` is defined using `q_\zeta(m)` even though the active symbol in the section is `q(t)`.

Minimal patch package:
1. Add a new opening subsection under `\section{Zeta-side decomposition}` titled along the lines of `Canonical zeta source theorem`.
2. In that subsection, state the quotient/phase normalization theorem:
   `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`, choose a continuous boundary phase on a compact interval, and define `q(t)=\Phi'(t)` from that source.
3. State the single-zero contribution theorem using the existing kernel
   `f_{\beta,\gamma}(t)=\frac{1-\beta}{(1-\beta)^2+(2t-\gamma)^2}+\frac{\beta}{\beta^2+(2t-\gamma)^2}`
   so the manuscript's `S` slot is explicitly the positive strip-edge zero contribution.
4. State the compact-interval summation/regularization theorem needed to justify the summed formula on the intervals used locally.
5. Immediately after that theorem package, define one background symbol and one zero scalar consistently:
   `q(t)=B_\zeta(t)+S(t)` and `S(m)=q(m)-B_\zeta(m)`.
6. Defer broader cleanup, but note that this insertion unlocks later replacement of `B_\zeta`, `B_{\Aut}`, and `B_{\bg}` by one identified background notation with local aliases only where genuinely needed.

Smallest unlocked cleanup:
- Replace the stray `q_\zeta` in `S(m):=q_\zeta(m)-B_\zeta(m)` by the now-canonical `q`.
- Add one explicit sentence fixing zero multiplicities.
- Add one explicit sentence identifying the background name used by the source theorem and how the later `B_{\Aut}` / `B_{\bg}` bookkeeping names relate to it.
- After that, later sections can treat the local package as source-backed instead of switching between abstract-phase and zeta-specific symbols.

## Exact refs
- `paper/proof_of_rh.tex:149-160`
- `paper/proof_of_rh.tex:271-288`
- `paper/proof_of_rh.tex:345-355`
- `paper/proof_of_rh.tex:1479-1490`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:28-30`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/birds-eye-view-for-rh-agent.md:153-163`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/notes/zeta_source_package.md:8-23`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:32-63`
- `grh/20260423-050630-research-team-grh-dirichlet-tau/paper/source_theorem_candidate_note.tex:81-125`

## Dependencies
- Promotion of the zeta quotient source theorem from the candidate note or equivalent fresh derivation in the canonical draft.
- A compact-interval convergence/regularization statement strong enough for the local windows actually used later.
- One explicit convention for multiplicities and one explicit identification of the background term.

## Strongest objection
The patch is minimal only at the paper-structure level. It is not minimal at the proof-burden level: the compact interval source theorem and the background identification are still real theorem content, not mere notation repair. So the insertion cannot honestly be presented as bookkeeping only.

## Needed for promotion
- Prove or promote into the main draft the quotient/phase normalization for `\phi(s)=\Lambda(2s-1)/\Lambda(2s)`.
- Make the factor-of-2 normalization and branch choice explicit in canonical form.
- State the single-zero term and compact-interval summation theorem in theorem form, not just as downstream kernel usage.
- Fix the notation immediately after insertion so `q`, `S`, and the background symbol are used consistently from that point onward.
- Honest verdict: this is the cleanest small patch because it closes the first source-specific gap without redesigning the endgame, but it remains conditional until the source theorem itself is promoted.
