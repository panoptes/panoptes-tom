FROM gcr.io/panoptes-exp/panoptes-utils:latest

ARG tomdir=/home/jzonkey/Documents/panoptes-tom
ARG port=8000

ENV TOMDIR $tomdir
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT $port

USER root

WORKDIR ${TOMDIR}

# Observation Portal requirements

COPY ./scripts/resources/requirements.txt ${TOMDIR}
RUN apt-get update && \
    apt-get install -y python3-pip python-dev libpq-dev && \
    pip3 install -U pip && \
    pip3 install --no-cache-dir -r requirements.txt

RUN apt-get autoremove --purge && \
    apt-get -y clean

COPY . ${TOMDIR}

# Define network port
EXPOSE ${PORT}


# #copy entrypoint.sh
# COPY ./resources/entrypoint.sh ${TOMDIR}
RUN chmod +x ./scripts/resources/entrypoint.sh


# run entrypoint.sh
ENTRYPOINT ["/bin/sh", "/home/jzonkey/Documents/panoptes-tom/scripts/resources/entrypoint.sh"]
