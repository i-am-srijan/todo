from django.contrib import admin
from . models import Task


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_completed', 'updated_at') # this is from model of todo app
    search_fields = ('task',) # this help to search task field of model in admin
    
admin.site.register(Task, TaskAdmin)

