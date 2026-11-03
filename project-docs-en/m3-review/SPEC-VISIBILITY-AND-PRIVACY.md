# Specification: Visibility, Authorization, Privacy, and Audit

**Status:** design specification derived from DD-07, DD-20–DD-22, DD-35, DD-37, and the visibility decisions in `DECISIONS.md` §3C. It does not add decisions.

## 1. Two separate visibility layers

- **Layer G (graph visibility):** whether a Person and a relationship path are visible to a viewer. Derived from confirmed relationships and network boundaries (OQ-21-03).
- **Layer F (field visibility):** whether a viewer can see a specific personal field. Controlled by the Person's own settings (DD-20).
- A viewer may see that a path exists without seeing any sensitive field (DD-37).
- Default for sensitive fields: no access (least privilege).

## 2. Access matrix (default posture)

| Viewer relationship to subject | Graph (Layer G) | Sensitive fields (Layer F) |
|---|---|---|
| Biological parent or child | Visible if confirmed in a shared network | Only as the subject allows; no automatic parental access to a child's sensitive data (P11) |
| Sibling (per confirmed parent) | Visible if confirmed | Only as allowed |
| In-law or marriage connection | Visible as a labelled marriage edge | No access by marriage alone (DD-10, §17.1) |
| Person seen in another network | Path only, labelled | No access to that network's details (OQ-21-03) |
| Deceased Person | Visible as deceased | Sensitive fields remain protected (OQ-21-12) |
| Living person named in a deceased record | Visible as living | Protected |
| Minor | Visible within the network | Sensitive fields restricted by default. Minor-specific rules require legal review, tracked as E-12 in `EXTERNAL-DEPENDENCIES-REGISTER.md` |
| Support staff | Only the minimum needed for a ticket | None by default |

**Rule:** where no explicit permission exists, sensitive-field access is denied. Access is never granted from marriage or family proximity alone.

## 3. Authorization enforcement

- Application authorization is mandatory for every read and write.
- Row-level security is an additional database boundary (DD-21, TD-04). It does not replace application authorization.
- Client-side hiding is never a control.

## 4. Audit

- Ordinary audit metadata (actor, time, action, affected entity) is visible to the actor and to governance participants as allowed.
- Sensitive before and after values are visible only to authorized audit roles, and every such access is logged (DD-22, DD-35).
- No ordinary role can modify or delete audit entries (TD-09).
- Retention: indefinite by default, subject to the legal review in E-03.

## 5. Deletion interaction

- Account deletion and Person deletion are separate (DD-25).
- Blocking, restriction, and network departure never delete Person records or relationships (DD-28, DD-24).
