# United States Jurisdiction Pack

## Scope

This pack covers US small-business bookkeeping support, especially expense-side workflows for sole proprietors, freelancers, single-member LLCs, and small service businesses.

It is the current baseline jurisdiction for this repository.

It does not replace a CPA, enrolled agent, payroll provider, attorney, or tax filing product. It should guide draft bookkeeping outputs, exception queues, and accountant-ready packages.

## When to load

Load this file before applying US-specific rules such as:

- Schedule C expense mapping
- Form 1099-NEC contractor tracking
- Form W-9 collection
- Form 1040-ES estimated tax planning
- home office deduction rules
- standard mileage vs actual vehicle expense rules
- business meals and entertainment rules
- depreciation, Section 179, bonus depreciation, and MACRS

## Core bookkeeping context

Capture these fields in `bookkeeping-setup` before applying US tax treatment:

- entity type: sole proprietor, single-member LLC, partnership, S corporation, C corporation, nonprofit, or unknown
- tax filing context: Schedule C, partnership return, corporate return, or unknown
- accounting method: cash, accrual, hybrid, or unknown
- home currency: usually USD
- state and local tax footprint
- sales tax registration status, if selling taxable goods or services
- payroll provider, if employees exist
- contractor payment process and W-9 status

If entity type or filing context is unknown, draft bookkeeping records but flag entity-specific tax treatment for professional review.

## Chart-of-accounts implications

For US sole proprietors and simple small businesses, map ordinary expenses to Schedule C lines where useful. Do not force all businesses into Schedule C if the entity or return type differs.

Common mappings:

| Area | US bookkeeping implication |
|---|---|
| Advertising | Schedule C Line 8 for sole proprietors |
| Car and truck | Track standard mileage vs actual expenses; support Form 4562 when needed |
| Contract labor | Track vendors, W-9 status, payment method, and 1099 exposure |
| Depreciation | Track asset basis, placed-in-service date, business-use percentage, method, and accumulated depreciation |
| Meals | Record full book expense, track deductible percentage separately |
| Travel | Separate travel from meals and entertainment |
| Home office | Keep simplified vs actual method evidence separate |
| Owner transactions | Separate owner draws, owner contributions, reimbursements, and personal expenses from business expenses |

## Current-law policy

US tax amounts and thresholds change. Before finalizing a tax-sensitive recommendation, verify year-specific facts against primary sources such as IRS publications, forms, instructions, or notices.

Tax-sensitive facts include:

- standard mileage rates
- Section 179 limits
- bonus depreciation percentage
- 1099 thresholds and e-filing thresholds
- penalty amounts
- tax brackets, Social Security wage base, and estimated-tax safe-harbor thresholds
- meals, entertainment, and employer-provided meal deductibility
- state and local sales tax or payroll requirements

If current-law verification is unavailable, label the output as draft and include the year assumed.

## Agent boundaries

Safe to draft:

- extracted receipt and invoice records
- categorized transaction tables
- Schedule C mapping suggestions
- reconciliation reports
- contractor 1099 exposure summaries
- estimated-tax worksheets
- monthly close packages
- tax-prep packets for accountant review

Requires user approval:

- posting entries to accounting software
- deleting or merging records
- locking periods
- applying manual overrides to amounts, dates, vendors, or categories
- submitting information returns or tax payments

Requires professional review:

- entity classification uncertainty
- worker classification uncertainty
- multi-state sales tax or payroll exposure
- inventory and COGS treatment
- depreciation elections
- large owner transactions
- amended returns or prior-year corrections
- any final tax filing position

## Related skills

- `bookkeeping-setup`
- `schedule-c-categories`
- `contractor-1099`
- `estimated-taxes`
- `home-office`
- `vehicle-expenses`
- `meals-deduction`
- `depreciation-assets`
