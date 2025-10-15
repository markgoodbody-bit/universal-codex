# Prompts (RFC)

## Decide (operator-facing)
Show metrics (invariants, ΔH_lo, CVaR[α], AGREE, DRIFT) → Output PERMIT/ABSTAIN/BLOCK + ≤120‑word lay rationale + tech note + evidence hashes.

## Drill (quarterly)
Simulate: drift spike, AGREE skips surge, publish‑fail, governance capture attempt. Require SCARs with hashes; publish recovery metrics.

## Publish
Emit weekly Telemetry JSONL: p05/p50/p95/max for EDD_days, FAR_pct_per_week, TTD_hours, FP, FN, ABSTAIN_RATE, ABSTAIN_COST (raw + z), π(90d), agree_skipped_pct, CDI, payload_sha256.
