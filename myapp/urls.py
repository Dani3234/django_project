from django.urls import path
from . import views

  
urlpatterns = [
    path('hello/<str:name>', views.hello),
    path('about/', views.about),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('index/', views.index),
    path('create_task/', views.create_task),
    # path('create_project/', views.create_project),
]