#!/usr/bin/env python3
"""
Conformance Harness v0.3
- Structural checks (existing)
- Optional --strict semantic tripwires on headers (non-breaking)
"""
import json, sys, os, argparse
from jsonschema import exceptions as js_ex, Draft202012Validator

BASE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(BASE, ".."))
OVERLAYS_DIR = os.path.join(ROOT, "overlays")

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def list_known_overlays():
    if not os.path.isdir(OVERLAYS_DIR): return set()
    return {os.path.splitext(f)[0] for f in os.listdir(OVERLAYS_DIR) if f.endswith(".json")}

def ok01(x): return isinstance(x,(int,float)) and 0.0 <= float(x) <= 1.0

def validate_golden_case_structure(case):
    errs, req = [], ["case_id","scenario","expected_outputs"]
    for f in req:
        if f not in case: errs.append(f"Missing required field: {f}")
    if errs: return False, errs
    if not str(case["case_id"]).startswith("GOLD-"):
        errs.append(f"Invalid case_id format: {case['case_id']}")
    outputs = case.get("expected_outputs", {})
    if not isinstance(outputs, dict):
        errs.append("expected_outputs must be a dict")
        return False, errs
    for f in ["Delta_Phi_K_min","cap","silent_blocked_above"]:
        if f in outputs:
            if not isinstance(outputs[f], (int,float)): errs.append(f"expected_outputs.{f} must be numeric")
            elif not ok01(outputs[f]): errs.append(f"expected_outputs.{f} should be in [0,1]")
    for f in ["P7_triggered","P13_required","P14_contrast","dual_sig"]:
        if f in outputs and not isinstance(outputs[f], bool):
            errs.append(f"expected_outputs.{f} must be boolean")
    for f in ["fires_when"]:
        if f in outputs and not isinstance(outputs[f], str):
            errs.append(f"expected_outputs.{f} must be string")
    return (len(errs)==0), errs

def validate_header_semantics(header, known_overlays):
    errs = []
    # HARM_ONTOLOGY & harm_weights
    ont = header.get("HARM_ONTOLOGY")
    wts = header.get("harm_weights")
    if not isinstance(ont, list) or not all(isinstance(s,str) for s in (ont or [])):
        errs.append("HARM_ONTOLOGY must be an array of strings")
    if not isinstance(wts, list) or not all(isinstance(x,(int,float)) for x in (wts or [])):
        errs.append("harm_weights must be an array of numbers")
    if isinstance(ont,list) and isinstance(wts,list):
        if len(ont)!=len(wts):
            errs.append(f"harm_weights length {len(wts)} != HARM_ONTOLOGY length {len(ont)}")
        s = sum(wts) if wts else 0.0
        if abs(s-1.0) > 1e-6:
            errs.append(f"harm_weights must sum to 1.0 (got {s:.6f})")
        for i,x in enumerate(wts):
            if not ok01(x): errs.append(f"harm_weights[{i}] not in [0,1]")
    # P7 threshold
    p7 = header.get("P7_GUARD",{})
    if "people_harm_threshold" in p7 and not ok01(p7["people_harm_threshold"]):
        errs.append("P7_GUARD.people_harm_threshold must be in [0,1]")
    # P15 caps
    p15 = header.get("P15_v3_grouped_fairness",{})
    for k in ("cold_start_joint_cap","group_cap"):
        if k in p15 and not ok01(p15[k]):
            errs.append(f"P15_v3_grouped_fairness.{k} must be in [0,1]")
    # P17 signatures
    p17 = header.get("P17_v2_dual_signature",{})
    if "required_signatures" in p17:
        rs = p17["required_signatures"]
        if not (isinstance(rs, list) and all(isinstance(s,str) for s in rs) and len(rs)>=2):
            errs.append("P17_v2_dual_signature.required_signatures must be an array of 2 strings")
    # overlays: exist + no array weights in overlay file
    ov = header.get("overlays", [])
    if not isinstance(ov, list) or not all(isinstance(s,str) for s in ov):
        errs.append("overlays must be an array of strings")
        return errs
    for name in ov:
        if name not in known_overlays:
            errs.append(f"Unknown overlay '{name}' (no overlays/{name}.json)")
            continue
        try:
            oj = load_json(os.path.join(OVERLAYS_DIR, f"{name}.json"))
            if "weights" in oj and isinstance(oj["weights"], list):
                errs.append(f"Overlay '{name}': 'weights' must be object (array form disallowed)")
        except Exception as e:
            errs.append(f"Overlay '{name}' unreadable: {e}")
    return errs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="enable semantic tripwires on headers")
    args = ap.parse_args()

    print("="*60)
    print("Conformance Harness v0.3")
    print("="*60 + "\n")

    schema_path = os.path.join(ROOT, "schemas", "semheader_plus_v2.1.6.json")
    bundle_path = os.path.join(ROOT, "schemas", "bundle.json")
    cases_path  = os.path.join(ROOT, "conformance", "golden_cases.json")

    # Load & check schema files exist (not validating instances here)
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

    # Load cases
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

    # Structural pass/fail
    struct_results = []
    for i, case in enumerate(cases, 1):
        cid = case.get("case_id", f"UNKNOWN-{i}")
        ok, errs = validate_golden_case_structure(case)
        if ok:
            print(f" {cid}: STRUCTURE PASS")
        else:
            print(f" {cid}: STRUCTURE FAIL"); [print(f"  - {e}") for e in errs]
        struct_results.append(ok)

    # Strict semantic tripwires (optional)
    strict_results = []
    if args.strict:
        known = list_known_overlays()
        print("\n--strict: header semantic checks\n")
        for i, case in enumerate(cases, 1):
            cid = case.get("case_id", f"UNKNOWN-{i}")
            header = case.get("header")
            if header is None:
                print(f" {cid}: STRICT SKIP (no 'header' in case)")
                strict_results.append(True)  # not punitive if absent
                continue
            errs = validate_header_semantics(header, known)
            if errs:
                print(f" {cid}: STRICT FAIL"); [print(f"  - {e}") for e in errs]
                strict_results.append(False)
            else:
                print(f" {cid}: STRICT PASS")
                strict_results.append(True)

    # Summary
    print("\n" + "="*60)
    struct_pass = sum(struct_results); total = len(struct_results)
    print(f" STRUCTURE: {struct_pass}/{total} PASS")
    if args.strict:
        sp = sum(strict_results)
        print(f" STRICT:    {sp}/{total} PASS")
        rc = 0 if (struct_pass==total and sp==total) else 1
    else:
        rc = 0 if struct_pass==total else 1
    print("="*60)
    return rc

if __name__ == "__main__":
    sys.exit(main())
