# Generated by Django 4.2.11 on 2024-03-04 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Galereya', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galereya',
            name='text',
            field=models.TextField(default=1, max_length=3040, verbose_name='Содержание'),
            preserve_default=False,
        ),
    ]
