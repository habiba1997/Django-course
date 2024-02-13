# Django project

Django is a high-level web framework for building web applications in Python, and it follows the Model-View-Controller (
MVC) architectural pattern. In Django, this pattern is often referred to as the Model-View-Template (MVT) pattern.

### Project vs. App:

- In Django, a project is the entire web application, and it consists of one or more apps.
- An app is a modular component within a Django project. It encapsulates a specific functionality or set of related
  functionalities.

- ### Folder Structure:

When you create a new Django project using the django-admin startproject command, it generates a folder structure like
this:

```
project_name/
├── manage.py
└── project_name/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── asgi.py
```

- manage.py: A command-line utility for interacting with your project, including running development servers,
  creating database tables, and more.
- project_name: The main project directory containing the settings, URL configurations, and other project-specific
  files.
    - `__init__.py`: An empty file that makes the directory a Python package.
    - `settings.py`: Configuration settings for the project, such as database settings, installed apps, middleware, etc.
    - `urls.py`: URL patterns for the project.
    - `asgi.py`: Entry point for ASGI (Asynchronous Server Gateway Interface) applications.

Note:   \
`asgi.py` is a file in a Django project that serves as the entry point for ASGI (Asynchronous Server Gateway Interface)
applications. ASGI is a specification for asynchronous web servers and frameworks, allowing for more efficient handling
of long-lived connections, such as WebSockets, and supporting asynchronous views and middleware.

```
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

application = get_asgi_application()
```

Explanation of the contents:

- os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings'): This line sets the DJANGO_SETTINGS_MODULE
  environment variable to point to your project's settings module. This ensures that when the ASGI server starts, it
  uses the correct Django settings for your project.

- get_asgi_application(): This function is part of Django's core ASGI support. It returns an instance of the Django ASGI
  application, which can handle ASGI requests.

### App Structure:

When you create a new Django app using python manage.py startapp, it generates a folder structure like this:

```
app_name/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

- migrations/: Stores database migration files.
- `__init__`.py: Makes the directory a Python package.
- admin.py: Configuration for the Django admin interface.
- apps.py: Configuration for the app.
- models.py: Defines database models using Django's Object-Relational Mapping (ORM).
- tests.py: Contains test cases for the app.
- views.py: Defines views that handle HTTP requests and produce HTTP responses.

Note:
In a Django project, there is only one admin site that is shared among all apps. The admin interface is a centralized
management interface provided by Django, and it consolidates the administration of models from all installed apps in a
project.
When you customize the admin.py file within each app, you are essentially providing instructions on how the models from
that app should be displayed and managed within the shared admin site. The customizations you define in each admin.py
file contribute to the overall appearance and behavior of the single Django admin site for the entire project.

### Templates, Static Files, and Media:

Django uses a template system for rendering HTML content.

- Templates are typically stored in a templates/ folder wit-in each app.
- Static files such as CSS, JavaScript, and images are stored in a static/ folder within each app.
- Media files, such as user-uploaded images, are stored in a media/ folder.

### Settings:

- The `settings.py` file in the project directory contains global configuration settings for the entire Django project.
  This includes database configuration, installed apps, middleware, and more.
- `Database Configuration:` Django supports multiple databases. The database configuration is specified in the DATABASES
  setting in the settings.py file.
- URL Patterns: The `urls.py` files in both the project and app directories define URL patterns. They map URL patterns
  to views, allowing you to handle different HTTP requests.
  Understanding this high-level structure should give you a good starting point for working with Django. As you delve
  deeper into Django development, you'll encounter additional features and concepts that contribute to the framework's
  power and flexibility.
- The `INSTALLED_APPS` setting is a list of Django applications that are installed and active in your project. These
  applications provide models, views, templates, and other components. It helps Django to know which apps are available
  and should be considered when processing various tasks like migrations, template rendering, etc.
  Some default apps are included, such as 'django.contrib.admin', 'django.contrib.auth', and '
  django.contrib.staticfiles'
  The INSTALLED_APPS provide essential functionalities and features for building web applications.
    - django.contrib.admin: This app provides the Django admin interface, which is a powerful, customizable, and
      automatic administrative interface for managing models and data in your Django project.
      It allows administrators to view, add, edit, and delete records in the database through a user-friendly web
      interface.
    - django.contrib.auth: The auth app handles user authentication and authorization. Features include user
      registration, login, logout, password management, and access control.
    - django.contrib.staticfiles: The staticfiles app helps manage static files (CSS, JavaScript, images, etc.) in your
      Django project.
- `ROOT_URLCONF`: The ROOT_URLCONF setting points to the Python module that defines the project's URL patterns. By
  default, it's set to 'myproject.urls'.
- `STATIC_URL` in Django is a setting that defines the base URL to serve static files (CSS, JavaScript, images, etc.).
  It is combined with the STATICFILES_DIRS setting to determine where Django should look for static files.
- `MEDIA_URL` is similar to STATIC_URL but is used for serving media files, such as user-uploaded images or files.
  It is combined with the MEDIA_ROOT setting, which specifies the local filesystem path where media files are stored.\
  Example in settings.py:

```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- `Middleware:` Middleware components are used to process requests and responses globally before reaching the view or
  after leaving the view.
  Middleware can perform tasks such as authentication, security, caching, and more. They are configured in the
  MIDDLEWARE setting in the settings.py file.\
  Example MIDDLEWARE setting in settings.py:

