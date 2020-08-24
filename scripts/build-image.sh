#!/bin/bash -e

SOURCE_DIR="/home/jzonkey/Documents/panoptes-tom"
BASE_CLOUD_FILE="cloudbuild.yaml"
TAG=${1:-develop}

cd "${SOURCE_DIR}"

echo "Building gcr.io/panoptes-exp/panoptes-tom:${TAG}"
gcloud builds submit \
    --timeout="5h" \
    --substitutions "_TAG=${TAG}" \
    --config "${SOURCE_DIR}/${BASE_CLOUD_FILE}" \
    "${SOURCE_DIR}" \
    --machine-type=n1-highcpu-8