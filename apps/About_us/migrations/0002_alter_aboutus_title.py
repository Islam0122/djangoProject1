# Generated by Django 4.2.11 on 2024-03-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About_us', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.CharField(max_length=2155, verbose_name='Заголовок'),
        ),
    ]
