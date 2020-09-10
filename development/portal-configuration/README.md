# Portal Configuration

### Setting Environment Variables

To configure the portal, create a `.env` file with the following information and save it in your project root:

**Create a `.env` file:**

```bash
$ touch .env
$ gedit .env
```

**Add the following environment vars:**

{% hint style="warning" %}
By default, the observation portal is configured to run a [Cloud SQL ](https://cloud.google.com/python/django/flexible-environment#understanding_the_code)db. For connection information, contact info@projectpanoptes.org. 
{% endhint %}

```bash
DEBUG=1

DJANGO_SETTINGS_MODULE=panoptes_tom.settings

SECRET_KEY="dkn94osg(gj*9wr=pa1a^-h__f%5_vb8h!8^9u%f(!m-ysb^1-"

# Use sqlite3 for local or postgresql for CloudSQL.
SQL_ENGINE=django.db.backends.sqlite3
#SQL_ENGINE=django.db.backends.postgresql

DJANGO_HOST=<DJANGO_HOST>

# Change the db name for CloudSQL.
SQL_DATABASE=tom_postgres_db

# If using authentication (required for CloudSQL).
# SQL_USER=<SQL_USER>
# SQL_PASSWORD=<SQL_PASSWORD>

# If using the CloudSQL proxy, uncomment the following.
# SQL_PORT=3306

# If using Cloud SQL uncomment following.
# GOOGLE_APPLICATION_CREDENTIALS=<PATH_TO_CREDENTIALS>
# INSTANCE_CONNECTION_NAME=<YOUR_INSTANCE_NAME>

```

