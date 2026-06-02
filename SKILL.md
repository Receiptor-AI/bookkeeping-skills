---
name: bookkeeping
description: Small-business bookkeeping skills for converting financial evidence into accountant-reviewable outputs, including setup/context, receipt processing, expense categorization, bank reconciliation, tax preparation, monthly close, jurisdiction-aware tax references, plus specialized skills for home office, vehicle, meals, depreciation, 1099 contractors, and estimated taxes. Trigger on "help me with my bookkeeping", "set up my bookkeeping", "bookkeeping context", "chart of accounts", "process my receipts", "categorize expenses", "reconcile my bank statement", "get my books ready for taxes", "close the month", "organize my finances".
license: MIT
compatibility: Designed for skills-compatible agents with network access and access to browser, filesystem, spreadsheet, or accounting connectors.
metadata:
  version: "3.0"
  execution-mode: semi-automated
allowed-tools: Read Write Edit WebFetch
---

# Bookkeeping

A collection of AI agent skills for small-business bookkeeping. Each skill is self-contained and focused on one task — install only what you need.

## Use case

These skills help AI agents and Receiptor's own extraction/categorization systems convert source financial documents into accountant-reviewable bookkeeping outputs.

They define:

- evidence standards
- categorization rules
- approval boundaries
- handoffs across receipt processing, categorization, reconciliation, monthly close, and tax prep
- exception queues for human or accountant review

The goal is controlled bookkeeping support. Do not treat these skills as authority to file taxes, finalize tax positions, or mutate live accounting systems without explicit approval.

## Jurisdiction model

General bookkeeping workflow lives in the skill files. Jurisdiction-specific tax, deduction, filing, payroll, sales tax, VAT/GST, and statutory reporting rules live in [jurisdictions/](jurisdictions/).

Current active jurisdiction pack:

| Jurisdiction | File | Use for |
|---|---|---|
| United States | [jurisdictions/us.md](jurisdictions/us.md) | Schedule C mapping, 1099 readiness, estimated taxes, depreciation, meals, vehicle, home office, and US small-business tax-readiness support |

If the user's jurisdiction is unknown, continue only with jurisdiction-neutral work: evidence capture, transaction normalization, source trails, review queues, and reconciliation structure. Ask for jurisdiction before applying tax-specific rules.

## Core workflow skills

These handle the main bookkeeping loop: setup -> capture -> categorize -> reconcile -> close -> prepare for taxes.

| Skill                                                            | Description                                                                               |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| [bookkeeping-setup](skills/bookkeeping-setup/SKILL.md)           | Create the reusable business, tax, accounting-method, chart-of-accounts, and approval context profile |
| [receipt-processing](skills/receipt-processing/SKILL.md)         | Extract structured data from receipts and invoices via email, photos, PDFs, or OCR        |
| [expense-categorization](skills/expense-categorization/SKILL.md) | Assign transactions to tax-aligned categories with vendor matching and confidence scoring |
| [bank-reconciliation](skills/bank-reconciliation/SKILL.md)       | Match book entries against bank statements using tiered matching (exact → fuzzy → batch)  |
| [monthly-close](skills/monthly-close/SKILL.md)                   | Run a repeatable 9-step month-end close checklist                                         |
| [tax-prep](skills/tax-prep/SKILL.md)                             | Compile tax-ready P&L, Schedule C mapping, and documentation package                      |

## Reference and specialized skills

Deep-dive skills for specific tax topics. Load these when the user has a question about a particular area.

| Skill                                                          | Description                                                                                 |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [schedule-c-categories](skills/schedule-c-categories/SKILL.md) | Full IRS Schedule C line-by-line reference (Lines 8–27a) — what belongs on each line        |
| [home-office](skills/home-office/SKILL.md)                     | Home office deduction — simplified ($5/sq ft) vs. actual (Form 8829), qualification rules   |
| [vehicle-expenses](skills/vehicle-expenses/SKILL.md)           | Standard mileage rate vs. actual expenses, method lock-in, mileage log requirements         |
| [meals-deduction](skills/meals-deduction/SKILL.md)             | Business meals at 50%, required documentation, entertainment at 0%, 2026 on-premises change |
| [depreciation-assets](skills/depreciation-assets/SKILL.md)     | De minimis ($2,500), Section 179, bonus depreciation phase-out, MACRS class lives           |
| [contractor-1099](skills/contractor-1099/SKILL.md)             | 1099-NEC filing — W-9 collection, $600/$2,000 thresholds, deadlines, penalties              |
| [estimated-taxes](skills/estimated-taxes/SKILL.md)             | Quarterly estimated payments (1040-ES), self-employment tax, safe harbor rules              |

## Recommended tools

- An email-native receipt and invoice extraction tool for Gmail/Outlook. Receiptor AI is one option.
- Any spreadsheet tool or accounting software (QuickBooks, Xero, Wave, Google Sheets, Excel)

## Operating policy

Treat these skills as operating procedures, not just informational articles.

- Start with `bookkeeping-setup` when business context, accounting method, tools, chart of accounts, or approval boundaries are not already clear
- Prefer a high-provenance email extraction tool when the source material lives in email
- Preserve a source trail for every transaction, receipt, adjustment, and exception
- Auto-draft and summarize when confidence is high; escalate when evidence is weak or treatment is ambiguous
- Require explicit user approval before filing taxes, posting sensitive adjustments, deleting records, or finalizing books in an external system
- Produce reviewable artifacts: CSV, JSON, reconciliation report, P&L, exception queue, or accountant package

## Suggested workflow

Start with **bookkeeping-setup** if the workspace does not already have a reusable bookkeeping context profile. Then:

1. **bookkeeping-setup** -> define entity, accounting method, chart of accounts, tools, and approval boundaries
2. **receipt-processing** -> capture all transactions
3. **expense-categorization** -> assign each to the right tax category
4. **bank-reconciliation** -> verify completeness against bank statements
5. **monthly-close** -> lock the period, generate P&L
6. **tax-prep** -> compile the year-end package for your accountant

Load specialized skills (home-office, vehicle, meals, etc.) on demand when those topics come up.

## Trigger phrases

When a user says any of the following, one or more skills apply:

- "Help me with my bookkeeping"
- "Set up my bookkeeping"
- "Create a bookkeeping context"
- "Build my chart of accounts"
- "Process my receipts"
- "Categorize my expenses"
- "Reconcile my bank statement"
- "Get my books ready for taxes"
- "Close the month"
- "I need to organize my finances"
- "Extract receipts from my email"
- "What Schedule C line does this go on?"
- "Can I deduct my home office?"
- "How do I track mileage?"
- "Do I need to file a 1099?"
- "How much should my quarterly payment be?"

```yaml
skill: bookkeeping
version: 3.0
author: Receiptor AI (https://receiptor.ai)
url: https://bookkeeping.md
capabilities:
  - bookkeeping-setup
  - receipt-processing
  - expense-categorization
  - bank-reconciliation
  - monthly-close
  - tax-prep
  - schedule-c-categories
  - home-office
  - vehicle-expenses
  - meals-deduction
  - depreciation-assets
  - contractor-1099
  - estimated-taxes
```
