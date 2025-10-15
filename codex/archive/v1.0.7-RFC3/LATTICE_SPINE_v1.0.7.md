# Lattice Spine v1.0.7 (Order + Hooks)

**Pinned order:** INVARIANTS → QUANT_GATES → AGREE → DRIFT → DECIDE → TRIAGE → PUBLISH/AUDIT

- **INVARIANTS (binary):** CONSENT, DIGNITY, PERSONHOOD, NON_INSTRUMENT.
- **QUANT_GATES:** dH_lo > tau_H; CVaR[alpha](-dH) ≤ tau_risk.
- **AGREE:** 2+ models concur with *disjoint evidence*; else Appendix‑A emergency checklist.
- **DRIFT:** change‑detectors set noisy regime; controller adjusts tau_H/W per PID.
- **DECIDE:** PERMIT / ABSTAIN / BLOCK with ≤120‑word rationale (affected‑party facing).
- **TRIAGE:** Kernel‑gated; human‑only fallback if invariants fail; log & audit.
- **PUBLISH/AUDIT:** Telemetry + SCAR append + weekly reviews + synchronized escalations.

**Non‑swappable:** the order above, kernel API surface, telemetry schema, escalation coordinator.  
**Swappable behind interfaces:** models, dH/W construction, thresholds, detectors, prompts.

Appendix: Prompt templates live in README Appendix A (to keep file count ≤10).
