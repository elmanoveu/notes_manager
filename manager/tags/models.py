from django.db import models
from django.urls import reverse


all_categories = (('Ссылка', 'Ссылка'), ('Заметка', 'Заметка'), ('Памятка', 'Памятка'), ('TODO', 'TODO'))


class Note(models.Model):
    id = models.IntegerField
    header = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    favourite = models.BooleanField(default=False, verbose_name='Избранное')
    author = models.CharField(max_length=255, default='', verbose_name='Автор')

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('note', kwargs={'note_id': self.id})

    def get_edit_url(self):
        return reverse('editnote', kwargs={'note_id': self.id})

    class Meta:
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметки'


class Category(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=255, choices=all_categories, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
