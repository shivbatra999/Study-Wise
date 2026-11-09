# 4 Use-Case Analysis

Owner: Lokesh Reddy Penugonda

## 4.1 Use cases selected for analysis

| Use case | Name | Why it was selected | Non-trivial steps |
|---|---|---|---|
| UC-02 | Ask a Question About Course Materials | Carries most of the product's value; touches the most quality requirements (QR-01, QR-03, CON-01); depends on an external system whose failure the student can see. Specified in full at P1. | (4) |
| UC-03 | Practice with a Generated Quiz | Second core goal; QR-04 (quiz quality) is the requirement we are least sure a small local model can meet (R2). Specified in full at P1. | (6), (10) |
| UC-01 | Import Course Materials | Every other use case depends on it; realizes five MUST/SHOULD requirements (FR-01 to FR-05) and QR-02; involves an external system (the student's file system) and a failure the student can see (FR-03). | (4), (6) |

UC-06 Set Up Study-Wise for First Use was considered but not analyzed: how the model is obtained during setup is still open (Q5), and expanding it now would mean inventing the answer. See 9.2.

## 4.2 Expanded use cases

### UC-02 Ask a Question About Course Materials

| Field | Content |
|---|---|
| Primary actor | Student |
| Supporting actors and external systems | Local LLM runtime (external system) |
| TUCBW | The student chooses to ask a question in one of their courses. |
| TUCEW | The student sees an answer with the source of each passage it used, or a statement that no material in the course covers the question. |
| Preconditions | Study-Wise is installed on the student's device. |
| Postconditions | The student has seen either an answer citing at least one passage from the selected course, or an explicit statement that none was found. No question, passage or answer has left the device. The course's materials are unchanged. |
| Traces to requirements | FR-07, FR-08, FR-09, FR-15, QR-01, QR-03, CON-01 |

| Actor input / action | System response |
|---|---|
| | (0) The system shows the student's courses, each with its name and number of materials. |
| (1) The student selects a course. | (2) The system shows the course name and its materials, each with its name and number of pages or slides, and invites a question about them. |
| (3) The student types a question and submits it. | (4) The system shows an answer built only from passages in the selected course, and, for each passage used, the material name and the page or slide number. |
| (5) The student reads the answer and the sources it cites. This is the acknowledgment. | |

| Alternate flow | At step | Condition | What happens | Ends or rejoins at |
|---|---|---|---|---|
| A1 | (0) | The student has no courses. | The system says there are no courses yet and offers to create one (UC-05). | Ends |
| A2 | (2) | The selected course has no materials. | The system says the course has no materials and offers to import some (UC-01). | Ends |
| A3 | (3) | The question is empty. | The system asks the student to type a question. | Rejoins (3) |
| A4 | (4) | No passage in the course relates to the question. | The system states that no material in this course covers the question and gives no answer (FR-09). | Ends |
| A5 | (4) | The local LLM runtime is not running or has no model. | The system says the runtime is unavailable and lists the steps to fix it (FR-15). The student fixes it and resubmits, or leaves. | Rejoins (3), or ends |
| A6 | (4) | No answer after 60 seconds. | The system shows that it is still working and offers to cancel. On cancel, no answer is shown. | Rejoins (4), or ends |
| A7 | (5) | The student selects one of the cited sources. | The system shows that page or slide of the material, with the passage used marked. | Ends |

### UC-03 Practice with a Generated Quiz

| Field | Content |
|---|---|
| Primary actor | Student |
| Supporting actors and external systems | Local LLM runtime (external system) |
| TUCBW | The student chooses to start a practice quiz in one of their courses. |
| TUCEW | The student sees their score and, for every question, the correct answer with its source. |
| Preconditions | Study-Wise is installed on the student's device. |
| Postconditions | The student has seen a score (correct out of total) and, for every question, the correct option with its material name and page or slide number. No material, question or answer has left the device. The course's materials are unchanged. |
| Traces to requirements | FR-10, FR-11, FR-12, FR-13, FR-14, FR-15, QR-04, CON-01 |

| Actor input / action | System response |
|---|---|
| | (0) The system shows the student's courses, each with its name and number of materials. |
| (1) The student selects a course to practise in. | (2) The system shows the course's materials, all chosen by default. |
| (3) The student chooses which materials the quiz should draw from. | (4) The system shows the chosen materials and asks for a question format and a number of questions from 1 to 20. |
| (5) The student chooses multiple choice and a number of questions. | (6) The system shows that many questions, each with four options, drawn only from the chosen materials. |
| (7) For each question, the student chooses one option. | (8) The system marks the chosen option for that question. |
| (9) The student submits the quiz. | (10) The system shows the number of correct answers out of the total and, for each question, the correct option with its material name and page or slide number. |
| (11) The student reads their score and the correct answers. This is the acknowledgment. | |

| Alternate flow | At step | Condition | What happens | Ends or rejoins at |
|---|---|---|---|---|
| A1 | (0) | The student has no courses. | The system says there are no courses yet and offers to create one (UC-05). | Ends |
| A2 | (2) | The selected course has no materials. | The system says the course has no materials and offers to import some (UC-01). | Ends |
| A3 | (3) | The student chooses no materials. | The system asks for at least one material. | Rejoins (3) |
| A4 | (5) | The number is outside 1 to 20. | The system shows the allowed range. | Rejoins (5) |
| A5 | (5) | The student chooses short answer (FR-11). | The system shows the questions; the student writes answers and submits; the system shows a model answer with its source for each question, with no score (Q6). | Ends |
| A6 | (6) | The local LLM runtime is not running or has no model. | As UC-02 A5 (FR-15). | Rejoins (5), or ends |
| A7 | (6) | The chosen materials are too short for the requested number. | The system shows as many questions as it could produce and states the actual number (assumption pending Q4). | Rejoins (7) |
| A8 | (9) | Some questions are unanswered. | The system lists the unanswered questions. The student answers them, or submits anyway and they count as incorrect. | Rejoins (7), or (10) |
| A9 | before (9) | The student abandons the quiz. | The system confirms the quiz was discarded; no score is shown. | Ends |

### UC-01 Import Course Materials

| Field | Content |
|---|---|
| Primary actor | Student |
| Supporting actors and external systems | Student's local file system (external system) |
| TUCBW | The student chooses to add materials to a course. |
| TUCEW | The student sees each imported material listed in the course with its number of pages or slides and marked ready for questions. |
| Preconditions | Study-Wise is installed on the student's device. |
| Postconditions | Each imported material is listed in the course with its page or slide count and can be used by UC-02 and UC-03, including after Study-Wise is closed and reopened. The student's original files are unchanged. Nothing has left the device. |
| Traces to requirements | FR-01, FR-02, FR-03, FR-04, FR-05, QR-02, QR-05, CON-01 |

| Actor input / action | System response |
|---|---|
| | (0) The system shows the student's courses, each with its name and number of materials. |
| (1) The student selects a course. | (2) The system shows the course's materials, each with its name and number of pages or slides. |
| (3) The student chooses to add materials. | (4) The system shows the PDF and PowerPoint files on the student's device. |
| (5) The student selects one or more files. | (6) The system shows each selected file in the course's materials with its number of pages or slides, and marks it ready for questions. |
| (7) The student sees the new materials listed as ready. This is the acknowledgment. | |

| Alternate flow | At step | Condition | What happens | Ends or rejoins at |
|---|---|---|---|---|
| A1 | (0) or (1) | The student has no course for these materials. | The system asks for a course name; the student enters one; the system shows the new, empty course (FR-04). | Rejoins (2) |
| A2 | (5) | A selected file contains no text that can be extracted. | The system names the file, says no text was found, and does not list it (FR-03). Other selected files continue. | Rejoins (6) |
| A3 | (5) | A selected file cannot be opened (damaged or password-protected). | The system names the file and says it could not be opened; the file is not listed. Other files continue. (No requirement yet; see 4.3.) | Rejoins (6) |
| A4 | (5) | A selected file is already in the course. | Behavior undecided (Q8). Assumed meanwhile: the system says the file is already there and does not add it again. | Rejoins (6) |
| A5 | (5) | The student cancels without selecting a file. | The system shows the course's materials unchanged. | Ends |

## 4.3 Self-review log

Each expanded use case was run against the ten questions of the Lesson 13 review checklist by a member who did not write it. Checks with no defect are listed once at the end.

| Use case | Checklist question | Defect found | How it was fixed |
|---|---|---|---|
| UC-02, UC-03 | 6. Are the pre-conditions things you may assume, not failures you must handle? | P1 pre-condition "the selected course contains at least one imported material" can be false in normal use, and P1 already handled it as flow 1a, so the two contradicted each other. | Removed from pre-conditions; kept as alternate flow A2. |
| UC-02, UC-03 | 6. (as above) | P1 pre-condition "Study-Wise is set up (UC-06)" can become false at any time if the runtime stops. | Removed; handled by UC-02 A5 and UC-03 A6 (FR-15). |
| All three | 2. Is there a step (0)? | P1 use cases had no step (0). | Added step (0) to each: the courses with their material counts. |
| UC-02 | 3. Does every row hold exactly one turn? | P1 steps 3 to 5 (find passages, send to runtime, runtime returns) were three system steps with no actor turn between them. | Merged into one system response, (4); the internal steps are split out in the 5.2 scenario table. |
| UC-03 | 3. (as above) | P1 step 6, "answers every question and submits the quiz," merged two actor actions. | Split into (7)/(8) and (9)/(10). |
| UC-02 | 5. Does it end with an acknowledgment the actor can perceive? | P1 ended with "reads the answer and, optionally, opens a cited source," which mixed the acknowledgment with an optional action. | Main flow ends at (5), the student reading the cited answer; opening a source became A7. |
| UC-01 | 8. Is every alternate named by the step it branches from? Does each trace to a requirement? | A3 (file cannot be opened) has no requirement behind it. | Proposed FR-16 through change control (0.2). |
| UC-01 | 8. (as above) | A4 (file already in course): the right behavior is a choice for users, not for us. | Recorded as open question Q8 instead of inventing an answer. |
| UC-03 | 7. Is there a post-condition a tester could turn into a test? | Whether a finished quiz and its score are kept is not stated anywhere. | Post-condition limited to what the student has seen; retention recorded as open question Q7. |
| All three | 1, 9, 10 | None found. The actor is the role Student; nothing happens that the student neither sees nor waits for (importing in UC-01 is waited for, per QR-02); external systems are named by role, not product, and no screen widgets or stores are named. | — |
| All three | 4. Does every item the actor supplies exist as a domain model attribute? | Checked against the domain model in 5.3 (K1). | See 5.3. |
