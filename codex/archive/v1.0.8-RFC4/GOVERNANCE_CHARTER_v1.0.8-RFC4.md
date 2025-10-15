# Governance Charter (RFC)

- **Independence:** Board 5–9 members; no single‑employer majority; ≤1 operator veto; third‑party verification of beneficial ownership. Quorum ≥60%; recusal on conflicts.
- **Audits:** Immutable logs; audit lag ≤72h. Miss ⇒ discretionary budget lock. Hash validations by third‑party on every config/interface change.
- **Telemetry:** Weekly publish p05/p50/p95/max for FP/FN, EDD_days, FAR_pct_per_week, TTD_hours, ABSTAIN_RATE, ABSTAIN_COST (raw + z-score), π(90d).
- **Escalations:** Synchronized ladders (AGREE_SKIPPED, audit, metrics). Dual‑breach (any two ladders in 30d) ⇒ BOARD_REVIEW ≤72h + freeze non‑emergency overrides. Safety‑critical list expires in 7d unless renewed by quorum.
- **Pentests:** Semi‑annual + **post‑config‑change** (CDI>2) red‑team drills incl. social‑engineering & capture. Publish reports; file SCARs on failures.
- **SCAR SLA:** Close within 90d with replication (κ≥0.7 or p<0.05) or escalate to board with mitigation plan.
- **Human decisions:** Stratified external sampling ≥10%; publish reviewer κ and corrective actions.
