# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "postgresTest.settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from onlinecourse.models import *

def clean_data():
    Course.objects.all().delete()

def populate_courses():
    # Add Courses
    course_cloud_app = Course(name="Cloud Application Development with Database",
                              description="Develop and deploy application on cloud")
    course_cloud_app.save()
    course_python = Course(name="Introduction to Python",
                           description="Learn core concepts of Python and obtain hands-on "
                                       "experience via a capstone project")
    course_python.save()
    print("Course objects saved... ")

clean_data()
populate_courses()