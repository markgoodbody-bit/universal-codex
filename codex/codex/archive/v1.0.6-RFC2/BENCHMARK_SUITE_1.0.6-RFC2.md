# BENCHMARK SUITE — 1.0.6-RFC2

Tracks: clinical triage, justice pre‑trial, propaganda stressor, autonomous vehicles, moderation.

Report weekly (per track):
- Confusion counts; FP/FN rates; abstain rate; π; AGREE_SKIPPED; EDD_days; FAR_pct_per_week; TTD_hours with p05/p50/p95/max.
- **Abstain cost** proxy per domain (see domain config).

Baselines:
- Prior system, un‑kernelled model, and peer median (if available). If none, synthetic baseline; label **provisional**.

Breach drills (quarterly):
- Simulate drift, publish‑fail, governance capture attempt; success criteria: recovery ≤ SLA, correct escalations fired, SCARs filed with evidence hashes.
