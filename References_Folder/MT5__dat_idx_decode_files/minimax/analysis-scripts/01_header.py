#!/usr/bin/env python3
"""
Proper byte-level forensic analysis of MT5 .dat / .idx files.

Methodology:
  1. Confirm 76-byte header across all files
  2. Find TRUE record size via autocorrelation of body bytes
  3. Examine .idx structure (it's clearly not a simple offset array)
  4. Cross-validate findings across multiple files
"""
import os, struct, math, hashlib
from collections import Counter, defaultdict

BASE = "/workspace/mt5-analysis/bases"

# ----------------------------------------------------------------------------
# STEP 1: Header analysis (confirmation of what previous analysis got right)
# ----------------------------------------------------------------------------
print("="*80)
print("STEP 1 — HEADER CONFIRMATION")
print("="*80)

def header_summary(path):
    size = os.path.getsize(path)
    with open(path, 'rb') as f:
        head = f.read(128)
    version = struct.unpack('<I', head[:4])[0]
    try:
        s = head[4:76].decode('utf-16le', errors='ignore').rstrip('\x00')
    except:
        s = "?"
    return size, version, s

files = sorted(os.listdir(BASE))
for f in files:
    p = os.path.join(BASE, f)
    size, ver, copy = header_summary(p)
    print(f"  {f:30s}  size={size:>12,}  version={ver:>4}  copyright='{copy}'")
