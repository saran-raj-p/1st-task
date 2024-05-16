from django.http import HttpResponse
from testingapp.models import Students

def student(request,r):
    try:
        sroll = Students.objects.get(roll=r)
    except:
        return HttpResponse(f"{r} not found")
    return HttpResponse(sroll.name)

def index(request):
    return HttpResponse("hello")
