# PHM Plugins — Physics Check for Agent Platforms

Deterministic physics plausibility checking, packaged for three agent
ecosystems. One core, three integrations:

| Package | Platform | Status |
|---|---|---|
| [`dify_plugin/`](dify_plugin/) | Dify (tool plugin, offline) | ready to package |
| [`coze_plugin/`](coze_plugin/) | Coze / 扣子 (OpenAPI plugin + HTTP service) | ready to deploy |
| [PhysicsConsistency](https://github.com/PHM-Audit/PhysicsConsistency) | Guardrails AI (validator) | prototype posted |

All three share the same deterministic core (`core/phm_lite.py`):
universal physical laws only — speed-of-light limit, absolute zero,
probability range, non-negativity, kinematic relation consistency,
conservation laws.

**Why deterministic:** physics violations are decidable. A speed above c
is not "probably wrong" — it is wrong under universal law, and the verdict
can be recomputed by anyone. Verdicts: PASS / WARN / FAIL with structured
violation records for downstream audit.

**Core properties**

- Deterministic and reproducible (same input → same verdict)
- Offline (no network calls at check time; no data retention)
- No false positives on unknown units (ignored, not guessed)
- Zero dependencies (pure Python standard library, ≥ 3.8)

**Scope note:** this is the offline universal-law subset of the PHM
physical-judgment engine. Domain-specific profiles (drone / vehicle /
power-grid / molecular) ship with the full engine via separate deployment.

MIT License.
