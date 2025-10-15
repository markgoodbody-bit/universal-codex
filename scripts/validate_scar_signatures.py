#!/usr/bin/env python3
import argparse, json, sys, re, datetime

HEX64 = re.compile(r"^[0-9a-fA-F]{64}$")
HEX40 = re.compile(r"^[0-9A-F]{40}$")
PGP_ARMOR_RE = re.compile(r"-----BEGIN PGP SIGNATURE-----[\s\S]+-----END PGP SIGNATURE-----")

def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield i, json.loads(line)
            except json.JSONDecodeError as e:
                print(f"INVALID JSON at line {i}: {e}", file=sys.stderr)
                sys.exit(1)

def tier1_check(e):
    errs = []
    need = ["attestor_id", "attestor_pubkey_fingerprint", "attestation_report_sha256", "attestation_timestamp", "signature"]
    for k in need:
        if k not in e:
            errs.append(f"missing {k}")
    if "attestation_report_sha256" in e and not HEX64.match(e["attestation_report_sha256"]):
        errs.append("attestation_report_sha256 not 64-hex")
    if "attestor_pubkey_fingerprint" in e and not HEX40.match(e["attestor_pubkey_fingerprint"]):
        errs.append("attestor_pubkey_fingerprint not 40 hex uppercase")
    if "signature" in e and not PGP_ARMOR_RE.search(e["signature"]):
        errs.append("signature not PGP armored")
    return errs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", required=True, help="SCAR log JSONL path")
    ap.add_argument("--warn-only-tier2", action="store_true")
    ap.add_argument("--grace-period", type=int, default=7)
    args = ap.parse_args()

    warn_count = 0
    for i, scar in load_jsonl(args.log):
        if not scar.get("replicated_by_external"):
            continue
        ev = scar.get("evidence", [])
        # must contain at least one external attestation object
        externals = [e for e in ev if "attestor_id" in e]
        if not externals:
            print(f"Line {i} ({scar.get('id')}): FAIL tier1 — no ExternalAttestation in evidence", file=sys.stderr)
            sys.exit(1)
        # Tier 1 checks
        errs = []
        for e in externals:
            errs.extend(tier1_check(e))
        if errs:
            print(f"Line {i} ({scar.get('id')}): FAIL tier1 — " + "; ".join(errs), file=sys.stderr)
            sys.exit(1)
        # Tier 2 (simulate network-dependent step with warning only)
        if args.warn-only-tier2:
            deadline = (datetime.datetime.utcnow() + datetime.timedelta(days=args.grace_period)).isoformat() + "Z"
            print(f"WARNING: Tier2 signature verification deferred for {scar.get('id')} (grace until {deadline})")
            warn_count += 1

    if warn_count:
        print(f"TIER2_WARNINGS={warn_count}")
    print("OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
