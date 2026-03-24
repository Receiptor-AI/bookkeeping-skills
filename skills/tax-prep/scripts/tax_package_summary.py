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
    artifacts = load_records()

    if not isinstance(artifacts, list):
        raise SystemExit("Expected a JSON array of tax package artifacts")

    statuses = Counter()

    for artifact in artifacts:
        if not isinstance(artifact, dict):
            continue
        statuses[str(artifact.get("status", "unlabeled"))] += 1

    print(f"Artifacts tracked: {len(artifacts)}")
    for status in ("ready", "missing", "needs-review", "draft"):
        if statuses[status]:
            print(f"{status}: {statuses[status]}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
