from rest_framework import viewsets, filters
from .models import Post
from .serializers import PostSerializer
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend



class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    filterset_class = PostFilter
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['publish_date']
    search_fields = ['fname', 'lname']




