#!/usr/bin/env python3
"""Check shipped byte coverage and record consistency, not mathematical adequacy."""
from hashlib import sha256
import json
from pathlib import Path
import re

base = Path(__file__).resolve().parents[1]
manifest = base / "MANIFEST.sha256"
if not manifest.is_file():
    raise SystemExit("Missing MANIFEST.sha256")
entries = {}
for line in manifest.read_text().splitlines():
    if not re.fullmatch(r"[0-9a-f]{64}  .+", line):
        raise SystemExit("Malformed manifest entry")
    digest, name = line.split("  ", 1)
    path = Path(name)
    if path.is_absolute() or ".." in path.parts or name in entries:
        raise SystemExit("Unsafe or duplicate manifest path")
    entries[name] = digest
    target = base / name
    if not target.is_file() or sha256(target.read_bytes()).hexdigest() != digest:
        raise SystemExit("Byte mismatch: " + name)
def shipped(p):
    rel = p.relative_to(base)
    return not any(part in {".git", ".venv", "__pycache__"} for part in rel.parts) and p.suffix not in {".aux", ".log", ".out", ".toc", ".pyc"} and rel.as_posix() != "MANIFEST.sha256"
actual = {p.relative_to(base).as_posix() for p in base.rglob("*") if p.is_file() and shipped(p)}
if actual != set(entries):
    raise SystemExit("Manifest coverage mismatch: " + str(sorted(actual ^ set(entries))))
for name in ("CLAIMS.json", "RESEARCH_GATES.json", "ENVIRONMENT.json", ".zenodo.json"):
    json.loads((base / name).read_text())
zenodo = json.loads((base / ".zenodo.json").read_text())
if zenodo["creators"] != [{"name": "Anonymous"}] or zenodo["version"] != "0.1.0-candidate":
    raise SystemExit("Citation identity mismatch")
pdf = (base / "paper.pdf").read_bytes()
if not pdf.startswith(b"%PDF-") or len(pdf) < 10000:
    raise SystemExit("Missing or implausible manuscript PDF")
private = re.compile(rb"/Users/|/home/runner/|/mnt/data/|sk-proj-[A-Za-z0-9]|ghp_[A-Za-z0-9]{20}")
for name in entries:
    if name.endswith((".md", ".json", ".tex", ".bib", ".cff", ".yml", ".txt")):
        if private.search((base / name).read_bytes()):
            raise SystemExit("Potential private host path or credential in " + name)
print(json.dumps({"status": "PASS", "files": len(entries), "scope": "Manifest coverage, exact hashes, readable JSON and bounded public-record consistency; not a proof audit."}))
