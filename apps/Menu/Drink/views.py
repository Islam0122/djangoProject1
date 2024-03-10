from rest_framework import viewsets
from rest_framework.response import Response
from .models import Drink
from .serializers import DrinkSerializer


class DrinkModelViewSet(viewsets.ModelViewSet):
    serializer_class = DrinkSerializer

    def get_queryset(self):
        return Drink.objects.filter(is_available=True)
