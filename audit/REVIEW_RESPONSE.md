# Response to the substantive review concerns

4 October 2026. This response concerns the revised research candidate,
*Sharp rank bounds and all-parameter tree--network separation*.
It summarizes the changes without reproducing
the supplied assessment. The accompanying mathematical audit identifies the
precise manuscript bytes it inspected.

The revision retains the original all-parameter conclusion, separates its two
different substitution-model regimes, and adds a sharp rank result with a
mixture consequence. Mathematical claims remain subject to external specialist
assessment. Neither this response, the internal audit, nor successful replay
constitutes journal acceptance, a priority certificate, formal verification,
or an awarded REF rating.

The response was checked against `paper.tex` with SHA-256
`3177f8135159a525447b3ec1aea0fd6f62e65ef9823b6da77ad58456ed8fbf75`.
The source labels below locate the revised statements independently of PDF
pagination:

| Manuscript location | Revision covered |
|---|---|
| Section 1.1 and `tab:comparison`; Section 5.1 | Theorem-level prior work and exact known JC specialization |
| Section 2 | Probability, generator, finite-time, attachment and flattening conventions |
| Section 3, `thm:rank`, `cor:mixture` | Sharp rank theorem and fixed-topology mixture consequence |
| Section 4, `lem:gm-reduction`, `thm:gm-network` | Positive GM reduction and larger-taxon conclusion |
| Section 5, `lem:generator`, `thm:triangle`, `lem:triangle-reduction`, `cor:reversible-large` | Full finite-state reversible triangle theorem and network reduction |
| Section 6, `prop:binary` | Exact binary-symmetric boundary and positive mimic |
| Section 7, `thm:triangle-closure`, `cor:compact` | Unrestricted tree-closure exclusion and compact-domain margin |
| Section 8, `cor:residual`, `cor:test` | Computable rank residual and qualified independent-site consequences |
| Section 9 and Declarations | Scope limits, boundaries, provenance and candidate status |

