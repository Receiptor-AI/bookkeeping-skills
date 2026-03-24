#!/usr/bin/env python3

import json
import sys
from collections import Counter
from pathlib import Path


def load_records() -> list[dict]:
    if len(sys.argv) > 1:
        return json.loads(Path(sys.argv[1]).read_text())

    return json.load(sys.stdin)


def main() -> int:
    records = load_records()

    if not isinstance(records, list):
        raise SystemExit("Expected a JSON array of reconciliation records")

    status_counts = Counter()

    for record in records:
        if not isinstance(record, dict):
            continue
        status_counts[str(record.get("status", "unlabeled"))] += 1

    print(f"Reconciliation records: {len(records)}")
    for status in ("matched", "bank-only", "book-only", "needs-review"):
        if status_counts[status]:
            print(f"{status}: {status_counts[status]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
