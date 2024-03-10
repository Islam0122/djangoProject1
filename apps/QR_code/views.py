from rest_framework import viewsets
from rest_framework.response import Response
from .models import QRCode
from .serializers import QRCodeSerializer


class QRCodeModelViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer
