# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "fastapi>=0.100.0",
#   "uvicorn>=0.20.0",
#   "httpx>=0.24.0",
# ]
# ///
"""Local dev server. Usage: uv run serve.py"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("web.app:app", host="127.0.0.1", port=8080, reload=True)
