from django.urls import path

from book import views

urlpatterns = [
    path('books/', views.BookAPIView.as_view(), name = 'all_books'),
    path('books/<int:id>', views.BookAPIView.as_view(), name = 'all_books'),
]