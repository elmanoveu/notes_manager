from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('note/<int:note_id>/', notes, name='note'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
