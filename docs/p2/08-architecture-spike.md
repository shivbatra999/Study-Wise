# 8 Prototype Evidence: Architecture Spike

Owner: Nandhan Alahari

| Field | Content |
|---|---|
| Spike ID and title | S-01 Can a student laptop run the model fast enough? |
| Risk or decision it addresses | R1 (laptops too slow), QAS-01 (from QR-01), ADR-04 (model choice); also FR-09 (off-topic refusal) and the answer path of ADR-02 and ADR-03 |
| Question (answerable yes or no) | On a laptop with no discrete GPU, does a local model, given the 3 most relevant lecture pages, answer at least 18 of the 20 benchmark questions within 20 seconds? Asked for an 8B and a 3B model. |
| Set-up | Python harness `run_benchmark.py` (PyMuPDF and the standard library). Ollama 0.34.3 on 127.0.0.1; embedding model `nomic-embed-text`; chat models `llama3.2:3b` and `llama3.1:8b`, both 4-bit. Data: the benchmark set (`docs/benchmark`, PR #30) and its two lecture decks, 71 pages (decks not committed, SH2). One chunk per page, cosine similarity, top 3 pages passed to the model; a 0.55 similarity gate refuses without calling the model. Machine: MacBook Air M3, 8 GB unified memory, macOS 26.0.1, the 8 GB laptop R1 asks for (not the 16 GB reference laptop). Simulated: no user interface and no store. |
| How it was measured | Time from submitting each question to the last token of the answer, including query embedding and retrieval; model loading (cold start) reported separately. Also recorded per question: best similarity score, pages retrieved, whether the expected page was retrieved, and the full answer for QR-03 scoring. The 5 off-topic questions from the benchmark README were run for FR-09. |
| Result (numbers) | **llama3.2:3b:** 20 of 20 within 20 s; median 7.4 s; 18th-fastest 15.1 s; slowest 18.1 s; cold start 13.2 s; 71 pages indexed in 5.5 s; expected page retrieved for 17 of 20; off-topic questions refused 4 of 5. **llama3.1:8b:** 486 s to load and give a first answer, then the laptop froze from swapping and had to be restarted; no benchmark answer completed. **Answer: yes for 3B, no for 8B on 8 GB.** Correctness, one reviewer's provisional read: about 13 of 20 (not the QR-03 result, which needs two reviewers). |
| What it changed or confirmed | Confirmed QR-01 and QAS-01 for a 3B model on 8 GB. Changed ADR-04 to a 3B default (CH-14). Raised R2: correctness, not speed, is now the main risk. Led to ADR-06 (FR-09 needs more than a threshold, CH-17) and risk R9 (broken ligatures in one deck's text, CH-18). Still open: the same run on a 16 GB laptop with both models. |
| Where to see it | `/spikes/S-01/` (moved from `/spike-01`): `run_benchmark.py`, `README.md`, and `results/` (per-question CSV and summary JSON for each run). Harness and results: PR #32, commit bf4e95e. Move to `/spikes/S-01` and the README's decision table: PR #41, commit 5a81270. |
