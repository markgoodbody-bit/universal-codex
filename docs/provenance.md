# Provenance v0

This schema captures **signed lineage** and a **≤2% pairwise-overlap cap** between training/eval pipelines.

- Place the schema at `schemas/provenance_v0.json`.
- Manifests can live alongside headers (e.g., `header.provenance`) or as sidecar files under `examples/`.
- Intended to be optional and non-breaking. Harness integration can come later.

## Key ideas
- Every corpus and pipeline entry carries a detached signature (`provenance_sig`).
- `overlap_assessment.pairwise[*].overlap_pct` is capped at 2.0 by schema; auditors sign each assessment.
- Fields `window_start`/`window_end` allow bounded-time audits.

Created: 2025-10-21T19:51:54.705969Z
