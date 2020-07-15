# panoptes-tom

A target and observation manager for [Project PANOPTES](https://github.com/panoptes) built with the [TOM Toolkit](https://tom-toolkit.readthedocs.io/en/stable/index.html).

## Deployment

A prototype observation manager site can be found [here](https://panoptes-tom.herokuapp.com/).

## Development

To develop, clone the repo and cd into the project's root directory:

```shell
$ git clone https://github.com/jlibermann/panoptes-tom.git
$ cd path-to-file/panoptes-tom
```

Next, install the necessary packages:
```shell
$ pip install -r requirements.txt
```


Then, run the necessary database migrations:
```shell
$ ./manage.py makemigrations
$ ./manage.py migrate
```
To launch the server:
```shell
$ ./manage.py runserver
```


