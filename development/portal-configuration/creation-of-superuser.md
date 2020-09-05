# Creation of Superuser

To gain admin privileges to your Django project, you must create a superuser account from within the running Docker container: 

```
$ docker-compose exec web python3 manage.py createsuperuser 
```

Confirm that the account was created successfully by going to your project's admin page at [http://0.0.0.0:8080/admin/](http://0.0.0.0:8080/admin/) and entering your superuser credentials. 







