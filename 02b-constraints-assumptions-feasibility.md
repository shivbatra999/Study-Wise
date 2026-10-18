## 2.4 Constraints

| ID | Constraint | Source | What it removes |
|---|---|---|---|
| C1 | No course material, question or generated content may leave the student's device. | Product vision [R7]; instructors' interest in their material (SH2) | Every cloud-hosted model or storage option |
| C2 | No paid services, subscriptions or API keys. | Product vision [R7]; students' cost need (SH1); team budget of $0 (SH6) | Commercial model APIs, even where they could be made private |
| C3 | Must run on students' own laptops (Windows 11 or macOS 14+, no discrete GPU). | Students (SH1), an assumption, see Q2 | Models too large to run on that hardware |
| C4 | Only components whose licences allow free use and publication of our source in a repository the instructor can open. | Licences [R4], [R6]; course repository requirement [R2] | Components with restrictive or unclear licences |

## 2.5 Assumptions and dependencies

| # | Assumption or dependency | What breaks if it does not hold |
|---|---|---|
| A1 | Assumption: most target students have laptops with at least 16 GB RAM. | A 7 to 8B-parameter model leaves little memory for a browser on 8 GB machines, so answers slow down and QR-01 becomes hard to reach; we would target smaller models with weaker answers (R4). |
| A2 | Dependency: a free local LLM runtime (Ollama [R4]) remains available for Windows and macOS and accepts requests from other programs on the same machine. | Q&A and quiz generation (FR-07, FR-10) have no model to call; we would have to switch runtimes, costing roughly a week of the schedule. |
| A3 | Assumption: course materials are text-based PDFs and PPTX files, not scans. | Imports appear to succeed but yield no text, so questions find nothing; OCR (currently out of scope) would be needed. FR-03 detects this case. |
| A4 | Assumption: processing instructor-provided materials locally for personal study is allowed by UTD and course policies. | The product's main input is disallowed; scope would shrink to student-written notes only (Q3, R3). |
| A5 | Dependency: an open-weight model small enough for A1 hardware produces usable quiz questions and grounded answers. | QR-03 and QR-04 fail; a larger model would violate C3, so features would have to be cut back to Q&A only (R6). |

## 2.6 Feasibility summary

| Feasibility gate | Verdict | Evidence behind the verdict |
|---|---|---|
| Technical | Feasible, conditional on A1 and A5 | Ollama documentation [R4] states 8 GB of RAM is the minimum for 7B models. No timing measurement exists yet: spike-01 is scheduled for 23 Oct (section 4.2) and its results will be committed to /spike-01. Until then the verdict rests on the vendor documentation, A1 and A5. Nandhan Alahari has prior Python experience from a UTD research internship; [add anyone with PDF-parsing experience and a link to a past repo, or delete this sentence]. |
| Operational | Feasible for technical students; uncertain for non-technical | All six team members are themselves users of the kind described in 2.3. Setup difficulty for non-technical students is untested, recorded as Q5 and risk R4, with two setup trials planned before P2. |
| Schedule | Feasible for the MUST set | 11 MUST functional requirements and 2 MUST quality requirements; the highest-effort features (OCR, sync, Canvas integration) are excluded in 1.2. The plan in 4.2 has dated milestones with owners through 8 November. |
| Economic / resource | Feasible | $0 cost: the runtime is MIT-licensed [R4]; candidate models are free to use [R6]; GitHub is free for students; development hardware is team-owned laptops. |
