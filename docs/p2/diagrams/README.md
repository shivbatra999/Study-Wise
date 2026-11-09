# P2 diagrams

Each figure has its exported image and, where the team made it in P2, its source file. Re-export after editing a source:

- Mermaid (`.mmd`): `mmdc -i fig5.1-domain-model.mmd -o fig5.1-domain-model.png -b white -s 2`
- Graphviz (`.dot`): `dot -Tpng -Gdpi=150 fig6.3-component-view.dot -o fig6.3-component-view.png`

| Figure | Section | Kind of model | Source |
|---|---|---|---|
| 2.1 Context diagram | 2.1 | Context (carried from P1) | P1 image |
| 3.4 Use case diagram | 3.4 | UML use case (carried from P1) | P1 image |
| 5.1 Domain model | 5.1 | UML class diagram, conceptual (analysis) | Hand-drawn by Pranab Neupane: `fig5.1-domain-model-pranab.jpeg`; text source `fig5.1-domain-model.mmd` |
| 5.2.1 UC-02 sequence | 5.2.1 | UML sequence diagram (analysis) | `fig5.2.1-seq-uc02.mmd` |
| 5.2.2 UC-03 sequence | 5.2.2 | UML sequence diagram (analysis) | `fig5.2.2-seq-uc03.mmd` |
| 6.3 Component view | 6.3 | UML component diagram (design) | `fig6.3-component-view.dot` |
| 6.4 Deployment view | 6.4 | UML deployment diagram with trust zones (design) | `fig6.4-deployment-view.dot` |
