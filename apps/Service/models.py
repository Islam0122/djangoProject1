from django.db import models
from apps.Basemodel.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Service(BaseModel):
    title = models.CharField(_('Название сервиса'), max_length=100)
    description = models.TextField(_('Описание сервиса'))
    price = models.CharField(_('Стоимость'), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("Сервис")
        verbose_name_plural = _("Сервисы")

    def __str__(self):
        return self.title
