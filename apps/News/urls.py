from django.urls import path
from .views import PostModelViewSet

post_list = PostModelViewSet.as_view({'get': 'list', })
post_detail = PostModelViewSet.as_view({'get': 'retrieve', })

urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:pk>/', post_detail, name='post-detail'),
]