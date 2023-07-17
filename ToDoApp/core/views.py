from datetime import datetime

# FOR PAGENATION
from django.core.paginator import Paginator

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import AddToListModel
from .models import *



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
    
    
    # receiving all data from model
    toDoListData = AddToListModel.objects.all()
    
    # showing just 2 lists to user
    paginator= Paginator(toDoListData,2)
    
    # Requesting current page number
    page_number= request.GET.get('page')
    
    #  retrieve the specified page number
    toDoListData_page=paginator.get_page(page_number)
    
    # total number of pages in the pagination object--- used for last page
    totalpage=toDoListData_page.paginator.num_pages
    
    
    
    context = {
        
        'toDoListData': toDoListData_page,
        
        # 'toDoListData_page': ,
        'last_page': totalpage,
        'page_list': [n+1 for n in range(totalpage)]
        
        
    }  

    return  render(request=request, template_name='viewToDo.html', context=context)




def deleteToDo(request, id):
    
    dele = AddToListModel.objects.get(id=id)
    dele.delete()
    
    return redirect('viewToDo')


def completedTodo(request, id):
    
    comp = AddToListModel.objects.get(id=id)
    
    
     # Creating new completed task instance
    completed_task = CompletedListModel(title=comp.title, description=comp.description)
    completed_task.save()
    
    
    
    
    # FOR PAGINATION
    
      
    
    # receiving all data from model
    toDoListData = CompletedListModel.objects.all()
    
    # showing just 2 lists to user
    paginator= Paginator(toDoListData,2)
    
    # Requesting current page number
    page_number= request.GET.get('page')
    
    #  retrieve the specified page number
    toDoListData_page=paginator.get_page(page_number)
    
    # total number of pages in the pagination object--- used for last page
    totalpage=toDoListData_page.paginator.num_pages
    
    
    #If user clicks complete button
    
    
    
    context = {
        
        'CompletedListModel': toDoListData_page,
        
        # 'toDoListData_page': ,
        'last_page': totalpage,
        'page_list': [n+1 for n in range(totalpage)]
        
        
    }  
    
    return redirect('viewToDo')

    
 
 
def completedList(request):
    
    return  render(request=request, template_name='completedList.html')
    
 
 
 
 
 