import django_filters
from student.models import Student


class StudentFilter(django_filters.FilterSet):
    # This describes the minimum published year to start with
    # The borrowed_book__published_year is the parameter name to be passed
    # This will be passed in the URL ---> ?borrowed_book__published_year=2000
    # After you type the above line in the URL this will get students who have borrowed books published after 2000
    borrowedbook_publishedyear = django_filters.NumberFilter(field_name='borrowed_book__published_year', lookup_expr='gt')

    # Type in the URL : ?name=I -------> this will show names that contain character 'i' or 'I'
    name = django_filters.CharFilter(lookup_expr='icontains')
    dep = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model =Student
        fields = ['age']


      