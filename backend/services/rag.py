"""Local RAG indexing and retrieval helpers for StudyWise."""

from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

_CHROMA_DIR = Path(__file__).resolve().parents[1] / "data" / "chroma"
_CHROMA_DIR.mkdir(parents=True, exist_ok=True)

_CLIENT = chromadb.PersistentClient(path=str(_CHROMA_DIR))
_COLLECTION = _CLIENT.get_or_create_collection(name="studywise_documents")
_MODEL = SentenceTransformer("all-MiniLM-L6-v2")


def index_chunks(document_id: str, chunks: list[str]) -> int:
    """Embed and index text chunks for a document, returning indexed chunk count."""
    if not chunks:
        return 0

    embeddings = _MODEL.encode(chunks).tolist()
    ids = [f"{document_id}:{i}" for i in range(len(chunks))]
    metadatas = [{"document_id": document_id} for _ in chunks]

    _COLLECTION.upsert(
        ids=ids,
        documents=chunks,
        metadatas=metadatas,
        embeddings=embeddings,
    )
    return len(chunks)


def query_chunks(topic: str, k: int = 5) -> list[str]:
    """Retrieve the top-k relevant chunk texts for a study topic query."""
    top_k = max(1, min(k, 20))
    embedding = _MODEL.encode([topic]).tolist()
    result = _COLLECTION.query(query_embeddings=embedding, n_results=top_k)
    documents = result.get("documents", [])
    if not documents:
        return []
    return [doc for doc in documents[0] if doc]
