from django.contrib import admin
from django.utils.html import format_html

from apps.About_us.models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return AboutUs.objects.exists()
    def image_(self, obj):
        return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.image.url))

    image_.admin_order_field = 'Изображение'

    fieldsets = (
        ('Персональная информация', {
            'fields': ('image_', 'image', 'title','text','created_at', 'updated_at',)
        }),)

    readonly_fields = ('image_','created_at', 'updated_at')