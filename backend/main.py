"""FastAPI application entrypoint for StudyWise."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers.quiz import router as quiz_router

app = FastAPI(title="StudyWise API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz_router)


@app.get("/health")
def health() -> dict[str, str]:
    """Return a basic service health status."""
    return {"status": "ok"}


@app.get("/api/v1/status")
def api_status() -> dict[str, str]:
    """Return API readiness information for local clients."""
    return {"service": "StudyWise API", "status": "ready"}
