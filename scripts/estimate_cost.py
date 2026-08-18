#!/usr/bin/env python3
"""Rough request-cost planner. Endpoint/account pricing remains authoritative."""
import argparse


def estimate(requests: int, low: float = 0.001, high: float = 0.01):
    if requests < 0:
        raise ValueError("requests must be >= 0")
    if low < 0 or high < 0 or low > high:
        raise ValueError("invalid price range")
    return requests * low, requests * high


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--requests", type=int, required=True)
    p.add_argument("--low", type=float, default=0.001)
    p.add_argument("--high", type=float, default=0.01)
    args = p.parse_args()
    lo, hi = estimate(args.requests, args.low, args.high)
    print(f"requests: {args.requests}")
    print(f"rough planning range: ${lo:.4f} - ${hi:.4f}")
    print("Actual current endpoint/account pricing is authoritative.")


if __name__ == "__main__":
    main()
