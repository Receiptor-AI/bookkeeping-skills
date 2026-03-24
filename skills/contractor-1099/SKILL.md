---
name: contractor-1099
title: 1099 contractor management
description: Track independent contractor payments, collect W-9s, determine 1099-NEC filing requirements, and avoid penalties. Covers the $600 threshold (2025) and $2,000 threshold (2026), Jan 31 deadline, corporate exceptions, backup withholding, and penalty schedule ($60–$660/form). Trigger on "1099", "contractor payment", "do I need to file a 1099", "W-9", "independent contractor".
publishDate: 2026-03-24
updatedDate: 2026-03-24
tags:
  - tax
  - 1099
  - contractors
featured: false
---

# 1099 Contractor Management

Track payments to independent contractors, determine who needs a 1099-NEC, collect W-9s, and file on time to avoid penalties.

## When do you need to file a 1099-NEC?

File a 1099-NEC for each person or non-corporate entity to whom you paid **$600 or more** during the calendar year for services performed in the course of your trade or business.

**Threshold change for 2026:** Starting with tax year 2026, the reporting threshold increases from $600 to **$2,000**. This means fewer 1099s to file, but you should still track all contractor payments — the threshold could change again.

## Who needs a 1099-NEC?

| Payee type | 1099-NEC required? | Notes |
|-----------|-------------------|-------|
| Individual (sole proprietor, freelancer) | **Yes** if ≥$600 | Most common scenario |
| Single-member LLC (disregarded entity) | **Yes** if ≥$600 | Treated as individual for tax purposes |
| Partnership / Multi-member LLC | **Yes** if ≥$600 | |
| S-Corporation | **Generally no** | **Exception:** payments for legal services and medical/health care services always require a 1099 regardless of entity type |
| C-Corporation | **Generally no** | Same exceptions as S-Corp: legal and medical services |
| Payments via credit/debit card or third-party networks | **No** | The payment processor (Stripe, PayPal, Venmo, Square) reports these on **1099-K** instead. You don't double-report. |
| Employees | **No** | They get a W-2, not a 1099 |
| Rent paid to real estate agents | **No (1099-NEC)** | Gets 1099-MISC instead |
| Payments for merchandise/inventory | **No** | 1099-NEC is for services, not goods |

## The W-9: Get it before you pay

**Form W-9** (Request for Taxpayer Identification Number) collects the information you need to file a 1099. Collect it from every contractor **before making the first payment.** This is critical — chasing down W-9s in January when you're trying to file is miserable.

**What the W-9 provides:** Legal name, business name (if different), federal tax classification (individual, LLC, corporation, etc.), address, and TIN (Taxpayer Identification Number — either SSN or EIN).

**If a contractor refuses to provide a W-9:** You are required to begin **backup withholding** at **24%** of all future payments to that contractor. You must remit the withheld amount to the IRS using Form 945. This is not optional — failing to withhold when required makes you liable for the tax.

**Best practice:** Make W-9 collection part of your contractor onboarding process. No W-9, no first payment. Store W-9s securely — they contain SSNs.

## Tracking payments throughout the year

Don't wait until January to figure out who needs a 1099. Track continuously:

| Contractor | Entity type | TIN on file? | Payment method | Q1 | Q2 | Q3 | Q4 | YTD total | 1099 required? |
|-----------|------------|-------------|---------------|-----|-----|-----|-----|-----------|---------------|
| Jane Smith Design | Individual | SSN ✓ | ACH | $2,100 | $2,100 | $2,100 | $2,100 | $8,400 | Yes |
| Acme Dev LLC | LLC (single-member) | EIN ✓ | Check | $6,000 | $6,000 | $6,000 | $6,000 | $24,000 | Yes |
| CloudFlare Inc | C-Corp | EIN ✓ | Credit card | $300 | $300 | $300 | $300 | $1,200 | No (corp + card) |
| Bob's Plumbing | Individual | None ❌ | Check | $0 | $0 | $800 | $0 | $800 | Yes (get W-9!) |
| Legal Eagle LLP | Partnership | EIN ✓ | ACH | $0 | $5,000 | $0 | $0 | $5,000 | Yes |

