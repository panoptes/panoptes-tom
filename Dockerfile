FROM gcr.io/panoptes-exp/panoptes-utils:latest

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT 8000
ENV PANUSER panoptes

USER root
RUN apt-get update -y \
    && apt-get install python3-venv -y

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /panoptes-tom

RUN apt-get update -y\
    && apt-get install -y \
    postgresql \
    && apt-get install python3-dev \
    && apt-get install python3-pip \
    && apt-get install musl \
    && apt-get install gcc -y \
    && apt-get install libpq-dev -y \
    && apt-get install netcat -y


RUN apt-get update && apt-get install -y --no-install-recommends \
    curl gnupg2 ca-certificates gcc git pkg-config && \
    # Nginx for reverse proxy (static files)
    echo "deb http://nginx.org/packages/debian buster nginx" \
    | tee /etc/apt/sources.list.d/nginx.list && \
    curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add - && \
    apt-get update && \
    apt-get install nginx && \
    chown -R $PANUSER:$PANUSER /panoptes-tom


# Observation Portal requirements
COPY ./requirements.txt .
RUN pip3 install -U pip && \
    pip3 install --no-cache-dir -r requirements.txt

RUN apt-get autoremove --purge -y gcc pkg-config && \
    apt-get autoremove --purge -y && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "$PANUSER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    # Remove default site and link our conf below.
    rm /etc/nginx/conf.d/default.conf





# Define network ports and server config
EXPOSE ${PORT}
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

#copy entrypoint.sh
COPY ./entrypoint.sh .

#Copy project
COPY --chown=panoptes:panoptes . .

# run entrypoint.sh
ENTRYPOINT ["/panoptes-tom/entrypoint.sh"]