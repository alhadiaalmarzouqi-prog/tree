# External Dependencies and Legal/Privacy Review Register

**Status:** tracks only matters that need legal advice, external review, or a real human approval. Engineering choices are not listed here (they are in `TECHNICAL-DECISIONS.md`). Nothing here is marked complete unless evidence exists.

| ID | Matter | Type | Blocks | Evidence of completion | Status |
|---|---|---|---|---|---|
| E-01 | Account-to-Person verification method: which additional evidence is acceptable and how disputes are reviewed | Legal and privacy review; owner policy (OQ-21-10, DR-30 / OPEN-19) | P8 and any association feature | Written review record | OPEN, NOT STARTED |
| E-02 | Deceased-person privacy and access rules, including living people named in deceased records | Legal and privacy review (OQ-21-12) | P6 production release | Written review record | OPEN |
| E-03 | Retention and deletion: account deletion, Person deletion, audit retention, pseudonymous audit identifiers, crypto-erase | Legal review (Q7, DR-19 remainder, DD-25) | P6 | Written review record | OPEN |
| E-04 | Marriage-recognition and cultural rules for each country served (no validity judgment is made by the platform) | Legal and cultural review per country (DD-10, R-11) | Country launch for each country | Per-country review record | OPEN |
| E-05 | Abuse-reporting, appeal, and temporary-restriction procedures | Legal review and owner policy (DD-28) | P11 | Written procedure approved by owner | OPEN |
| E-06 | Storage of login history and approximate location | Privacy review (R-09, DD-27) | P1 | Written review record | OPEN |
| E-07 | Independent AI review of the M3 documentation baseline | Process gate (Q11) — **moved into lifecycle by owner directive 2026-11-03** | Completion required before passing P3, P5, P6 high-risk gates (no longer blocks P0 or implementation start) | Review report with reviewer identity and findings | NOT PERFORMED (lifecycle; not represented as done) |
| E-08 | Independent human software-engineer review | Process gate (Q11, GOV-013) — **moved into lifecycle by owner directive 2026-11-03** | Completion required before passing P3, P5, P6 high-risk gates (no longer blocks P0 or implementation start) | Signed review record | NOT PERFORMED (lifecycle; not represented as done) |
| E-09 | Owner approval of review outcome | Process gate (Q11) — **moved into lifecycle by owner directive 2026-11-03** | Required before passing P3, P5, P6 high-risk gates | Owner approval record | NOT PERFORMED; no longer blocks implementation start |

**Superseded (historical record):** before 2026-11-03, E-07 to E-09 had the status "BLOCKED" for implementation of P3, P5 and P6, and E-09 was "BLOCKED by E-07, E-08". The owner directive of 2026-11-03 (`OWNER-DIRECTIVE-2026-11-03-REVIEW-LIFECYCLE.md`) supersedes that blocking effect for the start of implementation only.
| E-10 | Country-specific data-protection requirements for each country where users are hosted | Legal review | Hosting decision (DR-21 / OPEN-19 region) | Per-jurisdiction review | OPEN |
| E-11 | Key custody and recovery procedure approval (P13) | Security review by a qualified person | Production release | Written review and drill record | OPEN |
| E-12 | Rules for minors: visibility of minors' data, consent, and protection beyond default restriction | Legal review (directive §9, minors protection) | Any feature that displays or collects data about a minor; P6 | Written review record | OPEN |

## Notes

- A row being OPEN does not block unrelated foundational engineering. The per-phase gate in `IMPLEMENTATION-ROADMAP.md` states which phases each row blocks.
- No row is closed by this document. Closure requires the listed evidence.
