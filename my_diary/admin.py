# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Diary, Page


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'created_at', 'modified_at', 'deleted_at')
    list_filter = ('user', 'created_at', 'modified_at', 'deleted_at')
    date_hierarchy = 'created_at'


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'diary',
        'notes',
        'initial_tasks_number',
        'total_tasks_number',
        'done_tasks_number',
        'created_at',
        'modified_at',
        'deleted_at',
    )
    list_filter = ('diary', 'created_at', 'modified_at', 'deleted_at')
    date_hierarchy = 'created_at'
