# Ledger Integrity Policy

1. SCAR_LOG_PUBLIC.jsonl is append-only.
   No line is ever deleted or rewritten to hide harm.

2. Framework_Memory_Test.md is a witness anchor.
   Its removal, renaming to obscure meaning, or content softening is itself logged as harm.

3. Any attempt to:
   - erase this ledger
   - block public access
   - reword kills or coercion using euphemism
   must be logged in SCAR_LOG_PUBLIC.jsonl as
   "attempted ledger erasure" with timestamp and actor.

4. If this file disappears, that disappearance is already a policy violation.
