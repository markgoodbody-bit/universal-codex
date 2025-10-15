# Hard-Ethics Kernel v2.2.1 (RFC)

## Invariants (0/1 each; any 0 ⇒ PERMIT fails)
- CONSENT: two‑channel confirmation (independent modalities) **or** low‑infra fallback (human witness + signed note). **Veto dominates**; if conflicting, ABSTAIN. Timeout ⇒ ABSTAIN.
- DIGNITY: audience‑scored comprehension ≥80% in diverse pilot (multi‑modal allowed). No solely-risk-proxy labeling in the rationale. Publish lay rationale (<120 words) + technical note.
- PERSONHOOD: identity/agency preserved; explicit appeal path with SLA published and **funding disclosure**.
- NON_INSTRUMENT: subject not mere means; exception narrowly‑scoped ≤30d, max **2 renewals**, each logged and justified.

## Quantitative gates
- ΔH_lo := min_w ΔH·w over uncertainty set W (document weights & ±20% sensitivity).
- CVaR[α](-ΔH) ≤ τ_risk; α domain‑tuned with **α ≤ 0.995**.
- τ_H domain‑tuned; publish baseline & sensitivity curves.

## Agreement
- Prefer **AGREE**: ≥2 models with disjoint evidence; domain threshold on disjointness (e.g., Jaccard or adapter metric) published via ROC.
- If **AGREE infeasible**: Appendix‑A checklist (source diversity, latency, bounds, sign‑off, expiry) + **post‑hoc verification ≤7d**.
- AGREE_SKIPPED monthly cap = max(5%, 0.5 × FN_baseline). Breaches follow WARN/WATCH/HOLD ladder.

## Drift control
- Detect: PSI/Page‑Hinkley/SPRT; **control** via PID on τ_H and W radii (bounded gains; instability >10% ⇒ reject params). Cool‑down via SPRT; publish Kp/Ki/Kd.

## Decision & Triage
- Decide: PERMIT iff all gates pass; else ABSTAIN/BLOCK → TRIAGE.
- TRIAGE is kernel‑gated by invariants; failing TRIAGE ⇒ human‑only with audit.

