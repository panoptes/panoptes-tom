ARG image_url=gcr.io/panoptes-exp/panoptes-utils:latest
FROM ${image_url} AS base-image

ARG port=8080
ARG tomdir=/var/panoptes/panoptes-tom

ENV TOMDIR $tomdir
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT $port

ARG panuser=panoptes
ARG userid=1000
ARG pan_dir=/var/panoptes
ARG pocs_dir="${pan_dir}/POCS"
ARG conda_env_name="panoptes"

ENV PANDIR $pan_dir
ENV PANLOG "$pan_dir/logs"
ENV PANUSER $panuser
ENV POCS $pocs_dir

WORKDIR /app

# Observation Portal requirements
USER root
RUN apt-get update && \
    apt-get install --yes sqlite3 libpq-dev

# Install the module.
USER ${PANUSER}
COPY --chown=panoptes:panoptes ./requirements.txt /tmp/
RUN "${PANDIR}/conda/envs/${conda_env_name}/bin/pip" install -r /tmp/requirements.txt && \
    # Cleanup
    sudo apt-get autoremove --purge --yes && \
    sudo apt-get autoclean --yes && \
    sudo apt-get --yes clean && \
    sudo rm -rf /var/lib/apt/lists/* && \
    "${PANDIR}/conda/bin/conda" clean -tipy

COPY --chown=panoptes:panoptes ./ /app/

USER root
CMD ["/app/scripts/start-portal.sh"]
