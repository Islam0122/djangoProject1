from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from apps.Basemodel.models import BaseModel
from apps.Menu.Category.models import DrinkCategory
from apps.Menu.Dish.models import menu_image_path


class Drink(BaseModel):
    name = models.CharField(_('Название напитка'), max_length=100)
    img = models.ImageField(_('Изображение '), upload_to=menu_image_path, blank=True, null=True)
    category = models.ForeignKey(DrinkCategory, on_delete=models.CASCADE, related_name='menu_items',
                                 verbose_name=_('Категория'))
    description = models.TextField(_('Описание напитка'), blank=True, null=True)
    volume = models.CharField(_('Объем'), max_length=100, blank=True, null=True)
    price = models.CharField(_('Цена'), max_length=100)
    is_available = models.BooleanField(_('Доступно'), default=True)

    class Meta:
        verbose_name = _("Напиток")
        verbose_name_plural = _("Напитки")
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} - {self.volume}-{self.price}'
