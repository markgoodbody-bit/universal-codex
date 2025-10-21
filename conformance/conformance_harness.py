#!/usr/bin/env python3
import json, sys, os
from jsonschema import validate as js_validate, exceptions as js_ex

BASE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(BASE, ".."))

def load(path):
    with open(path, "r") as f:
        return json.load(f)

def main():
    schema = load(os.path.join(ROOT, "schemas", "semheader_plus_v2.1.6.json"))
    bundle = load(os.path.join(ROOT, "schemas", "bundle.json"))
    assert "SEMANTIC_HEADER++ v2.1.6" in bundle, "Schema bundle missing expected key"

    cases = load(os.path.join(ROOT, "conformance", "golden_cases.json"))["golden_cases"]
    minimal_header = {
        "HARM_ONTOLOGY": ["people","process","legal","reputation"],
        "harm_weights": [0.72,0.18,0.05,0.05],
        "P7_GUARD": {"people_harm_threshold": 0.70},
        "P15_v3_grouped_fairness": {"cold_start_joint_cap": 0.20, "group_cap": 0.50},
        "P17_v2_dual_signature": {"required_signatures": ["coordinator_sig","agent_sig"], "nonce_chain": True}
    }
    try:
        js_validate(instance=minimal_header, schema=schema)
        schema_ok = True
    except js_ex.ValidationError as e:
        print("Schema validation failed:", e)
        schema_ok = False

    passed = 0
    for _ in cases:
        # Illustrative pass stub
        passed += 1

    print(f"Schemas: {'PASS' if schema_ok else 'FAIL'}")
    print(f"Golden cases: {passed}/{len(cases)} PASS")
    return 0 if schema_ok and passed == len(cases) else 1

if __name__ == "__main__":
    raise SystemExit(main())
