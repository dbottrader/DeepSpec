import json
import subprocess
import sys
from pathlib import Path


def test_provenance_manifest_cli_generates_expected_fields(tmp_path: Path):
    sample = tmp_path / "sample_config.yaml"
    sample.write_text("model: example\nseed: 123\n", encoding="utf-8")
    output = tmp_path / "manifest.json"

    script = Path(__file__).resolve().parents[2] / "cp8" / "provenance_manifest.py"
    result = subprocess.run(
        [
            sys.executable,
            str(script),
            "--input",
            str(sample),
            "--output",
            str(output),
            "--artifact-family",
            "test-family",
            "--source-context",
            "pytest",
            "--author",
            "test-suite",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert output.exists()
    manifest = json.loads(output.read_text(encoding="utf-8"))
    assert manifest["manifest_type"] == "CP8_PROVENANCE_MANIFEST"
    assert manifest["artifact_family"] == "test-family"
    assert manifest["source_context"] == "pytest"
    assert manifest["author"] == "test-suite"
    assert manifest["evidence_level"] == "E2_LOCAL"
    assert manifest["claim_boundary"]["model_performance_claim"] is False
    assert len(manifest["inputs"]) == 1
    assert manifest["inputs"][0]["name"] == "sample_config.yaml"
    assert len(manifest["inputs"][0]["sha256"]) == 64
    assert len(manifest["manifest_sha256"]) == 64
    assert "Wrote CP8 manifest" in result.stdout
