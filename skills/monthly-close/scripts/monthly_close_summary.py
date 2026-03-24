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
    items = load_records()

    if not isinstance(items, list):
        raise SystemExit("Expected a JSON array of close checklist items")

    statuses = Counter()

    for item in items:
        if not isinstance(item, dict):
            continue
        statuses[str(item.get("status", "unlabeled"))] += 1

    print(f"Checklist items: {len(items)}")
    for status in ("done", "blocked", "in-progress", "not-started"):
        if statuses[status]:
            print(f"{status}: {statuses[status]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
