# ADR-06 Refuse off-topic questions with a similarity gate followed by a relevance check

Owner: Nandhan Alahari (first drafted by Lokesh Reddy Penugonda from the S-01 results; reviewed, revised and committed by this member)

| Field | Content |
|---|---|
| Status | Accepted 8 Nov 2026 |
| Date and owner | Drafted 7 Nov 2026 by Lokesh Reddy Penugonda from S-01 results; revised by Nandhan Alahari; accepted by the team 8 Nov 2026 |
| Context (drivers) | FR-09: the system must say no material was found rather than answer an off-topic question. In S-01, "Explain how a TCP three-way handshake works" scored 0.632 against the decks, higher than the real benchmark question B04 (0.605), and was answered from general knowledge. No single similarity threshold separates the two. |
| Options considered | (a) Similarity threshold only (S-01's 0.55 gate). (b) Gate first, then ask the model a separate yes/no question: do these passages answer the question? Answer only on yes. (c) A reranker model that scores each passage against the question. |
| Decision | We will use (b): AnswerService keeps the cheap gate to refuse clearly unrelated questions without calling the model, and adds the yes/no check (scenario row 4b) before generating. |
| Consequences | Favors FR-09 and academic integrity (SH3). Costs one extra short model call for every question that passes the gate, which uses part of QAS-01's 20 s budget (S-01's 18th-fastest answer left about 5 s). (a) is measured to fail; (c) adds another model to download and run on 8 GB laptops. |
| Evidence | S-01: off-topic questions refused 4 of 5 with the gate and prompt alone; three were refused by the gate in under 0.1 s, one by the model, and the TCP question was answered. The yes/no check is not yet measured. Q1 (CH-19): if the team adopts labelled general-knowledge answers, the same check decides whether to label an answer instead of refusing it, so the decision holds either way. |
| Related | FR-09, QAS-01, CH-17 |
