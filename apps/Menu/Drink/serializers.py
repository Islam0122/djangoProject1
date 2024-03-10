from rest_framework import serializers
from .models import Drink
from apps.Menu.Category.models import DrinkCategory

class DrinkSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=DrinkCategory.objects.all())
    class Meta:
        model = Drink
        fields = ('id', 'name', 'img', 'category', 'description',
                  'volume', 'price', 'is_available', 'created_at', 'updated_at')