#!/usr/bin/env python3
"""
Analyze deals_2022.03.dat (390KB, 11% dense) and liveupdate.dat (8KB, 47% dense)
— the only files with real content. Look for actual record structure.
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

# ---- LIVEUPDATE.DAT (small, dense, easier to analyze) ----
print("="*70)
print("LIVEUPDATE.DAT  (8,292 bytes body, 47% dense)")
print("="*70)

with open(os.path.join(BASE, "liveupdate.dat"), 'rb') as f:
    ldata = f.read()
lbody = ldata[HEADER:]
print(f"Body: {len(lbody)} bytes")
print()
print("First 256 bytes of body:")
print(hex_dump(lbody, 0, 16, 16))
print()
print("Bytes around offset 100 (where the sub-header / first record would be):")
print(hex_dump(lbody, 56, 16, 16))
print()

# Find non-zero regions
print("Non-zero regions in body:")
nz = [i for i, b in enumerate(lbody) if b != 0]
print(f"  {len(nz)} non-zero bytes")
# gaps
prev = -1
runs = []
start = None
for i in nz:
    if start is None:
        start = i
    elif i - prev > 8:
        runs.append((start, prev))
        start = i
    prev = i
if start is not None:
    runs.append((start, prev))
print(f"  {len(runs)} contiguous non-zero runs")
for s, e in runs[:20]:
    print(f"    {s:>6}..{e:>6}  (len={e-s+1})")
print()

# ASCII strings in body
print("ASCII-looking strings:")
import re
strs = re.findall(rb'[\x20-\x7e]{6,}', lbody)
for s in strs[:30]:
    print(f"    {s.decode('ascii', errors='ignore')!r}")

print()
# ---- DEALS_2022.03.DAT ----
print("="*70)
print("DEALS_2022.03.DAT  (390,704 bytes body, 11.1% dense)")
print("="*70)

with open(os.path.join(BASE, "deals_2022.03.dat"), 'rb') as f:
    ddata = f.read()
dbody = ddata[HEADER:]
print(f"Body: {len(dbody)} bytes")
print()
print("First 256 bytes of body:")
print(hex_dump(dbody, 0, 16, 16))
print()
print("Bytes 64..256 (after the first transition zone):")
print(hex_dump(dbody, 56, 16, 16))
print()

# Strings
strs = re.findall(rb'[\x20-\x7e]{6,}', dbody)
print(f"ASCII strings (>=6 chars): {len(strs)} found")
for s in strs[:30]:
    print(f"    {s.decode('ascii', errors='ignore')!r}")
print()

# UTF-16LE strings
strs = re.findall(rb'(?:[\x20-\x7e]\x00){6,}', dbody)
print(f"UTF-16LE strings (>=6 chars): {len(strs)} found")
for s in strs[:20]:
    try:
        decoded = s.decode('utf-16le', errors='ignore')
        print(f"    {decoded!r}")
    except:
        pass
