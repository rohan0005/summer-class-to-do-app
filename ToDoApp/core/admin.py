from django.contrib import admin

from .models import *


# Register your models here.
class newList(admin.ModelAdmin):
    list_display = ('title','priorityIs','endDate', 'description')




admin.site.register(AddToListModel, newList)


class cmpList(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(CompletedListModel, cmpList)