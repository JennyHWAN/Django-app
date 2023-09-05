# For lab2
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