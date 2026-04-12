FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app
COPY requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt --system
COPY . .

EXPOSE 8080
CMD ["uvicorn", "web.app:app", "--host", "0.0.0.0", "--port", "8080"]
