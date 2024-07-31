from rest_framework import viewsets
from blog.models import Post
from .serializers import MainApiSerializer

class MainModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = MainApiSerializer
