from django.db import models
from django.urls import reverse


class Note(models.Model):
    id = models.IntegerField
    header = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('note', kwargs={'note_id': self.id})

    class Meta:
        verbose_name = 'Заметки'
        verbose_name_plural = 'Заметки'
