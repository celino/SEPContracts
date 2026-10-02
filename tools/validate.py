#!/usr/bin/env python3
"""Checks the contract pack before packaging. Standard library only.

- every #sepc key used in the contract cfgs is defined in every language file
- all language files define the same keys, with no duplicates
- each string uses the same <<n>> placeholders in every language
- braces are balanced in every cfg
- CONTRACT_TYPE names are unique
- the .version file is valid JSON, and matches the git tag when run on a tag
- CHANGELOG.md has a section for the version in the .version file

Usage: python3 tools/validate.py [--tag vX.Y.Z]
"""
import glob
import json
import os
import re
import sys

PACK = os.path.join("GameData", "ContractPacks", "SEPContracts")
errors = []


def strip_comments(text):
    return "\n".join(line.split("//", 1)[0] for line in text.splitlines())


def read(path):
    with open(path, encoding="utf-8-sig") as f:
        return f.read()


def load_localization(path):
    keys = {}
    for line in strip_comments(read(path)).splitlines():
        m = re.match(r"\s*(#sepc\.[^\s=]+)\s*=\s*(.*?)\s*$", line)
        if not m:
            continue
        key, value = m.groups()
        if key in keys:
            errors.append(f"{path}: duplicate key {key}")
        keys[key] = value
    return keys


def placeholders(value):
    return sorted(set(re.findall(r"<<[A-Za-z]?:?(\d+)", value)))


# Localization
languages = {os.path.basename(p): load_localization(p)
             for p in sorted(glob.glob(os.path.join(PACK, "Localization", "*.cfg")))}
if "en-us.cfg" not in languages:
    errors.append("Localization/en-us.cfg is missing")
reference = languages.get("en-us.cfg", {})
for name, keys in languages.items():
    if name == "en-us.cfg":
        continue
    for key in sorted(set(reference) - set(keys)):
        errors.append(f"{name}: missing {key}")
    for key in sorted(set(keys) - set(reference)):
        errors.append(f"{name}: {key} is not in en-us.cfg")
    for key in sorted(set(reference) & set(keys)):
        if placeholders(reference[key]) != placeholders(keys[key]):
            errors.append(f"{name}: {key} uses <<{placeholders(keys[key])}>>, en-us uses <<{placeholders(reference[key])}>>")

# Contract cfgs
contract_files = sorted(glob.glob(os.path.join(PACK, "*.cfg")))
used = set()
contract_names = {}
for path in contract_files:
    text = strip_comments(read(path))
    used.update(re.findall(r'Format\("(#sepc\.[^"]+)"', text))
    depth = 0
    for n, line in enumerate(text.splitlines(), 1):
        depth += line.count("{") - line.count("}")
        if depth < 0:
            errors.append(f"{path}:{n}: unexpected closing brace")
            depth = 0
    if depth != 0:
        errors.append(f"{path}: {depth} unclosed brace(s)")
    for m in re.finditer(r"CONTRACT_TYPE\s*\{\s*name\s*=\s*(\S+)", text):
        name = m.group(1)
        if name in contract_names:
            errors.append(f"{path}: CONTRACT_TYPE {name} already defined in {contract_names[name]}")
        contract_names[name] = path
for name, keys in languages.items():
    for key in sorted(used - set(keys)):
        errors.append(f"{name}: {key} is used by a contract but not defined")

# .version
version_path = os.path.join(PACK, "SEPContracts.version")
try:
    v = json.loads(read(version_path))["VERSION"]
    version = f'{v["MAJOR"]}.{v["MINOR"]}.{v["PATCH"]}'
except Exception as e:  # noqa: BLE001 - report any problem with the file
    errors.append(f"{version_path}: {e}")
    version = None
if "--tag" in sys.argv and version:
    tag = sys.argv[sys.argv.index("--tag") + 1]
    if tag.lstrip("v") != version:
        errors.append(f"tag {tag} does not match .version {version}")
if version and not re.search(rf"^## {re.escape(version)}\b", read("CHANGELOG.md"), re.M):
    errors.append(f"CHANGELOG.md has no section for {version}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: version {version}, {len(contract_names)} contract types, "
      f"{len(reference)} keys in {len(languages)} languages")
