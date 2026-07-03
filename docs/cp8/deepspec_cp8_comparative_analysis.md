# DeepSpec vs. CP8 / ASIN-HHC: Comparative Analysis

**Repository:** `dbottrader/DeepSpec`  
**Review date:** 2026-07-03  
**Classification:** `E1_DRAFT` analysis; subject to promotion only through executable implementation, tests, and independent reproduction  
**Commit posture:** documentation-only comparative artifact

---

## Executive Summary

DeepSpec and CP8 / ASIN-HHC operate at different abstraction layers and should be treated as complementary rather than competing systems.

DeepSpec is an executable machine-learning research repository focused on speculative decoding, draft-model training, evaluation, checkpointing, and benchmark execution.

CP8 / ASIN-HHC is best positioned as a provenance, evidence-governance, workflow-orchestration, and human-interface layer around AI artifacts and reproducibility records.

The strongest integration path is therefore not to claim CP8 improves DeepSpec model performance. The strongest path is to let CP8 wrap DeepSpec runs with manifest generation, hashing, evidence-tier labels, reproducibility metadata, and audit records.

---

## Layer Comparison

| Dimension | DeepSpec | CP8 / ASIN-HHC |
| --- | --- | --- |
| Primary function | Speculative decoding research implementation | Provenance and evidence-governance layer |
| Evidence state | Executable repository | Documentation-first unless paired with runnable artifacts |
| Runtime role | Training/evaluation/model code | Workflow wrapper, manifest system, audit trail |
| Main output | Models, logs, checkpoints, benchmark results | Manifests, hash records, evidence labels, handoff packages |
| Risk if overstated | Benchmark or implementation claims beyond measured results | Evidence inflation and symbolic overreach |
| Best integration point | Config/result/checkpoint lifecycle | Hashing, manifesting, classification, reproducibility record |

---

## Recommended Integration Model

The cleanest boundary-preserving integration is:

```text
DeepSpec config/result/checkpoint
        -> CP8 hash manifest
        -> evidence-tier label
        -> reproducibility record
        -> human-readable handoff package
```

This creates a concrete, testable role for CP8 without altering DeepSpec training or evaluation semantics.

---

## What DeepSpec Contributes

DeepSpec provides the executable ML substrate:

1. Model-specific speculative-decoding implementations.
2. Trainer and evaluator abstractions.
3. Dataset and target-cache handling.
4. Distributed training support.
5. Checkpointing and resume behavior.
6. Benchmark-facing evaluation logic.

This gives the repository an implementation maturity that documentation-only systems do not have.

---

## What CP8 / ASIN-HHC Contributes

CP8 contributes a governance and handoff structure:

1. Evidence-tier labeling from idea through production readiness.
2. Artifact hashing and provenance records.
3. Human-readable workflow maps.
4. Audit packet conventions.
5. Boundary language that separates claims from observations.
6. Symbolic orientation vocabulary for memory, interface, and navigation.

The most engineering-relevant CP8 component is the evidence ladder, especially if paired with executable manifest generation and tests.

---

## Boundary Discipline

The comparative analysis should preserve these boundaries:

- CP8 does **not** author upstream DeepSpec algorithms.
- CP8 does **not** prove DeepSpec benchmark improvement.
- CP8 does **not** certify production readiness.
- CP8 does **not** convert symbolic language into scientific proof by documentation alone.
- DeepSpec does **not** provide CP8 provenance governance unless CP8-compatible manifests are added.

This boundary discipline protects both projects.

---

## Evidence Classification

A reasonable evidence classification is:

| Artifact | Current classification | Reason |
| --- | --- | --- |
| DeepSpec implementation | `E2_LOCAL` to `E3_REPRO`, depending on environment reproducibility | It contains executable source; independent reproduction depends on setup and artifact completeness. |
| CP8 support docs | `E1_DRAFT` | Documentation exists, but executable CP8 code is required for promotion. |
| This comparative analysis | `E1_DRAFT` | Analytical document only. |
| Future CP8 manifest wrapper | `E2_LOCAL` once runnable with tests | Requires source, CLI, fixtures, and local passing tests. |
| Independent CP8 reproducibility record | `E3_REPRO` only after third-party rerun | Requires outside reproduction with clean environment. |

---

## Recommended Next Engineering Step

Add a minimal executable CP8 wrapper:

```text
cp8/provenance_manifest.py
```

Minimum behavior:

1. Accept a DeepSpec config path.
2. Compute SHA-256 for the config.
3. Optionally hash result/checkpoint/log artifacts.
4. Emit a JSON manifest.
5. Include evidence-tier metadata.
6. Include tests and golden fixtures.

Suggested output path:

```text
docs/cp8/examples/run_manifest.example.json
```

Suggested schema path:

```text
docs/cp8/schemas/run_manifest.schema.json
```

---

## Strategic Verdict

DeepSpec is the stronger executable substrate. CP8 is the stronger provenance and evidence-governance vocabulary. The two systems become useful together only when the connection is made operational:

```text
DeepSpec executes.
CP8 records, classifies, hashes, and packages evidence.
```

That is the clean technical story. It is defensible, testable, and does not require inflated claims.