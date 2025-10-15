# Universal Codex v1.0.16 — Falsification Patch

Date: 2025-10-15T19:18:01Z

Changes:
- Reopened SCAR-001 due to circular evidence; added attestation schema v1.0.3
- Locked LATTICE_SPINE order (`order_immutable: true`)
- Non-overridable components documented in HARD_ETHICS_KERNEL v2.3.1
- Added External Replication Protocol v1.0
- Added reference spine pseudocode (spec only)
- Added checksum CI and canonical SHA256 script
- Staged SCAR proposals for v1.0.17 (005–010)

Packaging:
This ZIP is flat per project discipline. Place files into:
  * codex/v1.0.16/: SCAR_*.jsonl, LATTICE_SPINE_*.json, HARD_ETHICS_KERNEL_*.md, README_*.md
  * docs/: REPLICATION_PROTOCOL_v1.0.md
  * scripts/: canonical_sha256.py
  * tools/: spine_reference.md
  * .github/workflows/: validate-checksums.yml
