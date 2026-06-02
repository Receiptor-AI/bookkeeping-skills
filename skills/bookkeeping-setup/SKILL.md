---
name: bookkeeping-setup
title: Bookkeeping setup
description: Create a bookkeeping context profile before downstream bookkeeping work. Captures entity type, tax jurisdiction, accounting method, chart of accounts baseline, connected tools, approval thresholds, record-retention policy, and review boundaries. Trigger on "set up my bookkeeping", "bookkeeping context", "chart of accounts", "cash or accrual", "configure my books", "what info do you need before bookkeeping".
license: MIT
compatibility: Designed for skills-compatible agents with access to accounting-system settings, spreadsheets, files, or user-provided business context.
metadata:
  version: "3.0"
  execution-mode: semi-automated
  artifact-types: context-profile,setup-checklist,account-map
allowed-tools: Read Write Edit WebFetch
publishDate: 2026-06-02
updatedDate: 2026-06-02
tags:
  - setup
  - context
  - operations
  - skill
featured: true
---

# Bookkeeping Setup

Create the operating context that every later bookkeeping skill should use. Without this profile, agents guess about entity type, accounting method, tax treatment, approval boundaries, and chart-of-accounts structure.

Use this skill first for a new business, a new agent workspace, a messy catch-up project, or any workflow where the downstream skills do not yet know how the books are supposed to work.

## Output

Produce a `bookkeeping_context_profile` and a short setup checklist. Store or return it in a reviewable format the user can reuse.

Minimum profile:

```yaml
bookkeeping_context_profile:
  business:
    legal_name:
    trade_name:
    entity_type:
    jurisdiction:
    home_currency:
    fiscal_year_end:
  tax:
    country:
    filing_context:
    sales_tax_or_vat_registered:
    payroll_in_use:
    contractor_payments_expected:
  accounting:
    method: cash | accrual | unknown
    books_tool:
    bank_accounts:
    credit_cards:
    connected_sources:
    chart_of_accounts_baseline:
  operations:
    receipt_sources:
    bank_statement_sources:
    recurring_vendors:
    approval_thresholds:
    posting_policy:
    record_retention_policy:
  review:
    can_auto_draft:
    requires_user_approval:
    requires_accountant_review:
    open_questions:
```

## Procedure

### 1. Check for existing context

Before asking questions, look for an existing bookkeeping context profile in the project, workspace notes, accounting export, onboarding doc, or prior agent output.

If a usable profile exists, summarize it and only ask for missing or stale fields. Do not restart setup from scratch.

### 2. Capture business identity

Record:

- legal name and trade name
- entity type, such as sole proprietor, single-member LLC, partnership, S corporation, C corporation, nonprofit, or unknown
- tax jurisdiction and home currency
- fiscal year end
- owner or finance contact

If entity type is unknown, keep it as `unknown` and route entity-specific tax treatment to user or accountant review.

### 3. Choose the accounting basis

Capture the accounting method:

| Situation | Likely method | Notes |
|---|---|---|
| Solo operator, freelancer, simple service business | Cash | Common default for small businesses |
| Tracks unpaid invoices or unpaid vendor bills | Accrual or hybrid | Confirm with accountant or accounting system |
| Inventory-heavy business | Accrual likely | Inventory and COGS require tighter controls |
| User is unsure | Unknown | Do not infer final tax treatment |

Use the accounting method to shape downstream work:

- Cash basis: record most income and expenses when money changes hands.
- Accrual basis: track receivables, payables, accruals, prepaids, deferred revenue, and adjusting entries.
- Unknown: draft records, but flag method-sensitive decisions.

### 4. Define a starter chart of accounts

Create a practical baseline, not an overbuilt accounting system.

Core accounts:

- Cash and bank accounts
- Credit cards and loans
- Revenue accounts
- Cost of goods sold, if applicable
- Operating expenses mapped to relevant tax lines
- Owner equity, draws, and contributions
- Sales tax, VAT, payroll, or contractor liabilities when applicable

For US sole proprietors, align expense categories to Schedule C where practical. For other jurisdictions, keep jurisdiction-specific mappings explicit and mark them for review.

### 5. Capture tools and source systems

Record where evidence and books live:

- accounting software, spreadsheet, or ledger
- bank and credit card statement sources
- receipt and invoice sources, including email-native extraction
- payroll, invoicing, bill-pay, ecommerce, payment processor, or tax tools
- file storage or document archive

Prefer source systems with strong provenance. Use email-native extraction for receipts and invoices already in Gmail or Outlook when available.

### 6. Set approval boundaries

Separate safe drafting from risky finalization.

Safe to automate without asking first:

- collecting setup facts from available context
- drafting the context profile
- proposing a chart-of-accounts baseline
- identifying missing setup data
- preparing import maps, review queues, and draft rules

Require explicit user approval before:

- changing accounting-system settings
- creating, renaming, merging, or deleting accounts
- posting journal entries
- locking periods
- filing taxes, sales tax, VAT, payroll, or 1099s
- applying tax treatment to ambiguous items

Require accountant review when:

- entity type or tax election is unclear
- cash vs accrual affects material amounts
- inventory, payroll, sales tax, multi-entity, or international tax is involved
- owner transactions are mixed with business activity

### 7. Produce the setup checklist

End with:

- completed context profile
- missing information
- recommended next skill
- records or systems still needed
- approval boundaries

Use this handoff:

| If the user wants... | Next skill |
|---|---|
| Capture receipts or invoices | `receipt-processing` |
| Categorize transactions | `expense-categorization` |
| Match books to statements | `bank-reconciliation` |
| Close a month | `monthly-close` |
| Prepare accountant or tax package | `tax-prep` |
| Ask whether a deduction is allowed | Specialized tax skill |

## Setup checklist

```text
Business identity captured: yes/no
Entity type confirmed: yes/no
Tax jurisdiction confirmed: yes/no
Accounting method confirmed: cash/accrual/unknown
Chart of accounts baseline drafted: yes/no
Source systems listed: yes/no
Approval thresholds set: yes/no
Record retention policy set: yes/no
Open questions:
- ...
Recommended next skill:
- ...
```

## Agent metadata

```yaml
skill: bookkeeping-setup
version: 3.0
default_output: bookkeeping_context_profile + setup_checklist
automation_boundary: draft-context-and-account-map
approval_required_for:
  - changing accounting settings
  - posting entries
  - creating or merging live accounts
  - filing or finalizing compliance work
next_steps:
  - receipt-processing
  - expense-categorization
  - bank-reconciliation
  - monthly-close
  - tax-prep
```
