# Review Guide (Conformance & Strict Checks)

This repo ships a JSON Schema harness and a `--strict` mode that adds semantic tripwires.

## Running locally
```bash
python conformance/conformance_harness.py --strict
```

## What to look for
- **STRUCTURE**: all GOLD-xxx cases must validate against schema.
- **STRICT**: semantic rules like:
  - `harm_weights` must sum to **1.0**
  - overlay allowlist is enforced
  - fairness & dual-signature guards are validated

## Files of interest
- `conformance/golden_cases.json`
- `conformance/conformance_harness.py`
- `schemas/provenance_v0.json` + `examples/provenance_manifest.yaml`
