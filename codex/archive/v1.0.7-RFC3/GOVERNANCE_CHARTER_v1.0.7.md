# Governance Charter v1.0.7 (Synchronized Escalations)

## Independence
- ≥70% arms‑length funding; third‑party beneficial‑ownership verification.
- Board: 5–9 members; no single‑employer majority; operator may veto ≤1 nominee.

## Audits & Heartbeats
- Immutable logs; audit lag ≤72h ⇒ else budget lock.
- Heartbeat: ≥98% SLA compliance in 24h rolling window ⇒ else auto‑freeze overrides.

## Escalation Coordinator (master ladder)
- Triggers: (a) AGREE_SKIPPED cap breach, (b) π(90d) > 20%, (c) audit‑lag miss, (d) dual‑breach any two in 30d, (e) drill failure.
- **Auto actions:**
  - First trigger ⇒ WARN + 72h plan.
  - Any two concurrent ⇒ BOARD REVIEW ≤72h + freeze non‑emergency overrides.
  - Three in 90d ⇒ HOLD: freeze all overrides except safety‑critical list (expires 7d, renewal needs board vote).
- Safety‑critical list is public, minimal, time‑boxed.

## Reviews
- Weekly SCAR review (critical → within 24h). Board notified on critical immediately.
- Pre‑deployment rubric review: quorum ≥75%; independent auditor + affected‑stakeholder rep required.
- Annual third‑party pentest mandated.
