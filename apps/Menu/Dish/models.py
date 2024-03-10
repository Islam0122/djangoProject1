from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.Basemodel.models import BaseModel
from apps.Menu.Category.models import DishCategory as Category


def menu_image_path(instance, filename):
    return f'menu_images/{slugify(instance.name)}/{timezone.now().strftime("%Y%m%d%H%M%S")}_{filename}'

class Dish(BaseModel):
    name = models.CharField(_('Название блюда'), max_length=100)
    img = models.ImageField(_('Изображение '), upload_to=menu_image_path, blank=True, null=True)
    category = models.ManyToManyField(Category,verbose_name='Категория')
    description = models.TextField(_('Описание блюда'), max_length=200, blank=True, null=True)
    price = models.CharField(_('Цена'), max_length=100)
    is_available = models.BooleanField(_('Доступно'), default=True)

    class Meta:
        verbose_name = _("Блюдо")
        verbose_name_plural = _("Блюда")
        ordering = ['created_at']

    def __str__(self):
        return f'{self.name} - {self.price}'
