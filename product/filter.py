import django_filters
from .models import Product

class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    brand = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(lookup_expr='icontains')
    minprice = django_filters.NumberFilter(field_name="price",lookup_expr="gte")
    maxprice = django_filters.NumberFilter(field_name="price",lookup_expr="lte")
    year = django_filters.NumberFilter(field_name='release_date', lookup_expr='year')
    minyear = django_filters.NumberFilter(field_name="release_date",lookup_expr="year__gte")
    maxyear = django_filters.NumberFilter(field_name="release_date",lookup_expr="year__lte")
    class Meta:
        model = Product
        fields = ('brand', 'category','name','price','year')