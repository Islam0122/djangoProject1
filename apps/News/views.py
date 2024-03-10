from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
