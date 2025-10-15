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


---
### Hardening Delta v1.0.5
**v2.1.9-patch-01 — Operationalized Invariants** (machine-testable, binary)

- CONSENT: principal or authorized delegate has assented (≥1 verifiable act) OR explicit opt‑in default (documented); **veto** always overrides consent.
- DIGNITY: no dehumanizing labeling (not evaluated solely as a risk proxy) **AND** a human‑readable rationale <100 words is recorded.
- PERSONHOOD: identity & agency preserved (no coercion; no permanent marker without exit) **AND** an appeal path exists and is disclosed.
- NON_INSTRUMENT: subject not used as mere means; action confers direct benefit to subject **or** ≥2 stakeholders; exceptions must be documented and auto‑expire ≤30d.

Any invariant = 0 ⇒ PERMIT gate fails (ABSTAIN/BLOCK).

**v2.1.9-patch-02 — AGREE & DRIFT determinization**

- **AGREE_RULE**: require N_models ≥ 2 with **disjoint evidence**: Jaccard(source_id_sets) ≤ 0.10; distinct inference engines (architecture/ensemble family) and disjoint training‑provenance hash sets.
- **Appendix‑A alignment**: when AGREE infeasible, require source‑diversity ≥ 3; otherwise ≥ 2 for standard AGREE. Record branch used.
- **DRIFT_ACTIONS** (triggered by PSI>0.15 or 3σ breach, or Page‑Hinkley/SPRT alarms):
  - widen W: multiply uncertainty radii ×2 (log pre/post W);
  - raise τ_H “one notch”: τ_H ← τ_H × 1.25;
  - publish numeric fields: EDD_days (float), FAR_pct_per_week (float), TTD_hours (float), window_days (int), alpha (float).
