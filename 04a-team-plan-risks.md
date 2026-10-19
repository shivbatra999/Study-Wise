# 04a - Team Plan and Risks

## Planning basis

Study-Wise will provide local document ingestion, retrieval-grounded questions
and answers, and practice quizzes using Ollama. The current repository contains
a project overview, so this plan describes work to be completed rather than
reporting completed implementation.

Team membership, availability and course deadlines have not been recorded in
the repository. The responsibilities and six working weeks below are a proposed
baseline. At kickoff, the team will assign named owners and reviewers, map the
milestones to actual course dates, and adjust scope to available capacity.
One person may hold multiple roles, but another teammate should review their
work whenever possible.

## Responsibilities

| Role | Primary responsibility | Expected output |
| --- | --- | --- |
| Coordinator and integration owner | Maintain the task board, milestone dates, scope and integration readiness; surface blockers. | Current plan, integration checkpoints and release checklist. |
| Ingestion and storage owner | Parse PDFs and `.pptx` files, manage local course storage, build the index, and implement deletion and recovery. | Repeatable imports, local persistence, retrieval-ready chunks and deletion checks. |
| Retrieval and model owner | Connect to local Ollama, retrieve relevant passages, produce cited answers, and generate and validate quizzes. | Working local generation, grounding evaluation and model performance results. |
| Interface and usability owner | Build the import, question and quiz flows with clear progress, error feedback and keyboard access. | Usable application screens and results from student usability trials. |
| Quality and documentation owner | Coordinate test fixtures, acceptance evidence, setup instructions and risk reviews. | Traceable quality report, reproducible setup guide and current risk register. |

Each task must identify one accountable owner, a reviewer, dependencies and
completion criteria. Assign a backup for each core subsystem so that a single
absence does not prevent integration or the final demonstration.

## Milestones and dependencies

| Milestone | Proposed window | Work and dependencies | Exit criteria |
| --- | --- | --- | --- |
| M1: Agree on scope and prove local execution | Week 1 | Assign roles and dates; select the reference laptop and model; agree on interfaces, test corpus and quality targets; make one local Ollama request. | Owners and schedule recorded; sample request works offline after installation; model startup, memory use and generation latency recorded. |
| M2: Import and retrieve course material | Week 2 | Build parsers, local storage and indexing after M1 decisions. Implement invalid-file handling and document removal. | A PDF and `.pptx` can be imported and searched with page or slide metadata; invalid fixtures fail cleanly; removed content is no longer retrieved. |
| M3: Deliver the complete question workflow | Week 3 | Connect retrieval and Ollama to the interface after M2; add source references, insufficient-evidence responses and error recovery. | A student can import material and receive a cited answer through the interface; offline operation and unavailable-model handling are demonstrated. |
| M4: Deliver practice quizzes | Week 4 | Generate multiple-choice and short-answer questions from retrieved material; validate structure and present answers and explanations. Depends on the M3 integration. | Five-question quizzes work through the interface; answers, explanations and source references are present; malformed model output produces a recoverable error. |
| M5: Validate quality and resolve defects | Week 5 | Run the full quality suite, reviewed answer and quiz evaluations, keyboard checks, and five student usability trials. | Every quality requirement has evidence or a tracked defect with an owner; release-blocking defects are resolved before M6 acceptance. |
| M6: Stabilize and demonstrate | Week 6 | Complete remaining fixes, verify clean setup, finalize documentation and rehearse the demonstration. Reserve this week for stabilization rather than new features. | A fresh setup and offline demo succeed; all quality requirements pass or have documented, approved revisions; final revision and known limitations are recorded. |

The critical dependency sequence is local model feasibility, ingestion and
retrieval, integrated answers, quizzes, then acceptance. Interface mockups and
test preparation can proceed alongside backend work once the data contracts
are agreed. Optional polish must not delay this sequence.

## Collaboration and change workflow

- Hold two short team check-ins per week and one integration review at the end
  of each milestone. Record completed work, the next task, blockers and changes
  to risks. Raise a blocker within one working day of discovering it.
- Track tasks as To Do, In Progress, Review, Blocked or Done. Keep tasks small
  enough for a reviewer to understand and verify in one sitting.
- Work on personal or feature branches based on the latest `main`. Submit pull
  requests that explain the change and include relevant verification evidence.
  Obtain a teammate review and pass the relevant checks before merging.
- Agree on ingestion, retrieval and generation input/output formats before
  connecting components. Include source document and page or slide identifiers
  in the retrieval contract so citations survive integration.
- Keep synthetic or permission-cleared fixtures in the project. Do not commit
  private lecture material, generated indexes, model weights or local secrets.
- Record scope changes with the reason, affected milestone, affected quality
  requirements and team decision. Review any revised acceptance target before
  using it to judge a release.

## Definition of done

