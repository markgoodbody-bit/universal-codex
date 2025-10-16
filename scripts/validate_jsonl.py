import json, argparse
from jsonschema import validate

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True)
    ap.add_argument("--file",   required=True)
    args = ap.parse_args()

    with open(args.schema, "r", encoding="utf-8") as f:
        schema = json.load(f)

    ok = True
    with open(args.file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            s = line.strip()
            if not s: 
                continue
            try:
                validate(json.loads(s), schema)
            except Exception as e:
                print(f"Line {i}: {e}")
                ok = False
    raise SystemExit(0 if ok else 1)
