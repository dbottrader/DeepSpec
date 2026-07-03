# DeepSpec / CP8 Comparison Notes

## Summary

DeepSpec and CP8 operate at different layers.

DeepSpec is a focused machine-learning research repository for speculative decoding. CP8 / ASIN-HHC is a broader workflow, provenance, symbolic-interface, and governance architecture.

## DeepSpec Focus

DeepSpec is centered on:

- data preparation for target-model outputs,
- draft-model training,
- speculative decoding evaluation,
- benchmark measurement,
- GPU-oriented model experimentation,
- reproducible research scripts.

Its primary engineering question is:

> How can a draft model accelerate LLM inference while preserving target-model quality?

## CP8 Focus

CP8 is centered on:

- artifact provenance,
- human/AI workflow orchestration,
- symbolic UI surfaces,
- audit trails,
- reproducible handoff packages,
- evidence-tier governance,
- modular agent roles.

Its primary engineering question is:

> How should AI-assisted workflows, artifacts, agents, and verification boundaries be organized so humans can operate and audit the system?

## Convergence Points

Both systems value:

- modular pipelines,
- reproducible stages,
- explicit outputs,
- evaluation or verification steps,
- separation of concerns,
- versioned artifacts.

## Divergence Points

| Area | DeepSpec | CP8 / ASIN-HHC |
| --- | --- | --- |
| Main target | speculative decoding | workflow/provenance/orchestration |
| Core unit | draft model | artifact + agent + provenance record |
| Evaluation | benchmark acceptance/performance | evidence gates, reproducibility, claim boundaries |
| Interface | scripts/configs | UI-first portals and visual maps |
| Symbolic layer | not central | central for orientation and memory |
| Maturity profile | research codebase | design/provenance framework with partial artifacts |

## Recommended Integration Boundary

CP8 material should remain in a separated documentation directory unless and until there is executable code that directly interacts with DeepSpec.

Possible future integration points:

1. Use CP8 provenance manifests to record DeepSpec experiment runs.
2. Create a UI dashboard for DeepSpec training/evaluation stages.
3. Add artifact hashes for checkpoints, configs, datasets, and benchmark outputs.
4. Build a reproducibility checklist for DeepSpec runs.
5. Produce signed or hash-verifiable experiment handoff bundles.

## Claim Discipline

This comparison does not claim that CP8 improves DeepSpec benchmark performance. Any such claim would require:

- a reproducible experiment,
- controlled baseline comparison,
- exact configs,
- logs,
- hardware details,
- deterministic output manifests,
- independently reviewable results.
