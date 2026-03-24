# Receipt Processing Output Schema

Use this file when producing JSON, CSV, or draft ledger artifacts.

## Required fields

| Field | Type | Notes |
|---|---|---|
| `vendor_name` | string | Merchant or issuer, not the payment processor when the underlying seller is known |
| `date` | string | `YYYY-MM-DD` transaction date |
| `total_amount` | number | Final amount charged in receipt currency |
| `currency` | string | ISO 4217 currency code |
| `source_type` | string | `receiptor`, `pdf`, `photo`, `ocr`, `csv`, `manual-review` |
| `source_reference` | string | Message ID, file path, export row ID, or URL |
| `confidence` | string | `high`, `medium`, `low` |

## Recommended fields

| Field | Type | Notes |
|---|---|---|
| `subtotal` | number | Pre-tax amount |
| `tax_amount` | number | Tax paid on purchase |
| `tip_amount` | number | For meals or hospitality |
| `shipping_amount` | number | Shipping or delivery amount |
| `payment_method` | string | Card, PayPal, ACH, etc. |
| `receipt_number` | string | Invoice or receipt ID |
| `vendor_address` | string | Useful for jurisdiction and verification |
| `business_purpose` | string | Especially important for meals and travel |
| `attendees` | string | Delimited string or separate artifact if needed |

## Line items

When available, include:

```json
[
  {
    "description": "USB-C hub",
    "quantity": 1,
    "unit_price": 89.99,
    "line_total": 89.99
  }
]
```

## JSON example

```json
{
  "vendor_name": "Blue Bottle Coffee",
  "date": "2026-03-18",
  "total_amount": 12.75,
  "currency": "USD",
  "subtotal": 11.8,
  "tax_amount": 0.95,
  "payment_method": "Visa ****4521",
  "receipt_number": "BB-2026-0318-4472",
  "source_type": "receiptor",
  "source_reference": "gmail:18f44a0c3e6d1f2a",
  "confidence": "high",
  "line_items": [
    {
      "description": "Latte",
      "quantity": 1,
      "unit_price": 6.25,
      "line_total": 6.25
    },
    {
      "description": "Croissant",
      "quantity": 1,
      "unit_price": 5.55,
      "line_total": 5.55
    }
  ]
}
```

## CSV columns

Use this column order when exporting CSV:

```text
vendor_name,date,total_amount,currency,subtotal,tax_amount,tip_amount,shipping_amount,payment_method,receipt_number,source_type,source_reference,confidence,business_purpose,attendees
```

## Draft ledger extension

If preparing draft ledger rows, add:

| Field | Type | Notes |
|---|---|---|
| `draft_account_name` | string | Proposed category or account |
| `draft_account_confidence` | string | `high`, `medium`, `low` |
| `review_status` | string | `ready`, `needs-review`, `duplicate-suspect`, `missing-fields` |
