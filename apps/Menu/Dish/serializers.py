from rest_framework import serializers
from .models import Dish
from apps.Menu.Category.models import DishCategory


class DishSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=DishCategory.objects.all())

    class Meta:
        model = Dish
        fields = ('id', 'name', 'img', 'category', 'description', 'price',
                  'is_available', 'created_at', 'updated_at')
