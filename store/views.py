from django.db.models import Sum
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from store.models import Product
from store.serializers import ProductSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100000


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['get'], url_path="total-cost")
    def total_cost(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        total_cost = 0
        for i in queryset:
            total_cost += i.price * i.quantity
        return Response({"total-cost": total_cost})

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
