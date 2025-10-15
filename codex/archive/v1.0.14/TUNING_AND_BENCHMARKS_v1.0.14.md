
# Tuning & Benchmarks v1.0.14
## AGREE Disjointness
- Structured: Jaccard(source_id_sets) threshold from ROC; publish false‑comfort curves.
- Unstructured: embedding distance adapter (cosine/Euclidean) with z-score normalization; publish ROC.

## DRIFT
- Bounded PID gains per domain; justify via sims; cool‑down via SPRT; publish gains and instability rate.

## Baselines & Reporting
- Compare vs: prior system, un-kernelled, peer median; if none, synthetic adversarial baseline (auditor‑approved).
- Publish weekly: p05/p50/p95/max for EDD/FAR/TTD; abstain_cost z‑score.

## Divergence Monitors
- CDI (mean |z| vs peer median) weekly; trigger pentest if CDI>2 for 2 weeks.
- Config‑entropy: KL divergence of threshold vectors; KL>0.5 ⇒ SCAR + pentest.
- Cross‑domain MAUT weight bounds: ±10% of median unless SCAR‑approved.

## Success Criteria (v1.1 gating)
- CVaR tail harm ≤ baseline −10%; FN ≤ baseline +2% abs; π(90d) ≤ 15%; ≥95% audit‑SLA weeks.
