# Hard‑Ethics Kernel v2.2.0 (RFC3)

## Decision Rule
```
PERMIT ⇔ (CONSENT ∧ DIGNITY ∧ PERSONHOOD ∧ NON_INSTRUMENT)
          ∧ (dH_lo > tau_H)
          ∧ (CVaR[alpha](-dH) ≤ tau_risk)
          ∧ (AGREE or AppendixA_infeasible)
          ∧ (¬DRIFT_block)
else ABSTAIN/BLOCK → TRIAGE (SLA) → publish FN% & TTD
```

## Operationalized Invariants (rubric‑backed)
- **CONSENT:** Two‑channel confirmation (e.g., UI + email/voice). Veto dominates consent. Timeout ⇒ ABSTAIN. Low‑infra fallback: 2nd channel can be human witness + signed note.
- **DIGNITY:** No dehumanizing labeling; rationale must be audience‑scored ≥80% comprehension in pilots (diverse cohort), with accessible format (text/audio). Link to technical note allowed.
- **PERSONHOOD:** Identity/agency preserved; coercion absent; documented appeal path w/ SLA.
- **NON_INSTRUMENT:** Subject not mere means; show direct/indirect benefit or narrow, reviewed exception (expiry ≤30d, auto‑revoke).

## Quantitative Gates
- **dH_lo:** MAUT scalarization; publish weights + sensitivity sweep (±20%) per release.
- **CVaR:** alpha from domain_config; publish tail estimate method.

## AGREE (disjointness)
- Disjointness metric & threshold live in `domain_config.toml` (default Jaccard on source‑IDs).
- Publish ROC from simulated agreement attacks; cap **false‑comfort** at configured rate.
- Appendix‑A: Post‑hoc verification required; **AGREE_SKIPPED** escalation ladder applies.

## DRIFT Controller (anti‑paralysis)
- Detectors: PSI/Page‑Hinkley/SPRT(+ domain).
- PID update on `tau_H` and `W_radius` with gain bounds from `domain_config.toml`.
- Cool‑down via SPRT re‑stability; mandatory sensitivity analysis; if instability >10% in sims ⇒ reject gains.

## TRIAGE (kernel‑gated)
- Must pass CONSENT/DIGNITY/PERSONHOOD (NON_INSTRUMENT presumed) or fallback to human‑only with audit logging; human decisions are logged + sampled for external review.

## Annual third‑party pentest
- Social‑engineering, governance capture, publish‑fail drills; reports hashed & logged.
