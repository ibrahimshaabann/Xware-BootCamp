from django.shortcuts import render
from rest_framework import generics

from Students.models import Student
from Students.serializers import StudentSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class StudentRetrieve(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreation(generics.CreateAPIView):
    serializer_class = StudentSerializer


class StudentUpdate(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDelete(generics.DestroyAPIView):
    queryset = Student.objects.all()


 
# Create your views here.
