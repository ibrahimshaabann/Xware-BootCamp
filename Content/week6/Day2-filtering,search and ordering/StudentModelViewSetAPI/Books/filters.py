import django_filters
from Books.models import Book


class BookFilter(django_filters.FilterSet):
    borrowed_book__published_year = django_filters.NumberFilter(field_name='borrowed_book__published_year',lookup_expr='gt')
       
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'available']


