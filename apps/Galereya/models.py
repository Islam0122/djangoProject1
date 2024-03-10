from django.db import models

from apps.Basemodel.models import BaseModel


class Galereya(BaseModel):
    image = models.ImageField(upload_to='galereya/', verbose_name='Изображение')
    title = models.CharField(max_length=215, verbose_name='Заголовок')
    text = models.TextField(max_length=3040, verbose_name='Содержание')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
        ordering = ['created_at']
