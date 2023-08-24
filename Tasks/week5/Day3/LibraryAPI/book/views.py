from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from book.models import Book
from book.serializers import BookSerializer
from rest_framework import generics
#objct 404



class BookAPIView(APIView):
    
    def get(self, request, id):
        
        if id:
            book = Book.objects.filter(id=id).first()
            book_serializer = BookSerializer(book)

        # Question: why this get method excutes create method in BookSerializer?

        # We used .values() here to tourn the query set into list of dictionary objects

        else:
            book_querySet = Book.objects.all()        
            # note that when you call get method you  dont need to call .save() or .is_valid
            # many is passed to **kwargs
            book_serializer = BookSerializer(book_querySet, many = True)
            # book_serializer.is_valid(raise_exception=True)
            # book_serializer.save() note that .save creates 
     
        # sometimes we want te return the data again to the front end to do operations on it so we return it with response
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        book_serializer = BookSerializer(data = request.data)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    
    def put (self, request, id):
        book = Book.objects.filter(id=id).first()
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        book_serializer = BookSerializer(book,data = request.data)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    
    def patch (self, request, id):
        book = Book.objects.filter(id=id).first()
        print(book)
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        book_serializer = BookSerializer(book, data = request.data, partial = True)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response(book_serializer.data, status=status.HTTP_200_OK)
        

    
    def delete (self, request, id):
        book = Book.objects.filter(id=id).first()
        if book is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        book.delete()
        return Response(f"Delted", status=status.HTTP_204_NO_CONTENT)
        
        

        



# Create your views here.
