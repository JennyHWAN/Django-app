from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def course_list(request):
    # course = Course.objects.get(pk=6) 
    # pk stands for primary key and won't be duplicated even if you delete data,
    # so be carful each time you insert data in database
    course = Course.objects.get(name='Cloud Application Development with Database')
    template = '<html>' \
        "<body>The first course we created is `%s.`" \
        "</body>" \
        "</html>" % course.name
    return HttpResponse(content=template) # return it to the UI