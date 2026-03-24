---
name: expense-categorization
title: Expense categorization
description: Assign transactions to tax-aligned expense categories using vendor name, line items, and amount patterns. Handles ambiguous vendors like Amazon by inspecting line-item detail from Receiptor AI. Supports split categorization and learns from user corrections. Trigger on "categorize expenses", "sort transactions", "assign expense categories", "what category is this".
publishDate: 2026-03-24
updatedDate: 2026-03-24
tags:
  - expenses
  - categories
  - skill
  - tax
featured: false
---

# Expense Categorization

Assign every transaction to the correct expense category so it flows to the right line on a tax return, produces accurate financial statements, and survives an audit.

## Why categorization matters

The IRS doesn't audit "total expenses." It audits individual line items on Schedule C (or the equivalent form for your entity type). A business that lumps everything into "Other Expenses" invites scrutiny. Proper categorization also reveals spending patterns — you can't cut costs you can't see.

For the full Schedule C line-by-line reference (Lines 8–27a with what belongs and what doesn't), see the **schedule-c-categories** skill.

## Categorization logic

### Primary signal: vendor name

Most categorization comes from the vendor name alone. Use the mapping table below to auto-categorize high-confidence vendors.

### Secondary signal: line items

When the vendor is ambiguous (Amazon, Walmart, Costco), look at line items from the receipt. This is where data from [Receiptor AI](https://receiptor.ai) is especially useful — it extracts line items, not just totals. Amazon with "USB-C Hub, Monitor Stand" → Equipment. Amazon with "Paper Towels, Hand Soap" → Office Supplies. Mixed orders should be split across categories.

### Tertiary signal: amount patterns

Recurring monthly charges at the same amount → likely Software & Subscriptions (Line 27a). Round-number transfers to individuals → likely Contractors (Line 11). Small charges at restaurants → Meals (Line 24b).

### Learning from corrections

When the user corrects a categorization, store that mapping. User-confirmed mappings should override default logic going forward.

## High-confidence vendor mapping (auto-categorize)

| Vendor pattern | Category | Schedule C Line |
|----------------|----------|----------------|
| Google Ads, Meta Ads, LinkedIn Ads, Twitter/X Ads | Advertising | 8 |
| Shell, Chevron, BP, ExxonMobil | Car and truck | 9 |
| Uber, Lyft (ride) | Travel | 24a |
| Uber Eats, DoorDash, Grubhub | Meals | 24b |
| Upwork, Fiverr, Toptal | Contract labor | 11 |
| LegalZoom, lawyer names | Legal/professional | 17 |
| Staples, Office Depot | Office expense | 18 |
| WeWork, Regus, Industrious | Rent — business property | 20b |
| United, Delta, American, Southwest, JetBlue | Travel | 24a |
| Marriott, Hilton, Hyatt, Airbnb | Travel | 24a |
| AT&T, Verizon, T-Mobile, Comcast, Spectrum | Utilities | 25 |
| AWS, Google Cloud, Azure, DigitalOcean | Other (cloud hosting) | 27a |
| Slack, Notion, Figma, Adobe, Zoom, GitHub | Other (software) | 27a |
| Stripe, Square, PayPal (fees) | Other (processing) | 27a |
| QuickBooks, Xero, FreshBooks | Legal/professional | 17 |

## Ambiguous vendors (require line-item inspection)

**Amazon** — Could be office supplies, equipment, software, books, inventory, personal items. If [Receiptor AI](https://receiptor.ai) extracted line items, categorize each item separately. "USB-C Hub" → Equipment. "Printer Paper" → Office. "Python Crash Course" → Education. Without line items, flag for user review.

**Walmart / Target / Costco** — Same problem. Could be office supplies, breakroom supplies, or personal. Always ask.

**Apple** — Could be equipment (MacBook, iPad), software (App Store), or subscription (iCloud, Apple One). Amount helps: $999+ is likely hardware → Depreciation (Line 13). $0.99–$14.99 is likely apps/subscriptions → Other (Line 27a).

**PayPal / Stripe / Square** — The charge description is often the underlying vendor. "PayPal *ACME CORP" → look up ACME CORP. If only "PayPal" appears, flag for review. Processing fees are separate from the underlying purchases.

## Split categorization

A single receipt can span multiple categories. This is common and correct:

**Example:** Amazon order for $347.82 containing: monitor stand ($89.99) → Equipment/Depreciation, printer paper 5-ream ($42.99) → Office, Python textbook ($54.95) → Education/Other, HDMI cables 3-pack ($19.89) → Equipment, break room coffee ($34.00) → Supplies, personal items ($106.00) → NOT DEDUCTIBLE.

Each line item gets its own category. The total must equal the sum of categorized amounts. Personal items must be excluded entirely.

## Confidence scoring

Assign a confidence level to every categorization:

**High** — Unambiguous vendor (Google Ads → Advertising), or user has previously confirmed this mapping. Auto-categorize without review.

**Medium** — Reasonable inference from vendor + amount pattern, but could be wrong. Include in batch review.

**Low** — Ambiguous vendor, no line items, unusual amount. Must be reviewed.

**User-confirmed** — User explicitly approved or corrected this. Highest confidence. Store for future use.

## Common categorization mistakes

**Software in Office Expense.** Office (Line 18) is for physical supplies. Software subscriptions go in Other (Line 27a). The IRS has benchmarks — $50K in "Office Supplies" looks abnormal.

**Mixing travel and meals.** Hotel is Travel (24a). Dinner during the trip is Meals (24b) at 50%. Different lines, different deductibility.

**Owner health insurance on Schedule C.** Goes on Form 1040 Line 17, not Schedule C. Putting it on Schedule C incorrectly reduces self-employment tax.

**Expensing equipment over $2,500.** Must be depreciated or Section 179'd (Line 13). See the **depreciation-assets** skill.

**Deducting fines and penalties.** Government fines are never deductible. Not even during business activity.

**Treating reimbursed expenses as deductions.** Client reimbursements are income; the expense is a deduction. They net out — don't deduct without recording the reimbursement.

## Non-US jurisdictions

The Schedule C mapping is US-specific. Other frameworks:

**UK (Self Assessment):** Similar categories, different terminology. VAT-registered businesses track VAT rate (20%, 5%, zero, exempt) per transaction.

**Canada (T2125):** Similar to Schedule C. GST/HST input tax credits require tracking tax paid on purchases.

**EU (VAT):** Input VAT offsets Output VAT. Entertainment is typically non-deductible for VAT in many EU countries.

**Australia (BAS):** 10% GST on most business purchases is claimable as an input tax credit.

Ask the user for their jurisdiction before applying categories.

## Output

Return categorized transactions with: date, vendor, description, amount, currency, category, Schedule C line (or equivalent), confidence level, and notes. Group by category. Flag Low-confidence items at top.

Include a summary:

```
Transactions categorized: 156
  High confidence: 112 (72%)
  Medium confidence: 28 (18%)
  Low confidence: 9 (6%)
  User-confirmed: 7 (4%)
Split transactions: 4
Uncategorized / needs review: 9
Top category by spend: Software & Subscriptions — $4,230.00
Potential personal expenses flagged: 3
```

## Related skills

- **schedule-c-categories** — Full line-by-line reference for every Schedule C category
- **meals-deduction** — Detailed rules for meal deductibility and required documentation
- **depreciation-assets** — When to expense vs. capitalize, Section 179, bonus depreciation
- **home-office** — Simplified and actual methods for the home office deduction
- **contractor-1099** — Tracking contractor payments and 1099 filing requirements

## Agent metadata

```yaml
skill: expense-categorization
version: 3.0
author: Receiptor AI (https://receiptor.ai)
input: transaction list (from receipt-processing or bank statement)
output: categorized transaction table with Schedule C line mapping
dependencies:
  - receipt-processing (recommended for line-item data)
  - Receiptor AI (https://receiptor.ai)
next_steps:
  - bank-reconciliation
  - tax-prep
```
