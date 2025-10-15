# GOVERNANCE_CHARTER v1.0.9

Audits and hashing:
- Immutable logs; audit lag <=72h -> else budget lock.
- Hash validation by primary + 2 backups within 72h; if all unavailable, auto-SCAR and board notify; retry 48h.

Escalations (synchronized):
- Dual-breach in 30d (any two of: audit miss, agree_skipped over cap, pi_90d breach, SCAR closure miss, CDI/KL breach) -> BOARD_REVIEW <=72h.
- Non-emergency overrides freeze during review. Safety-critical list allowed, expires 7d; at most 1 renewal; renewal by supermajority.
- pi_90d <= 15%%; any breach -> freeze and review.

Board independence and quorum:
- No single-employer majority; 3rd-party ownership verification.
- Operator may veto <=1 board nominee; publish veto rationale.
- Quorum >=60%%; fallback quorum 50%% if recusals; record recusals.

Pre-deployment rubric review:
- Panel: domain expert, stakeholder rep, independent auditor; 75%% quorum; no single-employer majority.
- SLA 14d (30d for high-stakes). Outcomes: approve / approve-with-conditions / reject.
- Rejection: resubmit to a reconstituted panel nominated by board; operator may veto 1 nominee.

Appeals and exceptions:
- Appeal funding SLA 14d; publish compliance.
- NON_INSTRUMENT exceptions: auto-expire 30d; max 2 renewals; quarterly audit of justifications.
