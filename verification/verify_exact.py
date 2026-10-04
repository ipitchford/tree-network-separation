#!/usr/bin/env python3
"""Exact algebra and finite example checks, never a proof by enumeration.

No random search, floating-point arithmetic, or Python assert statements occur
in these checks. The article supplies the universal analytic arguments.
"""
from argparse import ArgumentParser
from itertools import combinations, product
import json
import platform
import sys
import time

import sympy as sp


R = sp.Rational
SPLITS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
MUTATIONS = ("f81-sign", "determinant-exponent", "omitted-mixture", "third-split-full-rank")


class VerificationError(RuntimeError):
    """A mathematical or data-integrity check failed."""


def require(condition, message):
    if not bool(condition):
        raise VerificationError(message)


def equal(actual, expected, message):
    require(actual == expected, message)


def f81(pi, attenuation):
    d = len(pi)
    return attenuation * sp.eye(d) + (1 - attenuation) * sp.ones(d, 1) * sp.Matrix([pi])


def rational_channel(d, seed):
    """Fixed positive, strictly diagonally dominant integer rows, normalized.

    All choices are deterministic. Strict diagonal dominance is inherited by
    row normalization, so nonsingularity does not depend on successful search.
    """
    rows = []
    for i in range(d):
        raw = [1 + ((i + 1) * (j + 2) + seed * (i + 2) + j * j) % 7
               for j in range(d)]
        raw[i] += sum(raw) + d + seed
        total = sum(raw)
        rows.append([R(value, total) for value in raw])
    return sp.Matrix(rows)


def check_channel(matrix, name):
    d = matrix.rows
    equal(matrix.cols, d, name + ": not square")
    require(all(value > 0 for value in matrix), name + ": not strictly positive")
    equal(matrix * sp.ones(d, 1), sp.ones(d, 1), name + ": not stochastic")
    require(matrix.det(method="domain-ge") != 0, name + ": singular")


def probability_tensor(tensor, name):
    equal(sum(tensor.values()), 1, name + ": total probability is not one")
    require(all(value > 0 for value in tensor.values()), name + ": nonpositive entry")


def four_cycle(pi, S, T, U, V, gamma):
    return {(i, j, k, l): pi[i] * S[i, j] * T[i, k]
            * (gamma * U[j, l] + (1 - gamma) * V[k, l])
            for i, j, k, l in product(range(len(pi)), repeat=4)}


def triangle_tensor(pi, S, U, V, gamma):
    return {(i, j, k): pi[i] * S[i, j]
            * (gamma * U[i, k] + (1 - gamma) * V[j, k])
            for i, j, k in product(range(len(pi)), repeat=3)}


def star_tensor(pi, channels):
    d = len(pi)
    return {states: sum(pi[h] * sp.prod(channels[axis][h, states[axis]]
                       for axis in range(len(channels))) for h in range(d))
            for states in product(range(d), repeat=len(channels))}


def apply_pendants(tensor, channels):
    d = channels[0].rows
    current = dict(tensor)
    for axis, channel in enumerate(channels):
        current = {states: sum(current[states[:axis] + (h,) + states[axis + 1:]]
                              * channel[h, states[axis]] for h in range(d))
                   for states in product(range(d), repeat=len(channels))}
    return current


def flatten(tensor, left, right, d):
    def entry(row, col):
        state = [None] * (len(left) + len(right))
        for axis, value in zip(left, row):
            state[axis] = value
        for axis, value in zip(right, col):
            state[axis] = value
        return tensor[tuple(state)]
    return sp.Matrix([[entry(row, col) for col in product(range(d), repeat=len(right))]
                      for row in product(range(d), repeat=len(left))])


def exact_rank(matrix):
    # Over QQ, a DomainMatrix avoids repeated general symbolic simplification.
    return int(sp.polys.matrices.DomainMatrix.from_Matrix(matrix).rank())


def gap_formula(A, B, C, gamma, X=1, Y=1, Z=1):
    return -(X * Y * Z) ** 2 * A * gamma * (1 - gamma) * B * C * (1 - A) ** 2


