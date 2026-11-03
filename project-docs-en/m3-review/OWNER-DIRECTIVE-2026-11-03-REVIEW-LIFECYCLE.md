# Owner Directive 2026-11-03 — Review Moved Into the Implementation Lifecycle

**Status:** owner decision, recorded as directed by the Project Owner (Execution Authorization, 2026-11-03).
**Scope:** review gating only. It does not change any owner decision (`DECISIONS.md`), M0, the 22 fixtures, the Arabic sources, or any acceptance criterion.

## 1. Decision

1. Independent AI review and independent human engineering review (Q11; GOV-013; external dependencies E-07, E-08, E-09) are **not prerequisites for starting implementation**.
2. These reviews are performed **during or after** the relevant implementation phases.
3. Before passing the following high-risk gates, the relevant review must be **completed and recorded**:
   - **P3** — relationship-governance writes;
   - **P5** — RLS and concurrency enforcement;
   - **P6** — privacy and deletion implementation.
4. A review is never represented as completed until it has actually occurred and left a review record (reviewer identity, scope, findings, and disposition).
5. The directive does not weaken automated tests, security validation, or acceptance criteria.

## 2. Superseded requirement (historical record preserved)

The previous requirement, recorded in `IMPLEMENTATION-ROADMAP.md` (Independent review gate), `IMPLEMENTATION-READINESS-REPORT.md` (§6 and §7), `EXTERNAL-DEPENDENCIES-REGISTER.md` (E-07 to E-09), `03-REQUIREMENTS.md` (GOV-013), `05-CONFLICTS-AND-GAPS.md` (CG-43), and `15-UNRESOLVED-CONTRADICTIONS.md`, required the Q11 review **before** M3 and before implementation of high-risk phases. That requirement is superseded for the start of implementation by this directive. The original text is retained in those files as the historical record and is not deleted.

## 3. Relationship to other gates (unchanged)

- The owner approval of the conceptual design (M3-R1 verdict NOT APPROVED) remains an open owner action. This directive does not approve the design.
- Open owner decisions in `IMPLEMENTATION-READINESS-REPORT.md` §5 remain open unless they are decided by the owner.
- External dependencies E-01 to E-06 and E-10 to E-12 are unchanged by this directive.

## 4. Verification standard

No document may state that a review was performed unless a review record exists in `project-docs-en/m3-review/` or another owner-designated location. As of this directive, no Q11 review record exists.
