# Generated by Django 4.2.10 on 2024-02-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QR_code', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='url',
            field=models.CharField(max_length=180, unique=True, verbose_name='URL или Текст '),
        ),
    ]
