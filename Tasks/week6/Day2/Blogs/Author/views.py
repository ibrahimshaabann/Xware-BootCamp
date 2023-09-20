from django.shortcuts import render
from rest_framework import viewsets
from .models import Author
from Author.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    
# Create your views here.
