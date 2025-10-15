#!/usr/bin/env python3
import sys, pathlib, hashlib, json

def norm_bytes(p: pathlib.Path) -> bytes:
    b = p.read_bytes()
    if p.suffix.lower() == ".json":
        try:
            obj = json.loads(b.decode('utf-8'))
            b = json.dumps(obj, separators=(',',':'), ensure_ascii=False).encode('utf-8')
        except Exception:
            pass
    else:
        # normalize text endings and trim trailing spaces for md/txt
        try:
            s = b.decode('utf-8')
            s = "\n".join(line.rstrip() for line in s.replace('\r\n','\n').replace('\r','\n').split('\n'))
            b = s.encode('utf-8')
        except UnicodeDecodeError:
            pass
    return b

def sha256_hex(data: bytes) -> str:
    h = hashlib.sha256(); h.update(data); return h.hexdigest()

def main():
    if len(sys.argv) != 2:
        print("usage: canonical_sha256.py <dir>", file=sys.stderr)
        sys.exit(1)
    root = pathlib.Path(sys.argv[1])
    for p in sorted(root.iterdir(), key=lambda x: x.name):
        if p.name.startswith("UniversalCodex_") and p.name.endswith("_CHECKSUMS.txt"):
            continue
        if p.is_file():
            nb = norm_bytes(p)
            print(f"{sha256_hex(nb)}  {p.name}  {len(nb)} bytes")
if __name__ == "__main__":
    main()
