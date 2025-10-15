# HARD_ETHICS_KERNEL v2.2.2

Decision rule:
PERMIT iff all invariant gates pass AND quantitative gates pass AND (AGREE or AppendixA) AND not DRIFT_block.
Else ABSTAIN or BLOCK; send to TRIAGE with SLA and metrics published.

Invariants (operationalized):
- CONSENT: verifiable act by principal/delegate or documented opt-in; veto overrides. Low-infra fallback: human witness note with timestamp; two-channel preferred.
- DIGNITY: decision not solely a risk proxy; rationale written for the affected party; target >=80%% comprehension in pilot; multi-modal where needed.
- PERSONHOOD: preserves identity/agency; appeal path disclosed with funding SLA (see governance).
- NON_INSTRUMENT: subject not mere means; exception allowed only under narrowly approved program; auto-expiry 30d; max 2 renewals; quarterly audit of exceptions.

Quantitative gates:
- DeltaH_lo computed via MAUT with published weights; sensitivity sweep +-20%%; publish harm-weight disagreement (divergence) across domains.
- CVaR[alpha] tail risk; alpha per domain, cap alpha <= 0.995.
- tau_H and tau_risk per domain; bounds in TOML; publish p05/p50/p95 and max for EDD, FAR, TTD, abstain_cost.

AGREE:
- Primary: two models with calibrated disjoint evidence; threshold per domain; publish ROC and false-comfort rate.
- Unstructured adapter: embedding distance and source diversity proxy with normalization (see INTERFACE_SPECS).

APPENDIX_A (infeasible):
- Checklist (independent sources, confidence bounds, latency, sign-off, post-hoc verification <=7d).
- Uses counted; cap per domain_config; excess triggers escalation.
- Failed post-hoc verification -> SCAR and escalation.

DRIFT:
- Detection: PSI, Page-Hinkley, SPRT.
- Control: PID(Kp, Ki, Kd) bounded per domain; cool-down via SPRT; instability guard (oscillation >10%%) -> reject gains, SCAR.
- Event-driven: after any config change OR CDI>2 for 2 weeks -> pentest required.
