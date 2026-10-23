
import hmac
import ipaddress
import json
import os
from pathlib import Path

import httpx
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response

# Keep the existing assistant bound to loopback.
BACKEND_CHAT_URL = "http://127.0.0.1:8000/chat"

TOKEN = os.environ.get("MOBILE_API_TOKEN", "")
HOST = os.environ.get("MOBILE_API_HOST", "")
CERT_FILE = os.environ.get("MOBILE_TLS_CERT", "")
KEY_FILE = os.environ.get("MOBILE_TLS_KEY", "")

MAX_BODY_BYTES = 16 * 1024
MAX_MESSAGE_CHARS = 8000
BACKEND_MESSAGE_FIELD = os.environ.get(
    "BACKEND_MESSAGE_FIELD", "message"
)

app = FastAPI(
    title="OfflineCodingAssistant Mobile Gateway",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)


def validate_configuration():
    if len(TOKEN) != 64 or any(c not in "0123456789abcdef" for c in TOKEN):
        raise RuntimeError(
            "MOBILE_API_TOKEN must be a 64-character lowercase hex token."
        )

    try:
        address = ipaddress.ip_address(HOST)
    except ValueError as exc:
        raise RuntimeError(
            "MOBILE_API_HOST must be your Mac's private IPv4 address."
        ) from exc

    carrier_nat = ipaddress.ip_network("100.64.0.0/10")

    if (
        address.version != 4
        or address.is_loopback
        or address.is_unspecified
        or address.is_multicast
        or address.is_link_local
        or not (address.is_private or address in carrier_nat)
    ):
        if not Path(CERT_FILE).is_file() or not Path(KEY_FILE).is_file():
            raise RuntimeError("TLS certificate or private key file not found.")

    if BACKEND_MESSAGE_FIELD not in {"message", "prompt"}:
        raise RuntimeError(
            "BACKEND_MESSAGE_FIELD must be message or prompt."
        )


def authorize(request: Request):
    supplied = request.headers.get("authorization", "")
    expected = f"Bearer {TOKEN}"

    if not hmac.compare_digest(supplied, expected):
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/mobile/health")
async def health(request: Request):
    authorize(request)
    return {"status": "ok"}


@app.post("/mobile/chat")
async def chat(request: Request):
    authorize(request)

    content_type = request.headers.get("content-type", "")
    if "application/json" not in content_type.lower():
        raise HTTPException(status_code=415, detail="Expected JSON")

    raw = await request.body()
    if len(raw) > MAX_BODY_BYTES:
        raise HTTPException(status_code=413, detail="Request too large")

    try:
        incoming = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise HTTPException(status_code=400, detail="Invalid JSON")

    if not isinstance(incoming, dict):
        raise HTTPException(status_code=400, detail="Expected JSON object")

    message = incoming.get("message")
    if not isinstance(message, str):
        raise HTTPException(
            status_code=422,
            detail="Expected a string field named 'message'",
        )

    message = message.strip()
    if not message:
        raise HTTPException(status_code=422, detail="Message cannot be empty")

    if len(message) > MAX_MESSAGE_CHARS:
        raise HTTPException(status_code=413, detail="Message too long")

    # Translate the mobile contract to the confirmed backend contract.
    backend_payload = {BACKEND_MESSAGE_FIELD: message}

    try:
        async with httpx.AsyncClient(
            timeout=httpx.Timeout(120.0)
        ) as client:
            upstream = await client.post(
                BACKEND_CHAT_URL,
                json=backend_payload,
            )
    except httpx.TimeoutException:
        raise HTTPException(status_code=504, detail="Assistant timed out")
    except httpx.HTTPError:
        raise HTTPException(
            status_code=502,
            detail="Cannot reach local assistant backend",
        )

    # Preserve the backend's status and body, without exposing its headers.
    return Response(
        content=upstream.content,
        status_code=upstream.status_code,
        media_type=upstream.headers.get(
            "content-type", "application/json"
        ),
    )


if __name__ == "__main__":
    validate_configuration()
    uvicorn.run(
        app,
        host=HOST,
        port=8765,
        ssl_certfile=CERT_FILE,
        ssl_keyfile=KEY_FILE,
        access_log=False,
    )
