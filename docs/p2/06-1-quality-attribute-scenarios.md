# 6.1 Architectural drivers: quality-attribute scenarios

Owner: Nandhan Alahari

| QAS | Quality attribute | Stimulus | Artifact | Response | Response measure | From |
|---|---|---|---|---|---|---|
| QAS-01 | Performance | A student submits one of the 20 benchmark questions on the reference laptop, with a model of up to 8B parameters and no other heavy application open | AnswerService, PassageIndex, RuntimeGateway and the local runtime | The answer is fully displayed with its citations | At least 18 of 20 answers within 20 s. S-01: met with the 3B model on an 8 GB laptop (20 of 20; 18th-fastest 15.1 s) | QR-01 |
| QAS-02 | Performance | A student imports a 50-page text PDF into a course on a freshly started application | MaterialIngestor, PassageIndex, LocalStore | The material is listed as ready for questions | Median of 5 imports at most 90 s | QR-02 |
| QAS-03 | Security (privacy) | A scripted 30-minute session: import two decks, ask the 20 benchmark questions, take one 10-question quiz, while network traffic is captured | The whole system as deployed (6.4) | No course material, question, answer or quiz content is sent off the device | 0 packets from Study-Wise processes to any non-loopback address | CON-01 |
| QAS-04 | Availability | The local runtime is stopped while Study-Wise is running, and the student asks a question | RuntimeGateway, AnswerService, StudyUI | The student is told the runtime is not running, with the steps to start it; the application keeps running | Message shown within 5 s; 0 materials lost; the same question succeeds once the runtime is restarted | FR-15 (measure added, CH-09) |

**Constraints that shape the architecture.** CON-01 puts every component and every stored byte on the student's device and allows only loopback communication. CON-03 (laptop, no GPU) limits the model to roughly 8B parameters or fewer and makes generation the slowest step. CON-02 and CON-04 limit us to free, openly licensed components (Ollama, MIT; SQLite, public domain; pypdf, BSD; python-pptx, MIT).

**Evidence behind the measures.** QAS-01's measure is QR-01's pass rule (the 18th-fastest of 20 answers within 20 s). Spike S-01 (section 8, `/spikes/S-01/results/llama3.2-3b-summary.json`) measured it on an 8 GB laptop: 20 of 20 within 20 s with `llama3.2:3b`; the 8B model did not run on that laptop. QAS-02 to QAS-04 are not measured yet; they are measured once the components exist (10.2).
