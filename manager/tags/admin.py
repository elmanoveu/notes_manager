from django.contrib import admin
from .models import *

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'created_date', 'category', 'favourite')
    list_display_links = ('id', 'header')
    search_fields = ('header', 'content')


admin.site.register(Note, NoteAdmin)
