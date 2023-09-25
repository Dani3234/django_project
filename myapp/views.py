from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task


# Create your views here.

def hello(request, name):
    return HttpResponse("hello %s" % name)

def about(request):
    username = "dani"
    return render(request, 'about.html',{
        'username': username
    })

def index(request):
    return render(request, 'index.html')

def projects(request):
    projects = Project.objects.all()
    # return HttpResponse("Projects: %s" % project)
    return render(request, 'Projects.html',{
        'projects':projects
    })

def tasks(request):
    tasks = Task.objects.all()
    # return HttpResponse("Tasks: %s" % task)
    return render(request, 'tasks.html',{
        'tasks': tasks
    })