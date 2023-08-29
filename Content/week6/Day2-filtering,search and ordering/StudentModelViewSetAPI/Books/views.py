from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from Books.models import Book
from Books.serializers import BookSerializer
from .filters import BookFilter


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
  
  
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

