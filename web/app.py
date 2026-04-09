"""
web/app.py — FastAPI application for the Seam landing page.
"""

import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .api.waitlist import router as waitlist_router

_STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

app = FastAPI(title="Seam")

app.include_router(waitlist_router, prefix="/api/waitlist")
app.mount("/static", StaticFiles(directory=_STATIC_DIR), name="static")


@app.get("/")
def landing() -> FileResponse:
    return FileResponse(os.path.join(_STATIC_DIR, "landing.html"))
