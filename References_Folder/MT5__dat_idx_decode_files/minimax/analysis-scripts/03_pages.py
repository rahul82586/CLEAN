#!/usr/bin/env python3
"""
MT5 .dat body is NOT fixed-size records. Hypothesis: it's a page-based storage
with a 4-byte page-header at the start of each page.

Common MT5 page sizes: 1024, 2048, 4096, 8192, 16384, 32768, 65536.

Method: for each candidate page size, check if every (page_start + 0..3) dword
matches a known pattern. Or: check the byte that would be the record-marker.
"""
import os, struct
from collections import Counter

BASE = "/workspace/mt5-analysis/bases"
HEADER = 76

def page_signature(path, label, page_size):
    size = os.path.getsize(path)
    with open(path, 'rb') as f:
        data = f.read()
    body = data[HEADER:]
    body_size = len(body)
    if body_size < page_size:
        return
    n_pages = body_size // page_size
    rem = body_size % page_size
    # take first dword of each page
    page_starts = []
    for i in range(min(n_pages, 50)):
        page_starts.append(struct.unpack('<I', body[i*page_size:i*page_size+4])[0])
    counter = Counter(page_starts)
    return n_pages, rem, page_starts, counter

for fname in ["orders.dat", "positions.dat", "users.dat", "deals_2022.03.dat",
              "liveupdate.dat", "kyc.dat"]:
    p = os.path.join(BASE, fname)
    print(f"\n=== {fname} ===")
    for ps in [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]:
        r = page_signature(p, fname, ps)
        if not r: continue
        n_pages, rem, starts, counter = r
        most_common = counter.most_common(3)
        marker = ""
        if rem == 0 and n_pages > 0:
            marker = "  ✓ body%pagesize==0"
        elif rem == HEADER:
            marker = "  (rem == 76 — header-like residue)"
        print(f"  pagesize={ps:>6}  n={n_pages:>6}  rem={rem:>4}{marker}  "
              f"first_dwords_top3={most_common}")
