#!/usr/bin/env python3
"""
CP8 Provenance Manifest Generator

Reads one or more input files and writes a CP8-compatible provenance manifest
with SHA-256 hashes, file sizes, timestamps, and evidence metadata.

This script is intentionally small and dependency-free so the CP8 documentation
package can cross the E1_DRAFT -> E2_LOCAL threshold with a reproducible local
executable artifact.

Example:
    python cp8/provenance_manifest.py \
        --input configs/example.yaml \
        --artifact-family deepspec-config \
        --output out/cp8_manifest.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List

VERSION = "0.1.0"
DEFAULT_EVIDENCE_LEVEL = "E2_LOCAL"


def sha256_file(path: Path) -> str:
    """Return the SHA-256 hex digest for a file."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def file_record(path: Path) -> Dict[str, Any]:
    """Build a deterministic metadata record for one input file."""
    stat = path.stat()
    return {
        "path": str(path),
        "name": path.name,
        "size_bytes": stat.st_size,
        "sha256": sha256_file(path),
        "modified_time_utc": dt.datetime.fromtimestamp(stat.st_mtime, tz=dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
    }


def build_manifest(
    inputs: List[Path],
    artifact_family: str,
    source_context: str,
    author: str,
    evidence_level: str,
) -> Dict[str, Any]:
    """Build a CP8 provenance manifest object."""
    generated_at = dt.datetime.now(tz=dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    records = [file_record(p) for p in inputs]

    manifest_payload = {
        "manifest_type": "CP8_PROVENANCE_MANIFEST",
        "manifest_version": VERSION,
        "generated_at_utc": generated_at,
        "artifact_family": artifact_family,
        "source_context": source_context,
        "author": author,
        "evidence_level": evidence_level,
        "claim_boundary": {
            "model_performance_claim": False,
            "production_claim": False,
            "independent_reproduction_claim": False,
            "symbolic_causality_claim": False,
        },
        "inputs": records,
        "environment": {
            "python_version_required": ">=3.9",
            "dependencies": [],
            "platform_note": "stdlib-only script; should run on any standard Python 3.9+ environment",
        },
        "failure_modes": [
            "input_file_missing",
            "permission_denied",
            "output_directory_missing_or_unwritable",
            "hash_changes_when_input_changes",
        ],
    }

    canonical = json.dumps(manifest_payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    manifest_payload["manifest_sha256"] = hashlib.sha256(canonical).hexdigest()
    return manifest_payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a CP8 provenance manifest for input files.")
    parser.add_argument("--input", action="append", required=True, help="Input file path. May be repeated.")
    parser.add_argument("--output", required=True, help="Output JSON manifest path.")
    parser.add_argument("--artifact-family", default="deepspec-supporting-data", help="Artifact family label.")
    parser.add_argument("--source-context", default="local", help="Source context or run description.")
    parser.add_argument("--author", default="unknown", help="Manifest author or generator identity.")
    parser.add_argument("--evidence-level", default=DEFAULT_EVIDENCE_LEVEL, help="Evidence label, default E2_LOCAL.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    inputs = [Path(p) for p in args.input]

    missing = [str(p) for p in inputs if not p.exists() or not p.is_file()]
    if missing:
        raise SystemExit(f"Missing or non-file input(s): {missing}")

    manifest = build_manifest(
        inputs=inputs,
        artifact_family=args.artifact_family,
        source_context=args.source_context,
        author=args.author,
        evidence_level=args.evidence_level,
    )

    output = Path(args.output)
    if output.parent and str(output.parent) != ".":
        output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote CP8 manifest: {output}")
    print(f"Manifest SHA-256: {manifest['manifest_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
