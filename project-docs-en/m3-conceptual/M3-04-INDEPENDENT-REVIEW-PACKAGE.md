# M3-04 — Independent Review Package (M3 Conceptual Architecture)

**Status:** review package prepared. **No review has been performed by this document.** Review status is recorded separately in §5.
**Language:** English.

---

## 1. Three separate activities

| Activity | Performed by | Status |
|---|---|---|
| 1. Architecture authoring | Authoring agent (this session) | Completed for M3 conceptual documents `M3-01` to `M3-03` |
| 2. Independent AI review | A separate reviewer agent with no authoring role | **Not performed** (see §5) |
| 3. Independent human software-engineer review | A human engineer independent of the authoring process | **Not performed. Pending.** |

The authoring agent must not act as reviewer. The reviewer must not be given the author's conclusions as a starting point.

---

## 2. Reviewer input (exact documents)

Reviewers receive these documents and the protected references, and nothing else from this session's conclusions:

1. `project-docs-en/DECISIONS.md` (all sections, including §3B, §3C, §4A).
2. `project-docs-en/m3-conceptual/M3-01-DOMAIN-MODEL.md`.
3. `project-docs-en/m3-conceptual/M3-02-PRIVACY-AUDIT-SECURITY.md`.
4. `project-docs-en/m3-conceptual/M3-03-MVP-SCOPE-AND-OPEN-ITEMS.md`.
5. `project-docs-en/09-MASTER-ARCHITECTURE.md` (§§3–9, §12, §19).
6. `project-docs-en/08-MATHEMATICAL-REFERENCE.md` (M0, read-only).
7. `project-docs/reference-fixtures/kinship-reference-cases.json` (read-only).

---

## 3. Review questions (the reviewer must answer each)

1. **Scope fit:** does the design match the product purpose (family discovery and awareness, not a legal authority), without unnecessary complexity?
2. **Person and Account separation:** does `M3-01` §3–§4 keep Person, Account, and association separate, with OQ-21-19 applied exactly?
3. **Seven concepts (OQ-21-14):** are the seven concepts kept distinct, with no collapsed status field?
4. **Network-specific adoption (OQ-21-01, OQ-21-16):** can one network accept and another reject without changing the other? Does any part imply a global biological determination?
5. **M0 compatibility:** does `M3-01` §8 leave M0 unchanged? Does it correctly state why a shortest-depth table is insufficient (path count, valid junction pairs, R)? Verify against M0 §C.3, §C.5, §C.7 and fixture conventions.
6. **Storage alternatives:** is the comparison in `M3-01` §8.4 fair, and does it avoid choosing an approach without analysis?
7. **Privacy and visibility:** does `M3-02` §1 respect Q10A, PRV-011–013, OQ-21-03 (default deny), and OQ-21-12?
8. **Authorization and RLS:** are application authorization and RLS described as complementary (P12, Q9)?
9. **Audit and integrity:** are append-only audit, same-transaction writing, and single-active-account rules (P2, P3, OQ-21-19) consistent?
10. **Correction and reopening:** does `M3-02` §4 keep previous states intact (Q17, OQ-21-06, OQ-21-18)?
11. **Notifications:** do review queues keep important items accessible (OQ-21-07)?
12. **Open items:** are the classes in `M3-03` §2 accurate, and is any open item wrongly described as decided?
13. **Missing requirements:** what is absent that would be needed for a safe first release?
14. **Performance:** are large-network risks identified, with no unsupported claims?

---

## 4. Required reviewer output

For each question: `AGREE`, `AGREE WITH CONCERN`, or `DISAGREE`, with the exact document section and a reason. Then list critical findings, data-model risks, authorization and privacy risks, concurrency and integrity risks, M0 compliance, network isolation, migration and recovery risks, performance, missing requirements, and any disagreement with the author.

Reviewers must state which documents they read, and whether they ran any check, with the exact command and result.

---

## 5. Review status (recorded truthfully)

| Review | Status | Evidence |
|---|---|---|
| Independent AI review | **Not performed.** No separate reviewer run has been recorded in this session. | None |
| Independent human engineer review | **Not performed. Pending.** | None |
| Owner approval of review outcome | Not applicable until reviews exist | None |

**Effect on work:** per the owner's instruction, the human review may remain pending while conceptual design proceeds. It blocks physical schema approval and production implementation (`DECISIONS.md` §3, Q11), not the conceptual documents.

---

## 6. Comparison and disagreement handling (when reviews exist)

1. Collect the AI findings and the human findings separately.
2. Compare them question by question.
3. Record each material disagreement, with its document section.
4. Resolve each disagreement by amending the document, or by recording it as an owner question if a product decision is needed.
5. Owner approves the outcome. Until then, nothing is marked reviewed.
