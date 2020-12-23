#!/usr/bin/env bash
set -e

export PANDIR=${PANDIR:-/var/panoptes}
export TOMDIR=${TOMDIR:-"${PANDIR}/panoptes-tom"}

INCLUDE_UTILS=${INCLUDE_UTILS:-false}
PANOPTES_UTILS=${PANOPTES_UTILS:-$PANDIR/panoptes-utils}
_UTILS_IMAGE_URL="gcr.io/panoptes-exp/panoptes-utils:latest"

build_utils() {
  INCLUDE_BASE=true /bin/bash "${PANOPTES_UTILS}/scripts/setup-local-environment.sh"
  # Use our local image for build below instead of gcr.io image.
  _UTILS_IMAGE_URL="panoptes-utils:develop"
}

echo "Building local panoptes-tom in ${TOMDIR}"
cd "${TOMDIR}"

# Build local panoptes-utils:develop if needed.
if [ "${INCLUDE_UTILS}" = true ]; then
  build_utils
fi

echo "Building local panoptes-tom:develop from ${_UTILS_IMAGE_URL}"
docker build \
  --build-arg "image_url=${_UTILS_IMAGE_URL}" \
  -t "panoptes-tom:develop" \
  -f "${TOMDIR}/docker/Dockerfile" \
  "${TOMDIR}"

cat <<EOF
Done building the local images. To run, enter:

docker-compose -f docker/docker-compose.yaml up -d
EOF
