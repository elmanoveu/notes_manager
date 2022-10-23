from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import DataMixin
from .models import *
from .forms import *


class NoteHome(DataMixin, ListView):
    model = Note
    template_name = 'tags/index.html'
    context_object_name = 'notes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мои заметки")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)


def show_note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'tags/note.html', {'note': note})


def about(request):
    return render(request, 'tags/about.html')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'tags/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'tags/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('')


def logout_user(request):
    logout(request)
    return redirect('login')


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            try:
                Note.objects.create(**form.cleaned_data, author=request.user.get_username())
                return redirect('')
            except:
                return form.add_error(None, 'Ошибка добавления заметки')
    else:
        form = AddNoteForm()
    return render(request, 'tags/addnote.html', {'form': form, 'title': 'Добавление статьи'})

"""
class AddNote(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddNoteForm
    template_name = 'tags/addnote.html'
    success_url = reverse_lazy('')
    login_url = reverse_lazy('')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление заметки")
        return dict(list(context.items()) + list(c_def.items()))
"""