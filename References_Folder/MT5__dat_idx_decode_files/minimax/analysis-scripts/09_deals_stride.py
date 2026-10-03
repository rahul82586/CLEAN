#!/usr/bin/env python3
"""
Verify record stride for deals_2022.03.dat.
Also do a final correlation check on the liveupdate findings.
"""
import os, struct
from collections import Counter

BASE = "/workspace/mt5-analysis/bases"
HEADER = 76

# ---- DEALS_2022.03.DAT stride detection ----
print("="*70)
print("DEALS_2022.03.DAT — stride hypothesis: same 528-byte slots?")
print("="*70)
with open(os.path.join(BASE, "deals_2022.03.dat"), 'rb') as f:
    dbody = f.read()[HEADER:]

# Look at first 2000 bytes to find first non-zero records
# Show the transition from header to data
print("First 700 bytes hex:")
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
print(hex_dump(dbody, 0, 16, 44))

# Find positions of any 528-stride pattern
# Look for repeated 12-byte metadata blocks (de 0d 00 00)
positions = []
for i in range(0, len(dbody) - 12, 4):
    if dbody[i:i+4] == bytes([0xde, 0x0d, 0x00, 0x00]):
        positions.append(i)
print(f"\nPositions of magic 'de 0d 00 00' in deals body: {len(positions)} found")
if positions:
    diffs = [positions[i+1]-positions[i] for i in range(len(positions)-1)]
    diff_counter = Counter(diffs)
    print(f"  Spacings (top 10): {diff_counter.most_common(10)}")
    print(f"  First 30 positions: {positions[:30]}")
    if 528 in diff_counter:
        print(f"  *** FOUND 528-byte stride! ({diff_counter[528]} occurrences)")

# Check if 528 is the dominant spacing
print()
print("="*70)
print("LIVENESS: any non-zero data at every 528-byte offset?")
print("="*70)
nz = set(i for i, b in enumerate(dbody) if b != 0)
nz_in_slots = 0
empty_slots = 0
total_slots = len(dbody) // 528
for s in range(total_slots):
    slot_start = s * 528
    slot_end = slot_start + 528
    if any(i in nz for i in range(slot_start, slot_end)):
        nz_in_slots += 1
    else:
        empty_slots += 1
print(f"  {nz_in_slots} of {total_slots} slots have non-zero data ({empty_slots} empty)")

# ---- Re-confirm liveupdate: count of slots / 528 ----
print()
print("="*70)
print("LIVEUPDATE.DAT 528-slot count")
print("="*70)
with open(os.path.join(BASE, "liveupdate.dat"), 'rb') as f:
    lbody = f.read()[HEADER:]
total_slots = len(lbody) // 528
rem = len(lbody) % 528
print(f"  body={len(lbody):,}  slots={total_slots}  rem={rem}")

# ---- Cross-check: do the .idx offset values point into the .dat? ----
print()
print("="*70)
print(".IDX offset values — what do they point to in the .dat?")
print("="*70)
for name_idx, name_dat in [("orders.idx","orders.dat"), ("positions.idx","positions.dat"),
                            ("deals_2022.03.idx","deals_2022.03.dat")]:
    with open(os.path.join(BASE, name_idx), 'rb') as f:
        idx = f.read()
    with open(os.path.join(BASE, name_dat), 'rb') as f:
        dat = f.read()
    # extract uint32 values from idx body
    body = idx[HEADER:]
    offsets = []
    for i in range(0, len(body)-4, 4):
        v = struct.unpack('<I', body[i:i+4])[0]
        if 76 < v < len(dat) - 4:
            offsets.append((i + HEADER, v))
    print(f"\n  {name_idx} → {name_dat}  (size {len(dat):,})")
    print(f"  Found {len(offsets)} plausible offsets")
    for pos, off in offsets[:10]:
        # show byte at offset
        b = dat[off:off+4]
        print(f"    idx_offset {pos:>5} → dat[{off}] = {b.hex()} ({struct.unpack('<I', b)[0]})")
