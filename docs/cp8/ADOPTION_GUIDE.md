# CP8 Adoption Guide

This guide explains how a third-party engineer can adopt the CP8 provenance wrapper pattern without adopting the entire ASIN-HHC symbolic layer.

## What CP8 Solves

CP8 addresses a recurring problem in AI-adjacent projects: artifacts often mix ideas, draft documentation, local experiments, reproduced results, and production claims without clear evidence boundaries.

CP8 provides:

- hash-based provenance records
- E0-E5 evidence labels
- claim boundaries
- promotion requirements
- anti-theater checks
- optional UI and symbolic orientation layers

## When to Use CP8

Use CP8 when you need to answer:

- What artifact was produced?
- What inputs generated it?
- What hashes identify it?
- What evidence level does it actually satisfy?
- What claims are explicitly not being made?
- What is required to promote it to a higher evidence level?

Do not use CP8 as a replacement for:

- model training code
- benchmark execution
- experiment tracking platforms
- production monitoring systems

CP8 can wrap those systems, but it does not replace them.

## Minimal Local Demo

Generate a manifest for any file:

```bash
python cp8/provenance_manifest.py \
  --input path/to/config.yaml \
  --artifact-family deepspec-config \
  --source-context local-demo \
  --author your-name \
  --output out/cp8_manifest.json
```

Expected result:

- `out/cp8_manifest.json` is created.
- It contains SHA-256 hash data for the input file.
- It declares `E2_LOCAL` by default.
- It explicitly avoids production, performance, independent reproduction, and symbolic causality claims.

## Run Tests

```bash
pytest tests/cp8/test_provenance_manifest.py
```

## Evidence Promotion Path

### E1_DRAFT -> E2_LOCAL

Required:

1. source file exists
2. executable command exists
3. sample input exists
4. output manifest is generated locally
5. failure modes are documented

### E2_LOCAL -> E3_REPRO

Required:

1. independent user runs the same command
2. environment is documented
3. generated output matches expected schema
4. hash behavior is verified
5. reproduction log is stored

## Symbolic Layer Boundary

CP8's core provenance functions do not require ANU-28, glyphs, or sacred-geometry motifs. Those elements can support human orientation and UI identity, but they are not evidence and cannot promote an artifact.

## Recommended Integration Pattern

For DeepSpec-style projects:

```text
config file / dataset metadata / run output
  -> CP8 manifest generator
  -> schema validation
  -> evidence label
  -> review or reproduction gate
```

## Next Integration Target

A future command should support:

```bash
cp8 deepspec wrap --config CONFIG --run-output RUN_DIR --output MANIFEST
```

This would make CP8 a reusable provenance wrapper around DeepSpec experiments.
