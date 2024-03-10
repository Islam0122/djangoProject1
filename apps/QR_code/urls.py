from django.urls import path
from .views import QRCodeModelViewSet

qrcode_list = QRCodeModelViewSet.as_view({'get': 'list',})
qrcode_detail = QRCodeModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})

urlpatterns = [
    path('', qrcode_list, name='qrcode-list'),
]