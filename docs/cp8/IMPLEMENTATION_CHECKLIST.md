# CP8 Implementation Checklist

This checklist converts the CP8 documentation layer into concrete engineering work.

## Phase 1 — Repository Hygiene

- [ ] Keep CP8 files isolated under `docs/cp8/` or a future `cp8/` package.
- [ ] Preserve DeepSpec license and attribution files.
- [ ] Add CP8 license terms if CP8 source files are introduced.
- [ ] Avoid modifying DeepSpec model/training/eval files unless there is a tested integration.

## Phase 2 — Minimal Runtime Definition

- [ ] Define the CP8 artifact schema.
- [ ] Define the CP8 agent/task message schema.
- [ ] Define a deterministic hashing protocol.
- [ ] Define evidence labels and promotion rules.
- [ ] Define the minimal command sequence for reproduction.

## Phase 3 — DeepSpec Integration Candidate

A clean integration would be a provenance wrapper around DeepSpec runs.

Candidate outputs:

- config hash,
- dataset metadata,
- target model identifier,
- draft model identifier,
- command invocation,
- benchmark name,
- output metrics,
- runtime environment,
- resulting manifest hash.

## Phase 4 — Test Harness

- [ ] Add sample DeepSpec run metadata.
- [ ] Add CP8 manifest generator.
- [ ] Add unit tests for manifest generation.
- [ ] Add a golden-output fixture.
- [ ] Add a reproduction command.

## Phase 5 — UI Layer

- [ ] Add a static HTML dashboard for manifest inspection.
- [ ] Display configs, checkpoints, benchmark outputs, and hashes.
- [ ] Clearly mark symbolic/orientation sections as non-benchmark material.

## Phase 6 — Promotion Gate

Before claiming E3_REPRO, require:

- [ ] clean repository checkout,
- [ ] dependency installation instructions,
- [ ] exact command sequence,
- [ ] deterministic output file,
- [ ] hash match,
- [ ] independent reviewer run log.

## Immediate Next Step

The safest next engineering addition would be:

```text
cp8/provenance_manifest.py
```

A small script that takes a DeepSpec config path and result file, computes hashes, and writes a CP8 manifest JSON.
