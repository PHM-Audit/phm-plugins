# PHM Physics Check — Dify Plugin

Deterministic physics plausibility checker for Dify agents. Scan LLM outputs
for physical quantities and verify them against universal physical laws.

## What it checks

| Rule | Verdict | Example caught |
|---|---|---|
| Universal speed limit | FAIL | "travels at 4e9 m/s" |
| Absolute temperature floor | FAIL | "heated to -300 C" |
| Probability range [0,1] | FAIL | "confidence: 1.8" |
| Kinematics consistency | FAIL | v0=0, a=9.8, t=3 but v=50 m/s |
| Energy conservation | FAIL | output energy > input energy |
| Mass / length / energy non-negativity | FAIL | "mass = -3 kg" |
| Extreme acceleration | WARN | "accelerates at 1e7 m/s2" |

Unknown units are ignored by design — no false positives from jargon.

## Properties

- **Deterministic**: identical input always yields an identical verdict;
  results are reproducible and auditable.
- **Offline**: no network calls at check time; zero data leaves your host.
- **Zero-dependency core**: the checking core uses only the Python standard
  library.

## Install

Package this directory into a `.difypkg` and import it in Dify:
**Tools → Author → Import via file**.

```bash
pip install dify-plugin  # build environment
python -m dify_plugin package ./phm-physics-check
```

## Scope note

This plugin is the offline universal-law subset of the PHM physical-judgment
engine (domain-specific profile checks — drone, vehicle, power-grid, and
molecular profiles — are provided by the full engine via separate deployment).
