#!/usr/bin/env python3
"""
Examine deals_2022.03.dat structure + all .idx files properly.
"""
import os, struct, re
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

# ---- DEALS_2022.03.DAT non-zero runs ----
print("="*70)
print("DEALS_2022.03.DAT — non-zero run analysis")
print("="*70)
with open(os.path.join(BASE, "deals_2022.03.dat"), 'rb') as f:
    dbody = f.read()[HEADER:]

# Find non-zero runs
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
print(f"  First 25 runs:")
for s, e in runs[:25]:
    print(f"    {s:>7}..{e:>7}  (len={e-s+1})")

# ---- DEALS_2022.03.IDX ----
print("\n" + "="*70)
print("DEALS_2022.03.IDX (48,720 bytes, 33% dense)")
print("="*70)
with open(os.path.join(BASE, "deals_2022.03.idx"), 'rb') as f:
    didx = f.read()

# full hex of header
print(f"\n  Header (first 128 bytes):")
print(hex_dump(didx[:128], 0, 16, 8))

# UTF-16 strings in idx
print(f"\n  UTF-16LE strings in idx (>=6 chars):")
strs = re.findall(rb'(?:[\x20-\x7e]\x00){6,}', didx)
for s in strs[:20]:
    decoded = s.decode('utf-16le', errors='ignore').rstrip('\x00')
    if decoded: print(f"    {decoded!r}")

# uint64 fields in idx
print(f"\n  First 16 uint64 values in idx body (offset 76+):")
for i in range(0, 128, 8):
    if 76 + i + 8 > len(didx): break
    v = struct.unpack('<Q', didx[76+i:76+i+8])[0]
    print(f"    idx offset {76+i:>5}  uint64 = {v:>20}  0x{v:016x}")

# ---- ORDERS.IDX, POSITIONS.IDX ----
for fname in ["orders.idx", "positions.idx"]:
    print("\n" + "="*70)
    print(f"{fname.upper()} full analysis")
    print("="*70)
    with open(os.path.join(BASE, fname), 'rb') as f:
        data = f.read()
    print(f"  size={len(data):,} bytes")
    print(f"\n  First 256 bytes:")
    print(hex_dump(data, 0, 16, 16))

    print(f"\n  UTF-16LE strings:")
    strs = re.findall(rb'(?:[\x20-\x7e]\x00){4,}', data)
    for s in strs[:10]:
        decoded = s.decode('utf-16le', errors='ignore').rstrip('\x00')
        if decoded: print(f"    {decoded!r}")

    print(f"\n  uint64 values (first 256 body bytes):")
    for i in range(0, 256, 8):
        if HEADER + i + 8 > len(data): break
        v = struct.unpack('<Q', data[HEADER+i:HEADER+i+8])[0]
        if v != 0: print(f"    offset {HEADER+i:>4}  uint64 = {v:>20}  0x{v:016x}")
