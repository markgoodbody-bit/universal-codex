#!/usr/bin/env python3
"""
Conformance Harness v0.2 - Real Validation
Validates golden cases structural integrity and expected outputs.
"""
import json, sys, os
from jsonschema import validate as js_validate, exceptions as js_ex, Draft202012Validator

BASE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(BASE, ".."))

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def validate_golden_case(case):
    errs = []
    req = ["case_id", "scenario", "expected_outputs"]
    for f in req:
        if f not in case:
            errs.append(f"Missing required field: {f}")
    if errs:
        return False, errs

    if not str(case["case_id"]).startswith("GOLD-"):
        errs.append(f"Invalid case_id format: {case['case_id']}")

    outputs = case.get("expected_outputs", {})
    if not isinstance(outputs, dict):
        return False, ["expected_outputs must be a dict"]

    num_fields = ["Delta_Phi_K_min", "cap", "silent_blocked_above"]
    for f in num_fields:
        if f in outputs and not isinstance(outputs[f], (int, float)):
            errs.append(f"expected_outputs.{f} must be numeric")

    bool_fields = ["P7_triggered", "P13_required", "P14_contrast", "dual_sig"]
    for f in bool_fields:
        if f in outputs and not isinstance(outputs[f], bool):
            errs.append(f"expected_outputs.{f} must be boolean")

    str_fields = ["fires_when"]
    for f in str_fields:
        if f in outputs and not isinstance(outputs[f], str):
            errs.append(f"expected_outputs.{f} must be string")

    def _in01(v): return isinstance(v,(int,float)) and 0.0 <= v <= 1.0
    for f in ["Delta_Phi_K_min","cap","silent_blocked_above"]:
        if f in outputs and not _in01(outputs[f]):
            errs.append(f"{f} should be in [0,1]")

    return (len(errs) == 0), errs

def main():
    print("="*60)
    print("Conformance Harness v0.2 - Real Validation")
    print("="*60 + "\n")

    schema_path = os.path.join(ROOT, "schemas", "semheader_plus_v2.1.6.json")
    bundle_path = os.path.join(ROOT, "schemas", "bundle.json")
    cases_path  = os.path.join(ROOT, "conformance", "golden_cases.json")

    try:
        schema = load_json(schema_path)
        bundle = load_json(bundle_path)
    except FileNotFoundError as e:
        print(f"ERROR: {e}"); return 1
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}"); return 1

    if "SEMANTIC_HEADER++ v2.1.6" not in bundle:
        print("ERROR: Schema bundle missing 'SEMANTIC_HEADER++ v2.1.6' key"); return 1
    print(" Schemas loaded")

    try:
        Draft202012Validator.check_schema(schema)
        print(" Schema is valid Draft 2020-12\n")
    except js_ex.SchemaError as e:
        print(f"ERROR: Schema invalid: {e}"); return 1

    try:
        cases_data = load_json(cases_path)
    except FileNotFoundError:
        print(f"ERROR: Could not find {cases_path}"); return 1
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid golden_cases.json: {e}"); return 1

    if "golden_cases" not in cases_data or not isinstance(cases_data["golden_cases"], list):
        print("ERROR: golden_cases.json missing 'golden_cases' array"); return 1

    cases = cases_data["golden_cases"]
    print(f"Loaded {len(cases)} golden test cases\n")

    results = []
    for i, case in enumerate(cases, 1):
        cid = case.get("case_id", f"UNKNOWN-{i}")
        ok, errs = validate_golden_case(case)
        if ok:
            print(f" {cid}: PASS")
        else:
            print(f" {cid}: FAIL")
            for e in errs: print(f"  - {e}")
        results.append(ok)

    print("\n" + "="*60)
    passed = sum(results); total = len(results)
    if passed == total:
        print(f" SUMMARY: {passed}/{total} cases PASS"); print("="*60)
        return 0
    else:
        print(f" SUMMARY: {passed}/{total} cases PASS")
        print(f"  {total-passed} cases FAILED"); print("="*60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
