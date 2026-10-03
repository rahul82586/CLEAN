#!/usr/bin/env python3
"""
Find TRUE record size using autocorrelation of byte values.

Method: treat body bytes as a 1-D signal. The record size = the lag that
maximises self-correlation. We compute autocorrelation for lags 32..2048 and
plot the top peaks. A genuine record boundary produces a sharp, isolated peak.
"""
import os, struct
from pathlib import Path

BASE = Path("/workspace/mt5-analysis/bases")
HEADER = 76

def autocorr_at_lag(data, lag):
    """Pearson correlation between data[i] and data[i+lag]."""
    n = len(data) - lag
    if n <= 0: return 0.0
    # subsample for speed: take 200k points
    step = max(1, n // 200000)
    a = []
    b = []
    for i in range(0, n, step):
        a.append(data[i])
        b.append(data[i + lag])
    if len(a) < 100: return 0.0
    ma = sum(a) / len(a)
    mb = sum(b) / len(b)
    num = sum((a[i]-ma)*(b[i]-mb) for i in range(len(a)))
    da = math.sqrt(sum((x-ma)**2 for x in a))
    db = math.sqrt(sum((x-mb)**2 for x in b))
    if da == 0 or db == 0: return 0.0
    return num / (da * db * len(a))

import math

def find_record_size(path, label, max_lag=2048):
    with open(path, 'rb') as f:
        data = f.read()
    body = data[HEADER:]
    body_size = len(body)
    print(f"\n{'='*70}")
    print(f"  {label}  body_size={body_size:,}")
    print(f"{'='*70}")

    # Quick candidate screen: sizes that divide body exactly
    candidates = []
    for rs in [32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128,
               144, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, 480,
               512, 576, 640, 672, 704, 768, 832, 896, 960, 1024, 1152, 1280,
               1408, 1536, 1664, 1792, 1920, 2048]:
        rem = body_size % rs
        candidates.append((rs, rem, body_size // rs))

    exact = [c for c in candidates if c[1] == 0]
    print("  Exact-divisor record-size candidates (size, records):")
    if exact:
        for rs, _, n in sorted(exact, key=lambda x: -n)[:15]:
            print(f"    {rs:5d}  →  {n:>8,} records")
    else:
        print("    (none in the candidate set)")

    # Autocorrelation scan for the most promising lag range
    # Skip lags that aren't plausible (must be multiple of small power of 2)
    print("  Top autocorrelation lags (signal of periodicity):")
    scores = []
    for lag in range(32, max_lag + 1, 4):
        # restrict to powers of 2 multiples
        if lag not in [32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128,
                       144, 160, 176, 192, 208, 224, 240, 256, 288, 320, 352,
                       384, 416, 448, 480, 512, 544, 576, 608, 640, 672, 704,
                       768, 832, 896, 960, 1024, 1152, 1280, 1408, 1536, 1664,
                       1792, 1920, 2048]:
            continue
        scores.append((lag, autocorr_at_lag(body, lag)))
    scores.sort(key=lambda x: -x[1])
    for lag, sc in scores[:10]:
        marker = "  <-- candidate" if sc > 0.05 else ""
        rem = body_size % lag
        print(f"    lag={lag:5d}  corr={sc:+.4f}  body%lag={rem}{marker}")

    return scores[:5]

# analyze the main data files
for fname in ["liveupdate.dat", "kyc.dat", "orders.dat", "positions.dat",
              "users.dat", "deals_2022.03.dat"]:
    p = BASE / fname
    if p.exists():
        find_record_size(str(p), fname)
