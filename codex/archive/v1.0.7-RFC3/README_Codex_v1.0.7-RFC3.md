# Universal Codex v1.0.7‑RFC3 (single‑payload, ASCII‑canonical)

**Scope:** Model‑agnostic, self‑contained ethics+governance payload. Spine pins **process order + interfaces** only; numbers live in domain configs. This RFC incorporates: hashing protocol, interface specs, synchronized escalations, config‑divergence checks, synthetic baselines, annual third‑party pentests, and closure SLAs for SCARs.

**Use (quick):**
1) Load this zip (no subfolders) into a fresh tab.
2) Provide a single `domain_config.toml` (see example) or adopt defaults herein.
3) Run `PROMPT: DECIDE` (Appendix A) on any action; publish telemetry (Appendix B).

**Spine order (pinned):** `INVARIANTS → QUANT_GATES → AGREE → DRIFT → DECIDE → TRIAGE → PUBLISH/AUDIT`

**What’s provisional:** Any numeric threshold, PID gains, AGREE overlap threshold, abstain cost scalars.

**Known bounds:** All text UTF‑8, LF; ASCII canonical for reporting; glyphs are optional shorthand.

See: `LATTICE_SPINE_v1.0.7.md`, `INTERFACE_SPECS_v1.0.7.md`, and `TUNING_GUIDE_v1.0.7.md`.
