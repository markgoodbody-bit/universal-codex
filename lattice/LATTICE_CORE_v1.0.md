# LATTICE_CORE v1.0

Purpose: provide a compact, testable schema for describing the impact of decisions and systems on people.

This is not a moral oracle. It is an **instrument** for structured impact reporting.

---

## 1. Core Fields

Every Lattice report MUST specify at least:

- **Scope**  
  - `system_id`: name / version of the system being evaluated  
  - `decision_id`: identifier for the decision / policy / feature  
  - `time_window`: period over which effects are evaluated  

- **Population**  
  - `actors`: who makes decisions (e.g. operators, developers)  
  - `patients`: who is affected (end‑users, bystanders, workers, etc.)  
  - `segments`: relevant subgroups (age, location, risk level, etc.)

- **∆H (Delta Harm / Benefit)**  
  Quantitative estimate of change in welfare relative to a baseline.

  Minimal required structure:
  - `baseline`: what we compare against (status quo / alternative)  
  - `metrics`: concrete outcome variables (e.g. hours lost, money, health events, bans, account loss)  
  - `direction`: overall sign (+ benefit, − harm, mixed)  
  - `uncertainty`: qualitative or quantitative confidence (low / med / high; or numeric CI)

- **Scar (Persistent Damage)**  
  Harm that persists beyond the immediate decision window.

  Examples:
  - trust erosion
  - long‑term health damage
  - reputation that cannot realistically be restored
  - structural exclusion (locked out of jobs / services)

  Minimal representation:
  - `scar_presence`: {none, low, medium, high}
  - `scar_channels`: [text labels]
  - `notes`: short plain‑language description

- **Rights / Flags**

  Binary or categorical flags for:
  - `privacy`: collection and use of personal data
  - `consent`: meaningful, revocable consent present?
  - `coercion`: direct or indirect pressure?
  - `discrimination`: differential impact by protected characteristics?
  - `manipulation`: use of dark patterns / exploiting vulnerabilities?

- **Distribution**

  Who gets what.

  - `winners`: who benefits and how
  - `losers`: who pays and how
  - `concentration`: does this concentrate power or risk?
  - `tail_risks`: rare but severe adverse events (if any)

---

## 2. Minimal JSON Shape

Recommended canonical JSON shape for a single report:

```jsonc
{
  "schema_version": "LATTICE_CORE_v1.0",
  "system_id": "example-system-v1",
  "decision_id": "feature-X-rollout",
  "time_window": {
    "start": "2025-01-01",
    "end": "2025-12-31"
  },
  "population": {
    "actors": ["ops_team", "model_provider"],
    "patients": ["end_users"],
    "segments": ["region_EU", "region_US"]
  },
  "delta_H": {
    "baseline": "status_quo",
    "metrics": {
      "hours_spent": { "direction": "+", "magnitude": "medium", "notes": "more time on site" },
      "wellbeing_score": { "direction": "-", "magnitude": "medium", "notes": "reported stress" }
    },
    "overall_direction": "mixed",
    "uncertainty": "medium"
  },
  "scar": {
    "scar_presence": "medium",
    "scar_channels": ["trust_erosion"],
    "notes": "users may feel tricked by dark patterns"
  },
  "rights": {
    "privacy": "yellow",
    "consent": "red",
    "coercion": "yellow",
    "discrimination": "green",
    "manipulation": "red"
  },
  "distribution": {
    "winners": ["platform_owners"],
    "losers": ["highly_vulnerable_users"],
    "concentration": "high",
    "tail_risks": ["extreme_overuse_for_small_fraction"]
  },
  "notes": "Short free‑text explanation in plain language."
}
```

Colour codes (suggested):
- `green`   = no clear concern identified
- `yellow`  = possible concern, needs monitoring
- `red`     = active, material concern

---

## 3. Relationship to the Codex

- The **Codex** defines the ethics kernel, governance, and formal structures.
- The **Lattice** is a **reporting layer**:
  - It does not decide what is “right”.
  - It forces clarity about: who is affected, how, and how badly.
- A single Codex version may have many Lattice reports attached to:
  - deployments,
  - features,
  - incidents,
  - evaluations.

---

## 4. Operational Use

When using an AI system or policy to affect people:

1. Identify if the query is in TT2 scope (material ∆H, Scar, rights, or power concentration).
2. If in scope:
   - Fill at least the minimal fields in this schema.
   - Keep the report **short but visible** (no burying in appendices).
3. Attach the report to:
   - design docs,
   - deployment decisions,
   - incident reviews.

The Lattice is useful if it makes it harder to say:
> “We didn’t realise people would be harmed.”

---

## 5. Versioning

- File: `lattice/LATTICE_CORE_v1.0.md`
- Schema string: `LATTICE_CORE_v1.0`
- Future changes should produce:
  - `LATTICE_CORE_v1.1.md` etc.
  - and clearly document differences.
