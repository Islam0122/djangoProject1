from django.contrib import admin

from apps.Menu.Category.models import DishCategory,DrinkCategory


@admin.register(DishCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(DrinkCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
