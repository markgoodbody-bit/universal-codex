# LATTICE_SPINE v1.0.10
Pinned process order (non-swappable):
1) INVARIANTS → 2) QUANT_GATES → 3) AGREE → 4) DRIFT → 5) DECIDE → 6) TRIAGE → 7) PUBLISH

Interfaces (JSON):
- ActionProposal: { "id": "...", "domain": "...", "context": {...} }
- DecisionReport: { "id": "...", "permit": true|false|null, "rationale": "...", "metrics": {...} }

Outputs must include: FP, FN, abstain_rate, EDD_days, FAR_pct_per_week, TTD_hours, payload_sha256.
