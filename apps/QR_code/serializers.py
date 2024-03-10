from rest_framework import serializers
from .models import QRCode


class QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QRCode
        fields = ('id', 'url', 'qr_code_image', 'created_at', 'updated_at')
