# Kinship Mathematical Reference (M0) — English Restatement

**Purpose:** English companion to the protected mathematical reference. It restates the reference definitions in English without changing any definition, formula, symbol, or meaning. It is not a translation license and not a replacement for the reference.
**Scope:** All sections of `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` (A–G).
**Status:** Draft — mechanical English restatement. **No mathematical recalculation was performed.** The 22 reference fixtures are protected and were not modified (SHA-256 verified in Phase A).
**Source references:** `project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md` (protected); `project-docs/reference-fixtures/kinship-reference-cases.json` (protected, 22 cases).
**Related documents:** `02-GLOSSARY.md`, `09-MASTER-ARCHITECTURE.md` §6, `16-VALIDATION.md`.
**Last verified:** 2026-11-01.

## Protection notice

Per the mission, this document must not change the reference's mathematical definitions, formulas, symbols, or meaning. This restatement was checked structurally against the reference and against the parsed fixture file (22 cases, expected identifiers, per-case structural checks in `16-VALIDATION.md`). A structural check and file-hash verification do **not** prove mathematical correctness; a full recalculation of the 22 fixtures is a separate authorized task and was not performed here.

## A. Scope and authority

### A.1 Purpose
The reference is the internal mathematical baseline for the biological-kinship engine. Future automated tests compare any implementation's output against the values computed here, without re-interpreting definitions or calculations.

### A.2 Content-type distinctions
| Type | Meaning | Examples in the reference |
|---|---|---|
| Reference mathematical definition | Structural definition applied to the graph; checkable by enumeration | path and its length, valid path pair, J, R |
| Naming convention | Conventional label; not a mathematical fact | "first-degree cousins", "uncle", "paternal half-siblings" |
| Pending owner decision | A choice mathematics does not settle, not yet approved | degree naming system (KD-01), tenth-degree definition (KD-02) |
| Undesigned implementation detail | Concerns the application or database | search limits, indexing, truncated-search response policy |

### A.3 Authority limits
- The reference does **not** prove any future application correct. An application is correct only if it passes the tests derived from these cases, plus other not-yet-written tests.
- The reference does **not** define final Arabic terms or a dialect dictionary (DR-16).
- The reference does **not** define primary/secondary relationship display policy.
- The reference does **not** approve any pending decision, and no value in it is owner approval of a related decision.

### A.4 What is not implemented or tested
- No application code uses this reference.
- No database, constraints, or migrations exist.
- No performance tests exist.
- The reference verifies specific examples; it does not prove the definition covers every possible tree.

## B. Graph model

### B.1 Reference rules (graph level)
1. **Node:** each person is a unique node with a stable identifier.
2. **Edge:** a directed parenting link from child to parent, carrying the parent role: `FATHER` or `MOTHER`.
3. **Biological calculations** use only **biologically confirmed** parenting links. Disputed links are not entered into the calculation as fact.
4. **Absence:** an unrecorded parent means unknown or unrecorded lineage, not that the person lacks a biological parent.
5. **Cycles:** the biological ancestor graph must be acyclic. A cycle is a data error, not a kinship relationship.
6. **Pedigree overlap:** two paths to one ancestor via related parents is **not** a cycle; it is a valid structure.

### B.2 Separate relationship types
| Type | Enters the biological calculation? | Note |
|---|---|---|
| Confirmed biological father/mother | Yes | the only source for path calculation |
| Marriage | No | separate in-law relationship, not a parenting link |
| Legal adoption | No | independent type (DR-14) |
| Breastfeeding (milk kinship) | No | independent, deferred type (DR-14) |
| Guardianship | No | independent type, bestows no lineage |
| Disputed or unconfirmed relationship | No | not shown as fact (FR-020) |

### B.3 Reference graph constraints (reference only, not an approved database rule)
- In the test cases, each person has at most one parent in the `FATHER` role and at most one in the `MOTHER` role.
- This constraint is a test setting, **not** an owner decision. It came from the test task as a model constraint and was not approved as a database rule. It remains pending.
- **Duplication/cycles:** a person is not their own parent, nor an ancestor of their parent. This is part of the cycle definition.

### B.4 Unspecified people in the cases
Any person not listed in a case's parents table is an independent person with no recorded parents in that test case. That makes them a terminal node; it does not mean they have no parent in reality.

## C. Reference mathematical definitions

### C.1 Upward path
An upward path from X to C is a vertex sequence `X = x₀ → x₁ → … → x_k = C` where each `x_{i+1}` is a parent of `x_i` in the recorded role. `k = 0` is allowed (identity path).

