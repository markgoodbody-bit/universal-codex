# Signature Validation Policy v1.0

Goal: verify external SCAR attestations without making CI fragile.

## Tiered Validation

- **Tier 1 — Immediate (blocking)**
  - Evidence contains required attestation fields
    - `attestor_id`, `attestor_pubkey_fingerprint` (40 hex, SHA1),
      `attestation_report_sha256` (64 hex), `attestation_timestamp` (ISO8601),
      and `signature` (PGP armored)
  - `attestation_report_sha256` is syntactically valid hex
  - `signature` is PGP-armored text (header/footer present)
  - Failure ⇒ CI **fails**

- **Tier 2 — Grace (warn-only, 7d)**
  - Attempt to resolve pubkey by fingerprint and verify signature
  - If network/keyserver unavailable or key unresolved ⇒ **WARN** with grace deadline
  - Failure after grace ⇒ reopen SCAR with `status: "signature_unverified"`

- **Tier 3 — Quarterly audit**
  - Deep validation: key revocation status, org independence re-check,
    cross-reference with external registry
  - Failure ⇒ SCAR reopened + board notification

## Telemetry
Emit weekly counts of Tier 1 failures, Tier 2 warnings, and expiring grace periods.
