from rest_framework import viewsets
from rest_framework.response import Response
from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
