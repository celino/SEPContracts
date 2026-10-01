#!/bin/sh
# Builds dist/SEPContracts-<version>.zip with GameData/ at the root of the zip
# (the layout SpaceDock and CKAN expect), plus README.md and LICENSE.
set -eu
cd "$(dirname "$0")/.."

version=$(python3 -c 'import json; v = json.load(open("GameData/ContractPacks/SEPContracts/SEPContracts.version"))["VERSION"]; print("%d.%d.%d" % (v["MAJOR"], v["MINOR"], v["PATCH"]))')
out="dist/SEPContracts-${version}.zip"

rm -rf dist
mkdir -p dist
python3 - "$out" <<'EOF'
import os, sys, zipfile
out = sys.argv[1]
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk("GameData"):
        for name in sorted(files):
            z.write(os.path.join(root, name))
    for name in ("README.md", "LICENSE"):
        z.write(name)
EOF
echo "$out"
