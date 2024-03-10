from django.contrib import admin
from django.utils.html import format_html

from .models import QRCode


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('url', 'qr_code_image', 'created_at', 'updated_at')
    search_fields = ('url',)

    def image_(self, obj):
        return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.qr_code_image.url))

    image_.admin_order_field = 'Изображение'

    fieldsets = (
        ('Детали QR-кода', {
            'fields': ('image_','qr_code_image','url',),
        }),
        ('Временные метки', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return QRCode.objects.exists()

    readonly_fields = ('image_','created_at', 'updated_at')

