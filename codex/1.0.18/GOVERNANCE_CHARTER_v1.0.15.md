# Governance Charter v1.0.15
- Independence: no single‑employer majority; ≤1 operator veto; third‑party ownership verification.
- Quorum: ≥60% (fallback ≥50% if recusals). Safety‑critical list expires in 7d; max 1 renewal (supermajority).
- Audits: ≤72h lag → else discretionary budget lock.
- Validators: primary+2 backups; 72h SLA (48h retry); failure ⇒ SCAR + lock.
- π valve: π(90d) ≤15%; breaches=0; else freeze non‑emergency overrides + board review ≤72h.
- Escalations: AGREE_SKIPPED cap → WARN (72h plan) → WATCH (freeze non‑emergency) → HOLD (freeze overrides).
- SCAR SLA: ≥1 closed per domain/quarter with κ≥0.7 or p<0.05 (replicated_by_external=true).
- Pentests: semi‑annual **and** on any config change or CDI>2 or KL>0.5.
- Human TRIAGE: sample ≥10% stratified; publish κ and outcomes.
