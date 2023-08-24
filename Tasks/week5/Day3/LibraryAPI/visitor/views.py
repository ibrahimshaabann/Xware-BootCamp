from django.shortcuts import render
from rest_framework.decorators import api_view
from visitor.models import Visitor
from visitor.serializers import VisitorSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def visitors (request):
    if request.method == "GET":
        visitors_querySet = Visitor.objects.all()
        visitor_serializer= VisitorSerializer(data=visitors_querySet, many=True)
        print(dir(visitor_serializer)) # all attribute of visitor_serializer
        visitor_serializer.is_valid()
        return Response(visitor_serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        visitor_serializer = VisitorSerializer(data=request.data)
        visitor_serializer.is_valid(raise_exception=True)
        visitor_serializer.save()
        return Response( f"Object Added Successfully {visitor_serializer.data}" , status=status.HTTP_200_OK)
    
        
@api_view(["PUT", "PATCH", "DELETE"])
def visitor_update(request, search_id):
    visitor = Visitor.objects.filter(id = search_id).first()

    if visitor is None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="DELETE":
        visitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    partial = False
    if request.method == "PATCH":
        partial = True

    visitor_serializer = VisitorSerializer(visitor, data=request.data, partial=partial)
    visitor_serializer.is_valid(raise_exception=True)
    visitor_serializer.save()

    # vistor_seriazlizer.data contains the new updated data in the
    return Response(visitor_serializer.data, status=status.HTTP_200_OK)


# @api_view(["GET"])  # "POST", "PUT", "PATCH", "DELETE"])
# def all_students(request):
#     # Student.objects.create(name = request.data['name'],
#     # age = request.data['age'] ,department = request.data['department'])
#     # Student.objects.create(*request.data*)
#     studentsList = Student.objects.all()
#     student_serializer = StudentSerializer(studentsList, many=True)
#     return Response(student_serializer.data, status=status.HTTP_200_OK)

# @api_view(["POST"])
# def add_student(request):
#     student_serializer = StudentSerializer(data=request.data)
#     student_serializer.is_valid(raise_exception=True)
#     student_serializer.save()
#     return Response(student_serializer.data, status=status.HTTP_200_OK)

    

# @api_view(["PUT", "PATCH", "DELETE"])
# def update_student(request, id):
#     student = Student.objects.filter(id=id).first()
#     if student is None:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "DELETE":
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     partial = False
#     if request.method == "PATCH":
#         partial = True

#     student_serializer = StudentSerializer(student, data=request.data, partial=partial)
#     student_serializer.is_valid(raise_exception=True)
#     student_serializer.save()    
#     return Response(student_serializer.data, status=status.HTTP_200_OK)


# Create your views here.

# Create your views here.