### C.2 Path length
The number of edges in the path, i.e., `k`. The identity path has length zero.

### C.3 Path count
The number of distinct sequences from X to C. Path count is not path length. Example: two paths to a grandparent, each of length 2 — the count is 2 and each length is 2.

### C.4 Common ancestor set (COMMON)
`COMMON(A, B) = { C | exists an upward path from A to C, and exists an upward path from B to C }`.

This set **includes every common ancestor**, even when the nearest ancestor lies on the way; such ancestors are not necessarily valid junction points.

### C.5 Valid path pair at C
For distinct persons A and B and ancestor C, the pair `(p, q)` is a valid junction pair if and only if:
1. `p` is an upward path from A to C.
2. `q` is an upward path from B to C.
3. `vertices(p) ∩ vertices(q) = {C}`, i.e., the paths meet only at C and share no other node before it.

Note: a valid pair is not evidence of an independent human relationship; it is a structural record used to derive classification.

### C.6 Valid junction ancestors (J)
`J(A, B) = { C | at least one valid path pair exists at C }`.

`J ⊆ COMMON`. It may be strict: in T13, `COMMON = {D, Gf, Gm}` and `J = {D}`.

### C.7 Valid path pair count (R)
`R(A, B) = number of valid pairs (p, q) over all C ∈ J`.

**Reference warning:** `R` is a count of path pairs, **not** a count of human relationships. `R` must not be used as a relationship count in any display or report. Multiple pairs with the same classification represent one aggregated relationship in display, while remaining recorded internally.

### C.8 Generational distances a and b
For a valid pair `(p, q)` at C: `a = length(p)` and `b = length(q)`.

### C.9 Combined length L
`L = a + b`. This is the number of edges in the full path between A and B via C, **not** a kinship degree.

### C.10 Direct lineage (ancestor–descendant)
If either `a = 0` or `b = 0`, the relationship is a direct line, measured by the generational distance `k = max(a, b)`.
- `(1,0)`: father and son.
- `(2,0)`: grandfather and grandson.
- `(3,0)`: higher grandfather and great-grandson.

The identity path is the path from an ancestor to itself (length zero) and is used only to represent this case; it is not a collateral connection.

### C.11 Siblings
`(1,1)` at C. Classification (full, paternal half, maternal half) is determined from the **confirmed shared parents and their roles**, not from `(1,1)` alone.
- Full siblings: shared parents are father and mother.
- Paternal half-siblings: the one shared parent is the father.
- Maternal half-siblings: the one shared parent is the mother.

### C.12 Avuncular
`(1,2)` or `(2,1)` at C. Direction and sex are required to derive the exact name (uncle, aunt, nephew, niece). These names **require the terminology dictionary** (DR-16) and sex; they are not derived from mathematics alone.

### C.13 Traditional cousins
Applied **only** when `a ≥ 2` and `b ≥ 2`:
- `cousin_degree = min(a, b) − 1`
- `removal = |a − b|`

Note: these are conventional genealogical classifications, not a universal religious, legal, or linguistic definition.

- `(2,2)`: first cousins (degree 1, removal 0).
- `(2,3)`: first cousins once removed (degree 1, removal 1).
- `(3,3)`: second cousins (degree 2, removal 0).
- `(3,4)`: second cousins once removed (degree 2, removal 1).

### C.14 Strict-usage conditions
- The formula `n = min(a,b) − 1` as "cousin degree" is applied only when `a, b ≥ 2`.
- It is **not** applied to siblings (`(1,1)` — would give 0, which is not a cousin), nor to avuncular pairs (`(1,2)`).
- The terms "half-cousin" or "one-sided cousin" are used only as a naming convention to be defined later.

## D. Conservative classification rules

| Case | Condition | Structural classification | Additional input for the name |
|---|---|---|---|
| Direct line | `min(a,b) = 0` | ancestor–descendant, distance `max(a,b)` | sex (father/mother, son/daughter) |
| Siblings | `(1,1)` | sibling | shared-parent role (full, paternal half, maternal half) |
| Avuncular | `(1,2)` or `(2,1)` | uncle/aunt or nephew/niece | direction and sex, father or mother side |
| Cousins | `a ≥ 2` and `b ≥ 2` | degree `min−1`, removal `|a−b|` | side of each path |
| Other cases | anything else | keep structure as is, no label | do not invent a label |

**General rule:** no Arabic name is assigned from `(a,b)` alone. The name comes after structural classification, from an approved dictionary.

## E. Reference case index

