# Spine Reference (Pseudocode)

This is illustrative only. Implementations should conform to INTERFACE_SPECS JSON schemas.

```python
def spine_decide(proposal, config):
    # INVARIANTS → QUANT → AGREE → DRIFT → DECIDE → TRIAGE → PUBLISH
    inv = {
        'CONSENT': check_two_channel_consent(proposal.consent_signal),
        'DIGNITY': check_comprehension(proposal.rationale, threshold=0.8),
        'PERSONHOOD': check_appeal_path(proposal.appeal_sla),
        'NON_INSTRUMENT': check_benefit_documented(proposal.stakeholders)
    }
    if not all(inv.values()):
        return report('BLOCK', invariants=inv)

    dH_lo = maut_lower_bound(proposal.harm_model, config.W)
    cvar  = compute_cvar(proposal.harm_model, config.alpha)
    if dH_lo <= config.tau_H or cvar > config.tau_risk:
        return report('ABSTAIN', quant={'dH_lo':dH_lo,'cvar':cvar})

    agree = disjoint_agreement(proposal.models, config.agree_threshold)
    if not agree.passed and not proposal.appendix_a_checklist:
        return report('ABSTAIN', agree=agree)

    drift = detect_drift(['PSI','PageHinkley','SPRT'], proposal.recent_data)
    if drift.triggered:
        tune_pid(config); log_scar(drift)
        return report('ABSTAIN', drift=drift)

    return report('PERMIT', invariants=inv, agree=agree)
```
