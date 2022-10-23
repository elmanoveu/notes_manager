from django.db.models import Count
from .models import *


menu = [{'title': "О сайте", 'url_name': 'about'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        # notes = Note.objects.annotate(Count('id'))

        user_menu = menu.copy()
        #if not self.request.user.is_authenticated:
        #    user_menu = []

        context['menu'] = user_menu
        # context['notes'] = notes

        return context
