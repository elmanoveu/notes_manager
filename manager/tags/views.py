from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    notes = Note.objects.all()
    return render(request, 'tags/index.html', {'notes': notes, 'title': 'Мои заметки'})


def notes(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'tags/note.html', {'note': note})


def login(request):
    return HttpResponse('Логин')


def register(request):
    return HttpResponse('Регистрация')
