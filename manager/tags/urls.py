from django.urls import path
from .views import *

urlpatterns = [
    path('', NoteHome.as_view(), name=''),
    path('note/<int:note_id>/', show_note, name='note'),
    path('addnote/', add_note, name='addnote'),
    path('editnote/<int:note_id>/', edit_note, name='editnote'),
    path('deletenote/<int:note_id>', delete_note, name='deletenote'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('about/', about, name='about'),
]
