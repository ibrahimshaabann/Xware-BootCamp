from rest_framework.decorators import api_view
from rest_framework.response import Response
from student.models import Student
from student.serializers import StudentSerializer
from rest_framework import status


@api_view(["GET"])  # "POST", "PUT", "PATCH", "DELETE"])
def all_students(request):
    # Student.objects.create(name = request.data['name'],
    # age = request.data['age'] ,department = request.data['department'])
    # Student.objects.create(*request.data*)
    studentsList = Student.objects.all()
    student_serializer = StudentSerializer(studentsList, many=True)
    return Response(student_serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def add_student(request):
    student_serializer = StudentSerializer(data=request.data)
    student_serializer.is_valid(raise_exception=True)
    student_serializer.save()
    return Response(student_serializer.data, status=status.HTTP_200_OK)

    

@api_view(["PUT", "PATCH", "DELETE"])
def update_student(request, id):
    student = Student.objects.filter(id=id).first()
    if student is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    partial = False
    if request.method == "PATCH":
        partial = True

    student_serializer = StudentSerializer(student, data=request.data, partial=partial)
    student_serializer.is_valid(raise_exception=True)
    student_serializer.save()    
    return Response(student_serializer.data, status=status.HTTP_200_OK)


# Create your views here.
