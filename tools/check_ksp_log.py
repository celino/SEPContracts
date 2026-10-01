#!/usr/bin/env python3
"""Reads the KSP.log from tools/ksp-headless-test.sh and fails if the pack did
not load cleanly: every CONTRACT_TYPE in the pack must be "Successfully loaded"
by Contract Configurator, and no error or exception may mention the pack.
Errors from other mods are listed for information only.

Usage: python3 tools/check_ksp_log.py [ksp-test/KSP.log]
"""
import glob
import os
import re
import sys

PACK = os.path.join("GameData", "ContractPacks", "SEPContracts")
log_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join("ksp-test", "KSP.log")
with open(log_path, encoding="utf-8", errors="replace") as f:
    lines = f.read().splitlines()

expected = set()
for path in glob.glob(os.path.join(PACK, "*.cfg")):
    with open(path, encoding="utf-8-sig") as f:
        text = "\n".join(l.split("//", 1)[0] for l in f.read().splitlines())
    expected.update(re.findall(r"CONTRACT_TYPE\s*\{\s*name\s*=\s*(\S+)", text))

loaded = set(re.findall(r"Successfully loaded CONTRACT_TYPE '([^']+)'", "\n".join(lines)))
ours = re.compile(r"SEPContracts|#sepc\.|'(" + "|".join(map(re.escape, expected)) + r")'")

problems = []
for name in sorted(expected - loaded):
    problems.append(f"CONTRACT_TYPE {name} was not loaded")
for i, line in enumerate(lines):
    if not re.match(r"\[(ERR|EXC|WRN)", line):
        continue
    # an error or exception can name the pack in its first stack lines;
    # a warning has to name it on its own line
    text = line if line.startswith("[WRN") else " ".join(lines[i:i + 4])
    if ours.search(text):
        problems.append(line.strip())

others = sum(1 for l in lines if re.match(r"\[(ERR|EXC)", l)) - sum(1 for p in problems if p.startswith(("[ERR", "[EXC")))
print(f"{len(loaded & expected)}/{len(expected)} contract types loaded; "
      f"{others} errors/exceptions from other mods (not checked)")
if problems:
    print("\n".join(problems))
    sys.exit(1)
print("OK")
