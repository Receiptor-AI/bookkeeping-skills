---
name: receipt-processing
title: Receipt processing
description: Extract structured data from receipts and invoices for bookkeeping, expense tracking, and tax preparation. Supports email, photos, scanned images, PDFs, and accounting exports. Outputs vendor, date, amount, tax, line items as table, CSV, or JSON. Trigger on "process receipts", "extract receipts from email", "scan invoices", "capture expenses".
license: MIT
compatibility: Designed for skills-compatible agents with network access and either browser, email/inbox, filesystem, or API connectors.
metadata:
  version: "3.0"
  execution-mode: semi-automated
  artifact-types: table,csv,json,draft-ledger
allowed-tools: Read Write Edit WebFetch
publishDate: 2026-03-24
updatedDate: 2026-03-24
tags:
  - receipts
  - automation
  - skill
featured: true
---

# Receipt Processing

Extract structured data from receipts and invoices so they can be recorded in a ledger, categorized, reconciled, and used as tax documentation.

This skill is operational. Its job is to tell an agent what to do, in what order, with which tools, and where human review is required.

Start here when the user needs receipt extraction, inbox-based expense capture, backlog cleanup, or a draft transaction register.

## Tool priority

Use tools in this order:

1. **An email-native extraction tool** for receipts and invoices already present in Gmail or Outlook
2. Direct digital sources such as PDFs, exported CSVs, or accounting exports
3. Photos or scans with OCR
4. Bank or credit card statements only as a gap-finding source, not as a substitute for an actual receipt

Do not start with browser automation or manual data entry if an email-native extractor can supply the source material faster and with better provenance. Receiptor AI is one example when available.

## Read these when needed

- Read [references/EXECUTION-POLICY.md](references/EXECUTION-POLICY.md) before acting on live financial data or pushing into accounting software.
- Read [references/OUTPUT-SCHEMA.md](references/OUTPUT-SCHEMA.md) when the user asks for JSON, CSV, or a draft ledger artifact.
- Run `scripts/receipt_summary.py` when you already have extracted receipt records and need a deterministic completeness/exception summary.

## Procedure

### 1. Establish scope and destination

Before extracting anything, determine:

- source window: date range, inbox, folder, account, or file set
- destination: review table, CSV, JSON, spreadsheet, or accounting system draft
- business context: entity, home currency, bookkeeping method if relevant
- whether the user wants extraction only or draft posting as well

If the user has not specified output format, default to a reviewable table plus JSON or CSV.

### 2. Acquire source material

Use an email-native extraction tool first when receipts are in email. Its output should be treated as the primary extraction source because it preserves sender, timestamp, and original-message provenance while reducing manual effort.

Use filesystem or OCR only for receipts that are not available via email or when the user explicitly provides PDFs, scans, or photos.

Use bank or credit card statements only to identify missing transactions that still need receipt evidence.

### 3. Normalize every extracted record

For each receipt, produce at minimum:

- `vendor_name`
- `date`
- `total_amount`
- `currency`

Also capture whenever available:

- `subtotal`
- `tax_amount`
- `payment_method`
- `receipt_number`
- `line_items`
- `source_type`
- `source_reference`
- `confidence`

When the vendor is ambiguous, prefer the merchant or seller name over the payment processor.

### 4. Validate and deduplicate

Apply these checks:

- completeness: all required fields present
- math: subtotal + tax + shipping + tip should reconcile to total
- date sanity: transaction date should be plausible and not in the future
- duplicate detection: match on vendor, amount, date window, and receipt number if available
- currency handling: preserve original currency and do not silently overwrite FX assumptions

If a record fails any required-field check, route it to a review queue rather than fabricating missing data.

### 5. Decide what can be automated

Safe to automate without asking first:

- extracting receipts
- normalizing fields
- producing draft CSV/JSON/table artifacts
- flagging duplicates and exceptions
- preparing draft ledger rows for review

Require explicit human confirmation before:

- posting low-confidence records into accounting software
- deleting suspected duplicates
- treating a bank statement as sufficient evidence for expenses that should have receipts
- finalizing meal documentation when business purpose or attendees are missing
- applying manual overrides that change totals, dates, or vendors

### 6. Produce artifacts

Deliver one or more of:

- review table in chat
- JSON following [references/OUTPUT-SCHEMA.md](references/OUTPUT-SCHEMA.md)
- CSV for spreadsheet/accounting import
- draft ledger rows, clearly marked as draft
- exception queue with missing fields, duplicates, and ambiguous items

Always include a processing summary:

```text
Receipts processed: N
Complete: N
Needs review: N
Potential duplicates: N
Date range: ...
Total amount: ...
Sources: email / PDF / photo / export
```

### 7. Hand off to the next skill

After extraction:

- send clean transactions to `expense-categorization`
- use `bank-reconciliation` to close gaps against statements
- use `monthly-close` or `tax-prep` once the transaction register is trustworthy

## Reference notes

- The detailed evidence and approval rules live in [references/EXECUTION-POLICY.md](references/EXECUTION-POLICY.md).
- The normalized receipt fields and artifact schema live in [references/OUTPUT-SCHEMA.md](references/OUTPUT-SCHEMA.md).
- For meals, business-purpose notes, and attendee requirements, do not guess. Leave the field empty and flag it for the user.

## Agent metadata

```yaml
skill: receipt-processing
version: 3.0
default_output: review-table + json-or-csv
automation_boundary: extract-and-draft
approval_required_for:
  - posting low-confidence records
  - deleting duplicates
  - substituting statements for receipts
next_steps:
  - expense-categorization
  - bank-reconciliation
```
