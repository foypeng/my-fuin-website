from django.contrib import admin
from .models import Series


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """设备系列管理类"""
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
