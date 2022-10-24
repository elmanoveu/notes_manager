from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import DataMixin
from .models import *
from .forms import *


class NoteHome(DataMixin, ListView):
    model = Note
    template_name = "tags/index.html"
    context_object_name = "notes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Мои заметки")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        quer = Note.objects.filter(author=self.request.user).order_by("-created_date")
        return quer

    def get_categories(self):
        return Category.objects.all()


class NoteFilter(NoteHome, ListView):
    template_name = "tags/index.html"

    def get_queryset(self):
        all_headers = []
        all_cats = [1, 2, 3, 4]
        all_favourites = [True, False]
        for n in list(Note.objects.filter(author=self.request.user)):
            all_headers.append(n.header)

        order_param = self.request.GET.getlist("order_param")[0]
        order_rule = self.request.GET.getlist("order_rule")[0]

        if (
            len(order_param) == 0
        ):  # если не задан параметр сортировки, выставляем сортировку по умолчанию
            order_result = "-created_date"
        else:
            order_result = "-" + order_param if order_rule == "desc" else order_param

        queryset = Note.objects.filter(
            category__in=all_cats
            if not self.request.GET.getlist("category")
            else self.request.GET.getlist("category"),
            header__in=all_headers
            if (
                not self.request.GET.getlist("header")
                or len(self.request.GET.getlist("header")[0]) == 0
            )
            else self.request.GET.getlist("header"),
            favourite__in=all_favourites
            if not self.request.GET.getlist("favourite")
            else self.request.GET.getlist("favourite"),
            created_date__gte="1900-01-01"
            if (
                not self.request.GET.getlist("created_date")
                or len(self.request.GET.getlist("created_date")[0]) == 0
            )
            else self.request.GET.getlist("created_date")[0],
        ).order_by(order_result)

        return queryset


def show_note(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, "tags/note.html", {"note": note})


def about(request):
    return render(request, "tags/about.html")


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = "tags/register.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("")


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "tags/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy("")


def logout_user(request):
    logout(request)
    return redirect("login")


def add_note(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            try:
                Note.objects.create(
                    **form.cleaned_data, author=request.user.get_username()
                )
                return redirect("")
            except:
                return form.add_error(None, "Ошибка добавления заметки")
    else:
        form = AddNoteForm()
    return render(
        request, "tags/addnote.html", {"form": form, "title": "Добавление заметки"}
    )


def edit_note(request, note_id):
    currow = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        form = AddNoteForm(request.POST, instance=currow)
        if form.is_valid():
            try:
                currow = form.save(commit=False)
                currow.save()
                currow.author = request.user
                return redirect("")
            except:
                return form.add_error(None, "Ошибка редактирования заметки")
    else:
        form = AddNoteForm(instance=currow)
    return render(
        request,
        "tags/editnote.html",
        {"form": form, "n": currow, "title": "Редактирование заметки"},
    )


def delete_note(request, note_id):
    if request.method == "GET":
        currow = get_object_or_404(Note, id=note_id)
        currow.delete()
    return redirect("")
