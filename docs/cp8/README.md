# CP8 / ASIN-HHC Supporting Data

This directory contains a bounded supporting-data package for the CP8 / ASIN-HHC architecture discussion alongside DeepSpec.

It does **not** modify DeepSpec training, evaluation, model, or data-preparation code. The purpose is to preserve a clear comparison layer between:

- **DeepSpec**: a speculative-decoding research codebase for training and evaluating draft models.
- **CP8 / ASIN-HHC**: a broader orchestration, provenance, symbolic-interface, and human/AI workflow framework.

## Scope

This package is documentation-first. It provides:

1. an architecture map,
2. a provenance and evidence boundary,
3. a DeepSpec comparison note,
4. a supporting-data manifest,
5. an implementation-readiness checklist.

## Boundary

The files here should be read as project documentation and design support material. They are not claims of upstream DeepSpec authorship, benchmark improvement, scientific validation, clinical validity, hardware certification, or production readiness.

## Directory

- `ARCHITECTURE.md` — CP8 component map and how it relates to AI workflow systems.
- `DEEPSPEC_COMPARISON.md` — explicit comparison between DeepSpec and CP8.
- `PROVENANCE.md` — evidence rules, hashing posture, and claim boundary.
- `SUPPORTING_DATA_MANIFEST.json` — machine-readable manifest of known CP8 artifacts and status.
- `IMPLEMENTATION_CHECKLIST.md` — concrete steps required to convert the documentation layer into a reproducible implementation.
