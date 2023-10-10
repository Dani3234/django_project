from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

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
    return render(request, 'Projects.html',{
        'projects':projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):

    if request.method == 'GET':

        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    
    else:
        Task.objects.create(title = request.POST['title'], description = request.POST['description'], Projectkey = 2)
        redirect('/tasks/')

def create_project(request):
    if request.method == 'GET':

        return render(request, 'create_project.html',{
            'Project': CreateNewProject()
        })
    
    else:
        Project.objects.create(name = request.POST['name'])
        redirect('/projects/')