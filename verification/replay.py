#!/usr/bin/env python3
"""Replay normal/optimized exact checks and verify expected mutation failures."""
from argparse import ArgumentParser
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess
import sys
import time


MUTATIONS = ("f81-sign", "determinant-exponent", "omitted-mixture", "third-split-full-rank")


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def child_run(base, optimized, mutation, extended_d5):
    command = [sys.executable] + (["-O"] if optimized else []) + [str(base / "verify_exact.py")]
    if extended_d5:
        command.append("--extended-d5")
    if mutation:
        command += ["--mutation", mutation]
    process = subprocess.run(command, capture_output=True, text=True, timeout=120, check=False)
    report = json.loads(process.stdout)
    require(report["schema"] == "gtr-exact-verification/v1", "unexpected child report schema")
    require(report["python_optimization"] == int(optimized), "child optimization mode mismatch")
    require(report["mutation"] == mutation, "child mutation mismatch")
    if mutation is None:
        require(process.returncode == 0 and report["status"] == "PASS", "baseline failed: " + process.stdout)
        require(set(report["checks"]["semantic_mutation_controls"]) == set(MUTATIONS), "missing built-in mutation controls")
    else:
        require(process.returncode == 1 and report["status"] == "FAIL", "mutation did not return a failing status")
        require(report.get("error_type") == "VerificationError", "mutation failed outside the intended checker")
        require(report.get("error", "").startswith("MUTATION_DETECTED[" + mutation + "]:"),
                "mutation failed for an unexpected reason")
    return {"command": command, "exit_code": process.returncode,
            "stderr": process.stderr, "report": report,
            "outcome": "EXPECTED_FAILURE_DETECTED" if mutation else "PASS"}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the complete JSON receipt to a new file")
    parser.add_argument("--extended-d5", action="store_true", help="include d=5 Markov and symmetric examples")
    args = parser.parse_args()
    started = time.monotonic()
    base = Path(__file__).resolve().parent
    receipt = {"schema": "gtr-replay-receipt/v1", "status": "FAIL",
               "started_utc": datetime.now(timezone.utc).isoformat(),
               "python": platform.python_version(), "extended_d5": args.extended_d5,
               "scope": "Exact identities and finite examples; neither a universal proof nor proof-assistant verification.",
               "source_sha256": {name: sha256((base / name).read_bytes()).hexdigest()
                                 for name in ("verify_exact.py", "replay.py", "README.md", "requirements.txt")},
               "runs": []}
    try:
        if args.output is not None:
            require(not args.output.exists(), "refusing to overwrite an existing replay receipt")
        for optimized in (False, True):
            receipt["runs"].append(child_run(base, optimized, None, args.extended_d5))
            for mutation in MUTATIONS:
                receipt["runs"].append(child_run(base, optimized, mutation, args.extended_d5))
        baseline_reports = [run["report"] for run in receipt["runs"] if run["report"]["mutation"] is None]
        require(baseline_reports[0]["checks"] == baseline_reports[1]["checks"],
                "normal and optimized Python produced different exact mathematical results")
        receipt["status"] = "PASS"
        receipt["summary"] = {"baseline_passes": 2, "expected_mutation_failures": 8,
                              "normal_optimized_mathematical_results_identical": True,
                              "markov_dimensions": [item["d"] for item in baseline_reports[0]["checks"]["general_markov_examples"]]}
    except Exception as exc:
        receipt["error_type"] = type(exc).__name__
        receipt["error"] = str(exc)
    receipt["elapsed_seconds"] = round(time.monotonic() - started, 6)
    receipt_written = False
    if args.output is not None and not args.output.exists():
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            # The exclusive mode closes the race between existence check and write.
            with args.output.open("x", encoding="utf-8") as handle:
                json.dump(receipt, handle, indent=2, sort_keys=True)
                handle.write("\n")
            receipt_written = True
        except OSError as exc:
            receipt["status"] = "FAIL"
            receipt["receipt_write_error"] = str(exc)
    if receipt_written:
        summary = {key: value for key, value in receipt.items() if key != "runs"}
        summary["receipt"] = str(args.output.resolve())
        print(json.dumps(summary, indent=2, sort_keys=True))
    else:
        print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
