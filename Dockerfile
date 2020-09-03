FROM gcr.io/panoptes-exp/panoptes-utils:latest

ARG port=8080

ENV TOMDIR $tomdir
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT $port

USER root

RUN mkdir /app
WORKDIR /app

# Observation Portal requirements

COPY ./scripts/resources/requirements.txt /app/
RUN apt-get update && \
    apt-get install -y python3-pip python-dev libpq-dev netcat && \
    pip3 install -U pip && \
    pip3 install --no-cache-dir -r requirements.txt

RUN apt-get autoremove --purge && \
    apt-get -y clean

COPY . /app/

# Define network port
EXPOSE ${PORT}


# run entrypoint.sh
ENTRYPOINT ["/bin/sh", "/app/scripts/resources/entrypoint.sh"]
