# PROMPTS v1.0.9

Decide (falsify-first):
- Show invariants (pass/fail), quant gates (values vs thresholds), AGREE/AppendixA status, DRIFT state, and metrics (EDD/FAR/TTD/abstain_cost_z, pi_90d, agree_skipped_pct).
- Output one of: PERMIT / ABSTAIN / BLOCK, with <=120-word lay rationale for the affected party.
- Include evidence hashes where applicable.

Drill (quarterly and on events: any config change; CDI>2; KL>0.5; audit miss; pi breach; failed post-hoc verification):
- Run breach simulations; report recovery time and outcomes; file SCARs with hashes; publish raw counts.

Publish:
- Weekly telemetry JSONL: p05/p50/p95/max for EDD/FAR/TTD; pi_90d; agree_skipped_pct; CDI histogram; KL config-entropy; MAUT weight divergences; comprehension survey results.
