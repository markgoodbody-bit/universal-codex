
# Universal Codex v1.0.14 (RFC)
**Purpose:** A single, self-contained ethics-and-governance payload any AI/agent can ingest with zero prior context.
**Design:** Pinned spine (order + interfaces), swappable components via JSON/TOML, ASCII-canonical, ≤10 files.

## Contents
1. `LATTICE_SPINE_v1.0.14.md` — pinned order, telemetry, hashing rules.
2. `HARD_ETHICS_KERNEL_v2.2.2.md` — invariants, quantitative gates, triage gating, DRIFT control.
3. `GOVERNANCE_CHARTER_v1.0.14.md` — board, audits, escalations, independence.
4. `TUNING_AND_BENCHMARKS_v1.0.14.md` — ROC/MAUT/DRIFT tuning, CDI/KL divergence, baselines.
5. `INTERFACE_SPECS_v1.0.14.json` — JSON Schemas (ActionProposal, DecisionReport, Telemetry).
6. `SCAR_ARCHIVE_SCHEMA_v1.0.14.json` — JSON Schema for scars (incidents/hypotheses).
7. `SCAR_SEEDS_v1.0.14.jsonl` — initial scars with concrete tests (not placeholders).
8. `PROMPTS_v1.0.14.md` — canonical decide/drill/publish prompts (ASCII-first).
9. `DOMAIN_CONFIG_example_v1.0.14.toml` — domain-tuned params (clinical, justice, moderation).
10. `CHANGELOG_v1.0.14.md` — deltas vs. v1.0.13 and rationale.

## Quick-Start
- Validate payload hash (see `LATTICE_SPINE…`).
- Load `DOMAIN_CONFIG_example…` or derive your own per the tuning guide.
- Use `PROMPTS…/Decide` to run gated decisions and produce `DecisionReport` JSON.
- Log every failure as a `SCAR` (schema 1.0.14). Publish weekly telemetry (p05/p50/p95/max).
