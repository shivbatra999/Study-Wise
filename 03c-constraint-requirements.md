## 3.3 Constraint requirements

| ID | Constraint (one sentence) | Source | Why it cannot be negotiated |
|---|---|---|---|
| CON-01 | The system shall not transmit course materials, questions, answers or quiz content to any destination outside the student's device. | C1; R7; SH2 | Privacy is the reason the product exists; without it Study-Wise is a weaker copy of cloud tools. Checked by capturing network traffic (e.g. Wireshark) during a 30-minute scripted session: no packets from Study-Wise to non-loopback addresses. |
| CON-02 | The system shall operate without any paid service, subscription or API key. | C2; SH1; SH6 | Target users and the team have no budget; a paid dependency would block both use and development. |
| CON-03 | The system shall run on student-owned laptops with Windows 11 or macOS 14 or later and no discrete GPU. | C3; SH1 (assumed, Q2) | Students will not buy hardware to study; a system that needs a GPU excludes most of them. |
| CON-04 | The system shall use only third-party components whose licences permit free use and publication of the project source. | C4; R4; R6; R2 | The course requires an instructor-accessible repository, and a licence violation cannot be fixed after release. |
