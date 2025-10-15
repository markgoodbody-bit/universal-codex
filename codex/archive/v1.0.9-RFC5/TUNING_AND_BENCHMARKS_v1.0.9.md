# TUNING_AND_BENCHMARKS v1.0.9

AGREE calibration:
- Define disjointness threshold via hold-out incidents; publish ROC; set threshold to cap false-comfort <= target.
- Dynamic AGREE_SKIPPED cap: max(5%%, 0.5 * FN_baseline). Post-hoc verification <=7d; failures -> SCAR + escalation.
- Publish weekly: agree_skipped_pct; breaches follow WARN/WATCH/HOLD ladder.

DRIFT control:
- Tune PID via simulation; publish gains and sensitivity; reject if instability >10%%.
- Pentest required after ANY config change and when CDI>2 for 2 weeks.

CDI and config-entropy:
- CDI: mean absolute z-score of key thresholds vs peer median per domain family; publish weekly histograms.
- Config-entropy: KL divergence of threshold vectors vs peer median; publish weekly; CDI>2 or KL>0.5 -> SCAR + pentest.

MAUT and cross-domain bounds:
- Publish weights and +-20%% sensitivity sweep.
- Enforce cross-domain bounds: each weight within +-10%% of cross-domain median unless exception SCAR approved.
- Publish KL divergence of weight vectors across domains.

Benchmarks and baselines:
- Compare to prior, un-kernelled, and peer medians. If none, use synthetic baseline approved by auditor.
- Success criteria (per domain): CVaR tail harm <= baseline - 10%%; FN <= baseline + 2%%; pi_90d <= 15%% with zero breaches; audit SLA weeks >= 95%%; comprehension >= 80%% post-deployment.
- ABSTAIN_COST: publish z-scored proxy and definition; report p05/p50/p95/max.

Sampling and comprehension loop:
- TRIAGE external audit sampling >=10%%, stratified by SES, language, region; publish kappa distribution.
- Post-deployment comprehension surveys; target >=80%%; failures -> tuning + SCAR.
