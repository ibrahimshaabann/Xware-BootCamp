# Connect your project to postgres

### Install Required Dependencies

Install Python, pip, PostgreSQL, and related dependencies:

```shell
sudo apt update
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

### Create PostgreSQL Database and User

Access the PostgreSQL shell and create a database and user:

```shell
sudo -u postgres psql
```

```sql
CREATE DATABASE myproject;
CREATE USER myproject_user WITH PASSWORD 'myproject_database_password';
ALTER ROLE myproject_user SET client_encoding TO 'utf8';
ALTER ROLE myproject_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE myproject_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myproject_user;
\q
```

### Set Up Virtual Environment

Install virtualenv, create a project directory, and set up a virtual environment:

```shell
pip install virtualenv
mkdir ~/myproject
cd ~/myproject
python3 -m virtualenv myprojectenv
source myprojectenv/bin/activate
```

### Install Django and psycopg2

Install Django and psycopg2 inside the virtual environment:

```shell
pip install Django psycopg2
```

### Start a Django Project

Create a new Django project:

```shell
django-admin startproject myproject .
```

### Configure Database Settings

Edit the Django project's settings to configure the database. Open `~/myproject/myproject/settings.py` in a text editor and add the following database settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myproject_user',
        'PASSWORD': 'myproject_database_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### Apply Migrations

Apply database migrations to create the database schema:

```shell
cd ~/myproject
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser

Create a superuser account for admin access:

```shell
python manage.py createsuperuser
```

### Allow Incoming Connections

Allow incoming connections on port 8000 if you plan to use the development server:

```shell
ufw allow 8000
```

### Run the Django Development Server

Start the Django development server to run your project:

```shell
python manage.py runserver 0.0.0.0:8000
```

