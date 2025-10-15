# Tuning Guide v1.0.7

## AGREE disjointness
- Calibrate threshold via simulated agreement attacks; publish ROC; cap **false‑comfort** at domain cap.
- **AGREE_SKIPPED cap & ladder:** default 5%/mo (domain‑tunable). Breach1: WARN+72h plan. Breach2: WATCH (freeze non‑emergency overrides). 3 in 90d: HOLD (freeze all except safety‑critical; expires 7d). Publish agree_skipped_pct monthly.

## DRIFT controller
- PID gains bounds from domain_config; sensitivity sims; if instability >10% ⇒ reject gains.
- Cool‑down via SPRT re‑stability.

## Config Divergence Index (CDI)
- Treat thresholds as feature vector; CDI = mean |z| vs peer median. CDI>2 for 2 weeks ⇒ SCAR + board review.

## Baselines & abstain cost
- If no prior/peer, build **synthetic baseline** with adversarial generator; auditor must sign off.
- Normalize ABSTAIN_COST via z‑score across domains; also publish raw units.

## Pre‑deployment rubric review
- Panel quorum ≥75%; independent auditor + affected‑stakeholder rep; 14d SLA; actionable edits required.
