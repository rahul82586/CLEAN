#!/usr/bin/env python3
"""
Check density and content distribution of each file.
"""
import os, struct
from collections import Counter

BASE = "/workspace/mt5-analysis/bases"
HEADER = 76

for fname in sorted(os.listdir(BASE)):
    p = os.path.join(BASE, fname)
    with open(p, 'rb') as f:
        data = f.read()
    body = data[HEADER:]

    # density
    nonzero = sum(1 for b in body if b != 0)
    density = nonzero / len(body) * 100
    # byte frequency
    counter = Counter(body)
    distinct = len(counter)
    top5 = counter.most_common(5)

    # check if file is "sparse" (mostly zeros with some non-zero clusters)
    # scan in 1KB blocks
    block_nonzero = 0
    nblocks = 0
    nonzero_blocks = 0
    for i in range(0, len(body), 1024):
        block = body[i:i+1024]
        nblocks += 1
        nb = sum(1 for b in block if b != 0)
        if nb > 0:
            nonzero_blocks += 1
        block_nonzero += nb

    # find first non-zero byte position in body
    first_nz = next((i for i, b in enumerate(body) if b != 0), -1)
    last_nz = next((i for i in range(len(body)-1, -1, -1) if body[i] != 0), -1)

    print(f"\n=== {fname} ===")
    print(f"  body={len(body):,}  nonzero={nonzero:,} ({density:.1f}%)  distinct_bytes={distinct}")
    print(f"  first_nz_offset_in_body={first_nz}  last_nz_offset_in_body={last_nz} (of {len(body)})")
    print(f"  non-zero blocks: {nonzero_blocks}/{nblocks} (1KB each)")
    print(f"  top5 bytes: {[(f'0x{b:02x}', c) for b, c in top5]}")
