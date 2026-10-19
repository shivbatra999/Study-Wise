## 2.1 Product perspective and context

![Context diagram](diagrams/context.png)

The boundary sits around the part that turns a student's files and questions into cited answers and quizzes. That is the part with no off-the-shelf equivalent that respects CON-01, so it is ours to build. The language model and the runtime that executes it are deliberately outside the box: we call them but do not build or train them, which is why they appear as an external system and as dependency A2. The student's file system is external because Study-Wise only reads files the student chooses and never modifies them. The Internet and cloud AI services are drawn outside the boundary with no interface at all, because CON-01 forbids one. Instructors never interact with the system, but their material enters through the file-system interface, which is why they are stakeholders without being actors.

## 2.2 Stakeholders and how we reached them

| Stakeholder | Role in relation to the system | What they need from it | How we learned this |
|---|---|---|---|
| SH1: Students (primary users) | Import their materials, ask questions, take practice quizzes | Correct answers traceable to their own slides; practice questions for exam prep; no cost; nothing uploaded | **Assumption** — from the six team members' own experience as students in this user class. To be confirmed by at least 8 student interviews and a hardware survey (15+ responses) run 22–27 Oct 2026 by Lavanya Bansal; results committed to /docs/elicitation. |
| SH2: Instructors who author the materials (never use it) | Their slides and notes are the system's input | Their material is not uploaded, redistributed or shared beyond the student who downloaded it | **Assumption** — inferred from typical course-material terms; not yet confirmed with any instructor (Q3). |
| SH3: UTD Office of Community Standards and Conduct (never uses it) | Enforces academic integrity | The tool supports practice and does not produce or submit graded work | Document review of the Student Code of Conduct [R5]. |
| SH4: Model and runtime licensors (never use it) | Own the LLM runtime and model weights we depend on | Use within licence terms: attribution, acceptable-use rules, no redistribution of weights | Document review of licences [R4], [R6]. |
| SH5: CS 3354 instructor and TAs | Set the deliverables and assess them | Deliverables on the syllabus dates; a repository they can open; requirements they can test | Syllabus and P1 template [R2]. |
| SH6: Development team (builders and maintainers) | Build, operate and test the system on their own laptops | A scope achievable by six students in one term with $0 budget | Team meeting, 15 Oct 2026; feasibility in 2.6. |

## 2.3 User characteristics

**Technical students (CS, CE, SE and other STEM majors):** Comfortable installing desktop software and following a README; many have used cloud chat assistants. They cannot be assumed to understand how LLMs work, so they need to be told when an answer has no support in their materials rather than receive a confident guess (FR-09). They use personal laptops, often on battery, and use the system hardest in the days before an exam, when they are short on time and impatient with slow answers (QR-01).

**Non-technical students (all other majors):** Can import files and type questions but cannot be assumed to use a terminal, install a runtime, or diagnose why a model is not running. This user class is why FR-15 exists and why first-time setup is a use case of its own (UC-06, Q5).

**Constraints from both classes:** Laptops are assumed to range from 8 GB to 16 GB+ RAM with no dedicated GPU (A1, CON-03); the hardware survey (22–27 Oct, Q2) will replace this assumption with data. Some students use screen readers or keyboard-only navigation; at P1 we have not written an accessibility requirement and record this as open question Q7 rather than invent a threshold.
