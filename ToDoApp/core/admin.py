from django.contrib import admin

from .models import AddToListModel

# Register your models here.
class newList(admin.ModelAdmin):
    list_display = ('title','priorityIs','endDate', 'description')




admin.site.register(AddToListModel, newList)
