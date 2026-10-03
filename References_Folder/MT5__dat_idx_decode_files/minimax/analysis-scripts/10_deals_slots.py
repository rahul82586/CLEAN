#!/usr/bin/env python3
"""
Find the slot structure pattern in deals_2022.03.dat.
"""
import os, struct
from collections import Counter

BASE = "/workspace/mt5-analysis/bases"
HEADER = 76

with open(os.path.join(BASE, "deals_2022.03.dat"), 'rb') as f:
    dbody = f.read()[HEADER:]

print(f"deals body: {len(dbody):,} bytes")

# For each potential stride, find how consistent the first few bytes are
for stride in [528, 472, 384, 376, 360, 320, 304, 280, 256, 240, 232, 224, 216, 208, 200, 192, 184, 176, 168, 160, 152, 144, 136, 128, 120, 112, 104, 96, 88, 80, 72, 64]:
    n = len(dbody) // stride
    if n < 10: continue
    # look at first byte of each slot
    firsts = Counter()
    for s in range(n):
        firsts[dbody[s*stride]] += 1
    most = firsts.most_common(3)
    marker = ""
    if most[0][1] > n * 0.5:
        marker = "  <-- strong marker"
    print(f"stride={stride:4d}  n={n:>5}  first_byte_top3={[(f'0x{b:02x}', c) for b, c in most]}  {marker}")

# Also check: per-offset-of-stride consistency
print("\n\nFor stride=528 in deals, what byte patterns repeat at each offset within the slot?")
stride = 528
n = len(dbody) // stride
print(f"  n_slots={n}")
for off_in_slot in range(0, 64):
    vals = [dbody[s*stride + off_in_slot] for s in range(n)]
    c = Counter(vals)
    if len(c) <= 5 and c.most_common(1)[0][1] > n * 0.3:
        print(f"  offset {off_in_slot:3d}: {c.most_common(5)}")
