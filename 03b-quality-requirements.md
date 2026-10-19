# 03b - Quality Requirements

**Project:** Study-Wise | **Team:** 02, Section 005

**P1 section owner:** Shivansh Batra | **Date:** 18 October 2026

## Purpose and baseline

This document presents section 3.2 of the team's P1 Proposal and Requirements
baseline. It preserves the proposal's five quality requirement identifiers,
thresholds, priorities and sources so that the team's use cases and traceability
matrix refer to the same requirements.

These are requirements for the planned system, not claims of measured results.
P1 states the conditions and methods needed to decide whether each requirement
passes; detailed test planning belongs to P3. Performance evidence from
spike-01 may support later revisions through the proposal's change-control
process.

## Measurement context

- **Reference laptop:** The proposal defines a team-owned laptop with 16 GB
  RAM, no discrete GPU, and Windows 11 or macOS 14 or later. It also records
  Lokesh's laptop as having 18 GB RAM. The actual reference configuration will
  be recorded with the performance results.
- **Benchmark set:** Twenty questions with known answers, written by the team
  from two lecture decks, to be stored in `/docs/benchmark`. This set supports
  QR-01 and QR-03.
- **Source identifiers:** SH1 refers to student users; SH3 refers to the UTD
  Office of Community Standards and Conduct; A1 is the assumption that most
  target students have at least 16 GB RAM. Section 2.3 describes the technical
  and non-technical student user classes.

## 3.2 Quality requirements

| ID | Requirement - threshold and condition | Priority | Source | How it will be verified |
| --- | --- | --- | --- | --- |
| QR-01 | At least 90% of answers shall be fully displayed within 20 seconds of submission on the reference laptop with a model of up to 8B parameters. | SHOULD | SH1, A1 | Run the 20-question benchmark set and record submission-to-completion time for every answer; pass if the 18th-fastest time is at most 20 seconds. Recalibrate the threshold from spike-01 only through change control. |
| QR-02 | A 50-page text PDF shall become available for questions within 90 seconds of import on the reference laptop. | SHOULD | SH1 | Import the same 50-page PDF five times, starting the application afresh for each run; pass if the median time from import to ready is at most 90 seconds. |
| QR-03 | At least 85% of answers to the benchmark set shall be correct and supported by their cited passage. | MUST | SH1, SH3 | Two team members independently score each answer against the answer key and cited page; a third resolves disagreements. Pass if at least 17 of 20 answers are both correct and supported. |
| QR-04 | At least 80% of generated multiple-choice questions shall have exactly one defensible correct option. | MUST | SH1 | Generate 30 questions from materials belonging to three different courses. Two reviewers independently judge each question; pass if at least 24 of 30 are agreed valid. |
| QR-05 | At least four of five first-time student testers shall import a file and receive a cited answer within 10 minutes without help. | SHOULD | SH1, section 2.3 | Conduct a moderated session with five students who are not on the team, starting after installation. Measure time to the first cited answer without giving hints; pass if at least four complete the task within 10 minutes. |

## Relationship to the rest of the proposal

| Quality requirement | Related use case(s) |
| --- | --- |
| QR-01 | UC-02 - Ask a Question About Course Materials |
| QR-02 | UC-01 - Import Course Materials |
| QR-03 | UC-02 - Ask a Question About Course Materials |
| QR-04 | UC-03 - Practice with a Generated Quiz |
| QR-05 | UC-01 and UC-02 |

Privacy remains CON-01; cost, supported hardware and licensing remain
CON-02 through CON-04. Import behavior, persistence, removal, citations and
runtime-error messages remain functional requirements. Short-answer quizzes
remain a COULD requirement under FR-11. Accessibility remains an open topic
for P2, as stated in the proposal, rather than an additional P1 threshold.

The owners, dates and risks for gathering evidence are recorded in
[04a - Team Plan and Risks](04a-team-plan-risks.md). Any change to a baselined
requirement requires agreement from all team members under the proposal's
change-control process.
