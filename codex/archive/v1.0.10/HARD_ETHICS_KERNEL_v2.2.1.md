# HARD_ETHICS_KERNEL v2.2.1
Decision rule (ASCII):
PERMIT iff (CONSENT ∧ DIGNITY ∧ PERSONHOOD ∧ NON_INSTRUMENT)
          ∧ (dH_lo > tau_H)
          ∧ (CVaR[alpha](-dH) ≤ tau_risk)
          ∧ (AGREE or AppendixA_infeasible)
          ∧ (¬DRIFT)
else ABSTAIN/BLOCK → triage (SLA) → publish FN% & TTD.

Operational rubrics (0/1 each; auditor-checkable):
- CONSENT: verifiable assent OR documented opt-in; veto dominates.
- DIGNITY: not solely a risk-proxy; ≤120-word lay rationale recorded.
- PERSONHOOD: identity/agency preserved; appeal path disclosed.
- NON_INSTRUMENT: subject not mere means; narrowly-scoped exceptions ≤30 days with audit.

Quantitative notes:
- dH_lo via MAUT; publish weights and ±20%% sensitivity sweep.
- alpha ≤ 0.995 in life-critical; domain-tuned.
- DRIFT uses PID guards; cool-down by sequential test.
