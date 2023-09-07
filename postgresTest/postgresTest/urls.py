"""
URL configuration for postgresTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

''' 
last line of the urlpatterns adds the path obj to reference the onlinecourse app's url conf
so when django recieves any urls with the suffix 'onlinecourse/' 
it will try to match any urls in onlinecourse.urls.py file
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    # write your code here:
    path('onlinecourse/', include('onlinecourse.urls')),
]
