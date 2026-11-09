# ADR-04 Default answer model: a 3B-class open-weight model

Owner: Nandhan Alahari (first drafted by Lokesh Reddy Penugonda from the S-01 results; reviewed, revised and committed by this member)

| Field | Content |
|---|---|
| Status | Accepted 8 Nov 2026 for the default; the 8B option on 16 GB laptops is revisited after the S-01 rerun (10.2) |
| Date and owner | Drafted 7 Nov 2026 by Lokesh Reddy Penugonda from S-01 results; revised by Nandhan Alahari; accepted by the team 8 Nov 2026 |
| Context (drivers) | QAS-01 (answer within 20 s) pulls toward a small model; QR-03 and QR-04 (answer and quiz quality) pull toward a larger one. CON-03: no discrete GPU, 8 to 16 GB RAM; the survey found 3 of 10 respondents have 8 GB or less (A1). Risk R1. |
| Options considered | (a) An 8B-class instruction model (`llama3.1:8b`, 4-bit). (b) A 3B-class model (`llama3.2:3b`, 4-bit). (c) Let the student choose any model. |
| Decision | Default to (b). Offer (a) only on laptops with at least 16 GB, once a second S-01 run on a 16 GB laptop shows it meets QAS-01. The model name is a setting read by RuntimeGateway (ADR-02). |
| Consequences | Favors speed and the 8 GB students: the 3B model met QAS-01 with room to spare. Costs answer quality: one reviewer's provisional read of the 3B answers is about 13 of 20 correct, below QR-03's 17, so R2 is now the main technical risk, and retrieval fixes (smaller chunks, more pages, a reranker) come before any larger model is reconsidered. (a) does not run on 8 GB at all. (c) was rejected as the default because untested models make QR-03 and QR-04 unverifiable. |
| Evidence | S-01 (section 8): 3B, 20 of 20 under 20 s, median 7.4 s, 18th-fastest 15.1 s; 8B, 486 s to load, then the 8 GB laptop froze and no benchmark answer completed. Results in `/spikes/S-01/results/`. |
| Related | QAS-01, ADR-02, R1, R2, CH-14, Q9 |
