# Elicitation Summary — P2

Owner: Lavanya Bansal (Elicitation lead), with interviews by Pranab Neupane · Collected 6–8 November 2026

## Sources

| Source | n | Notes |
|---|---|---|
| Hardware and study survey (Microsoft Forms) | 10 | All responses kept; 1 respondent is a team member who is also a student in the target user class. Names, emails and contact details removed. Data: `survey-results.csv`. |
| Student interviews | 5 | P01–P03 (written answers) conducted by Pranab Neupane; P04 (7 Nov) and P05 (8 Nov) conducted by Lavanya Bansal. Notes in `interviews/`; participant codes only. |
| Setup trials (Q5) | 0 | Not run before P2; carried forward. |

Planned in P1 (section 4.2): 15+ survey responses and 8 interviews. Achieved: 10 and 5.

## Survey results (n = 10)

| Question | Result |
|---|---|
| Major | Computer Science 7; biomedical sciences 1; biomedical engineering 1; healthcare studies 1 |
| Laptop | Windows 7; MacBook 3 |
| Operating system | Windows 11: 6; macOS 14 or later: 3; Windows 10: 1 → 9 of 10 meet CON-03 |
| RAM | 8 GB or less: 3; 16 GB: 2; 18–24 GB: 1; 32 GB or more: 3; not sure: 1 → 6 of 10 have 16 GB or more |
| Free storage | More than 50 GB: 6; 10–50 GB: 3; not sure: 1; less than 10 GB: 0 |
| Separate graphics card | No: 4; not sure: 3; yes: 3 |
| Laptop age | Under 1 year: 2; 1–2 years: 5; 3–4 years: 2; 5+ years: 1 |
| Where they study | On battery: 4; both: 4; plugged in: 2 → 8 of 10 study on battery at least some of the time |
| Terminal / README experience | Never: 4; yes, comfortably: 5; yes, with difficulty: 1 |
| Assistive features | 2 of 10 use at least one (zoom or large text: 2; speech-to-text: 1; screen reader: 1) |

The Mac chip question (Apple silicon vs Intel) was not included in the live form, so chip type is unknown.

## Interview results (n = 5)

| Topic | Result |
|---|---|
| Already use AI tools to study | 5 of 5 |
| Have uploaded course files to a cloud AI tool | 5 of 5; none raised privacy as a concern |
| Have received wrong answers from AI | 5 of 5; two said repeated inaccuracy would make them stop using a tool |
| Q1 — slides don't cover the question | 5 of 5 chose a general-knowledge answer clearly labelled as not from their materials. 1 said that under exam pressure they might prefer "not covered" |
| Citation to slide or page | Very important and would open it: 3; not really important: 2 |
| Q4 — too little material for 20 questions | 8 questions plus a note: 3; 20 questions with repeats: 2 (reason: repetition helps practice) |
| Q6 — short-answer questions | Model answer with source: 3; tool should mark the answer: 2 (both said they would only partly trust the mark) |
| Keep finished quizzes and scores for review (asked in P01–P03 only) | Yes: 3 of 3 |
| Importing a file already in the course (asked in P01–P03 only) | Replace it: 3 of 3 (reason: updated slides often keep the same name) |

## What this means for the requirements

1. **A1 holds only weakly.** 6 of 10 have 16 GB or more, but 3 of 10 have 8 GB or less. Spike S-01 should include an 8 GB laptop (risk R1).
2. **CON-03 confirmed.** 9 of 10 run Windows 11 or macOS 14+, and only 3 of 10 confirmed having a separate graphics card.
3. **Disk space is not a blocker.** No respondent reported less than 10 GB free.
4. **Setup support is needed.** 4 of 10 have never used a terminal, which supports FR-15, UC-06 and Q5.
5. **Q1 contradicts the P1 assumption.** All 5 interviewees wanted labelled general-knowledge answers, not materials-only answers. This is a team decision under change control (FR-07, FR-09, QR-03, SH3).
6. **The privacy need in SH1 is not confirmed by students.** All interviewees already upload files to cloud AI. The privacy driver for CON-01 rests on SH2 (instructors) and the product vision, not on student demand.
7. **New candidate requirements:** keep quiz history (3 of 3), and replace a duplicate import (3 of 3).
8. **Accessibility is a real need.** 2 of 10 use assistive features (new open question Q10).

Limits: small samples, mostly Computer Science students, and P01–P03 used a slightly different question set. Treat results as indicative, not conclusive.
