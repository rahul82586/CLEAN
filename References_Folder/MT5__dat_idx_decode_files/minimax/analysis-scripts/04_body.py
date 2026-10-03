#!/usr/bin/env python3
"""
Examine the actual byte structure of MT5 file bodies. Try:
  1. Specific-byte-position analysis (every Nth byte pattern)
  2. Sub-header hypothesis (extra metadata block before records)
  3. Cross-file ratio analysis
"""
import os, struct
from collections import Counter

BASE = "/workspace/mt5-analysis/bases"
HEADER = 76

def show_off(off):
    return f"{off:08x}"

# Try a sub-header theory: maybe the file has [76 hdr] + [X subhdr] + [records...]
# Find X by looking for transition from header-like to record-like byte pattern
for fname in ["liveupdate.dat", "orders.dat", "positions.dat", "users.dat", "deals_2022.03.dat", "kyc.dat"]:
    p = os.path.join(BASE, fname)
    with open(p, 'rb') as f:
        data = f.read()
    body = data[HEADER:]
    print(f"\n=== {fname}  body={len(body):,} bytes ===")

    # Try common sub-header sizes; check whether (body - subhdr) is a clean multiple of common record sizes
    for subhdr in [0, 8, 12, 16, 20, 24, 28, 32, 40, 48, 52, 56, 60, 64, 76, 80, 88, 96, 100, 104, 116, 124, 128]:
        if subhdr >= len(body): continue
        effective = len(body) - subhdr
        for rs in [64, 80, 96, 100, 108, 112, 120, 128, 144, 152, 160, 168, 176, 192, 200, 208, 224, 232, 240, 256,
                   288, 320, 360, 384, 400, 432, 448, 480, 504, 512, 528, 540, 560, 576, 600, 624, 640, 648, 656,
                   672, 688, 704, 720, 736, 752, 768, 784, 800, 816, 832, 848, 864, 880, 896, 912, 928, 944, 960]:
            if effective % rs == 0 and effective // rs > 10:
                # also check that the FIRST byte of each record isn't always 0
                first_bytes = Counter()
                for i in range(min(50, effective // rs)):
                    first_bytes[body[subhdr + i*rs]] += 1
                most = first_bytes.most_common(1)[0]
                # if more than 90% of records start with the SAME byte, that's a marker!
                marker_pct = most[1] / max(1, min(50, effective // rs))
                if marker_pct > 0.7:
                    print(f"  subhdr={subhdr:3d}  recordsize={rs:4d}  n={effective//rs:>8,}  first_byte_distinct={len(first_bytes):3d}  top_first_byte=0x{most[0]:02x} ({marker_pct*100:.0f}%)")
