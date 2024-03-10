from rest_framework import viewsets
from rest_framework.response import Response
from .models import DishCategory, DrinkCategory
from .serializers import DishCategorySerializer, DrinkCategorySerializer

class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer


class DrinkCategoryViewSet(viewsets.ModelViewSet):
    queryset = DrinkCategory.objects.all()
    serializer_class = DrinkCategorySerializer


