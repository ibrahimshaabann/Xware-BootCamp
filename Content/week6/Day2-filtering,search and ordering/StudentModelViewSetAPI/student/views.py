from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from student.models import Student
from student.serializerls import StudentSerializer
from .filters import StudentFilter




"""
    Parent Classes:  GenericAPIView ->  ModelViewSet-> GenericViewSet -> ModelViewSet
    
    The ModelViewSet parent class contains the next methods that you can override: 
        - def get_queryset(self):
        - def get_object(self):
        - def get_serializer(self, *args, **kwargs):
        - def get_serializer_class(self):

"""


class StudenViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
   
    # if we wrote the next lines, then we need to include the[DjangoFilterBackend] in the 
    filterset_class = StudentFilter

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter) # Note that it doesn't have to be a list , it can be dictionary
    ordering_fields = ['age'] # Params names in the URL ------> key: ordering, value: age
   
    # Params names in the URL ------> key: search, value: name or any character to search for
    search_fields = ['name'] # can also be ['first_name', 'last_name']

    ## ----------> This method is used when we want to apply a specific filter to the class
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = StudentFilter


    # def get_queryset(self):
    #     """
    #         Here we override the get_queryset method
    #     """
    #     name = self.request.query_params.get('name', None)
    #     age = self.request.query_params.get('age', None)
    #     if name:
    #         queryset = self.queryset.filter(name__icontains=name)

    #     if age:
    #         queryset = self.queryset.filter(age__gt=age)
        

    #     return queryset 



    # class UserLoginView(generics.CreateAPIView):
    # def post(self, request, *args, **kwargs):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     user = authenticate(username=username, password=password)
    #     if user:
    #         token, created = Token.objects.get_or_create(user=user)
    #         return Response({'token': token.key})
    #     else:
    #         return Response({'error': 'Invalid credentials'}, status=400)

