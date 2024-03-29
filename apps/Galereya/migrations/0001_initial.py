# Generated by Django 4.2.11 on 2024-03-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Galereya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('image', models.ImageField(upload_to='galereya/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=215, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
                'ordering': ['created_at'],
            },
        ),
    ]
