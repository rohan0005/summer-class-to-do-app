from django.urls import path
from . import views

urlpatterns =[

    # path('', views.index)
    path('', views.index),
    path('addtodolist/', views.addtodolist, name='addtodolist'),
    path('viewToDo/', views.viewToDo, name='viewToDo'),
    path('completedList/', views.completedList, name='completedList'),
    path('completedTodo/<int:id>/', views.completedTodo, name='completedTodo'),
    path('deleteToDo/<int:id>/', views.deleteToDo, name='deleteToDo'),
    path('deleteFromComplete/<int:id>/', views.deleteFromComplete, name='deleteFromComplete'),
    
    
    # for updating data
    
    path('addtodolist/<int:id>/', views.updateToDoList, name='addtodolist'),

]