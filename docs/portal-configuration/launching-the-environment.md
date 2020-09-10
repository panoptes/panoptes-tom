# Launching the Developer Environment

The portal development environment can be launched from a [Docker](https://docs.docker.com/get-started/overview/) container. 

{% hint style="info" %}
 To learn more about Docker, see the [PANOPTES Docker Overview](https://app.gitbook.com/@projectpanoptes/s/pocs-user-guide/building/software/addendum-docker-overview) or check out this [Docker Basics](https://vsupalov.com/6-docker-basics/) guide. 
{% endhint %}

To launch the container, make sure you are in your project root directory, which by default would be located in `PANDIR=/var/panoptes`:

```
$ cd $PANDIR/panoptes-tom
```

Then, run the `setup-local-environment` script:

```
$ bash INCLUDE_BASE-true scripts/setup-local-environment.sh
```

This will build a Docker image from the requirements specified within the `Dockerfile` in your project root. 

You can verify that your image has been built by entering `docker image ls` in your terminal. You should see a list that looks something like this:

```
$ docker image ls
REPOSITORY                           TAG                 IMAGE ID            CREATED             SIZE
panoptes-tom                         develop             5ef7449ecc75        2 minutes ago       2.47GB
```

Next, run:

```
$ docker-compose -f docker/docker-compose.yaml up -d
```

This will launch a Docker container based on your image. By specifying `-d` , the container will start up in detached mode. Detached mode runs containers in the background.

Launching the container will also start a development server at which the observation portal can be reached. Go to [http://0.0.0.0:8080/](http://0.0.0.0:8080/) to view the portal now.

