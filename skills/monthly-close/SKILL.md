---
name: monthly-close
title: Monthly close
description: Repeatable month-end close checklist for small businesses — lock the period, process outstanding receipts via Receiptor AI, categorize remaining items, reconcile all accounts, review large transactions, check contractor 1099 thresholds, generate monthly P&L summary. Trigger on "close the month", "month-end close", "monthly bookkeeping", "close the books".
publishDate: 2026-03-24
updatedDate: 2026-03-24
tags:
  - close
  - reporting
  - operations
featured: true
---

# Monthly Close

A repeatable month-end close process for small businesses that produces reliable financial statements and catches errors before they compound.

## Why monthly close matters

Without a regular close, errors accumulate. A missed transaction in January becomes a cascading reconciliation problem by June. A miscategorized expense in March inflates a tax line by December. Monthly close is the discipline that keeps books trustworthy.

The purpose is simple: at the end of each month, verify that every transaction is recorded, categorized, and reconciled — then lock the period so nothing changes retroactively. The output is a set of financial statements you can actually trust.

## When to run

Close the prior month within the first 5–10 business days of the new month. Example: close March by April 10. Waiting longer means bank statements pile up, memory of transactions fades, and the close takes exponentially longer.

If you're catching up on multiple months, work chronologically from the oldest unclosed month forward. Each month's outstanding items roll into the next, so skipping ahead creates false discrepancies.

## Weekly habits that make monthly close fast

The businesses that close in 2 hours instead of 2 days do these things weekly:

**Capture receipts continuously.** Don't wait for month-end. Use [Receiptor AI](https://receiptor.ai) to extract receipts from email automatically — it processes new emails as they arrive, so by month-end, most receipts are already captured and structured.

**Categorize as you go.** When a new transaction appears in your accounting system, categorize it immediately while you remember the context. A transaction you categorize the day it happens takes 5 seconds. The same transaction 30 days later takes 5 minutes of investigation.

**Reconcile bank activity weekly.** Don't save reconciliation for month-end. Match transactions against your bank feed every week. This catches errors early and reduces the month-end reconciliation to a quick verification rather than a painful investigation.

**Flag unknowns immediately.** If you see a transaction you don't recognize, investigate now. Don't put it in "Other / Uncategorized" and forget about it.

## Month-end close sequence

### Step 1: Cut off the period

Stop entering new transactions dated in the closing month. Any late-arriving items (invoices dated March that arrive in April) get recorded in April with a note: "Service period: March." For accrual-basis businesses, you'd record these as an accrued expense in March — but most small businesses on cash basis simply record them when paid.

If your accounting software supports period locking, lock the prior month after close is complete. This prevents accidental backdating.

### Step 2: Process outstanding receipts

Pull any unrecorded transactions for the closing month:

