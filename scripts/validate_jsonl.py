import sys, json
from jsonschema import validate, ValidationError
log_path, schema_path = sys.argv[1], sys.argv[2]
schema = json.load(open(schema_path, "r", encoding="utf-8"))
ok = True
for i, line in enumerate(open(log_path, "r", encoding="utf-8"), 1):
    line = line.strip()
    if not line: 
        continue
    try:
        obj = json.loads(line)
        validate(obj, schema)
    except Exception as e:
        print(f"Line {i}: {e}")
        ok = False
if not ok:
    sys.exit(1)