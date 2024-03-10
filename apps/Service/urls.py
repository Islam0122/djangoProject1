from django.urls import path
from .views import ServiceModelViewSet

service_list = ServiceModelViewSet.as_view({'get': 'list',})
service_detail = ServiceModelViewSet.as_view({'get': 'retrieve', })

urlpatterns = [
    path('services/', service_list, name='service-list'),
    path('services/<int:pk>/', service_detail, name='service-detail'),
]