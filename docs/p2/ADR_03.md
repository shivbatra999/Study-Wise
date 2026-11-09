### ADR-03 Keep the library and passage vectors in one local SQLite file, with similarity search inside the backend

| Field | Content |
| :--- | :--- |
| Status | Accepted 8 Nov 2026 |
| Date and owner | Drafted 6 Nov 2026 by Lokesh Reddy Penugonda; accepted by the team 8 Nov 2026 |
| Context (drivers) | FR-05 needs courses and materials to survive restarts. FR-07 and FR-09 need the most relevant passages within one course. QAS-01 limits retrieval time. CON-02 and CON-04 require free, openly licensed parts. A course is small: two lecture decks give 71 pages (S-01 dry run). |
| Options considered | (a) A dedicated vector database library (for example Chroma or FAISS). (b) One SQLite file holding courses, materials, passages and their vectors, with similarity computed in the backend over the selected course’s passages only. (c) Plain JSON files. |
| Decision | We will use (b). |
| Consequences | Favors simplicity (KISS): one dependency already in Python, one file to back up or delete, transactions so a crash mid-import does not corrupt the library. Costs: search time grows linearly with the passages in a course; past a few thousand passages per course it may become noticeable. Fitness check for P3: retrieval for a 20-deck course stays under 1 s, otherwise revisit (a). (a) is faster at scale but adds an install-heavy dependency for courses that are small; (c) has no transactions, so an interrupted import can break FR-05. |
| Evidence | S-01: 71 pages embedded and indexed in 5.5 s; one vector per page, cosine similarity computed in process, top 3 pages retrieved. Expected page retrieved for 17 of 20 questions; smaller chunks are a P3 option. |
| Related | QAS-01, QAS-02, R8 |