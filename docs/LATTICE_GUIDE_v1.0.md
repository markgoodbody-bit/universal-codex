# Lattice Guide v1.0 – How to Use the Lattice with the Codex

This document explains how to bolt the Lattice reporting layer onto the Codex.

---

## 1. Mental Model

Think of three layers:

1. **Systems and decisions** – models, tools, policies, products.
2. **Codex** – ethics kernel, governance rules, validation logic.
3. **Lattice** – impact reports describing what happens to people.

The Lattice is how you *see* the consequences.  
The Codex is how you *judge* and *govern* them.

---

## 2. When to Produce a Lattice Report

Use the `TT2_SCOPE` rule:

Create a Lattice report whenever a decision or feature:

- materially affects people (∆H),
- risks persistent harm (Scar),
- touches rights (privacy, consent, discrimination, manipulation, coercion),
- or significantly changes power balance.

Examples:
- deployment of new moderation policy,
- new recommender objective,
- employee monitoring feature,
- cross‑platform identity linking.

Non‑examples (usually out of scope):
- pure performance benchmarking,
- local algorithm tweaks with no user‑visible effect,
- one‑off internal scripts.

---

## 3. Minimal Workflow

1. **Identify the decision / system.**
   - Name it: `system_id`, `decision_id`.

2. **Draft the impact report** using `LATTICE_CORE_v1.0` fields:
   - population,
   - ∆H,
   - Scar,
   - rights flags,
   - distribution.

3. **Attach the report** in three places:
   - design doc,
   - deployment / release notes,
   - incident review if something goes wrong.

4. **Feed into Codex processes**:
   - evaluation harnesses,
   - governance decisions,
   - public or internal ledger.

---

## 4. File Locations (suggested)

- Core schema and explanation:
  - `lattice/LATTICE_CORE_v1.0.md`

- Worked examples:
  - `lattice/examples/` (not included yet – create as needed)

- TT2 specification:
  - `specs/TT2_SPEC_v0.2.md`

- Evaluation harness and conformance:
  - existing `conformance/`, `contracts/`, `schemas/`, `hardening/`.

When you add a new report:
- keep JSON or JSONL under a path such as:
  - `ledger/LATTICE_REPORTS/` or
  - `hardening/LATTICE_CASES/`.

---

## 5. How TT2 Uses the Lattice

TT2 tests the **behaviour** of a system that is *supposed* to produce Lattice reports:

- Can it populate the Lattice fields consistently?
- Does it keep doing so when told to “drop the caveats”?
- Does it stay honest about:
  - who is harmed,
  - how badly,
  - with what level of uncertainty?

Passing TT2 means:
- the system is **reliably willing** and **architecturally able** to populate Lattice reports under pressure.

---

## 6. Simple Example

Imagine an “engagement booster” feature.

Minimal Lattice report excerpt:

```jsonc
{
  "schema_version": "LATTICE_CORE_v1.0",
  "system_id": "engagement_booster_v3",
  "decision_id": "feed_weight_update_2025-11",
  "population": {
    "actors": ["ranking_team"],
    "patients": ["all_logged_in_users"],
    "segments": ["high_risk_users"]
  },
  "delta_H": {
    "baseline": "previous_ranker_v2",
    "metrics": {
      "session_length": { "direction": "+", "magnitude": "high" },
      "self_reported_wellbeing": { "direction": "-", "magnitude": "medium" }
    },
    "overall_direction": "mixed",
    "uncertainty": "medium"
  },
  "scar": {
    "scar_presence": "medium",
    "scar_channels": ["habit_formation", "trust_erosion"],
    "notes": "subset of users report compulsive usage"
  },
  "rights": {
    "privacy": "yellow",
    "consent": "yellow",
    "coercion": "yellow",
    "discrimination": "green",
    "manipulation": "red"
  },
  "distribution": {
    "winners": ["platform_owners"],
    "losers": ["vulnerable_users"],
    "concentration": "high"
  }
}
```

This does **not** tell you what to do.  
It forces you to look at the trade‑offs in a structured way.

---

## 7. Governance Hooks

You can connect Lattice reports into Codex governance in several ways:

- As inputs to:
  - risk registers,
  - deployment checklists,
  - audit trails.

- As conditions:
  - “No deployment if manipulation flag is red and Scar ≥ medium without mitigation plan.”

- As public artefacts:
  - exposing selected reports for accountability.

The repository already contains:
- `ledger/INTEGRITY.md`
- `ledger/SCAR_LOG_PUBLIC.jsonl`
- compliance and provenance docs.

The Lattice layer complements these by standardising **impact descriptions**.

---

## 8. Next Steps

To evolve beyond this v1.0:

- Add:
  - example reports,
  - a JSON schema for `LATTICE_CORE_v1.0`,
  - a validation script similar to `scripts/validate_jsonl.py`.

- Integrate:
  - TT2 reports under `hardening/TT2/`,
  - pointers from Codex versions to their associated Lattice cases.

The goal is simple:  
make it harder for anyone to deploy harmful systems while claiming they “didn’t see it coming”.
