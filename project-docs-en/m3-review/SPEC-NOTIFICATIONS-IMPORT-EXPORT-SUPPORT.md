# Specification: Notifications, Import/Export, Backups, Abuse, Support, Internationalization

**Status:** design specification derived from DD-14, DD-25–DD-29, DD-32, DD-38, and the owner features in `DECISIONS.md` §3A/§3C and the directive §14. No numeric limits are set here (owner policy; OQ-21-07).

## 1. Notifications

- Notifications go only to eligible participants, never to everyone (Q20).
- Daily limits and batching are configurable.
- **Critical class** (security, account integrity, privacy, safety, relationship governance) bypasses ordinary daily limits, is never silently dropped, and is escalated if unread (DD-32, TD-12).
- Pending governance items remain visible in the review queue regardless of batching (OQ-21-07).
- An expired response period is never automatic acceptance or rejection.

## 2. Import (GEDCOM, Excel, CSV)

- Stage, preview, validate, detect duplicates, show match suggestions, report errors, and let the user review before commit.
- No imported relationship is confirmed automatically (DD-26). Imported relations enter the proposal lifecycle.
- Matching never merges Persons under uncertainty.

## 3. Export (PDF, image, structured data)

- Every export is filtered by the requester's permissions. Hidden fields are omitted, not blanked silently.
- Exports must indicate whether the content is complete, paginated, or incomplete (DD-30).

## 4. Personal backups

- Configurable schedule; separate from platform operational backups.
- Restore only data the user is permitted to restore; conflicts reconciled; newer platform data never overwritten indiscriminately.

## 5. Abuse, blocking, impersonation, and appeal

- Block prevents direct communication; it does not delete or invalidate relationships (DD-28).
- Reports are reviewed by someone other than the original reporter's target where practical.
- Temporary privilege freeze only on strong indicators; the accused holder is notified in a way that does not reveal the reporter.
- Appeal is reviewed independently of the original decision (TD-14).
- Procedures require owner approval and legal review (E-05).

## 6. Support center

- Categories: technical, account, privacy, relationship, report, suggestion.
- Tickets with attachments, status, replies, and staff assignment.
- Staff see only what the ticket requires (DD-26, DD-28).

## 7. Internationalization

- Arabic and English at launch; locale structure extensible.
- Country-specific phone formats and calling codes, administrative subdivisions, time zones.
- No assumption that names, phone numbers, or family structures follow one country's convention.
- Marriage recognition rules are per country and are not decided by the platform (E-04).
