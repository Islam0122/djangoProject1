from rest_framework import serializers
from .models import DishCategory, DrinkCategory

class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = ('id', 'title', 'created_at', 'updated_at')

class DrinkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkCategory
        fields = ('id', 'title', 'created_at', 'updated_at')