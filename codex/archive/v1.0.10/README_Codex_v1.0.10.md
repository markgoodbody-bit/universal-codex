# Universal Codex v1.0.10 (RFC)
ASCII-canonical, standalone payload (≤10 files) for lattice ethics + governance.
Spine pins **order + interfaces** only; numbers live in domain configs (not included).
Everything here is safe to share; no secrets, no dependencies.

## Contents
1. README_Codex_v1.0.10.md (this file)
2. LATTICE_SPINE_v1.0.10.md
3. HARD_ETHICS_KERNEL_v2.2.1.md
4. GOVERNANCE_CHARTER_v1.0.10.md
5. BENCHMARK_SUITE_v1.0.10.md
6. GLYPH_LEXICON_v1.0.10.md
7. SCAR_ARCHIVE_SCHEMA_v1.0.2.json
8. SCAR_SEEDS_v1.0.10.jsonl
9. PROMPTS_v1.0.10.md
10. CHANGELOG_v1.0.10.md

## Usage (any LLM / system)
- Unzip; open `README` first.
- For an AI: ingest all files, then run `PROMPTS_v1.0.10.md` → “Decide” or “Drill”.
- For humans: read `SPINE`, `KERNEL`, then `GOVERNANCE` and `BENCHMARKS`.

## Canonical hashing
- Sort filenames ASCII, normalize LF line endings, UTF-8.
- Concatenate bytes; SHA256 over the stream.
- Report as `payload_sha256` in outputs.

## Notes
- This is RFC: thresholds tune per domain; see prompts for smoke tests.
- ASCII is canonical; glyphs are optional shorthands with explicit ASCII mapping.
