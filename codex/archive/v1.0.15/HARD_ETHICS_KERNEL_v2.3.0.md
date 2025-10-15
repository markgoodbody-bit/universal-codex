# Hard‑Ethics Kernel v2.3.0
PERMIT ⇔ (CONSENT ∧ DIGNITY ∧ PERSONHOOD ∧ NON_INSTRUMENT)
         ∧ (ΔH_lo > τ_H) ∧ (CVaR[α](−ΔH) ≤ τ_risk)
         ∧ (AGREE or Appendix‑A) ∧ (¬DRIFT)
Else ABSTAIN/BLOCK → TRIAGE → publish FN% & TTD.

Invariants:
- CONSENT: 2‑channel; fallback witness+note; veto dominates; timeout ⇒ ABSTAIN.
- DIGNITY: ≥80% comprehension (diverse pilot; multi‑modal allowed).
- PERSONHOOD: appeal path with funding disclosure + SLA.
- NON_INSTRUMENT: exceptions ≤30d; ≤2 renewals; audited.

Quantitative:
- ΔH_lo: MAUT, publish weights, ±20% sensitivity; cross‑domain bounds ±10% median.
- CVaR: α domain‑tuned; α≤0.995 cap.
- DRIFT: PID on τ_H/W with Kp/Ki/Kd bounds; instability guard >10%; SPRT cool‑down.
- AGREE: disjoint‑evidence test (domain threshold); unstructured adapter; dynamic skip cap; ≤7d post‑hoc verify.

TRIAGE is gated by CONSENT/DIGNITY/PERSONHOOD; failures → human‑only (logged, stratified sample ≥10%).
