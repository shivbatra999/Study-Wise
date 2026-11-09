# ADR-02 Reach the local LLM runtime only through RuntimeGateway, using Ollama's local HTTP API

Owner: Nandhan Alahari (first drafted by Lokesh Reddy Penugonda; reviewed, revised and committed by this member)

| Field | Content |
|---|---|
| Status | Accepted 8 Nov 2026 |
| Date and owner | Drafted 6 Nov 2026 by Lokesh Reddy Penugonda; revised by Nandhan Alahari with the S-01 evidence; accepted by the team 8 Nov 2026 |
| Context (drivers) | Two services need generated text and PassageIndex needs vectors. FR-15 and QAS-04 need one place that knows whether the runtime is running. The runtime is third-party software outside our trust boundary (dependency A2). |
| Options considered | (a) Each service calls Ollama directly. (b) All calls go through one RuntimeGateway component that calls Ollama over HTTP on 127.0.0.1:11434. (c) Load the model inside the backend process with an embedded inference library, with no separate runtime. |
| Decision | We will use (b). |
| Consequences | Favors modifiability: switching runtime or model touches one component (design for change), and FR-15's check lives in one place. Costs: one loopback HTTP hop per call (milliseconds next to seconds of generation), and the student must install and start Ollama separately (A2, Q5, R4). (a) spreads the runtime's API across three components; (c) removes a separate install but makes our process manage gigabytes of model memory and threads, and makes the backend crash when the model runs out of memory. |
| Evidence | Ollama documentation [R4] (MIT licence, Windows and macOS builds). S-01 called Ollama over loopback (`/api/embed` and `/api/chat` on 127.0.0.1:11434) for every answer and still met QAS-01 with the 3B model, so the gateway hop is not the bottleneck. S-01's 8B run also showed what option (c) would risk: the model exhausted memory and froze the whole laptop. |
| Related | QAS-01, QAS-04, ADR-04, R1 |
