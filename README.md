---
description: >-
  A target and observation manager for Project PANOPTES built with the TOM
  Toolkit.
---

# PANOPTES Observation Portal

## Deployment

A prototype observation manager site can be found [here](https://panoptes-tom.herokuapp.com/).

## Development

To develop, clone the repo and activate a virtual environment for managing the `panoptes-tom` packages:

```text
$ python3 -m venv tom_env/
$ source tom_env/bin/activate
```

Next, install the necessary packages:

```text
$ pip install -r requirements.txt
```

Then, cd into the root project directory and run the necessary database migrations:

```text
$ cd path-to-file/panoptes-tom
$ ./manage.py makemigrations
$ ./manage.py migrate
```

To launch the server:

```text
$ ./manage.py runserver
```

