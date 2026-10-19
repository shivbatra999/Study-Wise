## 4.4 Repository and tooling

Repository URL: https://github.com/shivbatra999/Study-Wise

Access: The repository is public, all six team members have write access. Dr. Seker and TAs can open the repo using the URL from above.

Branches: The main branch consists of reviewed work and is the baseline for each deliverable. Each member works on a short lived branch named `<initials>-<topic>` (for example, `na-section4`) and merges into main using a pull request that at least one other member has reviewed. Nobody commits directly to main.

Commits: Each commit message starts with a verb and names the section or requirements it touches, for example "Add risk mitigations to 4.3" or "Fix FR-05 acceptance criterion". Commits are made under each member's own GitHub account so the contribution record in section 0 matches the history.

Issues: Each open question (Q1 to Q6), each milestone in 4.2 and each requirement change is tracked as a GitHub issue with an assignee and a due date. Labels separate requirements, question, risk and docs. An issue is closed only when its resolution is written into the document, and the issue number is cited in the revision history in section 0.

Folders: /docs/elicitation for interview notes and survey results, /docs/benchmark for the 20-question benchmark set, and /spike-01 for the feasibility spike.

## 4.5 Declaration of AI tool use

| Tool | What it was used for | Who used it | How the output was checked |
|---|---|---|---|
| Claude (Anthropic) | Drafting first versions of P1 sections and the two diagrams from our README and the P1 template; checking requirement wording against the template rules | Lokesh, Nandhan | Each section owner reviewed and rewrote their section; every requirement was checked by hand against the Chapter 5 testability rule (single "shall", measurable, stated check); assumptions and unsourced claims were marked or removed. |
