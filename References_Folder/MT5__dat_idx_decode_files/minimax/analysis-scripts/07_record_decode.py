#!/usr/bin/env python3
"""
Decode a single liveupdate.dat record (528-byte stride starting at offset 660)
and look for structure in deals_2022.03.dat.
"""
import os, struct
from collections import Counter

BASE = "/workspace/mt5-analysis/bases"
HEADER = 76

def hex_dump(data, off=0, width=16, n=16):
    lines = []
    for r in range(n):
        i = off + r*width
        if i >= len(data): break
        chunk = data[i:i+width]
        hex_part = ' '.join(f'{b:02x}' for b in chunk)
        ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
        lines.append(f"{i:08x}  {hex_part:<{width*3}}  {ascii_part}")
    return '\n'.join(lines)

# ---- LIVEUPDATE record decode ----
print("="*70)
print("LIVEUPDATE.DAT — first 4 records at 528-byte stride")
print("="*70)
with open(os.path.join(BASE, "liveupdate.dat"), 'rb') as f:
    lbody = f.read()[HEADER:]

# Confirm stride by inspecting record boundaries
for i, off in enumerate([660, 1188, 1716, 2244]):
    print(f"\n--- Record #{i+1} at body offset {off} ---")
    print(hex_dump(lbody, off, 16, 32))

# Extract the first 64 bytes of each record and look for fields
print("\n\nField analysis (first 80 bytes of each record):")
for i, off in enumerate([660, 1188, 1716, 2244]):
    rec = lbody[off:off+80]
    print(f"\n  Record {i+1}:")
    # uint64 fields
    for j in range(0, 80, 8):
        v = struct.unpack('<Q', rec[j:j+8])[0]
        if v != 0:
            print(f"    offset {j:2d}  uint64 = {v:>20}  0x{v:016x}")

# Check the 12-byte sub-structure before each record
print("\n\nPre-record sub-structures (12 bytes at offsets 628, 1156, 1684, 2212):")
for i, off in enumerate([628, 1156, 1684, 2212]):
    sub = lbody[off:off+12]
    print(f"  offset {off}: {sub.hex()}")

# ---- DEALS_2022.03.DAT record structure ----
print("\n\n" + "="*70)
print("DEALS_2022.03.DAT — looking for record stride")
print("="*70)
with open(os.path.join(BASE, "deals_2022.03.dat"), 'rb') as f:
    dbody = f.read()[HEADER:]

# Look at non-zero runs
nz = [(i, b) for i, b in enumerate(dbody) if b != 0]
runs = []
prev_end = -1
for i, b in nz:
    if i > prev_end + 1:
        runs.append([i, i])
    else:
        runs[-1][1] = i
    prev_end = i

print(f"  {len(runs)} non-zero runs in {len(dbody):,} bytes")
print(f"  First 30 runs:")
for s, e in runs[:30]:
    print(f"    {s:>7}..{e:>7}  (len={e-s+1})")

# Try autocorrelation of non-zero positions
nz_positions = [i for i, _ in nz]
# differences between consecutive positions
diffs = [nz_positions[i+1]-nz_positions[i] for i in range(len(nz_positions)-1)]
diff_counter = Counter(diffs)
print(f"\n  Top 30 most common inter-byte spacings (in body):")
for d, c in diff_counter.most_common(30):
    print(f"    spacing={d:>6}  count={c}")
