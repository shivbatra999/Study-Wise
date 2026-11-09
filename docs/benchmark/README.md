# Benchmark set

Owner: Lokesh Reddy Penugonda

20 questions with known answers, written from two CS 3354 lecture decks. Used to verify QR-01 (answer time) and QR-03 (answer correctness), and as the input to spike S-01.

## Source materials

| File name used in `benchmark.csv` | Deck |
|---|---|
| `SEKER_L13_L14_Use_Case_Analysis.pdf` | Chapter 7, Lessons 13 and 14: Use Case Analysis (33 slides) |
| `SEKER_L15_L16_High_Level_Design.pdf` | Chapter 8, Lessons 15 and 16: High-Level Design (42 slides) |

`page` is the PDF page number, which is also the citation Study-Wise must produce (FR-08). For the Chapter 8 deck, every question comes from slides 1 to 35, where the page number and the slide number are the same.

## Question mix

| Type | Count | What it tests |
|---|---|---|
| fact | 8 | Exact numbers and names, so a wrong retrieval is obvious |
| definition | 6 | Short terms the student would look up |
| concept | 6 | Answers that combine more than one line of a slide |

## How QR-03 is scored

Two team members independently mark each answer correct only if it matches `expected_answer` **and** its citation points at the listed page. A third resolves disagreements. Pass: at least 17 of 20.

## Off-topic questions (FR-09)

Ask these in a course containing only the two decks. Each must return the "no relevant material" message.

1. Who won the 2022 FIFA World Cup?
2. What is the boiling point of water at sea level?
3. Explain how a TCP three-way handshake works.
4. What is the derivative of sin(x)?
5. Who wrote Pride and Prejudice?
