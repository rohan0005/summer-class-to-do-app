from django.urls import path
from . import views

urlpatterns =[

    # path('', views.index)
    path('', views.index),
    path('addtodolist/', views.addtodolist, name='addtodolist'),
    path('viewToDo/', views.viewToDo, name='viewToDo'),
    path('completedTodo/', views.completedTodo, name='completedTodo'),
    # path('savedmessage/', views.savedmessage, name='savedmessage'),



]