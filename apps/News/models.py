from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.Basemodel.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
    content = models.TextField(verbose_name=_('Содержание'))
    image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name=_('Изображение'))

    class Meta:
        verbose_name = _('Новости')
        verbose_name_plural = _('Новости')
        ordering = ['-created_at']

    def __str__(self):
        return self.title
