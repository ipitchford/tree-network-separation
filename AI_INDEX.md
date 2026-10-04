# Agent-readable research index

## Claim and status

Read [CLAIMS.json](CLAIMS.json) before using a theorem. It states the state counts, strict positivity, invertibility, inheritance and model-sharing assumptions, comparator classes and proof dependencies. [STATUS.md](STATUS.md) identifies this version as an unrefereed candidate. Do not turn internal checks or publication into external acceptance, formal verification, priority certification or a REF rating.

## Mathematical evidence

The authoritative argument is [paper.tex](paper.tex), with a [PDF](paper.pdf) and [Markdown rendering](paper.md). The main rank theorem is universal and sharp; the verification dimensions are finite examples, not its quantifiers. Homogeneous triangle results require a shared generator. Fixed-topology mixture results do not exclude arbitrary mixtures of different tree topologies.

## Replay and falsification

[verification/README.md](verification/README.md) gives the exact checks and limitations. Run [verification/replay.py](verification/replay.py) with `--extended-d5` and a new external receipt path. It invokes [verify_exact.py](verification/verify_exact.py) with ordinary and optimized Python and requires intended failure of all four semantic mutations in both modes. Read [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md) and the [retained public authoring receipt](verification/replay-authoring.public.json). The rational binary-symmetric full-tensor collision and symmetric rank witnesses guard the theorem boundaries.

## Sources and assurance

[CITATION_AUDIT.md](CITATION_AUDIT.md) and [research/theorem-comparison.md](research/theorem-comparison.md) distinguish known JC/CFN cases, universal upper bounds, generic network lower bounds and the residual statements. [RESEARCH_GATES.json](RESEARCH_GATES.json) records the actual search/extension decisions. [ASSURANCE.md](ASSURANCE.md) states remaining independent-review and numerical-statistics gaps. [audit/REVIEW_RESPONSE.md](audit/REVIEW_RESPONSE.md) maps revision requests to the candidate. [audit/final-math-audit.md](audit/final-math-audit.md) is a hash-bound internal audit, not external peer review.

## Bytes, environment and rights

Use [scripts/check_package.py](scripts/check_package.py) to check [MANIFEST.sha256](MANIFEST.sha256) and essential record consistency. [ENVIRONMENT.json](ENVIRONMENT.json) records the execution environment; [verification/requirements.txt](verification/requirements.txt) pins the symbolic dependency. [PROVENANCE.md](PROVENANCE.md), [LICENSES.md](LICENSES.md), [LICENSE](LICENSE) and [LICENSE-CODE](LICENSE-CODE) separate Anonymous scholarly creation, maintenance, CC0 records and MIT code. [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json) carry the public citation identity.

The manifest checker, JSON validators and successful execution receipts establish bounded mechanical facts. They do not decide whether every mathematical inference is correct or whether a literature search is exhaustive.
