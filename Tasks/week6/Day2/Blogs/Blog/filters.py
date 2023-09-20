import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='startswith')
    publish_date = django_filters.DateFilter(lookup_expr='gt')
    authorName = django_filters.CharFilter(field_name='author_id__fname', lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['']