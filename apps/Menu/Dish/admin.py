from django.contrib import admin
from .models import  Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name',  'price','is_available',  'created_at', 'updated_at')
    search_fields = ('name', 'category__title')
    list_filter = ('category__title','is_available',  'created_at')

    def image_(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.img.url))

    image_.admin_order_field = 'Изображение'
    fieldsets = (
        ('Основная информация', {
            'fields': ('image_', 'img', 'name', 'category', 'description', 'price','is_available', ),
        }),

        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('image_', 'created_at', 'updated_at')
