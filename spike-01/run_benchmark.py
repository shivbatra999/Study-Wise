"""Spike S-01: answer time (QR-01) and off-topic refusal (FR-09) on the benchmark set.

Indexes the two benchmark decks one chunk per PDF page, then for each question:
embed -> cosine top-k -> refuse if the best score is under the threshold -> otherwise
stream an answer from the chat model. The timed span is submit to last token.

Usage:
    python run_benchmark.py --decks DIR --benchmark benchmark.csv --model llama3.2:3b
"""

import argparse
import csv
import json
import math
import platform
import subprocess
import time
import urllib.request
from pathlib import Path

import pymupdf

OLLAMA = "http://127.0.0.1:11434"
NO_MATERIAL = "No material in this course covers that question."
OFF_TOPIC = [
    "Who won the 2022 FIFA World Cup?",
    "What is the boiling point of water at sea level?",
    "Explain how a TCP three-way handshake works.",
    "What is the derivative of sin(x)?",
    "Who wrote Pride and Prejudice?",
]
SYSTEM_PROMPT = (
    "You are a study assistant. Answer the question using ONLY the passages provided. "
    "Be concise (at most 3 sentences). After the answer, cite every passage you used by copying "
    "its header exactly, for example [SEKER_L13_L14_Use_Case_Analysis.pdf p.6]. "
    "If the passages do not contain the answer, reply with exactly this sentence and nothing else: "
    + NO_MATERIAL
)


def post(path, payload, stream=False):
    req = urllib.request.Request(
        OLLAMA + path, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req, timeout=600)
    return resp if stream else json.loads(resp.read())


def embed(texts, model):
    return post("/api/embed", {"model": model, "input": texts, "keep_alive": "30m"})["embeddings"]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def index_decks(deck_dir, embed_model):
    chunks = []
    for pdf in sorted(Path(deck_dir).glob("SEKER_*.pdf")):
        with pymupdf.open(pdf) as doc:
            for page_no, page in enumerate(doc, 1):
                text = " ".join(page.get_text().split())
                if text:
                    chunks.append({"file": pdf.name, "page": page_no, "text": text})
    start = time.perf_counter()
    vectors = []
    for i in range(0, len(chunks), 16):
        batch = chunks[i : i + 16]
        vectors += embed(["search_document: " + c["text"] for c in batch], embed_model)
    for c, v in zip(chunks, vectors):
        c["vec"] = v
    return chunks, time.perf_counter() - start


def ask(question, chunks, chat_model, embed_model, top_k, threshold):
    """Returns (seconds, answer, retrieved, best_score, eval_tokens)."""
    start = time.perf_counter()
    qvec = embed(["search_query: " + question], embed_model)[0]
    ranked = sorted(chunks, key=lambda c: cosine(qvec, c["vec"]), reverse=True)[:top_k]
    best = cosine(qvec, ranked[0]["vec"])
    retrieved = [(c["file"], c["page"]) for c in ranked]
    if best < threshold:
        return time.perf_counter() - start, NO_MATERIAL, retrieved, best, 0

    passages = "\n\n".join(f"[{c['file']} p.{c['page']}]\n{c['text']}" for c in ranked)
    payload = {
        "model": chat_model,
        "stream": True,
        "keep_alive": "30m",
        "options": {"temperature": 0, "num_ctx": 4096},
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Passages:\n{passages}\n\nQuestion: {question}"},
        ],
    }
    answer, eval_tokens = [], 0
    with post("/api/chat", payload, stream=True) as resp:
        for line in resp:
            msg = json.loads(line)
            answer.append(msg.get("message", {}).get("content", ""))
            if msg.get("done"):
                eval_tokens = msg.get("eval_count", 0)
    return time.perf_counter() - start, "".join(answer).strip(), retrieved, best, eval_tokens


