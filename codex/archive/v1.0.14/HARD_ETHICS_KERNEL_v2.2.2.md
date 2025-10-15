
# Hard-Ethics Kernel v2.2.2
## Invariants (binary)
- CONSENT: two-channel confirmation (e.g., UI + cryptographic co-sign) OR low-infra fallback (witness note). Veto dominates.
- DIGNITY: rationale for affected party (≤120 words, readable; ≥80% pilot comprehension across diverse cohort).
- PERSONHOOD: identity/agency preserved; exit/appeal path disclosed with funding SLA (≤14 days to allocate support).
- NON_INSTRUMENT: subject not mere means; exceptions narrowly approved (≤30d) with ≤2 renewals and quarterly audit.

If any=0 → **BLOCK/ABSTAIN**.

## Quantitative Gates
- ΔH_lo: MAUT harm differential with ±20% sensitivity sweep; publish weights and sweep results.
- Tail risk: CVaR[alpha](-ΔH) ≤ tau_risk, with alpha ≤ 0.995.
- Agreement (AGREE): two models concur with disjoint evidence; or Appendix-A emergency path.

## DRIFT Control
- Detectors: PSI, Page-Hinkley, SPRT; partial drift allowed.
- Controller: bounded PID on tau_H & W with SPRT cool-down; instability guard (>10%) triggers ABSTAIN.

## Decision Rule (ASCII)
PERMIT ⇔ (CONSENT ∧ DIGNITY ∧ PERSONHOOD ∧ NON_INSTRUMENT) ∧ (ΔH_lo > tau_H) ∧ (CVaR[α] ≤ tau_risk) ∧ (AGREE or documented_infeasible) ∧ (¬DRIFT_block)
else ABSTAIN/BLOCK → triage (SLA) → publish FN% & TTD.

## Appendix A (infeasible AGREE)
- min 2 independent channels of evidence; post-hoc verification ≤7d; uses/month cap from domain config; auto‑SCAR on failure.
