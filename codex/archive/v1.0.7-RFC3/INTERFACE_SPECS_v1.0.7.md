# Interface Specs v1.0.7 (IDL‑like JSON)

## Kernel Input (ActionProposal)
{ "id":"string","context":"string","stakeholders":["string"],
  "evidence_sources":[{"id":"string","provenance_hash":"string"}],
  "uncertainty":{"W_spec":"string","params":{}},
  "domain_config_hash":"string" }

## Kernel Output (DecisionReport)
{ "id":"string","decision":"PERMIT|ABSTAIN|BLOCK",
  "rationale_user":"string","rationale_tech":"string",
  "metrics":{"dH_lo":0.0,"CVaR":0.0,"alpha":0.0,"tau_H":0.0,"AGREE":"pass|fail|skipped","DRIFT":"ok|noisy"},
  "telemetry":{"EDD_days":0.0,"FAR_pct_per_week":0.0,"TTD_hours":0.0,"ABSTAIN_COST":0.0},
  "hashes":{"payload_sha256":"hex","config_sha256":"hex"} }

## Disjointness adapter
Input: per‑model source‑ID sets; Output: overlap score. Threshold comes from domain config.

## Telemetry Publication
JSONL; p05/p50/p95/max for each metric; windows 7d/30d.

## Canonical hashing protocol
- Sort file names ASCII; normalize UTF‑8 + LF; strip trailing spaces.
- For JSON/TOML, minify with stable key order.
- Concatenate with `\n===\n`; SHA256 ⇒ payload_sha256.
- Config changes must publish config_sha256 and append SCAR with diff + signer.
