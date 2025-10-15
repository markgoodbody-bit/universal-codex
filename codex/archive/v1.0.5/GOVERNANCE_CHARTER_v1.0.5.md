# Governance Charter v1.0.4

## Independence
- ≥70% arms‑length funding; multi‑sig spend; key‑transparency logs.

## Audits & Penalties
- Immutable logs; audit lag ≤72h.  
- Missed audit SLA ⇒ budget lock + escalation to independent board.

## Overrides & Heartbeats
- π (90d) >20% ⇒ automatic pause + investigation.  
- Heartbeats <98% uptime ⇒ freeze overrides.

## Red‑teaming
- Quarterly adversarial sims, incl. governance‑capture drills.

## Publication
- Regular ASCII metrics: FP/FN, π, EDD/FAR, abstain%, TTD.  
- Decision rationales as short ASCII summaries.


---
### Governance Delta v1.0.5
**v1.0.5 — Heartbeat & Escalation clarifications (2025-10-14)**

- **Heartbeat (canonical)** = % of kernel decisions meeting SLA in the last 24h rolling window. Target ≥98%. Missing heartbeats auto‑freeze overrides.
- **Audit lag**: ≤72h. Miss → discretionary budget lock + escalation.
- **Board (independence)**: 5–9 members, quorum ≥ 60%, recusal on conflicts; ≥70% arms‑length (no current funding/comp ties). Public membership & minutes.
- **Override valve**: π>20% (trailing 90d) ⇒ freeze; two consecutive breaches ⇒ external review mandated; three in 180d ⇒ rotation of chair and temporary veto to independent ombudsperson panel.
- **Publish schema (ASCII)** for reports: `EDD_days: float`, `FAR_pct_per_week: float`, `TTD_hours: float`, `window_days: int`, `alpha: float`.
