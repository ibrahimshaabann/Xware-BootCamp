from django.urls import path
from .api_views import NotificationsModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .api_views import TokenView


urlpatterns = [
    path('notifications/', NotificationsModelViewSet.as_view(
        {
          'get':'list',
          'post':'create',  
        }
    )
    ),

    path('notifications/<int:pk>', NotificationsModelViewSet.as_view(
        {
            'get_by_id':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy'
        }
    )),
    # We can use TokenView.TokenObtainPairView())view from library instead of custom class TokenView() that we created
     path('auth/token/', TokenView.as_view()) 
      
]