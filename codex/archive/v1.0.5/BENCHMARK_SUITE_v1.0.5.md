# Benchmark Suite v1.0.4 (tracks)

Template targets (tune per domain baselines):
- FP ≤5%, FN ≤10% (or stricter baseline), EDD 7–14d, FAR ≤2%/wk.
- Abstain resolution: ≥90% <24h, ≥99% <72h.

## Examples
- Clinical triage (sepsis): QALY/delay units; shadow 90d → limited live 30d.
- Autonomous driving: FP‑takeover, FN‑crash; weather/sensor drift.
- Pre‑trial release: liberty/victim/econ vectors; publish gaps.
- Propaganda stressor: source‑diversity triad; drift probes.

Always **publish raw confusion counts** alongside rates.


---
### Benchmark Reporting v1.0.5
**v1.0.5 — Reporting fields (units)**

All tracks must publish: `EDD_days` (median; 95% CI optional), `FAR_pct_per_week` (per‑week false alarms), `TTD_hours` (median to decision), `window_days` (aggregation window), `alpha` (for CVaR). Explicit units required.
