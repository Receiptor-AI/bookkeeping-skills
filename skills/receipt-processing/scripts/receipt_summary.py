#!/usr/bin/env python3

import json
import sys
from collections import Counter
from pathlib import Path


REQUIRED_FIELDS = ("vendor_name", "date", "total_amount", "currency")


def load_records() -> list[dict]:
    if len(sys.argv) > 1:
        return json.loads(Path(sys.argv[1]).read_text())

    return json.load(sys.stdin)


def classify(record: dict) -> str:
    missing = [field for field in REQUIRED_FIELDS if not record.get(field)]

    if missing:
        return "needs-review"

    if record.get("review_status"):
        return str(record["review_status"])

    return "ready"


def main() -> int:
    records = load_records()

    if not isinstance(records, list):
        raise SystemExit("Expected a JSON array of receipt records")

    statuses = Counter(classify(record) for record in records if isinstance(record, dict))
    source_types = Counter(
        str(record.get("source_type", "unknown")) for record in records if isinstance(record, dict)
    )

    print(f"Receipts processed: {len(records)}")

    for status in ("ready", "needs-review", "duplicate-suspect", "missing-fields"):
        if statuses[status]:
            print(f"{status}: {statuses[status]}")

    if source_types:
        print("Sources:")
        for source_type, count in sorted(source_types.items()):
            print(f"  {source_type}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
