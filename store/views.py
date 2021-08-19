from django.db.models import Sum
from rest_framework.response import Response

# Create your views here.
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from store.models import Product
from store.serializers import ProductAddSerializer, ProductViewSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100000


class ProductView(ModelViewSet):
    serializer_class = ProductAddSerializer
    queryset = Product.objects.all()
    pagination_class = StandardResultsSetPagination

    def create(self, *args, **kwargs):
        """p = Штук,kg = Килограмм,l = Литр"""
        return super().create(*args, **kwargs)

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
            serializer = ProductViewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductViewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductViewSerializer(instance)
        return Response(serializer.data)
