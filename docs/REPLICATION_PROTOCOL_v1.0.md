# External Replication Protocol v1.0

## Purpose
Define what "replicated_by_external=true" means for SCAR closure.

## Requirements

### 1. Independence
Replicator must be:
- Different legal entity than operator
- No financial dependency (>10% revenue from operator disqualifies)
- No shared board members/investors at time of replication

### 2. Methodology verification
Replicator must:
- Receive hypothesis, tests, and calibration method
- Generate independent test data OR use operator's data with different tooling
- Document any deviations from original methodology

### 3. Statistical criteria
Replication succeeds if one holds:
- κ (Cohen's kappa) ≥ 0.7 for classification agreement, OR
- p < 0.05 for null-hypothesis test, OR
- Effect size within 20% of original (continuous metrics)

### 4. Attestation format (JSON)
{
  "scar_id": "Scar-YYYYMMDD-NNN",
  "attestor_id": "org_name",
  "attestor_pubkey_fingerprint": "SHA1 of PGP/GPG key",
  "replication_date": "ISO8601",
  "methodology_deviations": ["list"],
  "statistical_result": {"metric":"kappa|p_value|effect_size","value":0.73,"meets_threshold":true},
  "report_sha256": "hash-of-full-report",
  "signature": "GPG detached signature of this JSON"
}

### 5. Publication
- Add attestation JSON to SCAR evidence array
- Publish full report at stable URL
- Signature verifiable via public keyserver

## Rejection criteria
- Replicator not independent (§1)
- Statistical threshold not met (§3)
- Report not published or signature invalid
- Methodology deviations >50% of original plan
