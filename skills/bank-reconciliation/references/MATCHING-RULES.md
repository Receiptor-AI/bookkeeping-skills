# Bank Reconciliation Matching Rules

Use this file when choosing what the agent can match automatically and what needs review.

## Safe auto-match tiers

- exact amount and exact date
- exact amount with date within 2 business days
- explicit shared reference number

## Review-required tiers

- fuzzy matches with date drift beyond 2 business days
- batch matches where multiple entries sum to one transaction
- near-equal amounts that depend on fees, FX, or rounding assumptions
- possible duplicates or sign reversals

## Never auto-resolve without approval

- deleting a book entry
- reclassifying owner draws, payroll, loan activity, or tax payments
- forcing a match only to make the balance reconcile
- changing historical entries in a closed period
