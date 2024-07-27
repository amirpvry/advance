from .serialaizers import PostSerializer, CategorySerializer
from blog.models import Post, Categories
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .paginations import LargeResultsSetPagination

"""'
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == "GET":
       
        posts = Post.objects.filter(status = True)
        serialaizers = PostSerializer(posts, many=True)
        return Response(serialaizers.data)
    elif request.method == "POST":
        serialaizers = PostSerializer(data=request.data)
        serialaizers.is_valid(raise_exception= True)
        serialaizers.save()
        return Response(serialaizers.data,)
        
@api_view(["GET" , "PUT" , "DELETE"])
@permission_classes([IsAuthenticated])
def postDetail(request , id):
   post = get_object_or_404(Post , pk=id ,status= True )
   if request.method == "GET":
       serialaizers = PostSerializer(post)
       return Response(serialaizers.data)
   elif request.method == "PUT":
       serialaizers = PostSerializer(post,data=request.data)
       if serialaizers.is_valid():
           serialaizers.save()
           return Response(serialaizers.data)
       return Response(serialaizers.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
       post.delete()
       return Response( {"details":"post was deleted"} , status=status.HTTP_204_NO_CONTENT)
   
""" ""


class PostViewSetModel(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "status": ["exact", "in"],
        "categories": ["exact"],
        "content": ["exact"],
    }
    search_fields = ["title"]
    ordering_fields = ["create_date"]
    pagination_class = LargeResultsSetPagination


class CategorySetModel(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()
