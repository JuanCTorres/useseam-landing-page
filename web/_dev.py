import uvicorn


def main() -> None:
    uvicorn.run("web.app:app", host="0.0.0.0", port=8080, reload=True)
