from django_filters import rest_framework as filters
from logistic.models import Stock, Product


class StockFilter(filters.FilterSet):
    products = filters.ModelMultipleChoiceFilter(
        field_name='products',
        queryset=Product.objects.all(),
    )

    class Meta:
        model = Stock
        fields = ['products']
