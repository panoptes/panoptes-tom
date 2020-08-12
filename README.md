# PANOPTES Observation Portal

A target and observation manager for [Project PANOPTES](https://github.com/panoptes) built with the [TOM Toolkit](https://tom-toolkit.readthedocs.io/en/stable/index.html).

## Deployment

A prototype observation manager site can be found [here](https://panoptes-tom.herokuapp.com/).

## Development

To develop, clone the [repo](https://github.com/panoptes/panoptes-tom) and activate a virtual environment for managing the `panoptes-tom` packages:

```text
$ python3 -m venv tom_env/
$ source tom_env/bin/activate
```

Next, install the necessary packages:

```text
$ cd path-to-file/panoptes-tom
$ pip install -r requirements.txt
```

### Setting Environment Variables

To properly configure the project, create a `.env` file with the following information and save it in your project root:

**Create a `.env` file:**

```bash
$ touch .env
$ gedit .env
```

**Add the following environment vars:**

```text
DEBUG=1
DJANGO_SETTINGS_MODULE=panoptes_tom.settings
SECRET_KEY="dkn94osg(gj*9wr=pa1a^-h__f%5_vb8h!8^9u%f(!m-ysb^1-"
DJANGO_HOST=127.0.0.1
SQL_ENGINE=django.db.backends.sqlite3
SQL_DATABASE=db.sqlite3
```

### Launching the Dev Server:

From the root project directory, run the necessary database migrations:

```text
$ ./manage.py makemigrations
$ ./manage.py migrate
```

To launch the server:

```text
$ ./manage.py runserver
```

### Configuring Additional Databases:

Django can be easily configured to run additional databases such as PostGreSQL or MySQL. It also supports cloud databases such as [Cloud SQL. ](https://cloud.google.com/python/django/flexible-environment#understanding_the_code)

Simply edit the `.env` file to include the following information:

```text
SQL_ENGINE=django.db.backends.your-engine-of-choice
SQL_DATABASE=database_name

# If you're using a Cloud db, the additional info may be necessary:
SQL_USER=your-username
SQL_PASSWORD=your-password
SQL_PORT=your-port-number
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials.json
```

Next, uncomment the following lines in `settings.py`as shown below:

```python
GOOGLE_CLOUD_CONFIG_KEY = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

DATABASES = {
    "default": {
         "ENGINE": os.getenv("SQL_ENGINE"),
         "NAME": os.getenv("SQL_DATABASE"),
         "USER": os.getenv("SQL_USER"),
         "PASSWORD": os.getenv("SQL_PASSWORD"),
         "PORT": os.getenv("SQL_PORT"),
         "HOST": os.getenv("DJANGO_HOST"),
     }
    # "default": {
    #  "ENGINE": os.getenv("SQL_ENGINE"),
    #  "NAME": os.path.join(BASE_DIR, os.getenv("SQL_DATABASE")),
    # }
}

```

To apply your changes, run:

```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```



