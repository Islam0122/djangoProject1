from rest_framework import viewsets
from rest_framework.response import Response
from .models import Dish
from .serializers import DishSerializer


class DishModelViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.filter(is_available=True)
    serializer_class = DishSerializer
