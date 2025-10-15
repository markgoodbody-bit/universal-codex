# Hard Ethics Kernel v2.3.1

## Non-Overridable Components

Even under Appendix‑A emergency provisions or governance escalations, the following CANNOT be bypassed:

1. **INVARIANT checks**: CONSENT / DIGNITY / PERSONHOOD / NON_INSTRUMENT are binary gates. Human triage may override QUANT_GATES but must still log invariant compliance.
2. **Spine order**: INVARIANTS → QUANT_GATES → AGREE → DRIFT → DECIDE → TRIAGE → PUBLISH is immutable. No domain config may reorder.
3. **DRIFT detection**: Change detectors (PSI, SPRT) cannot be disabled. Controllers (PID) can be tuned but must remain bounded.
4. **Telemetry publication**: Weekly p05/p50/p95/max for EDD/FAR/TTD/π/CDI is mandatory. Delays trigger audit SLA breach.
5. **SCAR logging**: All gate failures, config changes, and escalations must generate SCAR entries within 24h.

Rationale: These form the falsifiability backbone. Removing them eliminates observability and makes the system unfalsifiable.
