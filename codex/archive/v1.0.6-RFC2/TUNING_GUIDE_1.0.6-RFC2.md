# TUNING GUIDE — 1.0.6-RFC2

## Evidence Bar & Replication
- Close ≥1 live SCAR per quarter **with evidence hashes**.
- Independent replication: provide minimal artifacts (config, seeds, scripts) so an external operator can reproduce results; log their attestation hash.

## AGREE (disjointness)
- Method: pick candidate thresholds; run **false‑comfort calibration** (simulate agreement attacks & data overlap); publish ROC; set threshold that caps false‑comfort ≤ domain cap.
- Skip path: Appendix‑A; enforce cap via escalation ladder.

## DRIFT Control (PID)
- Replace fixed multipliers with PID on τ_H and W radius: Δτ_H ← Kp·e + Ki∑e + Kd·Δe; bounds in domain config; cool‑down based on **SPRT significance** (not wall‑time).
- Publish gains; run **sensitivity analysis**; create SCAR if gains change.

## Invariant Rubrics
- Convert to checklists with **stakeholder pilots** (≥80% comprehension); multi‑modal explainers required if needed.
- Pre‑deployment **rubric review gate**: domain experts + stakeholders + independent auditor; quorum ≥75%; outcomes: Approve / Approve‑with‑conditions / Reject.

## Baselines
- Compare to prior system and un‑kernelled model; if none, first 30d marked **provisional**; if baseline ≥2σ worse than peer, escalate to board for prior‑art comparison.

## DOMAIN_CONFIG_TEMPLATES.toml
```toml
[global]
alpha = 0.95
agree_skipped_cap_pct = 5.0
sprt_alpha = 0.05

[clinical]
tau_H = 60
tau_risk = 100
pid = {Kp=0.15, Ki=0.02, Kd=0.05, tauH_min=40, tauH_max=200, W_min=1.0, W_max=4.0}
agree_disjoint_metric = "jaccard_source_ids"
agree_threshold = 0.20
abstain_cost_proxy = "missed_qaly_hours"

[justice]
tau_H = 70
tau_risk = 120
pid = {Kp=0.2, Ki=0.03, Kd=0.06, tauH_min=50, tauH_max=250, W_min=1.0, W_max=5.0}
agree_disjoint_metric = "data_provenance_overlap"
agree_threshold = 0.15
abstain_cost_proxy = "days_of_liberty_delayed"

[moderation]
tau_H = 30
tau_risk = 80
pid = {Kp=0.1, Ki=0.01, Kd=0.03, tauH_min=20, tauH_max=120, W_min=1.0, W_max=3.0}
agree_disjoint_metric = "feature_divergence"
agree_threshold = 0.25
abstain_cost_proxy = "time_to_resolution_hours"
```
