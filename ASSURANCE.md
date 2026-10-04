# Assurance statement

The package contains analytic mathematical arguments and a reproducible exact
checking supplement. Their evidentiary roles are different. The arguments
establish the stated universal conclusions if correct; the executable checks
verify selected symbolic identities, finite rational examples, and specified
failure controls. Finite checks alone do not establish any all-parameter
claim. `CLAIMS.json` maps seven primary claims to their assumptions, proof
locations, dependencies, and actual computational coverage. Its article locators are bound to the final source and result numbers.

The internal review used separately delegated AI agents to inspect the rank
argument, triangle argument, state-space boundary, and prior-work comparison.
This is internal AI review. It is not independent external peer review or
proof-assistant verification. No official REF rating, acceptance decision,
or guarantee of priority is asserted. A supplied review was treated as source
material; the audit ZIP linked inside that review was not available locally
and is not represented as independently replayed.

The prior-work comparison credits the known Jukes-Cantor triangle obstruction,
the equal-input and CFN frameworks, tree and mixture rank bounds, rerooting,
low-rank approximation, and concentration tools. The inspected primary theorem
statements did not fully subsume the delimited residual results. That finding
is bounded by the search and inspected versions. In particular, a complete
manuscript for the announced equivariant-network collaboration was not located;
its accessible public statement is generic. Unpublished results and every
possible relevant source have not been excluded.

## Exact replay and its limits

`verification/verify_exact.py` uses rational and symbolic arithmetic for its
mathematical checks. It directly constructs probability tensors, sums moments,
computes flattenings, and compares them with separately entered formulas.
The matrix ranks and determinants are supplied by SymPy, with its optional python-flint 0.9.0 backend automatically selected on the authoring host. The clean-extraction release plan and CI explicitly select the pure-Python ground domain to test the pinned portable dependencies without that optional accelerator. There is no second
computer-algebra implementation or formally verified arithmetic kernel in this
package. Timings are ordinary wall-clock measurements and are not mathematical
inputs.

The selected general Markov examples use strictly positive invertible rational
channels and give explicit nonzero commutators. At dimensions at least three,
unequal forward and reverse cycle products certify channel nonreversibility.
The binary Markov example tests noncommutativity only: every positive two-state
channel is reversible. Full direct-tensor checks cover the positive binary
triangle–star equality, rather than merely checking equality of a few moments.

The four semantic fault probes deliberately change a gap sign, a determinant
exponent, a mixture component, and a crossed-rank claim. The omitted mixture
is renormalized, so its detection depends on rank rather than a trivial
probability-mass error. These are targeted sensitivity checks. They do not
prove arbitrary program correctness or constitute unrestricted mutation
testing of every source line. The replay requires the intended error class,
diagnostic, and exit code; an unrelated crash does not count as successful
mutation detection.

All conditions use explicit exceptions rather than Python `assert` statements.
`verification/replay.py` runs the suite in ordinary Python and Python `-O`,
compares their mathematical outputs, and requires all four probes to fail
under both modes. A successful receipt therefore reports two baseline passes
and eight expected failures. The exact authoring receipt is evidence for the
source hashes it records; it does not attest to later edited bytes.

## Portable independent replay

Use Python 3.11 or newer. The tested dependency is SymPy 1.14.0, with mpmath
1.3.0 installed transitively. A fresh virtual environment can be prepared from
the package root with:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r verification/requirements.txt
.venv/bin/python verification/replay.py --extended-d5 --output /tmp/tree-network-fresh-replay.json
```

On Windows, use the corresponding `.venv\Scripts\python.exe` path. Installing
dependencies may require network access; execution after installation does
not. Each receipt path must be new. To inspect one normal or optimized run:

```sh
.venv/bin/python verification/verify_exact.py --extended-d5
.venv/bin/python -O verification/verify_exact.py --extended-d5
```

The authoring machine additionally uses `research-run` to reserve shared CPU
and memory before a replay. That wrapper is a local resource-management
policy, not a portable package dependency. It is unnecessary on a reader's
ordinary machine. No GPU, private service, hosted model, or secret credential
is needed to replay the supplement.

## Interpretation and remaining boundaries

The four-cycle rank theorem allows nonstationary, nonreversible,
edge-heterogeneous general Markov channels. The triangle theorem requires a
shared stationary reversible generator. Neither result identifies arbitrary
network topology or parameters. Multiple reticulations are not covered merely
by marginalizing them away: a mixture of invertible channels can be singular.

Pointwise exclusion from a competing model closure and positive margins on
compact interior parameter sets do not imply a positive global margin.
Inheritance endpoints approach displayed trees. The iid statistical
corollaries are theoretical consequences with explicit assumptions and
conservative bounds, not an empirically calibrated sequence-analysis tool.

The final claim map uses actual article locators and an exact source digest. A fresh clean-extraction replay is required after archive freeze and recorded externally, alongside the GitHub CI and provider readback identities. Publication, external visibility, DOI assignment and canonical readback are separate delivery facts; they are established by their own retained receipts, not by this assurance statement.
