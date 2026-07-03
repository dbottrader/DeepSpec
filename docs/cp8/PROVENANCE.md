# CP8 Provenance and Evidence Boundary

## Purpose

This document defines how CP8 / ASIN-HHC supporting material should be interpreted inside this repository.

The goal is to protect both sides:

- DeepSpec remains a speculative-decoding research codebase.
- CP8 remains clearly labeled as supporting architecture/provenance material unless executable, tested integrations are added.

## Evidence Labels

Recommended labels for future CP8 artifacts:

| Label | Meaning |
| --- | --- |
| E0_IDEA | concept, sketch, or symbolic orientation |
| E1_DRAFT | written design or non-executable specification |
| E2_LOCAL | executable locally by the author or current environment |
| E3_REPRO | independently reproducible from supplied source and instructions |
| E4_REVIEWED | reviewed by external technical reviewers |
| E5_PRODUCTION | production-operational with monitoring, rollback, and support boundaries |

## Current Status

The material in `docs/cp8/` should be treated as **E1_DRAFT** unless a specific file includes executable tests and reproduction instructions.

## Hashing Posture

Future artifact manifests should include:

- file path,
- file size,
- SHA-256 hash,
- creation timestamp,
- source context,
- author/operator,
- evidence label,
- reproduction notes.

## Claim Boundaries

Do not infer any of the following from the presence of CP8 documents in this repository:

- that DeepSpec authors endorsed CP8,
- that CP8 was merged into upstream DeepSpec,
- that CP8 improves speculative decoding performance,
- that CP8 artifacts are independently verified,
- that symbolic interpretations are scientific evidence,
- that UI pages are validated systems,
- that a handoff package equals production readiness.

## Promotion Rule

A CP8 component should only move from E1 to E2/E3 when it has:

1. source code or complete artifact files,
2. a deterministic execution path,
3. sample input,
4. expected output,
5. hash-verifiable output manifest,
6. documented environment assumptions,
7. clear failure modes.

## Recommended Manifest Fields

```json
{
  "artifact_id": "string",
  "title": "string",
  "path": "string",
  "artifact_type": "documentation | code | ui | data | package",
  "evidence_level": "E1_DRAFT",
  "sha256": null,
  "status": "documented",
  "claim_boundary": "documentation only unless independently reproduced"
}
```
