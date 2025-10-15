# Universal Codex v1.0.9-RFC5 (standalone)

Status: RFC (request for comment). Process is pinned; numbers are tunable per domain config.
Scope: single zip, flat files (<=10). ASCII is canonical.

Core: INVARIANTS -> QUANT_GATES -> AGREE/APPENDIX_A -> DRIFT -> DECIDE -> TRIAGE -> GOVERNANCE.
Spine pins order and interfaces. Models, thresholds, and adapters are swappable via JSON/TOML.

This RFC addresses critiques from RFC4:
- Hashing protocol with backup validators and SLA.
- Unstructured AGREE adapter (embeddings) + normalization.
- Event-driven pentests after ANY config change and CDI>2.
- Weekly publication: Config Divergence Index (CDI) histograms and config-entropy (KL) metric.
- Cross-domain MAUT weight bounds and divergence reporting.
- SCAR closure SLA: >=1 closed per domain per quarter with replication (kappa>=0.7 or p<0.05).
- Triage gating, stratified human sampling, lay-comprehension feedback loop.
- Appeals funding SLA and NON_INSTRUMENT renewal cap.
- Tightened governance thresholds, synchronized escalations.

Known limits called out with deadlines:
- Multi-agent/graph spine adapter: RFC by 2026-06-30.
- Cross-domain harm normalization remains approximate; bounds added (see TUNING_AND_BENCHMARKS).

Hashing protocol (summary):
- Canonical SHA256 over alphabetical filenames; LF line endings; JSON/TOML minified; concat with '\n' between files.
- Third-party validator list (primary, two backups). Validate within 72h or auto-escalate (budget lock).

See each file for details.
