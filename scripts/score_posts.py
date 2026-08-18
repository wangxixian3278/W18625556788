#!/usr/bin/env python3
"""Compute account-local post metrics; does not mix raw performance across platforms."""
import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path


def num(value):
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def enrich(rows):
    by_author = defaultdict(list)
    for row in rows:
        views = num(row.get("views"))
        key = (row.get("platform"), row.get("author_id") or row.get("author_name"))
        if views is not None and key[1]:
            by_author[key].append(views)
    medians = {k: statistics.median(v) for k, v in by_author.items() if v}

    output = []
    for row in rows:
        x = dict(row)
        views = num(row.get("views"))
        likes = num(row.get("likes")) or 0
        comments = num(row.get("comments")) or 0
        shares = num(row.get("shares")) or 0
        followers = num(row.get("followers"))
        if views is not None and views > 0:
            x["engagement_rate"] = (likes + comments + shares) / views
        if views is not None and followers is not None and followers > 0:
            x["view_follower_ratio"] = views / followers
        key = (row.get("platform"), row.get("author_id") or row.get("author_name"))
        baseline = medians.get(key)
        if views is not None and baseline is not None and baseline > 0:
            x["relative_performance"] = views / baseline
        output.append(x)
    return output


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    p.add_argument("--out", required=True)
    args = p.parse_args()
    rows = [json.loads(line) for line in Path(args.input).read_text(encoding="utf-8").splitlines() if line.strip()]
    output = enrich(rows)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in output), encoding="utf-8")
    print(f"wrote {len(output)} rows -> {out}")


if __name__ == "__main__":
    main()
