from django.db import models
from apps.Basemodel.models import BaseModel


class AboutUs(BaseModel):
    image = models.ImageField(upload_to='about_us_images/', verbose_name='Изображение')
    title = models.CharField(max_length=215, verbose_name='Заголовок')
    text = models.TextField(max_length=3040, verbose_name='Содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
