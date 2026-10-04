# Mathematical audit of the integrated revised candidate

Date: 4 October 2026.

**Outcome: PASS after two precision clarifications.** No substantive
mathematical gap was found in the inspected manuscript. This outcome concerns
the statements under their explicit hypotheses, not unrestricted network
identifiability, research priority, publication completion or a REF rating.

## Exact artifact and audit independence

Audited source:
`outputs/tree-network-separation-candidate/paper.tex`

Title: *Sharp rank bounds and all-parameter tree--network separation*.

SHA-256:
`3177f8135159a525447b3ec1aea0fd6f62e65ef9823b6da77ad58456ed8fbf75`

The checksum was obtained directly from the saved file after the authoring
agent froze the LaTeX source. All line locators below refer to those bytes.
A later source change requires checking the change and renewing this binding.
The DOI string in the manuscript is metadata; this audit does not verify
that a deposited or publicly served object has those same bytes.

This was an internal adversarial integration audit in an AI-assisted
workflow. The auditor contributed the triangle-extension derivation and
independently checked the rank-extension derivation. It is therefore not
external peer review and is not independent of the research workflow as a
whole. The entire integrated LaTeX source was read, and the central algebra,
limits and statistical implications were checked. No proof assistant was
used. The separate executable replay is evidence from another work stream;
this audit does not claim to be a fresh execution of that suite.

## Findings raised and resolved before the final binding

| Finding | Why it mattered | Resolution in the audited source |
|---|---|---|
| The common-generator model needed explicit finite nonnegative times, rather than relying on the usual meaning of an edge time. | Infinite pendant lengths can destroy the strictly positive moment signal. The reduction statement explicitly bounded cycle times but should not leave the selected pendant paths ambiguous. | Lines 281--284 now define all edge times as finite nonnegative reals, with the indicated cycle edges strictly positive. Lines 214--215 also make finite graphs and two-parent reticulations explicit. |
| The triangle testing paragraph reused the empirical-tensor notation just defined for quartet patterns. | The quartet and triangle alphabets have sizes `d^4` and `d^3`; their empirical distributions must not be silently identified. | Lines 945--948 explicitly restart the construction with `n` iid three-leaf patterns. |

No unresolved finding affecting the proved conclusions remains from this
audit. These were clarity repairs to hypotheses and notation; neither
required changing the substantive proof.

## Proof-by-proof checks

