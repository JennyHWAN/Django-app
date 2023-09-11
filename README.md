# Django-app
This is created during learning Coursera course: IBM Full-stack development.

`lab1_template` is this course's code template.

<!-- <p align='center'>Content of this repo:</p> -->
**Content of this repo:**
<!-- <ol>
<li>
<a href='#start-django-project-with-a-databasepostgresql--for-postgrestest-folder'> Start django project with a database postgreSQL
</li>
</ol> -->
1. [postgresTest](#postgrestest)

## postgresTest
**Description: Start Django Project with a database(PostgreSQL)**

#### First part refers to: [Medium blog](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)
- clone this repo: `git clone git@github.com:JennyHWAN/Django-app.git`
- enter the repo dir: `cd Django-app`
- build virtual env for this dir: `python -m venv env`, where env is your virtual environment name
ps. I've used `virtualenv` in place of `venv`, the functionality are similar but differ in implementation, where venv is a built-in module in python3 but virtualenv is a third-party tool
- activate virtual env: `source env/bin/activate` (for mac) I don't know for sure but maybe for windows users just execute: `env/scripts/activate`
- in this virtual environment: `pip install django`, and you could run `pip freeze` to check the version
- create a django project: `django-admin startproject postgresTest`, which is a container for django apps and settings.
- start this project: `python manage.py startapp testdb` which will create a folder called testdb. You could run `python manage.py runserver` to make sure it's good to run. Then run `python manage.py`.

#### Second part refers to: IBM Full stack course
- All the same but not in a virtual env, just your local machine:
    ```
    $ pip install django
    $ django-admin startproject postfresTest
    ```
- The main file that django created for you:
    ```
    postgresTest/ # django project
        manage.py
        postgresTest/
            __init__.py
            settings.py # 
            urls.py
            ...
    ```
    For *project-related* files:
    <ol>
    <li><code>manage.py</code> is the command line interface that's used to interact with the django project to start the server, migrate models and so on, where django project is the same as a python package.</li>
    <li><code>settings.py</code> contains the settings and configurations for your django project.</li>
    <li><code>urls.py</code> contains the url and routing definitions of your django apps within the project.</li>
    </ol>
- Inside postgresTest project directory, run `python manage.py startapp onlinecourse` and django will create a temp app structure and some important app files.
- About onlinecourse:
    ```
    onlinecourse/
        __init__.py
        admin.py
        models.py
        views.py
        urls.py
        apps.py
        migrations/
        ...
    ```
    For *app-related* files:
    <ol>
    <li><code>admin.py</code> includes everything you need to create and customize the admin site to manage user and content.</li>
    <li><code>models.py</code> contains the data models and orm</li>
    <li><code>views.py</code> contains view functions and classes to create views.</li>
    <li><code>urls.py</code> contains URL declarations and routings for the app.</li>
    <li><code>apps.py</code> contains the application configurations class.</li>
    <li><code>migrations</code> folder contains scripts for model migration.</li>
    </ol>
- Include Django app to project: In `postgresTest/postgresTest/settings.py` find `INSTALLED_APPS` setting, add: `onlinecourse.apps.OnlinecourseConfig` to the list.
- Setup database: also in `settings.py`, find `DATABASE` seetting, add database settings.
- Till now, we have set up our app and database, we can define our django models as the orm components between objs and tables
- Edit `onlinecourse/models.py` and perform migrations to create necessary db tables: `python manage.py makemigrations onlinecourse`, (if you want to check the auto generated SQL, run `python manage.py sqlmigrate onlinecourse 0001`) then run the migration scripts: `python manage.py migrate`. Then you could find this `onlinecourse_course` table in your connected database, in my case: 
    ```
    $ psql
    $ \c test
    $ \dt
    ```
- Create a simple view and a hard-coded html template to present the course obj: inside of `onlinecourse/views.py`. 

    **Note:** view is for receiving HTTPRequest and return a HTTPResponse wrapping a simple HTML page as its content
- Then we assiciate the course view with the url so django will route the request url to the view to be handled. URL routes are defined in a `url.conf` for each app as well as for the django project, to create a `url.conf` file for onlinecourse app, we first create `onlinecourse/urls.py`, where add a `path` obj to point a url route to the course_list view we created.
- Next we point the route url conf file of `onlinecourse` app to the projects url conf file: `postgresTest/postgresTest/urls.py`. 
- (Added by myself) In order to get the server run, you need to add data in `Course` model since the output in `views.py` needs the `course.name`, so similiar to the following labs, add `write.py` in the root `postgresTest` folder (same as `manage.py`'s route). Note that we need to change the `os.environ.setdefault`'s second parameter to `postgresTest.settings` (relative route) differ from the other labs below. Finally, run `python write.py` to execute it.
- And voilà! Our django app is set up, check the result under `postgreTest/`(main) folder:
    ```
    $ python manage.py runserver
    ```
    which will start a development server locally on 127.0.0.1 with default port 8000 to host the django project and app.
    ![img](/onlinecourse.png)

## lab1_template: 
**Description: Create Django model**

reference: IBM Full stack course
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
## lab2_ormtemplate
**Description: Create a Standalone Django ORM Project Template**

reference: IBM Full stack course
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
## lab3_template (ori name: lab2_template)
**Description: CRUD operation on Django model objects**

reference: IBM Full stack course
- Download the code template for this lab:
    ```
    wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3_django_orm/lab2_template.zip"
    unzip lab2_template.zip
    rm lab2_template.zip
    ```
- Create a virtual environment and install Django and psycopg related packages: 
    ```
    pip install --upgrade distro-info
    pip3 install --upgrade pip==23.2.1
    pip install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate
    pip install Django psycopg2-binary
    ```
- Modify the `settings.py` for your own database set.
- Create models for an online course app: Modify the `crud/models.py` file. In addition to that, we override the `__str__(self)` method to create a string representation of a user object. This is convenient if you want to print a user object. Also feel free to add as many primitive fields as you like to the User model such as email or location. You could find more details about model field definitions here: [Django Model Fields](https://docs.djangoproject.com/en/3.1/ref/models/fields/)
- Next, let's add an Instructor model inherited from User model and make it as One-To-One relationship, still in `crud/models.py`. Instructor is an extension of User which adds some more instructor specific fields such as full_time and total_learners.
- Then, let's create a Course model append to `crud/models.py` which has a Many-To-Many relationship to Instructor model, defined by the reference field instructors.
- Append `crud/models.py` for Lesson model, Learner model, Enrollment model and update Course model to add a Many-To-Many relationship with Learner model via the Enrollment class (Doc Keyword: Extra fields on many-to-many relationships).
- Until now, the relationships:
    1. User and Instructor models with One-To-One relationship (Inherit)
    2. Course and Lessons models with One-To-Many relationship (set Lesson's foreign key Course)
    3. Course and Instructor with Many-To-Many relationship. (set ManyToManyField relation to Instructor under Course)
- Run migrations for the crud app to create those tables in our PostgreSQL database: `python3 manage.py makemigrations crud`. You should see Django is about to create the following tables:
    ```
    Migrations for 'crud':
      crud/migrations/0001_initial.py
        - Create model Course
        - Create model User
        - Create model Instructor
        - Create model Learner
        - Create model Lesson
        - Create model Enrollment
        - Add field instructors to course
        - Add field learners to course
    ```
- Run the migrations: `python3 manage.py migrate`
- Let's try to perform some create and delete operations on those models in `write.py`.
- Run the write.py in terminal: `python3 write.py`
- Read all courses: `read_courses.py` and run `python3 read_courses.py`
- Query instructors with filters to select subsets of instructors meeting some certain criterions in `read_instructor.py` and run: `python3 read_instructor.py`
- Query learners with filters to select subsets of learners meeting some certain criterions in `read_learners.py`
## lab4_template (ori name: lab3_template)
**Description: Activate models for an onlinecourse app**

reference: IBM Full stack course
- Download code template for lab4, remember to switch the name for the folder inside is called lab3 which is conflict with the previous lab. Ps. if you want to change the name of the file, run `mv [oldname] [newname]`:
    ```
    wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0251EN-SkillsNetwork/labs/m3_django_orm/lab3_template.zip"  
    unzip lab3_template.zip
    rm lab3_template.zip
    ```
- As usual, change the `setting.py` file to setup the database server.
- To summarize the relationships of these models:
    1. Learner and Instructor models are inherited from User model with One-To-One relationship
    2. Lesson has One-To-Many relationship with Course
    3. Instructor has Many-To-Many with Course
    4. Learner has Many-To-Many with Course model via Enrollment
- Activate the models:
    ```
    pip install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate
    pip install Django psycopg2-binary
    ```
- Then generate migration scripts for app related_objects: `python3 manage.py makemigrations related_objects` -> `python3 manage.py migrate` -> `python3 write.py`
- Making querying span relationships in `read_course_instructor.py`: 
    <ol>
    <li>Get courses taught by Instructor Yan, via both forward (explicit) and backward (implicit) access</li>
    <li>Get the instructors of Cloud app dev course</li>
    <li>Check the occupations of the courses taught by instructor Yan.</li>
    </ol>
    Then <code>python3 read_course_instructors.py</code>
- Inside `read_enrollments.py`:
    <ol>
    <li>Get the user information about learner David</li>
    <li>Get learner David information from user</li>
    <li>Get all learners for Introduction to Python course</li>
    <li>Check the occupation list for the courses taught by instructor Yan</li>
    <li>Check which courses the developer learners are enrolled in Aug, 2020</li>
    </ol>
    Then <code>python3 read_enrollments.py</code>

## Lab5_firstproject
**Description: Django app, deploy using Docker**

reference: IBM Full stack course

#### First part: a walkthrough of the workflow
- Install these must-have packages and setup the environment:
    ```
    pip install --upgrade distro-info
    pip3 install --upgrade pip==23.2.1
    pip install virtualenv
    virtualenv djangoenv
    source djangoenv/bin/activate
    ```
    In my case, I already have the virtual env called 'env', so I don't run this again, just run the last one to enter the virtual env and all the following actions will be made inside of this virtual env.

    **Note:** if you want to run the command together in single execution (using scripts), [here's](https://rowannicholls.github.io/bash/intro/myscript.html) the steps:    
    * Create the script: `touch [myscript].sh`
    * I personally use vim to edit the script: `vim [myscript].sh` and you could check the content inside using `cat [myscript].sh`
    * Done! Run `bash [myscript].sh`
    
    I created an example in `Django-app/testscript.sh`
- Install Django related pkgs:
    (inside virtual env) `pip install Django` -> create your Django **project**: `django-admin startproject lab5_firstproject` -> `cd lab5_firstproject`- > create a Django **app**: `python3 manage.py startapp firstapp`
    
    **Note**: Django created a project scaffold `lab5_firstproject/lab5_firstproject` for you containing the fundamental config and setting files for a Django project and app.
- You could just perform the migration and start the server for the plain site by: (for details, refer to previous section [postgresTest](#postgrestest))
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
    ```
- Add `'firstapp.apps.FirstappConfig',` in `lab5_firstproject/settings.py`
- In terminal: `cd firstapp` -> `touch urls.py`
- In `firstproject/urls.py`: update `from django.urls import path` to `from django.urls import path, include`, and add a new `path` entry: `path('firstapp/', include('firstapp.urls')),`
- Edit `firstapp/views.py` to receive HTTPRequest and return a HTTPResponse wrappin a html page as it's content.
- Configure the URL for the index view in `firstapp/urls.py`
- Now inside lab5_firstproject: `python3 manage.py runserver`

    **Note:** Django will map any HTTP requests starting with `/firstapp` to *firstapp* and search any matches for paths defined in `firstapp/urls.py`.

#### Second part: Containerizing the app using Docker
- The overall workflow:
    1. Create a `requirementx.txt file` [[1]](#step-1)
    2. Create a `Dockerfile` which contains instructions on how to build a Docker image [[2]](#step-2)
    3. Run `docker compose up` to create a container image, and run it
    4. Commit and push the image to a remote repo so others can run it exactly as you've configured

    **Note:** Docker images are commonly used in conjunction with Kubernetes, which is a service that manages containers.
- Modify `settings.py`, add ALLOWED_HOSTS. For detail info, check Django's [doc](https://docs.djangoproject.com/en/4.2/ref/settings/).

    **Note:** By deafult, django is configured to block all traffic from all hosts including the traffic coming from (Coursera) CloudIDE until we explicity define in them in `settings.py`.
- Appendix:
    #### Step 1.
    In the main `/lab5_firstproject` folder:
    ```
    pip install pipreqs
    pipreqs .
    ```
    where `pipreqs .` will create the `requirements.txt` file for you
    #### Step 2.
    Same directory:
    ```
    touch Dockerfile
    vim Dockerfile
    ```
    Or run `vim Dockerfile\` to check this existed file's content. 
    For details, check the `Dockerfile`, where the code will run line by line. Refer to the [doc](https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/) for how this code works.

    Open Docker, in terminal run `docker build . -t my-django-app:latest && docker run -e PYTHONUNBUFFERED=1 -p  8000:8000 my-django-app` which will take some time and create and run the container image (two commands).

    Then in Docker's container, you would find the container you just built. With this, you could share the Docker image by following these [instructions](https://docs.docker.com/get-started/04_sharing_app/).

    **Note:** docker container run is a shorthand for docker container create and docker container start. So, by definition, it creates a new container every time. ***So don't run the command again***.

    As for docker command, refer to the documentation, here's the brief case after the previous command `docker run -e PYTHONUNBUFFERED=1 -p  8000:8000 my-django-app`:
    * `docker ps` check the container id and copy it
    * `docker stop [container_id]` # eg. 72bd7003d569
    * `docker restart [container_id]`
    #### 1. Deploy with IBM Cloud Code Engine (lab5_firstproject-IBM-CE)
    - Create a project fist, follow the IBM code engine's instruction.
    - Set up your private IBM's icr [registry](https://cloud.ibm.com/registry/start) which involve some set up on your docker hub. (notyet)


    #### 2. Deploy with AWS Lambda / Zappa (lab5_firstproject-zappa-deploy)
    - Next, we are supposed to use IBM Cloud Code Engine to deploy our app, but since I ran some issue (resolved) to upgrade my IBM account so I use alternative product (whose feedback is not as good as code engine): AWS Lambda's Zappa service. (refer to [geeksforgeeks](https://www.geeksforgeeks.org/how-to-deploy-django-application-in-aws-lambda/))
    * Install aws's [CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html):
        ```
        $ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
        $ sudo installer -pkg AWSCLIV2.pkg -target /
        ```
    * Follow aws's [doc](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-started-assign-account-access-admin-user.html) to create a IAM Identity Center's user. Remember to follow best practice, don't create access keys in your root user! Enter your [AdministratorAccess account](https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html) through your specific sign-in URL, in my case: admin-jennyhuang and select `Command line or programmatic access` shown below, then configure your credential through the instructions.
    ![img](/admin-jennyhuang-console.png)
    * Run the AWS IAM Identity Center credentials (Recommended) && Option1. For Option 1, I created `aws-credentials.sh` and run `bash aws-credentials.sh` to create a session. Then you could run [AWS CLI](https://repost.aws/knowledge-center/s3-locate-credentials-error) through `aws configure list` to check your credential.

        **[Note](https://github.com/Zappa/Zappa#custom-aws-iam-roles-and-policies-for-deployment):** You can specify which local profile to use for deploying your Zappa application by defining the profile_name setting, which will correspond to a profile in your AWS credentials file that you just created, something like `aws s3 ls --profile AdministratorAccess-394349669210-as-admin-jennyhuang`
    - If some errors occurred, solve them while they come, as for me, I need to change the `s3_bucket` name to a less popular one in `zappa_settings.json` file, and DONT forget to add your domain name afterward in `settings.ALLOWED_HOSTS`, since we haven't setup CICD pipeline, we need to run `zappa update dev` afterward.
    - Then run `zappa deploy dev` to deploy.
    - Voilà, enjoy your own website `https://jqugqvg6g0.execute-api.us-east-2.amazonaws.com/dev/test`
    - **TODO:** Try to figure out how to deploy AWS [CICD](https://docs.aws.amazon.com/whitepapers/latest/docker-on-aws/cicd.html).