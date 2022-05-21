# Smart Store
## Technology
-   [JWT](https://jwt.io) - JWT is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object
-   [Django](https://www.djangoproject.com) - a python web framework
-   [Django REST Framework](http://www.django-rest-framework.org) - a flexible toolkit to build web APIs
-   [Postgresql](https://www.postgresql.org/) - this is a database server

## Requirements
-   Use Python 3.x.x+
-   Use Django 3.x.x+

## Features
1. JWT authentication system
2. Admin Panel
3. Add, update, delete product
4. Reviewing products
5. Adding an item to the cart
6. View a users's order history

## Running the application
Set up database connection in **storefront/settings.py** in DATABASES section:
```py 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DATABASENAME', # Please change Me 
        'USER': 'USERNAME',  # Please change Me
        'PASSWORD': 'PASSWORD', # Please change Me
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
To run this application, clone the repository on your local machine and execute the following command.

```sh
$ pipenv install
$ pipenv shell
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
