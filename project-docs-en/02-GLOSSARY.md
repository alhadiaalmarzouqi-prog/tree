# Controlled Technical Glossary

**Purpose:** Define the English terminology used consistently across this documentation set. Identify where a term comes from in the Arabic sources and how it is used here.
**Scope:** Nouns and phrases used throughout the documents. This glossary does not create new requirements or decisions.
**Status:** Draft — reconstructed from `REQUIREMENTS.md`, `MASTER-ARCHITECTURE.md`, `KINSHIP-MATHEMATICAL-REFERENCE.md`, `CONFLICTS-AND-GAPS.md`, and `DECISIONS-REQUIRED.md`.
**Last verified:** 2026-11-01.
**Related documents:** `03-REQUIREMENTS.md`, `09-MASTER-ARCHITECTURE.md`.

## Conventions

- Terms are singular English nouns unless otherwise noted.
- `[V: file]` marks a term whose source wording is verifiable in the named source file.
- Where the Arabic wording differs in a way that affects meaning, the English document quotes the Arabic and cites the source.

## Terms

| Term | Definition/usage | Arabic source equivalent | Source |
|---|---|---|---|
| Account | Access credential of a registered user; distinct from a Person Record. | حساب المستخدم | `REQUIREMENTS.md` FR-003; `MASTER-ARCHITECTURE.md` §3 |
| Person Record | Node in the kinship network representing a person; exists even without an account. | سجل الشخص | `REQUIREMENTS.md` FR-002–FR-005; `MASTER-ARCHITECTURE.md` §3 |
| Unregistered Person | Person with a record but no account; created by a relative with limited permissions. | شخص غير مسجل | `REQUIREMENTS.md` FR-004; `MASTER-ARCHITECTURE.md` §3.2 |
| Biological Link | Edge in the biological kinship graph, directed from child to parent, with parent role `FATHER` or `MOTHER`. | رابط أبوة | `KINSHIP-MATHEMATICAL-REFERENCE.md` §B.1; `MASTER-ARCHITECTURE.md` §4 |
| Network-Confirmed Link | Link that passed the endorsement/confirmation cycle and is usable in kinship calculation. **M2-R23 note:** "network-confirmed" means adopted within one family network under that network's rules (`DECISIONS.md` §3B.4, OQ-21-16). It does not mean a universally established biological fact. | رابط مؤكد بالشبكة | `MASTER-ARCHITECTURE.md` §5; `DECISIONS.md` §3B.4 |
| Link State | Conceptual state of a link: proposed, awaiting confirmation, confirmed, disputed, rejected, unresolved, corrected, cancelled. Conceptual, not a table. | حالة الرابط | `MASTER-ARCHITECTURE.md` §5.1 |
| Endorsement Cycle / Network Confirmation | Process by which eligible members confirm or object to a proposed link. | دورة التأكيد الشبكي | `REQUIREMENTS.md` FR-017; `MASTER-ARCHITECTURE.md` §5.3 |
| Independent Evidence | Evidence supporting a link that is not the parties' mutual agreement; its exact representation is OPEN-3. | أدلة مستقلة | `REQUIREMENTS.md` FR-018; `MASTER-ARCHITECTURE.md` §5.6 |
| Kinship Engine | Internal component that computes paths, common ancestors, junction points, and pair counts per M0. | محرك القرابة | `MASTER-ARCHITECTURE.md` §2.2; `KINSHIP-MATHEMATICAL-REFERENCE.md` |
| Upward Path | Sequence of vertices from a person to an ancestor via recorded parent edges. | مسار صاعد | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.1 |
| Path Length | Number of edges in a path; identity path length = 0. | طول المسار | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.2 |
| Common Ancestors (COMMON) | Set of ancestors reachable from both queried persons. | مجموعة الأسلاف المشتركة | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.4 |
| Valid Path Pair | Pair of paths to the same ancestor whose vertex sets intersect only at that ancestor. | زوج مسارات صالح | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.5 |
| Valid Junction Ancestors (J) | Ancestors with at least one valid path pair. J ⊆ COMMON. | نقاط الاتصال الصالحة | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.6 |
| Valid Path Pair Count (R) | Number of valid path pairs; explicitly NOT a count of human relationships. | عدد أزواج المسارات الصالحة | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.7 |
| Generational Distances (a, b) | Lengths of the two paths in a pair. | المسافات الجيلية | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.8 |
| Combined Length (L) | a + b; number of edges across the pair; not a kinship degree. | الطول المدمج | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.9 |
| Direct Line | Pair with a = 0 or b = 0 (ancestor–descendant). | خط مباشر | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.10 |
| Sibling Classification | Full, paternal half, or maternal half; derived from confirmed shared parents and their roles. | تصنيف الأشقاء | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.11 |
| Cousin Degree / Removal | Defined only for a, b ≥ 2: degree = min(a,b) − 1; removal = |a − b|. | درجة بن العم / الإزالة | `KINSHIP-MATHEMATICAL-REFERENCE.md` §C.13 |
| Pedigree Overlap | Two paths to one ancestor via related parents; valid structure, NOT a cycle. | تداخل الأسلاف | `KINSHIP-MATHEMATICAL-REFERENCE.md` §B.1(6) |
| Audit Trail / Audit Record | Immutable append-only log of link changes; distinct from current state. | سجل التدقيق | `REQUIREMENTS.md` FR-035; `MASTER-ARCHITECTURE.md` §8 |
| Closure Table | Derived index of ancestor–descendant pairs; design per DR-02/DR-03, in conflict with DR-28. | جدول Closure | `CONFLICTS-AND-GAPS.md` CG-02; `DECISIONS-REQUIRED.md` DR-02/DR-03 |
| Event Log | Proposed alternate history model (append-only) per DR-28; conflicts with DR-02. | سجل الأحداث | `DECISIONS-REQUIRED.md` DR-28 |
| RLS | Row-Level Security on PostgreSQL; an extra layer, not a replacement for application authorization. | RLS | `MASTER-ARCHITECTURE.md` §7.4 |
| Deceased Node | Visible node for a deceased person; does not vote, has no proxy. | المتوفى | `MASTER-ARCHITECTURE.md` §5.3 |
| Degree Ten (KD-02) | Definition of the "tenth degree" is OPEN; the reference does not decide it. | الدرجة العاشرة | `KINSHIP-MATHEMATICAL-REFERENCE.md` §A.2; `MASTER-ARCHITECTURE.md` OPEN-5 |
| Terminology Dictionary (KD-01/DR-16) | Independent, versioned data file for Arabic/Libyan kinship terms; not defined by mathematics. | قاموس المصطلحات | `KINSHIP-MATHEMATICAL-REFERENCE.md` §A.3; `DECISIONS-REQUIRED.md` DR-16 |

## Notes on equivalence

1. Some Arabic terms have no single English form in the sources (for example "التأكيد الشبكي" vs "تأكيد الطرفين"). Where meaning would be affected, the English document quotes the Arabic and marks it `[V: source]`.
2. This glossary does not define kinship naming rules; naming rules (KD-01) remain OPEN.
3. `[V: ...]` citations point to `project-docs/<path>` (Arabic sources), which stay the authority. Every term here is a documentation convention, not a new technical decision.