def symbolic_checks():
    A, B, C, g, X, Y, Z = sp.symbols("A B C gamma X Y Z", positive=True)
    pairs = (X * Y * A, X * Z * (g * B + (1 - g) * A * C),
             Y * Z * (g * A * B + (1 - g) * C))
    triple_over_kappa = X * Y * Z * A * (g * B + (1 - g) * C)
    expected = gap_formula(A, B, C, g, X, Y, Z)
    equal(sp.expand(triple_over_kappa ** 2 - sp.prod(pairs) - expected), 0,
          "symbolic F81 gap identity failed")
    r, u, v = sp.symbols("r u v", positive=True)
    laplace = g * sp.exp(-r * u) + (1 - g) * sp.exp(-r * v)
    curvature = -g * (1 - g) * (u - v) ** 2 * sp.exp(-r * (u + v)) / laplace ** 2
    equal(sp.simplify(sp.diff(-sp.log(laplace), r, 2) - curvature), 0,
          "strict-concavity curvature identity failed")
    return {"f81_gap": str(sp.factor(expected)), "curvature_identity": "PASS",
            "sign_domain": "0<A<1; B,C,X,Y,Z>0; 0<gamma<1; r>0; u!=v"}


def general_markov_example(d, include_pendants=False):
    pi = [R(i + 1, d * (d + 1) // 2) for i in range(d)]
    channels = [rational_channel(d, seed) for seed in (1, 2, 3, 4)]
    names = ("S", "T", "U", "V")
    S, T, U, V = channels
    for name, channel in zip(names, channels):
        check_channel(channel, name)
    commutators = {}
    for i, j in combinations(range(4), 2):
        commutator = channels[i] * channels[j] - channels[j] * channels[i]
        require(commutator != sp.zeros(d), "channels unexpectedly commute")
        h, k = next((h, k) for h, k in product(range(d), repeat=2) if commutator[h, k] != 0)
        commutators[names[i] + names[j]] = {"entry": [h, k], "value": str(commutator[h, k])}
    reversibility = {}
    if d >= 3:
        for name, channel in zip(names, channels):
            # Detailed balance would force equality of these oriented cycle products.
            clockwise = channel[0, 1] * channel[1, 2] * channel[2, 0]
            counterclockwise = channel[0, 2] * channel[2, 1] * channel[1, 0]
            require(clockwise != counterclockwise, name + ": selected cycle is not a nonreversibility witness")
            reversibility[name] = {"cycle": [0, 1, 2, 0], "clockwise": str(clockwise),
                                   "counterclockwise": str(counterclockwise)}
    else:
        reversibility = {"qualification": "Every positive two-state stochastic matrix is reversible; only noncommutativity is tested at d=2."}
    gamma = R(2, 5)
    core = four_cycle(pi, S, T, U, V, gamma)
    probability_tensor(core, "general Markov core")
    flats = [flatten(core, *split, d) for split in SPLITS]
    ranks = [exact_rank(mat) for mat in flats]
    equal(ranks[:2], [d * d, d * d], "displayed flattening rank failed")
    require(ranks[2] >= d * (d + 1) // 2, "crossed flattening sharp lower bound failed")
    det1 = sp.prod(pi[i] * S[i, j] for i, j in product(range(d), repeat=2))
    det1 *= T.det() ** d * U.det() ** d * gamma ** (d * (d - 1))
    det2 = sp.prod(pi[i] * T[i, k] for i, k in product(range(d), repeat=2))
    det2 *= S.det() ** d * V.det() ** d * (1 - gamma) ** (d * (d - 1))
    equal(flats[0].det(method="domain-ge"), det1, "first determinant identity failed")
    equal(flats[1].det(method="domain-ge"), det2, "second determinant identity failed")
    SinvT, Tinv = S.T.inv(), T.inv()
    for i, l in product(range(d), repeat=2):
        row_matrix = sp.Matrix(d, d, lambda j, k: core[(i, j, k, l)])
        avec = SinvT * sp.Matrix([S[i, j] * U[j, l] for j in range(d)])
        bvec = T.T.inv() * sp.Matrix([T[i, k] * V[k, l] for k in range(d)])
        e = sp.eye(d)[:, i]
        expected = pi[i] * (gamma * avec * e.T + (1 - gamma) * e * bvec.T)
        equal(SinvT * row_matrix * Tinv, expected, "crossed-row change-of-basis identity failed")
    pendant_result = "not repeated at this dimension"
    if include_pendants:
        pendants = [rational_channel(d, seed) for seed in (5, 6, 7, 8)]
        for i, channel in enumerate(pendants):
            check_channel(channel, "pendant " + str(i))
        observed = apply_pendants(core, pendants)
        probability_tensor(observed, "observed four-cycle")
        for (left, right), mat in zip(SPLITS, flats):
            observed_flat = flatten(observed, left, right, d)
            left_map = sp.kronecker_product(*(pendants[i] for i in left))
            right_map = sp.kronecker_product(*(pendants[i] for i in right))
            equal(observed_flat, left_map.T * mat * right_map,
                  "pendant Kronecker identity failed")
        pendant_result = "exact full-matrix identity on all three splits; each multiplier invertible"
    return {"d": d, "root_distribution": list(map(str, pi)),
            "channels": {name: [[str(value) for value in channel.row(i)] for i in range(d)]
                         for name, channel in zip(names, channels)},
            "ranks": ranks, "determinants": list(map(str, (det1, det2))),
            "noncommuting_witnesses": commutators, "nonreversibility_witnesses": reversibility,
            "crossed_row_basis_identity": "PASS", "pendant_identity": pendant_result}


def symmetric_rank_control(d=4, full_rank_claim=False):
    pi = [R(i + 1, d * (d + 1) // 2) for i in range(d)]
    S, U = f81(pi, R(2, 3)), f81(pi, R(4, 7))
    core = four_cycle(pi, S, S, U, U, R(1, 2))
    probability_tensor(core, "symmetric four-cycle")
    rank = exact_rank(flatten(core, (0, 3), (1, 2), d))
    expected_rank = d * d if full_rank_claim else d * (d + 1) // 2
    rank_message = ("MUTATION_DETECTED[third-split-full-rank]: universal full crossed rank is false"
                    if full_rank_claim else "symmetric crossed rank should attain the sharp bound")
    equal(rank, expected_rank, rank_message)
    boundary = four_cycle(pi, S, S, U, U, sp.Integer(1))
    boundary_rank = exact_rank(flatten(boundary, (0, 2), (1, 3), d))
    equal(boundary_rank, d, "inheritance-one tree boundary rank failed")
    return {"d": d, "symmetric_crossed_rank": rank, "full_rank": d * d,
            "gamma_one_tree_boundary_rank": boundary_rank}


def same_topology_mixture_control():
    d = 4
    pi1 = [R(i + 1, 10) for i in range(d)]
    pi2 = list(reversed(pi1))
    channels1 = [rational_channel(d, seed) for seed in (1, 2, 3, 4)]
    channels2 = [rational_channel(d, seed) for seed in (5, 6, 7, 8)]
    tree1 = four_cycle(pi1, *channels1, sp.Integer(1))
    tree2 = four_cycle(pi2, *channels2, sp.Integer(1))
    weight = R(3, 7)
    mixture = {state: weight * tree1[state] + (1 - weight) * tree2[state] for state in tree1}
    pendants = [f81(pi1, value) for value in (R(1, 2), R(2, 3), R(3, 4), R(4, 5))]
    observed = apply_pendants(mixture, pendants)
    probability_tensor(observed, "two-component common-topology tree mixture")
    rank = exact_rank(flatten(observed, (0, 2), (1, 3), d))
    equal(rank, 2 * d, "selected two-tree mixture should attain rank eight")
    require(rank < d * (d + 1) // 2, "two-tree example rank does not illustrate the separation")
    return {"d": d, "components": 2, "common_split": "02|13", "mixture_weight": str(weight),
            "common_split_rank": rank, "four_cycle_proved_lower_bound": d * (d + 1) // 2,
            "scope": "Finite illustration of the analytic bound for mixtures sharing one quartet topology."}


def normalized_moments(tensor, pi):
    d = len(pi)
    m = next(i for i, weight in enumerate(pi) if weight != R(1, 2))
    phi = [sp.Integer(i == m) - pi[m] for i in range(d)]
    mean = sum(pi[i] * phi[i] for i in range(d))
    variance = sum(pi[i] * phi[i] ** 2 for i in range(d))
    cubic = sum(pi[i] * phi[i] ** 3 for i in range(d))
    equal(mean, 0, "state function is not centered")
    require(variance > 0 and cubic != 0, "state function has unusable moments")
    pairs = [sum(prob * phi[states[i]] * phi[states[j]] for states, prob in tensor.items()) / variance
             for i, j in ((0, 1), (0, 2), (1, 2))]
    triple_over_kappa = sum(prob * sp.prod(phi[state] for state in states)
                            for states, prob in tensor.items()) / cubic
    return pairs, triple_over_kappa, variance, cubic, m


def f81_triangle_example(d, uniform, gap_sign=1):
    pi = [R(1, d)] * d if uniform else [R(i + 1, d * (d + 1) // 2) for i in range(d)]
    A, B, C, gamma = R(2, 3), R(4, 7), R(5, 8), R(2, 5)
    X, Y, Z = R(1, 2), R(2, 5), R(3, 7)
    core = triangle_tensor(pi, f81(pi, A), f81(pi, B), f81(pi, C), gamma)
    pendants = [f81(pi, value) for value in (X, Y, Z)]
    tensor = apply_pendants(core, pendants)
    probability_tensor(tensor, "F81 triangle")
    pairs, triple_over_kappa, variance, cubic, m = normalized_moments(tensor, pi)
    equal(pairs, [X * Y * A, X * Z * (gamma * B + (1 - gamma) * A * C),
                  Y * Z * (gamma * A * B + (1 - gamma) * C)], "direct F81 pair moments failed")
    equal(triple_over_kappa, X * Y * Z * A * (gamma * B + (1 - gamma) * C),
          "direct F81 triple moment failed")
    gap = triple_over_kappa ** 2 - sp.prod(pairs)
    gap_message = ("MUTATION_DETECTED[f81-sign]: wrong gap sign"
                   if gap_sign == -1 else "direct F81 gap failed")
    equal(gap, gap_sign * gap_formula(A, B, C, gamma, X, Y, Z), gap_message)
    require(gap < 0, "direct F81 gap is not strictly negative")
    star = star_tensor(pi, pendants)
    probability_tensor(star, "F81 star")
    star_pairs, star_triple, _, _, _ = normalized_moments(star, pi)
    equal(star_triple ** 2 - sp.prod(star_pairs), 0, "direct F81 star gap failed")
    return {"d": d, "stationary_type": "uniform" if uniform else "nonuniform",
            "pi": list(map(str, pi)), "selected_state": m, "unnormalized_variance": str(variance),
            "unnormalized_cubic": str(cubic), "normalized_pairs": list(map(str, pairs)),
            "triple_over_kappa": str(triple_over_kappa), "triangle_gap": str(gap), "star_gap": "0"}


def binary_symmetric_control():
    pi = [R(1, 2), R(1, 2)]
    A, B, C, gamma = R(1, 4), R(1, 2), R(1, 2), R(1, 2)
    pendants = [f81(pi, R(1, 2)) for _ in range(3)]
    triangle = apply_pendants(triangle_tensor(pi, f81(pi, A), f81(pi, B), f81(pi, C), gamma), pendants)
    star_attenuations = [R(1, 4), R(1, 4), R(5, 16)]
    star = star_tensor(pi, [f81(pi, value) for value in star_attenuations])
    probability_tensor(triangle, "binary symmetric triangle")
    probability_tensor(star, "binary symmetric star")
    equal(triangle, star, "binary positive triangle and positive star tensors differ")
    require(all(0 < value < 1 for value in [A, B, C, R(1, 2)] + star_attenuations),
            "binary control must have finite strictly positive branch lengths")
    expected = {(0, 0, 0): R(39, 256), (0, 0, 1): R(29, 256),
                (0, 1, 0): R(30, 256), (0, 1, 1): R(30, 256),
                (1, 0, 0): R(30, 256), (1, 0, 1): R(30, 256),
                (1, 1, 0): R(29, 256), (1, 1, 1): R(39, 256)}
    equal(triangle, expected, "binary tensor explicit entries failed")
    return {"pi": ["1/2", "1/2"], "gamma": "1/2", "cycle_attenuations": ["1/4", "1/2", "1/2"],
            "triangle_pendant_attenuations": ["1/2"] * 3,
            "equal_star_attenuations": list(map(str, star_attenuations)),
            "all_eight_entries": {"".join(map(str, state)): str(prob) for state, prob in triangle.items()},
            "interpretation": "Exact negative control against blanket d=2 triangle separation; lengths are -log(attenuation)."}


def mutation_probe(name):
    """Deliberately corrupt one semantic ingredient; each probe MUST raise."""
    if name == "f81-sign":
        f81_triangle_example(3, False, gap_sign=-1)
    elif name == "determinant-exponent":
        d, gamma = 2, R(2, 5)
        pi = [R(1, 3), R(2, 3)]
        S, T, U, V = [rational_channel(d, seed) for seed in (1, 2, 3, 4)]
        actual = flatten(four_cycle(pi, S, T, U, V, gamma), (0, 1), (2, 3), d).det()
        corrupt = sp.prod(pi[i] * S[i, j] for i, j in product(range(d), repeat=2))
        corrupt *= T.det() ** d * U.det() ** d * gamma ** (d * (d - 1) + 1)
        equal(actual, corrupt, "MUTATION_DETECTED[determinant-exponent]: wrong gamma exponent")
    elif name == "omitted-mixture":
        d, pi = 3, [R(1, 6), R(2, 6), R(3, 6)]
        S, T, U, V = [rational_channel(d, seed) for seed in (1, 2, 3, 4)]
        # The omitted component is renormalized away. A mass-only check cannot catch this.
        corrupt = four_cycle(pi, S, T, U, V, sp.Integer(1))
        probability_tensor(corrupt, "renormalized omitted mixture")
        rank = exact_rank(flatten(corrupt, (0, 2), (1, 3), d))
        require(rank > d, "MUTATION_DETECTED[omitted-mixture]: omitted component leaves a tree rank")
    elif name == "third-split-full-rank":
        symmetric_rank_control(full_rank_claim=True)
    else:
        raise VerificationError("unknown mutation: " + str(name))
    raise VerificationError("MUTATION_ESCAPED: " + name)


def run_suite(extended_d5=False):
    checks = {"symbolic_identities": symbolic_checks()}
    dimensions = (2, 3, 4, 5) if extended_d5 else (2, 3, 4)
    checks["general_markov_examples"] = [general_markov_example(d, include_pendants=(d == 4)) for d in dimensions]
    checks["symmetric_and_boundary_controls"] = [symmetric_rank_control(d) for d in dimensions]
    checks["same_topology_two_tree_mixture"] = same_topology_mixture_control()
    checks["normalized_f81_examples"] = [f81_triangle_example(d, uniform)
                                         for d in (3, 4, 5) for uniform in (True, False)]
    checks["binary_symmetric_exact_tree_equality"] = binary_symmetric_control()
    detections = {}
    for name in MUTATIONS:
        try:
            mutation_probe(name)
        except VerificationError as exc:
            message = str(exc)
            require(message.startswith("MUTATION_DETECTED[" + name + "]:"),
                    "mutation failed for an unexpected reason: " + message)
            detections[name] = message
        else:
            raise VerificationError("mutation did not fail: " + name)
    checks["semantic_mutation_controls"] = detections
    return checks


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--extended-d5", action="store_true", help="also run the larger d=5 Markov example")
    parser.add_argument("--mutation", choices=MUTATIONS, help="deliberately fail a named semantic check")
    args = parser.parse_args()
    started = time.monotonic()
    report = {"schema": "gtr-exact-verification/v1", "status": "FAIL",
              "kind": "exact symbolic identities and finite rational example checks",
              "universal_proof": "The analytic article, not finite testing, establishes the universal claims.",
              "formal_verification": False, "python": platform.python_version(),
              "sympy": sp.__version__, "python_optimization": sys.flags.optimize,
              "mutation": args.mutation}
    exit_code = 0
    try:
        if args.mutation:
            mutation_probe(args.mutation)
        report["checks"] = run_suite(args.extended_d5)
        report["status"] = "PASS"
    except Exception as exc:
        report["error_type"] = type(exc).__name__
        report["error"] = str(exc)
        exit_code = 1
    report["elapsed_seconds"] = round(time.monotonic() - started, 6)
    print(json.dumps(report, indent=2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
