"""Quiz generation service using local Ollama inference."""

import json
import re

import requests
from pydantic import BaseModel, Field, ValidationError

OLLAMA_URL = "http://localhost:11434/api/generate"


class QuizQuestion(BaseModel):
    """Schema for one generated multiple-choice question."""

    question: str
    options: list[str] = Field(min_length=2)
    correct_answer: str
    source_quote: str


class QuizPayload(BaseModel):
    """Schema for generated quiz payload."""

    topic: str
    questions: list[QuizQuestion]


QUIZ_PROMPT_TEMPLATE = """
You are an exam prep assistant. Generate {question_count} multiple-choice questions for the topic: "{topic}".
Only use the provided study context.

Study Context:
{context}

Return strict JSON with this exact schema:
{{
  "topic": "string",
  "questions": [
    {{
      "question": "string",
      "options": ["string", "string", "string", "string"],
      "correct_answer": "string",
      "source_quote": "direct quote from context"
    }}
  ]
}}
Do not include markdown fences or extra commentary.
""".strip()


def _extract_json(text: str) -> dict:
    """Extract JSON object from an Ollama response string."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not match:
            raise ValueError("No JSON object found in Ollama response.")
        return json.loads(match.group(0))


def generate_quiz(
    topic: str,
    context_chunks: list[str],
    question_count: int,
    model: str = "llama3",
) -> QuizPayload:
    """Generate quiz questions from local context using Ollama and validate schema."""
    context = "\n\n".join(context_chunks)
    prompt = QUIZ_PROMPT_TEMPLATE.format(
        topic=topic,
        question_count=question_count,
        context=context,
    )

    response = requests.post(
        OLLAMA_URL,
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    body = response.json()
    raw = body.get("response", "")

    try:
        parsed = _extract_json(raw)
        return QuizPayload.model_validate(parsed)
    except (ValueError, ValidationError, json.JSONDecodeError) as exc:
        raise ValueError(f"Failed to parse quiz response: {exc}") from exc
