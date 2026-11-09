# Spike S-01: Can a student laptop run the model fast enough?

Owner: Nandhan Alahari · Run on 6 November 2026 · Mitigates risk R1 · Evidence for QR-01 and FR-09

## Result in one paragraph

On an 8 GB laptop, a 3B model meets QR-01 and an 8B model does not run at all. `llama3.2:3b` answered all 20 benchmark questions within 20 seconds (median 7.4 s, 18th-fastest 15.1 s). `llama3.1:8b` took 486 seconds just to load and give its first answer, then pushed the laptop into swap until it froze and had to be force-restarted. Speed is not the 3B model's problem; correctness is. A provisional, single-reviewer read finds about 13 of 20 answers correct, short of the 17 that QR-03 needs, and one of the five off-topic questions was answered from general knowledge instead of refused (FR-09). The 8B model still has to be measured on a 16 GB laptop before the team picks a model.

## Machine and setup

| Item | Value |
|---|---|
| Laptop | MacBook Air M3 (Mac15,12), 8 GB unified memory, macOS 26.0.1. This is the 8 GB laptop R1 asks for. It is not the 16 GB reference laptop in QR-01. |
| Runtime | Ollama 0.34.3, Metal GPU |
| Embedding model | `nomic-embed-text` (274 MB) |
| Chat models | `llama3.2:3b` (2.0 GB), `llama3.1:8b` (4.9 GB), both Q4 quantised |
| Source material | `SEKER_L13_L14_Use_Case_Analysis.pdf` (33 pages) and `SEKER_L15_L16_High_Level_Design.pdf` (38 pages), 71 pages indexed |
| Retrieval | One chunk per PDF page, cosine similarity, top 3 pages passed to the model |
| Off-topic gate | If the best page scores below 0.55, the system refuses without calling the model; otherwise the model is told to refuse when the passages do not answer |
| Timed span | From submitting the question to the last token of the answer, including query embedding and retrieval (QR-01's "submission to completion") |

## QR-01: answer time

| Model | Under 20 s | Median | 18th-fastest | Slowest | Cold start | QR-01 |
|---|---|---|---|---|---|---|
| `llama3.2:3b` | 20 / 20 | 7.4 s | 15.1 s | 18.1 s | 13.2 s | Pass |
| `llama3.1:8b` | not measured | — | — | — | 486 s, then froze | Fail on 8 GB |

The cold start (loading the model for the first question) is reported separately and is not one of the 20 timed answers.

**About the 8B run.** On an 8 GB Mac the 5.7 GB loaded model does not fit in the GPU's share of memory, so Ollama split it 82% GPU and 18% CPU. Swap was already 12 GB full, so the system thrashed. The warm-up answer took 486 s, and the laptop then stopped responding and was reset with the power button. No benchmark answers completed. The harness now writes each row as it finishes, so a future crash keeps the completed rows.

**About run 1.** An earlier 3B run (`results/run1-*`) also passed (18 of 20 under 20 s), but its two slowest answers (33 s and 41 s for under 150 tokens) happened while the machine was under the same memory pressure. Its off-topic count of 5 of 5 also came from a lenient check that counted a speculative answer followed by the refusal sentence as a refusal. The clean rerun after a reboot (`results/llama3.2-3b*`) is the one to cite.

## FR-09: off-topic questions (3B, clean run)

4 of 5 refused. Three were refused by the similarity gate in under 0.1 s. "What is the boiling point of water" passed the gate (score 0.56) and the model refused it. **"Explain how a TCP three-way handshake works" failed:** it scored 0.63 against the sequence-diagram slides, passed the gate, and the model answered from general knowledge.

The gate alone cannot fix this. The lowest-scoring real benchmark question (B04, 0.605) scores below the TCP question (0.632), so no single threshold separates them on this material.

## Retrieval and provisional correctness (3B, clean run)

The expected page was among the three retrieved pages for 17 of 20 questions. The three misses were B02, B04 and B12.

QR-03 must be scored by two team members against `benchmark.csv`, with a third resolving disagreements. **The marks below are one reviewer's provisional read, to show where the model struggles. They are not the QR-03 result.**

| Outcome | Questions |
|---|---|
| Correct, cited at the expected page | B05, B06, B07, B08, B09, B10, B11, B13, B15, B16, B17, B18, B19 (13) |
| Right content, wrong page cited | B02 (cited p.17, the summary slide, instead of p.6) |
| Wrong or incomplete | B01 (levels mislabelled), B03 (names the checklist question instead of the test), B04 (answered about TUCBW with an invented expansion; page not retrieved), B12 (coupling levels; page not retrieved), B14 (wrong views and wrong "+1"), B20 (left out "context", added "stakeholders") |

## Findings for the team

1. **8B is not viable on 8 GB laptops.** If A1 (most students have 16 GB) turns out false in the hardware survey, the default model has to be 3B-class, or CON-03 needs a minimum RAM requirement.
2. **3B is fast enough but probably not accurate enough for QR-03.** Before trading speed for size, it is worth trying retrieval fixes: smaller chunks than a whole slide, more pages in the prompt, and a reranker.
3. **The decks extract with broken ligatures.** In the Chapter 8 PDF, "fi", "ti" and "ff" come out as other characters (for example "files" becomes "Dles", and "activity" loses its "ti"). PyMuPDF and pypdf give the same result, so the problem is in the PDF's font encoding. This probably caused the B12 miss (the coupling slide is badly garbled). It matters for FR-03 and QR-03, because extracting text from real student PDFs is not "solved" just because some text comes out.
4. **FR-09 needs more than a similarity threshold.** One option is to ask the model a separate yes/no question ("do these passages answer the question?") before answering.
5. **Still to do for R1:** run the same script on a 16 GB laptop (Lokesh's 18 GB machine is closest to the QR-01 reference laptop) with both models.

## How to reproduce

```bash
cd spikes/S-01
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
ollama pull nomic-embed-text && ollama pull llama3.2:3b
.venv/bin/python -u run_benchmark.py --decks <folder with the two SEKER_*.pdf decks> \
    --benchmark ../docs/benchmark/benchmark.csv --model llama3.2:3b
```

Close other apps first and run one model at a time. On an 8 GB machine, do not run `llama3.1:8b`. Each run writes `results/<model>.csv` (one row per question, with time, retrieved pages and the full answer) and `results/<model>-summary.json`.
