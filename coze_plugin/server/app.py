#!/usr/bin/env python3
"""PHM-Lite HTTP service for Coze / any OpenAPI-based plugin platform.

Thin wrapper around the vendored PHM-Lite core. Stateless, no storage,
no auth by default (add a token check before public deployment).
"""

import sys
from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

sys.path.insert(0, str(Path(__file__).parent))
from phm_lite import full_check  # noqa: E402

app = FastAPI(title="PHM Physics Check", version="1.0.0")


class Kinematics(BaseModel):
    v0: Optional[float] = None
    v: Optional[float] = None
    a: Optional[float] = None
    t: Optional[float] = None
    s: Optional[float] = None
    h: Optional[float] = None


class CheckRequest(BaseModel):
    text: str = Field(..., max_length=20000)
    kinematics: Optional[Kinematics] = None


@app.post("/v1/physics/check")
def physics_check(req: CheckRequest):
    kin = None
    if req.kinematics is not None:
        kin = {k: v for k, v in req.kinematics.model_dump().items() if v is not None}
        if not kin:
            kin = None
    return full_check(req.text, kinematics=kin)


@app.get("/healthz")
def healthz():
    return {"ok": True, "engine": "PHM-Lite", "deterministic": True}
