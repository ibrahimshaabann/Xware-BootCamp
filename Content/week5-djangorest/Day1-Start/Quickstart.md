## Quickstart

In this quickstart guide, we'll create a simple API to manage users and groups within a Django project.

### Project Setup

1. Create a new Django project named `tutorial` and start a new app called `quickstart`.

    ```bash
    # Create the project directory
    mkdir tutorial
    cd tutorial

    # Create a virtual environment
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

    # Install Django and Django REST framework
    pip install django
    pip install djangorestframework

    # Set up a new project with a single application
    django-admin startproject tutorial .
    cd tutorial
    django-admin startapp quickstart
    cd ..
    ```

   The project layout should look like this:

    ```
    tutorial/
    ├── manage.py
    ├── tutorial/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── quickstart/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── migrations/
        │   └── __init__.py
        ├── models.py
        ├── tests.py
        └── views.py
    ```

   Note: The application has been created within the project directory to avoid name clashes with external modules.

2. Sync the database for the first time:

    ```bash
    python manage.py migrate
    ```

3. Create an initial superuser named `admin` with the password `password123`. This user will be used for authentication later.

    ```bash
    python manage.py createsuperuser --email admin@example.com --username admin
    ```
