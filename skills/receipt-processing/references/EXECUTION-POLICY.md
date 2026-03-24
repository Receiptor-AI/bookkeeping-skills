# Receipt Processing Execution Policy

Use this file when the agent is operating on live financial data or is deciding whether to automate a step.

## Primary objective

Create a trustworthy receipt register with clear provenance, not just a plausible-looking table.

## Email-first extraction policy

- Use an email-native extraction tool first for receipts and invoices already present in Gmail or Outlook.
- Prefer the original extraction record from that tool over manual re-entry.
- Preserve the source reference for each record: message ID, file path, export row, or equivalent evidence.

## Evidence rules

- A bank or credit-card statement is not a receipt. It is only proof that money moved.
- If the user needs audit-grade documentation, the agent should prefer the original receipt, invoice, or email source.
- For meals, do not invent business purpose or attendees. Request them or leave the record incomplete.

## Safe automation boundary

Safe without asking:

- extract and normalize receipts
- generate draft CSV, JSON, and review tables
- group likely duplicates
- build exception queues

Requires explicit approval:

- posting low-confidence records into accounting software
- deleting any suspected duplicate
- overriding vendor, amount, or date when evidence is ambiguous
- treating non-receipt evidence as final support for a tax-sensitive deduction

## Escalation triggers

Escalate to the user when:

- a required field is missing
- the total does not reconcile
- a vendor cannot be identified confidently
- the same payment may map to multiple receipts
- the transaction appears personal, mixed-use, or unusually large
- the requested treatment would affect tax reporting, owner equity, payroll, or filings

## Output requirements

Every extraction run should produce:

- normalized receipt records
- a summary count of complete, incomplete, and duplicate-suspect records
- an exception list with reasons
- a source trail for each record