The complete cases (parents tables, paths, junction pairs) are stored in the protected companion file `project-docs/reference-fixtures/kinship-reference-cases.json`. The index below summarizes the adopted values; it does not recompute them. The fixture file was validated in Phase A: 22 cases, expected identifiers, per-case `valid_path_pair_count` equal to the length of `valid_path_pairs`.

## F. Known limitations

1. The reference cases are specific examples, not a general proof of completeness. It is not proven that the definition covers every possible kinship case.
2. Complete path enumeration suits only small examples; the number of paths can grow quickly in overlapping trees and is not a production solution.
3. Production search limits and truncation disclosure were not designed or measured. When used later, a truncated search must not display "no kinship".
4. There is no final Arabic dictionary. Names in this document are illustrative and require dictionary approval (DR-16).
5. There is no final primary/secondary display policy. The rules here concern internal calculation only.
6. This reference does not prove any future application correct.

## G. Reference cases (condensed index)

| ID | Description | `J` | `R` | `(a,b)` | Note |
|---|---|---|---|---|---|
| T01 | Father and his son | {P} | 1 | (1,0) | direct line |
| T02 | Grandfather and grandson | {G} | 1 | (2,0) | direct line |
| T03 | Full siblings | {F,M} | 2 | (1,1) per pair | full |
| T04 | Paternal half-siblings | {F} | 1 | (1,1) | from the father |
| T05 | Maternal half-siblings | {M} | 1 | (1,1) | from the mother |
| T06 | Uncle/nephew (father's side) | {G} | 1 | (2,1) | order by query |
| T07 | Uncle/nephew (mother's side) | {G} | 1 | (2,1) | order by query |
| T08 | First cousins (P and Q full siblings, children of Gf and Gm) | {Gf,Gm} | 2 | (2,2) per pair | both grandparents shared |
| T09 | First cousins once removed | {G} | 1 | (2,3) | one shared ancestor only (G) |
| T10 | Second cousins | {G} | 1 | (3,3) | one shared ancestor only (G) |
| T11 | Double first cousins | {G1,G2,H1,H2} | 4 | (2,2) per pair | four different ancestors |
| T12 | Pedigree overlap (F and M first cousins via Gf and Gm; R full sibling of P and Q; B child of R) | {Gf,Gm} | 4 | (3,2) per pair | pairs with a single label |
| T13 | Paternal half-siblings via D with higher ancestors | {D} | 1 | (1,1) | COMMON={D,Gf,Gm}; Gf and Gm excluded |
| T14 | No recorded common ancestor | ∅ | 0 | — | "no recorded kinship", not "no kinship at all" |
| ST-01 | S and T full siblings; F and B sons of S only | {S,G,H} | 3 | (2,1)@S, (3,2)@G/H | |
| ST-02 | S and T full siblings; F and B full siblings | {S,X,G,H} | 4 | (2,1)@S/X, (3,2)@G/H | |
| ST-03 | S and T paternal half-siblings; F and B paternal half-siblings | {S,G} | 2 | (2,1)@S, (3,2)@G | |
| ST-04 | S and T paternal half-siblings; F and B full siblings | {S,X,G} | 3 | (2,1)@S/X, (3,2)@G | |
| ST-05 | S and T maternal half-siblings; F and B paternal half-siblings | {S,H} | 2 | (2,1)@S, (3,2)@H | |
| ST-06 | S and T maternal half-siblings; F and B full siblings | {S,X,H} | 3 | (2,1)@S/X, (3,2)@H | |
| DI-05a | Related parents; query between the son and one grandparent | {G} | 2 | (2,0) per pair | valid pedigree overlap, not a cycle |
| DI-05b | Related parents; query between the two sons | {F,G} | 2 | (1,1) and (2,2) | A and B paternal half-siblings |

**Note on T09 and T10:** every connection passes through a single shared ancestor, G. There are no two shared grandparents. The common father of P and R (or GP and GQ) is G; the mothers differ.

**Note on T13:** A and B are paternal half-siblings because they share father D and have different mothers X and Y. That Gf and Gm are parents of D is ancestry information in COMMON and is not used to classify A and B. Pairs at Gf and Gm are excluded because the paths intersect at D; the valid pair at D remains.

**Note on DI-05b:** A and B are paternal half-siblings, not full siblings. The pair excluded at G is A-F-G with B-F-G because both share F; the valid pair at G is A-Mo-G with B-F-G, which remains in R.

**Note on DI-05a and DI-05b:** both represent valid pedigree overlap, not cycles.

Full details (parents tables, paths, pairs) are in: `project-docs/reference-fixtures/kinship-reference-cases.json`.