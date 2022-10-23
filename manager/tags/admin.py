from django.contrib import admin
from .models import *


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'created_date', 'category', 'favourite', 'author')
    list_display_links = ('id', 'header')
    search_fields = ('header', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