def machine_info():
    def sysctl(key):
        return subprocess.run(["sysctl", "-n", key], capture_output=True, text=True).stdout.strip()

    if platform.system() == "Darwin":
        ram = int(sysctl("hw.memsize") or 0) / 2**30
        return f"{sysctl('hw.model')} {sysctl('machdep.cpu.brand_string')} {ram:.0f} GB, macOS {platform.mac_ver()[0]}"
    return f"{platform.platform()} {platform.processor()}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decks", required=True)
    ap.add_argument("--benchmark", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--embed-model", default="nomic-embed-text")
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--threshold", type=float, default=0.55)
    ap.add_argument("--out", default="results")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(exist_ok=True)
    tag = args.model.replace(":", "-").replace("/", "-")

    chunks, index_s = index_decks(args.decks, args.embed_model)
    print(f"Indexed {len(chunks)} pages in {index_s:.1f} s")

    # Warm-up loads the model into memory; timed separately as cold start.
    cold_s, *_ = ask("What is a use case?", chunks, args.model, args.embed_model, args.top_k, -1)
    print(f"Cold start (model load + first answer): {cold_s:.1f} s")

    with open(args.benchmark, newline="") as f:
        questions = list(csv.DictReader(f))

    # Rows are written as they finish so a crash or freeze keeps the completed ones.
    fields = ["id", "kind", "seconds", "best_score", "expected", "retrieved", "check_passed", "eval_tokens", "answer"]
    rows = []
    csv_file = open(out_dir / f"{tag}.csv", "w", newline="")
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()

    def record(row):
        rows.append(row)
        writer.writerow(row)
        csv_file.flush()

    for q in questions:
        secs, answer, retrieved, best, toks = ask(
            q["question"], chunks, args.model, args.embed_model, args.top_k, args.threshold
        )
        hit = (q["source_file"], int(q["page"])) in retrieved
        record({
            "id": q["id"], "kind": "benchmark", "seconds": round(secs, 2), "best_score": round(best, 3),
            "expected": f"{q['source_file']} p.{q['page']}", "retrieved": "; ".join(f"{f} p.{p}" for f, p in retrieved),
            "check_passed": hit, "eval_tokens": toks, "answer": answer,
        })
        print(f"{q['id']} {secs:6.1f} s  score={best:.3f}  page_hit={hit}")

    for i, question in enumerate(OFF_TOPIC, 1):
        secs, answer, retrieved, best, toks = ask(
            question, chunks, args.model, args.embed_model, args.top_k, args.threshold
        )
        refused = answer.lower().startswith(NO_MATERIAL.lower().rstrip("."))
        record({
            "id": f"OT{i}", "kind": "off-topic", "seconds": round(secs, 2), "best_score": round(best, 3),
            "expected": "refusal", "retrieved": "; ".join(f"{f} p.{p}" for f, p in retrieved),
            "check_passed": refused, "eval_tokens": toks, "answer": answer,
        })
        print(f"OT{i} {secs:6.1f} s  score={best:.3f}  refused={refused}")
    csv_file.close()

    bench = sorted(r["seconds"] for r in rows if r["kind"] == "benchmark")
    under_20 = sum(s <= 20 for s in bench)
    summary = {
        "model": args.model, "embed_model": args.embed_model, "machine": machine_info(),
        "pages_indexed": len(chunks), "index_seconds": round(index_s, 1), "cold_start_seconds": round(cold_s, 1),
        "top_k": args.top_k, "threshold": args.threshold,
        "median_seconds": bench[len(bench) // 2], "p18_seconds": bench[17] if len(bench) >= 18 else None,
        "max_seconds": bench[-1], "under_20s": f"{under_20}/{len(bench)}",
        "qr01_pass": len(bench) >= 18 and bench[17] <= 20,
        "expected_page_retrieved": f"{sum(r['check_passed'] for r in rows if r['kind'] == 'benchmark')}/{len(bench)}",
        "off_topic_refused": f"{sum(r['check_passed'] for r in rows if r['kind'] == 'off-topic')}/{len(OFF_TOPIC)}",
    }
    (out_dir / f"{tag}-summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
