# 9 Traceability

## 9.1 Extended traceability matrix

Replaces the P1 matrix (old section 3.5). Use cases in bold were analyzed in sections 4 and 5. Analysis objects in italics are interaction objects (5.2).

| Requirement | Use case | Analysis classes | Component(s) | QAS / ADR | Evidence |
|---|---|---|---|---|---|
| FR-01 | **UC-01** | Material, PageOrSlide, Passage | MaterialIngestor, CourseLibrary, PassageIndex | QAS-02, ADR-03 | — |
| FR-02 | **UC-01** | Material, PageOrSlide, Passage | MaterialIngestor, CourseLibrary, PassageIndex | QAS-02, ADR-03 | — |
| FR-03 | **UC-01** A2 | Material | MaterialIngestor | — | — |
| FR-04 | **UC-01** A1; UC-05 | Course | CourseLibrary | — | — |
| FR-05 | **UC-01** postcondition; UC-05 | Course, Material, Passage | LocalStore, CourseLibrary | ADR-03 | — |
| FR-06 | UC-05 | Material, Passage | CourseLibrary, PassageIndex | ADR-03 | — |
| FR-07 | **UC-02** | Question, Passage, Answer, *QuestionHandler*, *PassageFinder* | AnswerService, PassageIndex | QAS-01, ADR-02, ADR-04 | Benchmark (PR #30); S-01 |
| FR-08 | **UC-02** | Answer, Citation | AnswerService, PassageIndex | ADR-05 | Benchmark (PR #30) |
| FR-09 | **UC-02** A4 (row 4b) | *QuestionHandler* | AnswerService | ADR-06 | S-01: off-topic refused 4 of 5 |
| FR-10 | **UC-03** | Quiz, QuizQuestion, Option, *QuizMaster*, *PassageFinder* | QuizService, PassageIndex | ADR-05 | — |
| FR-11 | **UC-03** A5 | QuizQuestion (model answer, student answer) | QuizService | — | — |
| FR-12 | **UC-03** (3), row 6b | Quiz *draws from* Material, *PassageFinder* | QuizService, PassageIndex | — | — |
| FR-13 | **UC-03** (10), rows 10a–10b | QuizResult, Option | QuizService | — | — |
| FR-14 | **UC-03** (10), row 10c | Option, Citation | QuizService | ADR-05 | — |
| FR-15 | **UC-02** A5; **UC-03** A6; UC-06 | Local LLM runtime (external) | RuntimeGateway, StudyUI | QAS-04, ADR-02 | — |
| FR-16 | **UC-01** A3 | Material | MaterialIngestor | — | — |
| FR-17 | **UC-03** postcondition | Quiz, QuizResult | QuizService, LocalStore | — | Interviews, Q7 |
| FR-18 | **UC-01** A4 | Material | MaterialIngestor, CourseLibrary | — | Interviews, Q8 |
| QR-01 | **UC-02** | — | AnswerService, PassageIndex, RuntimeGateway | QAS-01, ADR-02, ADR-04 | S-01: 20 of 20 within 20 s (3B, 8 GB) |
| QR-02 | **UC-01** | — | MaterialIngestor, PassageIndex, LocalStore | QAS-02, ADR-03 | Partial: S-01 indexed 71 pages in 5.5 s (no import flow or store) |
| QR-03 | **UC-02** | Answer, Citation | AnswerService | ADR-04, ADR-05, ADR-06 | Benchmark (PR #30); S-01 answers saved; provisional read about 13 of 20 |
| QR-04 | **UC-03** | QuizQuestion, Option | QuizService | ADR-04, ADR-05 | Not yet measured |
| QR-05 | **UC-01**, **UC-02** | — | StudyUI | — | Not yet measured (usability sessions, P3) |
| CON-01 | All | — | All; LocalApi binds to loopback | QAS-03, ADR-01 | Deployment view (6.4) |
| CON-02 | All | — | All | ADR-02, ADR-03 | Licences named in 6.1 |
| CON-03 | All | — | RuntimeGateway (model setting) | ADR-04 | S-01: 8B does not run on 8 GB; 3B does |
| CON-04 | None (build constraint) | — | All | ADR-02, ADR-03 | Licences named in 6.1; licence list file not yet in the repository |

## 9.2 Gap analysis

| Gap | Items | What we did about it |
|---|---|---|
| Requirements with no component | None | Every FR, QR and CON reaches at least one component. |
| Components with no requirement, QAS or ADR | None. LocalApi answers only to ADR-01 and QAS-03, not to a functional requirement. | Accepted: it exists because of the client–server decision, and ADR-01 records why. |
| Use cases not analyzed (and why that is acceptable) | UC-05 Manage Course Library; UC-06 Set Up Study-Wise | UC-05 is two simple MUST/SHOULD operations (FR-04, FR-06) with no external system; its requirements still reach CourseLibrary. UC-06 depends on Q5 (does Study-Wise download the model, or does the student?); expanding it now would invent the answer. Both are expanded at P3. |
| Requirements with no evidence yet, or failing evidence | QR-02 (partial), QR-03 (provisional 13 of 20), QR-04, QR-05, CON-04 | QR-03: two-reviewer scoring of the S-01 answers, then retrieval fixes (smaller chunks, more pages, a reranker). QR-02 and QR-04 are measured once MaterialIngestor and QuizService exist (10.2). QR-05 needs the usability sessions at P3. CON-04: a licence list is added to the repository at P3, and it must settle PyMuPDF (AGPL-3.0, used in S-01) before it enters the product. |
| Flow with no requirement (carried from P1) | UC-03 A7: too little material for the requested number of questions | Still waiting on Q4; ADR-05 uses the same behavior (generate fewer and say so) as the interim assumption. |
| Flows that became requirements during analysis | UC-01 A3 (file cannot be opened); UC-01 A4 and the UC-03 postcondition, once Q8 and Q7 were answered | Became FR-16 (CH-06), FR-18 (CH-21) and FR-17 (CH-20). |

**Findings carried from the P1 matrix**, still valid: FR-15 exists because UC-06 had no requirement behind it; FR-05 is traced through postconditions because no actor starts it; "Generate Quiz" and "Take Quiz" were merged into UC-03.
