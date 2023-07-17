from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import AddToListModel



# from ToDoApp.core.forms import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

def addtodolist(request):

    if request.method=='POST':
         title=request.POST.get('title')
         priorityIs=request.POST.get('priorityIs')
         endDate_str = request.POST.get('endDate')
         description=request.POST.get('description')

         endDate = datetime.strptime(endDate_str, '%H:%M %m/%d/%Y').strftime('%Y-%m-%d %H:%M')

         s=AddToListModel(title=title, priorityIs=priorityIs, endDate=endDate, description=description)
         s.save()
    return render(request, 'addtodolist.html')


def viewToDo(request):

    return  render(request, 'viewToDo.html')

def completedTodo(request):
     return render(request, 'completedList.html')

def savedmessage(request):
    return render(request, 'savedmessage.html')