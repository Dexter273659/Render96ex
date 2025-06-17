#!/usr/bin/env python3
import sys

# usage: python3 patch_core.py input.dll output.dll
data = open(sys.argv[1], "rb").read()
patched = data.replace(
    b"\xFF\xFF\xFF\x03",  # old mask = 0x03FFFFFF
    b"\xFF\xFF\xFF\x0F"   # new mask = 0x0FFFFFFF
)
open(sys.argv[2], "wb").write(patched)
