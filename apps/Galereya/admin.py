from django.contrib import admin
from django.utils.html import format_html

from .models import Galereya


class GalereyaAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at','image_preview')

    def image_preview(self, obj):
        return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.image.url))

    image_preview.short_description = 'Превью изображения'
    image_preview.allow_tags = True

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'image_preview', 'image','text'),
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


admin.site.register(Galereya, GalereyaAdmin)
