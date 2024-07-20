from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from . import models
from  django.db.models import Count
# Register your models here.


admin.site.register(models.Category)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    
    
    list_display=[
        'title',
        'satutes',
        'category',
        'user',
        'created_at',
        'tasks_count'
    ]
    list_editable=['satutes','category']
    list_per_page=10
    list_select_related=['category','user']
    def tasks_count(self,obj):
        return obj.tasks_count

    def get_queryset(self, request) :
        query=super().get_queryset(request)
        query=query.annotate(tasks_count=Count('task'))
        return query
    

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'project',
        'descreption',
        'is_completed',
        ]
    list_editable=['is_completed']
