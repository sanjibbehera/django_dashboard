# django_dashboard
My first project on Django ORM using python 3.7.4, Django 2.2.5 and postgres 11 as DB to create custom project dashboard

Tasks done so far. I used both OS (CentOS and Windows) for this.
Install Python 3.7.4 in both Windows 10 and CentOS 7

First install related modules using pip.
create a virtual environment for django (pip install virtualenv).

Once the environment is ready, activate it using the activate command.

Then use pip to install django.

Once installed, use django-admin to create your base project and then create your application.
django-admin startproject <project_name>
python manage.py startapp <app_name>

Additional Modules to be installed for the app's requirement.
pip install psycopg2    ## Required to connect to Postgres DB.
pip install djangorestframework   # Required to use CRUD operations via REST Framework.
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install django-crispy-forms  # Additional requirement to use Bootstrap in Django.
