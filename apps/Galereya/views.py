from rest_framework import viewsets
from rest_framework.response import Response
from .models import Galereya
from .serializers import GalereyaSerializer


class GalereyaViewSet(viewsets.ModelViewSet):
    queryset = Galereya.objects.all()
    serializer_class = GalereyaSerializer
