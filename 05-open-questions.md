# 11 Open Questions (updated; was P1 section 5)

Every P1 question is carried forward with its answer, or with a note that it is still open. Q7–Q10 are new in P2.

| ID | Question | Raised by | Owner and due date | Status or answer | Assumption meanwhile |
|---|---|---|---|---|---|
| Q1 | Should answers use only the student's materials, or also the model's general knowledge? | P1 | Students via interviews, Lavanya Bansal, 7 Nov | **Answered 8 Nov:** 5 of 5 interviewees preferred a general-knowledge answer clearly labelled as not from their materials. Requirement change pending a team decision (FR-07, FR-09, QR-03); materials-only kept until then. | Materials only (FR-07, FR-09) |
| Q2 | What RAM, operating system and GPU do target students have? | P1 | Students via survey, Lavanya Bansal, 7 Nov | **Answered 8 Nov:** survey n = 10 (see 2.3). 6 of 10 have 16 GB or more, 3 of 10 have 8 GB or less; 9 of 10 run Windows 11 or macOS 14+. A1 holds narrowly. | 16 GB, Windows 11 or macOS 14+, no GPU (A1) |
| Q3 | May students process instructor slides with a local AI tool for personal study? | P1 | Dr. Seker; sent by Shivansh Batra 6 Nov | **Open:** awaiting reply | Allowed (A4) |
| Q4 | When chosen materials are too short for the requested number of quiz questions: fewer, repeat, or refuse? | P1 | Students via interviews, Lavanya Bansal, 7 Nov | **Answered 8 Nov:** 3 of 5 chose "fewer questions and a note"; 2 of 5 chose 20 with repeated topics. The current assumption is confirmed, and an FR can now be written. | Generate fewer and say so (UC-03 A7, ADR-05) |
| Q5 | Should Study-Wise download the model at setup, or does the student install the runtime and model? | P1 | Non-technical students via setup trials, Lavanya Bansal, 30 Nov (moved from 5 Nov, CH-11) | **Open** | Student installs the runtime (ADR-02) |
| Q6 | Should short answers be marked, and against what standard? | P1 | Students (interviews) and Dr. Seker | **Students answered:** 3 of 5 want a model answer with its source; 2 of 5 want marking but would only partly trust it. Instructor's view still open (asked with Q3). | Not marked; model answer shown (UC-03 A5) |
| Q7 | Should a finished quiz and its score be kept for later review? | Analysis of UC-03 (4.3) | Students via interviews, Lavanya Bansal, 7 Nov | **Answered 8 Nov:** students want finished quizzes and scores kept. | Not kept (6.5) |
| Q8 | When a file already in the course is imported again: skip, replace, or add a second copy? | Analysis of UC-01 (4.3) | Students via interviews, Lavanya Bansal, 7 Nov | **Answered 8 Nov:** students said replace the old file, because updated slides often keep the same name. | Skip and tell the student (UC-01 A4) |
| Q9 | If the 8B model is too slow, would students accept faster but weaker answers from a smaller model? | ADR-04 | Students via interviews, Lavanya Bansal, 13 Nov | **Open** | Speed first: 3B default if S-01 fails |
| Q10 | Which accessibility features must Study-Wise support? | Survey (2.3) | Lavanya Bansal, before P3 | **Open:** 2 of 10 respondents use assistive features (zoom or large text, speech-to-text, a screen reader). | Keyboard navigation only |
