# panoptes-tom

A target and observation manager for [Project PANOPTES](https://github.com/panoptes) built with the [TOM Toolkit](https://tom-toolkit.readthedocs.io/en/stable/index.html).

# Deployment

A prototype observation manager site can be found [here](https://panoptes-tom.herokuapp.com/).

# Development

To develop, cd into the project's root directory, and run the necessary migrations:
```shell
$ cd Documents/panoptes-tom
$ ./manage.py makemigrations
$ ./manage.py migrate
```
To launch the server:
```shell
$ ./manage.py runserver
```


