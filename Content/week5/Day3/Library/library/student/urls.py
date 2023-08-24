from django.urls import path
from . import views
urlpatterns = [
    path('Students/', views.all_students, name="Students"),
    path('update_student/<int:id>/', views.update_student, name="update_student"),
    path('add_student/', views.add_student, name="add_student"),
]