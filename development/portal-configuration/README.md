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

```text
DEBUG=1
DJANGO_SETTINGS_MODULE=panoptes_tom.settings
SECRET_KEY="dkn94osg(gj*9wr=pa1a^-h__f%5_vb8h!8^9u%f(!m-ysb^1-"
DJANGO_HOST=my_db
GOOGLE_APPLICATION_CREDENTIALS=path-to-credentials
INSTANCE_CONNECTION_NAME=<YOUR_INSTANCE_NAME>
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=my_db
SQL_USER=my-username
SQL_PASSWORD=my-password
SQL_PORT=3306
```

