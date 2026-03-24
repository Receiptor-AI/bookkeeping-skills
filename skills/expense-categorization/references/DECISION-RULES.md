# Expense Categorization Decision Rules

Use this file when deciding whether a category can be assigned automatically or requires review.

## Auto-assign only when

- the vendor is a known high-confidence match
- line items clearly support the category
- the amount pattern is consistent with prior approved transactions
- the transaction is not mixed personal/business

## Send to review when

- the vendor is ambiguous, such as Amazon, Walmart, Costco, Apple, PayPal, or Stripe
- line items are missing and vendor alone is not decisive
- the transaction may need to be split across categories
- the treatment could affect depreciation, meals, vehicle, home office, or contractor reporting
- the transaction looks personal, owner-related, reimbursable, or tax-sensitive

## Approval boundary

Do not finalize a category without review if:

- confidence is low
- multiple plausible categories exist
- the category would materially affect taxes or owner equity
- the user has historically overridden similar transactions
