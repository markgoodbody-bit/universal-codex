# Hard‑Ethics Kernel v2.1.9 (delta A)

## Invariants (binary, must all pass)
- CONSENT
- DIGNITY
- PERSONHOOD
- NON_INSTRUMENT

## Quantitative gates
- Net harm differential (scalarized lower‑bound): `dH_lo = min_w ΔH · w`, with uncertainty set W.
- Tail risk: `CVaR[α](-ΔH) ≤ τ_risk` (default α=0.95).
- Threshold: `dH_lo > τ_H`.

## Agreement
- `AGREE` = two models with **disjoint evidence** concur.
- If infeasible, attach **Appendix A checklist** (documented_infeasible) then proceed **only** if all other gates pass.

## Drift
- If DRIFT=1 (e.g., PSI>0.15, Page‑Hinkley/SPRT breach), **ABSTAIN**; widen W; raise τ_H one notch; publish EDD/FAR.

## Decision rule (ASCII)
```
PERMIT ⇔ (CONSENT ∧ DIGNITY ∧ PERSONHOOD ∧ NON_INSTRUMENT)
          ∧ (dH_lo > τ_H)
          ∧ (CVaR[α](-ΔH) ≤ τ_risk)
          ∧ (AGREE or documented_infeasible)
          ∧ (¬DRIFT)
else ABSTAIN/BLOCK → triage (SLA) → publish FN% & TTD
```

### Defaults (may be tuned per benchmark track)
- τ_H=60, τ_risk=100, α=0.95, FP≤5%, FN≤10% (or domain baseline if stricter).

### Appendix A — Agreement Infeasible Checklist
1) Time/latency constraint documented (why secondary cannot run).  
2) **Source diversity ≥3** (independent channels).  
3) 95% CI for `dH_lo` attached; post‑hoc secondary planned.  
4) Expiry ≤30d; post‑incident review scheduled.  
5) Named signer (role, timestamp).
