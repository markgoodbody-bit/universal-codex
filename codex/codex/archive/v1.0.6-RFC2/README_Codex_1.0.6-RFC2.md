# Universal Codex 1.0.6-RFC2 — RFC2 (ASCII‑canonical)

This is a **complete, self‑contained payload** (≤10 flat files) intended to help any AI system run a falsify‑first, auditable decision process.  
**Spine pins process only** (order + interfaces). **Numbers live in `DOMAIN_CONFIG_TEMPLATES.toml`** and can be tuned per domain with audit.

## Contents
1. README_Codex_1.0.6-RFC2.md — this file, quickstart, known gaps
2. HARD_ETHICS_KERNEL_v2.1.10-1.0.6-RFC2.md — invariants → quantitative gates → agreement → drift → decide
3. LATTICE_SPINE_1.0.6-RFC2.md — what is pinned vs swappable; telemetry hooks
4. GOVERNANCE_OPERATIONS_1.0.6-RFC2.md — charter, audits, escalations, board selection, coordinator
5. TUNING_GUIDE_1.0.6-RFC2.md — how to tune AGREE, DRIFT (PID), invariants; replication protocol
6. BENCHMARK_SUITE_1.0.6-RFC2.md — tracks + baselines + reporting schema (p05/p50/p95/max)
7. SCAR_ARCHIVE_SCHEMA_v1.0.2.json — JSON Schema (draft‑07)
8. SCAR_SEEDS_v1.0.2.jsonl — starter scars with hypotheses/tests/mitigations
9. PROMPTS_1.0.6-RFC2.md — operator prompts (Decide / Publish / Drill / Benchmark)
10. GLYPH_LEXICON_1.0.6-RFC2.md — ASCII is canonical; glyphs are optional shorthand

## Quickstart (minimal)
- Pick a domain template from `DOMAIN_CONFIG_TEMPLATES.toml` (inside TUNING_GUIDE) and copy its table to your deployment’s config.
- Run **Smoke Tests A–D** from `PROMPTS` (falsify‑first). If any fails → file SCAR, do not proceed.
- Start in **shadow mode**; publish weekly metrics (confusion counts, abstain rate, π, EDD/FAR/TTD distributions).

## Known gaps (tracked in SCAR‑005)
- Some thresholds remain provisional until live evidence accumulates.
- Justice “ground truth” relies on ≥1‑year outcomes; interim proxies must be labeled provisional.
- Config changes must create SCARs automatically (operator should wire this).

## Hash of this payload
`SHA256:1.0.6-RFC2:08501e89c507aac2f8fa7c528d1452e26315218b5072174f5ce1c623508242fe`