**Monthly check:** During your monthly close, review contractor YTD totals. Flag anyone who has crossed or is approaching the threshold. Verify W-9s are on file for everyone above threshold.

[Receiptor AI](https://receiptor.ai) extracts contractor invoices from email automatically, making it easy to maintain accurate YTD totals throughout the year instead of scrambling in January.

## Filing deadline and forms

**Deadline:** **January 31** of the year following payment. Both the contractor's copy AND the IRS filing are due on January 31. There is **no extension** for 1099-NEC (unlike 1099-MISC, which has a March deadline for the IRS copy).

**What you file:**
- **Copy A** — to the IRS (electronically via FIRE system, or paper with Form 1096 transmittal)
- **Copy B** — to the contractor
- **Copy C** — for your records

**Electronic filing requirement:** If you're filing 10 or more information returns (any combination of 1099s, W-2s, etc.), you must file electronically. The threshold was 250 until 2024, when it dropped to 10.

**How to file:** Use the IRS FIRE (Filing Information Returns Electronically) system, or use a service like Tax1099.com, Track1099, QuickBooks, or Gusto that handles the filing for you. Paper filing with Form 1096 is still allowed if filing fewer than 10 total information returns.

## Penalties for late or incorrect filing

| When you file | Penalty per form |
|---|---|
| Within 30 days of deadline (by March 2) | **$60** |
| By August 1 | **$130** |
| After August 1 or not at all | **$330** |
| **Intentional disregard** (you knew and didn't file) | **$660** per form, **no maximum cap** |

**Annual maximums (for small businesses with gross receipts ≤$5 million):** $232,500 for the 30-day tier, $664,500 for the August tier, $1,328,500 for the "after August" tier. Intentional disregard has no maximum.

These penalties apply **per form** — if you have 20 contractors and miss all of them, multiply accordingly. The penalties also apply to incorrect forms (wrong TIN, wrong amount, wrong name).

## Correcting 1099s

If you discover an error after filing, file a corrected 1099-NEC:

**Type 1 correction:** Wrong amount, wrong code, or wrong checkbox. File a new 1099-NEC with the "CORRECTED" box checked and the correct information.

**Type 2 correction:** Wrong payee name or TIN. This requires two forms: one to zero out the incorrect payee, and one with the correct payee information.

File corrections as soon as you discover the error. If you correct before the IRS notices, you generally avoid penalties.

## Worker classification: Employee vs. contractor

This is the most dangerous area of 1099 compliance. If you classify a worker as a contractor when they should be an employee, you face:

- Back employment taxes (employer's share of FICA: 7.65% of all payments)
- Penalties for failure to withhold income tax
- Penalties for failure to file W-2s
- Interest on all of the above
- Potential state-level penalties (many states are even more aggressive than the IRS)

**Key factors the IRS considers (common law test):**

**Behavioral control:** Do you control how the work is done, or just the result? Contractors control their own methods. If you dictate hours, tools, processes, and work location, that looks like an employee.

**Financial control:** Does the worker have unreimbursed business expenses? Do they invest in their own tools/equipment? Can they profit or lose money? Do they offer services to the general public? Contractors typically say yes to all of these.

**Relationship:** Is there a written contract? Are there employee-type benefits (insurance, retirement, PTO)? Is the relationship permanent or project-based? Is the work a key part of your regular business? Employee indicators: ongoing relationship, benefits, work is core to the business.

**When in doubt:** File Form SS-8 with the IRS to request a worker classification determination. Or consult an employment attorney. The cost of getting it wrong vastly exceeds the cost of getting professional advice.

## Year-end checklist

By December 15:
- [ ] Review all contractor YTD totals
- [ ] Verify W-9 is on file for every contractor above threshold
- [ ] Request W-9s from any contractor without one
- [ ] Verify TINs match contractor names (consider TIN matching via IRS e-Services)

By January 31:
- [ ] Generate 1099-NEC forms for all qualifying contractors
- [ ] Mail or electronically deliver Copy B to each contractor
- [ ] File Copy A with the IRS (electronically if ≥10 forms)
- [ ] Retain Copy C for your records

After filing:
- [ ] Monitor for any IRS notices about mismatches
- [ ] File corrections promptly if errors are discovered
