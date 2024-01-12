from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['User','filename','file','file_type','created_at']