```
  MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Each middleware in the list processes the request or response in the order specified.

- `Template System:` Django uses its own template system to generate HTML dynamically.
  Templates are stored in the templates/ directory within each app.
  The TEMPLATES setting in settings.py configures the template engine and its options.\
  Example TEMPLATES setting in settings.py:

```TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

In this example, 'DIRS' specifies additional template directories, and 'APP_DIRS' enables Django to look for templates
within each app.

- The `DATABASES` setting configures the database connection.
- The `WSGI_APPLICATION` setting points to the WSGI application used to serve the project.
- The `AUTH_PASSWORD_VALIDATORS` setting defines a list of validators that Django uses to check the strength of user
  passwords.
- `USE_I18N` enables or disables internationalization (translation) in Django.
- `USE_TZ` enables or disables time zone support.
- The `DEFAULT_AUTO_FIELD` setting defines the default primary key field type for models.
  In modern Django versions, it's set to 'django.db.models.BigAutoField'.In Django, the BigAutoField is a type of model
  field used for automatically incrementing a unique integer value in a database table. It's specifically designed for
  databases that support 64-bit integers, such as PostgreSQL.

```
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

To start a pyhton project and create a virtual enviroment
`python -m venv ${virtual-enviroment-name}`

To check all installed python packages use
`pip freeze`

To create a requirmemt.txt folder
`pip freeze > requirements.txt `

To create django project
`django-admin startproject ${project-name}`

A django project is divided into apps
`cd .\watchmate`
`python manage.py startapp ${app_name}`

To run django server
`python manage.py runserver`

To migrate (is a command used to apply database migrations)
`python manage.py makemigrations`
`python manage.py migrate` \
The makemigrations command is used to create new database migration files based on the changes detected in your Django
models.
The migrate command is used to apply database migrations and update the database schema based on the migration files
generated by makemigrations.

To create a super user
`python manage.py createsuperuser`

admin panel on
`/admin`

### Notes:

- when you create a new model in one of the applications model.py file, then run migration command for django to create
  migration sql script
  finally add the model into admin.py file (register model) so it can be overviewed by admin panel\

- using Response instead of JSONResponse show the browsable api

### Serialization Vs De-Serialization

movies = Movies.objects.all (Model Object - query object - complex datatype)

- Complex Datatype(Queries) -- SERIALIZATION --> Python Native datatype(dictionaries) -- RENDER --> JSON data
- JSON data -- PARSE DATA --> Python Native Datatype -- DE-SERIALIZATION -->  Complex Datatype

### Questions

1- how is the association between the serializer and the model is explicit in the serializer class definition., where
how, how does it know which model to work on, how is it connected to database and get data ? how does it know when we
call serializer = MovieSerializer(movie)
it means get movie serialized while MovieSerializer(movie, data=request.data) means update or call update function in
serializer, how does it know whchh function to call and how save method save to database
ChatGPT
The association between the serializer and the model is established through the definition of the serializer class. In
your case, the MovieSerializer class explicitly defines the fields and their types, which correspond to the fields in
the Movie model. This explicit definition creates a connection between the serializer and the model. Let's break it down
further:

a- Serializer Class (MovieSerializer):

The serializer defines the fields and their types. In your case:

```
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()    
```

Here, the fields (id, name, description, active) are explicitly defined in the serializer. The types of these fields are
based on the corresponding fields in the Movie model.

b- Model (Movie):
The Movie model defines the structure of the database table for movies. It includes fields such as name, description,
and active.

c- Serializer Usage in View:
When you use serializer = MovieSerializer(movie), it means you are creating a serializer instance for a specific Movie
model instance (movie). The serializer uses the defined fields and types to convert the movie instance into a serialized
format (serializer.data).
When you use serializer = MovieSerializer(movie, data=request.data), it means you are creating a serializer instance for
the same Movie model, but this time you are providing updated data from the request. This triggers the serializer's
update method, which is responsible for updating the model instance with the provided data.

d- Serializer Methods (create and update):
The create and update methods in the serializer are responsible for handling how data is saved or updated in the
database.
When you call serializer.save() in the view, it internally decides whether to call the create method (for new instances)
or the update method (for existing instances) based on whether the serializer instance has an associated database
instance (movie in this case).

e- Database Connection:
Django ORM (Object-Relational Mapping) is responsible for the interaction with the database. When you call
Movie.objects.get(id=movie_id) in the view, it retrieves a Movie instance from the database. Similarly, when you call
serializer.save(), the serializer uses the Django ORM to save or update the data in the database.


In summary, the association between the serializer and the model is established through the explicit definition of
fields in the serializer class, which mirrors the fields in the model. The serializer knows which model to work on based
on its definition. The create and update methods in the serializer handle the logic for saving or updating data in the
database, and Django ORM is used for the actual database interaction. The serializer's methods are automatically called
based on the context (creation or update) when you use serializer.save() in the view.