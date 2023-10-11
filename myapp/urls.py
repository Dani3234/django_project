from django.urls import path
from . import views

  
urlpatterns = [
    path('hello/<str:name>', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('index/', views.index, name='index'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
]