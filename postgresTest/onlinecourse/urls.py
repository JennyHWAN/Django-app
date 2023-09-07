from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.course_list, name='course_list')
]
# route is empty meaning the route url host /onlinecourse 
# will be matched to course_list view 