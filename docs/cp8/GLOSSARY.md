# CP8 / ASIN-HHC Glossary

This glossary defines terms used in the CP8 / ASIN-HHC supporting documentation package. It is intended for third-party engineers, reviewers, and future AI agents reading the repository.

## Core Terms

### CP8
A workflow orchestration, provenance, and evidence-governance layer for AI-adjacent projects. In this repository, CP8 is documentation and supporting infrastructure around DeepSpec. CP8 does not replace DeepSpec's model-training or speculative-decoding code.

### ASIN-HHC
A project-origin acronym used for the broader symbolic and coordination framework. In engineering context, ASIN-HHC should be read as the human-facing design system and semantic orientation layer around CP8 artifacts.

### ANU-28
A 28-glyph symbolic vocabulary used as a semantic coordination grammar. In CP8 engineering documents, ANU-28 glyphs are non-causal symbolic labels or metadata cues only. They do not imply physical effects, consciousness, hidden memory, or model-internal control.

### HOS
HarmonyOS-style ecosystem architecture used by the project to describe how human interfaces, agents, manifests, storage, routing, and evidence gates connect. It is an architecture metaphor and planning layer, not a claim about Huawei HarmonyOS compatibility.

### Human Interface Layer
The UI-facing layer of CP8. It favors constrained, accessible surfaces such as single-file HTML dashboards, Android-friendly tools, visual provenance cards, and workflow maps.

### Agent / Workflow Layer
The layer that organizes task agents, file handlers, build steps, evaluation roles, and handoff workflows. This layer should eventually be expressed in executable scripts, CLI tools, or service adapters.

### Provenance Layer
The layer that records what artifact was produced, what input produced it, when it was created, what hashes identify it, and what evidence status it currently has.

### Symbolic / Orientation Layer
The optional layer containing glyphs, motifs, room names, narrative labels, and visual metaphors. Its engineering role is human orientation, memory, navigation, and identity continuity. It is not required for core provenance functions.

### Evaluation / Governance Layer
The layer that assigns evidence levels, defines promotion requirements, prevents overclaiming, and supports review or reproduction gates.

## Evidence Terms

### E0_IDEA
An idea, concept, sketch, or untested proposal.

### E1_DRAFT
A written specification or documentation artifact without executable verification.

### E2_LOCAL
An artifact that the author can execute locally with source, inputs, expected outputs, and environment notes.

### E3_REPRO
An artifact independently reproduced outside the original author context.

### E4_REVIEWED
An artifact reviewed by external technical reviewers under explicit criteria such as code review, architecture review, reproduction review, or security review.

### E5_PRODUCTION
An artifact used operationally with monitoring, rollback, ownership, support boundaries, and maintenance expectations.

### Evidence Decay
The rule that evidence status can become stale when dependencies, environments, data, or execution assumptions change. A previously reproduced artifact may need revalidation.

### Anti-Theater Check
A governance check designed to distinguish real capability from presentation, ceremony, branding, or unsupported claims.

## Project-Specific Terms

### Cathedral Spine MVP0
A bounded runtime-spine prototype or scaffold used in prior project materials. Unless source, tests, and reproduction logs are present, it should be treated as a documented artifact rather than a verified runtime system.

### Shock Kernel
A named experimental component in the broader CP8/Cathedral materials. It requires source code, tests, and reproduction evidence before being promoted beyond draft or template status.

### Weaver Epistemic Promotion Gate
A governance concept for deciding when an artifact can move from one evidence level to another. The gate should use explicit promotion requirements, manifests, tests, and review artifacts.

### Labyrinth Master Canon / LMC
A governance and documentation discipline used by the broader project to separate capability, authority, evidence, and claims.

### Universal Object Model
A proposed structured output pattern in the broader governance work. It typically includes artifact identity, evidence level, governance state, source fields, constraints, provenance, and failure modes.

## DeepSpec Terms

### DeepSpec
The upstream research project focused on speculative decoding and related model-training/evaluation workflows. CP8 documentation in this repository is adjacent support material, not a replacement for DeepSpec's code or research claims.

### Speculative Decoding
A model inference acceleration technique where a draft model proposes tokens and a target model verifies or accepts them under defined criteria. CP8 may wrap such workflows with provenance manifests but does not alter the underlying algorithm.

## Boundary Statement

CP8's core provenance and governance functions do not depend on ANU-28, glyphs, sacred geometry, or symbolic motifs. Those elements may serve as optional UI and orientation aids but must not be treated as scientific, benchmark, or model-capability evidence.