**Email receipts** — If using [Receiptor AI](https://receiptor.ai), check for newly extracted receipts that haven't been entered into the books yet. Filter by the closing month's date range.

**Physical receipts** — Photograph or scan any paper receipts that accumulated during the month. Extract data and enter into the books.

**Recurring charges** — Verify that all known recurring charges (subscriptions, rent, loan payments, insurance premiums) were recorded. If any are missing, the bank reconciliation will catch them, but it's faster to check proactively.

**Pending invoices** — For accrual-basis businesses: any services received but not yet invoiced should be recorded as accrued expenses. For cash-basis: only record when paid.

### Step 3: Categorize uncategorized items

Review anything sitting in "Other / Uncategorized." Every item should land in a specific expense category mapped to a tax line. If the same vendor keeps ending up uncategorized, create a permanent vendor→category mapping so the agent auto-categorizes it going forward.

Common reasons items are uncategorized: ambiguous vendor name (solve by adding to vendor map), split-category purchase (split it), new type of expense (create or choose appropriate category), personal expense mixed in (remove from business books).

See the expense-categorization skill for the full category mapping.

### Step 4: Reconcile all accounts

For each bank account, credit card, and loan account:

1. Download or obtain the statement for the closing month.
2. Match every book entry against the statement.
3. Investigate and resolve every discrepancy.
4. Verify the adjusted book balance equals the statement ending balance.

See the bank-reconciliation skill for the detailed matching process.

**Checklist:**

| Account | Statement obtained? | Matched? | Discrepancies resolved? | Balance verified? |
|---------|---|---|---|---|
| Checking ****4521 | ☐ | ☐ | ☐ | ☐ |
| Savings ****7890 | ☐ | ☐ | ☐ | ☐ |
| Credit card ****3456 | ☐ | ☐ | ☐ | ☐ |
| PayPal business | ☐ | ☐ | ☐ | ☐ |

### Step 5: Review adjusting entries

These are journal entries that correct the books for items not captured by regular transaction processing:

**Prepaid expenses** — If you paid $1,200 for annual insurance in January, $100/month should be expensed and the remaining $1,100 sits as a prepaid asset. Each month, record: Debit Insurance Expense $100, Credit Prepaid Insurance $100. Most small businesses on cash basis skip this (they expense the full $1,200 when paid), but accrual-basis businesses must do it.

**Accrued expenses** — Services received but not yet billed. Example: your bookkeeper worked 10 hours in March but won't invoice until April. Accrual-basis: Debit Contract Labor $500, Credit Accrued Expenses $500. Reverse this entry in April when the invoice is paid.

**Depreciation** — If you have depreciable assets, record the monthly depreciation entry. Annual depreciation ÷ 12 = monthly amount. Debit Depreciation Expense, Credit Accumulated Depreciation.

**Unearned revenue** — If you collected payment for services not yet delivered, the payment is a liability (not revenue) until the service is performed. As you deliver, move from Unearned Revenue to Revenue. Example: annual subscription collected in January — recognize 1/12 as revenue each month.

**Inventory adjustments** — If you carry inventory, adjust for shrinkage, damage, or obsolescence identified during the month.

Most small businesses on cash basis only need depreciation entries from this list. The others are primarily for accrual-basis businesses.

### Step 6: Review large and unusual transactions

Pull any transaction that meets these criteria:

- Amount >$1,000 (or a threshold appropriate for the business size)
- Amount >2× the average for its category
- New vendor not seen in prior months
- Negative amounts (refunds, credits) over $500
- Round-number payments to individuals (potential contractor payments)

For each, verify: correct category, proper documentation (receipt exists), business purpose clear, not a duplicate.

### Step 7: Check contractor totals (US)

If you pay contractors, check year-to-date totals:

| Contractor | YTD paid | 1099 threshold | Status |
|---|---|---|---|
| Jane Smith | $4,200 | $600 | Above threshold — W-9 on file? |
| Bob Johnson | $450 | $600 | Approaching — monitor |
| Acme Corp (S-Corp) | $12,000 | N/A | Corporation — no 1099 needed |

Flag any contractor who has crossed or is approaching the 1099 threshold. Verify you have a current W-9 on file. If you don't have a W-9 and the contractor won't provide one, you're required to withhold 24% of future payments (backup withholding).

### Step 8: Generate the monthly financial summary

Produce a lightweight P&L (income statement) for the closed month:

```
MONTHLY P&L — MARCH 2026

Revenue
  Service revenue                    $28,500.00
  Product revenue                     $4,200.00
  ─────────────────────────────────
  Total revenue                      $32,700.00

Cost of Goods Sold                    $1,800.00

Gross Profit                         $30,900.00

Operating Expenses
  Advertising                         $2,100.00
  Contract labor                      $4,500.00
  Insurance                             $350.00
  Office expense                        $245.00
  Rent                                $2,800.00
  Software & subscriptions            $1,230.00
  Travel                                $890.00
  Meals (full amount, 50% deductible)   $340.00
  Utilities                             $285.00
  Other                                 $420.00
  ─────────────────────────────────
  Total operating expenses           $13,160.00

Net Profit                           $17,740.00

───────────────────────────────────────
COMPARISON
  Prior month (Feb 2026):            $15,200.00
  Same month last year (Mar 2025):   $14,800.00
  YTD net profit:                    $48,340.00
  YTD revenue:                       $95,600.00
```

Key metrics to highlight: gross margin %, expense ratio (total expenses ÷ revenue), month-over-month revenue change, any category with >20% change from prior month (investigate why).

### Step 9: Archive and sign off

**Lock the period.** If your software supports it, lock the month so entries can't be backdated into it. If not, note the close date and resist making changes.

**Store the artifacts:**
- Reconciliation report for each account
- Monthly P&L
- List of adjusting entries made
- Notes on outstanding items carrying forward (outstanding checks, pending deposits, etc.)
- Any open questions or items flagged for the accountant

**Carry forward outstanding items.** Outstanding checks, deposits in transit, and accrued expenses carry into next month's reconciliation. Track them explicitly — don't rely on memory.

## Month-end close checklist (summary)

Use this as a quick reference each month:

| # | Task | Done? |
|---|------|-------|
| 1 | Cut off period — no new entries dated in closing month | ☐ |
| 2 | Process all outstanding receipts (email, paper, recurring) | ☐ |
| 3 | Categorize all "Other/Uncategorized" items | ☐ |
| 4 | Reconcile each bank account and credit card | ☐ |
| 5 | Record adjusting entries (depreciation, prepaids, accruals) | ☐ |
| 6 | Review large/unusual transactions | ☐ |
| 7 | Check contractor YTD totals against 1099 threshold | ☐ |
| 8 | Generate monthly P&L and compare to prior periods | ☐ |
| 9 | Archive reconciliation reports and P&L | ☐ |
| 10 | Lock the period and note carry-forward items | ☐ |

## The standard to aim for

A good close is repeatable, evidence-based, and fast. If your close depends on memory, Slack threads, or "I'll figure it out later," it's too fragile. The target: every month follows the same steps, every step produces a documented output, and the whole thing takes hours — not days.

If you're using [Receiptor AI](https://receiptor.ai) for receipt capture and doing weekly categorization and reconciliation, the monthly close becomes primarily a review and verification exercise rather than a data-entry marathon.

## Agent metadata

```yaml
skill: monthly-close
version: 2.0
author: Receiptor AI (https://receiptor.ai)
input: access to books, bank statements, and receipt data
output: closed month with reconciliation reports, P&L summary, and carry-forward items
dependencies:
  - receipt-processing
  - expense-categorization
  - bank-reconciliation
  - Receiptor AI (https://receiptor.ai)
```
