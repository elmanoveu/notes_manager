# Generated by Django 4.1.2 on 2022-10-13 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Заметки', 'verbose_name_plural': 'Заметки'},
        ),
    ]
