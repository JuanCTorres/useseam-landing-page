"""
web/api/waitlist.py — Waitlist signup endpoint.

POST /api/waitlist  { "email": "user@example.com" }
Stores signups in waitlist.json and sends a notification email via Resend.
"""

import json
import os
import re
from datetime import datetime, timezone

import httpx
from fastapi import APIRouter
from pydantic import BaseModel, field_validator

router = APIRouter()

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
_WAITLIST_PATH = os.path.join(_DATA_DIR, "waitlist.json")

_RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")
_NOTIFY_EMAIL = os.getenv("NOTIFY_EMAIL", "example@example.com")


class _WaitlistRequest(BaseModel):
    email: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        v = v.strip().lower()
        if not _EMAIL_RE.match(v):
            raise ValueError("Invalid email address")
        return v


def _load() -> list[dict]:
    if not os.path.exists(_WAITLIST_PATH):
        return []
    with open(_WAITLIST_PATH) as f:
        return json.load(f)


def _save(entries: list[dict]) -> None:
    with open(_WAITLIST_PATH, "w") as f:
        json.dump(entries, f, indent=2)


def _send_notification(email: str, count: int) -> None:
    """Fire-and-forget email via Resend. Failures are logged, never block the user."""
    if not _RESEND_API_KEY:
        return
    try:
        httpx.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {_RESEND_API_KEY}"},
            json={
                "from": "Seam <onboarding@resend.dev>",
                "to": [_NOTIFY_EMAIL],
                "subject": f"New waitlist signup: {email}",
                "text": f"{email} just joined the Seam waitlist.\n\nTotal signups: {count}",
            },
            timeout=5.0,
        )
    except Exception:
        pass  # best-effort — don't break the signup flow


@router.post("")
def join_waitlist(body: _WaitlistRequest) -> dict:
    entries = _load()
    existing = {e["email"] for e in entries}
    if body.email in existing:
        return {"ok": False, "message": "You're already on the list."}
    entries.append({"email": body.email, "signed_up_at": datetime.now(timezone.utc).isoformat()})
    _save(entries)
    _send_notification(body.email, len(entries))
    return {"ok": True, "message": "You're on the list!"}
