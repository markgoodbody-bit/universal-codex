# Tuning Guide (RFC)

## AGREE disjointness
- Choose metric: Jaccard (structured) or embedding distance (unstructured).
- Calibrate via **false‑comfort** study: simulate correlated errors; publish ROC; set threshold s.t. miss‑rate ≤ cap.
- Monthly **AGREE_SKIPPED cap** = max(5%, 0.5×FN_baseline). Breach ladder: WARN (plan ≤72h) → WATCH (freeze non‑emergency overrides) → HOLD (freeze all overrides).

## DRIFT control
- PID on τ_H & W radii with bounds; require sensitivity sims; reject params if instability >10%; cool‑down via SPRT.
- Publish Kp/Ki/Kd and stability plots.

## CDI (Config Divergence Index)
- CDI = mean |z| of key thresholds vs peer‑median. Publish weekly. CDI>2 for 2 consecutive weeks ⇒ SCAR + board review; pentest after any CDI>2 event.

## Cross‑domain harm normalization
- Publish MAUT weights + ±20% sweep; report sensitivity. For comparability, publish **z‑scores** of ABSTAIN_COST plus raw units.

## Human triage sampling
- Stratified by domain & stakeholder; external sample ≥10%; report κ and corrective actions.

## α and τ_H
- α ≤ 0.995 (clinical often 0.99–0.995). Document rationale. τ_H curves published with uncertainty.
