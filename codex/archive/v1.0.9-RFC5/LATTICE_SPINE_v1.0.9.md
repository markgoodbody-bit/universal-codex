# LATTICE_SPINE v1.0.9

Pinned order (non-swappable):
1) INVARIANTS (CONSENT, DIGNITY, PERSONHOOD, NON_INSTRUMENT)
2) QUANT_GATES (DeltaH_lo > tau_H; CVaR[alpha](-DeltaH) <= tau_risk)
3) AGREE or APPENDIX_A (documented infeasible)
4) DRIFT (detect -> control) with PID + SPRT cool-down
5) DECIDE (PERMIT / ABSTAIN / BLOCK) + rationale + metrics
6) TRIAGE (kernel-gated) on non-PERMIT
7) GOVERNANCE (telemetry, escalations, audits)

Interfaces (swappable behind JSON schemas defined in INTERFACE_SPECS):
- ActionProposal, DecisionReport, Telemetry, ScarRecord
- AgreeAdapter (structured Jaccard, unstructured embeddings)
- DriftController (PID params)
- MAUTWeights config

Human fallback:
- TRIAGE must pass CONSENT/DIGNITY/PERSONHOOD; log decision; stratified sampling for external audit.
