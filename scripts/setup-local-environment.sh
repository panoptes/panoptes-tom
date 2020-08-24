#!/usr/bin/env bash
set -e

export TOMDIR=${TOMDIR:-/home/jzonkey/Documents/panoptes-tom}


echo "Setting up local environment."

echo "Removing stale docker images to make space"
docker system prune --force

echo "Building local panoptes-tom"
cd "${TOMDIR}"

echo "Building local panoptes-tom:latest from panoptes-utils:latest"
docker build \
    --quiet --force-rm \
    --build-arg IMAGE_URL="panoptes-utils:latest" \
    -t "panoptes-tom:latest" \
    -f "${TOMDIR}/Dockerfile" \
    "${TOMDIR}"

docker system prune --force

cat << EOF
Done building the local images.
EOF