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
        raise SystemExit("Expected a JSON array of categorized transactions")

    confidence_counts = Counter()
    review_counts = Counter()
    category_counts = Counter()

    for record in records:
        if not isinstance(record, dict):
            continue
        confidence_counts[str(record.get("confidence", "unknown"))] += 1
        review_counts[str(record.get("review_status", "unlabeled"))] += 1
        category_counts[str(record.get("category", "uncategorized"))] += 1

    print(f"Transactions categorized: {len(records)}")
    print("Confidence:")
    for key, value in sorted(confidence_counts.items()):
        print(f"  {key}: {value}")
    print("Review status:")
    for key, value in sorted(review_counts.items()):
        print(f"  {key}: {value}")
    print("Top categories:")
    for key, value in category_counts.most_common(10):
        print(f"  {key}: {value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
