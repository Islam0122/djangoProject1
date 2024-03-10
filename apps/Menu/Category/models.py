from django.db import models

from apps.Basemodel.models import BaseModel
from django.utils.translation import gettext_lazy as _


class DishCategory(BaseModel):
    title = models.CharField(_('Категория'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Категория блюда")
        verbose_name_plural = _("Категории блюд")
        ordering = ['created_at']


class DrinkCategory(BaseModel):
    title = models.CharField(_('Категория'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Категория напитка")
        verbose_name_plural = _("Категории напитков")
        ordering = ['created_at']

