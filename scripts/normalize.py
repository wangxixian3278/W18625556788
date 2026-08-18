#!/usr/bin/env python3
"""Map platform-specific JSON records to a cross-platform post/comment schema."""
import argparse
import json
from pathlib import Path

POST_FIELDS = [
    "platform", "post_id", "url", "author_id", "author_name", "text",
    "published_at", "views", "likes", "comments", "shares", "saves",
    "followers", "duration_sec", "raw_source"
]


def dig(obj, dotted):
    cur = obj
    for part in dotted.split("."):
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return None
        elif isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
        if cur is None:
            return None
    return cur


def map_record(raw, mapping, constants=None, fields=None):
    constants = constants or {}
    fields = fields or POST_FIELDS
    out = {}
    for field in fields:
        if field in constants:
            out[field] = constants[field]
        elif field in mapping:
            out[field] = dig(raw, mapping[field])
        else:
            out[field] = None
    return out


def load_rows(path: Path):
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        return json.loads(text)
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--mapping", required=True, help="JSON file: normalized_field -> dotted source path")
    p.add_argument("--constants", default="{}")
    p.add_argument("--out", required=True)
    args = p.parse_args()

    rows = load_rows(Path(args.input))
    mapping = json.loads(Path(args.mapping).read_text(encoding="utf-8"))
    constants = json.loads(args.constants)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        for raw in rows:
            f.write(json.dumps(map_record(raw, mapping, constants), ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} rows -> {out_path}")


if __name__ == "__main__":
    main()
