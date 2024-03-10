from rest_framework import serializers
from .models import Galereya


class GalereyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galereya
        fields = ('id', 'image', 'title', 'text', 'created_at', 'updated_at')
