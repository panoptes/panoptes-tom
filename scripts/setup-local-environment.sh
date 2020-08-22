#!/usr/bin/env bash
set -e

export TOMDIR=${TOMDIR:-/home/jzonkey/Documents/panoptes-tom}


echo "Setting up local environment."

echo "Removing stale docker images to make space"
docker system prune --force

echo "Building local panoptes-tom"
. "${TOMDIR}/Docker/setup-local-environment.sh"


# In the local develop we need to pass git to the docker build context.
#sed -i s'/^\.git$/\!\.git/' .dockerignore

echo "Building local panoptes-tom:latest from panoptes-utils:latest"
docker build \
    --quiet --force-rm \
    --build-arg IMAGE_URL="panoptes-utils:latest" \
    -t "panoptes-tom:latest" \
    -f "${TOMDIR}/Docker/latest.Dockerfile" \
    "${TOMDIR}"


# Revert our .dockerignore changes.
#sed -i s'/^!\.git$/\.git/' .dockerignore

docker system prune --force

cat << EOF
Done building the local images.
EOF