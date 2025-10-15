
# Lattice Spine v1.0.14
**Pinned Order:** INVARIANTS → QUANT_GATES → AGREE → DRIFT → DECIDE → TRIAGE → PUBLISH → AUDIT.
**Non-swappable:** the order, required interfaces, and telemetry fields. Everything else is swappable behind interfaces.

## Telemetry (weekly; rolling 7d & 30d)
- FP, FN, abstain_rate, agree_skipped_pct, EDD_days, FAR_pct_per_week, TTD_hours, pi_override_90d.
- Abstain cost proxy (domain-specific, z-scored). Report p05/p50/p95/max.

## Canonical Hashing (payload integrity)
- Normalize LF endings; UTF-8.
- For each file: if JSON/TOML, minify (no whitespace); if MD, strip trailing spaces.
- Concatenate file bytes in **alphabetical filename order**; compute SHA256.
- Record as `payload_sha256` in DecisionReport.

## Human decisions (fallback)
- Human triage must produce a DecisionReport JSON (same schema); 10% stratified sample to external audit.

## Known Limits
- Multi-agent/graph adapter ETA: 2026‑06‑30 (tracked in SCAR-20251014-006).
