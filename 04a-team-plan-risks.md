# 04a - Team Plan and Risks

**Project:** Study-Wise | **Team:** 02, Section 005

**P1 section owner:** Shivansh Batra | **Date:** 18 October 2026

## Planning basis

This document follows sections 4.1 through 4.3 of the team's P1 Proposal and
Requirements baseline. It records the agreed roles, plan to P2 and initial
risks. The dates below are planned commitments for 2026, not claims that the
work has already been completed.

P1 establishes the proposal and requirements. Architecture and design models
are planned for P2; detailed test planning belongs to P3. The scope remains
local course materials, cited answers and multiple-choice practice quizzes.
Short-answer quizzes remain COULD under FR-11. OCR, cloud synchronization,
student-to-student sharing and Canvas integration remain outside the baseline.

## 4.1 Team roles and working agreement

| Team member | Role for P1 to P2 | Responsibility if a vote is tied |
| --- | --- | --- |
| Shivansh Batra | Project lead and document integrator; owns the repository and issue board; sends questions to the instructor. | The owner of the affected section decides, subject to the all-member approval rule for baseline changes. |
| Lavanya Bansal | Elicitation lead; runs interviews, the hardware survey and open-question follow-up. | Final say on wording in sections 2.2, 2.3 and 5. |
| Nandhan Alahari | Feasibility and quality lead; runs spike-01, benchmark timing and quality-threshold evaluation. | Final say on quality thresholds when supported by measurement. |
| Lokesh Reddy Penugonda | Requirements and use-case lead; owns functional and constraint requirements, use cases and traceability. | Final say on functional-requirement wording in section 3.1. |
| Malik Coleman | Quality reviewer; checks every requirement against the Chapter 5 testability rule and checks sources before each submission. | Final say on whether a requirement is testable. |
| Pranab Neupane | Repository and evidence maintainer; organizes `/docs` and `/spike-01` and checks that the contribution record matches commit history. | Final say on repository structure and evidence cited in section 0. |

These ongoing roles are distinct from the P1 file assignments in the proposal's
contribution record. Shivansh Batra's assigned P1 files are
`03b-quality-requirements.md` and `04a-team-plan-risks.md`.

The team discusses disagreements on its channel for up to 24 hours. If a
split remains, it takes a majority vote at the next meeting; a tie goes to
the owner of the affected section. Changes to baselined requirements require
agreement from all members, regardless of section ownership.

Shivansh reviews the issue board every Monday and Thursday. Members work on
short-lived personal branches and submit pull requests for review by at least
one other member before merging into `main`. Open questions, milestones and
requirement changes are tracked with an assignee and a due date. Repository
and AI-use details remain in the separately assigned section 4.4/4.5 document.

## 4.2 Plan to P2

| Date (2026) | What will be finished | Owner |
| --- | --- | --- |
| 25 October | At least eight student interviews and a hardware survey with at least 15 responses recorded in `/docs/elicitation`; Q1 and Q2 answered. | Lavanya Bansal |
| 30 October | spike-01 run on three member laptops; the 20-question benchmark set committed to `/docs/benchmark`. | Nandhan Alahari |
| 31 October | Requirements revised from interview and spike results through change control; revision history updated. | Lokesh Reddy Penugonda |
| 1 November | Instructor's answer to Q3 received after the question is sent on 31 October; Q4 through Q6 resolved or carried forward. | Shivansh Batra |
| 4 November | Draft software architecture using the Chapter 8 material. | Shivansh Batra, with Nandhan Alahari |
| 5 November | Draft class, sequence and state models using Chapters 7 and 9; two setup trials with non-technical students. | Nandhan Alahari (models); Lavanya Bansal (setup trials) |
| 6 November | Integrated P2 document reviewed by every team member. | Malik Coleman coordinates quality review; all members review. |
| 8 November | P2 submitted. | Shivansh Batra |

Interview and hardware findings inform the requirements revision, while
spike-01 supplies evidence about local model feasibility and quality targets.
The architecture and models then feed the integrated P2 review. Open questions
that cannot be resolved by their milestone are carried forward as the proposal
allows; their answers are not assumed to be known.

## 4.3 Risks

| ID | Risk | Likelihood | Impact | Mitigation - action and owner |
| --- | --- | --- | --- | --- |
| R1 | Student laptops cannot run a usable model fast enough (A1). | Medium | High | Nandhan Alahari runs spike-01 on three member laptops, including one with 8 GB RAM, by 30 October and commits the median answer time to `/spike-01`. If the median exceeds 20 seconds, the team switches to a smaller model and Lokesh Reddy Penugonda revises QR-01 through change control by 31 October. |
| R2 | A small local model gives wrong or unsupported answers and quiz keys (A5). | Medium | High | Nandhan Alahari commits the 20-question benchmark set to `/docs/benchmark` by 30 October and scores two candidate models against it. The team keeps the better model. If neither reaches 17 of 20, Lokesh Reddy Penugonda moves quiz generation out of the MUST set through change control by 31 October. |
| R3 | Instructor or UTD policy disallows processing course materials with AI (A4). | Low | High | Shivansh Batra sends Q3 to the instructor on 31 October. If the answer is no, Lavanya Bansal proposes a rescope to student-written notes by 7 November. |
| R4 | Non-technical students cannot complete setup without help (Q5). | Medium | Medium | Lavanya Bansal runs two setup trials with non-technical students by 5 November and records time taken and sticking points. Lokesh Reddy Penugonda turns the findings into setup steps for UC-06. |
| R5 | A member becomes unavailable or misses section deadlines. | Medium | Medium | Shivansh Batra reviews the issue board every Monday and Thursday. A section with no commit for three days is reassigned to a named backup member; Malik Coleman checks that the reassignment appears in the repository history. |

R1's median-time trigger is an early mitigation signal. QR-01 retains its
separate acceptance criterion: at least 18 of the 20 benchmark answers must
complete within 20 seconds. Likewise, R2's model-selection exercise does not
replace QR-04's separate quiz-quality check. Both criteria remain as stated in
[03b - Quality Requirements](03b-quality-requirements.md).

Risk mitigations that change scope or baselined requirements follow the
all-member change-control rule. The risk actions above are planned work;
completion must be supported by the corresponding repository evidence.
