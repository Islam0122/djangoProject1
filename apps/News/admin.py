from django.contrib import admin
from django.utils.html import format_html

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at','updated_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title', 'created_at', 'updated_at')
    def image_(self, obj):
        return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.image.url))

    image_.short_description = 'Изображение'
    image_.allow_tags = True

    fieldsets = (
        (None, {
            'fields': ('image_','image','title', 'content', )
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['image_','created_at', 'updated_at']
