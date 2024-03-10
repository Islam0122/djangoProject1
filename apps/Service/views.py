from rest_framework import viewsets
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer


class ServiceModelViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
