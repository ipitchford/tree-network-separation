# Sharp rank bounds and all-parameter tree–network separation

Anonymous · 4 October 2026

Candidate manuscript · DOI: [10.5281/zenodo.23140370](https://doi.org/10.5281/zenodo.23140370)

## Abstract

A generic identifiability theorem can leave exceptional positive parameters at which a phylogenetic network and a tree induce the same site-pattern probabilities. We establish all-parameter separation results for two single-reticulation models. First, for a $d$-state four-cycle with positive invertible Markov channels, two quartet flattenings have rank $d^2$ and the third has rank at least $d(d+1)/2$. The latter bound is sharp for every $d\ge2$, including positive continuous-time reversible examples. Consequently no such distribution is a mixture of at most $\lfloor d/2\rfloor$ general-Markov components sharing one tree topology; for nucleotide data this excludes two components. Bayes rerooting and marginalization extend the result to any single-reticulation network with at least four observable cycle attachments, without stationarity or reversibility. Second, a triangle evolving under one stationary irreducible reversible generator is separated from the entire closure of the homogeneous stationary reversible tree model for $d\ge3$, and also for two states with nonuniform stationary frequencies. The proof identifies the competing generator from an unaffected pair, then combines strict spectral concavity with a nonuniform equal-input moment obstruction. Its uniform four-state specialization is a known Jukes–Cantor inequality, which we explicitly credit. The remaining binary symmetric case admits an exact tree-mimicry criterion. Finally, the rank bounds yield a computable pointwise distance certificate and a conservative independent-site test. These conclusions concern the specified models, not unrestricted network identifiability or arbitrary rate heterogeneity.

**Keywords:** phylogenetic networks; general Markov model; time reversibility; flattening rank; mixture models; identifiability.

## 1 Introduction

A phylogenetic tree describes divergence through a sequence of branching events. A network can additionally represent reticulation, with different ancestral routes contributing to the distribution of an observed character. In a displayed-tree substitution model, one parent is chosen at each reticulation and evolution follows the resulting tree. Edges retained in several displayed trees carry the same transition matrices. This sharing is part of the model, rather than a restriction imposed after fitting an arbitrary mixture [\[9\]](#ref-Gross2021), [\[14\]](#ref-Sullivant2026).

The statistical question considered here is whether the complete site-pattern distribution can distinguish such a network from a tree. Generic identifiability settles this question outside an exceptional parameter set of lower dimension. An all-parameter result instead excludes every coincidence in a specified domain. These are different assertions: a distribution satisfying a special symmetry can be nongeneric while all its transition probabilities, branch lengths and inheritance weights remain strictly positive.

We study two complementary settings. A four-cycle permits a direct linear-algebraic argument under arbitrary positive invertible general-Markov (GM) channels. A triangle needs a different argument: we assume one stationary reversible generator throughout the network and allow a competing tree to choose its own stationary distribution and generator. The results are stated separately because the triangle assumption cannot be removed by the four-cycle proof.

The main rank theorem gives the following sharp universal statement. For a $d$-state positive Markov four-cycle, the three quartet flattening ranks are 

$$
d^2,\qquad d^2,\qquad r\ge \frac{d(d+1)}2.
$$

 The third rank can equal its lower bound, so replacing it by $d^2$ would be false. The proof uses a determinant factorization for the first two splits and a filtration of the transformed row space for the third. Since a mixture of $m$ GM components on one tree topology has rank at most $md$ at that topology’s split, the theorem excludes every such mixture when $m\le\lfloor d/2\rfloor$. For $d=4$, all three network ranks are at least 10, whereas a two-component single-topology mixture has one rank at most 8. This conclusion permits unrelated parameters in the competing mixture’s components.

The reversible triangle theorem treats every possible spectrum of the shared generator. A matrix logarithm identifies the competing tree’s generator up to scale. If there are two distinct nonzero decay rates, strict concavity of a two-route log mixture produces a contradiction. If all nonzero rates coincide, the generator is an equal-input generator; a centered third moment then separates the models. This second case is necessary for an all-parameter assertion. The argument works for every positive stationary distribution with at least three states. It also works for two states unless their frequencies are equal. We classify that last case explicitly and exhibit a positive triangle whose entire tensor equals that of a positive tree.

### 1.1 Relation to previous results

The use of flattening ranks is established in mathematical phylogenetics. Casanellas and Fernández-Sánchez give GM tree-clade rank constraints on networks [\[3\]](#ref-CFS2021), and develop the corresponding equivariant framework [\[4\]](#ref-CFS2025). Snyman, Fox and Bryant prove an all-parameter tree rank formula under positivity and nonsingularity assumptions, with explicit rerooting and restriction arguments [\[13\]](#ref-Snyman2023). Sullivant gives universal network rank upper bounds and generic lower bounds obtained from displayed-tree boundary points [\[14, Theorems 7.8 and 7.11\]](#ref-Sullivant2026). The lower-bound argument uses semicontinuity, so it does not itself exclude positive exceptional parameters. A related five-author theorem, publicly announced in 2025, likewise states a generic network lower bound [\[15, slide 23\]](#ref-SullivantIMSI2025). We compare that public statement; the complete manuscript of the announced collaboration was unavailable.

All-parameter separation already occurs in more restricted substitution models. Englander and coauthors obtain a Jukes–Cantor trinet inequality [\[8, Proposition 2.26\]](#ref-Englander2025); Currie and coauthors reproduce it and describe the semialgebraic JC triangle model [\[6, Theorem 3.1 and Appendix A\]](#ref-Currie2026). Brits and coauthors prove full results, modulo triangle orientation, for level-1 networks under JC, K2P and K3P, together with a broader JC tree–network theorem excluding 2-blobs [\[2\]](#ref-Brits2026). Generic identifiability of triangle-free level-1 networks under these group-based models provides an earlier baseline [\[9, Theorem 2\]](#ref-Gross2021).

Our equal-input calculation specializes exactly to the known JC obstruction. We do not claim a new JC invariant. The triangle contribution is the extension to nonuniform equal-input frequencies and its combination with the exhaustive shared-generator spectral argument. Equal-input models with arbitrary state spaces and frequencies are themselves well established [\[5\]](#ref-CasanellasSteel2017). Likewise, the binary classification uses the standard CFN tripod moment inversion [\[10\]](#ref-Hill2024).

For mixture comparisons, Allman, Rhodes and Sullivant already show that a limited number of same-topology continuous-time components cannot mimic an unmixed different tree, subject to its refinement qualification, and obtain stronger arbitrary-class conclusions under JC and K2P [\[1, Theorems 1 and 3\]](#ref-ARS2012). The bound $md$ on a single-topology mixture flattening is therefore an established tool. The additional ingredient here is the universal GM four-cycle lower bound. The JC/K2P specialization of the mixture conclusion is covered more strongly by the earlier linear-test result.

Table [1](#tab:comparison) summarizes the closest comparisons. These comparisons concern hypotheses and quantifiers; they do not assert priority relative to unavailable work.

<div id="tab:comparison">

| Result | Model and scope | Relation to the present result |
|:---|:---|:---|
| Englander et al.; Currie et al. [\[8\]](#ref-Englander2025), [\[6\]](#ref-Currie2026) | Universal JC triangle/trinet obstruction; semialgebraic triangle analysis | Exact precedent for the uniform four-state moment identity. |
| Brits et al. [\[2\]](#ref-Brits2026) | Full level-1 results modulo triangle orientation for JC/K2P/K3P; broader JC separation excluding 2-blobs | Different substitution assumptions; includes more network topologies. |
| Casanellas–Fernández-Sánchez [\[3\]](#ref-CFS2021), [\[4\]](#ref-CFS2025) | Universal GM and equivariant tree-clade rank upper bounds | Does not supply the positive four-cycle lower bound. |
| Sullivant and announced collaboration [\[14\]](#ref-Sullivant2026), [\[15\]](#ref-SullivantIMSI2025) | Universal cut upper bounds and generic network lower bounds | Does not rule out positive exceptional rank loss. |
| Snyman–Fox–Bryant [\[13\]](#ref-Snyman2023) | Universal positive nonsingular GM tree rank theorem | Supplies established tree-rank and rerooting mechanisms. |
| Allman–Rhodes–Sullivant [\[1\]](#ref-ARS2012) | Universal limited-class mixture versus unmixed-tree results with a refinement qualification; stronger JC/K2P results | Rank subadditivity is known; the GM network lower bound is the extra input. |
| Theorem [3.1](#thm:rank) | Positive invertible GM four-cycle, every $d\ge2$ | Sharp universal crossed rank $d(d+1)/2$ and bounded-mixture exclusion. |
| Theorems [5.2](#thm:triangle) and [7.1](#thm:triangle-closure) | Shared stationary reversible generator; $d\ge3$, or nonuniform binary frequencies | Separation from the whole competing tree closure, including repeated spectra. |

Theorem-level comparison. “Universal” always refers to the stated parameter domain.

</div>

<a id="sec:models"></a>

## 2 Models and elementary rank facts

All state spaces are $[d]=\{1,\ldots,d\}$ with $d\ge2$. A stochastic matrix is row-stochastic. A *positive* matrix has every entry strictly positive, and *invertible* always means invertible as a real matrix. A probability vector is written as a column; its transpose is used for row-vector propagation. All trees and networks here are finite; each reticulation has exactly two incoming edges. The GM model on a rooted tree assigns a probability vector to the root and a stochastic matrix to each directed edge. The joint law is the root probability multiplied by the edge transition probabilities, and a leaf tensor is obtained by summing over internal states.

<div class="definition">

**Definition 2.1** (Displayed-tree mixture). At a reticulation with parents $u,v$, choose the incoming edge from $u$ with probability $\gamma$ and that from $v$ with probability $\delta=1-\gamma$. Conditional on the choice, the character evolves on the retained tree. All edges common to the displayed trees retain the same matrices. Throughout the separation results $0<\gamma<1$.

</div>

The corresponding conditional factor at the reticulation is $\gamma U_{jl}+\delta V_{kl}$, where $j,k$ are its parental states and $l$ is its own state. Thus the displayed-tree model can also be written as a DAG model with a constrained conditional distribution [\[14\]](#ref-Sullivant2026). We do not incorporate a coalescent process.

<div class="definition">

**Definition 2.2** (Observable cycle attachment). For a network with one underlying undirected cycle, delete the cycle edges. A component attached to a cycle vertex is observable if it contains an observed leaf. The attachment below the reticulation is required to be observable. Suppressing unused degree-two cycle vertices gives its reduced cycle. A triangle has three retained attachment vertices; a four-cycle has four.

</div>

For a four-leaf tensor $P=(P_{ijkl})$, its flattening $F_{ij\mid kl}(P)$ is the $d^2\times d^2$ matrix with row index $(i,j)$, column index $(k,l)$ and entry $P_{ijkl}$, using lexicographic order. The other two flattenings are defined similarly. Flattening preserves the Euclidean norm of all tensor entries as the Frobenius matrix norm.

<div id="lem:tree-rank" class="lemma">

**Lemma 2.3** (Tree rank and leaf actions). A $d$-state GM quartet tree has a flattening of rank at most $d$ at its internal split. A star tree has this bound at all three splits. A mixture of $m$ GM distributions on one quartet topology has rank at most $md$ at that topology’s split. Applying invertible stochastic channels to the four leaves preserves all three flattening ranks.

</div>

<div class="proof">

*Proof.* Cutting an internal tree edge and conditioning on its endpoint states factors the corresponding flattening as $L^T D_p M R$, where $L,R$ are conditional leaf-pattern matrices and the middle factors are $d\times d$. Its rank is at most $d$. A central-state conditioning gives the star-tree assertion. The mixture statement follows by rank subadditivity, with no equality of numerical parameters required between components. These are standard flattening facts; see, for example, [\[3\]](#ref-CFS2021), [\[1\]](#ref-ARS2012), [\[13\]](#ref-Snyman2023).

For leaf channels $E_1,\ldots,E_4$, the first flattening transforms as 

$$
F_{12\mid34}(P')=(E_1^T\otimes E_2^T)
                       F_{12\mid34}(P)(E_3\otimes E_4).
$$

 Both multiplying matrices are invertible, as are their analogues for the other splits. Their inverses need not be stochastic. ◻

</div>

A continuous-time generator $Q$ satisfies $Q\mathbf 1=0$ and has nonnegative off-diagonal entries. It is irreducible when its directed rate graph is strongly connected. If $Q$ is irreducible, $e^{tQ}$ is positive and invertible for each finite $t>0$. Reversibility with respect to a positive probability vector $\pi$ means $D Q=Q^T D$, where $D=\mathop{\mathrm{diag}}\pi$. Then $H=D^{1/2}QD^{-1/2}$ is symmetric. Stationarity means the root law is $\pi$. A *homogeneous stationary reversible model* uses one such generator throughout an object, with edge-specific times that are finite nonnegative real numbers. Cycle-edge times are strictly positive where stated. For $d=4$ this is the usual shared-generator GTR setting. The GM rank results below require none of these additional generator restrictions.

<a id="sec:rank"></a>

## 3 A sharp universal four-cycle rank bound

Place the middle ordinary vertex at $i$, the parental vertices at $j,k$, and the reticulation at $l$. The cycle is $i-j-l-k-i$. Its core tensor is 

<a id="eq:core"></a>

$$
C_{ijkl}=p_iS_{ij}T_{ik}\bigl(\gamma U_{jl}+\delta V_{kl}\bigr),
 \qquad\delta=1-\gamma.
\tag{1}
$$

 Conditional on $i$, the two parental states evolve independently through $S,T$. The reticulation then chooses one of $U,V$. Four pendant channels map the core states to the observed leaves.

<div id="thm:rank" class="theorem">

**Theorem 3.1** (Sharp positive Markov four-cycle ranks). Let $p$ be strictly positive, let $S,T,U,V$ be positive invertible $d\times d$ stochastic matrices, and let $0<\gamma<1$. Apply any four invertible stochastic pendant channels to [(1)](#eq:core), obtaining $P$. Then 

<a id="eq:adjacent-ranks"></a>

<a id="eq:crossed-rank"></a>

$$
\begin{aligned}
 \mathop{\mathrm{rank}}F_{ij\mid kl}(P)&=d^2,\qquad
 \mathop{\mathrm{rank}}F_{ik\mid jl}(P)=d^2,\\
 \frac{d(d+1)}2\ &\le\mathop{\mathrm{rank}}F_{il\mid jk}(P)\le d^2.
 
\end{aligned}
\tag{2, 3}
$$

 The lower bound in [(3)](#eq:crossed-rank) is attained for every $d\ge2$, even by positive continuous-time reversible channels.

</div>

<div class="proof">

*Proof.* Lemma [2.3](#lem:tree-rank) allows us to work with $C$. For the first flattening let $D_0=\mathop{\mathrm{diag}}(p_iS_{ij})$, with diagonal index $(i,j)$. For $1\le k\le d$ let $R_k=\mathbf 1V_{k\cdot}$, a $d\times d$ matrix all of whose rows are row $k$ of $V$. Direct entrywise multiplication gives 

<a id="eq:det-factor"></a>

$$
F_{ij\mid kl}(C)=D_0(T\otimes U)
                 \left[\gamma I_{d^2}+
                       \delta\mathop{\mathrm{diag}}(R_1,\ldots,R_d)\right].
\tag{4}
$$

 Indeed the first term has entry $p_iS_{ij}T_{ik}\gamma U_{jl}$. For the second term, $U\mathbf 1=\mathbf 1$ makes its entry $p_iS_{ij}T_{ik}\delta V_{kl}$. Since $V_{k\cdot}\mathbf 1=1$, $R_k$ is a rank-one idempotent. Each block $\gamma I_d+\delta R_k$ has eigenvalue $\gamma+\delta=1$ once and eigenvalue $\gamma$ with multiplicity $d-1$. Hence 

<a id="eq:first-determinant"></a>

$$
\det F_{ij\mid kl}(C)=
 \left(\prod_{i,j}p_iS_{ij}\right)
 (\det T)^d(\det U)^d\gamma^{d(d-1)}\ne0.
\tag{5}
$$

 Exchanging the two parents yields 

<a id="eq:second-determinant"></a>

$$
\det F_{ik\mid jl}(C)=
 \left(\prod_{i,k}p_iT_{ik}\right)
 (\det S)^d(\det V)^d\delta^{d(d-1)}\ne0.
\tag{6}
$$

 These formulas use the stated lexicographic index orders.

For the crossed split, view row $(i,l)$ as a matrix in indices $(j,k)$. Apply to every row matrix the same invertible linear map 

$$
\mathcal L(M)=S^{-T}MT^{-1}.
$$

 Let $e_i$ denote coordinate vector $i$ and define 

<a id="eq:AiBi"></a>

$$
A_i=S^{-T}\mathop{\mathrm{diag}}(S_{i1},\ldots,S_{id})U,
 \qquad B_i=T^{-T}\mathop{\mathrm{diag}}(T_{i1},\ldots,T_{id})V.
\tag{7}
$$

 The transformed row is 

<a id="eq:row-star"></a>

$$
R_{il}=p_i\{\gamma A_i[:,l]e_i^T+
                   \delta e_iB_i[:,l]^T\}.
\tag{8}
$$

 In particular it is supported on row $i$ or column $i$. Every $A_i$ is invertible: all entries in row $i$ of $S$ are nonzero. Row-stochasticity gives $A_i\mathbf 1=B_i\mathbf 1=e_i$, so 

<a id="eq:diagonal-aggregate"></a>

$$
\sum_l R_{il}=p_i e_ie_i^T.
\tag{9}
$$

 Thus the full diagonal subspace $\mathcal D$, of dimension $d$, lies in the transformed row space.

Put $\mathcal V_i=\operatorname{span}\{R_{il}:l\in[d]\}$ and 

$$
\mathcal W_0=\mathcal D,\qquad
 \mathcal W_i=\mathcal D+\mathcal V_1+\cdots+\mathcal V_i.
$$

 For $1\le i\le d-1$, project onto the entries $(h,i)$ with $h>i$. This projection annihilates $\mathcal W_{i-1}$: diagonal matrices vanish there, and every earlier family $r<i$ is supported only on row $r$ or column $r$. Its image on $\mathcal V_i$ has dimension $d-i$. In fact [(8)](#eq:row-star) shows that the image matrix is precisely the $h>i$ row submatrix of $p_i\gamma A_i$, which has full row rank because $A_i$ is invertible. Therefore 

$$
\dim\mathcal W_i\ge\dim\mathcal W_{i-1}+d-i.
$$

 Summing gives 

$$
\mathop{\mathrm{rank}}F_{il\mid jk}(C)\ge\dim\mathcal W_{d-1}
 \ge d+\sum_{i=1}^{d-1}(d-i)=\frac{d(d+1)}2.
$$

 The upper bound is the matrix size.

For sharpness take $T=S$, $V=U$ and $\gamma=\delta=1/2$. Then [(1)](#eq:core) is unchanged by interchanging $j$ and $k$. The crossed columns $(j,k)$ and $(k,j)$ agree, leaving at most $d(d+1)/2$ distinct columns. The lower bound forces equality. For example, with uniform $p$ one can use 

<a id="eq:sharp-example"></a>

$$
S=T=U=V=(1-\epsilon)I+\epsilon\mathbf 1\mathbf 1^T/d,
 \qquad 0<\epsilon<1.
\tag{10}
$$

 These are positive finite-time transitions of a symmetric irreducible generator. Positive invertible pendant channels may be added freely. ◻

</div>

<div class="remark">

Remark 3.2. The crossed rank is generically $d^2$: at an inheritance endpoint the core reduces to a tree, and its crossed flattening is full rank under the stated positive channels; continuity of its determinant preserves this rank for nearby interior weights. This observation agrees with the generic lower-bound mechanism in [\[14\]](#ref-Sullivant2026). It does not replace the universal lower bound. We make no assertion that every integer between $d(d+1)/2$ and $d^2$ occurs.

</div>

<div id="cor:mixture" class="corollary">

**Corollary 3.3** (Exclusion of bounded single-topology mixtures). A tensor in Theorem [3.1](#thm:rank) cannot be a mixture of at most $\lfloor d/2\rfloor$ $d$-state GM components sharing any one quartet tree topology. Components may have independent numerical parameters and root distributions, including degenerate stochastic parameters.

</div>

<div class="proof">

*Proof.* Such an $m$-component mixture has a split of rank at most $md$ by Lemma [2.3](#lem:tree-rank), whereas every network split has rank at least $d(d+1)/2>md$. A star is covered by the same lemma. Nonbinary topologies can also be resolved by identity channels. ◻

</div>

The common-topology qualification is essential. The four-cycle itself is a two-component mixture of different displayed topologies. The corollary is therefore not a claim against arbitrary two-tree mixtures.

<a id="sec:gm-large"></a>

## 4 Reduction of larger general-Markov networks

We next lift the four-cycle theorem without imposing reversibility. The underlying rerooting operation is standard [\[13, Proposition 6\]](#ref-Snyman2023); the issue to check is that it is performed on a common backbone law and therefore preserves the shared-edge mixture structure.

<div id="lem:gm-reduction" class="lemma">

**Lemma 4.1** (Four-attachment reduction). Let $N$ be a rooted network with exactly one reticulation and one underlying cycle. Assume a positive root distribution, positive invertible stochastic edge matrices and interior inheritance probability. Suppose at least four cycle-attachment components are observable, including the component below the reticulation. Then a four-leaf marginal of its distribution has the form of Theorem [3.1](#thm:rank).

</div>

<div class="proof">

*Proof.* Let $h$ be the reticulation and delete its two incoming edges. The component containing the original root is a Markov tree, the *backbone*, whose law is identical under both inheritance choices. The other component is a descendant tree rooted at $h$. Select one leaf there and one leaf in each of three distinct ordinary cycle attachments. Deleting $h$ from the cycle leaves a path in the backbone. Write the three selected attachment vertices as $j,i,k$ in their path order, with $i$ the middle vertex.

Reroot the backbone at $i$. For completeness, an edge $u\to v$ with transition $M$ and positive marginal vectors $p_u,p_v$, where $p_v^T=p_u^TM$, reverses to 

<a id="eq:bayes-reverse"></a>

$$
M^{\mathrm{rev}}=D_{p_v}^{-1}M^TD_{p_u}.
\tag{11}
$$

 It is positive, stochastic and invertible, and $D_{p_u}M=(D_{p_v}M^{\mathrm{rev}})^T$ preserves the edge joint law. Successive reversals preserve the whole backbone distribution. No incoming reticulation edge is reversed, and the backbone is rerooted only once, before multiplying by its unchanged reticulation conditional factor.

Marginalize branches containing no chosen leaf and contract degree-two paths. Products of positive invertible stochastic matrices retain all three properties. The paths from $i$ to $j,k$ give $S,T$. Continue from $j$ along its remaining cycle arm to its parental endpoint and then into $h$; its product gives $U$. The other arm gives $V$. The selected leaf paths give four invertible pendant channels. The resulting core law is exactly [(1)](#eq:core), with a positive marginal distribution at $i$. Both parental routes remain and the inheritance weight is unchanged. ◻

</div>

<div id="thm:gm-network" class="theorem">

**Theorem 4.2** (Arbitrary-taxon GM separation). A network satisfying Lemma [4.1](#lem:gm-reduction) cannot equal a mixture of at most $\lfloor d/2\rfloor$ $d$-state GM components sharing one tree topology on its full observed leaf set. In particular it cannot equal any single GM tree distribution.

</div>

<div class="proof">

*Proof.* Equality of full distributions implies equality of the four-leaf marginals selected by the lemma. Restricting each component of a fixed tree topology produces GM distributions on the same induced quartet topology, although their numerical parameters may differ. Corollary [3.3](#cor:mixture) gives a contradiction. ◻

</div>

<div class="remark">

Remark 4.3 (Several reticulations). The preceding proof is for one reticulation. Pruning another cycle can produce a convex combination of path matrices, which need not be invertible even if both matrices are positive and invertible. For example 

$$
A=\begin{pmatrix}3/4&1/4\\1/4&3/4\end{pmatrix},\qquad
 B=\begin{pmatrix}1/4&3/4\\3/4&1/4\end{pmatrix}
$$

 have this property, whereas $(A+B)/2$ has rank one. This is an obstruction to that automatic reduction argument, not a claimed counterexample to every possible multiple-cycle theorem.

</div>

<a id="sec:triangle"></a>

## 5 Homogeneous reversible triangles

For the remainder of the triangle argument fix a positive probability vector $\pi$ and an irreducible generator $Q$ reversible with respect to $\pi$. The same $Q$ acts on every network edge. Let $a,b,c>0$ and $0<\gamma<1$. The triangle core is 

<a id="eq:triangle-core"></a>

$$
P^0_{ijl}=\pi_i(e^{aQ})_{ij}
       \{\gamma(e^{bQ})_{il}+\delta(e^{cQ})_{jl}\}.
\tag{12}
$$

 Attach pendant transitions $e^{xQ},e^{yQ},e^{zQ}$, where $x,y,z\ge0$ are finite. Allowing zero pendant times strengthens the statement; the ordinary cycle time $a$ and the two parental route times remain positive. All one-leaf marginals equal $\pi$.

A competing homogeneous stationary reversible tree may choose its own positive stationary distribution, irreducible generator and finite nonnegative lengths. By reversibility it can be rooted at the central vertex of its induced three-leaf tree.

<div id="lem:generator" class="lemma">

**Lemma 5.1** (Identification of a competing generator). If the triangle tensor equals a homogeneous stationary reversible tree tensor, then the two generators are positive scale multiples of each other. The scale can be absorbed into the tree lengths.

</div>

<div class="proof">

*Proof.* One-leaf marginals force the tree stationary distribution to be $\pi$. Write $D=\mathop{\mathrm{diag}}\pi$ and $L=x+a+y>0$. The unaffected pair has joint matrix $De^{LQ}$. For a competing generator $Q'$ and tree path length $L'$, equality implies 

$$
e^{LQ}=e^{L'Q'}.
$$

 The left side is positive and is not the identity, so $L'>0$. Conjugating by $D^{1/2}$ produces exponentials of real symmetric matrices. Their common value is symmetric positive definite and has a unique real symmetric logarithm. Hence $LQ=L'Q'$. This argument requires no simple spectrum and asserts uniqueness only within real symmetric logarithms. ◻

</div>

<div id="thm:triangle" class="theorem">

**Theorem 5.2** (All-parameter reversible triangle separation). The tensor defined by [(12)](#eq:triangle-core) and its pendant channels cannot equal any homogeneous stationary reversible tree tensor if either

1.  $d\ge3$; or

2.  $d=2$ and $\pi\ne(1/2,1/2)$.

The competing tree may initially choose its own generator and stationary distribution, and may have finite nonnegative edge lengths.

</div>

<div class="proof">

*Proof.* By Lemma [5.1](#lem:generator), it suffices to compare a tree using $Q$. The symmetric conjugate of $Q$ has one zero eigenvalue and $d-1$ strictly negative eigenvalues. Write the nonzero decay rates as positive numbers. We treat their exhaustive dichotomy.

*At least two distinct decay rates.* For a decay rate $t>0$, the first hybrid-involving pair has an attenuation factor $e^{-(x+z)t}(\gamma e^{-tb}+\delta e^{-t(a+c)})$. A single tree path would require the same effective extra length 

<a id="eq:effective-length"></a>

$$
F(t)=-\frac1t\log(\gamma e^{-tb}+\delta e^{-t(a+c)})
\tag{13}
$$

 at every nonzero decay rate. Put $h(t)=tF(t)$. It has $h(0)=0$, and when $b\ne a+c$, 

<a id="eq:strict-concavity"></a>

$$
h''(t)=-\frac{\gamma\delta(b-a-c)^2e^{-t(b+a+c)}}
 {\{\gamma e^{-tb}+\delta e^{-t(a+c)}\}^2}<0.
\tag{14}
$$

 For $0<r<s$, strict concavity at $r=(r/s)s+(1-r/s)0$ gives $h(r)/r>h(s)/s$. Thus equality with a tree forces $b=a+c$. Applying the same argument to the other hybrid-involving pair forces $a+b=c$. Together these imply $a=0$, a contradiction. Repeated eigenvalues other than the two chosen distinct values cause no problem.

*One common nonzero decay rate.* Suppose all nonzero eigenvalues equal $-\lambda$, with $\lambda>0$. The reversible spectral decomposition and the one-dimensional stationary eigenspace give 

<a id="eq:equal-input"></a>

$$
Q=\lambda(\mathbf 1\pi^T-I).
\tag{15}
$$

 This is the established equal-input model, known as F81 for four states [\[5\]](#ref-CasanellasSteel2017). Every centered state function is an eigenfunction with attenuation $e^{-\lambda t}$.

Under either hypothesis of the theorem, choose a state $m$ with $\pi_m\ne1/2$. For $d\ge3$ a state of minimum frequency suffices. Define 

<a id="eq:contrast"></a>

$$
\phi(i)=\frac{\mathbf1_{\{i=m\}}-\pi_m}
                  {\sqrt{\pi_m(1-\pi_m)}},\qquad
 \kappa=\mathbb E_\pi\phi^3=
       \frac{1-2\pi_m}{\sqrt{\pi_m(1-\pi_m)}}\ne0.
\tag{16}
$$

 Then $\mathbb E_\pi\phi=0$ and $\mathbb E_\pi\phi^2=1$. Write 

$$
A=e^{-\lambda a},\quad B=e^{-\lambda b},\quad C=e^{-\lambda c},
 \qquad X=e^{-\lambda x},\quad Y=e^{-\lambda y},\quad Z=e^{-\lambda z}.
$$

 For observed leaves $L_1,L_2,L_3$, put $M_{rs}=\mathbb E[\phi(L_r)\phi(L_s)]$ and $W=\mathbb E[\phi(L_1)\phi(L_2)\phi(L_3)]$. Conditional expectations along an edge multiply a centered function by its attenuation. This gives 

<a id="eq:triangle-pairs"></a>

<a id="eq:triangle-third"></a>

$$
\begin{aligned}
 M_{12}&=XYA, &
 M_{13}&=XZ(\gamma B+\delta AC), &
 M_{23}&=YZ(\gamma AB+\delta C),\\
 W&=XYZ\kappa A(\gamma B+\delta C).&&&
\end{aligned}
\tag{17, 18}
$$

 To check the third moment directly, under the first inheritance choice root the core at $i$. Conditional independence gives $\mathbb E[\phi(i)\phi(j)\phi(l)]=AB\mathbb E_\pi\phi^3$. Under the second choice reroot at $j$ by reversibility, giving $AC\kappa$. Mixing and multiplying the three pendant factors proves [(18)](#eq:triangle-third).

On an equal-input tree with pendant attenuation factors $u,v,w$, conditioning on the central state instead gives 

$$
M_{12}=uv,\qquad M_{13}=uw,\qquad M_{23}=vw,
 \qquad W=\kappa uvw.
$$

 Therefore every such tree satisfies $W^2/\kappa^2=M_{12}M_{13}M_{23}$, including when an edge is zero. For the triangle, substitution and expansion give 

<a id="eq:defect"></a>

$$
\begin{aligned}
 \frac{W^2}{\kappa^2}-M_{12}M_{13}M_{23}
 &=(XYZ)^2\bigl[A^2(\gamma B+\delta C)^2
  -A(\gamma B+\delta AC)(\gamma AB+\delta C)\bigr]\\
 &=-(XYZ)^2 A\gamma\delta BC(1-A)^2<0.
\end{aligned}
\tag{19}
$$

 Here all displayed factors are positive and $A<1$. This contradiction completes the proof. ◻

</div>

### The known JC specialization

For uniform four-state frequencies, [(19)](#eq:defect) is the known JC triangle obstruction of Englander et al. and Currie et al. [\[8\]](#ref-Englander2025), [\[6\]](#ref-Currie2026). The equivalence can be stated explicitly. Relabel Currie’s hybrid leaf 1 as our leaf 3, and their leaves 2,3 as our leaves 1,2. In their absorbed Appendix A parameters set 

$$
a_2=X,\qquad a_3=Y,\qquad a_5=A,\qquad
 a_4=Z\gamma B,\qquad a_6=Z\delta C.
$$

 Their Fourier coordinates $(q_{ACC},q_{CAC},q_{CCA},q_{CGT})$ become $(M_{12},M_{23},M_{13},W/\kappa)$ in this specialization. Their positive factorization is exactly the negative of [(19)](#eq:defect). Relabelling and sign reversal do not yield a new identity. The present use of a nonuniform contrast and the preceding spectral case have different hypotheses from that known specialization.

<div id="lem:triangle-reduction" class="lemma">

**Lemma 5.3** (Three-attachment reversible reduction). A homogeneous stationary reversible single-reticulation network with at least three observable cycle attachments, including the hybrid attachment, and positive finite cycle lengths has a triangle marginal of the form [(12)](#eq:triangle-core) with $a,b,c>0$ and unchanged interior inheritance.

</div>

<div class="proof">

*Proof.* Select one leaf below the reticulation and one in each of two other observable attachments. Marginalization commutes with the two-term mixture. Remove unused subtrees and suppress degree-two paths, using $e^{sQ}e^{tQ}=e^{(s+t)Q}$. If suppression passes through a split vertex, stationary reversibility gives the fork identity 

<a id="eq:fork"></a>

$$
\sum_i\pi_i(e^{sQ})_{ij}(e^{tQ})_{ik}
       =\pi_j(e^{(s+t)Q})_{jk}.
\tag{20}
$$

 Indeed detailed balance changes $\pi_i(e^{sQ})_{ij}$ to $\pi_j(e^{sQ})_{ji}$, after which matrix multiplication gives the right side. Distinct retained attachments leave three nonempty cycle paths, hence positive summed lengths. Both routes into the hybrid attachment remain. The selected leaf paths give the pendant lengths, and the weight is unchanged. ◻

</div>

<div id="cor:reversible-large" class="corollary">

**Corollary 5.4**. Theorem [5.2](#thm:triangle) applies to homogeneous stationary reversible single-reticulation networks on any number of observed taxa satisfying Lemma [5.3](#lem:triangle-reduction). For $d=4$ this gives the specified all-parameter GTR tree–network separation with three or more observable cycle attachments.

</div>

<div class="proof">

*Proof.* An equality with a full tree distribution would imply equality of the selected three-leaf marginals. The induced tree remains homogeneous, stationary and reversible, so Theorem [5.2](#thm:triangle) excludes it. ◻

</div>

<a id="sec:binary"></a>

## 6 The binary symmetric boundary

The state-space qualification in Theorem [5.2](#thm:triangle) is substantive. When $d=2$ and $\pi=(1/2,1/2)$, every centered contrast has zero third moment. All irreducible reversible generators with that stationary law are positive scale multiples of the binary symmetric generator. The following result substitutes the network’s moments into the established CFN tripod geometry [\[10\]](#ref-Hill2024).

<div id="prop:binary" class="proposition">

**Proposition 6.1** (Exact binary symmetric criterion). In the triangle model with $d=2$ and uniform frequencies, use the attenuations defined above and put 

$$
q=\gamma B+\delta AC,\qquad r=\gamma AB+\delta C.
$$

 The triangle tensor equals a finite positive-length homogeneous stationary reversible tree tensor if and only if 

<a id="eq:binary-criterion"></a>

$$
Z^2qr<A.
\tag{21}
$$

 The unique positive tree attenuation factors are 

<a id="eq:binary-inverse"></a>

$$
u=X\sqrt{Aq/r},\qquad v=Y\sqrt{Ar/q},\qquad
 w=Z\sqrt{qr/A}.
\tag{22}
$$

 If $Z^2qr=A$, a finite nonnegative-length tree matches, with its third edge of length zero. If $Z^2qr>A$, no finite nonnegative-length tree matches.

</div>

<div class="proof">

*Proof.* Encode states by spins $\sigma_i\in\{-1,1\}$. Simultaneous sign-reversal symmetry makes every odd moment zero. Fourier inversion on the three-spin cube gives 

<a id="eq:binary-fourier"></a>

$$
P(\sigma_1,\sigma_2,\sigma_3)=\frac18
 \{1+\sigma_1\sigma_2M_{12}+\sigma_1\sigma_3M_{13}
                         +\sigma_2\sigma_3M_{23}\}.
\tag{23}
$$

 Thus the three pair moments determine the whole tensor. They are $XYA,XZq,YZr$. A tree must satisfy $uv=XYA$, $uw=XZq$, $vw=YZr$, whose unique positive solution is [(22)](#eq:binary-inverse).

The first two factors are strictly below one because 

$$
r-Aq=\delta C(1-A^2)>0,\qquad
 q-Ar=\gamma B(1-A^2)>0,
$$

 and $0<X,Y\le1$. All three factors are positive. Positive finite tree lengths are therefore equivalent to $w<1$, giving [(21)](#eq:binary-criterion). Allowing zero lengths replaces $<$ by $\le$. One-leaf marginals exclude a competing nonuniform stationary law, and the generator scale is absorbed into these factors. ◻

</div>

For an exact positive example choose 

$$
\gamma=\delta=\tfrac12,\qquad A=\tfrac14,
 \qquad B=C=X=Y=Z=\tfrac12.
$$

 Then $q=r=5/16$ and the pair moments are $(1/16,5/64,5/64)$. The matching tree factors are $(u,v,w)=(1/4,1/4,5/16)$, all strictly below one. At decay rate one the network lengths are $(\log4,\log2,\log2,\log2,\log2,\log2)$, while the tree lengths are $(\log4,\log4,\log(16/5))$. The entire common tensor is 

$$
P(+++) = P(---)=39/256,\qquad
 P(++-) = P(--+)=29/256,
$$

 with each remaining pattern equal to $30/256$. This example concerns a triangle. The GM four-cycle rank theorem applies even when $d=2$.

<a id="sec:closure"></a>

## 7 Separation from the full reversible tree closure

Let $\mathcal T_d$ be the set of three-leaf distributions generated by a homogeneous irreducible reversible generator at stationarity, with a positive stationary distribution and finite positive tree lengths. Each competing tree may choose all these parameters independently. Write $\overline{\mathcal T_d}$ for its Euclidean closure in the $d^3$-pattern probability simplex. In particular, this closure allows sequences with changing generators, changing stationary distributions, unbounded lengths and vanishing edges.

<div id="thm:triangle-closure" class="theorem">

**Theorem 7.1** (Triangle exclusion from tree closure). Every triangle tensor satisfying either state-space hypothesis of Theorem [5.2](#thm:triangle) lies outside $\overline{\mathcal T_d}$.

</div>

<div class="proof">

*Proof.* Suppose tree tensors $P_n\in\mathcal T_d$ converge to the triangle tensor $P$. Their common leaf marginals $\pi_n$ converge to $\pi>0$. Put $D_n=\mathop{\mathrm{diag}}\pi_n$, $D=\mathop{\mathrm{diag}}\pi$, and let $J_{rs,n},J_{rs}$ be the pair joint-distribution matrices. Define 

$$
S_{rs,n}=D_n^{-1/2}J_{rs,n}D_n^{-1/2},\qquad
 S_{rs}=D^{-1/2}J_{rs}D^{-1/2}.
$$

 These converge pairwise. With $H=D^{1/2}QD^{-1/2}$, the triangle’s normalized matrices are 

<a id="eq:pair-spd"></a>

$$
\begin{aligned}
 S_{12}&=e^{(x+a+y)H},\\
 S_{13}&=e^{(x+z)H}\{\gamma e^{bH}+\delta e^{(a+c)H}\},\\
 S_{23}&=e^{(y+z)H}\{\gamma e^{(a+b)H}+\delta e^{cH}\}.
\end{aligned}
\tag{24}
$$

 Each is symmetric positive definite. Its eigenvalue on $\sqrt\pi$ is one, and every other eigenvalue lies strictly between zero and one. Thus the symmetric logarithms 

$$
A_{rs}=-\log S_{rs},\qquad t_{rs}=\mathop{\mathrm{tr}}A_{rs}>0
$$

 are finite. Continuity of this logarithm on the positive definite cone gives $A_{rs,n}\to A_{rs}$ and $t_{rs,n}\to t_{rs}$.

Write the symmetric generator of tree $n$ as $H_n=D_n^{1/2}Q_nD_n^{-1/2}$ and its three central pendant lengths as $\ell_{1,n},\ell_{2,n},\ell_{3,n}>0$. Then 

$$
A_{rs,n}=-(\ell_{r,n}+\ell_{s,n})H_n.
$$

 Normalize through the unaffected pair: 

<a id="eq:normalized-generator"></a>

$$
B_n=\frac{A_{12,n}}{t_{12,n}}
 =\frac{-H_n}{-\mathop{\mathrm{tr}}H_n}
 \longrightarrow B=\frac{A_{12}}{t_{12}}
 =\frac{-H}{-\mathop{\mathrm{tr}}H}.
\tag{25}
$$

 This step absorbs arbitrary generator and length scales; no bound on $Q_n$ is assumed. Define 

$$
s_{1,n}=\tfrac12(t_{12,n}+t_{13,n}-t_{23,n})
$$

 and cyclically define $s_{2,n},s_{3,n}$. They equal $(-\mathop{\mathrm{tr}}H_n)\ell_{r,n}>0$ and converge to finite values $s_r\ge0$. The tree edge channels consequently converge to 

<a id="eq:limit-channels"></a>

$$
E_r=D^{-1/2}e^{-s_r B}D^{1/2}
     =e^{\{s_r/(-\mathop{\mathrm{tr}}Q)\}Q}.
\tag{26}
$$

 The root distribution converges to $\pi$. The finite sum over the central state is continuous, so the limiting tree tensor is exactly the tree with generator $Q$, root law $\pi$ and the finite nonnegative lengths in [(26)](#eq:limit-channels). This contradicts Theorem [5.2](#thm:triangle). ◻

</div>

The same closure exclusion holds for a larger single-reticulation network with a triangle marginal satisfying the theorem. A convergent sequence of full tree tensors would induce a convergent sequence of their three-leaf tree marginals, contradicting Theorem [7.1](#thm:triangle-closure).

<div id="cor:compact" class="corollary">

**Corollary 7.2** (Uniform margins on compact network domains). Let $K$ be any nonempty compact set of triangle parameter tuples satisfying Theorem [5.2](#thm:triangle). In the binary case, require every tuple to have nonuniform stationary frequencies. Then 

$$
\epsilon_K=\min_{\theta\in K}\min_{T\in\overline{\mathcal T_d}}
                \mathop{\mathrm{TV}}(P_\theta,T)>0,
 \qquad \mathop{\mathrm{TV}}(p,q)=\tfrac12\sum_\omega|p_\omega-q_\omega|.
$$

 The competing tree class remains unrestricted.

</div>

<div class="proof">

*Proof.* The image of $K$ is compact by continuity of the model. The closed tree model is a closed subset of a finite probability simplex and is compact. The distance minimum is attained; if zero, it contradicts Theorem [7.1](#thm:triangle-closure). ◻

</div>

This corollary gives existence, not an evaluated useful lower bound on a biological parameter box. The unrestricted open network class has distance infimum zero from trees: as $\gamma$ approaches an endpoint, the network approaches one of its displayed trees. Pointwise exclusion from tree closure is therefore consistent with intersection of the two model closures.

<a id="sec:statistics"></a>

## 8 Observable rank margins and independent-site testing

The rank theorem supplies a directly computable pointwise certificate. For $1\le m\le\lfloor d/2\rfloor$, let $\mathcal M_m$ be the union, over quartet tree topologies, of their GM mixtures with at most $m$ components on a common topology. If $\sigma_1\ge\cdots\ge\sigma_{d^2}$ are a flattening’s singular values, put 

<a id="eq:rank-residual"></a>

$$
R_m(P)=\min_{s\in\{12|34,13|24,14|23\}}
       \left(\sum_{a>md}\sigma_a(F_s(P))^2\right)^{1/2}.
\tag{27}
$$

 Tail-singular-value scores and their interpretation as lower bounds on phylogenetic model distance are established tools [\[7\]](#ref-EckartYoung1936), [\[12\]](#ref-LongKubatko2021). The role of Theorem [3.1](#thm:rank) is to make this score positive throughout the specified network domain.

<div id="cor:residual" class="corollary">

**Corollary 8.1** (Computable pointwise margin). Every $P$ in Theorem [3.1](#thm:rank) satisfies 

$$
\mathop{\mathrm{dist}}_2(P,\overline{\mathcal M_m})\ge R_m(P)>0.
$$

 The function $R_m$ is $1$-Lipschitz in the Euclidean norm of tensor entries.

</div>

<div class="proof">

*Proof.* For a split $s$, let $\mathcal D_s$ be the closed determinantal set of tensors whose $s$-flattening has rank at most $md$, and let $\mathcal D=\bigcup_s\mathcal D_s$. By Lemma [2.3](#lem:tree-rank), $\mathcal M_m\subseteq\mathcal D$. The finite union $\mathcal D$ is closed, so it also contains $\overline{\mathcal M_m}$. Flattening is an isometry and the Eckart–Young theorem gives 

$$
\mathop{\mathrm{dist}}_2(P,\mathcal D)=R_m(P).
$$

 All three network ranks exceed $md$, hence $P\notin\mathcal D$ and this distance is positive. Distance to any nonempty set is $1$-Lipschitz. ◻

</div>

<div id="cor:test" class="corollary">

**Corollary 8.2** (A conservative iid test). Observe $n$ independent identically distributed quartet patterns and let $\widehat P_n$ be their empirical distribution. Put $K_4=d^4$ and, for $0<\alpha<1$, define 

$$
\tau_{n,\alpha}=\sqrt{\frac{K_4\log(2K_4/\alpha)}{2n}}.
$$

 Reject $P\in\overline{\mathcal M_m}$ when $R_m(\widehat P_n)>\tau_{n,\alpha}$. Its type-I error is at most $\alpha$ uniformly over the null. Its power tends to one at every fixed positive four-cycle distribution satisfying Theorem [3.1](#thm:rank).

</div>

<div class="proof">

*Proof.* If $\|\widehat P_n-P\|_2>\eta$, some coordinate differs by more than $\eta/\sqrt{K_4}$. Each coordinate is an empirical mean of independent Bernoulli indicators. Two-sided Hoeffding [\[11\]](#ref-Hoeffding1963) and a union bound give 

<a id="eq:coordinate-hoeffding"></a>

$$
\mathbb P_P\{\|\widehat P_n-P\|_2>\eta\}
       \le2K_4e^{-2n\eta^2/K_4}.
\tag{28}
$$

 No independence between coordinates is needed. Under the null, $R_m(P)=0$, so the Lipschitz property bounds $R_m(\widehat P_n)$ by the norm error. Substitution of $\tau_{n,\alpha}$ proves the level bound. At each allowed fixed alternative, $R_m(P)>0$, the empirical tensor converges almost surely to $P$, and the threshold tends to zero. ◻

</div>

For comparison, Corollary [7.2](#cor:compact) gives a related existence statement for triangle testing. Let $K$ and $\epsilon_K$ be as there. For $n$ iid three-leaf patterns, let $\widehat P_n$ denote their empirical distribution. Consider the idealized rule selecting the network when 

$$
\mathop{\mathrm{dist}}_{\mathop{\mathrm{TV}}}(\widehat P_n,\overline{\mathcal T_d})>\epsilon_K/2.
$$

 Both error probabilities are at most 

<a id="eq:triangle-test"></a>

$$
\min\{1,\ 2^{d^3}e^{-n\epsilon_K^2/2}\}.
\tag{29}
$$

 To see this, total variation on an alphabet of size $M=d^3$ equals $\max_{A\subseteq[M]}(\widehat P_n(A)-P(A))$. Apply one-sided Hoeffding to each subset and take a union bound over $2^M$ subsets. If the variation error is less than $\epsilon_K/2$, the rule is correct under either class by the triangle inequality.

These are conservative theoretical consequences. The triangle rule assumes a known margin and a distance to the full tree closure that we do not provide an efficient algorithm to compute. The four-cycle score is computable by three singular-value decompositions, but a finite-precision implementation needs numerical error control. Neither rule addresses site dependence, optimal sample complexity or empirical biological calibration. For larger networks, any selected quartet supplied by Lemma [4.1](#lem:gm-reduction) can be used with the quartet rule; a multiple-quartet selection scheme would require its own error analysis.

<a id="sec:discussion"></a>

## 9 Examples, limitations and further questions

The sharp family [(10)](#eq:sharp-example) has crossed ranks $3,6,10$ for $d=2,3,4$, respectively. It shows that exceptional rank loss can persist strictly inside the positive continuous-time parameter domain, while the rank remains above every tree threshold. The determinant formulas and the row-space filtration explain why this loss is harmless for the stated separation result. Numerical evidence of generic full rank would not establish this fact.

The binary example in Section [6](#sec:binary) gives the opposite type of boundary information: removing the nonuniform-frequency or $d\ge3$ condition from triangle separation would make that statement false. The full distribution, not just selected pair summaries, agrees with a tree there. Conversely, the repeated-spectrum equal-input case is included in the positive separation theorem whenever a nonzero third centered moment is available.

The two model classes have distinct strengths. The four-cycle result permits nonstationarity, arbitrary independent edge matrices and a limited number of site-mixture classes on the competing tree. It still requires positive invertible network channels and four observable attachments. The triangle theorem permits three attachments but requires a shared reversible generator at stationarity. It does not cover unrelated edge-specific generators, and its closure theorem concerns the homogeneous reversible tree class rather than every GM tree. The GM comparator permits singular and boundary stochastic parameters; the network side does not.

Neither result identifies reticulation orientation, all edge parameters or an arbitrary network topology. An arbitrary independently parameterized mixture of different tree topologies is outside the exclusion claim. Unrestricted rate mixtures and coalescent processes are also outside the models. The finite-mixture result concerns an upper bound on the number of components sharing a topology, rather than every possible representation of site heterogeneity.

Exact separation does not give a uniform practical detection margin on the whole interior. In [(19)](#eq:defect), the gap tends to zero at inheritance endpoints, as the ordinary cycle length vanishes, or as pendant attenuation becomes small. In particular $(1-e^{-\lambda a})^2\sim\lambda^2a^2$ as $a\to0$. The same distinction holds for the rank residual: it is positive at every allowed point but can be arbitrarily small across the model. Compact parameter restrictions give uniform margins only because the resulting network image stays away from the competing closed set.

Several extensions remain separate questions. A general description of the crossed-rank strata could refine the sharp minimum proved here. Multiple-reticulation reductions require control of effective observation channels, because convex mixtures can lose invertibility. Triangle separation under independently varying reversible edge generators is not settled by the spectral proof. These questions require additional arguments; the present proofs do not answer them by genericity.

## Declarations

##### Data and code availability.

The results are analytic. The accompanying candidate archive supplies source files and finite exact verification examples. Such examples check algebra and implementations; they do not replace the universal proofs or constitute proof-assistant verification. No empirical biological dataset is used.

##### Authorship and AI assistance.

The manuscript is released under the author name Anonymous. Conceptualization, formal analysis, writing and verification were developed through an AI-assisted workflow. The manuscript is an unrefereed candidate; internal AI-assisted checking is not external peer review.

##### Funding, interests and ethics.

No funding information or competing interests were declared for this candidate. No human participants, identifiable personal data or animal experiments were involved; ethics approval is not applicable.

##### Reuse.

The original manuscript, claims and accompanying public records are released under CC0 1.0 (CC0-1.0). Original executable verification code is released under the MIT License. Cited works retain their own rights.

## References

<a id="ref-ARS2012"></a>

**[1]**

E. S. Allman, J. A. Rhodes, and S. Sullivant. When do phylogenetic mixture models mimic other phylogenetic models? *Systematic Biology* **61**(6), 1049–1059 (2012). [doi:`10.1093/sysbio/sys064`](https://doi.org/10.1093/sysbio/sys064). Inspected preprint: [arXiv:1202.2396v2](https://arxiv.org/abs/1202.2396v2).

<a id="ref-Brits2026"></a>

**[2]**

J. Brits, N. Holtgrefe, L. van Iersel, and S. Martin. On tree–network distinguishability and full identifiability of phylogenetic networks (2026). [arXiv:2607.12919v3](https://arxiv.org/abs/2607.12919v3), 25 August 2026. [doi:`10.48550/arXiv.2607.12919`](https://doi.org/10.48550/arXiv.2607.12919).

<a id="ref-CFS2021"></a>

**[3]**

M. Casanellas and J. Fernández-Sánchez. Rank conditions on phylogenetic networks. In *Extended Abstracts GEOMVAP 2019*, Trends in Mathematics, pp. 65–69 (2021). [doi:`10.1007/978-3-030-84800-2_11`](https://doi.org/10.1007/978-3-030-84800-2_11). Inspected preprint: [arXiv:2004.12988v1](https://arxiv.org/abs/2004.12988v1).

<a id="ref-CFS2025"></a>

**[4]**

M. Casanellas and J. Fernández-Sánchez. Phylogenetic invariants: from the general Markov to equivariant models. *SIAM Journal on Applied Algebra and Geometry* **9**(4), 765–793 (2025). [doi:`10.1137/24M1644821`](https://doi.org/10.1137/24M1644821). Theorem numbers refer to the inspected accepted manuscript.

<a id="ref-CasanellasSteel2017"></a>

**[5]**

M. Casanellas and M. Steel. Phylogenetic mixtures and linear invariants for equal input models. *Journal of Mathematical Biology* **74**(5), 1107–1138 (2017). [doi:`10.1007/s00285-016-1055-8`](https://doi.org/10.1007/s00285-016-1055-8).

<a id="ref-Currie2026"></a>

**[6]**

B. Currie, A. K. Englander, J. A. Esparza-Lozano, E. Gross, M. Hill, C. Long, D. Olds, K. O’Connor, U. Ranasinghe, and C. Sum. Semialgebraic conditions for identifying triangles in phylogenetic networks (2026). [arXiv:2606.26673v1](https://arxiv.org/abs/2606.26673v1), 25 June 2026. [doi:`10.48550/arXiv.2606.26673`](https://doi.org/10.48550/arXiv.2606.26673).

<a id="ref-EckartYoung1936"></a>

**[7]**

C. Eckart and G. Young. The approximation of one matrix by another of lower rank. *Psychometrika* **1**(3), 211–218 (1936). [doi:`10.1007/BF02288367`](https://doi.org/10.1007/BF02288367).

<a id="ref-Englander2025"></a>

**[8]**

A. K. Englander, M. Frohn, E. Gross, N. Holtgrefe, L. van Iersel, M. Jones, and S. Sullivant. Identifiability of phylogenetic level-2 networks under the Jukes–Cantor model. bioRxiv preprint, version posted 24 April 2025. [doi:`10.1101/2025.04.18.649493`](https://doi.org/10.1101/2025.04.18.649493). Proposition 2.26 in the inspected version.

<a id="ref-Gross2021"></a>

**[9]**

E. Gross, L. van Iersel, R. Janssen, M. Jones, C. Long, and Y. Murakami. Distinguishing level-1 phylogenetic networks on the basis of data generated by Markov processes. *Journal of Mathematical Biology* **83**, Article 32 (2021). [doi:`10.1007/s00285-021-01653-8`](https://doi.org/10.1007/s00285-021-01653-8).

<a id="ref-Hill2024"></a>

**[10]**

M. Hill, S. Roch, and J. I. Rodriguez. Maximum likelihood estimation for unrooted 3-leaf trees: an analytic solution for the CFN model. *Bulletin of Mathematical Biology* **86**, Article 106 (2024). [doi:`10.1007/s11538-024-01340-x`](https://doi.org/10.1007/s11538-024-01340-x).

<a id="ref-Hoeffding1963"></a>

**[11]**

W. Hoeffding. Probability inequalities for sums of bounded random variables. *Journal of the American Statistical Association* **58**(301), 13–30 (1963). [doi:`10.1080/01621459.1963.10500830`](https://doi.org/10.1080/01621459.1963.10500830).

<a id="ref-LongKubatko2021"></a>

**[12]**

C. Long and L. Kubatko. Hypothesis testing with rank conditions in phylogenetics. *Frontiers in Genetics* **12**, 664357 (2021). [doi:`10.3389/fgene.2021.664357`](https://doi.org/10.3389/fgene.2021.664357).

<a id="ref-Snyman2023"></a>

**[13]**

J. Snyman, C. Fox, and D. Bryant. Parsimony and the rank of a flattening matrix. *Journal of Mathematical Biology* **86**, Article 44 (2023). [doi:`10.1007/s00285-023-01875-y`](https://doi.org/10.1007/s00285-023-01875-y).

<a id="ref-Sullivant2026"></a>

**[14]**

S. Sullivant. Phylogenetic network models as graphical models. *Bulletin of Mathematical Biology* **88**, Article 136 (2026). [doi:`10.1007/s11538-026-01695-3`](https://doi.org/10.1007/s11538-026-01695-3). Theorem numbers refer to [arXiv:2507.23056v2](https://arxiv.org/abs/2507.23056v2).

<a id="ref-SullivantIMSI2025"></a>

**[15]**

S. Sullivant. Phylogenetic network models and graphical models. IMSI lecture slides, 24 July 2025, slide 23 of 25. <https://cdn.imsi.institute/videos/59496/IKcB160s62/slides.pdf>. The cited slide attributes its generic rank theorem to M. Casanellas, J. Fernández-Sánchez, E. Gross, B. Hollering and S. Sullivant.
