from django.urls import path
from visitor import views


urlpatterns = [
    path('visitors/', views.visitors, name= 'get-or_post'),
    path('visitors/<int:search_id>', views.visitor_update, name= 'get-or_post')
]