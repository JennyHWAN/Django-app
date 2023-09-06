# Django-app
This is created during learning Coursera course: IBM Full-stack development.

`lab1_template` is this course's code template.

## Start Django Project with a database(PostgreSQL)--for `postgresTest` folder
reference: https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
- clone this repo: `git clone git@github.com:JennyHWAN/Django-app.git`
- enter the repo dir: `cd Django-app`
- build virtual env for this dir: `python -m venv env`, where env is your virtual environment name
ps. I've used `virtualenv` in place of `venv`, the functionality are similar but differ in implementation, where venv is a built-in module in python3 but virtualenv is a third-party tool
- activate virtual env: `source env/bin/activate` (for mac) I don't know for sure but maybe for windows users just execute: `env/scripts/activate`
- in this virtual environment: `pip install django`, and you could run `pip freeze` to check the version
- create a project: `django-admin startproject postgresTest`
- start this project: `python manage.py startapp testdb` which will create a folder called testdb. You could run `python manage.py runserver` to make sure it's good to run. `python manage.py` is the command that's used to run django

## For lab1_template (reference: IBM Full stack course)
- `cd lab1_template`
- set up a virtual environment which to contain all the packages we need: `pip install virtualenv`
- `virtualenv djangoenv`
- `source djangoenv/bin/activate`
- `pip install -r requirements.txt`
- modify `orm/models.py` to create a User model, after the User model is defined, Django will be creating a corresponding database table called orm_user. The first part orm is your app name and the second part user is the model name. Whenever you make changes to your models such as creating new models or modifying existing models, you need to perform database migrations. Django provides utils via manage.py interface to help you perform migrations.
- First, you will need to generate migration scripts for orm app: `python3 manage.py makemigrations orm`
- `orm/migrations` folder is where Django stores the changes to your models.
- You may wonder what SQL statements Django has created for your model migrations: `python3 manage.py sqlmigrate orm 0001`
- Next, you can perform the migration to create orm_user table by running: `python3 manage.py migrate` and a table will be created in the database test.
![img](/create-table.png)
- test.py contains a test_setup() method to save a mockup user object, run: `python3 test.py`
## For lab2_ormtemplate (reference: IBM Full stack course)
- standalone folder acts as the container folder for an empty Django app called standalone.
- The snippet added to the `manage.py` file as the setting module of our `lab2_ormtemplate` project and be able to execute Django built-in commands such as migrations.
- Add a simple database settings to `settings.py`.
- `lab2_ormtemplate/standalone/models.py` containing model definitions and a folder named migrations containing migration scripts in standalone app.
- Then ask lab2_ormtemplate app to generate the Test table by running migration command-lines: `cd lab2_ormtemplate`
- Set up a virtual env which will contain all the packages we need:
    ```sh
    pip install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate
    ```
- Install the required pkgs:
    ```
    pip install django==4.2.4 psycopg2-binary==2.9.7
    ```
- Then generate migration scripts for standalone app: `python3 manage.py makemigrations standalone`
- run migration: `python3 manage.py migrate`
- Write some python testing code in a python script file to test my model in `lab2_ormtemplate/test.py`
- check whether the test obj was inserted correctly: `python3 test.py`