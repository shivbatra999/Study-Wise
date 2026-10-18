"""Document parsing and chunking helpers for StudyWise."""

from pathlib import Path

import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pptx import Presentation


def parse_document(file_path: str) -> str:
    """Extract text content from a local PDF or PPTX file path."""
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix == ".pdf":
        with pdfplumber.open(path) as pdf:
            pages = [(page.extract_text() or "").strip() for page in pdf.pages]
        return "\n\n".join(page for page in pages if page)

    if suffix == ".pptx":
        presentation = Presentation(str(path))
        slide_text: list[str] = []
        for slide in presentation.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text") and shape.text:
                    slide_text.append(shape.text.strip())
        return "\n\n".join(text for text in slide_text if text)

    raise ValueError("Unsupported file type. Only .pdf and .pptx are allowed.")


def chunk_text(
    text: str,
    chunk_size: int = 800,
    chunk_overlap: int = 80,
) -> list[str]:
    """Split extracted text into retrieval-friendly chunks between 200 and 1000 chars."""
    bounded_size = max(200, min(chunk_size, 1000))
    bounded_overlap = max(0, min(chunk_overlap, bounded_size // 4))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=bounded_size,
        chunk_overlap=bounded_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return [chunk for chunk in splitter.split_text(text) if chunk.strip()]
