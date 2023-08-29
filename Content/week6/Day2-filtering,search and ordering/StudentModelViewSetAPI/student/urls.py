from django.urls import path,include
from student.views import StudenViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudenViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('Student/', StudenViewSet.as_view({
#         'get':'list',
#         'post':'create',   
#     }  
#     )),
#     path ('Student/<int:pk>/', StudenViewSet.as_view(
#         {
#             'get_by_id':'retrieve',
#             'put':'update',
#             'patch':'partial_update',
#             'delete':'destroy'
#         }
#     ))
# ]

# """
#     A viewset that provides default `create()`, `retrieve()`, `update()`,
#     `partial_update()`, `destroy()` and `list()` actions.
# """