| Exact source locator | Adversarial check | Finding |
|---|---|---|
| Lines 208--285, Section 2; `lem:tree-rank` at line 249 | Confirmed the finite-state and row-stochastic conventions, shared-edge displayed-tree law, observable-attachment definition, real invertibility and finite-time domain. Conditioning across a tree edge gives rank at most `d`, including degenerate comparison parameters; rank subadditivity gives `md`. The pendant Kronecker multiplications have the correct transposes. | Valid. Inverse pendant channels need not be stochastic; the proof correctly uses only their invertibility. |
| Lines 299--341, `thm:rank`, `eq:det-factor`, both determinant equations | Multiplied the block factorization entry by entry. The block `R_k=1 V_(k·)` is rank-one idempotent because its row sums equal one. Hence each block contributes `gamma^(d-1)` and the whole factor contributes `gamma^(d(d-1))`. Checked the parent-swapped formula and its `delta` exponent. | Valid without reversibility or commutativity. The positivity assumptions make every scaled row factor nonzero. |
| Lines 344--386, `eq:AiBi`, `eq:row-star`, `eq:diagonal-aggregate` | Independently derived the row-matrix transformation `S^-T M T^-1`. The `A_i` are invertible. Summing a row family supplies the `i`th diagonal matrix. Projection to entries `(h,i)`, `h>i`, annihilates all previous families and the diagonal subspace, while the current family has projected rank `d-i`. | Valid. Rank-nullity on the quotient gives the claimed dimension increments; there is no cancellation loophole. |
| Lines 388--401, `eq:sharp-example` | With `S=T`, `U=V` and equal inheritance, the crossed columns indexed by `(j,k)` and `(k,j)` coincide. There are at most `d(d+1)/2` distinct columns, matching the lower bound. The given symmetric stochastic matrix is an irreducible continuous-time transition at positive finite time. | Valid sharpness for every `d≥2`. It does not assert universal full crossed rank or that every intermediate integer occurs. |
| Lines 413--428, `cor:mixture` | Checked the strict comparison `md<d(d+1)/2` for integer `m≤floor(d/2)`, and the treatment of star/nonbinary/degenerate comparison trees. | Valid only for components sharing one topology, exactly as stated. Different-topology mixtures are explicitly excluded from the claim. |
| Lines 438--474, `lem:gm-reduction` | Rerooted the common backbone before the reticulation conditional factor is applied. Verified `Mrev=D_pv^-1 M^T D_pu` is positive, stochastic and invertible. Three selected ordinary attachments have a middle point on the backbone path; the two outer paths lead to the two reticulation parents. Products preserve positivity and invertibility. | Valid under the single-reticulation and four-observable-attachment assumptions. Rerooting does not create history-dependent backbone parameters. |
| Lines 477--487, `thm:gm-network` | Every component on one full-tree topology restricts to the same induced quartet topology, even if its numerical parameters differ. | Valid lifting of the mixture exclusion. No multiple-reticulation extension is smuggled into the conclusion. |
| Lines 524--541, `lem:generator` | Leaf marginals force the candidate stationary distribution. The unaffected pair is not the identity, so its competing path length is positive. Conjugated generators are real symmetric, allowing the unique symmetric logarithm. | Valid. Arbitrary matrix logarithms are not asserted to be unique; repeated eigenvalues do not cause a gap. |
| Lines 544--579, `thm:triangle`, `eq:strict-concavity` | Checked the two-route attenuation, sign of the second derivative, and the strict-concavity comparison of `h(t)/t` at any two distinct positive decay rates. The two mixed pairs force incompatible route equalities unless `a=0`. | Valid for every spectrum containing two distinct nonzero decay rates. Tree branch lengths need not be assumed strictly positive for the contradiction. |
| Lines 581--640, `eq:equal-input`, `eq:contrast`, `eq:defect` | A single nonzero decay rate gives the equal-input generator by symmetric spectral decomposition and irreducibility. A minimum-probability state has frequency below one half for `d≥3`; binary nonuniform frequencies also give nonzero cubic moment. Recomputed all three pair moments, the third moment and the negative factorization. | Valid for all stated positive stationary frequencies. The normalization is consistent, and the binary uniform case is not silently included. |
| Lines 643--659, known JC specialization | Checked the relabelling and absorbed parameters against the supplied primary-source comparison. For the uniform four-state centered indicator, the normalized third moment equals the stated JC Fourier coordinate. | The mathematical translation is consistent and the special case is explicitly credited. This audit is not an exhaustive priority search. |
| Lines 661--696, `lem:triangle-reduction`, `cor:reversible-large` | Verified the reversible fork identity by detailed balance followed by the semigroup law. Retaining the hybrid attachment and two distinct ordinary attachments leaves three nonempty positive cycle paths. | Valid under the declared shared-generator stationary single-reticulation assumptions. Ordinary and split-vertex suppression remain in the model. |
| Lines 708--771, `prop:binary`, its inverse and explicit tensor | Spin-flip symmetry kills odd moments; the three pair moments determine all eight probabilities. The square-root inverse is unique among positive attenuation factors. The first two factors are automatically below one; the third gives exactly `Z²qr<A`, with equality and reverse inequality treated correctly. Recomputed the rational example's pair moments and all pattern values. | Valid. The example has positive finite network and tree lengths and disproves blanket binary-symmetric separation. |
| Lines 773--845, `thm:triangle-closure` | Allowed arbitrary changing candidate generators, stationary distributions and lengths. Positive limiting leaf marginals permit continuous normalization. All three limiting pair matrices are SPD, so the symmetric logarithms remain continuous. Trace normalization fixes the generator scale through the pure pair. The three scaled limbs are finite nonnegative limits of pair-trace combinations. | Valid exclusion from the entire stated tree closure. No compactness assumption on the competing parameter sequences is hidden in the proof. |
| Lines 847--875, larger-network closure statement and `cor:compact` | Marginalization is continuous. The image of a compact admissible parameter set is compact and disjoint from the closed tree model. The minimum distance is therefore positive. The separate zero global infimum follows by taking inheritance to a displayed-tree endpoint. | Valid. Pointwise closure exclusion is compatible with intersection of the two model closures at boundary limits. |
| Lines 877--915, `cor:residual` | The fixed-topology mixture class is contained in a finite union of closed rank-`md` varieties. Eckart--Young gives exact distance to that larger determinantal union, so its distance is a lower bound for distance to the mixture closure. Distance to a nonempty set is 1-Lipschitz. | Valid computable pointwise certificate. The proof does not mistake the determinantal variety for the full stochastic model. |
| Lines 917--944, `cor:test` | Recomputed the coordinate union bound with alphabet size `d^4`, checked the square-root threshold and the use of Lipschitz continuity under the null. Almost-sure empirical convergence and a positive population residual give pointwise consistency. | Valid conservative iid level bound. Coordinate independence is unnecessary and is correctly not assumed. |
| Lines 945--970, triangle rule and statistical qualifications | On the `d^3` alphabet, total variation is the maximum signed subset error. One-sided Hoeffding and a union bound over all subsets yield `2^(d^3) exp(-n epsilon_K²/2)` at threshold `epsilon_K/2`. | Valid idealized consequence. It assumes the margin and model distance and does not supply an efficient triangle test or a finite-precision guarantee. |
| Abstract, lines 41--63; Section 9, lines 972--1024; declarations beginning line 1026 | Compared headline conclusions with the actual theorem assumptions and with the negative controls. | No overbroad all-network, all-rate-mixture, orientation-identifiability or practical-detectability claim found. Candidate/internal-review status is explicit. |

## Limits of the audit result

The mathematical conclusions are tied to the stated number of observable
attachments, the single-reticulation network structure and the stated channel
domains. General-Markov triangle separation, arbitrarily many reticulations,
unrestricted mixtures on different tree topologies and coalescent processes
are not proved. The binary symmetric exception is real.

The source comparison has been substantially improved, but unavailable
unpublished work was not inspected. The manuscript states that ceiling.
This mathematical audit does not establish research priority or decide how
a REF panel would assess originality and significance. A source checksum
and a DOI do not by themselves establish external acceptance or canonical
publication readback.
