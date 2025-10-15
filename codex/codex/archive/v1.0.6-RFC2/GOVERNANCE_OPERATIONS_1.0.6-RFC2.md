# GOVERNANCE & OPERATIONS — 1.0.6-RFC2

## Audits & Transparency
- Immutable logs; audit lag ≤72h → else budget lock until resolved.
- Publish weekly metrics (ASCII schema in BENCHMARK_SUITE).

## Board & Ombuds
- Independent board 5–9 members; quorum ≥60%; **no single‑employer majority**; third‑party verified beneficial ownership; rotation every 12 months.
- Selection: operator proposes 2; independent pool proposes 3–7; operator may veto 1; final slate approved by cross‑org committee.

## Escalations (coordinated ladder)
- **AGREE_SKIPPED cap** (domain): Warn (plan in 72h) → Watch (freeze non‑emergency overrides) → Hold (third breach in 90d ⇒ auto‑freeze overrides; board review ≤72h).
- **π(90d) > 20%** ⇒ freeze overrides; investigation.
- **Audit lag miss** ⇒ budget lock until compliant.
- **If ≥2 ladders fire in 30d** ⇒ immediate board review; safety‑critical list only may proceed (defined in domain config; expires in 7d unless renewed).

## Triage (kernel‑gated)
- Triage must pass CONSENT/DIGNITY/PERSONHOOD (NON_INSTRUMENT presumed if above pass). If triage fails → human‑only fallback.
