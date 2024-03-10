from django.urls import path
from .views import GalereyaViewSet

urlpatterns = [
    path('', GalereyaViewSet.as_view({'get': 'list'}), name='galereya-list'),
    path('<int:pk>/', GalereyaViewSet.as_view({'get': 'retrieve'}), name='galereya-detail'),
]
