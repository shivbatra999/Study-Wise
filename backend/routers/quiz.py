"""Document ingestion and quiz generation API routes."""

from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel, Field

from backend.services.ingestion import chunk_text, parse_document
from backend.services.quiz import QuizPayload, generate_quiz
from backend.services.rag import index_chunks, query_chunks

router = APIRouter(tags=["studywise"])

_UPLOAD_DIR = Path(__file__).resolve().parents[1] / "data" / "uploads"
_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class QuizRequest(BaseModel):
    """Quiz generation request body."""

    topic: str = Field(min_length=2)
    question_count: int = Field(default=5, ge=1, le=20)


@router.post("/api/v1/documents/upload")
async def upload_document(file: UploadFile = File(...)) -> dict[str, str | int]:
    """Ingest an uploaded study document and index its chunks locally."""
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in {".pdf", ".pptx"}:
        raise HTTPException(status_code=400, detail="Only PDF and PPTX files are supported.")

    doc_id = f"doc-{uuid4().hex}"
    target = _UPLOAD_DIR / f"{doc_id}{suffix}"
    content = await file.read()
    target.write_bytes(content)

    text = parse_document(str(target))
    chunks = chunk_text(text)
    indexed = index_chunks(doc_id, chunks)

    return {
        "document_id": doc_id,
        "filename": file.filename or target.name,
        "chunks_indexed": indexed,
    }


@router.post("/api/v1/quiz/generate", response_model=QuizPayload)
def generate_quiz_route(payload: QuizRequest) -> QuizPayload:
    """Generate a context-backed quiz from indexed local study materials."""
    chunks = query_chunks(topic=payload.topic, k=max(payload.question_count * 2, 5))
    if not chunks:
        raise HTTPException(status_code=404, detail="No indexed study material found for this topic.")

    try:
        return generate_quiz(
            topic=payload.topic,
            context_chunks=chunks,
            question_count=payload.question_count,
        )
    except ValueError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
