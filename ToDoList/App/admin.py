from django.contrib import admin
# from App.models import Task
# # Register your models here.
# admin.site.register(Task)
from .models import * 
# Register your models here.

@admin.register(Task)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title','desc', 'time')