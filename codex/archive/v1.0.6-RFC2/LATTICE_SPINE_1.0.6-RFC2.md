# LATTICE SPINE — 1.0.6-RFC2

Pinned:
1) Invariant checks → 2) Quantitative gates → 3) Agreement/Appendix‑A → 4) Drift control → 5) Decide → 6) Triage (kernel‑gated) → 7) Publish metrics → 8) SCAR logging → 9) Governance escalation.

Swappable (must conform to interfaces):
- Models, weights, W‑construction, thresholds (from domain config), readers/writers.

Telemetry (publish weekly, rolling 7/30d windows; p05/p50/p95/max):
- FP/FN/Abstain counts & rates; π (override); AGREE_SKIPPED rate; EDD_days; FAR_pct_per_week; TTD_hours; drift alarms; abstain‑cost proxy.

Config integrity:
- Every **config change** (thresholds, weights, PID gains, AGREE method) → auto‑SCAR with diff + signer + hash.
