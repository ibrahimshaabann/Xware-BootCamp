from django.urls import path
from Students.views import StudentList, StudentRetrieve, StudentCreation, StudentDelete, StudentUpdate

urlpatterns=[
    path('StudentsList/', StudentList.as_view(), name='StudentList'),
    path('StudentRetrieve/<int:pk>/', StudentRetrieve.as_view(), name='StudentRetrieve'),
    path('StudentCreation/', StudentCreation.as_view(), name='StudentCreation'),
    path('StudentUpdate/<int:pk>/', StudentUpdate.as_view(), name='StudentUpdate'),
    path('StudentDelete/<int:pk>/', StudentDelete.as_view(), name='StudentDelete')

]