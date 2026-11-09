# Study-Wise 📚🧠

Study-Wise is a private, local-first AI study assistant designed to help students master their course materials. Instead of uploading your dense lecture notes, textbooks, and slide decks to a third-party cloud service, Study-Wise runs entirely on your machine. It securely parses your documents, indexes them locally, and uses a local Large Language Model (via [Ollama](https://ollama.com/)) to help you review key concepts, ask questions, and generate custom practice quizzes.

---

## Key Features

* **100% Private & Local:** All your study materials and AI interactions stay on your device. No cloud storage, external API keys, or subscriptions required.
* **Document Ingestion:** Drop in your course PDFs and PowerPoint slide decks to instantly index your curriculum.
* **Smart Quiz Generation:** Automatically generate targeted multiple-choice or short-answer practice questions based directly on your uploaded lectures.
* **Interactive Q&A:** Query your notes using Retrieval-Augmented Generation (RAG) to get precise answers grounded in your specific class materials.

---

## Getting Started

### Prerequisites
Make sure you have the following installed on your machine:
* Python 3.10 or higher
* Node.js & npm
* [Ollama](https://ollama.com/) (running locally)

### 1. Set Up the Backend
Open your terminal in the root project directory and run:

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install required Python packages
pip install -r backend/requirements.txt

## Course deliverables (CS 3354)

| Milestone | Where |
|---|---|
| P1 Requirements (v0.6) | Section files `00-…` to `06-…` in the repository root; diagrams in `docs/p1/diagrams` |
| P2 Analysis and High-Level Design (v1.0) | `docs/p2/` (section files and `Study-Wise_P2_v1.0.pdf`); diagrams in `docs/p2/diagrams`; tag `p2` |
| Benchmark set | `docs/benchmark` |
| Elicitation (survey, interviews) | `docs/elicitation` |
| Spike S-01 | `spikes/S-01` |
| AI use log | `data/ai-use-log.md` |