| Review concern or requested improvement | Concrete response in this candidate | Evidence and remaining limit |
|---|---|---|
| Compare the closest results theorem by theorem. | Added a comparison of the actual network classes, substitution assumptions, positive versus generic parameter claims, and conclusions in the introduction and source supplement. | `theorem-comparison.md`, `prior-art.md`, bibliography and source manifest. The search is bounded and does not establish worldwide priority. |
| Credit the known Jukes--Cantor triangle obstruction. | Explicitly credits Englander and the later Currie semialgebraic treatment; supplies the exact relabelling and parameter translation to the moment identity used here. | The comparison shows algebraic coincidence in the uniform four-state case. No novelty is claimed for that factorization. |
| Distinguish the residual triangle contribution. | Isolates the shared-generator identification by a symmetric logarithm, the multiple-decay-rate argument, and the arbitrary-frequency equal-input case. | The triangle proof treats every allowed spectrum, including repeated eigenvalues. It does not cover unrelated GTR generators on different triangle edges. |
| Resolve the specific equivariant-network overlap lead. | Compared the accessible announced theorem and published equivariant results directly. The announced lower bound is generic; the inspected published results provide upper constraints. | Source/version/slide locators are recorded. The complete five-author manuscript was not located, so undisclosed results have not been ruled out. No first-ever claim is made. |
| Replace commission-oriented presentation with a research article. | Uses a research title, abstract, related-work comparison and explicit contribution statement. Commission recovery and operational provenance belong to the supplement. | Main manuscript and supplementary audit material are separate. AI-assisted derivation and internal checking remain disclosed. |
| Promote the general Markov four-cycle theorem. | Makes the four-cycle result a main result with its own assumptions and proof. It requires neither stationarity, reversibility, a common generator nor commuting channels. | Positive root weights, positive nonsingular core channels and interior inheritance remain explicit hypotheses. |
| Strengthen significance through a wider mathematical consequence. | Strengthens the crossed-flattening bound to the sharp value `d(d+1)/2`, with equality in a symmetric family. The other two flattenings have rank `d²`. | The universal proof uses a subspace filtration; examples do not establish the lower bound. This is a substantive extension, not a claim of an achieved quality rating. |
| Clarify what the rank result excludes beyond a single tree. | Excludes mixtures of at most `floor(d/2)` arbitrary `d`-state GM components on one common tree topology. For four states this includes two-component mixtures. | Uses the established rank upper bound `md` for such mixtures. Components with different tree topologies and unrestricted class counts are outside the conclusion. |
| Define observable cycle attachments and justify larger networks. | Gives the concrete component-after-cycle-edge-removal definition and separately states reduction results preserving the relevant transition model. | Single-reticulation and observable-attachment assumptions are visible. Unobservable two-attachment cycles and arbitrary overlapping reticulations are excluded. |
| Make contraction and rerooting reproducible. | States the reversible fork identity for shared-generator triangles and the positive Bayes reversal/path contraction used for GM reductions. | These established mechanisms are cited. The relevant positivity, nonsingularity and conditional independence assumptions are retained. |
| Make flattening conventions and inheritance notation explicit. | Defines index order before determinant calculations and keeps `delta=1-gamma` explicit. | Determinant and transformed-row identities are checked against directly constructed tensors in the supplement. |
| Preserve the distinction between exact separation and practical detection. | Adds exclusion of positive triangle points from the entire unrestricted homogeneous reversible tree closure, then proves a positive margin on every compact admissible network parameter family. | The competing tree family is not artificially compactified by bounding its parameters. The margin is existential; no useful numerical lower bound or efficient distance algorithm is supplied. |
| Explain boundary degeneration. | Retains the zero global infimum distance as inheritance tends to a displayed-tree endpoint, and the decay of the cubic defect for short cycle edges or strongly attenuated pendants. | Compact-family separation does not imply one uniform positive margin over the whole open parameter domain. |
| Clarify the finite-sequence implication. | For four-cycles, the sharp rank result makes a standard singular-value residual strictly positive at every allowed parameter. A conservative independent-site threshold gives an explicit type-I bound and pointwise consistency. | The score and low-rank approximation principle are credited as established tools. No near-optimal sample complexity, numerical-error guarantee, site-dependence guarantee or biological calibration is claimed. |
| Extend the state-space theorem carefully. | Proves triangle separation for every `d≥3` and also for nonuniform two-state stationarity. | Irreducibility and a positive stationary distribution are required. The equal-input model itself is established prior work. |
| Include a binary-symmetric negative control. | Gives the complete positivity criterion for a matching CFN tripod and an exact example with positive lengths on both objects. | Attributes the underlying CFN moment inversion to existing literature. All eight pattern probabilities are checked directly. A blanket binary separation claim is explicitly false. |
| Exercise genuinely noncommuting and nonreversible examples. | Adds deterministic rational GM examples in dimensions 2--5, nonzero commutator witnesses, and nonreversibility witnesses for dimensions at least three. | Positive two-state channels are reversible, and the supplement says so. Finite examples test scope and algebra, not universal validity. |
| Make verification robust and appropriately described. | Uses exact symbolic/rational checks, normal and optimized Python replays, source hashes and deliberate semantic fault controls. Preserves the symmetric rank-10 and inheritance-boundary controls. | The recorded replay reports two passing baseline modes and eight expected mutation failures. This is reproducible computational checking, not a proof assistant or external peer review. |
| Preserve provenance without confusing it with acceptance. | Keeps manuscript sources, source records, receipts and internal mathematical audits in the evidence bundle; the article carries a concise disclosure. | The independent roles were internal to the same AI-assisted workflow. External review, publication state and theorem correctness remain separate questions. |
| Strengthen the case for a prospective REF four-star assessment. | Adds a sharper universal rank theorem, a precise fixed-topology mixture consequence, an exact state-space boundary and a tree-closure result, alongside a more complete literature comparison. | These changes supply material for reassessment. They do not guarantee significance, lasting influence, institutional eligibility, an official score or a future panel decision. |

## Exact scope retained

For triangles, the result concerns stationary evolution with one irreducible
reversible generator per object, shared across its edges. A competing tree may
choose its own generator and stationary distribution. For four-cycles, the
transition matrices may be unrelated general Markov channels, subject to the
stated positivity and nonsingularity requirements.

The paper does not establish full network reconstruction, unique reticulation
orientation, recovery of all edge parameters, arbitrary edge-specific GTR
triangle separation, arbitrary rate heterogeneity, coalescent identifiability,
or mixtures on different tree topologies. More extensive prior art or an
external mathematical objection could change the assessment. The revised
document is a strengthened, inspectable research candidate.
