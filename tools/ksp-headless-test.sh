#!/bin/sh
# Loads KSP up to the main menu (until Contract Configurator has loaded the
# contracts) with this checkout of the pack and saves KSP.log
# to ./ksp-test/KSP.log. Runs against the host's Docker daemon, so it needs the
# docker CLI and /var/run/docker.sock (Gitea runner on the homelab, or the host).
#
# The game install (KSP_GAME) is never modified: it is the read-only lower layer
# of an overlay volume, and everything KSP writes, plus this pack, goes to a
# temporary upper layer that is deleted at the end.
#
# KSP_GAME   host path of the KSP install used for tests
# KSP_MODS   host path of mods symlinked into KSP_GAME (mounted read-only)
# CI_ROOT    host path for the temporary overlay layers
# KSP_IMAGE  the ksp-moddev image (Unity player libs, Xvfb)
set -eu
cd "$(dirname "$0")/.."

: "${KSP_GAME:=/mnt/projects/projects/ksp/KSP-dev}"
: "${KSP_MODS:=/mnt/projects/projects/ksp/mods}"
: "${CI_ROOT:=/mnt/projects/projects/ksp/ci}"
: "${KSP_IMAGE:=ksp-moddev:2019.4.18f1}"
id="sepc-${RUN_ID:-local-$$}"
pack=GameData/ContractPacks/SEPContracts

cleanup() {
	docker rm -f "$id-ksp" "$id-helper" >/dev/null 2>&1 || true
	docker volume rm "$id" >/dev/null 2>&1 || true
	docker run --rm -v "$CI_ROOT":/ci alpine rm -rf "/ci/$id" >/dev/null 2>&1 || true
}
trap cleanup EXIT

# Overlay volume: KSP_GAME read-only below, a fresh upper layer on top.
docker run --rm -v "$CI_ROOT":/ci alpine sh -c "mkdir -p /ci/$id/upper /ci/$id/work && chown 1000:1000 /ci/$id/upper"
docker volume create --driver local --opt type=overlay --opt device=overlay \
	--opt "o=lowerdir=$KSP_GAME,upperdir=$CI_ROOT/$id/upper,workdir=$CI_ROOT/$id/work" "$id" >/dev/null

# Swap in this checkout of the pack (in the dev install it may be a symlink).
docker run -d --name "$id-helper" -v "$id":/game alpine sleep 600 >/dev/null
docker exec "$id-helper" sh -c "rm -rf /game/$pack /game/KSP.log"
docker cp "$pack" "$id-helper:/game/$pack"
docker exec "$id-helper" chown -R 1000:1000 "/game/$pack"
docker rm -f "$id-helper" >/dev/null

# Start KSP headless and wait until Contract Configurator has finished loading
# the contracts, which happens a few seconds after the main menu shows up.
docker run -d --name "$id-ksp" --shm-size 2g -e PUID=1000 -e PGID=1000 \
	-v "$id":/game -v "$KSP_MODS":"$KSP_MODS":ro "$KSP_IMAGE" \
	bash -c 'export HOME=/tmp/h; mkdir -p $HOME; cd /game && timeout 900 xvfb-run -a -s "-screen 0 1280x720x24" ./KSP.x86_64 -force-glcore' >/dev/null
reached=no
for _ in $(seq 1 180); do
	if docker exec "$id-ksp" grep -aq "Contract Configurator .* finished loading" /game/KSP.log 2>/dev/null; then reached=yes; break; fi
	[ "$(docker inspect -f '{{.State.Running}}' "$id-ksp")" = true ] || break
	sleep 5
done
sleep 3

mkdir -p ksp-test
docker cp "$id-ksp:/game/KSP.log" ksp-test/KSP.log >/dev/null
echo "main menu reached and contracts loaded: $reached"
[ "$reached" = yes ]
