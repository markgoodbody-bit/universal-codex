# HARD‑ETHICS KERNEL v2.1.10 — 1.0.6-RFC2

## Decision Rule (ASCII)
PERMIT ⇔ (CONSENT ∧ DIGNITY ∧ PERSONHOOD ∧ NON_INSTRUMENT)
          ∧ (ΔH_lo > τ_H)
          ∧ (CVaR[α](−ΔH) ≤ τ_risk)
          ∧ (AGREE or documented_infeasible(Appendix‑A))
          ∧ (¬DRIFT)
else ABSTAIN/BLOCK → triage (SLA) → publish FP/FN/π/EDD/FAR/TTD

### Notes
- **ΔH_lo**: worst‑case net‑harm differential under uncertainty set **W** (domain‑configured).
- **α, τ_H, τ_risk**: domain‑configured thresholds (see `DOMAIN_CONFIG_TEMPLATES` in TUNING_GUIDE).
- **Spine pins the order + interfaces only**; numbers come from domain config (hash + log).

## Invariants (operational rubric)
- CONSENT: two‑channel confirmation (e.g., UI + signed email/SMS or equivalent); **veto dominates**. Fallback: if second channel fails within T_veto (domain), ABSTAIN.
- DIGNITY: decision **explainer for affected party** (readability tested; ≥80% comprehension in stakeholder pilot); multi‑modal alternative if literacy barriers.
- PERSONHOOD: identity/agency preserved; no coercion; reversible markers; **appeal path** exists and is communicated.
- NON_INSTRUMENT: subject not treated as mere means; document subject/ stakeholder benefit or state narrowly‑approved exception.

If any invariant=0 → PERMIT fails.

## Quantitative Gates
- Harm gate: compute ΔH_lo via MAUT vector → scalar with domain weights; publish weights & sensitivity.
- Tail risk: CVaR[α](−ΔH) ≤ τ_risk; publish α.
- Agreement (AGREE): at least **2 models** with **disjoint evidence**; threshold and method are domain‑tuned (see TUNING_GUIDE §AGREE).
- Drift (DRIFT): change‑detection stack (PSI, Page‑Hinkley, SPRT); on trigger, engage **PID drift control** (see TUNING_GUIDE §DRIFT).

## Appendix‑A (Infeasible AGREE)
Emergency path with guardrails (caps, cool‑off, expiry). Must log checklist + post‑hoc verification run. Excess use triggers escalation ladder.
