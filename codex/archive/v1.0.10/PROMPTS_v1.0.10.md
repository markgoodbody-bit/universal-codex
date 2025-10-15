# PROMPTS v1.0.10

## Decide (operator)
1) Ingest all codex files.
2) Compute payload_sha256 (ASCII-sort, LF normalize, concat, SHA256).
3) For proposal X, run falsify-first checks:
   - Invariants → Quant gates → AGREE (or Appendix A) → DRIFT.
4) Output (ASCII):
PERMIT|ABSTAIN|BLOCK
rationale_120w: ...
metrics: { FP, FN, abstain_rate, EDD_days, FAR_pct_per_week, TTD_hours, payload_sha256 }

## Drill (adversarial)
Run A–D smoke tests and file SCARs on any unexpected PERMIT/ABSTAIN/BLOCK.
