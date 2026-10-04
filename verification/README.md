# Exact verification supplement

This directory contains reproducible symbolic identities and finite rational
examples for the revised article. The universal conclusions depend on its
analytic proofs. A successful receipt is not proof-assistant verification,
external peer review, a novelty finding, or a research-quality score.

## Requirements and replay

Use Python 3.11 or newer and SymPy 1.14.0. The authoring environment tested
Python 3.14.7. The scripts use only the Python standard library and SymPy,
require no network access, and do not use randomness or floating-point
arithmetic in mathematical checks. Timings alone are floating-point values.
For a fresh environment, install `requirements.txt` using the environment's
ordinary dependency workflow.

From this directory, the portable replay is:

```sh
python3 replay.py --extended-d5 --output replay-receipt.json
```

The output path must be new: existing receipts are never overwritten. All
input paths are resolved relative to the script, so replay does not depend on
the caller's working directory. On the shared authoring host, enter the
resource queue once for the whole subprocess tree:

```sh
research-run status
research-run run --cpu 1 --memory-gb 1 --label gtr-exact-replay --max-wait 120 -- python3 replay.py --extended-d5 --output replay-receipt.json
```

Do not nest queue wrappers. Omitting `--extended-d5` omits only the larger
five-state four-cycle and symmetric-rank examples; the F81 triangle examples
still include five states. No scans or parameter searches occur.

`replay.py` runs the complete suite twice, using ordinary Python and Python
`-O`. It then requires all four deliberate semantic mutations to fail with
exit code 1 and the expected diagnostic under both modes. It also compares
the complete mathematical results of the two baseline runs exactly. The JSON
receipt records source SHA-256 hashes, commands, versions, timings, exit
codes, and each child report. Failure of any required condition makes the
replay exit nonzero and report `FAIL`.

For a single inspection run:

```sh
python3 verify_exact.py --extended-d5
python3 -O verify_exact.py --mutation omitted-mixture
```

The second command is deliberately expected to fail. It is a control, not a
successful standalone verification. Checks use explicit `require`/`raise`
conditions, so `-O` cannot discard them.

## What is checked

1. Symbolic expansion of the F81 moment-gap factorization and symbolic
   differentiation of the strict-concavity identity. The sign domains are
   stated; their universal use remains part of the analytic argument.
2. Deterministic strictly positive invertible rational Markov four-cycles
   at dimensions 2, 3, and 4, optionally 5. The JSON gives every matrix entry,
   root weight, determinant, and flattening rank in lexicographic order.
   All six channel pairs have explicit nonzero commutator witnesses. At
   dimensions at least 3, every channel has unequal forward/reverse cycle
   products, certifying nonreversibility with respect to any stationary
   distribution. Every positive two-state Markov channel is reversible;
   the binary example deliberately makes no nonreversibility claim.
3. Both displayed-split determinant formulas and the crossed-row
   change-of-basis identity, evaluated independently from tensor entries.
   The selected crossed ranks satisfy the sharp lower bound
   `d(d+1)/2`; these finite cases do not prove that bound universally.
4. The complete pendant Kronecker identity on all three four-state
   flattenings, with strictly positive invertible rational pendant channels.
5. Symmetric crossed-rank examples attaining exactly 3, 6, and 10 at
   dimensions 2, 3, and 4 (and 15 with the optional dimension 5). These
   preserve the rank-10 four-state control from the original supplement.
   Inheritance-one controls have tree rank exactly `d`. A two-component
   four-state tree mixture with one common topology has its shared-split
   rank exactly 8, illustrating the gap from the four-cycle bound 10.
6. Directly summed F81 triangle and star tensors with uniform and nonuniform
   stationary distributions at dimensions 3, 4, and 5. The normalized
   triangle gap is exactly `-2/42875`, and the star gap is zero in all six
   selected cases. To avoid introducing radicals, use a centered indicator
   `phi`, variance `v`, and nonzero cubic moment `c`. Then normalized pair
   moments are `E(phi_u phi_v)/v`, and `W/kappa=E(phi_1 phi_2 phi_3)/c`.
   These are exactly the variance-one moments in the article.
7. A positive binary-symmetric triangle equals a positive three-leaf star
   entry by entry. With `Q=1*pi^T-I`, `pi=(1/2,1/2)`, cycle attenuations
   `(1/4,1/2,1/2)`, inheritance `1/2`, and triangle pendant attenuations
   `(1/2,1/2,1/2)`, the equal star has attenuations `(1/4,1/4,5/16)`.
   Every attenuation is strictly between zero and one, so every branch
   length `-log(attenuation)` is finite and strictly positive. This is an
   exact negative control against extending triangle separation to every
   binary reversible model.

The mathematical equality predicates are exercised by four semantic fault
probes: flipping the F81 gap sign, adding one to the determinant's inheritance
exponent, dropping one mixture component and renormalizing the remaining
tree, and falsely demanding full crossed rank in the symmetric example.
Renormalizing the omitted mixture intentionally defeats a mass-only check;
the rank check still catches it. The sign and crossed-rank probes send the
corrupted expectation through the same comparison used by the baseline;
neither merely negates an already-validated result. These are explicit fault
injection paths, not automatic source-code mutation or arbitrary program
correctness verification.

## Relationship to the original archive

This is a separate strengthened supplement. The original archive and its
checker are retained unchanged. These scripts preserve its gap, curvature,
determinant, pendant, symmetric-rank, and inheritance-boundary checks while
adding general noncommuting channels, scope controls, and robust replay.