A task is done when its completion criteria are demonstrated, relevant checks
pass, another teammate has reviewed the change, and needed documentation is
updated. A milestone is done when its exit criteria are met on the integrated
application. Final acceptance uses the IDs and evidence requirements in
[03b - Quality Requirements](03b-quality-requirements.md).

## Risk register

Likelihood and impact use High, Medium and Low ratings. High impact means a
core workflow, privacy requirement or milestone could fail; Medium impact
means significant rework or reduced usability; Low impact means a localized
issue. These are initial planning estimates, not measured probabilities.
All risks start open and are reassessed at each milestone review.

| ID | Risk | Likelihood | Impact | Warning sign or trigger | Prevention and mitigation | Contingency if triggered | Accountable role |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | The local model is too slow or exceeds available memory. | High | High | The M1 prototype runs out of memory or exceeds QR-06 latency targets. | Benchmark early on the reference laptop; limit prompt size and output length; compare suitable smaller local models. | Select a smaller model and repeat grounding and timing checks; revise scope or targets through a recorded team decision if still infeasible. | Retrieval and model owner |
| R-02 | Answers or quiz questions contain unsupported claims. | High | High | Reviewed outputs fail QR-07 or QR-08, or citations do not resolve to supporting text. | Preserve source metadata; retrieve relevant passages; request source-grounded output and explicitly handle insufficient evidence; evaluate a fixed question set. | Block acceptance, investigate retrieval and prompt failures, and rerun the full reviewed set after fixes. | Retrieval and model owner |
| R-03 | Course documents cannot be parsed reliably. | High | Medium | Files produce empty text, missing page metadata or repeated extraction errors. | Test PDF and `.pptx` fixtures early, validate file types and sizes, and reject unsupported image-only documents with clear feedback. | Explain the unsupported format and request a text-based export; keep OCR and legacy format support outside the initial scope. | Ingestion and storage owner |
| R-04 | Private study content leaves the device or appears in logs. | Medium | High | A workflow contacts a nonlocal inference endpoint or logs contain document text. | Default all services to loopback, avoid external inference dependencies, keep content out of routine logs, and verify offline behavior and network traffic. | Stop acceptance, disable the offending path, remove exposed application log content where possible, and rerun QR-01 and QR-02 before release. | Ingestion and storage owner |
| R-05 | Components work separately but fail when integrated. | Medium | High | API formats diverge or the end-to-end question flow is not working by M3. | Agree on contracts in M1, keep changes small, and integrate a complete import-to-answer path early. | Pause optional work and pair the affected owners until the core flow works; update dependent milestone dates. | Coordinator and integration owner |
| R-06 | Team availability or uneven workload causes missed milestones. | Medium | High | A critical task has no owner, a blocker lasts more than two working days, or an owner reports insufficient capacity. | Review capacity at check-ins, identify backups, share setup knowledge and split oversized tasks. | Reassign work to a backup, reduce optional scope, and record a revised schedule with the team. | Coordinator and integration owner |
| R-07 | Scope grows beyond the course timeline. | High | High | New features are added without estimates or core milestone tasks remain incomplete. | Prioritize ingestion, grounded answers and quizzes; place OCR, cloud sync, collaboration and advanced analytics outside the baseline. | Defer optional work and protect the stabilization week; seek a recorded team decision for any change to core scope. | Coordinator and integration owner |
| R-08 | Interrupted imports or incomplete deletion leave inconsistent local data. | Medium | High | Searches return deleted material, failed imports appear complete, or saved courses disappear after restart. | Make imports atomic or clean up failed work; test restart, interruption and deletion scenarios using known fixtures. | Stop acceptance, repair the affected storage path, and rebuild derived indexes from intact source material; never silently discard user files. | Ingestion and storage owner |
| R-09 | Installation or model download fails on demonstration hardware. | Medium | High | A clean setup requires undocumented commands, incompatible versions or an unexpected external download. | Document tested versions and model setup; perform a fresh installation and prepare the model before the demonstration. | Use a previously verified team machine with local fixtures and model installed, then track and fix the original setup failure. | Quality and documentation owner |
| R-10 | The interface confuses students or blocks keyboard users. | Medium | Medium | Testers cannot complete core tasks, focus becomes trapped, or processing appears stalled. | Use clear labels, visible progress and actionable errors; review keyboard flows early and recruit five testers before M5. | Prioritize task-blocking interface fixes and repeat the affected usability and keyboard checks. | Interface and usability owner |

## Risk review and escalation

At each review, update the likelihood, impact, assigned person's name, observed
trigger, mitigation status and next action for each open risk. Prioritize High
impact risks that have triggered or have High likelihood. Escalate any risk
that threatens a milestone or a release-blocking quality requirement at the
next check-in, or immediately if local data is at risk.

A risk is closed only when there is evidence that its mitigation works or its
exposure no longer applies. Preserve the decision and evidence in the project
record so that the final report distinguishes resolved risks from accepted
limitations.
