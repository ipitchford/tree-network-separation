# Sharp rank bounds and all-parameter tree–network separation

**Anonymous · 0.1.0-candidate · 4 October 2026 · unrefereed candidate**

[Paper (PDF)](paper.pdf) · [Accessible mathematical text](paper.md) · [Source](paper.tex) · [DOI](https://doi.org/10.5281/zenodo.23140370)

For a positive invertible d-state Markov four-cycle, two quartet flattenings have rank d² and the crossed flattening has rank at least d(d+1)/2. The latter bound is attained for every d≥2. It excludes mixtures of at most floor(d/2) general Markov trees sharing any one topology. For four states this is a rank-10 versus rank-8 obstruction to a two-class mixture on one tree topology.

A separate theorem treats triangles under one stationary homogeneous irreducible reversible generator. It excludes the closure of the whole competing homogeneous stationary reversible tree class for d≥3, and for binary nonuniform stationary frequencies. The binary uniform exception is classified and an exact positive network/tree collision is supplied. Marginal reductions cover larger single-reticulation networks with the stated observable attachments. None of these claims identifies arbitrary networks or treats unrelated generators on triangle edges.

Read [CLAIMS.json](CLAIMS.json) for exact scope and proof dependencies, [ASSURANCE.md](ASSURANCE.md) for evidence boundaries, and [AI_INDEX.md](AI_INDEX.md) for an agent-readable evidence map. The sharp rank proof, triangle spectral/moment proof and closure arguments are analytic. Finite checks support formulas and examples; they are not universal proof by enumeration, external peer review, or formal verification.

## Reproduce the exact checks

Use Python 3.11 or later and SymPy 1.14.0 in an isolated environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r verification/requirements.txt
python3 verification/replay.py --extended-d5 --output /tmp/tree-network-fresh-replay.json
python3 scripts/check_package.py
```

Choose a new output filename: the replay refuses to overwrite an existing receipt. It runs the exact suite under ordinary and optimized Python, compares mathematical outputs, and demands eight intended failures from four semantic mutations. The shipped [receipt](verification/replay-authoring.public.json) records authoring execution; the release's separate archive-bound gate receipt records clean-extraction execution. See [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md) for their distinct scope. CI repeats the portable suite on Python 3.11 and 3.13.

The manuscript is standalone LaTeX. A conventional build is `pdflatex paper.tex` twice; no external bibliography file is required. The shipped PDF is the reviewed output. Source snapshots of cited third-party papers and the private supplied review are not redistributed.

## Known boundaries

- Inheritance endpoints, singular channels and boundary lengths are outside the strict network domain. The global distance to trees is zero as inheritance approaches an endpoint.
- The mixture result requires a common competing tree topology. The network is itself a mixture of two different displayed topologies.
- A standard singular-value residual yields a conservative iid level test and pointwise consistency, not a calibrated biological power guarantee.
- The JC triangle polynomial, CFN inversion and standard rank/SVD tools have explicit precedents. The claim of extension is bounded by the inspected literature; an announced five-author collaboration has only a publicly inspected generic theorem, not a located complete manuscript.

Original research prose, claims and records: CC0-1.0. Original code: MIT. Scholarly creator: Anonymous. Ian Pitchford maintains and publishes the repository; account ownership is not an authorship claim. See [LICENSES.md](LICENSES.md) and [PROVENANCE.md](PROVENANCE.md).
